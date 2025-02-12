# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GenerateSwmmInp
                                 A QGIS plugin
 This plugin generates SWMM Input files
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-09
        copyright            : (C) 2021 by Jannik Schilling
        email                : jannik.schilling@posteo.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Jannik Schilling'
__date__ = '2024-01-31'
__copyright__ = '(C) 2021 by Jannik Schilling'

import numpy as np
import os
import pandas as pd
from qgis.core import (
    QgsProcessingAlgorithm,
    QgsProcessingException,
    QgsProcessingParameterBoolean,
    QgsProcessingParameterCrs,
    QgsProcessingParameterDefinition,
    QgsProcessingParameterEnum,
    QgsProcessingParameterFile,
    QgsProcessingParameterFolderDestination,
    QgsProcessingParameterString
)
from qgis.PyQt.QtCore import QCoreApplication
from .g_s_defaults import (
    curve_cols_dict,
    def_annotation_field,
    def_layer_names_dict,
    def_ogr_driver_dict,
    def_ogr_driver_names,
    def_sections_dict,
    def_sections_geoms_dict,
    def_sections_geoms_list,
    def_stylefile_dict,
    def_tables_dict,
    ImportDataStatus,
    pattern_times
)
from .g_s_read_write_data import (
    create_layer_from_df,
    save_layer_to_file,
    layerlist_to_excel
)
from .g_s_import_helpers import (
    add_layer_on_completion,
    adjust_column_types,
    adjust_line_length,
    build_df_for_section,
    build_df_from_vals_list,
    del_kw_from_list,
    extract_sections_from_text,
    insert_nan_after_kw,
    sect_list_import_handler
)


class ImportInpFile (QgsProcessingAlgorithm):
    """
    generates geodata and tables from a swmm input file
    """
    ADD_Z = 'ADD_Z'
    CREATE_EMPTY = 'CREATE_EMPTY'
    DATA_CRS = 'DATA_CRS'
    GEODATA_DRIVER = 'GEODATA_DRIVER'
    INP_FILE = 'INP_FILE'
    PREFIX = 'PREFIX'
    SAVE_FOLDER = 'SAVE_FOLDER'
    TRANSFORM_CRS = 'TRANSFORM_CRS'

    def initAlgorithm(self, config):
        """
        inputs and outputs of the algorithm
        """
        self.addParameter(
            QgsProcessingParameterFile(
                name=self.INP_FILE,
                description=self.tr('SWMM input file to import'),
                extension='inp'
            )
        )

        self.addParameter(
            QgsProcessingParameterEnum(
                self.GEODATA_DRIVER,
                self.tr("Which format should be used for geodata"),
                def_ogr_driver_names,
                defaultValue=[0]
            )
        )

        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.SAVE_FOLDER,
                self.tr('Folder in which the imported data will be saved.')
            )
        )

        self.addParameter(
            QgsProcessingParameterString(
                self.PREFIX,
                self.tr('Prefix for imported data'),
                optional=True
            )
        )

        self.addParameter(
            QgsProcessingParameterCrs(
                self.DATA_CRS,
                self.tr('CRS of the SWMM input file'),
                defaultValue='epsg:25833'
            )
        )
        
        add_z_coord_param = QgsProcessingParameterBoolean(
                self.ADD_Z,
                self.tr('Add z-coordinates to conduits and nodes'),
                defaultValue=False,
                optional=True
            )
        add_z_coord_param.setFlags(add_z_coord_param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
        self.addParameter(add_z_coord_param)

        empt_param = QgsProcessingParameterBoolean(
            self.CREATE_EMPTY,
            self.tr('Create Empty?'),
            defaultValue=False,
        )
        # Hide the parameter CREATE_EMPTY , because it´s only for the default data tool
        self.addParameter(empt_param)
        empt_param.setFlags(empt_param.flags() | QgsProcessingParameterDefinition.FlagHidden)

        transform_crs = QgsProcessingParameterString(
        self.TRANSFORM_CRS,
        self.tr('Transform to Crs'),
        defaultValue='NA',
        )
        # Hide the parameter CREATE_EMPTY , because it´s only for the default data to
        self.addParameter(transform_crs)
        transform_crs.setFlags(transform_crs.flags() | QgsProcessingParameterDefinition.FlagHidden)

    def name(self):
        return 'ImportInpFile'

    def shortHelpString(self):
        return self.tr(""" The tool imports a swmm inp file and saves the data in a folder selected by the user (temporary folders won´t work!).\n
        You can add a prefix to the files. Try to aviod characters which could cause trouble with file systems (e.g. '.',',','\','/') \n
        The layers (e.g geopackages, shapefiles) are added to the QGIS project.\n
        If the tool fails to load the layers, please check the selected CRS and try again.\n
        """)

    def displayName(self):
        return self.tr('3_ImportInpFile')

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return ''

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ImportInpFile()

    def processAlgorithm(self, parameters, context, feedback):
        pluginPath = os.path.dirname(__file__)
        # transfer of parameters
        folder_save = self.parameterAsString(parameters, self.SAVE_FOLDER, context)
        readfile = self.parameterAsString(parameters, self.INP_FILE, context)
        result_prefix = self.parameterAsString(parameters, self.PREFIX, context)
        crs_result = self.parameterAsCrs(parameters, self.DATA_CRS, context)
        crs_result = str(crs_result.authid())
        geodata_driver_num = self.parameterAsEnum(parameters, self.GEODATA_DRIVER, context)
        geodata_driver_name = def_ogr_driver_names[geodata_driver_num]
        geodata_driver_extension = def_ogr_driver_dict[geodata_driver_name]
        create_empty = self.parameterAsBoolean(parameters, self.CREATE_EMPTY, context)
        add_z_bool = self.parameterAsBoolean(parameters, self.ADD_Z, context)
        transform_crs_string = self.parameterAsString(parameters, self.TRANSFORM_CRS, context)

        # parameters shared by many functions
        import_parameters_dict = {
            'add_z_bool': add_z_bool,
            'create_empty': create_empty,
            'context': context,
            'crs_result': crs_result,
            'geodata_driver_num': geodata_driver_num,
            'geodata_driver_name': geodata_driver_name,
            'geodata_driver_extension': geodata_driver_extension,
            'folder_save': folder_save,
            'result_prefix': result_prefix,
            'pluginPath': pluginPath,
            'transform_crs_string': transform_crs_string
        }
        
        # check if the selected folder is temporary
        if parameters['SAVE_FOLDER'] == 'TEMPORARY_OUTPUT':
            raise QgsProcessingException(
                'The data set needs to be saved in a directory '
                + '(temporary folders won´t work). Please select a directoy'
            )
        else:
            # check if files are already in folder
            for section_name in def_layer_names_dict.keys():
                layer_name = def_layer_names_dict[section_name]
                if result_prefix != '':
                    layer_name = (
                        str(import_parameters_dict['result_prefix'])
                        +'_'
                        + layer_name
                    )
                geodata_driver_name = def_ogr_driver_names[geodata_driver_num]
                geodata_driver_extension = def_ogr_driver_dict[geodata_driver_name]
                fname = os.path.join(
                    folder_save, 
                    layer_name+ '.' +geodata_driver_extension
                )
                if os.path.isfile(fname):
                    raise QgsProcessingException('File '+fname
                        + ' already exists. Please choose another folder.')
            for section_name in def_tables_dict.keys():
                save_name = def_tables_dict[section_name]['filename']
                if result_prefix != '':
                    save_name = str(result_prefix)+'_'+save_name
                ext = '.xlsx' # default setting
                save_name_ext = save_name + ext
                fname = os.path.join(folder_save, save_name_ext)
                if os.path.isfile(fname):
                    raise QgsProcessingException('File '+fname
                        + ' already exists. Please choose another folder.')


        # reading input text file
        feedback.setProgressText(self.tr('reading inp ...'))
        feedback.setProgress(3)
        encodings = ['utf-8', 'windows-1250', 'windows-1252']  # add more
        for e in encodings:
            try:
                with open(readfile, 'r', encoding=e) as f:
                    inp_text = f.readlines()
            except UnicodeDecodeError:
                feedback.setProgressText('got unicode error with %s , trying different encoding' % e)
            else:
                feedback.setProgressText('opening the file with encoding:  %s ' % e)
                break
        
        # delete unused lines
        inp_text = [x for x in inp_text if x != '\n']
        inp_text = [x for x in inp_text if x != '\r']
        inp_text = [x for x in inp_text if not x.startswith(';;')]
        inp_text = [x.replace('\n', '') for x in inp_text]
        inp_text = [x.strip() for x in inp_text]

        # SWMM sections in the text file
        inp_text_sections = [i for i in inp_text if i.startswith('[') and i.endswith(']')]
        pos_start_list = [inp_text.index(sect) for sect in inp_text_sections]
        pos_end_list = pos_start_list[1:]+[len(inp_text)]
        
        # make a dict of sections to extract
        dict_search = {
            s[1:-1].upper(): [
                pos_start_list[i],
                pos_end_list[i]
            ] for i, s in enumerate(inp_text_sections) if s[1:-1].upper() in def_sections_dict.keys()
        }
        
        # sections which are not available
        unknown_sections = [s for s in inp_text_sections if not s[1:-1].upper() in def_sections_dict.keys()]
        if len(unknown_sections) > 0:
            feedback.pushWarning(
                            'Warning: unknown sections in input file: '
                            + (' ,').join(unknown_sections)
                            + 'These sections will be ignored'
                        )

        # dict for raw values for every section
        dict_all_vals = {
            k: extract_sections_from_text(
                inp_text,
                dict_search[k],
                k
            ) for k in dict_search.keys()
        }  
        
        # sections which will be converted into tables
        # --------------------------------------------
        dict_res_table = {}
        
        # options section
        if 'OPTIONS' in dict_all_vals.keys():
            section_name = 'OPTIONS'
            feedback.setProgressText('Preparing section \"'+section_name+'\"')
            feedback.setProgress(5)
            from .g_s_options import convert_options_format_for_import
            df_options = build_df_for_section(
                'OPTIONS',
                dict_all_vals
            )
            df_options_converted = convert_options_format_for_import(
                df_options,
                import_parameters_dict,
                feedback
            )
            if import_parameters_dict['add_z_bool']:
                if not 'LINK_OFFSETS' in df_options_converted['Option'].tolist():
                    import_parameters_dict['link_offsets'] = 'elevation'  # assume absolute elevation if no info
                    feedback.pushWarning(
                        'OPTIONS: no value for LINK_OFFSETS in inp file. LINK_OFFSETS = ELEVATION is assumed for z-coordinates'
                    )
                else:
                    link_offset_value = df_options_converted.loc[
                        df_options_converted['Option'] == 'LINK_OFFSETS',
                        'Value'
                    ].tolist()[0]
                    if link_offset_value == 'DEPTH':
                        import_parameters_dict['link_offsets'] = 'depth'  # relative
                    elif link_offset_value == 'ELEVATION':
                        import_parameters_dict['link_offsets'] = 'elevation'  # absolute
                    else:
                        import_parameters_dict['link_offsets'] = 'elevation'  # absolute
                        feedback.pushWarning(
                            'OPTIONS: value \"'
                            + link_offset_value
                            + '\" for LINK_OFFSETS in inp file is not valid. LINK_OFFSETS = ELEVATION is assumed for z-coordinates'
                        )
            dict_res_table['OPTIONS'] = {
                'OPTIONS': df_options_converted
            }
            

        # inflows section
        section_name = 'INFLOWS'
        feedback.setProgressText('Preparing section \"'+section_name+'\"')
        feedback.setProgress(8)
        if 'INFLOWS' in dict_all_vals.keys():
            df_inflows = build_df_for_section(
                'INFLOWS',
                dict_all_vals
            )
        else:
            df_inflows = build_df_from_vals_list(
                [],
                def_sections_dict['INFLOWS']
            )
        if 'DWF' in dict_all_vals.keys():
            df_dry_weather = build_df_for_section(
                'DWF',
                dict_all_vals
            )
        else:
            df_dry_weather = build_df_from_vals_list(
                [],
                def_sections_dict['DWF']
            )
        if 'HYDROGRAPHS' in dict_all_vals.keys():
            from .g_s_nodes import get_hydrogrphs
            df_hydrographs_raw = build_df_for_section(
                'HYDROGRAPHS',
                dict_all_vals
            )
            hg_name_list = np.unique(df_hydrographs_raw['Name'])
            df_hydrographs = pd.DataFrame()
            for hg_name in hg_name_list:
                df_hydrographs = pd.concat([df_hydrographs, get_hydrogrphs(hg_name, df_hydrographs_raw)])
            df_hydrographs = df_hydrographs.reset_index(drop=True)
        else:
            df_hydrographs = build_df_from_vals_list(
                [],
                list(def_tables_dict['INFLOWS']['tables']['Hydrographs'].keys())
            )
        if 'RDII' in dict_all_vals.keys():
            df_rdii = build_df_for_section(
                'RDII',
                dict_all_vals
            )
        else:
            df_rdii = build_df_from_vals_list(
                [],
                def_sections_dict['RDII']
            )
        dict_inflows = {
            'Direct': df_inflows,
            'Dry_Weather': df_dry_weather,
            'Hydrographs': df_hydrographs,
            'RDII': df_rdii
        }
        dict_res_table['INFLOWS'] = dict_inflows
        
        pattern_types = list(def_tables_dict['PATTERNS']['tables'].keys())
        pattern_cols = {k: list(v.keys())for k, v in def_tables_dict['PATTERNS']['tables'].items()}

        if 'PATTERNS' in dict_all_vals.keys():
            section_name = 'PATTERNS'
            feedback.setProgressText('Preparing section \"'+section_name+'\"')
            feedback.setProgress(12)
            all_patterns = build_df_for_section('PATTERNS', dict_all_vals)
            if len(all_patterns) == 0:
                all_patterns = dict()
            else:
                occuring_patterns_types = all_patterns.loc[all_patterns[1].isin(pattern_types), [0, 1]].set_index(0)
                occuring_patterns_types.columns = ["PatternType"]
                all_patterns = all_patterns.fillna(np.nan)
                all_patterns = all_patterns.replace({
                    'HOURLY': np.nan,
                    'DAILY': np.nan,
                    'MONTHLY': np.nan,
                    'WEEKEND': np.nan
                })

                def adjust_patterns_df(pattern_row):
                    """
                    reorders a list of the patterns section for the input file
                    :param list pattern_row
                    :return: pd.DataFrame
                    """
                    pattern_adjusted = [[pattern_row[0], i] for i in pattern_row[1:] if pd.notna(i)]
                    return (pd.DataFrame(pattern_adjusted, columns=['Name', 'Factor']))

                all_patterns = pd.concat([adjust_patterns_df(all_patterns.loc[i, :]) for i in all_patterns.index])
                all_patterns = all_patterns.join(
                    occuring_patterns_types,
                    on='Name'
                )
                all_patterns = {k: v.iloc[:, :-1] for k, v in all_patterns.groupby("PatternType")}
        else:
            all_patterns = dict()

        def add_pattern_timesteps(pattern_type):
            """
            adds time strings from the pattern_times dict
            :param str pattern_row
            :return: list
            """
            count_patterns = int(len(all_patterns[pattern_type])/len(pattern_times[pattern_type]))
            new_col = pattern_times[pattern_type]*count_patterns
            return new_col
        for pattern_type in pattern_cols.keys():
            if pattern_type in all_patterns.keys():
                all_patterns[pattern_type]['Time'] = add_pattern_timesteps(pattern_type)
                all_patterns[pattern_type] = all_patterns[pattern_type][['Name', 'Time', 'Factor']]
                if pattern_type == 'DAILY':
                    all_patterns[pattern_type] = all_patterns[pattern_type].rename({'Time': 'Day'})
                if pattern_type == 'MONTHLY':
                    all_patterns[pattern_type] = all_patterns[pattern_type].rename({'Time': 'Month'})
                all_patterns[pattern_type]['Factor'] = [float(x) for x in all_patterns[pattern_type]['Factor']]
                all_patterns[pattern_type].columns = pattern_cols[pattern_type]
            else:
                all_patterns[pattern_type] = build_df_from_vals_list([], pattern_cols[pattern_type])
        dict_res_table['PATTERNS'] = all_patterns

        # curves section
        if 'CURVES' in dict_all_vals.keys():
            section_name = 'CURVES'
            feedback.setProgressText('Preparing section \"'+section_name+'\"')
            feedback.setProgress(16)
            curve_type_dict = {x[0]: x[1] for x in dict_all_vals['CURVES']['data'] if x[1].capitalize() in curve_cols_dict.keys()}
            occuring_curve_types = list(set(curve_type_dict.values()))
            all_curves = [del_kw_from_list(x, occuring_curve_types, 1) for x in dict_all_vals['CURVES']['data'].copy()]
            all_curves = build_df_from_vals_list(
                all_curves,
                def_sections_dict['CURVES']
            )
            all_curves['CurveType'] = [curve_type_dict[i].capitalize() for i in all_curves['Name']]  # capitalize as in curve_cols_dict
            all_curves['XVal'] = [float(x) for x in all_curves['XVal']]
            all_curves['YVal'] = [float(x) for x in all_curves['YVal']]
            all_curves = {k: v[['Name', 'XVal', 'YVal']] for k, v in all_curves.groupby('CurveType')}
        else:
            all_curves = dict()
        for curve_type in curve_cols_dict.keys():
            if curve_type in all_curves.keys():
                all_curves[curve_type].columns = curve_cols_dict[curve_type]
            else:
                all_curves[curve_type] = build_df_from_vals_list([], curve_cols_dict[curve_type])
        dict_res_table['CURVES'] = all_curves

        # quality section
        feedback.setProgressText('Preparing QUALITY parameters')
        feedback.setProgress(20)
        quality_cols_dict = {
            k: def_sections_dict[k] for k in [
                'POLLUTANTS',
                'LANDUSES',
                'COVERAGES',
                'LOADINGS',
                'BUILDUP',
                'WASHOFF'
            ]
        }
        all_quality = {k: build_df_for_section(k, dict_all_vals) for k in quality_cols_dict.keys()}
        if len(all_quality['BUILDUP']) == 0:  # fill with np.nan in order to facilitate join below
            if len(all_quality['LANDUSES']) > 0:
                landuse_names = all_quality['LANDUSES']['Name']
                landuse_count = len(landuse_names)
                all_quality['BUILDUP'].loc[0:landuse_count, :] = np.nan
                all_quality['BUILDUP']['Name'] = landuse_names
        landuses = all_quality['BUILDUP'].copy().join(all_quality['LANDUSES'].copy().set_index('Name'), on='Name')
        col_names = all_quality['LANDUSES'].columns.tolist()
        col_names.extend(all_quality['BUILDUP'].columns.tolist()[1:])
        landuses = landuses[col_names]
        landuses['join_name'] = landuses['Name']+landuses['Pollutant']
        all_quality['WASHOFF']['join_name'] = all_quality['WASHOFF']['Name'] + all_quality['WASHOFF']['Pollutant']
        all_quality['WASHOFF'] = all_quality['WASHOFF'].drop(columns=['Name', 'Pollutant'])
        landuses = landuses.join(all_quality['WASHOFF'].set_index('join_name'), on='join_name')
        landuses = landuses.drop(columns=['join_name'])
        all_quality['LANDUSES'] = landuses
        del all_quality['BUILDUP']
        del all_quality['WASHOFF']
        all_quality = {
            k: adjust_column_types(
                v, def_tables_dict['QUALITY']['tables'][k]
            ) for k, v in all_quality.items()
        }
        dict_res_table['QUALITY'] = all_quality

        # timeseries section
        ts_cols_dict = def_tables_dict['TIMESERIES']['tables']['TIMESERIES']
        if 'TIMESERIES' in dict_all_vals.keys():
            all_time_series = [adjust_line_length(x, 1, 4) for x in dict_all_vals['TIMESERIES']['data'].copy()]
            # for external File
            all_time_series = [insert_nan_after_kw(x, 2, 'FILE', [3, 4]) for x in all_time_series]
            all_time_series = [del_kw_from_list(x, 'FILE', 2) for x in all_time_series]
            all_time_series = build_df_from_vals_list(
                all_time_series,
                def_sections_dict['TIMESERIES']
            )
        else:
            all_time_series = build_df_from_vals_list([], list(ts_cols_dict.keys()))
        all_time_series = adjust_column_types(all_time_series, ts_cols_dict)
        dict_res_table['TIMESERIES'] = {'TIMESERIES': all_time_series}

        # streets and inlets section
        if 'STREETS' in dict_all_vals.keys() or 'INLETS' in dict_all_vals.keys():
            section_name = 'STREETS'
            feedback.setProgressText('Preparing section \"'+section_name+'\"')
            feedback.setProgress(25)
            street_data = {}
            street_data['STREETS'] = build_df_for_section('STREETS', dict_all_vals)
            if 'INLETS' in dict_all_vals.keys():
                from .g_s_links import get_inlet_from_inp
                inl_list = [get_inlet_from_inp(inl_line) for inl_line in dict_all_vals['INLETS']['data']]
                street_data['INLETS'] = build_df_from_vals_list(inl_list, def_sections_dict['INLETS'])
            else:
                street_data['INLETS'] = build_df_for_section('INLETS', dict_all_vals)
            street_data['INLET_USAGE'] = build_df_for_section('INLET_USAGE', dict_all_vals)
            dict_res_table['STREETS'] = street_data

        # transects in hec2 format
        if 'TRANSECTS' in dict_all_vals.keys():
            feedback.setProgress(1)
            transects_columns = [
                'TransectName',
                'RoughnessLeftBank',
                'RoughnessRightBank',
                'RoughnessChannel',
                'BankStationLeft',
                'BankStationRight',
                'ModifierMeander',
                'ModifierStations',
                'ModifierElevations'
            ]
            section_name = 'TRANSECTS'
            feedback.setProgressText('Preparing section \"'+section_name+'\"')
            transects_list = dict_all_vals['TRANSECTS']['data'].copy()
            tr_startp = [i for i, x in enumerate(transects_list) if x[0] == 'NC']
            n_trans = len(tr_startp)
            tr_endp = tr_startp[1:]+[len(transects_list)]

            def get_transects_data2(tr_i):
                tr_roughness = [float(x) for x in tr_i[0][1:]]
                tr_name = tr_i[1][1]
                tr_count = tr_i[1][2]
                tr_bankstat_left = float(tr_i[1][3])
                tr_bankstat_right = float(tr_i[1][4])
                tr_modifier = [float(x) for x in tr_i[1][7:10]]
                tr_data = [tr_name]+tr_roughness+[tr_bankstat_left]+[tr_bankstat_right]+tr_modifier
                tr_values = [del_kw_from_list(x, 'GR', 0) for x in tr_i[2:]]
                tr_values = [x for sublist in tr_values for x in sublist]
                tr_values_splitted = [[
                    tr_name,
                    float(tr_values[x*2]),   # split into list of lists of len 2
                    float(tr_values[(x*2)+1])
                ] for x in range(int(tr_count))]
                return tr_values_splitted, tr_data
                
            all_tr_vals = []
            all_tr_dats = []
            for i, x in enumerate(zip(tr_startp, tr_endp)):
                if feedback.isCanceled():
                    break
                val, dat = get_transects_data2(transects_list[x[0]:x[1]])
                all_tr_vals = all_tr_vals + val
                all_tr_dats = all_tr_dats + [dat]
                feedback.setProgress(((i+1)/n_trans)*90)

            all_tr_vals_df = build_df_from_vals_list(
                all_tr_vals,
                ['TransectName', 'Elevation', 'Station']
            )
            feedback.setProgress(92)
            all_tr_vals_df = all_tr_vals_df[[
                'TransectName',
                'Station',
                'Elevation'
            ]]  # order of columns according to swmm interface
            feedback.setProgress(93)
            all_tr_dats_df = build_df_from_vals_list(all_tr_dats, transects_columns)
            feedback.setProgress(94)
            all_tr_dats_df = all_tr_dats_df[[
                'TransectName',
                'RoughnessLeftBank',
                'RoughnessRightBank',
                'RoughnessChannel',
                'BankStationLeft',
                'BankStationRight',
                'ModifierStations',
                'ModifierElevations',
                'ModifierMeander'
            ]]  # order of columns according to swmm interface
            transects_dict = {
                'Data': all_tr_dats_df,
                'XSections': all_tr_vals_df
            }
            feedback.setProgress(95)
            dict_res_table['TRANSECTS'] = transects_dict
            feedback.setProgress(100)


        # writing tables: 
        feedback.setProgressText('Writing tables ...')
        n_itms = len(dict_res_table)
        for i, it in enumerate(dict_res_table.items()):
            if feedback.isCanceled():
                break
            layer_list = []
            section_name = it[0]
            for sheet_name, df in it[1].items():
                data_dict = {
                    'data': df,
                    'layer_name': sheet_name
                }
                created_layer = create_layer_from_df(
                    data_dict,
                    section_name,
                    feedback=feedback,
                    **import_parameters_dict
                )
                layer_list = layer_list+[created_layer]
            layerlist_to_excel(
                layer_list,
                section_name,
                feedback = feedback,
                **import_parameters_dict
            )
            del layer_list

        # sections with geometries, which will be added as layers
        #------------------------------
        # prepare
        feedback.setProgress(0)
        for section_name in def_sections_geoms_list:  # the list is used to keep the order
            if feedback.isCanceled():
                break
            if section_name in dict_all_vals.keys():
                sect_list_import_handler(
                    section_name,
                    dict_all_vals,
                    'geodata',
                    feedback,
                    import_parameters_dict
                )

        # make layers
        n_itms = len(def_sections_geoms_dict.keys())
        for n, section_name in enumerate(def_sections_geoms_dict.keys()):
            if feedback.isCanceled():
                break
            if section_name in dict_all_vals.keys():
                if dict_all_vals[section_name]['status'] == ImportDataStatus.GEOM_READY:
                    data_dict = dict_all_vals[section_name]
                    if result_prefix != '':
                        layer_name = (
                            str(import_parameters_dict['result_prefix'])
                            +'_'
                            + def_layer_names_dict[section_name]
                        )
                    else:
                        layer_name = def_layer_names_dict[section_name]
                    data_dict['layer_name'] = layer_name
                    created_layer = create_layer_from_df(
                        data_dict,
                        section_name,
                        feedback=feedback,
                        custom_fields=def_annotation_field,
                        **import_parameters_dict
                    )
                    save_layer_to_file(
                        created_layer,
                        layer_name,
                        **import_parameters_dict
                    )
                    dict_all_vals[section_name]['status'] = ImportDataStatus.FILE_READY
            feedback.setProgress((n+1)/n_itms*100)

        # add layers to canvas
        feedback.setProgressText(
            self.tr('Adding layers to canvas')
        )
        n_itms = len(def_sections_geoms_dict.keys())
        for n, section_name in enumerate(def_sections_geoms_dict.keys()):
            if feedback.isCanceled():
                break
            if section_name in dict_all_vals.keys():
                if dict_all_vals[section_name]['status'] == ImportDataStatus.FILE_READY:
                    data_dict = dict_all_vals[section_name]
                    add_layer_on_completion(
                        data_dict['layer_name'],
                        def_stylefile_dict[section_name],
                        **import_parameters_dict
                    )
                dict_all_vals[section_name]['status'] == ImportDataStatus.DONE

        feedback.setProgressText(
            self.tr('all data was saved in '+str(folder_save))
        )
        return {}

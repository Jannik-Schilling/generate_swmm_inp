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
__date__ = '2024-02-17'
__copyright__ = '(C) 2021 by Jannik Schilling'


# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import pandas as pd
import numpy as np
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingParameterBoolean,
    QgsProcessingParameterDefinition,
    QgsProcessingException,
    QgsProcessingParameterFile,
    QgsProcessingParameterFileDestination,
    QgsProcessingParameterVectorLayer
)
# imports from own scripts
from .g_s_defaults import (
    def_qgis_fields_dict,
    def_sections_geoms_dict,
    def_tables_dict,
    curve_cols_dict,
    def_sections_dict
)
from .g_s_export_helpers import (
    check_columns,
    check_deprecated,
    data_preparation,
    get_annotations_from_raw_df,
    get_coords_from_geometry,
    use_z_if_available
)
from .g_s_links import del_first_last_vt
from .g_s_read_write_data import (
    read_data_direct
)


class GenerateSwmmInpFile(QgsProcessingAlgorithm):
    """
    generates a swmm input file from geodata and tables
    """
    QGIS_OUT_INP_FILE = 'QGIS_OUT_INP_FILE'
    FILE_RAINGAGES = 'FILE_RAINGAGES'
    FILE_CONDUITS = 'FILE_CONDUITS'
    FILE_JUNCTIONS = 'FILE_JUNCTIONS'
    FILE_DIVIDERS = 'FILE_DIVIDERS'
    FILE_ORIFICES = 'FILE_ORIFICES'
    FILE_OUTFALLS = 'FILE_OUTFALLS'
    FILE_OUTLETS = 'FILE_OUTLETS'
    FILE_STORAGES = 'FILE_STORAGES'
    FILE_PUMPS = 'FILE_PUMPS'
    FILE_SUBCATCHMENTS = 'FILE_SUBCATCHMENTS'
    FILE_WEIRS = 'FILE_WEIRS'
    FILE_CURVES = 'FILE_CURVES'
    FILE_PATTERNS = 'FILE_PATTERNS'
    FILE_OPTIONS = 'FILE_OPTIONS'
    FILE_TIMESERIES = 'FILE_TIMESERIES'
    FILE_INFLOWS = 'FILE_INFLOWS'
    FILE_QUALITY = 'FILE_QUALITY'
    FILE_TRANSECTS = 'FILE_TRANSECTS'
    FILE_STREETS = 'FILE_STREETS'
    USE_Z_VALS = 'USE_Z_VALS'

    def initAlgorithm(self, config):
        """
        inputs and output of the algorithm
        """
        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.QGIS_OUT_INP_FILE,
                self.tr('Where should the inp file be saved?'),
                'INP files (*.inp)',
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_RAINGAGES,
                self.tr('Rain gages Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_JUNCTIONS,
                self.tr('Junctions Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_CONDUITS,
                self.tr('Conduits Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_SUBCATCHMENTS,
                self.tr('Subcatchments Layer'),
                types=[QgsProcessing.SourceType.TypeVectorAnyGeometry],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_STORAGES,
                self.tr('Storages Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_OUTFALLS,
                self.tr('Outfalls Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_DIVIDERS,
                self.tr('Dividers Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_PUMPS,
                self.tr('Pumps Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_WEIRS,
                self.tr('Weirs Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_ORIFICES,
                self.tr('Orifices Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_OUTLETS,
                self.tr('Outlets Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_OPTIONS,
                self.tr('Options table file'),
                QgsProcessingParameterFile.File,
                optional=True,
                fileFilter='Tables (*.xlsx *.xls *.odf)'
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_CURVES,
                self.tr('Curves table file'),
                QgsProcessingParameterFile.File,
                optional=True,
                fileFilter='Tables (*.xlsx *.xls *.odf)'
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_PATTERNS,
                self.tr('Patterns table file'),
                QgsProcessingParameterFile.File,
                optional=True,
                fileFilter='Tables (*.xlsx *.xls *.odf)'
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_TIMESERIES,
                self.tr('Timeseries table file'),
                QgsProcessingParameterFile.File,
                optional=True,
                fileFilter='Tables (*.xlsx *.xls *.odf)'
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_INFLOWS,
                self.tr('Inflows table file'),
                QgsProcessingParameterFile.File,
                optional=True,
                fileFilter='Tables (*.xlsx *.xls *.odf)'
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_QUALITY,
                self.tr('Quality table file'),
                QgsProcessingParameterFile.File,
                optional=True,
                fileFilter='Tables (*.xlsx *.xls *.odf)'
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_TRANSECTS,
                self.tr('Transects table file'),
                QgsProcessingParameterFile.File,
                optional=True,
                fileFilter='Tables (*.xlsx *.xls *.odf)'
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_STREETS,
                self.tr('Streets and Inlets table file'),
                QgsProcessingParameterFile.File,
                optional=True,
                fileFilter='Tables (*.xlsx *.xls *.odf)'
            )
        )

        use_z_vals_param = QgsProcessingParameterBoolean(
            self.USE_Z_VALS,
            self.tr(
                'Use z-coordinates for conduits and nodes instead'
                +' of \"Elevation\"/\"InOffset\"/\"OutOffset\" in '
                +'the attribute tables'    
            ),
            defaultValue=False,
            optional=True
        )
        use_z_vals_param.setFlags(use_z_vals_param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
        self.addParameter(use_z_vals_param)

    def processAlgorithm(self, parameters, context, feedback):
        """
        main process algorithm of this tool
        """
        # input file name and path"
        inp_file_path = self.parameterAsString(parameters, self.QGIS_OUT_INP_FILE, context)
        inp_file_name = os.path.basename(inp_file_path)
        project_dir = os.path.dirname(inp_file_path)


        
        export_params = {
            'all_nodes': list(),
            'all_subcatchments': list(),
            'feedback': feedback,
            'link_offsets': 'ELEVATION',  # assumes absolute elevation data, if parameter not in options file
            'main_infiltration_method': None,
            'use_z_bool': self.parameterAsBoolean(parameters, self.USE_Z_VALS, context),  # advanced parameter for z_values
        }

        # initializing the input dictionary
        """
        inp_dict = {
            SECTION: {
                'data': pd.df,
                'annotations': {
                    'object_name1': 'annotation_string'
                    'object_name2': 'annotation_string'
                }
            }
        }
        """
        inp_dict = dict()
        inp_dict['TITLE'] = {'data': pd.DataFrame(['test'])}
        inp_dict['XSECTIONS'] = {
            'data': pd.DataFrame(),
            'annotations': {}
        } 
        inp_dict['COORDINATES'] = {'data': pd.DataFrame()}
        inp_dict['VERTICES'] = {'data': dict()}


        # putting together all dita in a dict
        export_data = {
            # layers
            'RAINGAGES': {'file': self.parameterAsVectorLayer(parameters, self.FILE_RAINGAGES, context)},
            'OUTFALLS': {'file': self.parameterAsVectorLayer(parameters, self.FILE_OUTFALLS, context)},
            'STORAGE': {'file': self.parameterAsVectorLayer(parameters, self.FILE_STORAGES, context)},
            'SUBCATCHMENTS': {'file': self.parameterAsVectorLayer(parameters, self.FILE_SUBCATCHMENTS, context)},
            'CONDUITS': {'file': self.parameterAsVectorLayer(parameters, self.FILE_CONDUITS, context)},
            'JUNCTIONS': {'file': self.parameterAsVectorLayer(parameters, self.FILE_JUNCTIONS, context)},
            'PUMPS': {'file': self.parameterAsVectorLayer(parameters, self.FILE_PUMPS, context)},
            'WEIRS': {'file': self.parameterAsVectorLayer(parameters, self.FILE_WEIRS, context)},
            'ORIFICES': {'file': self.parameterAsVectorLayer(parameters, self.FILE_ORIFICES, context)},
            'OUTLETS': {'file': self.parameterAsVectorLayer(parameters, self.FILE_OUTLETS, context)},
            'DIVIDERS': {'file': self.parameterAsVectorLayer(parameters, self.FILE_DIVIDERS, context)},
            # tables
            'OPTIONS': {'file': self.parameterAsString(parameters, self.FILE_OPTIONS, context)},
            'INFLOWS': {'file': self.parameterAsString(parameters, self.FILE_INFLOWS, context)},
            'PATTERNS': {'file': self.parameterAsString(parameters, self.FILE_PATTERNS, context)},
            'CURVES': {'file': self.parameterAsString(parameters, self.FILE_CURVES, context)},
            'QUALITY': {'file': self.parameterAsString(parameters, self.FILE_QUALITY, context)},
            'TIMESERIES': {'file': self.parameterAsString(parameters, self.FILE_TIMESERIES, context)},
            'TRANSECTS': {'file': self.parameterAsString(parameters, self.FILE_TRANSECTS, context)},
            'STREETS': {'file': self.parameterAsString(parameters, self.FILE_STREETS, context)},
        }
        export_data = {k: v for k, v in export_data.items() if v['file'] is not None}
        export_data = {k: v for k, v in export_data.items() if v['file'] != ''}
        
        # adding data type information
        for k in export_data.keys():
            if k in def_sections_geoms_dict.keys():
                export_data[k]['d_type'] = 'layer'
            elif k in def_tables_dict.keys():
                export_data[k]['d_type'] = 'table'
            else:
                #unknown data type
                raise QgsProcessingException(
                    'Unknown file type for file ' 
                    + k
                )
        feedback.setProgressText(self.tr('done \n'))


        # check crs for layer
        feedback.setProgressText('Checking CRS of layers...')
        raw_layers_crs_list = [
            v['file'].crs().authid() for v in export_data.values() if v['d_type'] == 'layer'
        ]
        unique_crs = np.unique(raw_layers_crs_list)
        if len(unique_crs) > 1:
            feedback.pushWarning(
                'Warning: different CRS in the selected layers.'
                + 'This may lead to unexpected locations in SWMM'
            )
        feedback.setProgressText(self.tr('done \n'))


        # store pandas dataframes for each layer     
        feedback.setProgressText('Reading layers and tables...')   
        read_data_direct(export_data, feedback = feedback)
        feedback.setProgressText(self.tr('done \n'))



        feedback.setProgressText(self.tr('preparing data for input file:'))
        # main handler
        def data_export_handler(
            data_name,
            export_data,
            inp_dict,
            export_params
        ):
            feedback.setProgressText(self.tr(data_name+'...'))
            data_entry = export_data[data_name]['data']
            data_type = export_data[data_name]['d_type']
            f_name = export_data[data_name]['file']
            # check columns
            if data_type == 'table':
                for sheet_name in data_entry.keys():
                    cols_to_check = list(def_tables_dict[data_name]['tables'][sheet_name].keys())
                    check_columns(
                        f_name,
                        cols_to_check,
                        data_entry[sheet_name].keys()
                    )
            else:
                if data_name != 'STORAGE':  # check columns is performed within get_storages_from_geodata for different storage types
                    cols_to_check = list(def_qgis_fields_dict[data_name].keys())
                    check_columns(
                        f_name,
                        cols_to_check,
                        data_entry.keys()
                    )

            # data preparation
            processed_data_dict = data_preparation(
                data_name,
                data_entry,
                export_params
            )

            # geometry
            if data_type == 'layer':
                sections_coords = get_coords_from_geometry(data_entry)
                if data_name in [
                    'RAINGAGES',
                    'SUBCATCHMENTS',
                    'PUMPS',
                    'WEIRS',
                    'OUTLETS',
                    'ORIFICES'
                ]:  # skip for these
                    if data_name == 'RAINGAGES':
                        # rename coordinates
                        sections_coords['SYMBOLS'] = sections_coords.pop('COORDINATES')
                        if 'Z_Coord' in sections_coords['SYMBOLS']['data'].keys():
                            sections_coords['SYMBOLS']['data'].drop("Z_Coord", axis=1, inplace=True)
                    inp_dict.update(sections_coords)  # write to inp dict
                        
                else:
                    link_offsets = export_params['link_offsets']
                    if (
                        link_offsets == 'depth' and
                        list(sections_coords.keys())[0] == 'VERTICES' and
                        'COORDINATES' in inp_dict.keys()
                    ):
                        coords_nodes = inp_dict['COORDINATES']['data']
                    else:
                        coords_nodes = None
                    # use z coordinate if desired
                    processed_data_dict[data_name]['data'] =  use_z_if_available(
                        processed_data_dict[data_name]['data'],
                        sections_coords,
                        export_params['use_z_bool'],
                        feedback,
                        export_params['link_offsets'],
                        layer_name=f_name,
                        coords_nodes=coords_nodes,
                    )
                
                # write geometry info to inp dict
                if def_sections_geoms_dict[data_name] == 'LineString':
                    vertices_before = sections_coords['VERTICES']['data']
                    vertices_adjusted = {k: del_first_last_vt(v) for k, v in vertices_before.items() if len(v) > 2}
                    inp_dict['VERTICES']['data'].update(vertices_adjusted)
                elif (
                    def_sections_geoms_dict[data_name] == 'Point' and
                    data_name != 'RAINGAGES'
                ):
                    # add nodes names to all_nodes list
                    new_nodes = processed_data_dict[data_name]['data']['Name'].tolist()
                    export_params['all_nodes'] = export_params['all_nodes']+new_nodes
                    # update coordinates
                    inp_dict['COORDINATES']['data'] = pd.concat(
                        [
                            inp_dict['COORDINATES']['data'],
                            sections_coords['COORDINATES']['data']
                        ],
                        ignore_index = True
                    )
                    inp_dict['COORDINATES']['data'] = inp_dict['COORDINATES']['data'].reset_index(drop=True)
                else:
                    pass  # subcatchments and raingages are already written

            # annotations
            if data_name in [
                'OPTIONS',
                'PATTERNS',
                'CURVES',
                'QUALITY',
                'TIMESERIES',
                'STREETS',
                'INFLOWS',
                'TRANSECTS'
            ]:  # ToDo: Tables annotations
                annotations_df = None
            else:
                annotations_df = get_annotations_from_raw_df(data_entry.copy())

            # write to inp dict
            if 'XSECTIONS' in processed_data_dict:
                xsections_data = processed_data_dict.pop('XSECTIONS')
                inp_dict['XSECTIONS']['data'] = pd.concat(
                    [
                        inp_dict['XSECTIONS']['data'],
                        xsections_data['data']
                    ],
                    ignore_index = True
                )
                inp_dict['XSECTIONS']['data'] = inp_dict['XSECTIONS']['data'].reset_index(drop=True)
            inp_dict.update(processed_data_dict)
            if annotations_df is not None:
                # das ggf. für jede subgruppe
                inp_dict[data_name]['annotations'] = annotations_df



        # check deprecated data
        for data_name in [
            'CONDUITS',
            'ORIFICES',
        ]:
            if data_name in export_data:
                export_data[data_name]['data'] = check_deprecated(
                    swmm_data_file=export_data[data_name]['file'],
                    swmm_section=data_name,
                    df=export_data[data_name]['data'],
                    cols_deprecated={'Shape': 'XsectShape'},
                    feedback=feedback
                )


        # run export handler
        for data_name in [
            'OPTIONS',  #  first, needed for link_offsets
            'SUBCATCHMENTS',
            'JUNCTIONS',  # second: nodes for coordinates section
            'OUTFALLS',
            'STORAGE',
            'DIVIDERS',
            'RAINGAGES',
            'CONDUITS',  # third: links
            'PUMPS',
            'WEIRS',
            'OUTLETS',
            'ORIFICES',
            'INFLOWS',  # fourth: tables for additional parameters / information
            'PATTERNS',
            'CURVES',
            'QUALITY',
            'TIMESERIES',
            'TRANSECTS',
            'STREETS'
        ]:
            if data_name == 'INFLOWS':
                if len(export_params['all_nodes']) == 0:
                    continue
            if data_name == 'TRANSECTS':
                if not (('CONDUITS' in inp_dict) or ('WEIRS' in inp_dict)):
                    continue
            if data_name in export_data.keys():
                data_export_handler(
                    data_name,
                    export_data,
                    inp_dict,
                    export_params
                )

        # delete sections with empty data
        inp_dict = {k: v for k, v in inp_dict.items() if len(v['data'])>0}

        feedback.setProgressText(self.tr('done \n'))


        # writing inp file
        feedback.setProgressText(self.tr('Creating inp file:'))
        inp_dict = {k: v for k, v in inp_dict.items() if len(v['data']) > 0}  # remove empty sections
        from .g_s_write_inp import write_inp
        write_inp(inp_file_name,
                  project_dir,
                  inp_dict,
                  feedback)
        feedback.setProgress(98)
        feedback.setProgressText(
            self.tr(
                'input file saved in ' + str(os.path.join(
                    project_dir,
                    inp_file_name)
                )
            )
        )
        return {}

    def shortHelpString(self):
        return self.tr(""" With this tool you can write a swmm input file based on QGIS layers (and supplementary data in .xslx files).\n
        The column names within attribute tables have to be the same as in the default data set.
        Proposed workflow:\n
        1) load default data with the first tool.\n
        2) copy all files to a new folder and edit the data set.\n
        3) select the edited layers / files to create the input file (.inp)\n
        4) run the input file in swmm
        """)

    def name(self):
        return 'GenerateSwmmInpFile'

    def displayName(self):
        return self.tr('2_GenerateSwmmInpFile')

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return ''

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return GenerateSwmmInpFile()

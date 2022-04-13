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
__date__ = '2021-07-09'
__copyright__ = '(C) 2021 by Jannik Schilling'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import pandas as pd
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingParameterVectorLayer)
from .g_s_various_functions import check_columns, get_coords_from_geometry
from .g_s_defaults import def_sections_dict, def_curve_types
from .g_s_read_data import read_data_from_table_direct, read_shapefiles_direct

class GenerateSwmmInpFile(QgsProcessingAlgorithm):
    """
    generates a swmm input file from geodata and tables
    """
    QGIS_OUT_INP_FILE = 'QGIS_OUT_INP_FILE'
    FILE_CONDUITS = 'FILE_CONDUITS'
    FILE_JUNCTIONS = 'FILE_JUNCTIONS'
    FILE_DIVIDERS = 'FILE_DIVIDERS'
    FILE_ORIFICES = 'FILE_ORIFICES'
    FILE_OUTFALLS = 'FILE_OUTFALLS'
    FILE_OUTLETS = 'FILE_OUTLETS'
    FILE_STORAGES = 'FILE_STORAGES'
    FILE_PUMPS    = 'FILE_PUMPS'
    FILE_SUBCATCHMENTS= 'FILE_SUBCATCHMENTS'
    FILE_WEIRS = 'FILE_WEIRS'
    
    FILE_CURVES = 'FILE_CURVES'
    FILE_PATTERNS = 'FILE_PATTERNS'
    FILE_OPTIONS = 'FILE_OPTIONS'
    FILE_TIMESERIES = 'FILE_TIMESERIES'
    FILE_INFLOWS = 'FILE_INFLOWS'
    FILE_QUALITY = 'FILE_QUALITY'
    FILE_TRANSECTS = 'FILE_TRANSECTS'
    FILE_STREETS = 'FILE_STREETS'
    
    
    
    def initAlgorithm(self, config):
        """
        inputs and output of the algorithm
        """
        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.QGIS_OUT_INP_FILE,
                self.tr('Where should the inp file be saved?'),
                'INP files (*.inp)', #defaultValue=['date.inp'] 
            )
        )
        
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_JUNCTIONS,
                self.tr('Junctions Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional = True#,defaultValue = 'SWMM_junctions'
                ))
                
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_CONDUITS,
                self.tr('Conduits Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional = True#,defaultValue = 'SWMM_conduits'
                ))
        
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_SUBCATCHMENTS,
                self.tr('Subcatchments Layer'),
                types=[QgsProcessing.SourceType.TypeVectorAnyGeometry],
                optional = True#,defaultValue = 'SWMM_subcatchments'
                ))
        
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_STORAGES,
                self.tr('Storages Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional = True#,defaultValue = 'SWMM_storages'
                ))
                
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_OUTFALLS,
                self.tr('Outfalls Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional = True#,defaultValue = 'SWMM_outfalls'
                ))
                
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_DIVIDERS,
                self.tr('Dividers Layer'),
                types=[QgsProcessing.SourceType.TypeVectorPoint],
                optional = True#,defaultValue = 'SWMM_dividers'
                ))
                
                
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_PUMPS,
                self.tr('Pumps Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional = True#,defaultValue = 'SWMM_Pumps'
                ))
                
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_WEIRS,
                self.tr('Weirs Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional = True#,defaultValue = 'SWMM_weirs'
                ))
                
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_ORIFICES,
                self.tr('Orifices Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional = True#,defaultValue = 'SWMM_orifices'
                ))
                
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.FILE_OUTLETS,
                self.tr('Outlets Layer'),
                types=[QgsProcessing.SourceType.TypeVectorLine],
                optional = True#,defaultValue = 'SWMM_outlets'
                ))
        
        
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_OPTIONS,
                self.tr('Options table file'),
                QgsProcessingParameterFile.File,
                'xlsx',
                optional = True
                ))
                
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_CURVES,
                self.tr('Curves table file'),
                QgsProcessingParameterFile.File,
                'xlsx',
                optional = True
                ))

        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_PATTERNS,
                self.tr('Patterns table file'),
                QgsProcessingParameterFile.File,
                'xlsx',
                optional = True
                ))
                

        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_TIMESERIES,
                self.tr('Timeseries table file'),
                QgsProcessingParameterFile.File,
                'xlsx',
                optional = True
                ))
                
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_INFLOWS,
                self.tr('Inflows table file'),
                QgsProcessingParameterFile.File,
                'xlsx',
                optional = True
                ))

        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_QUALITY,
                self.tr('Quality table file'),
                QgsProcessingParameterFile.File,
                'xlsx',
                optional = True
                ))
                
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_TRANSECTS,
                self.tr('Transects table file'),
                QgsProcessingParameterFile.File,
                'xlsx',
                optional = True
                ))
                
        self.addParameter(
            QgsProcessingParameterFile(
                self.FILE_STREETS,
                self.tr('Streets and Inlets table file'),
                QgsProcessingParameterFile.File,
                'xlsx',
                optional = True
                ))


    def processAlgorithm(self, parameters, context, feedback):  
        """input file name and path"""
        inp_file_path = self.parameterAsString(parameters, self.QGIS_OUT_INP_FILE, context)
        inp_file_name = os.path.basename(inp_file_path)
        project_dir = os.path.dirname(inp_file_path)

        """initializing the input dictionary and error text"""
        inp_dict = dict()
        inp_dict['junctions_df'] = pd.DataFrame()
        inp_dict['conduits_df'] = pd.DataFrame()
        inp_dict['storage_df'] = pd.DataFrame()
        inp_dict['xsections_df'] = pd.DataFrame()
        inp_dict['vertices_dict'] = {}

        """ reading geodata"""
        feedback.setProgressText(self.tr('Reading shapfiles'))
        feedback.setProgress(5)
        file_outfalls = self.parameterAsVectorLayer(parameters, self.FILE_OUTFALLS, context)
        file_storages = self.parameterAsVectorLayer(parameters, self.FILE_STORAGES, context)
        file_subcatchments = self.parameterAsVectorLayer(parameters, self.FILE_SUBCATCHMENTS, context)
        file_conduits = self.parameterAsVectorLayer(parameters, self.FILE_CONDUITS, context)
        file_junctions = self.parameterAsVectorLayer(parameters, self.FILE_JUNCTIONS, context)
        file_pumps = self.parameterAsVectorLayer(parameters, self.FILE_PUMPS, context)
        file_weirs = self.parameterAsVectorLayer(parameters, self.FILE_WEIRS, context)
        file_orifices = self.parameterAsVectorLayer(parameters, self.FILE_ORIFICES, context)
        file_outlets = self.parameterAsVectorLayer(parameters, self.FILE_OUTLETS, context)
        file_dividers = self.parameterAsVectorLayer(parameters, self.FILE_DIVIDERS, context)
        raw_data_dict = read_shapefiles_direct(file_outfalls,
                                           file_storages,
                                           file_subcatchments,
                                           file_conduits,
                                           file_junctions,
                                           file_pumps,
                                           file_weirs,
                                           file_orifices,
                                           file_outlets,
                                           file_dividers)
        feedback.setProgressText(self.tr('done \n'))
        feedback.setProgress(20)

        """reading data in tables (curves, patterns, inflows ...)"""
        feedback.setProgressText(self.tr('Reading tables'))
        file_curves = self.parameterAsString(parameters, self.FILE_CURVES, context)
        file_patterns = self.parameterAsString(parameters, self.FILE_PATTERNS, context)
        file_options = self.parameterAsString(parameters, self.FILE_OPTIONS, context)
        file_timeseries = self.parameterAsString(parameters, self.FILE_TIMESERIES, context)
        file_inflows = self.parameterAsString(parameters, self.FILE_INFLOWS, context)
        file_quality = self.parameterAsString(parameters, self.FILE_QUALITY, context)
        file_transects = self.parameterAsString(parameters, self.FILE_TRANSECTS, context)
        file_streets = self.parameterAsString(parameters, self.FILE_STREETS, context)
        
        
        """options table"""
        if file_options != '': #check if parameter is given as a string
            raw_data_dict['options_df'] = read_data_from_table_direct(file_options)
        """curves table"""
        if file_curves != '':
            raw_data_dict['curves'] = {}
            for curve_type in def_curve_types:
                curve_df = read_data_from_table_direct(file_curves,
                                                       sheet = curve_type)
                if len(curve_df)>0:
                    raw_data_dict['curves'][curve_type] = curve_df
        """patterns table"""
        if file_patterns != '':
            raw_data_dict['patterns'] = {}
            for pattern_type in ['HOURLY','DAILY','MONTHLY','WEEKEND']:
                raw_data_dict['patterns'][pattern_type] = read_data_from_table_direct(file_patterns,
                                                                                      sheet = pattern_type)
        """inflows table"""
        if file_inflows != '':
            raw_data_dict['inflows'] = {}
            for inflow_type in ['Direct','Dry_Weather']:
                 raw_data_dict['inflows'][inflow_type] = read_data_from_table_direct(file_inflows,
                                                                                     sheet = inflow_type)
        """timeseries table"""
        if file_timeseries != '':
            raw_data_dict['timeseries'] = read_data_from_table_direct(file_timeseries)   
        """quality table"""
        if file_quality != '':
            raw_data_dict['quality'] = {}
            for quality_param in['POLLUTANTS', 'LANDUSES', 'COVERAGES','LOADINGS']:
                raw_data_dict['quality'][quality_param] = read_data_from_table_direct(file_quality,
                                                                                      sheet = quality_param)
        """transects table"""
        if file_transects != '':
                raw_data_dict['transects'] = {}
                for transects_param in['Data', 'XSections']:
                    raw_data_dict['transects'][transects_param] = read_data_from_table_direct(file_transects,
                                                                                              sheet = transects_param)
                                                                                              
        """streets table"""
        if file_streets != '':
                raw_data_dict['streets'] = {}
                for streets_param in['STREETS', 'INLETS', 'INLET_USAGE']:
                    raw_data_dict['streets'][streets_param] = read_data_from_table_direct(file_streets,
                                                                                              sheet = streets_param)
        feedback.setProgressText(self.tr('done \n'))
        feedback.setProgress(25)
        
        feedback.setProgressText(self.tr('preparing data for input file:'))
        
        """options"""
        main_infiltration_method = None 
        if 'options_df' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[OPTIONS] section'))
            from .g_s_options import get_options_from_table
            inp_dict['options_dict'] = get_options_from_table(raw_data_dict['options_df'].copy())
            if 'INFILTRATION' in inp_dict['options_dict'].keys():
                main_infiltration_method = inp_dict['options_dict']['INFILTRATION']                
        """subcatchments"""
        if 'subcatchments_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[SUBCATCHMENTS] section'))
            from .g_s_subcatchments import get_subcatchments_from_shapefile, rg_position
            subcatchments_df = get_subcatchments_from_shapefile(raw_data_dict['subcatchments_raw'],
                                                                main_infiltration_method)
            inp_dict['polygons_dict'] = get_coords_from_geometry(subcatchments_df)
            inp_dict['subcatchments_df'] = subcatchments_df
            rg_x_mean, rg_y_mean = rg_position(inp_dict['polygons_dict']) # mean position of catchments for rain gage
            inp_dict['rg_pos'] = [rg_x_mean, rg_y_mean]

        """conduits"""
        if 'conduits_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[CONDUITS] section'))
            from .g_s_links import get_conduits_from_shapefile, del_first_last_vt
            conduits_df, xsections_df, losses_df =  get_conduits_from_shapefile(raw_data_dict['conduits_raw'].copy())
            conduits_verts = get_coords_from_geometry(raw_data_dict['conduits_raw'].copy())
            conduits_verts = {k: del_first_last_vt(v) for k,v in conduits_verts.items() if len(v) > 2} #first and last vertices are in nodes coordinates anyway
            inp_dict['vertices_dict'].update(conduits_verts)
            inp_dict['conduits_df'] = conduits_df
            inp_dict['xsections_df'] = xsections_df
            inp_dict['losses_df'] = losses_df

        """pumps"""
        if 'pumps_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[PUMPS] section'))
            from .g_s_links import get_pumps_from_shapefile, del_first_last_vt
            pumps_df = get_pumps_from_shapefile(raw_data_dict['pumps_raw'].copy())
            pumps_verts = get_coords_from_geometry(raw_data_dict['pumps_raw'].copy())
            pumps_verts = {k: del_first_last_vt(v) for k,v in pumps_verts.items() if len(v) > 2}
            inp_dict['vertices_dict'].update(pumps_verts)
            inp_dict['pumps_df'] = pumps_df

        """weirs"""
        if 'weirs_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[WEIRS] section'))
            from .g_s_links import get_weirs_from_shapefile, del_first_last_vt
            weirs_df, xsections_df= get_weirs_from_shapefile(raw_data_dict['weirs_raw'])
            weirs_verts = get_coords_from_geometry(raw_data_dict['conduits_raw'].copy())
            weirs_verts = {k: del_first_last_vt(v) for k,v in weirs_verts.items() if len(v) > 2} #first and last vertices are in nodes coordinates anyway
            inp_dict['vertices_dict'].update(weirs_verts)
            inp_dict['xsections_df'] = inp_dict['xsections_df'].append(xsections_df)
            inp_dict['xsections_df'] = inp_dict['xsections_df'].reset_index(drop=True)
            inp_dict['weirs_df'] = weirs_df

        """outlets"""
        if 'outlets_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[OUTLETS] section'))
            from .g_s_links import get_outlets_from_shapefile, del_first_last_vt
            inp_dict['outlets_df'] = get_outlets_from_shapefile(raw_data_dict['outlets_raw'])
            outlets_verts = get_coords_from_geometry(raw_data_dict['outlets_raw'].copy())
            outlets_verts = {k: del_first_last_vt(v) for k,v in outlets_verts.items() if len(v) > 2}
            inp_dict['vertices_dict'].update(outlets_verts)
            
        """optional: transects for conduits or weirs"""
        if 'conduits_raw' in raw_data_dict.keys() or 'weirs_raw' in raw_data_dict.keys():
            if 'transects' in raw_data_dict.keys():
                feedback.setProgressText(self.tr('[TRANSECTS] section'))
                from .g_s_links import get_transects_from_table
                transects_string_list = get_transects_from_table(raw_data_dict['transects'].copy())
                inp_dict['transects_string_list'] = transects_string_list
        
        """orifices"""
        if 'orifices_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[ORIFICES] section'))
            from .g_s_links import get_orifices_from_shapefile, del_first_last_vt
            orifices_df, xsections_df= get_orifices_from_shapefile(raw_data_dict['orifices_raw'])
            orifices_verts = get_coords_from_geometry(raw_data_dict['orifices_raw'].copy())
            orifices_verts = {k: del_first_last_vt(v) for k,v in orifices_verts.items() if len(v) > 2} #first and last vertices are in nodes coordinates anyway
            inp_dict['vertices_dict'].update(orifices_verts)
            inp_dict['xsections_df'] = inp_dict['xsections_df'].append(xsections_df)
            inp_dict['xsections_df'] = inp_dict['xsections_df'].reset_index(drop=True)
            inp_dict['orifices_df'] = orifices_df

        feedback.setProgress(40)


        """nodes (junctions, outfalls, orifices)"""
        all_nodes = list()
        if 'junctions_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[JUNCTIONS] section'))
            junctions_df = raw_data_dict['junctions_raw'].copy()
            # check columns
            junctions_cols = list(def_sections_dict['JUNCTIONS'].keys())
            junctions_layer_name = 'Junctions Layer'
            check_columns(junctions_layer_name,
                          junctions_cols,
                          junctions_df.keys())
            junctions_df['X_Coord'],junctions_df['Y_Coord'] = get_coords_from_geometry(junctions_df)
            inp_dict['junctions_df'] = junctions_df
            all_nodes = all_nodes+junctions_df['Name'].tolist()
        if 'outfalls_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[OUTFALLS] section'))
            outfalls_cols = list(def_sections_dict['OUTFALLS'].keys())
            outfalls_layer_name = 'Outfalls Layer'
            check_columns(outfalls_layer_name,
                          outfalls_cols,
                          raw_data_dict['outfalls_raw'].keys())
            from .g_s_nodes import get_outfalls_from_shapefile
            outfalls_df = get_outfalls_from_shapefile(raw_data_dict['outfalls_raw'].copy())
            outfalls_df['X_Coord'],outfalls_df['Y_Coord'] = get_coords_from_geometry(outfalls_df)
            inp_dict['outfalls_df'] = outfalls_df
            all_nodes = all_nodes+outfalls_df['Name'].tolist()
        if 'storages_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[STORAGES] section'))
            # check columns is performed within get_storages_from_geodata for different storage types
            from .g_s_nodes import get_storages_from_geodata
            storage_df = get_storages_from_geodata(raw_data_dict['storages_raw'].copy())
            inp_dict['storage_df'] = storage_df
            all_nodes = all_nodes+storage_df['Name'].tolist()
        if 'dividers_raw' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[DIVIDERS] section'))
            dividers_df = raw_data_dict['dividers_raw'].copy()
            dividers_df['X_Coord'],dividers_df['Y_Coord'] = get_coords_from_geometry(dividers_df)
            # check columns
            dividers_cols = list(def_sections_dict['DIVIDERS'].keys())
            dividers_layer_name = 'Dividers Layer'
            check_columns(dividers_layer_name,
                          dividers_cols,
                          dividers_df.keys())
                          
            dividers_df['CutoffFlow'] = dividers_df['CutoffFlow'].fillna('')
            dividers_df['Curve'] = dividers_df['Curve'].fillna('')
            dividers_df['WeirMinFlo'] = dividers_df['WeirMinFlo'].fillna('')
            dividers_df['WeirMaxDep'] = dividers_df['WeirMaxDep'].fillna('')
            dividers_df['WeirCoeff'] = dividers_df['WeirCoeff'].fillna('')
            inp_dict['dividers_df'] = dividers_df
            all_nodes = all_nodes+dividers_df['Name'].tolist()
            # pass
        feedback.setProgress(50)

        """inflows"""
        if len(all_nodes) > 0:
            if 'inflows' in raw_data_dict.keys():
                feedback.setProgressText(self.tr('[INFLOWS] section'))
                from .g_s_nodes import get_inflows_from_table
                dwf_dict , inflow_dict = get_inflows_from_table(raw_data_dict['inflows'],all_nodes)
                if len(inflow_dict) > 0:
                    inp_dict['inflow_dict'] = inflow_dict
                if len(dwf_dict) > 0:
                    inp_dict['dwf_dict'] = dwf_dict
        feedback.setProgress(55)
        
        """Streets and inlets"""
        if 'streets' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[STREETS] and [INLETS] section'))
            from .g_s_links import get_street_from_tables
            streets_df , inlets_df, inlet_usage_df = get_street_from_tables(raw_data_dict['streets']) #all nodes all conduits?
            if len(streets_df) > 0:
                inp_dict['streets_df'] = streets_df
            if len(inlets_df) > 0:
                inp_dict['inlets_df'] = inlets_df
            if len(inlet_usage_df) > 0:
                inp_dict['inlet_usage_df'] = inlet_usage_df
            
        """Curves"""
        if 'curves' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[CURVES] section'))
            from .g_s_various_functions import get_curves_from_table
            inp_dict['curves_dict'] = get_curves_from_table(raw_data_dict['curves'],
                                                                 name_col='Name')
        feedback.setProgress(60)

        """patterns"""
        if 'patterns' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[PATTERNS] section'))
            from .g_s_various_functions import get_patterns_from_table
            inp_dict['patterns_dict'] = get_patterns_from_table(raw_data_dict['patterns'],
                                                                 name_col='Name')
        feedback.setProgress(65)
        
        """time series"""
        if 'timeseries' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[TIMESERIES] section'))
            from .g_s_various_functions import get_timeseries_from_table, get_raingages_from_timeseries
            inp_dict['timeseries_dict'] = get_timeseries_from_table(raw_data_dict['timeseries'],
                                                                 name_col='Name',
                                                                 feedback = feedback)
            """rain gages"""
            inp_dict['raingages_dict'] = get_raingages_from_timeseries(inp_dict['timeseries_dict'],feedback)
            if 'rg_pos' in inp_dict.keys():
                pass
            else:
                inp_dict['rg_pos'] = [1,2]
        feedback.setProgress(70)
   
        """quality"""
        if 'quality' in raw_data_dict.keys():
            feedback.setProgressText(self.tr('[POLLUTANTS] and [LANDUSES] section'))
            from .g_s_quality import get_quality_params_from_table
            if 'subcatchments_df' in inp_dict.keys():
                inp_dict['quality_dict'] = get_quality_params_from_table(raw_data_dict['quality'], inp_dict['subcatchments_df'].copy())
            else: 
                inp_dict['quality_dict'] = get_quality_params_from_table(raw_data_dict['quality'])
        
        feedback.setProgressText(self.tr('done \n'))
        feedback.setProgress(80)


        feedback.setProgressText(self.tr('Creating inp file:'))
        """writing inp"""
        from .g_s_write_inp import write_inp
        write_inp(inp_file_name,
                  project_dir,
                  inp_dict,
                  feedback)
        feedback.setProgress(98)
        
        feedback.setProgressText(self.tr('input file saved in '+str(os.path.join(project_dir,inp_file_name))))
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

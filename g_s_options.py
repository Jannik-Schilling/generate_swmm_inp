# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GenerateSwmmInp
                                 A QGIS plugin
 This plugin generates SWMM Input files
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-09
        copyright            : (C) 2022 by Jannik Schilling
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
__date__ = '2022-04-28'
__copyright__ = '(C) 2022 by Jannik Schilling'


import numpy as np
import pandas as pd
from datetime import datetime, time
from qgis.core import QgsProcessingException

def adjust_options_dtypes(opt_key, opt_val, opt_source, feedback = None):
    """
    converts datetime formats to string and vice versa
    :param str opt_key
    :param any opt_val
    :param str opt_source: 'table' (source is the options table) or 'input' (source is the SWMM input file)
    """        
    def_options_dtypes ={'START_DATE':[[datetime],'%m/%d/%Y'],
                        'REPORT_START_DATE':[[datetime],'%m/%d/%Y'],
                        'END_DATE':[[datetime],'%m/%d/%Y'],
                        'SWEEP_START':[[datetime],'%m/%d'],
                        'SWEEP_END':[[datetime],'%m/%d'],
                        'START_TIME':[[time, datetime],'%H:%M:%S'],
                        'REPORT_START_TIME':[[time, datetime],'%H:%M:%S'],
                        'END_TIME':[[time, datetime],'%H:%M:%S'],
                        'REPORT_STEP':[[time, datetime],'%H:%M:%S'],
                        'WET_STEP':[[time, datetime],'%H:%M:%S'],
                        'DRY_STEP':[[time, datetime],'%H:%M:%S'],
                        'ROUTING_STEP':[[time, datetime],'%H:%M:%S'],
                        'RULE_STEP':[[time, datetime],'%H:%M:%S'],
                        'FLOW_UNITS':[[str],['CFS','GPM','MGD','CMS','LPS','MLD']],
                        'INFILTRATION':[[str], ['HORTON','MODIFIED_HORTON','GREEN_AMPT','MODIFIED_GREEN_AMPT','CURVE_NUMBER']],
                        'FLOW_ROUTING':[[str],['STEADY','KINWAVE','DYNWAVE']],
                        'LINK_OFFSETS':[[str],['DEPTH','ELEVATION']],
                        'FORCE_MAIN_EQUATION':[[str],['H-W','D-W']],
                        'IGNORE_RAINFALL':[[str],['YES','NO']],
                        'IGNORE_SNOWMELT':[[str],['YES','NO']],
                        'IGNORE_GROUNDWATER':[[str],['YES','NO']],
                        'IGNORE_RDII':[[str],['YES','NO']],
                        'IGNORE_ROUTING':[[str],['YES','NO']],
                        'IGNORE_QUALITY':[[str],['YES','NO']],
                        'ALLOW_PONDING':[[str],['YES','NO']],
                        'SKIP_STEADY_STATE':[[str],['YES','NO']],
                        'SYS_FLOW_TOL':[[int,float]], 
                        'LAT_FLOW_TOL':[[int,float]], 
                        'DRY_DAYS':[[int]],
                        'LENGTHENING_STEP':[[int,float]],
                        'VARIABLE_STEP':[[int,float]],
                        'MINIMUM_STEP':[[int,float]],
                        'INERTIAL_DAMPING':[[str],['NONE','PARTIAL','FULL']],
                        'NORMAL_FLOW_LIMITED':[[str],['SLOPE','FROUDE','BOTH']],
                        'MIN_SURFAREA':[[int,float]], 
                        'MIN_SLOPE':[[int,float]], 
                        'MAX_TRIALS':[[int]], 
                        'HEAD_TOLERANCE':[[int,float]], 
                        'THREADS':[[int]],
                        'TEMPDIR':[[str]]
                      }
    d_type_val = type(opt_val)
    d_type_def = def_options_dtypes[opt_key][0]
    if opt_source == 'table':
        if d_type_val in d_type_def:
            if d_type_def[0] in [time,datetime]:
                d_struct = def_options_dtypes[opt_key][1]
                opt_val = opt_val.strftime(d_struct)
            if  (d_type_def[0] is str) and (opt_key!='TEMPDIR'):
                def_vals = def_options_dtypes[opt_key][1]
                if opt_val not in def_vals:
                    raise QgsProcessingException('[OPTIONS]: Value for '+opt_key+' must be one of '+', '.join(def_vals))
    if opt_source == "input":
        if d_type_def[0] == datetime:
            d_struct = def_options_dtypes[opt_key][1]
            opt_val= datetime.strptime(opt_val, d_struct).date()
        if d_type_def[0] == time:
            d_struct = def_options_dtypes[opt_key][1]
            if opt_key in ['REPORT_STEP','WET_STEP','DRY_STEP'] and int(opt_val.split(':')[0]) > 23:
                feedback.reportError('Warning: '+str(opt_key)+ ' was more than 24h. To avoid time format errors in Python, this value was set to 01:00:00')
                opt_val =  datetime.strptime('01:00:00', d_struct).time()
            else:
                opt_val= datetime.strptime(opt_val, d_struct).time()
        if d_type_def[0] == int:
            opt_val = float(opt_val)
    return opt_val


    
def get_options_from_table(options_df): 
    """
    converts file_options_df to dict and 
    converts datetime formats to string
    :param pd.DataFrame options_df
    """
    options_dict = {k:adjust_options_dtypes(k,v,'table') for k,v in zip(options_df['Option'],options_df['Value'])}
    return options_dict
    
def convert_options_format_for_import(dict_options, feedback):
    '''
    converts formats in dict_options for the options file
    :param dict dict_options
    :param QgsProcessingFeedback feedback
    '''
    dict_options = {k:adjust_options_dtypes(k,v,'input',feedback) for k,v in dict_options.items()}
    df_options = pd.DataFrame()
    df_options['Option'] = dict_options.keys()
    df_options['Value'] = dict_options.values()
    return df_options
    

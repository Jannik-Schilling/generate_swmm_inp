# -*- coding: utf-8 -*-
"""
Created on Mon May 17 14:45:10 2021

@author: schilling
"""
import numpy as np
import pandas as pd
from datetime import datetime, time
from qgis.core import QgsProcessingException

def adjust_options_dtypes(opt_key, opt_val, opt_source):
    """
    converts datetime formats to string and vice versa
    :param str opt_key
    :param any opt_val
    :param str opt_source
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
    
def convert_options_format_for_import(dict_options):
    '''
    converts formats in dict_options for the options file
    :param dict dict_options
    '''
    dict_options = {k:adjust_options_dtypes(k,v,'input') for k,v in dict_options.items()}
    df_options = pd.DataFrame()
    df_options['Option'] = dict_options.keys()
    df_options['Value'] = dict_options.values()
    return df_options
    

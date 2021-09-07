# -*- coding: utf-8 -*-
"""
Created on Mon May 17 14:45:10 2021

@author: schilling
"""
import numpy as np
import pandas as pd
from qgis.core import QgsWkbTypes

## geometry functions
def get_coords_from_geometry(df):
    '''extracts coords from any gpd.geodataframe'''
    def extract_xy_from_simple_line(line_simple):
        '''extracts x and y coordinates from a LineString'''
        xy_arr = np.dstack((p.x(),p.y()) for p in line_simple)[0]
        xy_df = pd.DataFrame(xy_arr.T,columns = ['x','y'])
        return xy_df
    def extract_xy_from_line(line_row):
        '''extraxts xy from LineString or MultiLineString'''
        if QgsWkbTypes.displayString(line_row.wkbType()) == 'LineString':
            return extract_xy_from_simple_line(line_row.asPolyline())
        if QgsWkbTypes.displayString(line_row.wkbType()) == 'MultiLineString':
            xy_list = [extract_xy_from_simple_line(line_simple) for line_simple in line_row.asMultiPolyline()]
            return pd.concat(xy_list, ignore_index=True)
    if all(QgsWkbTypes.displayString(g_type.wkbType()) in ['Point'] for g_type in df.geometry):
        df['X_Coord'] = [str(df_row.asPoint().x()) for df_row in df['geometry']]
        df['Y_Coord'] = [str(df_row.asPoint().y()) for df_row in df['geometry']]
        return df['X_Coord'],df['Y_Coord']
    if all(QgsWkbTypes.displayString(g_type.wkbType()) in ['LineString', 'MultiLineString'] for g_type in df.geometry):
        return {na:extract_xy_from_line(geom) for geom,na in zip(df.geometry,df.Name)}
    if all(QgsWkbTypes.displayString(g_type.wkbType()) in ['Polygon', 'MultiPolygon'] for g_type in df.geometry):
        def extract_xy_from_area(geom_row):
            '''extraxts xy from MultiPolygon or Polygon'''
            if QgsWkbTypes.displayString(geom_row.wkbType()) == 'MultiPolygon':
                xy_arr = np.dstack((v.x(),v.y()) for v in geom_row.vertices())[0]
                xy_df = pd.DataFrame(xy_arr.T,columns = ['x','y'])
                return xy_df
            if QgsWkbTypes.displayString(geom_row.wkbType()) == 'Polygon':
                xy_arr = np.dstack((v.x(),v.y()) for v in geom_row.vertices())[0]
                xy_df = pd.DataFrame(xy_arr.T,columns = ['x','y'])
                return xy_df
        return {na:extract_xy_from_area(ge) for ge,na in zip(df.geometry,df.Name)}

def get_point_from_x_y(sr):
    '''converts x and y coordinates from a pd.Series (arg: sr) to a QgsPoint geometry'''
    from qgis.core import QgsGeometry
    x_coord = sr['X_Coord']
    y_coord = sr['Y_Coord']
    geom = QgsGeometry.fromWkt('POINT('+str(x_coord)+' '+str(y_coord)+')')
    return [sr['Name'],geom]



def check_columns(x_df, col_df):
    '''checks if all columns are in a dataframe'''
    cols_oblig =  col_df[col_df['oblig'] == True]
    cols_volunt = col_df[col_df['oblig'] == False]
    if not all(np.isin(cols_oblig['col_name'],x_df.columns)):
        return 'Error: obligatory columns missing'
    for check_col in cols_volunt['col_name']:
        if np.isin(check_col, x_df.columns):
            pass 
        else:
            x_df[check_col] = cols_volunt.loc[cols_volunt['col_name']==check_col,'default'].values[0]
    return x_df


## functions for data in tables
def get_curves_from_table(curves_raw, name_col):
    """generates curve data for the input file from tables (curve_raw)"""
    from .g_s_defaults import def_curve_types
    curve_dict = dict()
    for curve_type in def_curve_types:
        if curve_type in curves_raw.keys():
            curve_df = curves_raw[curve_type]
            if len(curve_df.columns) > 3:
                curve_df = curve_df[curve_df.columns[:3]]
            curve_df = curve_df[curve_df[name_col] != ";"]
            curve_df = curve_df[pd.notna(curve_df[name_col])]
            if curve_df.empty:
                pass
            else:
                curve_df.set_index(keys=[name_col], inplace=True)
                for i in curve_df.index.unique():
                    curve = curve_df[curve_df.index == i]
                    curve = curve.reset_index(drop=True)
                    curve_dict[i] = {'Name':i, 'Type':curve_type,'frame':curve}
    return(curve_dict)
    

def get_patterns_from_table(patterns_raw, name_col):
    """generates a pattern dict for the input file from tables (patterns_raw)"""
    pattern_types = ['HOURLY','DAILY','MONTHLY','WEEKEND']
    pattern_dict = {}
    for pattern_type in pattern_types:
        pattern_df = patterns_raw[pattern_type]
        pattern_df = pattern_df[pattern_df[name_col] != ";"]
        pattern_df = pattern_df[pd.notna(pattern_df[name_col])]
        if pattern_df.empty:
            pass
        else:
            pattern_df.set_index(keys=[name_col], inplace=True)
            for i in pattern_df.index.unique():
                pattern = pattern_df[pattern_df.index == i]
                pattern = pattern.drop(columns = pattern.columns[0])
                pattern = pattern.reset_index(drop=True)
                pattern_dict[i] = {'Name':i, 'Type':pattern_type,'Factors':pattern}
    return(pattern_dict)
    
    
def get_timeseries_from_table(ts_raw, name_col):
    """generates a timeseries dict for the input file from tables (ts_raw)"""
    ts_dict = dict()
    ts_raw = ts_raw[ts_raw[name_col] != ";"]
    if ts_raw.empty:
        pass
    else:
        for i in ts_raw[name_col].unique():
            ts_df = ts_raw[ts_raw[name_col] == i]
            ts_df['Date']= [t.strftime('%m/%d/%Y') for t in ts_df['Date']]
            try:
                ts_df['Time'] = [t.strftime('%H:%M:%S') for t in ts_df['Time']]
            except:
                #temp_time = [datetime.strptime(t,'%H:%M:%S') for t in ts_df['Time']]
                #ts_df['Time']= [t.strftime('%H:%M:%S') for t in temp_time]
                ts_df['Time'] = [str(t) for t in ts_df['Time']]
            ts_description= ts_df['Description'].fillna('').unique()[0]
            ts_format= ts_df['Format'].fillna('').unique()[0]
            ts_type = ts_df['Type'].unique()[0]
            ts_dict[i] = {'Name':i,
                   'Type':ts_type,
                   'TimeSeries':ts_df[['Name','Date','Time','Value']], 
                   'Description':ts_description,
                   'Format':ts_format}
    return(ts_dict)
    
    

def get_raingages_from_timeseries(ts_dict):
    """generates a raingages dict for the input file from timeseries dict"""
    from datetime import datetime
    rg_dict= {}
    rg_list = [k for k in ts_dict.keys() if (ts_dict[k]['Type'] == 'rain_gage')]
    for rg in rg_list:
        rg_i = ts_dict[rg]
        rg_i['TimeSeries'] = rg_i['TimeSeries'].reset_index(drop=True)
        timediff = datetime.strptime(rg_i['TimeSeries']['Time'][1],'%H:%M:%S')-datetime.strptime(rg_i['TimeSeries']['Time'][0],'%H:%M:%S')
        #rg_hours, remainder = divmod(timediff.total_seconds(), 3600)
        #rg_minutes, seconds = divmod(remainder, 60)
        rg_interval = str(timediff)[:-3]
        rg_dict[rg_i['Description']] = {'Name':rg_i['Description'],
               'Format':rg_i['Format'],
               'Interval': rg_interval,
               'SCF':'1',
               'Source':'TIMESERIES'+' '+rg}
    return (rg_dict)
               
    
def get_inflows_from_table(inflows_raw,junctions_df):
    '''
    generates a dict for direct inflow and
    dry weather inflow from tables in swmm_inflows.xlsx
    '''
    def compose_infl_dict(inflow,i,inf_type):
        if inf_type == 'Direct':
            i_dict = {'Name':i,
               'Constituent':inflow['Constituent'],
               'Time_Series':inflow['Time_Series'],
               'Type':inflow['Type'],
               'Mfactor':1,
               'Sfactor':inflow['Scale_Factor'],
               'Baseline':inflow['Baseline'],
               'Pattern':inflow['Baseline_Pattern']}
        else:
            i_dict = {'Name':i,
                      'Constituent':inflow['Constituent'],
                      'Baseline':inflow['Average_Value'],
                      'Patterns':' '.join([inflow['Time_Pattern1'],
                                           inflow['Time_Pattern2'],
                                           inflow['Time_Pattern3'],
                                           inflow['Time_Pattern4']])}
        return i_dict
    err_txt = ''
    for inflow_type in ['Direct','Dry_Weather']:
        inflow_df = inflows_raw[inflow_type]
        inflow_df = inflow_df[inflow_df['Name'] != ";"]
        infl_err = inflow_df[~inflow_df['Name'].isin(junctions_df['Name'])]
        infl_err = infl_err[pd.notna(infl_err['Name'])]
        if len(infl_err)>0:
            err_txt = err_txt+'\n---\nFehlende Junctions für Abflusstyp "'+inflow_type+'":\n'+'\n'.join([n for n in infl_err['Name'].unique()])
        inflow_df = inflow_df[inflow_df['Name'].isin(junctions_df['Name'])]
        inflow_df = inflow_df[pd.notna(inflow_df['Name'])]
        inflow_df = inflow_df.fillna('""')
        if inflow_df.empty:
            if inflow_type == 'Direct':
                inflow_dict={}
            else:
                dwf_dict={}
        else:
            a_l = inflow_df['Name'].tolist()
            b_l = inflow_df['Constituent'].tolist()
            inflow_df['temp'] = [str(a)+'    '+str(b) for a,b in zip(a_l, b_l)]
            inflow_df.set_index(keys=['temp'], inplace=True)
            if inflow_type == 'Direct':
                inflow_dict = {i:compose_infl_dict(inflow_df.loc[i,:],i,inflow_type)  for i in inflow_df.index}
            else: 
                dwf_dict = {i:compose_infl_dict(inflow_df.loc[i,:],i,inflow_type)  for i in inflow_df.index}

    return dwf_dict, inflow_dict, err_txt
    
    
def get_options_from_table(options_df): 
    '''
    converts file_options_df to dict and 
    converts datetime formats to string
    Args:
        options_df
    '''
    from datetime import datetime, time
    options_dict = {k:v for k,v in zip(options_df['Option'],options_df['Value'])}
    if type(options_dict['START_DATE']) is datetime:
        options_dict['START_DATE'] = options_dict['START_DATE'].strftime('%m/%d/%Y')
    if type(options_dict['REPORT_START_DATE']) is datetime:
        options_dict['REPORT_START_DATE'] = options_dict['REPORT_START_DATE'].strftime('%m/%d/%Y')
    if type(options_dict['END_DATE']) is datetime:
        options_dict['END_DATE'] = options_dict['END_DATE'].strftime('%m/%d/%Y')
    if type(options_dict['SWEEP_START']) is datetime:
        options_dict['SWEEP_START'] = options_dict['SWEEP_START'].strftime('%m/%d')
    if type(options_dict['SWEEP_END']) is datetime:
        options_dict['SWEEP_END'] = options_dict['SWEEP_END'].strftime('%m/%d')
    if type(options_dict['START_TIME']) in [datetime, time]:
        options_dict['START_TIME'] = options_dict['START_TIME'].strftime('%H:%M:%S')
    if type(options_dict['REPORT_START_TIME']) in [datetime, time]:
        options_dict['REPORT_START_TIME'] = options_dict['REPORT_START_TIME'].strftime('%H:%M:%S')
    if type(options_dict['END_TIME']) in [datetime, time]:
        options_dict['END_TIME'] = options_dict['END_TIME'].strftime('%H:%M:%S')
    if type(options_dict['REPORT_STEP']) in [datetime, time]:
        options_dict['REPORT_STEP'] = options_dict['REPORT_STEP'].strftime('%H:%M:%S')
    if type(options_dict['WET_STEP']) in [datetime, time]:
        options_dict['WET_STEP'] = options_dict['WET_STEP'].strftime('%H:%M:%S')
    if type(options_dict['DRY_STEP']) in [datetime, time]:
        options_dict['DRY_STEP'] = options_dict['DRY_STEP'].strftime('%H:%M:%S')
    if type(options_dict['ROUTING_STEP']) in [datetime, time]:
        options_dict['ROUTING_STEP'] = options_dict['ROUTING_STEP'].strftime('%H:%M:%S')
    if type(options_dict['RULE_STEP']) in [datetime, time]:
        options_dict['RULE_STEP'] = options_dict['RULE_STEP'].strftime('%H:%M:%S')
    return options_dict
    
def convert_options_format_for_import(dict_options):
    from datetime import datetime
    dict_options['START_DATE'] = datetime.strptime(dict_options['START_DATE'],'%m/%d/%Y').date()
    dict_options['REPORT_START_DATE'] = datetime.strptime(dict_options['REPORT_START_DATE'],'%m/%d/%Y').date()
    dict_options['END_DATE'] = datetime.strptime(dict_options['END_DATE'],'%m/%d/%Y').date()
    dict_options['SWEEP_START'] = datetime.strptime(dict_options['SWEEP_START'],'%m/%d').date()
    dict_options['SWEEP_END'] = datetime.strptime(dict_options['SWEEP_END'],'%m/%d').date()
    dict_options['START_TIME'] = datetime.strptime(dict_options['START_TIME'],'%H:%M:%S').time()
    dict_options['REPORT_START_TIME'] = datetime.strptime(dict_options['REPORT_START_TIME'],'%H:%M:%S').time()
    dict_options['END_TIME'] = datetime.strptime(dict_options['END_TIME'],'%H:%M:%S').time()
    dict_options['REPORT_STEP'] = datetime.strptime(dict_options['REPORT_STEP'],'%H:%M:%S').time()
    dict_options['WET_STEP'] = datetime.strptime(dict_options['WET_STEP'],'%H:%M:%S').time()
    dict_options['DRY_STEP'] = datetime.strptime(dict_options['DRY_STEP'],'%H:%M:%S').time()
    dict_options['ROUTING_STEP'] = datetime.strptime(dict_options['ROUTING_STEP'],'%H:%M:%S').time()
    dict_options['RULE_STEP'] = datetime.strptime(dict_options['RULE_STEP'],'%H:%M:%S').time()
    df_options = pd.DataFrame()
    df_options['Option'] = dict_options.keys()
    df_options['Value'] = dict_options.values()
    return df_options
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
from .g_s_defaults import def_sections_dict
from .g_s_various_functions import check_columns, get_coords_from_geometry

# Outfalls
def get_outfalls_from_shapefile(outfalls_raw):
    outfalls_raw.loc[outfalls_raw['Type'] == 'TIDAL', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'TIDAL','Curve_TS']
    outfalls_raw.loc[outfalls_raw['Type'] == 'TIMESERIES', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'TIMESERIES','Curve_TS']
    outfalls_raw.loc[outfalls_raw['Type'] == 'FIXED', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'FIXED','FixedStage']
    outfalls_raw.loc[outfalls_raw['Type'] == 'FREE', 'Data'] = ''
    outfalls_raw.loc[outfalls_raw['Type'] == 'NORMAL', 'Data'] = ''
    outfalls_raw['RouteTo'] = outfalls_raw['RouteTo'].fillna('')
    outfalls_raw['Data'] = outfalls_raw['Data'].fillna('')
    return outfalls_raw

outfall_field_vals = {
    'FlapGate':{
        'NO':'NO',
        'YES':'YES'},
    'Type':{
        'FIXED':'FIXED',
        'FREE':'FREE',
        'NORMAL':'NORMAL',
        'TIMESERIES':'TIMESERIES',
        'TIDAL':'TIDAL'}}



# Storages
st_types_def = {
    'FUNCTIONAL':['Coeff','Exponent','Constant'],
    'TABULAR':['Curve'],
    'PYRAMIDAL':['MajorAxis','MinorAxis','SideSlope'],
    'PARABOLIC':['MajorAxis','MinorAxis','SurfHeight'],
    'CONICAL':['MajorAxis','MinorAxis','SideSlope'],
    'CYLINDRICAL':['MajorAxis','MinorAxis']}
all_st_type_cols = [
    'Curve',
    'Coeff',
    'Exponent',
    'Constant',
    'MajorAxis',
    'MinorAxis',
    'SideSlope',
    'SurfHeight']


def get_storages_from_geodata(storages_raw):
    '''creates a df for storages from raw storage data'''
    storages_layer_name = 'Storages Layer'
    storage_df = storages_raw.copy()
    check_columns(storages_layer_name,
                  ['Type'],
                  storage_df.keys())
    occuring_storage_types = list(set(storages_raw['Type']))
    st_types_needed = list(set([col for s_t in occuring_storage_types for col in st_types_def[s_t]]))
    st_types_not_needed = [col for col in all_st_type_cols if col not in st_types_needed]
    storages_cols = list(def_sections_dict['STORAGE'].keys())
    storages_cols_needed = [col for col in storages_cols if col not in st_types_not_needed]
    check_columns(storages_layer_name,
                  storages_cols_needed,
                  storage_df.keys())
    storage_df['X_Coord'],storage_df['Y_Coord'] = get_coords_from_geometry(storage_df)
    def st_type_adjustment(st_row):
        st_type_i = st_row['Type']
        cols_needed_i = st_types_def[st_type_i]
        if len(cols_needed_i) == 1: #TABULAR
            return st_row[cols_needed_i[0]], '', '' 
        elif len(cols_needed_i) == 2: #CYLINDRICAL
            return st_row[cols_needed_i[0]], st_row[cols_needed_i[1]], 0 
        else:
            return st_row[cols_needed_i[0]], st_row[cols_needed_i[1]], st_row[cols_needed_i[2]]
    storage_df[['Shape1','Shape2','Shape3']] = [st_type_adjustment(storage_df.loc[i]) for i in storage_df.index]
    storage_df['Psi'] = storage_df['Psi'].fillna('')
    storage_df['Ksat'] = storage_df['Ksat'].fillna('')
    storage_df['IMD'] = storage_df['IMD'].fillna('')
    storage_df = storage_df.drop(columns=st_types_needed)
    return storage_df

def get_storages_from_inp(st_raw_line):
    '''adjusts '''
    init_elems = st_raw_line[:5]
    st_type_i = st_raw_line[4]
    st_cols_i = st_types_def[st_type_i]
    st_vals_i = {col:st_raw_line[5+i] for i,col in enumerate(st_cols_i)}
    st_missing = {col_0:np.nan for col_0 in all_st_type_cols if col_0 not in st_vals_i.keys()}
    st_vals_i.update(st_missing)
    type_elems = [st_vals_i[t_c] for t_c in all_st_type_cols]
    # Seepage and Evaporation loss
    if st_type_i == 'TABULAR':
        sur_elems = st_raw_line[6:]
    else:
        sur_elems = st_raw_line[8:]
    if len(sur_elems) == 2:
        sur_elems = sur_elems+[np.nan,np.nan,np.nan]
    # resulting line
    st_line_adjusted = init_elems+type_elems+sur_elems
    return(st_line_adjusted)
    


#inflows
def get_inflows_from_table(inflows_raw,all_nodes):
    '''
    generates a dict for direct inflow and
    dry weather inflow from tables in "inflows_raw"
    '''
    def compose_infl_dict(inflow,i,inf_type):
        if inf_type == 'Direct':
            i_dict = {'Name':i,
               'Constituent':inflow['Constituent'],
               'Time_Series':inflow['Time_Series'],
               'Type':inflow['Type'],
               'Mfactor':inflow['Units_Factor'],
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
    for inflow_type in ['Direct','Dry_Weather']:
        # check if all columns exits
        inflow_df = inflows_raw[inflow_type]
        if inflow_type == 'Direct':
            inflow_cols_needed = list(def_sections_dict['INFLOWS'])
        if inflow_type == 'Dry_Weather':
            inflow_cols_needed = list(def_sections_dict['DWF'])
        table_name = inflow_type+' table'
        check_columns(table_name,
                      inflow_cols_needed,
                      inflow_df.columns)
        # delete inflows for nodes which do no exist
        inflow_df = inflow_df[inflow_df['Name'] != ";"]
        inflow_df = inflow_df[inflow_df['Name'].isin(all_nodes)]
        inflow_df = inflow_df[pd.notna(inflow_df['Name'])]
        inflow_df = inflow_df.fillna('""')
        if inflow_df.empty: 
            #if no flow of the current inflow_type and existing nodes is given, return empty dicts
            if inflow_type == 'Direct':
                inflow_dict={}
            else:
                dwf_dict={}
        else:
            # prepare a dict with node names and constituents
            a_l = inflow_df['Name'].tolist()
            b_l = inflow_df['Constituent'].tolist()
            inflow_df['temp'] = [str(a)+'    '+str(b) for a,b in zip(a_l, b_l)]
            inflow_df.set_index(keys=['temp'], inplace=True)
            if inflow_type == 'Direct':
                inflow_dict = {i:compose_infl_dict(inflow_df.loc[i,:],i,inflow_type)  for i in inflow_df.index}
            else: 
                dwf_dict = {i:compose_infl_dict(inflow_df.loc[i,:],i,inflow_type)  for i in inflow_df.index}
    return dwf_dict, inflow_dict



# dividers
divider_types = ('CUTOFF','OVERFLOW','TABULAR','WEIR')
divider_field_vals =  {'Type':{t:t for t in divider_types}}
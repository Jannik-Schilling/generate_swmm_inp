# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:48:56 2021

@author: schilling
"""

import pandas as pd
import numpy as np
from qgis.core import QgsProcessingException


#subcatchments_df = raw_data_dict['subcatchments_raw']
def get_subcatchments_from_shapefile(subcatchments_df, main_infiltration_method):
    '''
    reads subcatchment shapefile
    '''
    if 'kind' in subcatchments_df.columns and 'InfMethod' not in subcatchments_df.columns:
        raise QgsProcessingException('Subcatchments Layer: With version 0.15 the column name for the infiltration method was renamed into "InfMethod" (before: "kind"). Please rename column.')
    def rename_for_infiltation(subc_row, main_infiltration_method):
        """selects and renames different columns according to the columns 'InfMethod'"""
        infiltr_method = subc_row['InfMethod']
        if pd.isna(infiltr_method):
            # take main infiltration method, if not given for subcatchment
            infiltr_method = main_infiltration_method
        if infiltr_method in ['GREEN_AMPT','MODIFIED_GREEN_AMPT']:
            subc_row = subc_row.rename({'SuctHead':'Param1',
                                        'Conductiv':'Param2',
                                        'InitDef':'Param3'})
            subc_row['Param4'] = ''
            subc_row['Param5'] = ''
        if infiltr_method in ['HORTON','MODIFIED_HORTON']:
            subc_row = subc_row.rename({'MaxRate':'Param1', 
                                        'MinRate':'Param2',
                                        'Decay':'Param3',  
                                        'DryTime':'Param4', 
                                        'MaxInf':'Param5'})
        if infiltr_method == 'CURVE_NUMBER':
            subc_row = subc_row.rename({'CurveNum':'Param1',
                                        'Conductiv':'Param2', 
                                        'DryTime':'Param3'})
            subc_row['Param4'] = ''
            subc_row['Param5'] = ''
        if infiltr_method is None:
            subc_row['Param1'] = ''
            subc_row['Param2'] = ''
            subc_row['Param3'] = ''
            subc_row['Param4'] = ''
            subc_row['Param5'] = ''
        return subc_row
    subcatchments_df = subcatchments_df.apply(rename_for_infiltation, 
                                              axis=1, 
                                              args=(main_infiltration_method,))
    subcatchments_df['SnowPack'] = subcatchments_df['SnowPack'].fillna('')
    subcatchments_df['PctRouted'] = subcatchments_df['PctRouted'].fillna(100)
    subcatchments_df = subcatchments_df.reset_index(drop=True)
    return(subcatchments_df)

def create_subcatchm_attributes_from_inp_df(all_subcatchments, all_subareas, all_infiltr, main_infiltration_method):
    infiltr_dtypes = {'InfMethod':'String',
                      'SuctHead':'Double',
                      'Conductiv':'Double',
                      'InitDef':'Double',
                      'MaxRate':'Double',
                      'MinRate':'Double',
                      'Decay':'Double',
                      'DryTime':'Double',
                      'MaxInf':'Double',
                      'CurveNum':'Double'}
    def create_infiltr_df(infiltr_row, main_infilt_method):
        if pd.isna(infiltr_row['InfMethod']):
            infiltr_row['InfMethod'] = main_infilt_method
        if infiltr_row['InfMethod'] in ['GREEN_AMPT','MODIFIED_GREEN_AMPT']:
            infiltr_row = infiltr_row.rename({'Param1':'SuctHead',
                               'Param2':'Conductiv',
                               'Param3':'InitDef'})
            infiltr_row = infiltr_row.drop(['Param4','Param5'])
            cols_not_in_infilt =[k for k in infiltr_dtypes.keys() if k not in infiltr_row.index]# missing columns
            for c in cols_not_in_infilt:
                infiltr_row[c] = np.nan
        if infiltr_row['InfMethod'] in ['HORTON','MODIFIED_HORTON']:
            infiltr_row = infiltr_row.rename({'Param1':'MaxRate',
                                   'Param2':'MinRate',
                                   'Param3':'Decay',
                                   'Param4':'DryTime',
                                   'Param5':'MaxInf'})
            cols_not_in_infilt =[k for k in infiltr_dtypes.keys() if k not in infiltr_row.index]# missing columns
            for c in cols_not_in_infilt:
                infiltr_row[c] = np.nan
        if infiltr_row['InfMethod'] == 'CURVE_NUMBER':
            infiltr_row = infiltr_row.rename({'Param1':'CurveNum',
                               'Param2':'Conductiv',
                               'Param3':'DryTime'})
            infiltr_row = infiltr_row.drop(['Param4','Param5'])
            cols_not_in_infilt =[k for k in infiltr_dtypes.keys() if k not in infiltr_row.index]# missing columns
            for c in cols_not_in_infilt:
                infiltr_row[c] = np.nan
        return infiltr_row
    all_infiltr = all_infiltr.apply(lambda x: create_infiltr_df(x, main_infiltration_method), axis =1)
    all_infiltr = all_infiltr[['Name']+list(infiltr_dtypes.keys())]
    all_infiltr = all_infiltr.dropna(how='all', axis=1)
    infiltr_dtypes = {k:v for k,v in infiltr_dtypes.items() if k in all_infiltr.columns} 
    all_subcatchments = all_subcatchments.join(all_subareas.set_index('Name'), on = 'Name')
    all_subcatchments = all_subcatchments.join(all_infiltr.set_index('Name'), on = 'Name')
    return all_subcatchments, infiltr_dtypes

def rg_position(polyg_dict):
    all_yx = pd.concat([v for k,v in polyg_dict.items()])
    x_mean = np.mean(all_yx['x'])+10
    y_mean = np.mean(all_yx['y'])+10
    return x_mean, y_mean
    
#actually not in use... but this could be used to check if all columns exist:
# subcatchment_columns = pd.DataFrame([['Name',True,''],#Name
 # ['RainGage',False,'Gage1'],
 # ['Outlet',True,''], #Name of Junction
 # ['Area',True,''], # Area
 # ['Imperv',False,100], #Imperviousness
 # ['Width',True,''],    
 # ['Slope',True,''], 
 # ['CurbLen',False,0], 
 # ['SnowPack',False,''], 
 # ['N_Imperv',False,'0.1'], #Mannings-N for impervious area
 # ['N_Perv',False,'0.01'], # Mannings-N for pervious area
 # ['S_Imperv',False,'0.05'], #depth of depression storage on impervious area [mm]
 # ['S_Perv',False,'0.05'], #depth of depression storage on pervious area [mm]
 # ['PctZero',False,'25'], #percent of impervious area with no depression storage
 # ['RouteTo',False,'OUTLET'], #internal routing between pervious an impervious subarea #'OUTLET','IMPERVIOUS','PERVIOUS'
 # ['PctRouted',False,100],#percent of routed between subareas
 # ['Param1',False,3],
 # ['Param2',False,0.5],
 # ['Param3',False,4],
 # ['Param4',False,''],
 # ['Param5',False,'']]
    # , columns =['col_name','oblig','default']) 
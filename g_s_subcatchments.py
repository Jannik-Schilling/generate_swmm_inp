# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:48:56 2021

@author: schilling
"""
import pandas as pd
import os


#subcatchments_df = raw_data_dict['subcatchments_raw']
def get_subcatchments_from_shapefile(subcatchments_df):
    '''reads subcatchment shapefile'''
    def rename_for_infiltation(subc_row):
        """selects and renames different columns according to the columns 'kind'"""
        if subc_row['kind'] == 'MODIFIED_GREEN_AMPT':
            subc_row = subc_row.rename({'SuctHead':'Param1',#mod-green ampt
                                        'Conductiv':'Param2', #mod-green ampt
                                        'InitDef':'Param3'})#mod-green ampt
            subc_row['Param4'] = ''
            subc_row['Param5'] = ''
        if subc_row['kind'] == 'HORTON':
            subc_row = subc_row.rename({'MaxRate':'Param1', 
                                        'MinRate':'Param2', #Horton
                                        'Decay':'Param3',  #Horton
                                        'DryTime':'Param4', #Horton
                                        'MaxInf':'Param5'})#Horton
        return subc_row
    subcatchments_df = subcatchments_df.apply(rename_for_infiltation, axis =1)
    subcatchments_df['SnowPack'] = subcatchments_df['SnowPack'].fillna('')
    subcatchments_df = subcatchments_df[subcatchments_df['Outlet'] != '']
    subcatchments_df = subcatchments_df[subcatchments_df['Outlet'].notna()]
    subcatchments_df = subcatchments_df.reset_index(drop=True)
    return(subcatchments_df)






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
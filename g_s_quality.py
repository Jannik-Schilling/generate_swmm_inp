# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:27:19 2021

@author: schilling
"""
import pandas as pd
import numpy as np

def fill_landuse_params(df,pollutant_names,landuses_names,b_w):
    '''
    fills buildup or washoff data frames
    '''
    missing = []
    for l_n in landuses_names:
        df_sub = df[df['Name'] == l_n]
        if b_w == 'b':
            missing = missing + [[l_n,p_n,'NONE',0,0,0,'AREA'] for p_n in pollutant_names if p_n not in df_sub['Pollutant'].to_list()]
        if b_w == 'w':
            missing = missing + [[l_n,p_n,'NONE',0,0,0,0] for p_n in pollutant_names if p_n not in df_sub['Pollutant'].to_list()]
    missing_df = pd.DataFrame(missing)
    missing_df.columns = df.columns
    return missing_df
    
def get_quality_params_from_table(quality_raw_dict, subcatchments_df = None):
    """generates a dictionary with quality data from an excel file"""
    quality_params = ['POLLUTANTS', 'LANDUSES', 'COVERAGES','LOADINGS']
    for q_p in quality_params:
        q_df_raw = quality_raw_dict[q_p]
        if q_p == 'POLLUTANTS':
            pollutants_df = q_df_raw[['Name', 
                                      'Units', 
                                      'RainConcentr', 
                                      'GwConcentr', 
                                      'IiConcentr',
                                      'DecayCoeff', 
                                      'SnowOnly', 
                                      'CoPollutant',
                                      'CoFraction',
                                      'DwfConcentr', 
                                      'InitConcetr']]
            pollutants_df = pollutants_df[pollutants_df['Name'] != '']
            pollutants_df = pollutants_df[pd.notna(pollutants_df['Name'])]
            pollutant_names = pollutants_df['Name'].to_list() #names of pollutants for fill function
            pollutants_df = pollutants_df.fillna('*')
        if q_p == 'LANDUSES':
            q_df_raw = q_df_raw[q_df_raw['Name'] != ";"]
            landuses_df = q_df_raw[['Name', 'SweepingInterval', 'SweepingFractionAvailable', 'LastSwept']].drop_duplicates()
            landuses_df = landuses_df[pd.notna(landuses_df['Name'])]
            landuses_names = landuses_df['Name'].drop_duplicates().to_list() #names of land uses for fill function
            landuses_df = landuses_df.reset_index(drop=True)
            buildup_df = q_df_raw[['Name', 
                                   'Pollutant',
                                   'BuildupFunction', 
                                   'BuildupMax', 
                                   'BuildupRateConstant',
                                   'BuildupExponent_SatConst', 
                                   'BuildupPerUnit']]
            buildup_df = buildup_df.append(fill_landuse_params(buildup_df,pollutant_names,landuses_names,'b'))
            washoff_df = q_df_raw[['Name', 
                                   'Pollutant',
                                   'WashoffFunction',
                                   'WashoffpCoefficient', 
                                   'WashoffExponenet', 
                                   'WashoffCleaninfEfficiency',
                                   'WashoffBmpEfficiency']]
            washoff_df = washoff_df.append(fill_landuse_params(washoff_df,pollutant_names,landuses_names,'w'))
        if q_p == 'COVERAGES':
            coverages_df = q_df_raw[q_df_raw['Subcatchment']!=';']
            coverages_df = coverages_df[['Subcatchment',
                                         'Landuse',
                                         'Percent']]
            if subcatchments_df is not None: 
                coverages_df = coverages_df[coverages_df['Subcatchment'].isin(subcatchments_df['Name'])]
            else:
                coverages_df = coverages_df[coverages_df['Subcatchment'].isin([])] # if no subcatchments, delete all coverages data
        if q_p == 'LOADINGS':
            loadings_df = q_df_raw
            loadings_df = loadings_df[['Subcatchment',
                                         'Pollutant',
                                         'InitialBuildup']]
    return {'POLLUTANTS':pollutants_df,
            'LANDUSES':landuses_df,
            'BUILDUP':buildup_df,
            'WASHOFF':washoff_df,
            'COVERAGES':coverages_df,
            'LOADINGS':loadings_df}
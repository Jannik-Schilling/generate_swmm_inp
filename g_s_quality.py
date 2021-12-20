# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:27:19 2021

@author: schilling
"""

def get_quality_params_from_table(quality_raw_dict, subcatchments_df = None):
    """generates a dictionary with quality data from an excel file"""
    quality_params = ['POLLUTANTS', 'LANDUSES', 'COVERAGES','LOADINGS']
    #q_p = 'COVERAGES'
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
            pollutants_df = pollutants_df.fillna('*')
        if q_p == 'LANDUSES':
            q_df_raw = q_df_raw[q_df_raw['Name'] != ";"]
            landuses_df = q_df_raw[['Name', 'SweepingInterval', 'SweepingFractionAvailable', 'LastSwept']].drop_duplicates()
            landuses_df = landuses_df.reset_index(drop=True)
            buildup_df = q_df_raw[['Name', 
                                   'Pollutant',
                                   'BuildupFunction', 
                                   'BuildupMax', 
                                   'BuildupRateConstant',
                                   'BuildupExponent_SatConst', 
                                   'BuildupPerUnit']]
            washoff_df = q_df_raw[['Name', 
                                   'Pollutant',
                                   'WashoffFunction',
                                   'WashoffpCoefficient', 
                                   'WashoffExponenet', 
                                   'WashoffCleaninfEfficiency',
                                   'WashoffBmpEfficiency']]
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
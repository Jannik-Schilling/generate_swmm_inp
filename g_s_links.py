# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:56:10 2021

@author: schilling
"""

import pandas as pd

def get_conduits_from_shapefile(conduits_raw):
    """
    prepares conduits data for writing an input file
    removes columns which are not needed, replaces empty values with '' or '*' 
    """
    conduits_df = conduits_raw[['Name',
                               'FromNode',
                               'ToNode',
                               'Length',
                               'Roughness',
                               'InOffset',
                               'OutOffset',
                               'InitFlow',
                               'MaxFlow']].copy()
    conduits_df['InOffset'] = conduits_df['InOffset'].fillna('*')
    conduits_df['OutOffset'] = conduits_df['OutOffset'].fillna('*')
    
    xsections_df = conduits_raw[['Name',
                                'Shape',
                                'Geom1',
                                'Geom2',
                                'Geom3',
                                'Geom4',
                                'Barrels',
                                'Culvert',
                                'Curve',
                                'Tsect']].copy()
    xsections_df['Culvert'] = xsections_df['Culvert'].fillna('')
    xsections_df['Curve'] = xsections_df['Curve'].fillna('')
    xsections_df['Tsect'] = xsections_df['Tsect'].fillna('')
    losses_df = conduits_raw[['Name',
                              'Inlet',
                              'Outlet',
                              'Averge',
                              'FlapGate',
                              'Seepage']].copy()
    return conduits_df, xsections_df, losses_df



def get_weirs_from_shapefile(weirs_raw):
    """prepares weirs data for writing an input file"""
    weirs_df = weirs_raw
    return weirs_df




pumps_columns = pd.DataFrame([['Name',True,''],
 ['FromNode',True,''],
 ['ToNode',True,''], 
 ['PumpCurve',False,'*'], 
 ['Status',False,'OFF'], 
 ['Startup',False,1.75], 
 ['Shutoff',False,0.75]] 
    , columns =['col_name','oblig','default']) 

def get_pumps_from_shapefile(pumps_raw):
    """prepares pumps data for writing an input file"""
    from .g_s_various_functions import check_columns
    pumps_df = pumps_raw.rename(columns={'Curve':'PumpCurve'})
    pumps_df = check_columns(pumps_df.copy(), pumps_columns)
    pumps_df = pumps_df.reset_index(drop=True)
    return pumps_df



# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:56:28 2021

@author: schilling
"""


# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:15:28 2021

@author: schilling
    """
    
import os
#from datetime import datetime, date
import pandas as pd
import numpy as np



os.chdir('C:\\Q_GIS_Projekte\\Projekte\\Testgebiet_SWMM\\generate_swmm_inp') # working directory

readfile = 'C:\Q_GIS_Projekte\Projekte\Testgebiet_SWMM\default\swmm_data\\test_input.inp' #input file
folder_save = 'C:\Q_GIS_Projekte\Projekte\Testgebiet_SWMM\default\eingelesen' #folder to save shapefiles and tables

crs_result = {'init': 'epsg:5650'} # CRS of data in input file
section_list = ['[TITLE]',
                    '[OPTIONS]',
                    '[EVAPORATION]',
                    '[RAINGAGES]',
                    '[SUBCATCHMENTS]',
                    '[SUBAREAS]',
                    '[INFILTRATION]',
                    '[JUNCTIONS]',
                    '[OUTFALLS]',
                    '[STORAGE]',
                    '[CONDUITS]',
                    '[PUMPS]',
                    '[WEIRS]',
                    '[OUTLETS]',
                    '[XSECTIONS]',
                    '[LOSSES]',
                    '[POLLUTANTS]',
                    '[LANDUSES]',
                    '[COVERAGES]',
                    '[LOADINGS]',
                    '[BUILDUP]',
                    '[WASHOFF]',
                    '[INFLOWS]',
                    '[DWF]',
                    '[CURVES]',
                    '[TIMESERIES]',
                    '[PATTERNS]',
                    '[REPORT]',
                    '[COORDINATES]',
                    '[VERTICES]',
                    '[Polygons]',
                    '[SYMBOLS]']

with open(readfile) as f:
    inp_text = f.readlines()

inp_text = [x for x in inp_text if x != '\n']
inp_text = [x for x in inp_text if x != '\s']
inp_text = [x for x in inp_text if not x.startswith(';;')]
inp_text = [x.replace('\n','') for x in inp_text]

section_list = [sect for sect in section_list if sect in inp_text] #remove section which are not available
pos_start_list = [inp_text.index(sect) for sect in section_list] 

section_list = [x.replace('[','') for x in section_list] #remove brackets
section_list = [x.replace(']','') for x in section_list]
pos_end_list = pos_start_list[1:]+[len(inp_text)]
dict_search = {section_list[i]:[pos_start_list[i],pos_end_list[i]] for i in range(len(section_list))}

def text_extract(text_limits):
    return inp_text[text_limits[0]+1:text_limits[1]]
    
dict_raw = {k:text_extract(dict_search[k]) for k in dict_search.keys()}
'''
a= 'CURVES'
text_section = dict_raw[a].copy()
col_names = sections_def_dict[a]
'''
def df_builder(text_section, col_names):
    df = pd.DataFrame()
    df = df.append([row.split() for row in text_section])
    col_len = len(df.columns)
    if col_names == None:
        pass
    else:
        df.columns = col_names[0:col_len]
        if len(col_names) > col_len: #if missing vals in inp-data
            for i in col_names[col_len:]:
                df[i]=np.nan
    return df


sections_def_dict={'TITLE':None,
 'OPTIONS':['Option', 'Value'],
 'EVAPORATION':None,
 'RAINGAGES':None,
 'SUBCATCHMENTS': ['Name', 'RainGage', 'Outlet', 'Area', 'Imperv', 'Width', 'Slope', 'CurbLen', 'SnowPack'], 
 'SUBAREAS':['Name', 'N_Imperv', 'N_Perv', 'S_Imperv', 'S_Perv', 'PctZero', 'RouteTo','PctRouted'],
 'INFILTRATION':['Name','Param1', 'Param2', 'Param3', 'Param4','Param5'],# ['Name','kind', 'SuctHead', 'Conductiv', 'InitDef','LidContr'],
 'JUNCTIONS':['Name', 'Elevation','MaxDepth', 'InitDepth','SurDepth', 'Aponded'],
 'OUTFALLS':['Name', 'Elevation', 'Type', 'Data', 'FlapGate', 'RouteTo'], #Data funktioniert nicht
 'STORAGE':['Name', 'Elevation','MaxDepth','InitDepth','Type', 'Curve','Apond','Fevap','Psi','Ksat','IMD'],
 'CONDUITS': ['Name','FromNode','ToNode','Length','Roughness','InOffset','OutOffset','InitFlow','MaxFlow'],
 'PUMPS':['Name','FromNode','ToNode','PumpCurve','Status','Startup','Shutoff'],
 'WEIRS':['Name','FromNode','ToNode','Type','CrestHeigh','Qcoeff','FlapGate','EndContrac','EndCoeff','Surcharge','RoadWidth','RoadSurf','Coeff_Curve'],
 'OUTLETS':['Name','FromNode','ToNode','InOffset','Rate_Curve','Qcoeff','Qexpon','FlapGate'], #funktioniert nicht wenn qexpon nan ist
 'XSECTIONS':['Name','Shape','Geom1','Geom2','Geom3','Geom4','Barrels','Culvert'],
 'LOSSES': ['Name','Inlet','Outlet','Averge','FlapGate','Seepage'],
 'POLLUTANTS':['Name','Units','RainConcentr','GwConcentr','IiConcentr','DecayCoeff','SnowOnly','CoPollutant','CoFraction','DwfConcentr','InitConcetr'],
 'LANDUSES':['Name', ' SweepingInterval', ' SweepingFractionAvailable', 'LastSwept'],
 'COVERAGES':['Subcatchment','Landuse','Percent'],
 'LOADINGS':['Subcatchment','Pollutant','Buildup'],
 'BUILDUP':['Name','Pollutant','BuildupFunction', 'BuildupMax', 'BuildupRateConstant','BuildupExponent_SatConst','BuildupPerUnit'],
 'WASHOFF':['Name', 'Pollutant','WashoffFunction','WashoffpCoefficient', 'WashoffExponenet', 'WashoffCleaninfEfficiency','WashoffBmpEfficiency'],
 'INFLOWS':['Name','Constituent','Baseline','Baseline_Pattern','Time_Series','Scale_Factor','Type'],
 'DWF':['Name','Constituent','Average_Value','Time_Pattern1','Time_Pattern2','Time_Pattern3','Time_Pattern4'],
 'CURVES':['Name','Type','XVal','YVal'],
 'TIMESERIES':['Name','Date','Time','Value'],
 'PATTERNS':None,
 'REPORT':None,
 'COORDINATES':['Name','X_Coord','Y_Coord'],
 'VERTICES':['Name','X_Coord','Y_Coord'],
 'Polygons':['Name','X_Coord','Y_Coord'],
 'SYMBOLS':['Name','X_Coord','Y_Coord']}

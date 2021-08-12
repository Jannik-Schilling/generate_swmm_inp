# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:56:28 2021

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
 'SYMBOLS':['Name','X_Coord','Y_Coord'],
 'TAGS': None}

with open(readfile) as f:
    inp_text = f.readlines()

inp_text = [x for x in inp_text if x != '\n']
inp_text = [x for x in inp_text if x != '\s']
inp_text = [x for x in inp_text if not x.startswith(';;')]
inp_text = [x.replace('\n','') for x in inp_text]

section_list_brackets = ['['+k+']' for k in sections_def_dict.keys()]
section_list_brackets = [sect for sect in section_list_brackets if sect in inp_text] #remove section which are not available
pos_start_list = [inp_text.index(sect) for sect in section_list_brackets] 

# remove brackets
section_list = [x.replace('[','') for x in section_list_brackets] 
section_list = [x.replace(']','') for x in section_list]

# sort section_list according to occurance of sections in inp_text
section_list = [section_list[i] for i in np.argsort(pos_start_list).tolist()]  

# sort startpoints of sections in inp_text
pos_start_list = sorted(pos_start_list)

# endpoints of sections in inp_text
pos_end_list = pos_start_list[1:]+[len(inp_text)]

# make a dict of sections to extract
dict_search = {section_list[i]:[pos_start_list[i],pos_end_list[i]] for i in range(len(section_list))}


def text_extract(text_limits):
    '''extracts sections from inp_text'''
    return inp_text[text_limits[0]+1:text_limits[1]]
    
dict_raw = {k:text_extract(dict_search[k]) for k in dict_search.keys()}

'''
k= 'PATTERNS'
text_section = dict_raw[k].copy()
col_names = sections_def_dict[k]
'''


def df_builder(text_section, col_names, k):
    '''builds dataframes from strings in dict_raw'''
    text_section = [x for x in text_section if not x.startswith(';')]
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


dict_sections = dict()
for k in section_list:
    dict_sections[k] = df_builder(dict_raw[k].copy(), sections_def_dict[k], k)



### Excel files
 
# options    
dict_sections['OPTIONS'].to_excel(os.path.join(folder_save,'gisswmm_options.xlsx'),
             sheet_name='gisswmm_options',
             index = False)
dict_sections['OPTIONS'] = 'written'

# inflows
with pd.ExcelWriter(os.path.join(folder_save,'gisswmm_inflows.xlsx')) as writer:
    if not 'INFLOWS' in dict_sections.keys():
        dict_sections['INFLOWS'] = pd.DataFrame(columns = sections_def_dict['INFLOWS'])
    dict_sections['INFLOWS'].to_excel(writer,
                 sheet_name='Direct',
                 index = False)
    dict_sections['INFLOWS'] = 'written'
    if not 'DWF' in dict_sections.keys():
        dict_sections['DWF'] = pd.DataFrame(columns = sections_def_dict['DWF'])
    dict_sections['DWF'].to_excel(writer,
                 sheet_name='Dry_Weather',
                 index = False)
    dict_sections['DWF'] = 'written'


# patterns
pattern_times={'HOURLY':['0:00','1:00','2:00','3:00','4:00','5:00','6:00','7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'],
 'DAILY':['So','Mo','Tu','We','Th','Fr','Sa'],
 'MONTHLY':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
 'WEEKEND':['0:00','1:00','2:00','3:00','4:00','5:00','6:00','7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']
 }
pattern_cols={'HOURLY':['Name','Time','Factor'],
              'DAILY':['Name','Day','Factor'],
              'MONTHLY':['Name','Month','Factor'],
              'WEEKEND':['Name','Time','Factor']}
all_patterns = dict_sections['PATTERNS'].copy()
occuring_patterns_types = all_patterns.loc[all_patterns[1].isin(['HOURLY','DAILY','MONTHLY','WEEKEND']),[0,1]].set_index(0)
occuring_patterns_types.columns = ["PatternType"]
all_patterns = all_patterns.fillna(np.nan)
all_patterns = all_patterns.replace({'HOURLY':np.nan,'DAILY':np.nan,'MONTHLY':np.nan,'WEEKEND':np.nan})
def adjust_patterns_df(pattern_row):
    pattern_adjusted = [[pattern_row[0],i] for i in pattern_row[1:] if pd.notna(i)]
    return (pd.DataFrame(pattern_adjusted, columns = ['Name','Factor']))
all_patterns = pd.concat([adjust_patterns_df(all_patterns.loc[i,:]) for i in all_patterns.index])
all_patterns = all_patterns.join(occuring_patterns_types, on = 'Name')
all_patterns = {k:v.iloc[:,:-1] for k, v in all_patterns.groupby("PatternType")}
def add_pattern_timesteps(pattern_type):
    count_patterns = int(len(all_patterns[pattern_type])/len(pattern_times[pattern_type]))
    new_col = pattern_times[pattern_type]*count_patterns
    return new_col
for pattern_type in all_patterns.keys():
    all_patterns[pattern_type]['Time'] = add_pattern_timesteps(pattern_type)
    all_patterns[pattern_type] = all_patterns[pattern_type][['Name','Time','Factor']]
    if pattern_type == 'DAILY':
        all_patterns[pattern_type] = all_patterns[pattern_type].rename({'Time':'Day'})
    if pattern_type == 'MONTHLY':
        all_patterns[pattern_type] = all_patterns[pattern_type].rename({'Time':'Month'})
    all_patterns[pattern_type]['Factor'] = [float(x) for x in all_patterns[pattern_type]['Factor']]
with pd.ExcelWriter(os.path.join(folder_save,'gisswmm_patterns.xlsx')) as writer:
    for pattern_type in pattern_times.keys():
        if not pattern_type in all_patterns.keys():
            df = pd.DataFrame(columns=pattern_cols[pattern_type])
        else:
            df = all_patterns[pattern_type]
        df.to_excel(writer, sheet_name=pattern_type,index = False)
dict_sections['PATTERNS'] = 'written'
# quality

# curves section
def adjust_curve_columns(curve_point):
    if curve_point['Type'] in ['STORAGE','Pump1','Pump2','Pump3','Pump4','Rating','Weir']:
        return curve_point
    else:
        curve_point['YVal'] = curve_point['XVal']
        curve_point['XVal'] = curve_point['Type']
        curve_point['Type'] = np.nan
        return curve_point
dict_sections['CURVES'] = dict_sections['CURVES'].apply(adjust_curve_columns, axis = 1)
curve_type_dict= {dict_sections['CURVES'].loc[x,'Name']:dict_sections['CURVES'].loc[x,'Type'] for x in dict_sections['CURVES'][pd.notna(dict_sections['CURVES']['Type'])].index}
all_curves = dict_sections['CURVES'].join(pd.DataFrame.from_dict(curve_type_dict, orient = 'index',columns=['CurveType']), on = 'Name')
all_curves = {k:v[['Name','XVal','YVal']] for k, v in all_curves.groupby('CurveType')}

curve_cols_dict = {'Pump1': ['Name','Volume','Flow'],
                   'Pump2': ['Name','Depth','Flow'],
                   'Pump3': ['Name','Head','Flow'],
                   'Pump4': ['Name','Depth','Flow'],
                   'STORAGE': ['Name','Depth','Area'],
                   'Rating': ['Name','Head/Depth','Outflow'],
                   'Weir': ['Name','Head','Coefficient']}
for curve_type in all_curves.keys():
    all_curves[curve_type].columns = curve_cols_dict[curve_type]
    all_curves[curve_type]['Notes']=np.nan
with pd.ExcelWriter(os.path.join(folder_save,'gisswmm_curves.xlsx')) as writer:
    for curve_type in all_curves.keys():
        df = all_curves[curve_type]
        df.iloc[:,1] = [float(x) for x in df.iloc[:,1]]
        df.iloc[:,2] = [float(x) for x in df.iloc[:,2]]
        df.to_excel(writer, sheet_name=curve_type,index = False)
dict_sections['CURVES'] = 'written'

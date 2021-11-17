# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:56:10 2021

@author: schilling
"""

import pandas as pd
from qgis.core import QgsProcessingException

def get_conduits_from_shapefile(conduits_raw):
    """
    prepares conduits data for writing an input file
    removes columns which are not needed, replaces empty values with '' or '*' 
    :param pd.DataFrame conduits_raw
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
    # Asteriscs indicate that InOffset or OutOffset is the same as node elevation: 
    conduits_df['InOffset'] = conduits_df['InOffset'].fillna('*')
    conduits_df['OutOffset'] = conduits_df['OutOffset'].fillna('*')
    
    xsections_df = conduits_raw[['Name',
                                'Shape',
                                'Geom1',
                                'Geom2',
                                'Geom3',
                                'Geom4',
                                'Barrels',
                                'Culvert']].copy()
    xsections_df['Culvert'] = xsections_df['Culvert'].fillna('')
    if any(xsections_df['Shape'] == 'IRREGULAR') or any(xsections_df['Shape'] == 'CUSTOM'):
        if 'Shp_Trnsct' not in conduits_raw.columns:
            raise QgsProcessingException('Column "Shp_Trnsct is missing for IRREGULAR or CUSTOM Shape')
        else:
            xsections_df.loc[xsections_df['Shape'] == 'IRREGULAR', 'Geom1'] = conduits_raw.loc[xsections_df['Shape'] == 'IRREGULAR','Shp_Trnsct']
            xsections_df.loc[xsections_df['Shape'] == 'CUSTOM', 'Geom2'] = conduits_raw.loc[xsections_df['Shape'] == 'CUSTOM','Shp_Trnsct']
    if 'Inlet' in conduits_raw.columns and 'Kentry' not in conduits_raw.columns:
        raise QgsProcessingException('Conduits Layer: With version 0.14 the column name for the Entry Loss Coeff. was renamed into "Kentry" (before: "Inlet"')
    if 'Outlet' in conduits_raw.columns and 'Kexit' not in conduits_raw.columns:
        raise QgsProcessingException('Conduits Layer: With version 0.14 the column name for the Exit Loss Coeff. was renamed into "Kexit" (before: "Outlet"')
    if 'Averge' in conduits_raw.columns and 'Kavg' not in conduits_raw.columns:
        raise QgsProcessingException('Conduits Layer: With version 0.14 the column name for the Avg. Loss Coeff. was renamed into "Kavg" (before: "Average"')
    losses_df = conduits_raw[['Name',
                              'Kentry',
                              'Kexit',
                              'Kavg',
                              'FlapGate',
                              'Seepage']].copy()
    losses_df['Seepage'] = losses_df['Seepage'].fillna('0')
    losses_df['Kentry'] = losses_df['Kentry'].fillna('0')
    losses_df['Kexit'] = losses_df['Kexit'].fillna('0')
    losses_df['Kavg'] = losses_df['Kavg'].fillna('0')
    return conduits_df, xsections_df, losses_df

def del_first_last_vt(link):
    """
    deletes first and last vertex as it is already in nodes coordinates
    :param list link
    """
    return link[1:-1]

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
    pumps_df = check_columns(pumps_raw.copy(), pumps_columns)
    pumps_df = pumps_df.reset_index(drop=True)
    return pumps_df



def get_weirs_from_shapefile(weirs_raw):
    #from .g_s_defaults import def_sections_dict
    """prepares weirs data for writing an input file"""
    weirs_raw = weirs_raw.rename(columns={'Height':'Geom1',
                                         'Length':'Geom2',
                                         'SideSlope':'Geom3'})
    weirs_df = weirs_raw.copy()
    weirs_df['CrestHeigh'] = weirs_df['CrestHeigh'].fillna('*')
    weirs_df['RoadWidth'] = weirs_df['RoadWidth'].fillna('*')
    weirs_df['RoadSurf'] = weirs_df['RoadSurf'].fillna('*')
    weirs_df['Coeff_Curv'] = weirs_df['Coeff_Curv'].fillna('')
    weirs_df['EndContrac'] = weirs_df['EndContrac'].fillna('0')
    weirs_df['EndCoeff'] = weirs_df['EndCoeff'].fillna('0')
    weirs_df=weirs_df[['Name',
                       'FromNode',
                       'ToNode',
                       'Type',
                       'CrestHeigh',
                       'Qcoeff',
                       'FlapGate',
                       'EndContrac',
                       'EndCoeff',
                       'Surcharge',
                       'RoadWidth',
                       'RoadSurf',
                       'Coeff_Curv']]
    shape_dict = {'TRANSVERSE':'RECT_OPEN',
     'SIDEFLOW':'RECT_OPEN',
     'V-NOTCH':'TRIANGULAR',
     'TRAPEZOIDAL':'TRAPEZOIDAL',
     'ROADWAY':'RECT_OPEN'}
    weirs_raw['Shape'] = [shape_dict[x] for x in weirs_raw['Type']]
    weirs_raw['Geom3'] = weirs_raw['Geom3'].fillna('0')
    weirs_raw['Geom4'] = weirs_raw['Geom3']
    xsections_df = weirs_raw[['Name',
                                'Shape',
                                'Geom1',
                                'Geom2',
                                'Geom3',
                                'Geom4']].copy()
    xsections_df['Barrels'] = ''
    xsections_df['Culvert'] = ''
    return weirs_df, xsections_df


def get_orifices_from_shapefile(orifices_raw):
    """
    prepares orifices data for writing an input file
    param: pd.DataFrame orifices_raw
    """
    from .g_s_defaults import def_sections_dict
    orifices_attrs = list(def_sections_dict['ORIFICES'].keys())
    orifices_df = orifices_raw.copy()
    orifices_df['InOffset'] = orifices_df['InOffset'].fillna('*')
    orifices_df = orifices_df[orifices_attrs]
    orifices_raw['Geom1'] = orifices_raw['Height']
    orifices_raw['Geom2'] = orifices_raw['Width']
    orifices_raw['Geom2'] = orifices_raw['Geom2'].fillna('0')
    orifices_raw['Geom3'] = 0
    orifices_raw['Geom4'] = 0
    xsections_df = orifices_raw[['Name',
                                'Shape',
                                'Geom1',
                                'Geom2',
                                'Geom3',
                                'Geom4']].copy()
    return orifices_df, xsections_df

def get_outlets_from_shapefile(outlets_raw):
    """prepares outlets data for writing an input file"""
    def get_outl_curve(outl_row):
        """selects curve data according to rating curve type"""
        if outl_row['Rate_Curve'] in ['FUNCTIONAL/DEPTH', 'FUNCTIONAL/HEAD']:
            return outl_row['Qcoeff']
        else:
            return outl_row['CurveName']
    outlets_raw['QCurve'] = [get_outl_curve(outlets_raw.loc[i]) for i in outlets_raw.index] 
    outlets_df = outlets_raw[['Name', 
                             'FromNode',
                             'ToNode', 
                             'InOffset', 
                             'Rate_Curve', 
                             'QCurve',
                             'Qexpon', 
                             'FlapGate']]
    return outlets_df 
    
# transects_raw = raw_data_dict['transects'].copy()
def get_transects_from_table(transects_raw):
    """writes strings for transects"""
    tr_data = transects_raw['Data']
    tr_vals = transects_raw['XSections']
    def write_transect_lines (T_Name):
        tr_data_i = tr_data[tr_data['TransectName'] == T_Name] 
        tr_vals_i = tr_vals[tr_vals['TransectName'] == T_Name]
        tr_count_i = len(tr_vals_i)
        tr_roughn_i = tr_data_i[['RoughnessLeftBank', 'RoughnessRightBank', 'RoughnessChannel']].values.tolist()[0]
        tr_bank_i = tr_data_i[['BankStationLeft','BankStationRight']].values.tolist()[0]
        tr_modifier_i = tr_data_i[['ModifierMeander','ModifierStations', 'ModifierElevations']].values.tolist()[0]
        NC_data_i = ['NC']+tr_roughn_i
        NC_string_i = '    '.join([str(i) for i in NC_data_i])
        X1_data_i = ['X1', T_Name, '', tr_count_i]+tr_bank_i+[0.0,0.0]+tr_modifier_i
        X1_string_i = '    '.join([str(i) for i in X1_data_i])
        tr_vals_i_list = [tr_vals_i.loc[i,['Elevation','Station']].to_list() for i in tr_vals_i.index]
        tr_vals_i_list = [str(x) for sublist in tr_vals_i_list for x in sublist]
        tr_vals_i_list_splitted = [tr_vals_i_list[i:i + 10] for i in range(0, len(tr_vals_i_list), 10)]
        tr_vals_i_list_splitted = [['GR']+x for x in tr_vals_i_list_splitted]
        def concat_tr_str(tr_line):
            return'    '.join([str(i) for i in tr_line])
        GR_strings_i = [concat_tr_str(x) for x in tr_vals_i_list_splitted]
        GR_strings_i_joined = '\n'.join(GR_strings_i)
        tr_string = NC_string_i+'\n'+X1_string_i+'\n'+GR_strings_i_joined
        return tr_string
    transects_string_list = [write_transect_lines(x) for x in tr_data['TransectName']]
    return transects_string_list
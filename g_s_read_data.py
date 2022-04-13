# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:42:33 2021

@author: schilling
"""
import pandas as pd
import os
import numpy as np
from qgis.core import (NULL,
                       QgsProcessingException)

def read_shapefiles_direct(file_outfalls,
                       file_storages,
                       file_subcatchments,
                       file_conduits,
                       file_junctions,
                       file_pumps,
                       file_weirs,
                       file_orifices,
                       file_outlets,
                       file_dividers):
    """reads shapefiles from swmm model"""
    data_dict = dict()
    def del_none_bool(df):
        """
        replaces None or NULL with np.nan
        replaces True and False with 'YES' and 'NO'
        ...except of geometry column
        """
        df[df.columns[:-1]] =  df[df.columns[:-1]].fillna(value=np.nan)
        def replace_null_nan(atrr_value):
            if atrr_value == NULL:
                return np.nan
            else:
                return atrr_value
        df = df.applymap(replace_null_nan)
        df[df.columns[:-1]] =  df[df.columns[:-1]].replace('True','YES').replace('False','NO')
        return df
    def load_shapefile_to_df(vlayer):
        """reads shapefile attributes and geometries"""
        cols = [f.name() for f in vlayer.fields()]
        # check for null geometries
        if any(not(f.hasGeometry()) for f in vlayer.getFeatures()):
            name_missing_geom = [f['Name'] for f in vlayer.getFeatures() if not(f.hasGeometry())]
            raise QgsProcessingException('Failed to load layer: missing geometries in '+vlayer.name()+': '+', '.join(name_missing_geom))
        datagen = ([f[col] for col in cols]+[f.geometry()] for f in vlayer.getFeatures())
        df = pd.DataFrame.from_records(data=datagen, columns=cols+['geometry'])
        return df
        
    if file_outfalls is not None:
        data_dict['outfalls_raw'] = load_shapefile_to_df(file_outfalls)
    
    if file_storages is not None:
        data_dict['storages_raw'] = load_shapefile_to_df(file_storages)
    
    if file_subcatchments is not None:
        data_dict['subcatchments_raw'] = load_shapefile_to_df(file_subcatchments)
    
    if file_conduits is not None:
        data_dict['conduits_raw'] = load_shapefile_to_df(file_conduits)
    
    if file_junctions is not None:
        data_dict['junctions_raw'] = load_shapefile_to_df(file_junctions)
    
    if file_pumps is not None:
        data_dict['pumps_raw'] = load_shapefile_to_df(file_pumps)
    
    if file_outlets is not None:
        data_dict['outlets_raw'] = load_shapefile_to_df(file_outlets)
    
    if file_orifices is not None:
        data_dict['orifices_raw'] = load_shapefile_to_df(file_orifices)
    
    if file_weirs is not None:
        data_dict['weirs_raw'] = load_shapefile_to_df(file_weirs)
    
    if file_dividers is not None:
        data_dict['dividers_raw'] = load_shapefile_to_df(file_dividers)
    data_dict = {key_i:del_none_bool(data_dict[key_i]) for key_i in data_dict.keys()}
    return data_dict



    
def read_data_from_table_direct(file, sheet=0): 
    '''reads curves or other tables from excel or csv'''
    filename, file_extension = os.path.splitext(file)
    if file_extension == '.xlsx' or file_extension == '.xls' or file_extension == '.ods':
        if sheet == 0:
            data_df = pd.read_excel(file,sheet_name = sheet)
        else:
            #print ('sheet not 0')
            if sheet in pd.ExcelFile(file).sheet_names:
                data_df = pd.read_excel(file,sheet_name = sheet)
            elif str(sheet).upper() in pd.ExcelFile(file).sheet_names:
                data_df = pd.read_excel(file,sheet_name = str(sheet).upper())
            elif str(sheet).lower() in pd.ExcelFile(file).sheet_names:
                data_df = pd.read_excel(file,sheet_name = str(sheet).lower())
            elif str(sheet).capitalize() in pd.ExcelFile(file).sheet_names:
                data_df = pd.read_excel(file,sheet_name = str(sheet).capitalize())
            else:
                data_df = pd.DataFrame()
    if file_extension == '.csv':
        data_df = pd.read_csv(file)
    return data_df

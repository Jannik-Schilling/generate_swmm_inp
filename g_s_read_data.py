# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:42:33 2021

@author: schilling
"""
import pandas as pd
import os
import numpy as np
from qgis.core import (QgsVectorLayer, NULL)


def read_shapefiles(data_dir,
                       file_outfalls,
                       file_storages,
                       file_subcatchments,
                       file_conduits,
                       file_junctions,
                       file_pumps,
                       file_weirs,
                       file_outlets):
    """reads shapefiles from swmm model"""
    data_dict = dict()
    def del_none_bool(df):
        """
        replaces None or NULL with np.nan
        replaces True and False with 'YES' and 'NO'
        ...except of geometry column
        """
        df[df.columns[:-1]] =  df[df.columns[:-1]].fillna(value=np.nan)
        df[df.columns[:-1]] =  df[df.columns[:-1]].replace(NULL,np.nan)
        df[df.columns[:-1]] =  df[df.columns[:-1]].replace('True','YES').replace('False','NO')
        return df
        
    def load_shapefile_to_df(data_file):
        """reads shapefile attributes and geometries"""
        vlayer = QgsVectorLayer(data_file,'temp','ogr')
        cols = [f.name() for f in vlayer.fields()]
        datagen = ([f[col] for col in cols]+[f.geometry()] for f in vlayer.getFeatures())
        df = pd.DataFrame.from_records(data=datagen, columns=cols+['geometry'])
        return df
        
    if file_outfalls is None:
        pass 
    else:
        data_dict['outfalls_raw'] = load_shapefile_to_df(os.path.join(data_dir,file_outfalls))
    
    if file_storages is None:
        pass 
    else:
        data_dict['storages_raw'] = load_shapefile_to_df(os.path.join(data_dir,file_storages))
    
    if file_subcatchments is None:
        pass 
    else:
        data_dict['subcatchments_raw'] = load_shapefile_to_df(os.path.join(data_dir,file_subcatchments))
    
    if file_conduits is None:
        pass 
    else:
        data_dict['conduits_raw'] = load_shapefile_to_df(os.path.join(data_dir,file_conduits))
    
    if file_junctions is None:
        pass 
    else:
        data_dict['junctions_raw'] = load_shapefile_to_df(os.path.join(data_dir,file_junctions))
    
    if file_pumps is None:
        pass 
    else:
        data_dict['pumps_raw'] = load_shapefile_to_df(os.path.join(data_dir,file_pumps))
    
    if file_outlets is None:
        pass 
    else:
        data_dict['outlets_raw'] = load_shapefile_to_df(os.path.join(data_dir,file_outlets))

        
    if file_weirs is None:
        pass 
    else:   
        data_dict['weirs_raw'] = load_shapefile_to_df(os.path.join(data_dir,file_weirs))
    data_dict = {key_i:del_none_bool(data_dict[key_i]) for key_i in data_dict.keys()}
    return data_dict





def read_data_from_table(data_dir,
                         file, sheet=0): 
    '''reads curves or other tables from excel or csv'''
    filename, file_extension = os.path.splitext(file)
    if file_extension == '.xlsx':
        data_df = pd.read_excel(os.path.join(data_dir,file),sheet_name = sheet)
    if file_extension == '.csv':
        data_df = pd.read_csv(os.path.join(data_dir,file))
    return data_df
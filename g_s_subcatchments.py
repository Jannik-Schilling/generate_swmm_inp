# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GenerateSwmmInp
                                 A QGIS plugin
 This plugin generates SWMM Input files
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-09
        copyright            : (C) 2021 by Jannik Schilling
        email                : jannik.schilling@posteo.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Jannik Schilling'
__date__ = '2023-05-09'
__copyright__ = '(C) 2021 by Jannik Schilling'


import pandas as pd
import numpy as np
from qgis.core import (
    NULL,
    QgsGeometry
)
from .g_s_defaults import (
    def_infiltration_types,
    def_qgis_fields_dict,
    def_sections_dict
)


# Export
# Subcatchments
def get_subcatchments_from_layer(
        subcatchments_df,
        export_params
    ):
    """
    reads subcatchment layer
    :param pd.DataFrame subcatchments_df
    :param dict export_params
    :return: tuple (four pd.DataFrames)
    """
    main_infiltration_method = export_params['main_infiltration_method']

    def rename_for_infiltation(subc_row, main_infiltration_method):
        """
        selects and renames different columns
        according to the columns 'InfMethod'
        """
        infiltr_method = subc_row['InfMethod']
        if pd.isna(infiltr_method):
            # take main infiltration method, if not given for subcatchment
            infiltr_method = main_infiltration_method
        if infiltr_method in ['GREEN_AMPT', 'MODIFIED_GREEN_AMPT']:
            subc_row = subc_row.rename({
                'SuctHead': 'Param1',
                'Conductiv': 'Param2',
                'InitDef': 'Param3'
            })
            subc_row['Param4'] = ''
            subc_row['Param5'] = ''
        if infiltr_method in ['HORTON', 'MODIFIED_HORTON']:
            subc_row = subc_row.rename({
                'MaxRate': 'Param1',
                'MinRate': 'Param2',
                'Decay': 'Param3',
                'DryTime': 'Param4',
                'MaxInf': 'Param5'
            })
        if infiltr_method == 'CURVE_NUMBER':
            subc_row = subc_row.rename({
                'CurveNum': 'Param1',
                'Conductiv': 'Param2',
                'DryTime': 'Param3'
            })
            subc_row['Param4'] = ''
            subc_row['Param5'] = ''
        if infiltr_method is None:
            subc_row['Param1'] = ''
            subc_row['Param2'] = ''
            subc_row['Param3'] = ''
            subc_row['Param4'] = ''
            subc_row['Param5'] = ''
        return subc_row
    subcatchments_df = subcatchments_df.apply(
        rename_for_infiltation,
        axis=1,
        args=(main_infiltration_method, )
    )
    subcatchments_df['CurbLen'] = subcatchments_df['CurbLen'].fillna('0')
    subcatchments_df['SnowPack'] = subcatchments_df['SnowPack'].fillna('')
    subcatchments_df['PctRouted'] = subcatchments_df['PctRouted'].fillna(100)
    subcatchments_df = subcatchments_df.reset_index(drop=True)
    # select columns
    infiltration_df = subcatchments_df[def_sections_dict['INFILTRATION']]
    subareas_df = subcatchments_df[def_sections_dict['SUBAREAS']]
    subcatchments_df = subcatchments_df[def_sections_dict['SUBCATCHMENTS']]
    export_params['all_subcatchments'] = list(subcatchments_df['Name'])
    return subcatchments_df, subareas_df, infiltration_df

# import
# infiltration
def prepare_infiltration_inp_lines(
    inp_line,
    main_infiltration_method='HORTON',
    **kwargs
):
    """
    adjusts the line length in the infiltration section
    """
    if inp_line[-1] in def_infiltration_types:
        current_infiltration_method = inp_line[-1]
        inp_line = inp_line[:-1]
    else:
        current_infiltration_method = main_infiltration_method
    if len(inp_line) == 4:
        # fill non-HORTON or missing values
        inp_line = inp_line+[np.nan, np.nan]
    if len(inp_line) == 5:
        # fill missing values
        inp_line = inp_line+[np.nan]
    inp_line = inp_line+[current_infiltration_method]
    return inp_line


# infiltration
InfiltrDtypes = [
    'InfMethod',
    'SuctHead',
    'Conductiv',
    'InitDef',
    'MaxRate',
    'MinRate',
    'Decay',
    'DryTime',
    'MaxInf',
    'CurveNum'
]
   
def create_infiltr_df(infiltr_row):
    """
    creates a pd.DataFrame for infiltration values
    :param pd.Series infiltr_row
    """
    if infiltr_row['InfMethod'] in ['GREEN_AMPT', 'MODIFIED_GREEN_AMPT']:
        infiltr_row = infiltr_row.rename({
            'Param1': 'SuctHead',
            'Param2': 'Conductiv',
            'Param3': 'InitDef'
        })
        infiltr_row = infiltr_row.drop(['Param4', 'Param5'])
        cols_not_in_infilt = [k for k in InfiltrDtypes if k not in infiltr_row.index]  # missing columns
        for c in cols_not_in_infilt:
            infiltr_row[c] = np.nan
    if infiltr_row['InfMethod'] in ['HORTON', 'MODIFIED_HORTON']:
        infiltr_row = infiltr_row.rename({
            'Param1': 'MaxRate',
            'Param2': 'MinRate',
            'Param3': 'Decay',
            'Param4': 'DryTime',
            'Param5': 'MaxInf'
        })
        cols_not_in_infilt = [k for k in InfiltrDtypes if k not in infiltr_row.index]  # missing columns
        for c in cols_not_in_infilt:
            infiltr_row[c] = np.nan
    if infiltr_row['InfMethod'] == 'CURVE_NUMBER':
        infiltr_row = infiltr_row.rename({
            'Param1': 'CurveNum',
            'Param2': 'Conductiv',
            'Param3': 'DryTime'
        })
        infiltr_row = infiltr_row.drop(['Param4', 'Param5'])
        cols_not_in_infilt = [k for k in InfiltrDtypes if k not in infiltr_row.index]  # missing columns
        for c in cols_not_in_infilt:
            infiltr_row[c] = np.nan
    return infiltr_row

# geometries
def get_polygon_from_verts(polyg_name, dict_all_vals):
    """
    creates polygon geometries from vertices
    :param str polyg_name
    :param dict_all_vals
    :returns: list
    """
    all_polygons = dict_all_vals['POLYGONS']['data']
    verts = all_polygons.copy()[all_polygons.index == polyg_name]
    verts = verts.reset_index(drop=True)
    if len(verts) == 0: # no geometry given
        polyg_geom = NULL
    elif len(verts) < 3:  # only 1 or 2 vertices
        # set geometry to buffer around first vertice
        verts_points = [x.asPoint() for x in verts]
        polyg_geom = QgsGeometry.fromPointXY(verts_points[0]).buffer(5, 5)
    else:
        polyg_geom = QgsGeometry.fromPolygonXY(
            [[x.asPoint() for x in verts['geometry']]] 
        )
    return [polyg_name, polyg_geom]

def create_polygons_df(df_processed, dict_all_vals, feedback):
    """
    converts a point x-y-list into POINT-df
    :param pd.DataFrame df_processed
    :param dict dict_all_vals
    :param QgsProcessingFeedback feedback
    :return: pd.DataFrame
    """
    #polygons_created = [
    #    get_polygon_from_verts(n, dict_all_vals) for n in df_processed['Name']
    #]
    polygons_created = []
    len_itms = len(df_processed['Name'])
    for i, n in enumerate(df_processed['Name']):
        if feedback.isCanceled():
            break
        polygons_created = polygons_created + [get_polygon_from_verts(n, dict_all_vals)]
        feedback.setProgress((i+1)/len_itms*95)
    polygons_created = pd.DataFrame(
        polygons_created,
        columns=['Name', 'geometry']
    ).set_index('Name')
    feedback.setProgress(100)
    return polygons_created

# import of rain gages
def get_raingages_from_inp(rg_line, feedback):
    """
    prepares a list of raingage values in the correct order from an inp line
    :param list rg_line
    :return list
    """
    if rg_line[4] == 'TIMESERIES':
        rg_source = {
            'DataSource': 'TIMESERIES',
            'SeriesName': rg_line[5],
            'FileName': np.nan,
            'StationID': np.nan,
            'RainUnits': np.nan
        }
    else:  # FILE
        rg_source = {
            'DataSource': 'FILE',
            'SeriesName': np.nan,
            'FileName': rg_line[5],
            'StationID': rg_line[6],
            'RainUnits': rg_line[7]
        }
    interval_split = str(rg_line[2]).split(':')  # Interval splitted in HH:mm
    if len(interval_split) == 1:
        interval_split = interval_split + ['00']  # if only hours
    if len(interval_split[0]) == 1:
        interval_split[0] = '0' + interval_split[0]  # if one digit hour
    interval = interval_split[0] + ':' + interval_split[1]
    rg_list = [
        rg_line[0],  # Name
        rg_line[1],  # Format
        interval,
        rg_line[3]  # SCF
    ] + list(rg_source.values())
    return rg_list

# export of rain gages
def get_raingage_from_qgis_row(rg_row):
    """
    adjusts columns in a row from a QGIS raingage layer
    :param pd.series rg_row
    """
    if rg_row['DataSource'] == 'TIMESERIES':
        rg_row['SourceName'] = rg_row['SeriesName']
        rg_row['StationID'] = ''
        rg_row['RainUnits'] = ''
    else:  # FILE
        rg_row['SourceName'] = rg_row['FileName']
    # unused columns (FileName and SeriesName) are deleted later on
    return rg_row

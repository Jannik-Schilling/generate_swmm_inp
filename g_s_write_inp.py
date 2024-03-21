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

import os
import pandas as pd

inflow_keys_dict = {
    'DWF':['Name','Baseline','Patterns'],
    'INFLOWS':[
        'Name',
        'Time_Series',
        'Type',
        'Mfactor',
        'Sfactor',
        'Baseline',
        'Pattern'
    ]
}

def write_inp(
    inp_file_name,
    project_dir,
    inp_dict,
    feedback
):
    """
    This script writes the data in inp_dict into a text file
    :param str inp_file_name
    :param str project_dir
    :param dict inp_dict
    :param QgsProcessingFeedback feedback 
    """

    # write input file
    file_path = os.path.join(project_dir, inp_file_name) 
    file1 = open(file_path, 'w')

    # function to write      
    def df_to_inp_section(section_name, only_cols=None):
        """
        writes a input file section from pd.Dataframe to file1
        :param str section_name
        :param list only_cols
        """
        if section_name in inp_dict.keys():
            feedback.setProgressText('writing ['+section_name+']...')
            print_df = inp_dict[section_name]['data']
            if 'annotations' in inp_dict[section_name].keys():
                annotations_dict = inp_dict[section_name]['annotations']
                if len(annotations_dict) > 0:
                    annotations_df = pd.DataFrame.from_dict(
                        annotations_dict, 
                        orient='index',
                        columns=['Name']
                    )
                    annotations_df['Name'] = [';'+str(i) for i in annotations_df['Name']]
                    # prepare indices for insertion
                    replace_index = [k-0.5 for k in print_df.index if print_df.loc[k, 'Name'] in annotations_df.index]
                    annotations_df.index = replace_index
                    missing_cols = print_df.columns.drop('Name')
                    annotations_df[missing_cols] = ''
                    print_df = pd.concat(
                        [print_df, annotations_df]
                    )
                    print_df = print_df.sort_index(ascending=True)
            if only_cols is not None:
                print_df = print_df[only_cols]
            file1.write('['+section_name+']\n')
            file1.write(print_df.to_string(header=False, index=False))
            file1.write('\n')
            file1.write('\n')   

    # header
    df_to_inp_section('TITLE')
    df_to_inp_section('OPTIONS')

    # raingages
    df_to_inp_section('RAINGAGES')

    # subcatchments
    df_to_inp_section('SUBCATCHMENTS')
    df_to_inp_section('SUBAREAS')
    df_to_inp_section('INFILTRATION')

    # nodes
    df_to_inp_section('JUNCTIONS')

    # outfalls
    if 'OUTFALLS' in inp_dict.keys():
        feedback.setProgressText('writing [OUTFALLS]...')
        outfalls_df = inp_dict['OUTFALLS']['data']
        file1.write('[OUTFALLS]\n')
        for i in range(len(outfalls_df)):
            outl =  outfalls_df.loc[i, :]
            file1.write(str(outl['Name'])+'    '+
                        str(outl['Elevation'])+'    '+
                        str(outl['Type'])+'    '+
                        str(outl['Data'])+'    '+
                        str(outl['FlapGate'])+'    '+
                        str(outl['RouteTo']))
            file1.write('\n')
        file1.write('\n')

    # dividers
    if 'DIVIDERS' in inp_dict.keys():
        feedback.setProgressText('writing [DIVIDERS]...')
        dividers_df = inp_dict['DIVIDERS']['data']
        file1.write('[DIVIDERS]\n')
        for i in range(len(dividers_df)):
            div =  dividers_df.loc[i, :]
            file1.write(str(div['Name'])+'    '+
                        str(div['Elevation'])+'    '+
                        str(div['DivertLink'])+'    '+
                        str(div['Type'])+'    '+
                        str(div['CutoffFlow'])+'    '+
                        str(div['WeirMinFlo'])+'    '+
                        str(div['WeirMaxDep'])+'    '+
                        str(div['WeirCoeff'])+'    '+
                        str(div['MaxDepth'])+'    '+
                        str(div['InitDepth'])+'    '+
                        str(div['SurDepth'])+'    '+
                        str(div['Aponded']))
            file1.write('\n')  
        file1.write('\n')    

    # storages
    df_to_inp_section('STORAGE')

    # conduits
    df_to_inp_section('CONDUITS')

    # pumps
    df_to_inp_section('PUMPS')

    # weirs orifices and outlets
    df_to_inp_section('WEIRS')
    df_to_inp_section('ORIFICES')
    df_to_inp_section('OUTLETS')
    
    # cross sections
    if 'XSECTIONS' in inp_dict.keys():
        feedback.setProgressText('writing [XSECTIONS]...')
        xsections_df = inp_dict['XSECTIONS']['data']
        file1.write('[XSECTIONS]\n')
        for i in range(len(xsections_df)):
            xscn = xsections_df.loc[i, :]
            file1.write(str(xscn['Name'])+'   '+
                        str(xscn['XsectShape'])+'    '+
                        str(xscn['Geom1'])+'    '+
                        str(xscn['Geom2'])+'    '+
                        str(xscn['Geom3'])+'    '+
                        str(xscn['Geom4'])+'    '+
                        str(xscn['Barrels'])+'    '+
                        str(xscn['Culvert']))
            file1.write('\n')
        file1.write('\n')


    # transects
    if 'TRANSECTS' in inp_dict.keys():
        feedback.setProgressText('writing [TRANSECTS]...')
        file1.write('[TRANSECTS]\n')
        transects_string_list = inp_dict['TRANSECTS']['data']
        for tr_string in transects_string_list:
            file1.write(tr_string)
            file1.write('\n')
        file1.write('\n')

    # streets
    df_to_inp_section('STREETS')

    # inlets
    df_to_inp_section('INLETS')
    df_to_inp_section('INLET_USAGE')

    # losses
    if 'LOSSES' in inp_dict.keys():
        feedback.setProgressText('writing [LOSSES]...')
        file1.write('[LOSSES]\n')
        losses_df = inp_dict['LOSSES']['data']
        for i in range(len(losses_df)):
            los = losses_df.loc[i,:]
            file1.write(str(los['Name'])+'   '+
                        str(los['Kentry'])+'   '+
                        str(los['Kexit'])+'   '+
                        str(los['Kavg'])+'   '+
                        str(los['FlapGate'])+'   '+
                        str(los['Seepage']))
            file1.write('\n')
        file1.write('\n')

    # quality
    if 'QUALITY' in inp_dict.keys():
        feedback.setProgressText('writing [Quality Parameters]...')
        quality_dict = inp_dict['QUALITY']['data']
        for q_k in quality_dict.keys():
            q_df = quality_dict[q_k]
            file1.write('['+str(q_k)+']\n')
            if q_df.empty:
                pass
            else:
                file1.write(q_df.to_string(header=False, index=False))
                file1.write('\n')
            file1.write('\n')

    def compose_dict_text(dict_i, section, inflow_keys_dict):
        """writes text lines from inflows dictionaries"""
        section_keys = inflow_keys_dict[section]
        return ['    '.join([str(dict_i[item_key][s_k]) for s_k in section_keys])+'\n' for item_key in dict_i.keys()]

    # inflows
    if 'INFLOWS' in inp_dict.keys():
        feedback.setProgressText('writing [INFLOWS]...')
        inflow_dict = inp_dict['INFLOWS']['data']
        file1.write('[INFLOWS]\n')
        file1.write(''.join(
            compose_dict_text(
                inflow_dict,
                'INFLOWS',
                inflow_keys_dict
            )
        ))
        file1.write('\n')

    if 'DWF' in inp_dict.keys():
        feedback.setProgressText('writing [Dry Weather Flows]...')
        dwf_dict = inp_dict['DWF']['data']
        file1.write('[DWF]\n')
        file1.write(''.join(
            compose_dict_text(
                dwf_dict,
                'DWF',
                inflow_keys_dict
            )
        ))
        file1.write('\n')
        
    df_to_inp_section('HYDROGRAPHS')
    df_to_inp_section('RDII')
        
        
    # curves
    if 'CURVES' in inp_dict.keys():
        feedback.setProgressText('writing [CURVES]...')
        curves_dict = inp_dict['CURVES']['data']
        file1.write('[CURVES]\n')
        for curve_key in curves_dict.keys():
            curve_dict_i = curves_dict[curve_key].copy()
            for i in range(len(curve_dict_i['frame'])):
                if i == 0:
                    file1.write(curve_dict_i['Name']+'    '+
                                curve_dict_i['Type']+'    '+
                                str(curve_dict_i['frame'].iloc[0, 0])+'    '+
                                str(curve_dict_i['frame'].iloc[0, 1]))
                    file1.write('\n')
                else:
                    file1.write(curve_dict_i['Name']+'    '+'    '+
                                 str(curve_dict_i['frame'].iloc[i, 0])+'    '+
                                 str(curve_dict_i['frame'].iloc[i, 1]))
                    file1.write('\n')
            file1.write(';\n')
        file1.write('\n')

    # time series
    if 'TIMESERIES' in inp_dict.keys():
        feedback.setProgressText('writing [TIMESERIES]...')
        timeseries_dict = inp_dict['TIMESERIES']['data']
        file1.write('[TIMESERIES]\n')
        for ts_key in timeseries_dict.keys():
            ts_dict_i = timeseries_dict[ts_key].copy()
            ts_df = ts_dict_i['TimeSeries']
            file1.write(';'+ts_dict_i['Annotations']+'\n')
            file1.write(ts_df.to_string(header=False, index=False))
            file1.write('\n')
        file1.write('\n')

    # patterns
    if 'PATTERNS' in inp_dict.keys():
        feedback.setProgressText('writing [PATTERNS]...')
        patterns_dict = inp_dict['PATTERNS']['data']
        file1.write('[PATTERNS]\n')
        for patterns_key in patterns_dict.keys():
            patterns_dict_i = patterns_dict[patterns_key].copy()
            if patterns_dict_i['Type'] == 'DAILY':
                file1.write(patterns_dict_i['Name']+'    '+
                            patterns_dict_i['Type']+'    '+
                            '    '.join([str(j) for j in patterns_dict_i['Factors'].iloc[:, 0]]))
                file1.write('\n')
            else:
                for i in range(int(len(patterns_dict_i['Factors'])/6)):
                    if i == 0:
                        file1.write(patterns_dict_i['Name']+'    '+
                                    patterns_dict_i['Type']+'    '+
                                    '    '.join([str(j) for j in patterns_dict_i['Factors'].iloc[0:6, 0]]))
                        file1.write('\n')
                    else:
                        file1.write(patterns_dict_i['Name']+'    '+'    '+
                                    '    '.join([str(j) for j in patterns_dict_i['Factors'].iloc[6*i:6*(i+1), 0]]))
                        file1.write('\n')
            file1.write(';\n')
        file1.write('\n')

    # report options
    feedback.setProgressText('writing [REPORT options]...')
    file1.write('[REPORT]\n')
    file1.write('SUBCATCHMENTS ALL\n')
    file1.write('NODES ALL\n')
    file1.write('LINKS ALL\n')
    file1.write('\n')

    # tags
    file1.write('[TAGS]\n')
    file1.write('\n')

    # point coordinates
    df_to_inp_section('COORDINATES')

    # line coordinates
    if 'VERTICES' in inp_dict.keys():
        feedback.setProgressText('writing [VERTICES]...')
        file1.write('[VERTICES]\n')
        vertices_dict = inp_dict['VERTICES']['data']
        for vert_key in vertices_dict.keys():
            vert_df = vertices_dict[vert_key].copy()
            vert_df['vertice'] = vert_key
            vert_df = vert_df[['vertice', 'x', 'y']]
            file1.write(vert_df.to_string(header=False, index=False))
            file1.write('\n')
        file1.write('\n')

    # subcatchment polygons
    if 'POLYGONS' in inp_dict.keys():
        feedback.setProgressText('writing [POLYGONS]...')
        polygons_dict = inp_dict['POLYGONS']['data']
        file1.write('[POLYGONS]\n')
        for pol_key in polygons_dict.keys():
            pol_df = polygons_dict[pol_key].copy()
            pol_df['subcatch']=pol_key
            pol_df = pol_df[['subcatch', 'x', 'y']]
            file1.write(pol_df.to_string(header=False, index=False))
            file1.write('\n')
        file1.write('\n')

    # gage symbol
    df_to_inp_section('SYMBOLS')

    file1.close()

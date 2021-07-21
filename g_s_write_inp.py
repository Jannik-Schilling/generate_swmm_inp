# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:53:11 2020

@author: schilling


"""
def write_inp(inp_file_name,
              project_dir,
              inp_dict):
    import os
    
    keys_dict = {'DWF':['Name','Baseline','Patterns'],
             'INFLOWS':['Name','Time_Series','Type','Mfactor','Sfactor','Baseline','Pattern']}
    
    
    # write input file
    file_path = os.path.join(project_dir,inp_file_name) 
    file1 = open(file_path,'w')
    
    
    ### header
    file1.write('[TITLE]\n' +
                ';;Project Title/Notes\n' +
                'test_name\n' +
                '\n')
    
    file1.write('[OPTIONS]\n')
    options_dict = inp_dict['options_dict']
    for key in options_dict.keys():
        file1.write(str(key)+'    '+str(options_dict[key])+'\n')
    file1.write('\n')
    
    ##evaporation
    file1.write('[EVAPORATION]\n'+
                'CONSTANT         0.0\n'+
                'DRY_ONLY         NO\n'+
                '\n')
    
    ##raingages
    if 'raingages_dict' in inp_dict.keys():
        print('writing [RAINGAGES]...')
        file1.write('[RAINGAGES]\n')
        raingages_dict = inp_dict['raingages_dict']
        for rg_key in raingages_dict.keys():
            rg_i = raingages_dict[rg_key]
            file1.write(str(rg_i['Name'])+'    '+
                        str(rg_i['Format'])+'    '+
                        str(rg_i['Interval'])+'    '+
                        str(rg_i['SCF'])+'    '+
                        str(rg_i['Source']))
            file1.write('\n')
        file1.write('\n')
    
    
    
    ##subcatchments
    if 'subcatchments_df' in inp_dict.keys():
        print('writing [SUBCATCHMENTS]...')
        subcatchments_df = inp_dict['subcatchments_df']
        file1.write('[SUBCATCHMENTS]\n')
        for i in range(len(subcatchments_df)):
            scm = subcatchments_df.loc[i,:]
            file1.write(str(scm['Name'])+'    '+
                        str(scm['RainGage'])+'    '+
                        str(scm['Outlet'])+'    '+
                        str(scm['Area'])+'    '+
                        str(scm['Imperv'])+'    '+
                        str(scm['Width'])+'    '+
                        str(scm['Slope'])+'    '+
                        str(scm['CurbLen'])+'    '+
                        str(scm['SnowPack']))
            file1.write('\n')
        file1.write('\n') 
        print('done')
        
        
        
    ## subareas 
    if 'subcatchments_df' in inp_dict.keys():
        print('writing [SUBAREAS]...')
        subcatchments_df = inp_dict['subcatchments_df']
        file1.write('[SUBAREAS]\n')
        for i in range(len(subcatchments_df)):
            scm = subcatchments_df.loc[i,:]
            file1.write(str(scm['Name'])+'    '+
                        str(scm['N_Imperv'])+'    '+
                        str(scm['N_Perv'])+'    '+
                        str(scm['S_Imperv'])+'    '+
                        str(scm['S_Perv'])+'    '+
                        str(scm['PctZero'])+'    '+
                        str(scm['RouteTo'])+'    '+
                        str(scm['PctRouted']))
            file1.write('\n')
        file1.write('\n')    
        print('done')
    
    
    ## infiltration
    if 'subcatchments_df' in inp_dict.keys():
        print('writing [INFILTRATION]...')
        subcatchments_df = inp_dict['subcatchments_df']
        file1.write('[INFILTRATION]\n')
        for i in range(len(subcatchments_df)):
            scm = subcatchments_df.loc[i,:]
            file1.write(str(scm['Name'])+'    '+
                        str(scm['Param1'])+'    '+
                        str(scm['Param2'])+'    '+
                        str(scm['Param3'])+'    '+
                        str(scm['Param4'])+'    '+
                        str(scm['Param5'])+'    '+
                        str(scm['kind']))
            file1.write('\n')   
        file1.write('\n')    
        print('done')
    
    
    ## junctions
    if 'junctions_df' in inp_dict.keys():
        print('writing [JUNCTIONS]...')
        junctions_df = inp_dict['junctions_df']
        file1.write('[JUNCTIONS]\n')
        for i in range(len(junctions_df)):
            jnct = junctions_df.loc[i,:]
            file1.write(str(jnct['Name'])+'    '
                        +str(jnct['Elevation'])+'    '
                        +str(jnct['MaxDepth'])+'    '
                        +str(jnct['InitDepth'])+'    '
                        +str(jnct['SurDepth'])+'    '
                        +str(jnct['Aponded']))
            file1.write('\n')  
        file1.write('\n')   
        print('done')
    
    
    ## outfalls
    if 'outfalls_df' in inp_dict.keys():
        print('writing [OUTFALLS]...')
        outfalls_df = inp_dict['outfalls_df']
        file1.write('[OUTFALLS]\n')
        for i in range(len(outfalls_df)):
            outl =  outfalls_df.loc[i,:]
            file1.write(str(outl['Name'])+'    '+
                        str(outl['Elevation'])+'    '+
                        str(outl['Type'])+'    '+
                        str(outl['Data'])+'    '+
                        str(outl['FlapGate'])+'    '+
                        str(outl['RouteTo']))
            file1.write('\n')  
        file1.write('\n')          
        print('done')
    
    ## storages
    if 'storage_df' in inp_dict.keys():
        print('writing [STORAGES]...')
        storage_df = inp_dict['storage_df']
        file1.write('[STORAGE]\n')
        for i in range(len(storage_df)):
            stor = storage_df.loc[i,:]
            file1.write(str(stor['Name'])+'    '+
                        str(stor['Elevation'])+'    '+
                        str(stor['MaxDepth'])+'    '+
                        str(stor['InitDepth'])+'    '+
                        str(stor['Type'])+'    '+
                        str(stor['Curve'])+'    '+
                        str(stor['Apond'])+'    '+
                        str(stor['Fevap'])+'    '+
                        str(stor['Psi'])+'    '+
                        str(stor['Ksat'])+'    '+
                        str(stor['IMD']))  
            file1.write('\n')  
        file1.write('\n')  
        print('done')
    
    ## conduits
    if 'conduits_df' in inp_dict.keys():
        print('writing [CONDUITS]...')
        conduits_df = inp_dict['conduits_df']
        file1.write('[CONDUITS]\n')
        for i in range(len(conduits_df)):
            con = conduits_df.loc[i,:]
            file1.write(str(con['Name'])+'    '
                        + str(con['FromNode'])+'    '
                        + str(con['ToNode'])+'    '
                        + str(con['Length'])+'    '
                        + str(con['Roughness'])+'    '
                        + str(con['InOffset'])+'    '
                        + str(con['OutOffset'])+'    '
                        + str(con['InitFlow'])+'    '
                        + str(con['MaxFlow']))
            file1.write('\n')     
        file1.write('\n')  
        print('done')
    
    ## pumps
    if 'pumps_df' in inp_dict.keys():
        print('writing [PUMPS]...')
        pumps_df = inp_dict['pumps_df']
        file1.write('[PUMPS]\n')
        for i in range(len(pumps_df)):
            pmp = pumps_df.loc[i,:]
            file1.write(str(pmp['Name'])+'   '+
                        str(pmp['FromNode'])+'    '+
                        str(pmp['ToNode'])+'    '+
                        str(pmp['PumpCurve'])+'    '+
                        str(pmp['Status'])+'    '+
                        str(pmp['Startup'])+'    '+
                        str(pmp['Shutoff']))
            file1.write('\n')
        file1.write('\n')
        print('done')
        
    ## weirs orifices and outlets
    if 'weirs_df' in inp_dict.keys():
        # to_do: orifices
        print('writing [WEIRS]...')
        weirs_df = inp_dict['weirs_df']
        file1.write('[WEIRS]\n')
        file1.write(weirs_df.to_string(header = False, index = False))
        file1.write('\n')
        file1.write('\n')
        print('done')
        
    if 'outlets_df' in inp_dict.keys():
        print('writing [OUTLETS]...')
        outlets_df = inp_dict['outlets_df']
        file1.write('[OUTLETS]\n')
        file1.write(outlets_df.to_string(header = False, index = False))
        file1.write('\n')
        file1.write('\n')
        print('done')
    
    ## cross sections
    if 'xsections_df' in inp_dict.keys():
        print('writing [XSECTIONS]...')
        xsections_df = inp_dict['xsections_df']
        file1.write('[XSECTIONS]\n')
        for i in range(len(xsections_df)):
            xscn = xsections_df.loc[i,:]
            file1.write(str(xscn['Name'])+'   '+
                        str(xscn['Shape'])+'    '+
                        str(xscn['Geom1'])+'    '+
                        str(xscn['Geom2'])+'    '+
                        str(xscn['Geom3'])+'    '+
                        str(xscn['Geom4'])+'    '+
                        str(xscn['Barrels'])+'    '+
                        str(xscn['Culvert']))
            file1.write('\n')
        file1.write('\n')
        print('done')
        
    ## losses
    if 'losses_df' in inp_dict.keys():
        print('writing [LOSSES]...')
        file1.write('[LOSSES]\n')
        losses_df = inp_dict['losses_df']
        for i in range(len(losses_df)):
            los = losses_df.loc[i,:]
            file1.write(str(los['Name'])+'   '+
                        str(los['Inlet'])+'   '+
                        str(los['Outlet'])+'   '+
                        str(los['Averge'])+'   '+
                        str(los['FlapGate'])+'   '+
                        str(los['Seepage']))
            file1.write('\n')
        file1.write('\n')
        print('done')
        
    ## quality
    if 'quality_dict' in inp_dict.keys():
        print('writing [Quality Parameters]...')
        quality_dict = inp_dict['quality_dict'].copy()
        for q_k in quality_dict.keys():
            q_df = quality_dict[q_k]
            file1.write('['+str(q_k)+']\n')
            if q_df.empty:
                pass
            else:
                file1.write(q_df.to_string(header = False, index = False))
                file1.write('\n')
            file1.write('\n')
        print('done')

    def compose_dict_text(dict_i, section, keys_dict):
        section_keys = keys_dict[section]
        return ['    '.join([str(dict_i[item_key][s_k]) for s_k in section_keys])+'\n' for item_key in dict_i.keys()]
        
    ## inflows
    if 'inflow_dict' in inp_dict.keys():
        print('writing [INFLOWS]...')
        inflow_dict = inp_dict['inflow_dict'].copy()
        file1.write('[INFLOWS]\n')
        file1.write(''.join(compose_dict_text(inflow_dict,'INFLOWS',keys_dict)))
        file1.write('\n')
        print('done')
        
    if 'dwf_dict' in inp_dict.keys():
        print('writing [Dry Weather Flows]...')
        dwf_dict = inp_dict['dwf_dict'].copy()
        file1.write('[DWF]\n')
        file1.write(''.join(compose_dict_text(dwf_dict,'DWF',keys_dict)))
        file1.write('\n')
        print('done')
        
    ## curves
    if 'curves_dict' in inp_dict.keys():
        print('writing [CURVES]...')
        curves_dict = inp_dict['curves_dict'].copy()
        file1.write('[CURVES]\n')
        for curve_key in curves_dict.keys():
            curve_dict_i = curves_dict[curve_key].copy()
            for i in range(len(curve_dict_i['frame'])):
                if i == 0:
                    file1.write(curve_dict_i['Name']+'    '+
                                curve_dict_i['Type']+'    '+
                                str(curve_dict_i['frame'].iloc[0,0])+'    '+
                                str(curve_dict_i['frame'].iloc[0,1]))
                    file1.write('\n')
                else:
                    file1.write(curve_dict_i['Name']+'    '+'    '+
                                 str(curve_dict_i['frame'].iloc[i,0])+'    '+
                                 str(curve_dict_i['frame'].iloc[i,1]))
                    file1.write('\n')
            file1.write(';\n')
        file1.write('\n')
        print('done')
                                 
                    
        
    
    ## time series
    if 'timeseries_dict' in inp_dict.keys():
        print('writing [TIMESERIES]...')
        timeseries_dict = inp_dict['timeseries_dict'].copy()
        file1.write('[TIMESERIES]\n')
        for ts_key in timeseries_dict.keys():
            ts_dict_i = timeseries_dict[ts_key].copy()
            ts_df = ts_dict_i['TimeSeries']
            file1.write(';'+ts_dict_i['Description']+'\n')
            file1.write(ts_df.to_string(header = False, index = False))
            file1.write('\n')
        file1.write('\n')
        print('done')
    
    
    if 'patterns_dict' in inp_dict.keys():
        print('writing [PATTERNS]...')
        patterns_dict = inp_dict['patterns_dict'].copy()
        file1.write('[PATTERNS]\n')
        for patterns_key in patterns_dict.keys():
            patterns_dict_i = patterns_dict[patterns_key].copy()
            if patterns_dict_i['Type'] == 'DAILY':
                file1.write(patterns_dict_i['Name']+'    '+
                            patterns_dict_i['Type']+'    '+
                            '    '.join([str(j) for j in patterns_dict_i['Factors'].iloc[:,0]]))
                file1.write('\n')
            else:
                for i in range(int(len(patterns_dict_i['Factors'])/6)):
                    if i == 0:
                        file1.write(patterns_dict_i['Name']+'    '+
                                    patterns_dict_i['Type']+'    '+
                                    '    '.join([str(j) for j in patterns_dict_i['Factors'].iloc[0:6,0]]))
                        file1.write('\n')
                    else:
                        file1.write(patterns_dict_i['Name']+'    '+'    '+
                                    '    '.join([str(j) for j in patterns_dict_i['Factors'].iloc[6*i:6*(i+1),0]]))
                        file1.write('\n')
            file1.write(';\n')
        file1.write('\n')
        print('done')
        
    ## report options
    print('writing [REPORT options]...')
    file1.write('[REPORT]\n')
    file1.write('SUBCATCHMENTS ALL\n')
    file1.write('NODES ALL\n')
    file1.write('LINKS ALL\n')
    file1.write('\n')
    print('done')
    
    
    ##tags
    file1.write('[TAGS]\n')
    file1.write('\n')
    
    
    ## point coordinates
    file1.write('[COORDINATES]\n')
    print('writing [COORDINATES]...')
    if 'junctions_df' in inp_dict.keys():
        junctions_df = inp_dict['junctions_df'].copy()
        for i in range(len(junctions_df)):
            geb = junctions_df.loc[i,:]
            file1.write(str(geb['Name'])+'    '+str(geb['X_Coord'])+'    '+str(geb['Y_Coord']))
            file1.write('\n')
        
    if 'outfalls_df' in inp_dict.keys():
        outfalls_df = inp_dict['outfalls_df'].copy()
        for i in range(len(outfalls_df)):
            outl =  outfalls_df.loc[i,:]
            file1.write(str(outl['Name'])+'    '+str(outl['X_Coord'])+'    '+str(outl['Y_Coord']))
            file1.write('\n')
            
    if 'storage_df' in inp_dict.keys():
        storage_df = inp_dict['storage_df'].copy()
        for i in range(len(storage_df)):
            stor = storage_df.loc[i,:]
            file1.write(str(stor['Name'])+'    '+str(stor['X_Coord'])+'    '+str(stor['Y_Coord']))
            file1.write('\n') 
    file1.write('\n')
    print('done')
    
    ## line coordinates
    if 'vertices_dict' in inp_dict.keys():
        print('writing [VERTICES]...')
        file1.write('[VERTICES]\n')
        vertices_dict = inp_dict['vertices_dict']
        for vert_key in vertices_dict.keys():
            vert_df = vertices_dict[vert_key].copy()
            vert_df['vertice'] = vert_key
            vert_df['y'] = round(vert_df['y'],2)
            vert_df['x'] = round(vert_df['x'],2)
            vert_df = vert_df[['vertice','x','y']]
            file1.write(vert_df.to_string(header = False, index = False))
            file1.write('\n')
        file1.write('\n')
        print('done')
    
    
    ## subcatchment polygons
    if 'polygons_dict' in inp_dict.keys():
        print('writing [Polygons]...')
        polygons_dict = inp_dict['polygons_dict']
        file1.write('[Polygons]\n')
        for pol_key in polygons_dict.keys():
            pol_df = polygons_dict[pol_key].copy()
            pol_df['subcatch']=pol_key
            pol_df['y'] = round(pol_df['y'],2)
            pol_df['x'] = round(pol_df['x'],2)
            pol_df = pol_df[['subcatch','x','y']]
            file1.write(pol_df.to_string(header = False, index = False))
            file1.write('\n')
        file1.write('\n')
        print('done')
    
    
    ## gage symbol
    if 'raingages_dict' in inp_dict.keys():
        raingages_dict = inp_dict['raingages_dict']
        file1.write('[SYMBOLS]\n')
        for gr_key in raingages_dict.keys():
            file1.write(gr_key+'            315142.721       5998080.373     \n')
        
    file1.close() 

from g_s_defaults import def_sections_dict
import numpy as np


# Outfalls
def get_outfalls_from_shapefile(outfalls_raw):
    outfalls_raw.loc[outfalls_raw['Type'] == 'TIDAL', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'TIDAL','Curve_TS']
    outfalls_raw.loc[outfalls_raw['Type'] == 'TIMESERIES', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'TIMESERIES','Curve_TS']
    outfalls_raw.loc[outfalls_raw['Type'] == 'FIXED', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'FIXED','FixedStage']
    outfalls_raw.loc[outfalls_raw['Type'] == 'FREE', 'Data'] = ''
    outfalls_raw.loc[outfalls_raw['Type'] == 'NORMAL', 'Data'] = ''
    outfalls_raw['RouteTo'] = outfalls_raw['RouteTo'].fillna('')
    outfalls_raw['Data'] = outfalls_raw['Data'].fillna('')
    return outfalls_raw


# Storages
st_types = {'FUNCTIONAL':['Coeff',
                          'Exponent',
                          'Constant'],
            'TABULAR':['Curve'],
            'PYRAMIDAL':['MajorAxis',
                         'MinorAxis',
                         'SideSlope'],
            'PARABOLIC':['MajorAxis',
                         'MinorAxis',
                         'SurfHeight'],
            'CONICAL':['MajorAxis',
                       'MinorAxis',
                       'SideSlope'],
            'CYLINDRICAL':['MajorAxis',
                          'MinorAxis']}
all_st_type_cols = ['Curve', 'Coeff' ,'Exponent', 'Constant','MajorAxis' , 'MinorAxis', 'SideSlope','SurfHeight']
st_col_def = def_sections_dict['STORAGE']

def get_storages_from_inp(st_raw_list_i):
    init_elems = st_raw_list_i[:5]
    st_type_i = st_raw_list_i[4]
    st_cols_i = st_types[st_type_i]
    st_vals_i = {col:st_raw_list_i[5+i] for i,col in enumerate(st_cols_i)}
    st_missing = {col_0:np.nan for col_0 in all_st_type_cols if col_0 not in st_vals_i.keys()}
    st_vals_i.update(st_missing)
    type_elems = [st_vals_i[t_c] for t_c in all_st_type_cols]
    # Seepage and Evaporation loss
    if st_type_i == 'TABULAR':
        sur_elems = st_raw_list_i[6:]
    else:
        sur_elems = st_raw_list_i[8:]
    if len(sur_elems) == 2:
        sur_elems = sur_elems+[np.nan,np.nan,np.nan]
    # resulting line
    st_raw_list_i_adjusted = init_elems+type_elems+sur_elems
    return(st_raw_list_i_adjusted)


import numpy as np
from .g_s_defaults import def_sections_dict
from .g_s_various_functions import check_columns, get_coords_from_geometry

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
st_types_def = {'FUNCTIONAL':['Coeff',
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


def get_storages_from_geodata(storages_raw):
    '''creates a df for storages from raw storage data'''
    storage_df = storages_raw.copy()
    occuring_storage_types = list(set(storages_raw['Type']))
    st_types_needed = list(set([col for s_t in occuring_storage_types for col in st_types_def[s_t]]))
    st_types_not_needed = [col for col in all_st_type_cols if col not in st_types_needed]
    storages_cols = list(def_sections_dict['STORAGE'].keys())
    storages_cols_needed = [col for col in storages_cols if col not in st_types_not_needed]
    storages_layer_name = 'Storages Layer'
    check_columns(storages_layer_name,
                  storages_cols_needed,
                  storage_df.keys())
    storage_df['X_Coord'],storage_df['Y_Coord'] = get_coords_from_geometry(storage_df)
    def st_type_adjustment(st_row):
        st_type_i = st_row['Type']
        cols_needed_i = st_types_def[st_type_i]
        if len(cols_needed_i) == 1: #TABULAR
            return st_row[cols_needed_i[0]], '', '' 
        elif len(cols_needed_i) == 2: #CYLINDRICAL
            return st_row[cols_needed_i[0]], st_row[cols_needed_i[1]], 0 
        else:
            return st_row[cols_needed_i[0]], st_row[cols_needed_i[1]], st_row[cols_needed_i[2]]
    storage_df[['Shape1','Shape2','Shape3']] = [st_type_adjustment(storage_df.loc[i]) for i in storage_df.index]
    storage_df['Psi'] = storage_df['Psi'].fillna('')
    storage_df['Ksat'] = storage_df['Ksat'].fillna('')
    storage_df['IMD'] = storage_df['IMD'].fillna('')
    storage_df = storage_df.drop(columns=all_st_type_cols)
    return storage_df




def get_storages_from_inp(st_raw_line):
    '''adjusts '''
    init_elems = st_raw_line[:5]
    st_type_i = st_raw_line[4]
    st_cols_i = st_types_def[st_type_i]
    st_vals_i = {col:st_raw_line[5+i] for i,col in enumerate(st_cols_i)}
    st_missing = {col_0:np.nan for col_0 in all_st_type_cols if col_0 not in st_vals_i.keys()}
    st_vals_i.update(st_missing)
    type_elems = [st_vals_i[t_c] for t_c in all_st_type_cols]
    # Seepage and Evaporation loss
    if st_type_i == 'TABULAR':
        sur_elems = st_raw_line[6:]
    else:
        sur_elems = st_raw_line[8:]
    if len(sur_elems) == 2:
        sur_elems = sur_elems+[np.nan,np.nan,np.nan]
    # resulting line
    st_line_adjusted = init_elems+type_elems+sur_elems
    return(st_line_adjusted)


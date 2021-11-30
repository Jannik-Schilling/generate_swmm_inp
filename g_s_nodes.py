def get_outfalls_from_shapefile(outfalls_raw):
    outfalls_raw.loc[outfalls_raw['Type'] == 'TIDAL', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'TIDAL','Curve_TS']
    outfalls_raw.loc[outfalls_raw['Type'] == 'TIMESERIES', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'TIMESERIES','Curve_TS']
    outfalls_raw.loc[outfalls_raw['Type'] == 'FIXED', 'Data'] = outfalls_raw.loc[outfalls_raw['Type'] == 'FIXED','FixedStage']
    outfalls_raw.loc[outfalls_raw['Type'] == 'FREE', 'Data'] = ''
    outfalls_raw.loc[outfalls_raw['Type'] == 'NORMAL', 'Data'] = ''
    outfalls_raw['RouteTo'] = outfalls_raw['RouteTo'].fillna('')
    outfalls_raw['Data'] = outfalls_raw['Data'].fillna('')
    return outfalls_raw
    
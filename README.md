# generate_swmm_inp
A QGIS plugin which generates an SWMM input file from existing shapefiles

Default data can be loaded with the first tool. So far shapefiles are provided for
- junctions (SWMM_junctions.shp)
- conduits (SWMM_conduits.shp)
- subcatchments (SWMM_subcatchments.shp)
- storages (SWMM_storages.shp)
- outfalls (SWMM_outfalls.shp)
- pumps (SWMM_pumps.shp)
- weirs (SWMM_weirs.shp)
- outfalls (SWMM_outfalls.shp)

Further data is provided in tables:
- curves (gisswmm_curves.xlsx)
- inflows (gisswmm_inflows.xlsx)
- options (gisswmm_options.xlsx)
- patterns (gisswmm_patterns.xlsx)
- quality  (gisswmm_quality.xlsx)
- timeseries (gisswmm_timeseries.xlsx)


The second tool writes the swmm input file (.inp). Please use the default files as a template for your own model, because File names and column names have to be matching in order to identify the correct information for the inp file.

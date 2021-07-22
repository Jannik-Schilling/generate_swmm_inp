# generate_swmm_inp
A QGIS plugin which generates an SWMM input file from existing shapefiles

## Recommended Workflow
### 0 Install 
- [SWMM](https://www.epa.gov/water-research/storm-water-management-model-swmm)
- the generate_swmm_inp plugin in QGIS (from the official QGIS plugin repository or from zip-file)

### 1 Load default the data 
...with the first tool. To date shapefiles are provided for the main infrastructures:
- junctions (SWMM_junctions.shp)
- conduits (SWMM_conduits.shp)
- subcatchments (SWMM_subcatchments.shp)
- storages (SWMM_storages.shp)
- outfalls (SWMM_outfalls.shp)
- pumps (SWMM_pumps.shp)
- weirs (SWMM_weirs.shp)
- outfalls (SWMM_outfalls.shp)

Further data is provided in tables and can be edited there:
- curves (gisswmm_curves.xlsx)
- inflows (gisswmm_inflows.xlsx)
- options (gisswmm_options.xlsx)
- patterns (gisswmm_patterns.xlsx)
- quality  (gisswmm_quality.xlsx)
- timeseries (gisswmm_timeseries.xlsx)

### 2 Write a swmm input file (.inp)
...with the second tool. The default files serve as a template for your own model, because file names and column names have to be matching in order to identify the correct information for the inp file.

### 3 Run the model
...in SWMM or with the help of scripts (e.g. [swmm_api by Markus Pichler](https://gitlab.com/markuspichler/swmm_api)). 
After a first test run you can edit the data in QGIS (and data in Tables). Then use the second tool to generate a new inp file (**step 2**). Sections which are not implemented in the plugin yet (see [issue 2](https://github.com/Jannik-Schilling/generate_swmm_inp/issues/2)) can be added directly in SWMM.



# ![icon](/icons/icon.png) generate_swmm_inp
A QGIS plugin which provides tools to create a SWMM input file from layers in QGIS, and to import input files into QGIS. The documentation can be found [here](https://github.com/Jannik-Schilling/generate_swmm_inp/blob/main/documentation/g_s_i_documentation_v_0_2.pdf).


## Recommended Workflow
### 0 Install 
- [SWMM](https://www.epa.gov/water-research/storm-water-management-model-swmm) or other software to run the simulation ([see Links below](#further-useful-packages))
- the generate_swmm_inp plugin in QGIS (from the official QGIS plugin repository or from zip-file)
- if needed: the python packages "pandas" and "openpyxl": 
    - for windows: https://landscapearchaeology.org/2018/installing-python-packages-in-qgis-3-for-windows/
    - for linux, install via pip 

### 1 Load the default data 
...with the first tool (**1_GenerateDefaultData**). Alternatively you can load existing geodata into QGIS (**step 5**). Starting with version 0.18, geopackages (instead of shapefiles) are provided for the main infrastructures:
- junctions (SWMM_junctions.gpkg)
- conduits (SWMM_conduits.gpkg)
- subcatchments (SWMM_subcatchments.gpkg)
- storages (SWMM_storages.gpkg)
- outfalls (SWMM_outfalls.gpkg)
- pumps (SWMM_pumps.gpkg)
- weirs (SWMM_weirs.gpkg)
- outlets (SWMM_outlets.gpkg)
- orifices (SWMM_orifices.gpkg)
Further data is provided in tables and can be edited there:
- curves (gisswmm_curves.xlsx)
- inflows (gisswmm_inflows.xlsx)
- options (gisswmm_options.xlsx)
- patterns (gisswmm_patterns.xlsx)
- quality  (gisswmm_quality.xlsx)
- timeseries (gisswmm_timeseries.xlsx)
- transects (gisswmm_transects.xlsx)

### 2 Edit
A first test run with the default data is recommended (**steps 3 and 4**).
Then you can edit the geodata in QGIS and data in tables to create your own model. When filling the attribute tables, the [SWMM user manual](https://www.epa.gov/water-research/storm-water-management-model-swmm-version-51-users-manual) migth help you to find the right columns and suitable values. SWMM sections/infrastructures which are not implemented in the plugin yet (see [issue 2](https://github.com/Jannik-Schilling/generate_swmm_inp/issues/2)) can be added directly in SWMM later.

If you start from scratch, a useful tool to create a network from a line layer is the QGIS plugin "WaterNetAnalyzer" (available in the [QGIS plugin repository](https://plugins.qgis.org/plugins/WaterNetAnalyzer-master/) or on [Github](https://github.com/Jannik-Schilling/WaterNetAnalyzer)).

### 3 Write a swmm input file (.inp)
...with the second tool **(2_GenerateSwmmInpFile)**. The default files serve as a template for your own model, because column names have to be matching in order to identify the correct information for the inp file. 
 - until version 0.10 you chose the folder in which all geodata and tables are stored. The file names have to remain the same as in the default data set.
 - from version 0.11 on you don´t have to keep the original file names. Now you can rename the file e.g. in order to have different variants of conduits layers.

### 4 Run the model
...dirctly in SWMM or with the help of scripts in R or python (see below). There migth be several errors in th model at first -> return to step 2.

### 5 Import existing inp files (for future edits)
You can import existing inp files with the third tool (**3_ImportInpFile**). Creating a new folder (e.g. "swmm_data_v2") for the data is recommended.

## Further useful packages
Python:
- [SWMM5 for Python](https://pypi.org/project/SWMM5/)
- [swmm_api](https://gitlab.com/markuspichler/swmm_api) 
- [swmmio](https://github.com/aerispaha/swmmio)
- [pyswmm](https://github.com/OpenWaterAnalytics/pyswmm)
- [swmmtoolbox](https://pypi.org/project/swmmtoolbox/)


R:
- https://github.com/cran/swmmr



## Contribute
:+1: Feel free to contribute, contact me, report issues and propose new features/code...

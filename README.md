# ![icon](/icons/icon.png) generate_swmm_inp
A QGIS plugin which provides tools to create a SWMM input file from layers in QGIS, and to import input files into QGIS. The plugin was recently updated according to new functions in SWMM 5.2. Input files from SWMM 5.1.15 will still work. 

## Documentation
[Link](https://github.com/Jannik-Schilling/generate_swmm_inp/blob/main/documentation/g_s_i_documentation_v_0_2.pdf) to the documentation file

## Provided tools:
1. **1_GenerateDefaultData**: Load a default set of layers to your QGIS project
2. **2_GenerateSwmmInpFile**: Select a set of layers in QGIS to create an input file for a SWMM simulation
3. **3_ImportInpFile**: Import an existing SWMM model into QGIS (layers and tables).
4. **4_CreateSubModel**: Create a submodel (of an existing set SWMM layers in QGIS) below or above a certain node

## Recommended Workflow
### 0 Install 
- the generate_swmm_inp plugin in QGIS (from the official QGIS plugin repository or from zip-file)
- if needed: the python packages "pandas" and "openpyxl": 
    - for windows: https://landscapearchaeology.org/2018/installing-python-packages-in-qgis-3-for-windows/
    - for linux, install via pip 
- [SWMM](https://www.epa.gov/water-research/storm-water-management-model-swmm) or other software to run the simulation ([see Links below](#further-useful-packages))


### 1 Load the default data set
...with the first tool. Alternatively you can import existing models into QGIS (**step 5**). Separate layers are provided for the main infrastructures:
- rain gages 
- junctions 
- conduits 
- subcatchments 
- storages 
- outfalls 
- pumps
- weirs
- outlets
- orifices


Further data is provided in tables (which will be saved in the chosen directory) and can be edited there:
- curves
- inflows
- options
- patterns
- quality
- timeseries
- transects
- streets (only for swmm 5.2 and later)

### 2 Edit
Now you can do some modifactions.
You can edit the layers in QGIS and data in tables to create your own model. When filling the attribute tables, the [documentation file](https://github.com/Jannik-Schilling/generate_swmm_inp/blob/main/documentation/g_s_i_documentation_v_0_2.pdf) and the [SWMM user manual](https://www.epa.gov/water-research/storm-water-management-model-swmm-version-51-users-manual) migth help you to find the right columns and suitable values. SWMM sections/infrastructures which are not implemented in the plugin yet (see [issue 2](https://github.com/Jannik-Schilling/generate_swmm_inp/issues/2)) can be added directly in SWMM later. Saving layer as a new file, e.g. if you want to have different variants of conduits layers, is recommended. 

If you start from scratch, a useful tool to create a network from a line layer is the QGIS plugin "WaterNetAnalyzer" (available in the [QGIS plugin repository](https://plugins.qgis.org/plugins/WaterNetAnalyzer-master/) or on [Github](https://github.com/Jannik-Schilling/WaterNetAnalyzer)).

### 3 Write a swmm input file (.inp)
...with the second tool **(2_GenerateSwmmInpFile)**. You select the layers and tables which you want to use for your new models. The column names of the attribute tables are used by the tool in order to identify the correct information for the inp file. So be careful if you renamed or deleted any columns.

### 4 Run the model
...dirctly in SWMM or with the help of scripts in R or python (see below). There migth be several errors in th model at first -> return to step 2.

### 5 Import existing inp files (for future edits)
You can import existing inp files with the third tool (**3_ImportInpFile**). Creating a new folder (e.g. "swmm_data_v2") for the data is recommended. You can choose a prefix (e.g. "v2") which will be added and the data format (.shp, .gpkg, .gml, .kml, .geojson).

Some formats seem to have problems with certain coordinate reference systems. GPKG and SHP worked fine so far


## Further useful packages
Python:
- [SWMM5 for Python](https://pypi.org/project/SWMM5/)
- [swmm_api](https://gitlab.com/markuspichler/swmm_api) 
- [swmmio](https://github.com/aerispaha/swmmio)
- [pyswmm](https://github.com/OpenWaterAnalytics/pyswmm)
- [swmmtoolbox](https://pypi.org/project/swmmtoolbox/)


R:
- https://github.com/cran/swmmr



## Contributing
- if you encounter any issues while using the plugin please report [here](https://github.com/Jannik-Schilling/generate_swmm_inp/issues).
- you can also propose new features and discuss them at the issues page. 
- You can fork this repository to implement your own code and send a pull request

## Cite
> *Schilling, J.; Tränckner, J. Generate_SWMM_inp: An Open-Source QGIS Plugin to Import and Export Model Input Files for SWMM. Water 2022, 14, 2262. https://doi.org/10.3390/w14142262*

## Funding
First versions of this plugin have been developed within the project PROSPER-RO, funded by BMBF, grant number 033L212

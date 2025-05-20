---
author: Jannik Schilling
email: <jannik.schilling@posteo.de>
title: generate_swmm_inp
subtitle: Manual for the QGIS plugin, version 0.39.2
title: generate_swmm_inp
---

This work is licensed under a Creative Commons Attribution 4.0 License\
If you use the plugin in scientific work or other studies, please cite
as: Schilling, J.; Tränckner, J. GenerateSWMMinp: An Open-Source QGIS
Plugin to Import and Export Model Input Files for SWMM. Water 2022, 14,
2262. https://doi.org/10.3390/w14142262\
Funding:

-   First versions (0.1 to 0.31) of this plugin have been developed
    within the project PROSPER-RO, funded by BMBF (German Federal
    Ministry of Education and Research), grant number 033L212.

-   New features and bugfixes (since version 0.32) have been added
    within the project OSWeGe (<https://oswege.auf.uni-rostock.de/>),
    funded by BMUV (German Federal Ministry for the Environment, Nature
    Conservation, Nuclear Safety and Consumer Protection), grant number
    67DAS263.

# Introduction

SWMM is an open-source model and software by the US EPA for the
simulation of rainfall-runoff and routing in water bodies, sewer systems
and wastewater infrastructures. An intruduction to the model itself and
details about attributes used in SWMM can be found in the official
manual ([see US EPA website](https://www.epa.gov/water-research/storm-water-management-model-swmm)).\
For a new SWMM model, objects such as nodes, links and catchments can
either be drawn via the graphical user interface (GUI) of SWMM or
specified in a plain text file in \".inp\" format (*input file*). The
required data regarding sewer geometries and rivers systems are usually
available as geodata (e.g. *geopackage, shapefiles\...*). A direct
import function for such files is not available in SWMM so far. To fix
this problem, the plugin \"generate_swmm_input\" enables the conversion
of geodata in QGIS into *input files* for SWMM. Additionally, the plugin
provides a tool to import *input files* from SWMM into QGIS. This allows
you to edit the model data as layers with the aid of the large toolbox
of QGIS.\
This documentation explains how to install the plugin and how to prepare
the geodata in QGIS. It is (and will remain) a \"work in progress\". If
you find any mistakes or you miss explanations for certain tools,
layers, \... please write an issue on GitHub or an email to the author.\


## Installation

**The plugin:** \"generate_swmm_inp\" can be installed within QGIS from
the official QGIS plugin repository. The latest experimental version of
the plugin will always be available on GitHub and can be installed from
a zip file after downloading it from the [GitHub repository](https://github.com/Jannik-Schilling/generate_swmm_inp) of the plugin. 
As this is a processing plugin, the tools will be
added to the processing toolbox.\
\
**In some cases: missing Python packages.** The plugin needs the Python
package \"pandas\" whis is normally already part of the standard
installation of QGIS. If this is not the case, the tools will raise
errors, when running. To install missing packages, various instructions
can be found online. Here are some examples\...

-   Windows:

    -   If you have had an \"advanced install\" of QGIS with the osgeo4w
        installer, you can simply open the osgeo4w installer again,
        search for the packages and select the checkbox to install them.

    -   until QGIS version 3.18: Open the OSGeo4W shell and run
        `py3_env`.\
        Then run
        `python -m pip install pandas`

    -   for QGIS version 3.20 and later: Open the OSGeo4W shell and
        directly run\
        `python -m pip install pandas`.

-   Linux: open the terminal and install via pip:
    `python -m pip install pandas`.

**SWMM:** To run the models, SWMM has to be installed. Alternatively you
can use the \"swmmr\" package ([see github page here](https://github.com/dleutnant/swmmr)) for R or packages such as
\"pyswmm\" for Python.\

## Hints for this documentation 

Two different types of tables will appear in the documentation. The
first type shows the column names and attributes which are used in
geodata and .xlsx (.xls, .ods) files. Such a table will look like this:

|**Name in attribute table** | **Data type** |**Name in SWMM GUI (5.2.1)** | **annotations**|
|------------|--------|-------|--------|
|... |... |... | |
|... |... |... | |


The second type shows examples of how tables in the .xlsx (.xls, .ods)
files have to be organised. Such a table will look like this:



| **1st col.** | **2nd col.** | **3rd col.** |  **4th col.** |  **5th col.**|
|------------|--------|-------|--------|-----|
| some |  random |  data | ... | ...| 
| ... |  ... |  ... | ... | ...| 

## Latest changes

Version 0.39:

-	new feature: import and Z-Coordinates for conduits and nodes (advanced option) in tools 1,2 and 3

-	fix for QgsGeometry deprecation warning

-	headers in inp file


Notable changes in former versions:

-   Version 0.34: replacement of column **\"Shape\"** by
    **\"XsectShape\"** in **conduits** layers and **orifices** layers
    because of issues with ESRI-Shapefiles. Currently, a deprecation
    warning will appear and the tools will still work with old SWMM
    layers. However it is recommended to apply these changes from now
    on.

-   Version 0.34: removal of \"openpyxl\" due to several crashes on
    Windows

-   Version 0.32: bugfixes for package import and \"rounded\" vertices

-   Version 0.30: new feature: import of SWMM report files (QgsAction)

-   Version 0.28: new feature: hydrographs und rdii tables (inflows)

-   Version 0.25: new tool '4_SelectSubModel' ; added import and export
    of descriptions / annotations

-   Version 0.23: added option 'empty layers' to tool 1

-   Version 0.23: raingages can now only be added as layers. This
    replaces former rain gage setting in time series (see subsection
    [4.2.3](#sect_timeseries){reference-type="ref"
    reference="sect_timeseries"}).

-   Version 0.22: new feature forms

-   Version 0.20: \"RoadWidth\" was renamed in version 0.20, before:
    (unfortunately) \"CurbWidth\"

-   Version 0.19: New features of SWMM 5.2 are integrated in the plugin.
    Therefore new columns, tables and keywords had to be added. If you want to continue working with SWMM 5.1 the plugin
    can still generate suitable input files as long as you don´t choose
    the new features and keywords.\

# The tools 

## 1_GenerateDefaultData 

The first tool will give you a default data set to see the data
structure needed for the export and conversion into a input file later
on. You can choose wether you would like empty layers, a data sample for
SWMM 5.1 or a data sample for SWMM 5.2. You can directly create the
layers with the coordinate reference system (CRS) for your region. The
default CRS is \"epsg:25833\". 
<span style="color:red"> Elevations, and offsets can be imported as z-coordinates for conduits
and nodes.</span> 
The files will be saved in the selected
folder. Geodata are provided for the main infrastructures:

-   rain gages (SWMM_raingages.gpkg)

-   junctions (SWMM_junctions.gpkg)

-   conduits (SWMM_conduits.gpkg)

-   subcatchments (SWMM_subcatchments.gpkg)

-   storages (SWMM_storages.gpkg)

-   outfalls (SWMM_outfalls.gpkg)

-   pumps (SWMM_pumps.gpkg)

-   weirs (SWMM_weirs.gpkg)

-   outlets (SWMM_outlets.gpkg)

-   orifices (SWMM_orifices.gpkg)

-   dividers (SWMM_dividers.gpkg)

Further data is provided in tables and can be edited there:

-   curves (gisswmm_curves.xlsx)

-   inflows (gisswmm_inflows.xlsx)

-   options (gisswmm_options.xlsx)

-   patterns (gisswmm_patterns.xlsx)

-   quality (gisswmm_quality.xlsx)

-   timeseries (gisswmm_timeseries.xlsx)

-   transects (gisswmm_transects.xlsx)

-   streets (gisswmm_streets.xlsx)

## 2_GenerateSwmmInpFile 

With the second tool, you can directly convert layers from QGIS into
input files. You can add further data (e.g. curves, inflows patterns) from tables to the input file. The default
data serve as a template for your own model, because column names have
to be matching in order to identify the correct information for the
input file. Actions in the user interface:

1.  Select the layers and files you want to have in your SWMM model

2.  Choose a location and name for the resulting input file (\".inp\")

3. <span style="color:red">Use z-coordinates of nodes to replace the attribute "Elevation" in a nodes layer, and
z-coordinates of conduits (and nodes in case of INLET_OFFSET = DEPTH in the OPTIONS table) to replace "InOffset" and "OutOffset" </span>

The tool will not check if the layers are in the same CRS. This can lead
to unexpected results. So make sure, that all selected layers have the
same CRS (or save a copy of the layer in the desired CRS).

## 3_ImportInpFile

The third tool allows you to import input files into QGIS. All sections
(if already implemented) of the input file will be connverted into QGIS
layers (e.g. shapefiles) and tables. Actions in the user interface:

1.  Choose the input file (\".inp\") to import

2.  Choose the file format for geodata

3.  Choose the (expected) CRS of the data in the input file

4.  Optional: choose a prefix to specify the name of the resulting
    files. For example, if the prefix is set to \"20210101\", then the
    name of the junctions file will be \"20210101_SWMM_junctions\". Try
    to avoid any characters here, which could cause trouble with file
    systems (e.g. \".\", \",\" , \"/\"\... )

5. <span style="color:red">Optional, advanced parameter: Elevations, and offsets can be imported as z-coordinates for conduits and
nodes.</span>

6.  Select a folder to save the resulting files in. Creating and chosing
    a new, empty folder for the import is recommended.

**Attention**: SWMM was a command line tool in the beginning. Therefore,
\"visible\" geometries (polygons, lines, points) are not neccessary to
run a simulation in SWMM. QGIS, by contrast, needs geometries. If a
geometry is not available in the input file, the tool will set a default
geometry for this feature.

## 4_SelectSubModel

This tool allows you to create a new set of layers as a \"submodel\" of
already existing SWMM layers in QGIS. You start by selecting exactly one
node/point in any node layer (Junction, Storage, Divider, Outfall). Then
you double-click on the tool to open it. You choose, wether you´d like
to

-   keep/select all the features above the selected node

-   exclude all the features above the selected node

for the new SWMM layers. You can define a prefix, which will be added to
the layer names. If you do not define a prefix, then \"Subset\" will be
taken by default, here. As in tool 2 you
choose the layers to be included in the model and a folder to save the
resulting layers in. The new layers will automatically added to the QGIS
project in a new group (named with the chosen prefix).

# Feature forms

Style files (.qml) with custom feature forms for every SWMM layer are
added to the layers with the first tool by default. Alternatively you
can download the style files or copy them from your QGIS plugin folder.
These feature forms will help you to insert suitable values when you add
or edit a feature:\

<img src="/figures/feature_forms.png" alt= “feature_forms” width="50%">

After you ran a simulation in SWMM (or with a python package) you can
add the results from a report file. You´ll find the button for the
QgisAction in the feature form of a SWMM layer. You select the report file, the SWMM
feature type and the desired report section. The report table will be
opened as a new window. You can now save the the table as a csv file. By
default, the resulting file will be added to the QGIS project (if you
don´t want this, uncheck the checkbox).

<img src="/figures/action_report.png" alt= “action_report” width="50%">

# Field names and column names in geodata and tables 

## Geodata

In the first versions of the plugin, the main file type for geodata were
shapefiles. This limited the length of the field names in the attribute
to 10 characters. Hence, in some cases, the field names required for the
tools differ from those used in the graphical user interface (GUI) in
SWMM. For example, the rate of seepage loss into the surrounding soil of
a conduit can be defined with the field \"Seepage\" in the conduits
layer, which refers to \"Seepage Loss Rate\" in
the SWMM GUI.

### Rain gages

layer type: point\
description: Rain gages are used in SWMM to set
precipitation data for subcatchments. The rain gages layer was added in
version 0.22 of the plugin.\


|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
|---------|----------|------------|------|
|Name | string | Name | |
|Format | string | Rain Format ||
|Interval | string | Time Interval | format: HH:mm|
|SCF | float | Snow Catch Factor| |
|DataSource | string | Data Source | 'FILE' or 'TIMESERIES'|
|SeriesName | string | Series Name | if \"DataSource\" is 'TIMESERIES'|
|FileName | string | File Name | if \"DataSource\" is 'FILE'|
|StationID | string | Station ID | if \"DataSource\" is 'FILE'|
|RainUnits | string | Rain Units | 'IN' or 'MM'; if \"DataSource\" is 'FILE'|
|Annotation | string | Description | optional column|



### Nodes

layer type: point\
Four types of nodes can be added to a SWMM-file: junctions, storage
units, dividers or outfalls. Inflows into any kind of nodes can be are
defined in the 'Inflows' table.
Treatment of pollutatants is not implemented yet.

#### Junctions

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string| Name | |
|Elevation | float | Invert El. | |
|MaxDepth | float | Max. Depth | |
|InitDepth | float | Initial Depth | |
|SurDepth | float | Surcharge Depth | 
|Aponded | float | Ponded Area |
|Annotation | string | Description | optional column|


#### Storage units

[description]{.smallcaps}: Storage units are represented in a point
layer in QGIS. Until SWMM version 5.1 the shape of a storage could
be described either by a function ('FUNCTIONAL') or in a table
('TABULAR') as a storage curve. [With SWMM version 5.2 storage units can
have a variety of shape types (see \"Type\")].
Different columns in the attribute table are required for different
shape types. Of course you can also have shape types for different
storages within one storage layer.

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|Elevation | float | Invert El. | |
|MaxDepth | float | Max. Depth | |
|InitDepth | float | Initial Depth| |
|SurDepth | float | Surcharge Depth | |
|Type | string | Storage Curve | 'FUNCTIONAL', 'TABULAR', 'PYRAMIDAL','PARABOLIC','CONICAL' or 'CYLINDRICAL'|
|Curve | string | Curve Name | for TABULAR storage curves; the names of the curves have to be matching with those in the storage curves table|
|Coeff | float | Coefficient | |
|Exponent |float | Exponent | |
|Constant | float | Constant ||
|MajorAxis | float | [(Base) Major Axis Length |
| MinorAxis | float | (Base) Minor Axis Length (Width)|
|SideSlope | float | Side (Wall) Slope||
|SurfHeight| float | Heigth of Axis Surface| |
|Fevap | float | Evap. Factor ||
|Psi | float | Suction Head | for seepage loss; inches or mm|
|Ksat |float | Conductivity | for seepage loss; in/h or mm/h|
|IMD | float | Initial Deficit & for seepage loss; difference between porosity and moisture content|
|Annotation | string | Description | optional column|



#### Dividers

Description] If the routing option (see options section)
is set to 'Steady Flow' or 'Kinematic Wave', flow dividers divert
inflows in a certain way, prescribed by the user with the attribute
\"Type\". With the 'Dynamic wave' routing model, dividers are treatet as
junctions.



|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|Elevation | float | Invert El. | |
|DivertLink | string | Outlet Node ||
|MaxDepth | float | Max. Depth ||
|InitDepth | float | Initial Depth ||
|SurDepth | float | Surcharge Depth||
|Aponded | float | Ponded Area||
|Type | string | Type | 'CUTOFF', 'TABULAR', 'WEIR' or 'OVERFLOW'|
|CutoffFlow | float | Cutoff Flow | if Type is CUTOFF|
|Curve | float | Curve Name | if Type is TABULAR; the names of the curves have to be matching with those in the divider curves table|
|WeirMinFlo | float | Outlet Offset |
|WeirMaxDep | float | Initial Flow|
|WeirCoeff | float | Maximum Flow|
|Annotation | string | Description | optional column|


#### Outfalls

Description: Outfalls are the terminal nodes of the model.
Only one link can be connected to an outfall.

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|Elevation | float | Invert El. | |
|FlapGate | string | Tide Gate | 'YES' or 'NO'|
|RouteTo | string | Route To |Subcatchment outflow ist routed onto; leave blank if not applicable|
|Type | string | Type | 'FREE','NORMAL','FIXED','TIDAL' or 'TIMESERIES'|
|FixedStage | float | Fixed Stage | for outfalls with FIXED type|
|Curve_TS | string | Curve Name or Series Name | for TIDAL type: the name of the tidal curve has to be matching with the name in the curves table; for TIMESERIES type: the name of the time series has to be matching with then name in the time series table|
|Annotation | string | Description | optional column|

### Links

layer type: line\
Links are represented as line layers in QGIS. These can be conduits,
pumps, weirs, orifices or outlets.

#### Conduits

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|FromNode | string | Inlet Node ||
|ToNode | string | Outlet Node||
|Length | float | Length ||
|Roughness | float |Roughness ||
|InOffset | float |Inlet Offset ||
|OutOffset | float | Outlet Offset ||
|InitFlow | float | Initial Flow&||
|MaxFlow | float | Maximum Flow||

*Data for cross sections (XSECTIONS):*

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Shape | string | | See SWMM manual for shape types|
|Geom1 | float | | for most of the shapes this is the 'Max. Depth'|
|Geom2 | float | |
|Geom3 | float | |
|Geom4 | float | |
|Barrels | int | Number of Barrels|
|ShpTrnsct | string | - |Transect name if \"Shape\" is IRREGULAR, shape curve name if \"Shape\" is CUSTOM or street type name if \"Shape\" is STREET |
|Culvert | float | Culvert Code| |

*Data for LOSSES:*

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Kentry | float | Entry Loss Coeff. |
|Kexit | float | Entry Loss Coeff. |
|Kavg | float | Avg. Loss Coeff. |
|FlapGate | String | Flap Gate | can be 'YES' or 'NO'|
|Seepage |float | Seepage Loss Rate|
|Annotation | string | Description | optional column|


#### Pumps 

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|FromNode | string | Inlet Node | |
|ToNode | string | Outlet Node| |
|PumpCurve | string | Pump Curve & has to be matching with the curve name in the pump curves table; set an asterisk ('\*') here for ideal pump
|Status | string | Initial Status & 'ON' or 'OFF'|
|Startup | float | Startup Depth||
|Shutoff | float | Shutoff Depth ||
|Annotation | string | Description | optional column|


#### Weirs

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|FromNode | string | Inlet Node | |
|ToNode | string | Outlet Node| |
|Type | string | Type | 'TRANSVERSE', 'SIDEFLOW', 'V-NOTCH', 'TRAPEZIODAL' or 'ROADWAY'|
|Height | float | Height | |
|Length | float | Length | |
|SideSlope | float | Side Slope | Slope (width-to-height) of TRAPEZIODAL weir side walls|
|CrestHeigh | float | Inlet Offset | |
|Qcoeff | float | Discharge Coeff. | |
|FlapGate | string | Flap Gate | 'YES' or 'NO'|
|EndContrac | int | End Contractions | 0, 1 or 2|
|EndCoeff | float | End Coeff. | For TRAPEZIODAL weirs|
|Surcharge |string | Can Surcharge | 'YES' or 'NO'|
|CoeffCurve | float | Coeff. Curve | the name of the curve has to be matching to the name in the table for weir curves|
|RoadWidth |float | Road Width | |
|RoadSurf | float | Road Surface | |
|Annotation | string | Description | optional column|

#### Orifices

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|FromNode | string | Inlet Node | |
|ToNode | string | Outlet Node| |
|Type | string | Type | 'SIDE' or 'BOTTOM'|
|XsectShape | string | Shape | 'CIRCULAR' or 'RECT_CLOSED'|
|Height | float | Heigth | in ft or meter|
|Width | float | Width | in ft or meter|
|InOffset | float | Inlet Offset ||
|Qcoeff | float | Discharge Coeff. ||
|FlapGate | string | Flap Gate | 'YES' or 'NO'|
|CloseTime| float | Time to Open/Close | in hours|
|Annotation | string | Description | optional column|

#### Outlets

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|FromNode | string | Inlet Node | |
|ToNode | string | Outlet Node| |
|InOffset | float | Inlet Offset ||
|FlapGate | string | Flap Gate | 'YES' or 'NO'|
|RateCurve  |string | Shape | 'FUNCTIONAL/DEPTH', 'TABULAR/DEPTH', 'FUNCTIONAL/HEAD' or 'TABULAR/HEAD'|
Qcoeff | float | Coefficient | for FUNCTIONAL curves|
Qexpon | float | Exponent | for FUNCTIONAL curves|
CurveName | float | Curve Name | for TABULAR curves; has to be matching with the name in the oulet curves table|
|Annotation | string | Description | optional column|


### Subcatchments 

layer type: point / polygon\
description: Subcatchments can either be points or
polygons. Each subcatchment has to have a unique name (attribute
*Name*). The required fields in the attribute table are:


|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|RainGage | string | Rain Gage | the name of the rain gage|
|Outlet| string | Outlet | the name of the junction into which water of the subcatchment flows|
|Area | float | Area & Area in hectares (or other unit defined in the options table)|
|Imperv | float | % Imperv ||
|Width | float | Width ||
|Slope | float | % Slope ||
|CurbLen | float | Curb Length | Optional parameter needed only for buildup functions (quality)|
|SnowPack | string | Snow Pack |for snow melt analysis only|

*Data for SUBAREAS:*

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|NImperv | float | N-Imperv ||
|NPerv | float | N-Perv ||
|SImperv | float | Dstore-Imperv ||
|SPerv | float | Dstore-Perv ||
|PctZero | float | % Zero-Imperv ||
|RouteTo | float | Subarea Routing | 'OUTLET','PERVIOUS' or 'IMPERVIOUS'|
|PctRouted | float | Percent Routed||
 
*Data for INFILTRATION*[^4]:

|**Name in attribute table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
| InfMethod | string | Infiltration Method |'HORTON', 'MODIFIEDHORTON', 'GREENAMPT', 'MODIFIEDGREENAMPT','CURVENUMBER'; if empty then the infiltration method defined in the options table will be applied|
|MaxRate | float | Max. Infil. Rate | Maximum infiltration rate on the Horton infiltration curve in mm/h or in/h|
|MinRate | float | Min. Infil. Rate | Minimum infiltration rate on the Horton infiltration curve in mm/h or in/h|
|Decay | float | Decay constant | Decay constant for the Horton curve in 1/h|
|DryTime | float | Drying Time | Drying time (number of days it takes a fully saturated soil to dry)|
|MaxInf | float | Max. Volume | Maximum infiltration volume possible (Max. Infil. Vol.) in inches or mm; 0 if not applicable|
|SuctHead | float | Suction head | Suction head in inches or mm|
|Conductiv | float | Conductivity | Soil saturated hydraulic conductivity (in/h or mm/h)|
|InitDef | float | Initial deficit | This is the fraction of soil volume that is initially dry \[0 to 1\]|
|CurveNum | float | SCS curve number | see SWMM Manual for details|
|Annotation | string | Description | optional column|


## Tables 

### Options 

File in default data: gisswmmoptions.xlsx\
Description: You may want to set the options already in
your input file. To do so, you simply write them in a table with two
columns: \"Option\" and \"Value\". So far, **time steps longer than one
day cannot be chosen here**, as the date format in python is in conflict
with the notation in SWMM (e.g. in SWMM a time step of two days will be
written as '48:00:00'. However, Python only accepts 0-23 hours)

### Curves

File in default data: gisswmmcurves.xlsx\
Description: Any type of curves can be imported as a table
in an xlsx file. Each curve type has to be in a seperate sheet/table
named with the curve type. Different curves oft the same type are stored
in the same table by using different names. Just like in the SWMM GUI,
curves always consist of three columns: Name, a x-value and a y-value.
More culomns can be added (e.g. for annotations), but only the first
three columns are relevant for the import into SWMM. Rows beginning with
a semicolon (\";\") will be ignored. Curve types are:

-   Pump1
-   Pump2
-   Pump3
-   Pump4
-   [Pump5]{style="color: blue"}
-   Weir
-   Storage
-   Rating
-   Tidal
-   Control
-   Diversion
-   Shape

Example for a table of two storage curves (where \"Depth\" is the
x-value and \"Area\" is the y-value) :

|**Name** | **Depth** | **Area** |**Annotation**|
|-------|--------|-------|--------|
|StC_1 | 0 | 3 | this is the first storage curve|
|StC_1 | 0.5 | 4 ||
|StC_1 | 1 | 4 ||
|StC_1 | 1.5 | 5 ||
|; | | | this row will be ignored|
|second_StC | 0 | 10 | this is the second storage curve|
|second_StC | 1 | 10 ||
|second_StC | 2 | 11 ||
|second_StC | 3 | 11 ||
|second_StC | 4 | 12 ||

### Timeseries 

File in default data: gisswmmtimeseries.xlsx\
Description: All time series for one SWMM model are saved
in a .xlsx file (any sheet name). For a standard time series you only
fill the columns \"Name\", \"Date\" (optional), \"Time\" and \"Value\"
(See example \"TS_1\" below). Alternatively you can define a time series
in an external data file. Rows beginning with a semicolon (\";\") will
be ignored.\
In former versions of the plugin, rain gages could also be defined with
the time series table by writing 'rain_gage' in the column \"Type\", the
rain format in the column \"Format\" and the name of the rain gage in
the column \"Description\". Starting with version 0.23 of the plugin
this is not possible any longer. Raingages are defined directly in a the
rain gages layer in QGIS\

|**Column in table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
Date | date format | Date | |
Time | time format | Time | |
Value | float | Value | |
File_Name | string | - | file name for external data file; if used, keep \"Date\", \"Time\" and \"Value\" empty (see example TS_2 below)|

Exemplary table for a normal time series and a time series with an
external data file:

|**Name** |**Date** | **Time** | **Value** |**File_Name** |**Annotation**|
| -------------|-----|-----|------|---|---|
|TS_1 | 2021-01-02 | 01:00:00 | 0 | | This is the first time series|
|TS_1 | 2021-01-02 | 01:30:00 | 0 ||
|TS_1 | 2021-01-02 |02:00:00 | 0 ||
|TS_1 | 2021-01-02 | 02:30:00 | 0.2 ||
|TS_1 | 2021-01-02 | 03:00:00 | 0.3 | |
|; | | | | | This line will be ignored|
|TS_2 | | | | external_file.dat | This is the second time series which is using an external data file|


### Patterns

File in default data: gisswmmpatterns.xlsx\
Description: Patterns can be imported in an .xlsx file,
where each pattern type is stored in a separate sheet named after the
pattern type. Patterns of the same type are written in the same table.
Each table consist of three columns: \"Name\", a Time_Stamp column and
\"Factor\". Pattern types are:

-   HOURLY, where the Time_Stamp column is called \"Hour\" (from 0:00 to
    23:00)
-   DAILY, where the Time_Stamp column is called \"Day\" (from Sunday to
    Saturday)
-   MONTHLY, where the Time_Stamp column is called \"Month\" (from
    January to December)
-   WEEKEND, where the Time_Stamp column is called \"Hour\" (from 12AM
    to 11PM)

For example, a table for two DAILY patterns ('p1' and 'p2') will look
like this:

|**Name** | **Day** | **Factor**|
|---|---|---|
|p1 | Sun | 2.0|
|p1 | Mon |1.6|
|p1 | Tue |1.4|
|p1 | Wed | 1.8|
|p1 | Thu | 2.5|
|p1 | Fri | 2.0|
|p1 | Sat | 1.8|
|; |||
|p2 | Sun | 2.8|
|p2 | Mon | 2.7|
|... |... |...|

### Quality

[File in default data]{.smallcaps}: gisswmmquality.xlsx\
[Description]{.smallcaps}: Quality parameters can be imported with a
.xlsx file with the four tables/sheets: 'POLLUTANTS', 'LANDUSES',
'COVERAGES', 'LOADINGS'.

#### POLLUTANTS

|**Column in table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name | |
|Units | string | Units ||
|RainConcentr | float | Rain Concen. ||
|GwConcentr | float | GW Concen. ||
|IiConcentr | float | I&i Concen ||
|DecayCoeff | float |Decay Coeff ||
|SnowOnly | string | Snow Only | 'YES' or 'NO'|
|CoPollutant | string | Co-Pollutant ||
|CoFraction | string | Co-Fraction ||
|DwfConcentr | float | DWF Concen ||
|InitConcetr | float | Init. Concen ||

#### LANDUSES

This sheet sets up buildup and washoff functions for different landuses.
Since one landuse can have more than one pollutant with individual
functions for buildup and washoff, the have defined in different rows of
this sheet (see exemplary table).

|**Column in table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Land Use Name | |
|SweepingInterval | float | Interval | in days|
|SweepingFractionAvailable | float | Availability & between 0 and 1|
|LastSwept | float | Last Swept | in days|
|Pollutant | string | - |
|BuildupFunction | string | Function | 'NONE', 'POW', 'EXP', 'SAT' or 'EXT'|
|BuildupMax | float | Max. Buildup | kg per Normalizer (area or curb length)|
|BuildupRateConstant | float | Rate Constant | |
|BuildupExponentSatConst | float | Power/Sat. Constant ||
|BuildupPerUnit | string | Normalizer | 'AREA' or 'CURB'|
|WashoffFunction | string | Function | 'NONE', 'EXP', 'RC' or 'EMC'|
|WashoffpCoefficient | float | Coefficient ||
|WashoffExponenet | float | Exponent ||
|WashoffCleaninfEfficiency | float | Cleaning Effic. | percent|
|WashoffBmpEfficiency | float | BMP Effic. | percent|


#### COVERAGES

This sheet refers to *Land Uses* in the GUI of subcatchments. As one
subcatchment can have morge than one land use covering its area[^5],
they are defined in the quality table. Example for one subcatchment with
two land use types:

| **Subcatchment** | **Landuse** | **Percent**|
| -------------|-----|-----|
|SC1 | LU_1 | 24.5|
|SC1 | LU_2 | 75.5|


#### LOADINGS

This sheet refers to *Initial Buildup* in the GUI of subcatchments. As
one subcatchment can have morge than one pollutants the initial buildup
is defined in the quality table. Values in the column \"InitialBuildup\"
are mass per area (e.g. kg/ha or lbs/ac). Example for two subcatchments
with two pollutants:


| **Subcatchment** | **Pollutant** |**InitialBuildup**|
| -------------|-----|-----|
|SC1 | COD | 1|
|SC1 | TN | 0.6|
|SC2 | COD | 0.8|
|SC2 | TN | 0.4|


### Inflows

File in default data: gisswmminflows.xlsx\
Description: The .xlsx file for inflows contains four
tables/sheets (older files with two tables will still work).

-   for direct inflow (sheet name: \"Direct\")

-   for dry weather inflow (sheet name: \"Dry_Weather\")

-   for RDII: sheets \"Hydrographs\" and \"RDII\"

More than one constituent can have inflows to a node.

#### Direct

|**Column in table** | **Data type** |**Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name |name of the Node |
|Constituent | string | Constituent | 'FLOW' or name of the pollutant|
|Baseline | float | Baseline ||
|Baseline_Pattern | string | Baseline Pattern ||
|Time_Series | string | Time Series ||
|Scale_Factor | float | Scale Factor ||
|Type & string | Type | \"MASS\", \"CONCEN\"; applies, when Constituent is not FLOW|
|Units_Factor | float | Units Factor ||


#### DryWeather

| **Column in table** | **Data type** | **Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
|Name | string | Name ||
|Constituent | string | Constituent ||
|Average_Value | float | Average Value ||
|Time_Pattern1 | string |||
|Time_Pattern2 | string |||
|Time_Pattern3 | string |||
|Time_Pattern4 | string |||

#### Hydrographs


| **Column in table** | **Data type** | **Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
Name | string | Name of UH Group |
RainGage | string | Rain Gage Used ||
Months | string | Hydrographs For | 'All' or name abbreviation of the month|
RShortTerm | float | R (for short-term response) ||
TShortTerm | float | T (for short-term response) ||
KShortTerm | float | K (for short-term response) ||
DmaxShortTerm | float | Dmax (for short-term response) ||
DrecoveryShortTerm | float | Drec (for short-term response) ||
DinitShortTerm | float | Do (for short-term response) ||
RMediumTerm | float | R (for medium-term response) ||
TMediumTerm | float | T (for medium-term response) ||
KMediumTerm | float | K (for medium-term response) ||
DmaxMediumTerm | float | Dmax (for medium-term response) ||
DrecoveryMediumTerm | float & Drec (for medium-term response) ||
DinitMediumTerm | float | Do (for medium-term response) ||
RLongTerm | float | R (for long-term response) ||
TLongTerm | float | T (for long-term response) ||
KLongTerm | float | K (for long-term response) ||
DmaxLongTerm | float | Dmax (for long-term response) |
DrecoveryLongTerm | float | Drec (for long-term response) ||
DinitLongTerm | float | Do (for long-term response) ||


#### RDII

| **Columns in table** | **Data type** | **Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
Node | string | Constituent | name of the Node|
UnitHydrograph | string | Unit Hydrograph Group ||
SewerArea_Pattern | float | Sewershed Area ||



### Transects

[File in default data]{.smallcaps}: gisswmmtransects.xlsx\
[Description]{.smallcaps}: The .xlsx file for transects (for IRREGULAR
cross-sections) contains two tables/sheets (\"Data\" and \"XSections\"):

#### Data

| **Columns in table** | **Data type** | **Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
TransectName | string | Name |
Station | float | Station |
Elevation | float | Elevation |

#### XSections

| **Columns in table** | **Data type** | **Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
TransectName | string | Name ||
RoughnessLeftBank | float | Left Bank ||
RoughnessRightBank | float | Right Bank ||
RoughnessChannel | float | Channel ||
BankStationLeft | float | Left||
BankStationRight| float | Right ||
ModifierStations | float | Stations ||
ModifierElevations | float | Elevations ||
ModifierMeander | float | Meander ||

### Streets and Inlets

File in default data: gisswmmstreets.xlsx\
Description: [Streets and Inlets are completely new
features in SWMM version 5.2]{style="color: blue"}. The .xlsx file for
streets (for STREET cross-sections) contains three tables/sheets
(\"STREETS\", \"INLETS\" and \"INLETUSAGE\"):

#### STREETS {#sect_streets}

| **Columns in table** | **Data type** | **Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
Name | string | Street Section Name |
RoadWidth | float | Road Width |
CurbHeigth | float | Curb Heigth |
CurbSlope | float | Curb Slope |
RoadRoughn | float | Road Roughness |
GuttDepres | float | Gutter Depression |
GuttWidth | float | Gutter Width |
Sides | int | One Sided / Two Sided | 1 or 2|
BackWidth | float | Backing Width |
BackSlope | float | Backing Slope |
BackRoughn | float | Backing Roughness |


#### INLETS

| **Columns in table** | **Data type** | **Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
Name | string | Name ||
Type | string | Inlet Type | 'GRATE', 'CUSTOM', 'CURB', 'SLOTTED', 'DROPGRATE', 'DROPCURB' or 'CUSTOM'|
Length | float | Length ||
Width | float | Width ||
Heigth | float | Heigth ||
Shape | String | - | Type for GRATE, DROPGRATE inlets; Throat Angle for CURB inlets; Curve name for CUSTOM inlets|
OpenFract | float | Open Fraction ||
SplashVel | float |Splash Velocity ||


#### INLET_USAGE

| **Columns in table** | **Data type** | **Name in SWMM GUI** | **annotations**|
| -------------|-----|-----|------|
Conduit | string | - | Name of the conduit|
Inlet | string | Inlet Structure ||
CaptNode | int | Capture Node | The Name has to be matching to one node name|
Number | float | Number of Inlets | 1 - 5|
PercClog | float | Percent Clogged | 0 - 100|
MaxFlow | float | Flow Restriction | 0 for no flow restriction|
DeprHeigth | float | Depression Height ||
DeprWidth | float | Depression Width ||
Placement | string | Inlet Placement | 'AUTOMATIC', 'ONGRADE' or 'ONSAG'|



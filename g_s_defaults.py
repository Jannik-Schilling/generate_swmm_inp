# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GenerateSwmmInp
                                 A QGIS plugin
 This plugin generates SWMM Input files
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-09
        copyright            : (C) 2022 by Jannik Schilling
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
__date__ = '2022-04-28'
__copyright__ = '(C) 2022 by Jannik Schilling'


class SwmmObject:
    SwmmNodesList = list()
    SwmmLinksList = list()
    SwmmSubcatchmentsList = list()
    SwmmRainGagesList = list()
    
    SwmmSeparatorList = ['    ','\t']
    SwmmSep = SwmmSeparatorList[0]
    

def_curve_types = ['Control',
                   'Pump1',
                   'Pump2',
                   'Pump3',
                   'Pump4',
                   'Pump5',
                   'Storage',
                   'Rating',
                   'Weir',
                   'Tidal',
                   'Diversion',
                   'Shape']

def_infiltr_dtypes = {'InfMethod':'String',
                      'SuctHead':'Double',
                      'Conductiv':'Double',
                      'InitDef':'Double',
                      'MaxRate':'Double',
                      'MinRate':'Double',
                      'Decay':'Double',
                      'DryTime':'Double',
                      'MaxInf':'Double',
                      'CurveNum':'Double'}

"""defaults for the import from .inp files"""
def_sections_dict={'TITLE':None,
         'OPTIONS':['Option', 'Value'],
         'REPORT':None,
         'FILES': None,
         'RAINGAGES':{'Name':'String',
                      'Format':'String',
                      'Interval':'String',
                      'SCF':'Double',
                      'DataSource':'String',
                      'SourceName':'String',
                      'StationID':'String',
                      'RainUnits':'String'},
         'EVAPORATION':None,
         'TEMPERATURE':None,
         'ADJUSTMENTS':None,
         'SUBCATCHMENTS': {'Name':'String',
                           'RainGage':'String', 
                           'Outlet':'String',
                           'Area':'Double', 
                           'Imperv':'Double',
                           'Width':'Double',
                           'Slope':'Double',
                           'CurbLen':'Double',
                           'SnowPack':'String'}, 
         'SUBAREAS':{'Name':'String',
                     'N_Imperv':'Double',
                     'N_Perv':'Double',
                     'S_Imperv':'Double',
                     'S_Perv':'Double',
                     'PctZero':'Double',
                     'RouteTo':'String',
                     'PctRouted':'Double'},
         'INFILTRATION':{'Name':'String',
                         'Param1':'String', 
                         'Param2':'Double',
                         'Param3':'Double',
                         'Param4':'Double',
                         'Param5':'String',
                         'InfMethod':'String'},
         'LID_CONTROLS':None,
         'LID_USAGE':None,
         'AQUIFERS':None,
         'GROUNDWATER':None,
         'GWF':None,
         'SNOWPACKS':None,
         'JUNCTIONS':{'Name':'String',
                      'Elevation':'Double',
                      'MaxDepth':'Double', 
                      'InitDepth':'Double',
                      'SurDepth':'Double', 
                      'Aponded':'Double'},
         'OUTFALLS':{'Name':'String',
                     'Elevation':'Double',
                     'Type':'String',
                     'FixedStage':'Double',
                     'Curve_TS':'String',
                     'FlapGate':'String',
                     'RouteTo':'String'}, 
         'DIVIDERS':{'Name':'String',
                     'Elevation':'Double',
                     'DivertLink':'String',
                     'Type':'String',
                     'CutoffFlow':'Double',
                     'Curve':'String',
                     'WeirMinFlo':'Double',
                     'WeirMaxDep':'Double',
                     'WeirCoeff':'Double',
                     'MaxDepth':'Double',
                     'InitDepth':'Double',
                     'SurDepth':'Double',
                     'Aponded':'Double'},
         'STORAGE':{'Name':'String',
                    'Elevation':'Double',
                    'MaxDepth':'Double',
                    'InitDepth':'Double',
                    'Type':'String',
                    'Curve':'String',
                    'Coeff':'Double',
                    'Exponent':'Double',
                    'Constant':'Double',
                    'MajorAxis':'Double',
                    'MinorAxis':'Double',
                    'SideSlope':'Double',
                    'SurfHeight':'Double',
                    'SurDepth':'Double',
                    'Fevap':'Double',
                    'Psi':'Double',
                    'Ksat':'Double',
                    'IMD':'Double'},
         'CONDUITS': {'Name':'String',
                      'FromNode':'String',
                      'ToNode':'String',
                      'Length':'Double',
                      'Roughness':'Double',
                      'InOffset':'Double',
                      'OutOffset':'Double',
                      'InitFlow':'Double',
                      'MaxFlow':'Double'},
         'PUMPS':{'Name':'String',
                  'FromNode':'String',
                  'ToNode':'String',
                  'PumpCurve':'String',
                  'Status':'String',
                  'Startup':'Double',
                  'Shutoff':'Double'},
         'ORIFICES':{'Name':'String',
                  'FromNode':'String',
                  'ToNode':'String',
                  'Type':'String',
                  'InOffset':'Double',
                  'Qcoeff':'Double',
                  'FlapGate':'String',
                  'CloseTime':'Double'},
         'WEIRS':{'Name':'String',
                  'FromNode':'String',
                  'ToNode':'String',
                  'Type':'String',
                  'CrestHeigh':'Double',
                  'Qcoeff':'Double',
                  'FlapGate':'String',
                  'EndContrac':'Double',
                  'EndCoeff':'Double',
                  'Surcharge':'String',
                  'RoadWidth':'Double',
                  'RoadSurf':'String',
                  'CoeffCurve':'String'},
         'OUTLETS':{'Name':'String',
                  'FromNode':'String',
                  'ToNode':'String',
                  'InOffset':'Double',
                  'RateCurve':'String',
                  'Qcoeff':'Double',
                  'Qexpon':'Double',
                  'FlapGate':'String',
                  'CurveName':'String'},
         'XSECTIONS':{'Name':'String',
                      'Shape':'String',
                      'Geom1':'Double',
                      'Geom2':'Double',
                      'Geom3':'Double',
                      'Geom4':'Double',
                      'Barrels':'Double',
                      'Culvert':'String'},
         'STREETS':{'Name':'String',
                    'RoadWidth':'Double',
                    'CurbHeigth':'Double',
                    'CurbSlope':'Double',
                    'RoadRoughn':'Double',
                    'GuttDepres':'Double',
                    'GuttWidth':'Double',
                    'Sides':'Int',
                    'BackWidth':'Double',
                    'BackSlope':'Double',
                    'BackRoughn':'Double'},
         'INLETS':{'Name':'String',
                   'Type':'String',
                   'Length':'Double',
                   'Width':'Double',
                   'Heigth':'Double',
                   'Shape':'String',
                   'OpenFract':'Double',
                   'SplashVel':'Double'
                   },
         'INLET_USAGE':{'Conduit':'String',
                        'Inlet':'String',
                        'CaptNode':'String',
                        'Number':'Int',
                        'PercClog':'Double',
                        'MaxFlow':'Double',
                        'DeprHeigth':'Double',
                        'DeprWidth':'Double',
                        'Placement':'String'},
         'TRANSECTS':None,
         'LOSSES': {'Name':'String',
                    'Kentry':'Double',
                    'Kexit':'Double',
                    'Kavg':'Double',
                    'FlapGate':'String',
                    'Seepage':'Double'},
         'CONTROLS':None,
         'POLLUTANTS':{'Name':'String',
                       'Units':'String',
                       'RainConcentr':'Double',
                       'GwConcentr':'Double',
                       'IiConcentr':'Double',
                       'DecayCoeff':'Double',
                       'SnowOnly':'String',
                       'CoPollutant':'String',
                       'CoFraction':'Double',
                       'DwfConcentr':'Double',
                       'InitConcetr':'Double'},
         'LANDUSES':{'Name':'String', 
                     'SweepingInterval':'Double', 
                     'SweepingFractionAvailable':'Double', 
                     'LastSwept':'Double'},
         'COVERAGES':{'Subcatchment':'String',
                      'Landuse':'String',
                      'Percent':'Double'},
         'LOADINGS':{'Subcatchment':'String',
                     'Pollutant':'String',
                     'InitialBuildup':'Double'},
         'BUILDUP':{'Name':'String',
                    'Pollutant':'String',
                    'BuildupFunction':'String', 
                    'BuildupMax':'Double', 
                    'BuildupRateConstant':'Double',
                    'BuildupExponent_SatConst':'Double',
                    'BuildupPerUnit':'String'},
         'WASHOFF':{'Name':'String', 
                    'Pollutant':'String',
                    'WashoffFunction':'String',
                    'WashoffpCoefficient':'Double', 
                    'WashoffExponenet':'Double', 
                    'WashoffCleaninfEfficiency':'Double',
                    'WashoffBmpEfficiency':'Double'},
         'TREATMENT':None,
         'INFLOWS':['Name','Constituent','Time_Series',
                    'Type', 'Units_Factor',
                    'Scale_Factor','Baseline', 'Baseline_Pattern'],
         'DWF':['Name','Constituent','Average_Value',
                'Time_Pattern1','Time_Pattern2',
                'Time_Pattern3','Time_Pattern4'],
         'RDII':None,
         'HYDROGRAPHS':None,
         'CURVES':['Name','XVal','YVal'],
         'TIMESERIES':['Name','Date','Time','Value','File_Name'],
         'PATTERNS':None,
         'COORDINATES':['Name','X_Coord','Y_Coord'],
         'VERTICES':['Name','X_Coord','Y_Coord'],
         'Polygons':['Name','X_Coord','Y_Coord'],
         'SYMBOLS':['Name','X_Coord','Y_Coord'],
         'LABELS':None,
         'BACKDROP':None,
         'PROFILES':None,
         'MAP':None,
         'TAGS': None}
                
                
                
def_ogr_driver_dict = {'ESRI Shapefile':'shp',
                        'GPKG':'gpkg',
                        'GML':'gml', 
                        'GeoJSON':'geojson',
                        'KML':'kml'}
def_ogr_driver_names = list(def_ogr_driver_dict.keys())

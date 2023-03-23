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

import os
from qgis.core import QgsGeometry

def_curve_types = [
    'Control',
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
    'Shape'
]

def_infiltration_types = [
    'GREEN_AMPT',
    'MODIFIED_GREEN_AMPT',
    'HORTON',
    'MODIFIED_HORTON',
    'CURVE_NUMBER'
]

# all possible columns in the input file
def_sections_dict = {
    'TITLE': None,
    'OPTIONS': ['Option', 'Value'],
    'REPORT': None,
    'FILES': None,
    'RAINGAGES': [
        'Name',
        'Format',
        'Interval',
        'SCF',
        'DataSource',
        'SourceName',
        'StationID',
        'RainUnits'
     ],
    'EVAPORATION': None,
    'TEMPERATURE': None,
    'ADJUSTMENTS': None,
    'SUBCATCHMENTS': [
        'Name',
        'RainGage',
        'Outlet',
        'Area',
        'Imperv',
        'Width',
        'Slope',
        'CurbLen',
        'SnowPack'
     ],
    'SUBAREAS': [
        'Name',
        'N_Imperv',
        'N_Perv',
        'S_Imperv',
        'S_Perv',
        'PctZero',
        'RouteTo',
        'PctRouted'
    ],
    'INFILTRATION': [
        'Name',
        'Param1',
        'Param2',
        'Param3',
        'Param4',
        'Param5',
        'InfMethod'
    ],
    'LID_CONTROLS': None,
    'LID_USAGE': None,
    'AQUIFERS': None,
    'GROUNDWATER': None,
    'GWF': None,
    'SNOWPACKS': None,
    'JUNCTIONS': [
        'Name',
        'Elevation',
        'MaxDepth',
        'InitDepth',
        'SurDepth',
        'Aponded'
    ],
    'OUTFALLS': [
        'Name',
        'Elevation',
        'Type',
        'FixedStage',
        'Curve_TS',
        'FlapGate',
        'RouteTo'
    ],
    'DIVIDERS': [
        'Name',
        'Elevation',
        'DivertLink',
        'Type',
        'CutoffFlow',
        'Curve',
        'WeirMinFlo',
        'WeirMaxDep',
        'WeirCoeff',
        'MaxDepth',
        'InitDepth',
        'SurDepth',
        'Aponded'
    ],
    'STORAGE': [
        'Name',
        'Elevation',
        'MaxDepth',
        'InitDepth',
        'Type',
        'Curve',
        'Coeff',
        'Exponent',
        'Constant',
        'MajorAxis',
        'MinorAxis',
        'SideSlope',
        'SurfHeight',
        'SurDepth',
        'Fevap',
        'Psi',
        'Ksat',
        'IMD'
    ],
    'CONDUITS': [
        'Name',
        'FromNode',
        'ToNode',
        'Length',
        'Roughness',
        'InOffset',
        'OutOffset',
        'InitFlow',
        'MaxFlow'
    ],
    'PUMPS': [
        'Name',
        'FromNode',
        'ToNode',
        'PumpCurve',
        'Status',
        'Startup',
        'Shutoff'
    ],
    'ORIFICES': [
        'Name',
        'FromNode',
        'ToNode',
        'Type',
        'InOffset',
        'Qcoeff',
        'FlapGate',
        'CloseTime'
    ],
    'WEIRS': [
        'Name',
        'FromNode',
        'ToNode',
        'Type',
        'CrestHeigh',
        'Qcoeff',
        'FlapGate',
        'EndContrac',
        'EndCoeff',
        'Surcharge',
        'RoadWidth',
        'RoadSurf',
        'CoeffCurve'
    ],
    'OUTLETS': [
        'Name',
        'FromNode',
        'ToNode',
        'InOffset',
        'RateCurve',
        'Qcoeff',
        'Qexpon',
        'FlapGate',
        'CurveName'
    ],
    'XSECTIONS': [
        'Name',
        'Shape',
        'Geom1',
        'Geom2',
        'Geom3',
        'Geom4',
        'Barrels',
        'Culvert'
    ],
    'STREETS': [
        'Name',
        'RoadWidth',
        'CurbHeigth',
        'CurbSlope',
        'RoadRoughn',
        'GuttDepres',
        'GuttWidth',
        'Sides',
        'BackWidth',
        'BackSlope',
        'BackRoughn'
    ],
    'INLETS': [
        'Name',
        'Type',
        'Length',
        'Width',
        'Heigth',
        'Shape',
        'OpenFract',
        'SplashVel'
    ],
    'INLET_USAGE': [
        'Conduit',
        'Inlet',
        'CaptNode',
        'Number',
        'PercClog',
        'MaxFlow',
        'DeprHeigth',
        'DeprWidth',
        'Placement'
    ],
    'TRANSECTS': None,
    'LOSSES': [
        'Name',
        'Kentry',
        'Kexit',
        'Kavg',
        'FlapGate',
        'Seepage'
    ],
    'CONTROLS': None,
    'POLLUTANTS': [
        'Name',
        'Units',
        'RainConcentr',
        'GwConcentr',
        'IiConcentr',
        'DecayCoeff',
        'SnowOnly',
        'CoPollutant',
        'CoFraction',
        'DwfConcentr',
        'InitConcetr'
    ],
    'LANDUSES': [
        'Name',
        'SweepingInterval',
        'SweepingFractionAvailable',
        'LastSwept'
    ],
    'COVERAGES': [
        'Subcatchment',
        'Landuse',
        'Percent'
    ],
    'LOADINGS': [
        'Subcatchment',
        'Pollutant',
        'InitialBuildup'
    ],
    'BUILDUP': [
        'Name',
        'Pollutant',
        'BuildupFunction',
        'BuildupMax',
        'BuildupRateConstant',
        'BuildupExponent_SatConst',
        'BuildupPerUnit'
    ],
    'WASHOFF': [
        'Name',
        'Pollutant',
        'WashoffFunction',
        'WashoffpCoefficient',
        'WashoffExponenet',
        'WashoffCleaninfEfficiency',
        'WashoffBmpEfficiency'
    ],
    'TREATMENT': None,
    'INFLOWS': [
        'Name',
        'Constituent',
        'Time_Series',
        'Type',
        'Units_Factor',
        'Scale_Factor',
        'Baseline',
        'Baseline_Pattern'
    ],
    'DWF': [
        'Name',
        'Constituent',
        'Average_Value',
        'Time_Pattern1',
        'Time_Pattern2',
        'Time_Pattern3',
        'Time_Pattern4'
    ],
    'RDII': [
        'Node',
        'UnitHydrograph',
        'SewerArea'
    ],
    'HYDROGRAPHS': [
        'Name',
        'RG_Month',
        'Response',
        'R',
        'T',
        'K',
        'D_max',
        'D_recovery',
        'D_init'
    ],
    'CURVES': ['Name', 'XVal', 'YVal'],
    'TIMESERIES': ['Name', 'Date', 'Time', 'Value', 'File_Name'],
    'PATTERNS': None,
    'COORDINATES': ['Name', 'X_Coord', 'Y_Coord'],
    'VERTICES': ['Name', 'X_Coord', 'Y_Coord'],
    'Polygons': ['Name', 'X_Coord', 'Y_Coord'],
    'SYMBOLS': ['Name', 'X_Coord', 'Y_Coord'],
    'LABELS': None,
    'BACKDROP': None,
    'PROFILES': None,
    'MAP': None,
    'TAGS': None
}


# names of the imported tables
"""
    'file_key': {
        'filename': 'name_str',
        'tables': {
            'table_name': {
                'column_name': 'type_str',
                'column_name': ['excel_type_str, gpkg_type_str']
            }
        }
    }
"""
def_tables_dict = {
    'OPTIONS': {
        'filename': 'gisswmm_options',
        'tables': {
            'OPTIONS': {
                'Option': 'String',
                'Value': 'String'
            }
        }
     },
    'INFLOWS': {
        'filename': 'gisswmm_inflows',
        'tables': {
            'Direct': {
                'Name': 'String',
                'Constituent': 'String',
                'Time_Series': 'String',
                'Type': 'String',
                'Units_Factor': 'Double',
                'Scale_Factor': 'Double',
                'Baseline': 'Double',
                'Baseline_Pattern': 'String'
            },
            'Dry_Weather': {
                'Name': 'String',
                'Constituent': 'String',
                'Average_Value': 'Double',
                'Time_Pattern1': 'String',
                'Time_Pattern2': 'String',
                'Time_Pattern3': 'String',
                'Time_Pattern4': 'String'
            },
            'RDII': {
                'Node': 'String',
                'UnitHydrograph': 'String',
                'SewerArea': 'Double'
            },
            'Hydrographs': {
                'Name': 'String',
                'Rain_Gage': 'String',
                'Months': 'String',
                'R_ShortTerm': 'Double',
                'T_ShortTerm': 'Double',
                'K_ShortTerm': 'Double',
                'D_max_ShortTerm': 'Double',
                'D_recovery_ShortTerm': 'Double',
                'D_init_ShortTerm': 'Double',
                'R_MediumTerm': 'Double',
                'T_MediumTerm': 'Double',
                'K_MediumTerm': 'Double',
                'D_max_MediumTerm': 'Double',
                'D_recovery_MediumTerm': 'Double',
                'D_init_MediumTerm': 'Double',
                'R_LongTerm': 'Double',
                'T_LongTerm': 'Double',
                'K_LongTerm': 'Double',
                'D_max_LongTerm': 'Double',
                'D_recovery_LongTerm': 'Double',
                'D_init_LongTerm': 'Double'
            }
        }
     },
    'PATTERNS': {
        'filename': 'gisswmm_patterns',
        'tables': {
            'HOURLY': {
                'Name': 'String',
                'Time': 'String',
                'Factor': 'Double'
            },
            'MONTHLY': {
                'Name': 'String',
                'Month': 'String',
                'Factor': 'Double'
            },
            'DAILY': {
                'Name': 'String',
                'Day': 'String',
                'Factor': 'Double'
            },
            'WEEKEND': {
                'Name': 'String',
                'Time': 'String',
                'Factor': 'Double'
            }
        }
    },
    'CURVES': {
        'filename': 'gisswmm_curves',
        'tables': {
            'Pump1': {
                'Name': 'String',
                'Volume': 'Double',
                'Flow': 'Double'
            },
            'Pump2': {
                'Name': 'String',
                'Depth': 'Double',
                'Flow': 'Double'
            },
            'Pump3': {
                'Name': 'String',
                'Head': 'Double',
                'Flow': 'Double'
            },
            'Pump4': {
                'Name': 'String',
                'Depth': 'Double',
                'Flow': 'Double'
            },
            'Pump5': {
                'Name': 'String',
                'Head': 'Double',
                'Flow': 'Double'
            },
            'Storage': {
                'Name': 'String',
                'Depth': 'Double',
                'Area': 'Double'
            },
            'Rating': {
                'Name': 'String',
                'Head/Depth': 'Double',
                'Outflow': 'Double'
            },
            'Tidal': {
                'Name': 'String',
                'Hour_of_Day': 'Int',
                'Stage': 'Double'
            },
            'Control': {
                'Name': 'String',
                'Value': 'Double',
                'Setting': 'Double'
            },
            'Diversion': {
                'Name': 'String',
                'Inflow': 'Double',
                'Outflow': 'Double'
            },
            'Shape': {
                'Name': 'String',
                'Depth': 'Double',
                'Width': 'Double'
            },
            'Weir': {
                'Name': 'String',
                'Head': 'Double',
                'Coefficient': 'Double'
            }
        }
    },
    'QUALITY': {
        'filename': 'gisswmm_quality',
        'tables': {
            'POLLUTANTS': {
                'Name': 'String',
                'Units': 'String',
                'RainConcentr': 'Double',
                'GwConcentr': 'Double',
                'IiConcentr': 'Double',
                'DecayCoeff': 'Double',
                'SnowOnly': 'String',
                'CoPollutant': 'String',
                'CoFraction': 'Double',
                'DwfConcentr': 'Double',
                'InitConcetr': 'Double'
            },
            'LANDUSES': {
                'Name': 'String',
                'SweepingInterval': 'Double',
                'SweepingFractionAvailable': 'Double',
                'LastSwept': 'Double',
                'Pollutant': 'String',
                'BuildupFunction': 'String',
                'BuildupMax': 'Double',
                'BuildupRateConstant': 'Double',
                'BuildupExponent_SatConst': 'Double',
                'BuildupPerUnit': 'String',
                'WashoffFunction': 'String',
                'WashoffpCoefficient': 'Double',
                'WashoffExponenet': 'Double',
                'WashoffCleaninfEfficiency': 'Double',
                'WashoffBmpEfficiency': 'Double'
            },
            'COVERAGES': {
                'Subcatchment': 'String',
                'Landuse': 'String',
                'Percent': 'Double'
            },
            'LOADINGS': {
                'Subcatchment': 'String',
                'Pollutant': 'String',
                'InitialBuildup': 'Double'
            }
        }
    },
    'TIMESERIES': {
        'filename': 'gisswmm_timeseries',
        'tables': {
            'TIMESERIES': {
                'Name': 'String',
                'Date': 'Date',
                'Time': 'Time',
                'Value': 'Double',
                'File_Name': 'String'
            }
        }
    },
    'TRANSECTS': {
        'filename': 'gisswmm_transects',
        'tables': {
            'Data': {
                'TransectName': 'String',
                'RoughnessLeftBank': 'Double',
                'RoughnessRightBank': 'Double',
                'RoughnessChannel': 'Double',
                'BankStationLeft': 'Double',
                'BankStationRight': 'Double',
                'ModifierStations': 'Double',
                'ModifierElevations': 'Double',
                'ModifierMeander': 'Double'
            },
            'XSections': {
                'TransectName': 'String',
                'Station': 'Double',
                'Elevation': 'Double'
            }
        }
    },
    'STREETS': {
        'filename': 'gisswmm_streets',
        'tables': {
            'STREETS': {
                'Name': 'String',
                'RoadWidth': 'Double',
                'CurbHeigth': 'Double',
                'CurbSlope': 'Double',
                'RoadRoughn': 'Double',
                'GuttDepres': 'Double',
                'GuttWidth': 'Double',
                'Sides': 'Int',
                'BackWidth': 'Double',
                'BackSlope': 'Double',
                'BackRoughn': 'Double'
            },
            'INLETS': {
                'Name': 'String',
                'Type': 'String',
                'Length': 'Double',
                'Width': 'Double',
                'Heigth': 'Double',
                'Shape': 'String',
                'OpenFract': 'Double',
                'SplashVel': 'Double'
            },
            'INLET_USAGE': {
                'Conduit': 'String',
                'Inlet': 'String',
                'CaptNode': 'String',
                'Number': 'Int',
                'PercClog': 'Double',
                'MaxFlow': 'Double',
                'DeprHeigth': 'Double',
                'DeprWidth': 'Double',
                'Placement': 'String'
            }
        }
    }
}


# geometries of SWMM layers in QGIS
def_sections_geoms_dict = {
    'RAINGAGES': 'Point',
    'SUBCATCHMENTS': 'Polygon',
    'JUNCTIONS': 'Point',
    'OUTFALLS': 'Point',
    'DIVIDERS': 'Point',
    'STORAGE': 'Point',
    'CONDUITS': 'LineString',
    'PUMPS': 'LineString',
    'ORIFICES': 'LineString',
    'WEIRS': 'LineString',
    'OUTLETS': 'LineString'
}

# style_file
def_stylefile_dict = {
    'st_files': {
        'RAINGAGES': 'style_raingages.qml',
        'SUBCATCHMENTS': 'style_catchments.qml',
        'JUNCTIONS': 'style_junctions.qml',
        'OUTFALLS': 'style_outfalls.qml',
        'DIVIDERS': 'style_dividers.qml',
        'STORAGE': 'style_storages.qml',
        'CONDUITS': 'style_conduits.qml',
        'PUMPS': 'style_pumps.qml',
        'ORIFICES': 'style_orifices.qml',
        'WEIRS': 'style_weirs.qml',
        'OUTLETS': 'style_outlets.qml'
    },
    'st_files_path': os.path.join('test_data', 'swmm_data')
}

# default raingage coord
def_rg_geom = QgsGeometry.fromWkt(
        'POINT(' + str(0) + ' '+str(0) + ')'
    )

# all possible fields in qgis files for the creation of layers
def_annotation_field = {'Annotation': 'String'}
annotation_field_name = list(def_annotation_field.keys())[0]

def_qgis_fields_dict = {
    'RAINGAGES': {
        'Name': 'String',
        'Format': 'String',
        'Interval': 'String',
        'SCF': 'Double',
        'DataSource': 'String',
        'SeriesName': 'String',
        'FileName': 'String',
        'StationID': 'String',
        'RainUnits': 'String'
    },
    'SUBCATCHMENTS': {
        'Name': 'String',
        'RainGage': 'String',
        'Outlet': 'String',
        'Area': 'Double',
        'Imperv': 'Double',
        'Width': 'Double',
        'Slope': 'Double',
        'CurbLen': 'Double',
        'SnowPack': 'String',
        'N_Imperv': 'Double',
        'N_Perv': 'Double',
        'S_Imperv': 'Double',
        'S_Perv': 'Double',
        'PctZero': 'Double',
        'RouteTo': 'String',
        'PctRouted': 'Double',
        'InfMethod': 'String',
        'SuctHead': 'Double',
        'Conductiv': 'Double',
        'InitDef': 'Double',
        'MaxRate': 'Double',
        'MinRate': 'Double',
        'Decay': 'Double',
        'DryTime': 'Double',
        'MaxInf': 'Double',
        'CurveNum': 'Double'
    },
    'JUNCTIONS': {
        'Name': 'String',
        'Elevation': 'Double',
        'MaxDepth': 'Double',
        'InitDepth': 'Double',
        'SurDepth': 'Double',
        'Aponded': 'Double'
    },
    'OUTFALLS': {
        'Name': 'String',
        'Elevation': 'Double',
        'Type': 'String',
        'FixedStage': 'Double',
        'Curve_TS': 'String',
        'FlapGate': 'String',
        'RouteTo': 'String'
    },
    'DIVIDERS': {
        'Name': 'String',
        'Elevation': 'Double',
        'DivertLink': 'String',
        'Type': 'String',
        'CutoffFlow': 'Double',
        'Curve': 'String',
        'WeirMinFlo': 'Double',
        'WeirMaxDep': 'Double',
        'WeirCoeff': 'Double',
        'MaxDepth': 'Double',
        'InitDepth': 'Double',
        'SurDepth': 'Double',
        'Aponded': 'Double'
    },
    'STORAGE': {
        'Name': 'String',
        'Elevation': 'Double',
        'MaxDepth': 'Double',
        'InitDepth': 'Double',
        'Type': 'String',
        'Curve': 'String',
        'Coeff': 'Double',
        'Exponent': 'Double',
        'Constant': 'Double',
        'MajorAxis': 'Double',
        'MinorAxis': 'Double',
        'SideSlope': 'Double',
        'SurfHeight': 'Double',
        'SurDepth': 'Double',
        'Fevap': 'Double',
        'Psi': 'Double',
        'Ksat': 'Double',
        'IMD': 'Double'
    },
    'CONDUITS': {
        'Name': 'String',
        'FromNode': 'String',
        'ToNode': 'String',
        'Length': 'Double',
        'Roughness': 'Double',
        'InOffset': 'Double',
        'OutOffset': 'Double',
        'InitFlow': 'Double',
        'MaxFlow': 'Double',
        'Shape': 'String',
        'Geom1': 'Double',
        'Geom2': 'Double',
        'Geom3': 'Double',
        'Geom4': 'Double',
        'Barrels': 'Double',
        'Culvert': 'String',
        'Shp_Trnsct': 'String',
        'Kentry': 'Double',
        'Kexit': 'Double',
        'Kavg': 'Double',
        'FlapGate': 'String',
        'Seepage': 'Double'
    },
    'PUMPS': {
        'Name': 'String',
        'FromNode': 'String',
        'ToNode': 'String',
        'PumpCurve': 'String',
        'Status': 'String',
        'Startup': 'Double',
        'Shutoff': 'Double'
    },
    'ORIFICES': {
        'Name': 'String',
        'FromNode': 'String',
        'ToNode': 'String',
        'Type': 'String',
        'InOffset': 'Double',
        'Qcoeff': 'Double',
        'FlapGate': 'String',
        'CloseTime': 'Double',
        'Shape': 'String',
        'Height': 'Double',
        'Width': 'Double'
    },
    'WEIRS': {
        'Name': 'String',
        'FromNode': 'String',
        'ToNode': 'String',
        'Type': 'String',
        'CrestHeigh': 'Double',
        'Qcoeff': 'Double',
        'FlapGate': 'String',
        'EndContrac': 'Double',
        'EndCoeff': 'Double',
        'Surcharge': 'String',
        'RoadWidth': 'Double',
        'RoadSurf': 'String',
        'CoeffCurve': 'String',
        'Height': 'Double',
        'Length': 'Double',
        'SideSlope': 'Double'
    },
    'OUTLETS': {
        'Name': 'String',
        'FromNode': 'String',
        'ToNode': 'String',
        'InOffset': 'Double',
        'RateCurve': 'String',
        'Qcoeff': 'Double',
        'Qexpon': 'Double',
        'FlapGate': 'String',
        'CurveName': 'String'
    },
}

# driver list for the import function
def_ogr_driver_dict = {
    'ESRI Shapefile': 'shp',
    'GPKG': 'gpkg',
    'FlatGeobuf':'fgb',
    'GML': 'gml',
    'GeoJSON': 'geojson',
    'KML': 'kml'
}
def_ogr_driver_names = list(def_ogr_driver_dict.keys())

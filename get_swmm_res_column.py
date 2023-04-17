import os
import pandas as pd
import numpy as np
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from pyswmm import Output
from swmm.toolkit.shared_enum import (
    LinkAttribute,
    NodeAttribute,
    SubcatchAttribute,
    SystemAttribute
)


current_layer = [layer]
if 'Name' in current_layer.fields().names():
    name_list = [f['Name'] for f in current_layer.getFeatures()]
else:
    raise BaseException('Missing column \"Name\"')


'''
out_request = {
    'outfile': 'C:\\Q_GIS_Projekte\\Projekte\\SWMM_Dummerstorf\\Modelle\\20230302_ZN_GW_kl_100cm_Aq_5.out',
    'layer': 'JUNCTIONS',
    'obj_names': name_list,
    'attr': 0,
    'aggregate': 0
    }
'''

# This loads the .ui file
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__),
    'custom_interface',
    'get_res_all.ui')
)

swmm_obj_types = {
    #'RAINGAGE': 'SYSTEM',
    'SUBCATCHMENTS': 'SUBCATCH',
    'JUNCTIONS': 'NODE',
    'OUTFALLS': 'NODE',
    'DIVIDERS': 'NODE',
    'STORAGE': 'NODE',
    'CONDUITS': 'LINK',
    'PUMPS': 'LINK',
    'ORIFICES': 'LINK',
    'WEIRS': 'LINK',
    'OUTLETS': 'LINK'
}

result_aggregates = {
    0: 'sum',
    1: 'mean',
    2: 'median',
    3: 'max',
    4: 'min'
}

nodes_attrs = {
    0: [NodeAttribute.FLOODING_LOSSES, 'q'],
    1: [NodeAttribute.HYDRAULIC_HEAD, 'd'],
    2: [NodeAttribute.INVERT_DEPTH, 'd'],
    3: [NodeAttribute.LATERAL_INFLOW, 'q'],
    4: [NodeAttribute.POLLUT_CONC_0, None],
    5: [NodeAttribute.PONDED_VOLUME, 'vol'],
    6: [NodeAttribute.TOTAL_INFLOW, 'q']
}
link_attrs = {
    0: [LinkAttribute.FLOW_RATE, 'q'],
    1: [LinkAttribute.FLOW_DEPTH, 'd'],
    2: [LinkAttribute.FLOW_VELOCITY,'vel'],
    3: [LinkAttribute.FLOW_VOLUME,'vol'],
    4: [LinkAttribute.CAPACITY, None],
    5: [LinkAttribute.POLLUT_CONC_0, None]
}
subcatch_attrs = {
    0: [SubcatchAttribute.EVAP_LOSS, 'q_d'],
    1: [SubcatchAttribute.GW_OUTFLOW_RATE, 'q'],
    2: [SubcatchAttribute.GW_TABLE_ELEV, 'd'],
    3: [SubcatchAttribute.INFIL_LOSS, 'q_hr'],
    4: [SubcatchAttribute.POLLUT_CONC_0, None],
    5: [SubcatchAttribute.RAINFALL, 'q_hr'],
    6: [SubcatchAttribute.RUNOFF_RATE, 'q'],
    7: [SubcatchAttribute.SNOW_DEPTH, 'd'],
    8: [SubcatchAttribute.SOIL_MOISTURE, None]
}


def agg_ts(dat_list, agg_type):
    dat_list = list(dat_list)
    if agg_type == 0:
        df_agg = sum(dat_list)
    elif agg_type == 1:
        df_agg = np.mean(dat_list)
    elif agg_type == 2:
        df_agg = np.median(dat_list)
    elif agg_type == 3:
        df_agg = max(dat_list)
    elif agg_type == 4:
        df_agg = min(dat_list)
    else:
        raise BaseException('Unbekannte Aggregation')
    df_agg = round(df_agg, 4)
    return df_agg

def get_node_ts(obj_name, agg_type, out, req_attr):
    if obj_name in out.nodes.keys():
        result_ts = out.node_series(
            obj_name, 
            req_attr
        )
        result_agg = agg_ts(result_ts.values(), agg_type)
        return result_agg
    else:
        raise ValueError('Objekt nicht in den Ergebnissen')

def get_link_ts(obj_name, agg_type, out, req_attr):
    if obj_name in out.links.keys():
        result_ts = out.link_series(
            obj_name, 
            req_attr
        )
        result_agg = agg_ts(result_ts.values(), agg_type)
        return result_agg
    else:
        raise ValueError('Objekt nicht in den Ergebnissen')

def get_subc_ts(obj_name, agg_type, out, req_attr):
    if out_request['obj_name'] in out.subcatchments.keys():
        result_ts = out.subcatch_series(
            out_request['obj_name'], 
            req_attr
        )
        result_agg = agg_ts(result_ts.values(), agg_type)
        return result_agg
    else:
        raise ValueError('Objekt nicht in den Ergebnissen')

def get_results(out_request):
    with Output(out_request['outfile']) as out:
        swmm_units = out.units
        swmm_units_flow = swmm_units['flow']
        swmm_units_system = swmm_units['system']
        swmm_units_pollutants = swmm_units['pollutant']
        req_swmm_type = swmm_obj_types[out_request['layer']]
        agg_type = out_request['aggregate']
        if req_swmm_type == 'NODE':
            req_attr = nodes_attrs[out_request['attr']][0]
            req_unit_type = nodes_attrs[out_request['attr']][1]
            res_dict = {obj_name: get_node_ts(obj_name, agg_type, out, req_attr) for obj_name in out_request['obj_names']}
        elif req_swmm_type == 'LINK':
            req_attr = link_attrs[out_request['attr']][0]
            req_unit_type = link_attrs[out_request['attr']][1]
            res_dict = {obj_name: get_link_ts(obj_name, agg_type, out, req_attr) for obj_name in out_request['obj_names']}
        elif req_swmm_type == 'SUBCATCH':
            req_attr = subcatch_attrs[out_request['attr']][0]
            req_unit_type = subcatch_attrs[out_request['attr']][1]
            res_dict = {obj_name: get_subc_ts(obj_name, agg_type, out, req_attr) for obj_name in out_request['obj_names']}
        #elif req_swmm_type == 'SYSTEM':
        #    req_attr = SystemAttribute.RAINFALL
        else:
            raise BaseException('Unbekannter SWMM-Objekttyp')



class getSwmmResDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(getSwmmResDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        #self.out_file.fileChanged.connect(self.check_dp_path)
        
        self.layer_sel_box.currentData()
        self.layer_sel_box.currentIndexChanged.connect(self.apply_filter)
        
        out_request = {
            'outfile': self.out_file.filePath(),
            'layer': layer_sel_box.currentText(),
            'obj_names': name_list,
            'attr': self.aggregate_box.currentIndex(),
            'aggregate': self.aggregate_box.currentIndex()
            }
        
        def update_attrs(self):
            self.combo_box2.clear()
            d_type = swmm_obj_types(self.layer_sel_box.currentText())
            #if d_type == 'SYSTEM':
            #    self.attr_select_box.addItems(['a'])
            if dtype == 'SUBCATCH':
                val_list = [x[0].name for x in subcatch_attrs.values()]
                self.attr_select_box.addItems(val_list)
            if dtype == 'NODE':
                val_list = [x[0].name for x in nodes_attrs.values()]
                self.attr_select_box.addItems(val_list)
            if dtype == 'LINK':
                val_list = [x[0].name for x in link_attrs.values()]
                self.attr_select_box.addItems(val_list)



class progressbarWindow(QtWidgets.QDialog, FORM_CLASS2):
    def __init__(self, parent=None):
        """Constructor."""
        super(progressbarWindow, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        #self.out_file.fileChanged.connect(self.check_dp_path)
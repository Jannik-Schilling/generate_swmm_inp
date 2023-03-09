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
import matplotlib.pyplot as plt




'''
out_request = {
    'outfile': 'C:\\Q_GIS_Projekte\\Projekte\\Testgebiet\\SWMM\\0_2_dev-gisdata\\Test_5_2.out',
    'layer': 'CONDUITS',
    'obj_name': 'C_1',
    'attr': 0,
    }
    
ts = get_results(out_request)
df = pd.DataFrame(ts.items())
plt.plot(df[0],df[1])
plt.show()
'''

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__),
    'custom_interface',
    'get_res_timeseries.ui')
)

'''
# This loads the .ui file
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    'C:\\Q_GIS_Projekte\\Projekte\\Testgebiet\\SWMM\\generate_swmm_inp',
    'custom_interface',
    'get_res_timeseries.ui')
)
'''

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



def get_node_ts(obj_name, out, req_attr):
    if obj_name in out.nodes.keys():
        result_ts = out.node_series(
            obj_name, 
            req_attr
        )
        return result_ts
    else:
        raise ValueError('Objekt nicht in den Ergebnissen')

def get_link_ts(obj_name, out, req_attr):
    if obj_name in out.links.keys():
        result_ts = out.link_series(
            obj_name, 
            req_attr
        )
        return result_ts
    else:
        raise ValueError('Objekt nicht in den Ergebnissen')

def get_subc_ts(obj_name, out, req_attr):
    if out_request['obj_name'] in out.subcatchments.keys():
        result_ts = out.subcatch_series(
            out_request['obj_name'], 
            req_attr
        )
        return result_ts
    else:
        raise ValueError('Objekt nicht in den Ergebnissen')

def get_results(out_request):
    with Output(out_request['outfile']) as out:
        swmm_units = out.units
        swmm_units_flow = swmm_units['flow']
        swmm_units_system = swmm_units['system']
        swmm_units_pollutants = swmm_units['pollutant']
        req_swmm_type = swmm_obj_types[out_request['layer']]
        if req_swmm_type == 'NODE':
            req_attr = nodes_attrs[out_request['attr']][0]
            req_unit_type = nodes_attrs[out_request['attr']][1]
            result_ts = get_node_ts(out_request['obj_name'], out, req_attr)
        elif req_swmm_type == 'LINK':
            req_attr = link_attrs[out_request['attr']][0]
            req_unit_type = link_attrs[out_request['attr']][1]
            result_ts = get_link_ts(out_request['obj_name'], out, req_attr)
        elif req_swmm_type == 'SUBCATCH':
            req_attr = subcatch_attrs[out_request['attr']][0]
            req_unit_type = subcatch_attrs[out_request['attr']][1]
            result_ts = get_subc_ts(out_request['obj_name'], out, req_attr)
        #elif req_swmm_type == 'SYSTEM':
        #    req_attr = SystemAttribute.RAINFALL
        else:
            raise BaseException('Unbekannter SWMM-Objekttyp')
        return result_ts



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
        
        #self.layer_sel_box.currentData()
        
        self.out_request = {
            'outfile': self.out_file.filePath(),
            'layer': self.layer_sel_box.currentText(),
            'obj_name': obj_name,
            'attr': self.attr_select_box.currentIndex(),
            }
    
    def update_attrs(self):
        self.attr_select_box.clear()
        d_type = swmm_obj_types[self.layer_sel_box.currentText()]
        # print(d_type)
        #if d_type == 'SYSTEM':
        #    self.attr_select_box.addItems(['a'])
        if d_type == 'SUBCATCH':
            val_list = [x[0].name for x in subcatch_attrs.values()]
            self.attr_select_box.addItems(val_list)
        if d_type == 'NODE':
            val_list = [x[0].name for x in nodes_attrs.values()]
            self.attr_select_box.addItems(val_list)
        if d_type == 'LINK':
            val_list = [x[0].name for x in link_attrs.values()]
            self.attr_select_box.addItems(val_list)
    
    self.layer_sel_box.currentIndexChanged.connect(self.update_attrs)
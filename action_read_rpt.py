from generate_swmm_inp.add_report_show_tabel import joinSwmmReportDialog

swmm_layer = QgsProject.instance().mapLayer('[% @layer_id %]')

swmm_geom_types = {
    0: 'NODES',
    1: 'LINKS',
    2: 'SUBCATCHMENTS'
}

layer_geom = swmm_layer.geometryType()

if layer_geom in swmm_geom_types.keys():
    swmm_type = swmm_geom_types[layer_geom]
    w = joinSwmmReportDialog(swmm_layer,swmm_type)
    w.show()

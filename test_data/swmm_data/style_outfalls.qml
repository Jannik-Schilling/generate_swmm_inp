<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.22.7-Białowieża" styleCategories="Symbology|Labeling|Forms" labelsEnabled="0">
  <renderer-v2 forceraster="0" type="singleSymbol" referencescale="-1" symbollevels="0" enableorderby="0">
    <symbols>
      <symbol clip_to_extent="1" alpha="1" force_rhr="0" type="marker" name="0">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <Option type="Map">
            <Option value="0" type="QString" name="angle"/>
            <Option value="square" type="QString" name="cap_style"/>
            <Option value="0,254,8,255" type="QString" name="color"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="triangle" type="QString" name="name"/>
            <Option value="0,0.59999999999999998" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="no" type="QString" name="outline_style"/>
            <Option value="0" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="3.6" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop k="angle" v="0"/>
          <prop k="cap_style" v="square"/>
          <prop k="color" v="0,254,8,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="0,0.59999999999999998"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="no"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3.6"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="offset">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="'0'|| ',' || tostring(0.166667*(if( @map_scale> 6000 ,max(3.6*6000/@map_scale,2),3.6)))" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
                <Option type="Map" name="size">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="if( @map_scale> 6000 ,max(3.6*6000/@map_scale,2),3.6)" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Elevation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="FIXED" type="QString" name="FIXED"/>
              </Option>
              <Option type="Map">
                <Option value="FREE" type="QString" name="FREE"/>
              </Option>
              <Option type="Map">
                <Option value="NORMAL" type="QString" name="NORMAL"/>
              </Option>
              <Option type="Map">
                <Option value="TIDAL" type="QString" name="TIDAL"/>
              </Option>
              <Option type="Map">
                <Option value="TIMESERIES" type="QString" name="TIMESERIES"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="FixedStage">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Curve_TS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="FlapGate">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option value="NO" type="QString" name="NO"/>
              <Option value="YES" type="QString" name="YES"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="RouteTo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>tablayout</editorlayout>
  <attributeEditorForm>
    <attributeEditorField showLabel="1" index="0" name="fid"/>
    <attributeEditorField showLabel="1" index="1" name="Name"/>
    <attributeEditorField showLabel="1" index="2" name="Elevation"/>
    <attributeEditorField showLabel="1" index="6" name="FlapGate"/>
    <attributeEditorField showLabel="1" index="7" name="RouteTo"/>
    <attributeEditorField showLabel="1" index="3" name="Type"/>
    <attributeEditorContainer showLabel="0" visibilityExpressionEnabled="1" name="Tidal or Timeseries" columnCount="1" groupBox="1" visibilityExpression=" &quot;Type&quot; in ('TIDAL','TIMESERIES')">
      <attributeEditorField showLabel="1" index="5" name="Curve_TS"/>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="0" visibilityExpressionEnabled="1" name="Fixed" columnCount="1" groupBox="1" visibilityExpression=" &quot;Type&quot; = 'FIXED'">
      <attributeEditorField showLabel="1" index="4" name="FixedStage"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="Curve_TS"/>
    <field editable="1" name="Elevation"/>
    <field editable="1" name="FixedStage"/>
    <field editable="1" name="FlapGate"/>
    <field editable="1" name="Name"/>
    <field editable="1" name="RouteTo"/>
    <field editable="1" name="Type"/>
    <field editable="1" name="fid"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="Curve_TS"/>
    <field labelOnTop="0" name="Elevation"/>
    <field labelOnTop="0" name="FixedStage"/>
    <field labelOnTop="0" name="FlapGate"/>
    <field labelOnTop="0" name="Name"/>
    <field labelOnTop="0" name="RouteTo"/>
    <field labelOnTop="0" name="Type"/>
    <field labelOnTop="0" name="fid"/>
  </labelOnTop>
  <reuseLastValue>
    <field reuseLastValue="0" name="Curve_TS"/>
    <field reuseLastValue="0" name="Elevation"/>
    <field reuseLastValue="0" name="FixedStage"/>
    <field reuseLastValue="0" name="FlapGate"/>
    <field reuseLastValue="0" name="Name"/>
    <field reuseLastValue="0" name="RouteTo"/>
    <field reuseLastValue="0" name="Type"/>
    <field reuseLastValue="0" name="fid"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <layerGeometryType>0</layerGeometryType>
</qgis>

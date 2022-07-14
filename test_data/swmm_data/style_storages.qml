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
            <Option value="255,255,255,255" type="QString" name="color"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="square" type="QString" name="name"/>
            <Option value="0.00000000000000006,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="solid" type="QString" name="outline_style"/>
            <Option value="0.4" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="4.30667" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <prop k="angle" v="0"/>
          <prop k="cap_style" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0.00000000000000006,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="4.30667"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="size">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="if( @map_scale> 6000 ,4*6000/@map_scale,4)" type="QString" name="expression"/>
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
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Elevation">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="MaxDepth">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="InitDepth">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="CONICAL" type="QString" name="CONICAL"/>
              </Option>
              <Option type="Map">
                <Option value="CYLINDRICAL" type="QString" name="CYLINDRICAL"/>
              </Option>
              <Option type="Map">
                <Option value="FUNCTIONAL" type="QString" name="FUNCTIONAL"/>
              </Option>
              <Option type="Map">
                <Option value="PARABOLIC" type="QString" name="PARABOLIC"/>
              </Option>
              <Option type="Map">
                <Option value="PYRAMIDAL" type="QString" name="PYRAMIDAL"/>
              </Option>
              <Option type="Map">
                <Option value="TABULAR" type="QString" name="TABULAR"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Curve">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Coeff">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Exponent">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Constant">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="MajorAxis">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="MinorAxis">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="SideSlope">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="SurfHeight">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="SurDepth">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Fevap">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Psi">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Ksat">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="IMD">
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
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" name="General" columnCount="1" groupBox="0" visibilityExpression="">
      <attributeEditorField showLabel="1" index="1" name="Name"/>
      <attributeEditorField showLabel="1" index="2" name="Elevation"/>
      <attributeEditorField showLabel="1" index="3" name="MaxDepth"/>
      <attributeEditorField showLabel="1" index="4" name="InitDepth"/>
      <attributeEditorField showLabel="1" index="14" name="SurDepth"/>
      <attributeEditorField showLabel="1" index="15" name="Fevap"/>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" name="Storage seepage" columnCount="1" groupBox="0" visibilityExpression="">
      <attributeEditorField showLabel="1" index="16" name="Psi"/>
      <attributeEditorField showLabel="1" index="17" name="Ksat"/>
      <attributeEditorField showLabel="1" index="18" name="IMD"/>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" name="Storage shape" columnCount="1" groupBox="0" visibilityExpression="">
      <attributeEditorField showLabel="1" index="5" name="Type"/>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="1" name="Conical" columnCount="1" groupBox="1" visibilityExpression="&quot;Type&quot; =  'CONICAL' ">
        <attributeEditorField showLabel="1" index="10" name="MajorAxis"/>
        <attributeEditorField showLabel="1" index="11" name="MinorAxis"/>
        <attributeEditorField showLabel="1" index="12" name="SideSlope"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="1" name="Cylindrical" columnCount="1" groupBox="1" visibilityExpression="&quot;Type&quot; =  'CYLINDRICAL' ">
        <attributeEditorField showLabel="1" index="10" name="MajorAxis"/>
        <attributeEditorField showLabel="1" index="11" name="MinorAxis"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="1" name="Functional" columnCount="1" groupBox="1" visibilityExpression="&quot;Type&quot; = 'FUNCTIONAL'">
        <attributeEditorField showLabel="1" index="9" name="Constant"/>
        <attributeEditorField showLabel="1" index="7" name="Coeff"/>
        <attributeEditorField showLabel="1" index="8" name="Exponent"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="1" name="Tabular" columnCount="1" groupBox="1" visibilityExpression="&quot;Type&quot; =  'TABULAR' ">
        <attributeEditorField showLabel="1" index="6" name="Curve"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="1" name="Pyramidal" columnCount="1" groupBox="1" visibilityExpression="&quot;Type&quot; =  'PYRAMIDAL' ">
        <attributeEditorField showLabel="1" index="10" name="MajorAxis"/>
        <attributeEditorField showLabel="1" index="11" name="MinorAxis"/>
        <attributeEditorField showLabel="1" index="12" name="SideSlope"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="1" name="Parabolic" columnCount="1" groupBox="1" visibilityExpression="&quot;Type&quot; =  'PARABOLIC' ">
        <attributeEditorField showLabel="1" index="10" name="MajorAxis"/>
        <attributeEditorField showLabel="1" index="11" name="MinorAxis"/>
        <attributeEditorField showLabel="1" index="13" name="SurfHeight"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="Coeff"/>
    <field editable="1" name="Constant"/>
    <field editable="1" name="Curve"/>
    <field editable="1" name="Elevation"/>
    <field editable="1" name="Exponent"/>
    <field editable="1" name="Fevap"/>
    <field editable="1" name="IMD"/>
    <field editable="1" name="InitDepth"/>
    <field editable="1" name="Ksat"/>
    <field editable="1" name="MajorAxis"/>
    <field editable="1" name="MaxDepth"/>
    <field editable="1" name="MinorAxis"/>
    <field editable="1" name="Name"/>
    <field editable="1" name="Psi"/>
    <field editable="1" name="SideSlope"/>
    <field editable="1" name="SurDepth"/>
    <field editable="1" name="SurfHeight"/>
    <field editable="1" name="Type"/>
    <field editable="1" name="fid"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="Coeff"/>
    <field labelOnTop="0" name="Constant"/>
    <field labelOnTop="0" name="Curve"/>
    <field labelOnTop="0" name="Elevation"/>
    <field labelOnTop="0" name="Exponent"/>
    <field labelOnTop="0" name="Fevap"/>
    <field labelOnTop="0" name="IMD"/>
    <field labelOnTop="0" name="InitDepth"/>
    <field labelOnTop="0" name="Ksat"/>
    <field labelOnTop="0" name="MajorAxis"/>
    <field labelOnTop="0" name="MaxDepth"/>
    <field labelOnTop="0" name="MinorAxis"/>
    <field labelOnTop="0" name="Name"/>
    <field labelOnTop="0" name="Psi"/>
    <field labelOnTop="0" name="SideSlope"/>
    <field labelOnTop="0" name="SurDepth"/>
    <field labelOnTop="0" name="SurfHeight"/>
    <field labelOnTop="0" name="Type"/>
    <field labelOnTop="0" name="fid"/>
  </labelOnTop>
  <reuseLastValue>
    <field reuseLastValue="0" name="Coeff"/>
    <field reuseLastValue="0" name="Constant"/>
    <field reuseLastValue="0" name="Curve"/>
    <field reuseLastValue="0" name="Elevation"/>
    <field reuseLastValue="0" name="Exponent"/>
    <field reuseLastValue="0" name="Fevap"/>
    <field reuseLastValue="0" name="IMD"/>
    <field reuseLastValue="0" name="InitDepth"/>
    <field reuseLastValue="0" name="Ksat"/>
    <field reuseLastValue="0" name="MajorAxis"/>
    <field reuseLastValue="0" name="MaxDepth"/>
    <field reuseLastValue="0" name="MinorAxis"/>
    <field reuseLastValue="0" name="Name"/>
    <field reuseLastValue="0" name="Psi"/>
    <field reuseLastValue="0" name="SideSlope"/>
    <field reuseLastValue="0" name="SurDepth"/>
    <field reuseLastValue="0" name="SurfHeight"/>
    <field reuseLastValue="0" name="Type"/>
    <field reuseLastValue="0" name="fid"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <layerGeometryType>0</layerGeometryType>
</qgis>

<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.22.7-Białowieża" styleCategories="Symbology|Labeling|Fields|Forms" labelsEnabled="0">
  <renderer-v2 forceraster="0" type="singleSymbol" enableorderby="0" referencescale="-1" symbollevels="0">
    <symbols>
      <symbol alpha="1" clip_to_extent="1" force_rhr="0" type="marker" name="0">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <Option type="Map">
            <Option type="QString" value="0" name="angle"/>
            <Option type="QString" value="square" name="cap_style"/>
            <Option type="QString" value="0,0,0,255" name="color"/>
            <Option type="QString" value="1" name="horizontal_anchor_point"/>
            <Option type="QString" value="bevel" name="joinstyle"/>
            <Option type="QString" value="diamond" name="name"/>
            <Option type="QString" value="0,0" name="offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="offset_unit"/>
            <Option type="QString" value="35,35,35,255" name="outline_color"/>
            <Option type="QString" value="solid" name="outline_style"/>
            <Option type="QString" value="0" name="outline_width"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale"/>
            <Option type="QString" value="MM" name="outline_width_unit"/>
            <Option type="QString" value="diameter" name="scale_method"/>
            <Option type="QString" value="3.4" name="size"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="size_map_unit_scale"/>
            <Option type="QString" value="MM" name="size_unit"/>
            <Option type="QString" value="1" name="vertical_anchor_point"/>
          </Option>
          <prop k="angle" v="0"/>
          <prop k="cap_style" v="square"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="diamond"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3.4"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="size">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="if( @map_scale> 6000 ,3.4*6000/@map_scale,3.4)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
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
    <field configurationFlags="None" name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Elevation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="DivertLink">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option type="QString" value="CUTOFF" name="CUTOFF"/>
              <Option type="QString" value="OVERFLOW" name="OVERFLOW"/>
              <Option type="QString" value="TABULAR" name="TABULAR"/>
              <Option type="QString" value="WEIR" name="WEIR"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="CutoffFlow">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" value="false" name="IsMultiline"/>
            <Option type="bool" value="false" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Curve">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" value="false" name="IsMultiline"/>
            <Option type="bool" value="false" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WeirMinFlo">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" value="false" name="IsMultiline"/>
            <Option type="bool" value="false" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WeirMaxDep">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WeirCoeff">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" value="false" name="IsMultiline"/>
            <Option type="bool" value="false" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="MaxDepth">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="InitDepth">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="SurDepth">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Aponded">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" index="0" name=""/>
    <alias field="Name" index="1" name=""/>
    <alias field="Elevation" index="2" name=""/>
    <alias field="DivertLink" index="3" name=""/>
    <alias field="Type" index="4" name=""/>
    <alias field="CutoffFlow" index="5" name=""/>
    <alias field="Curve" index="6" name=""/>
    <alias field="WeirMinFlo" index="7" name=""/>
    <alias field="WeirMaxDep" index="8" name=""/>
    <alias field="WeirCoeff" index="9" name=""/>
    <alias field="MaxDepth" index="10" name=""/>
    <alias field="InitDepth" index="11" name=""/>
    <alias field="SurDepth" index="12" name=""/>
    <alias field="Aponded" index="13" name=""/>
  </aliases>
  <defaults>
    <default expression="" field="fid" applyOnUpdate="0"/>
    <default expression="" field="Name" applyOnUpdate="0"/>
    <default expression="" field="Elevation" applyOnUpdate="0"/>
    <default expression="" field="DivertLink" applyOnUpdate="0"/>
    <default expression="" field="Type" applyOnUpdate="0"/>
    <default expression="" field="CutoffFlow" applyOnUpdate="0"/>
    <default expression="" field="Curve" applyOnUpdate="0"/>
    <default expression="" field="WeirMinFlo" applyOnUpdate="0"/>
    <default expression="" field="WeirMaxDep" applyOnUpdate="0"/>
    <default expression="" field="WeirCoeff" applyOnUpdate="0"/>
    <default expression="" field="MaxDepth" applyOnUpdate="0"/>
    <default expression="" field="InitDepth" applyOnUpdate="0"/>
    <default expression="" field="SurDepth" applyOnUpdate="0"/>
    <default expression="" field="Aponded" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="1" field="fid" unique_strength="1" exp_strength="0" constraints="3"/>
    <constraint notnull_strength="0" field="Name" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Elevation" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="DivertLink" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Type" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="CutoffFlow" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Curve" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="WeirMinFlo" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="WeirMaxDep" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="WeirCoeff" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="MaxDepth" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="InitDepth" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="SurDepth" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Aponded" unique_strength="0" exp_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="fid" desc="" exp=""/>
    <constraint field="Name" desc="" exp=""/>
    <constraint field="Elevation" desc="" exp=""/>
    <constraint field="DivertLink" desc="" exp=""/>
    <constraint field="Type" desc="" exp=""/>
    <constraint field="CutoffFlow" desc="" exp=""/>
    <constraint field="Curve" desc="" exp=""/>
    <constraint field="WeirMinFlo" desc="" exp=""/>
    <constraint field="WeirMaxDep" desc="" exp=""/>
    <constraint field="WeirCoeff" desc="" exp=""/>
    <constraint field="MaxDepth" desc="" exp=""/>
    <constraint field="InitDepth" desc="" exp=""/>
    <constraint field="SurDepth" desc="" exp=""/>
    <constraint field="Aponded" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
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
    <attributeEditorField index="0" showLabel="1" name="fid"/>
    <attributeEditorField index="1" showLabel="1" name="Name"/>
    <attributeEditorField index="2" showLabel="1" name="Elevation"/>
    <attributeEditorField index="3" showLabel="1" name="DivertLink"/>
    <attributeEditorField index="4" showLabel="1" name="Type"/>
    <attributeEditorField index="10" showLabel="1" name="MaxDepth"/>
    <attributeEditorField index="11" showLabel="1" name="InitDepth"/>
    <attributeEditorField index="12" showLabel="1" name="SurDepth"/>
    <attributeEditorField index="13" showLabel="1" name="Aponded"/>
    <attributeEditorContainer visibilityExpressionEnabled="1" visibilityExpression="&quot;Type&quot; = 'CUTOFF'" columnCount="1" groupBox="1" showLabel="0" name="Cutoff">
      <attributeEditorField index="5" showLabel="1" name="CutoffFlow"/>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpressionEnabled="1" visibilityExpression="&quot;Type&quot; = 'TABULAR'" columnCount="1" groupBox="1" showLabel="0" name="Tabular">
      <attributeEditorField index="6" showLabel="1" name="Curve"/>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpressionEnabled="1" visibilityExpression="&quot;Type&quot; = 'WEIR'" columnCount="1" groupBox="1" showLabel="0" name="Weir">
      <attributeEditorField index="7" showLabel="1" name="WeirMinFlo"/>
      <attributeEditorField index="8" showLabel="1" name="WeirMaxDep"/>
      <attributeEditorField index="9" showLabel="1" name="WeirCoeff"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="Aponded"/>
    <field editable="1" name="Curve"/>
    <field editable="1" name="CutOffFlow"/>
    <field editable="1" name="CutoffFlow"/>
    <field editable="1" name="DivertLink"/>
    <field editable="1" name="Elevation"/>
    <field editable="1" name="InitDepth"/>
    <field editable="1" name="MaxDepth"/>
    <field editable="1" name="Name"/>
    <field editable="1" name="SurDepth"/>
    <field editable="1" name="Type"/>
    <field editable="1" name="WeirCoeff"/>
    <field editable="1" name="WeirMaxDep"/>
    <field editable="1" name="WeirMinFlo"/>
    <field editable="1" name="fid"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="Aponded"/>
    <field labelOnTop="0" name="Curve"/>
    <field labelOnTop="0" name="CutOffFlow"/>
    <field labelOnTop="0" name="CutoffFlow"/>
    <field labelOnTop="0" name="DivertLink"/>
    <field labelOnTop="0" name="Elevation"/>
    <field labelOnTop="0" name="InitDepth"/>
    <field labelOnTop="0" name="MaxDepth"/>
    <field labelOnTop="0" name="Name"/>
    <field labelOnTop="0" name="SurDepth"/>
    <field labelOnTop="0" name="Type"/>
    <field labelOnTop="0" name="WeirCoeff"/>
    <field labelOnTop="0" name="WeirMaxDep"/>
    <field labelOnTop="0" name="WeirMinFlo"/>
    <field labelOnTop="0" name="fid"/>
  </labelOnTop>
  <reuseLastValue>
    <field reuseLastValue="0" name="Aponded"/>
    <field reuseLastValue="0" name="Curve"/>
    <field reuseLastValue="0" name="CutOffFlow"/>
    <field reuseLastValue="0" name="CutoffFlow"/>
    <field reuseLastValue="0" name="DivertLink"/>
    <field reuseLastValue="0" name="Elevation"/>
    <field reuseLastValue="0" name="InitDepth"/>
    <field reuseLastValue="0" name="MaxDepth"/>
    <field reuseLastValue="0" name="Name"/>
    <field reuseLastValue="0" name="SurDepth"/>
    <field reuseLastValue="0" name="Type"/>
    <field reuseLastValue="0" name="WeirCoeff"/>
    <field reuseLastValue="0" name="WeirMaxDep"/>
    <field reuseLastValue="0" name="WeirMinFlo"/>
    <field reuseLastValue="0" name="fid"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <layerGeometryType>0</layerGeometryType>
</qgis>

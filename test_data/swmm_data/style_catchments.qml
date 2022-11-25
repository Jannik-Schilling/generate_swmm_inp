<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="0" labelsEnabled="0" simplifyDrawingHints="1" styleCategories="Symbology|Labeling|Fields|Forms|AttributeTable|Rendering" simplifyMaxScale="1" version="3.28.0-Firenze" simplifyDrawingTol="1" simplifyLocal="1" simplifyAlgorithm="0" symbologyReferenceScale="-1" hasScaleBasedVisibilityFlag="0" maxScale="0">
  <renderer-v2 type="singleSymbol" symbollevels="0" referencescale="-1" forceraster="0" enableorderby="0">
    <symbols>
      <symbol frame_rate="10" alpha="1" clip_to_extent="1" is_animated="0" type="fill" force_rhr="0" name="0">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="3x:0,0,0,0,0,0" type="QString" name="border_width_map_unit_scale"/>
            <Option value="0,0,0,255" type="QString" name="color"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="solid" type="QString" name="outline_style"/>
            <Option value="0.26" type="QString" name="outline_width"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option value="f_diagonal" type="QString" name="style"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="GeometryGenerator" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="Line" type="QString" name="SymbolType"/>
            <Option value="if ( @map_scale > 10000, NULL, make_line(centroid($geometry),geometry(get_feature( replace(@layer_name,'subcatchments','junctions' ), 'Name',&quot;Outlet&quot;))))" type="QString" name="geometryModifier"/>
            <Option value="MapUnit" type="QString" name="units"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol frame_rate="10" alpha="1" clip_to_extent="1" is_animated="0" type="line" force_rhr="0" name="@0@1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer class="SimpleLine" enabled="1" locked="0" pass="0">
              <Option type="Map">
                <Option value="0" type="QString" name="align_dash_pattern"/>
                <Option value="square" type="QString" name="capstyle"/>
                <Option value="5;2" type="QString" name="customdash"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="customdash_map_unit_scale"/>
                <Option value="MM" type="QString" name="customdash_unit"/>
                <Option value="0" type="QString" name="dash_pattern_offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="dash_pattern_offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="dash_pattern_offset_unit"/>
                <Option value="0" type="QString" name="draw_inside_polygon"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="35,35,35,255" type="QString" name="line_color"/>
                <Option value="dot" type="QString" name="line_style"/>
                <Option value="0.26" type="QString" name="line_width"/>
                <Option value="MM" type="QString" name="line_width_unit"/>
                <Option value="0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="0" type="QString" name="ring_filter"/>
                <Option value="0" type="QString" name="trim_distance_end"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="trim_distance_end_map_unit_scale"/>
                <Option value="MM" type="QString" name="trim_distance_end_unit"/>
                <Option value="0" type="QString" name="trim_distance_start"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="trim_distance_start_map_unit_scale"/>
                <Option value="MM" type="QString" name="trim_distance_start_unit"/>
                <Option value="0" type="QString" name="tweak_dash_pattern_on_corners"/>
                <Option value="0" type="QString" name="use_custom_dash"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="width_map_unit_scale"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <fieldConfiguration>
    <field configurationFlags="None" name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="RainGage">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Outlet">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Area">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Imperv">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Width">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Slope">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="CurbLen">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="SnowPack">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="N_Imperv">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="N_Perv">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="S_Imperv">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="S_Perv">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="PctZero">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="RouteTo">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="IMPERVIOUS" type="QString" name="IMPERVIOUS"/>
              </Option>
              <Option type="Map">
                <Option value="OUTLET" type="QString" name="OUTLET"/>
              </Option>
              <Option type="Map">
                <Option value="PERVIOUS" type="QString" name="PERVIOUS"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="PctRouted">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="InfMethod">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="CURVE_NUMBER" type="QString" name="CURVE_NUMBER"/>
              </Option>
              <Option type="Map">
                <Option value="GREEN_AMPT" type="QString" name="GREEN_AMPT"/>
              </Option>
              <Option type="Map">
                <Option value="HORTON" type="QString" name="HORTON"/>
              </Option>
              <Option type="Map">
                <Option value="MODIFIED_GREEN_AMPT" type="QString" name="MODIFIED_GREEN_AMPT"/>
              </Option>
              <Option type="Map">
                <Option value="MODIFIED_HORTON" type="QString" name="MODIFIED_HORTON"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="SuctHead">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Conductiv">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="InitDef">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="MaxRate">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="MinRate">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Decay">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="DryTime">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="MaxInf">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="CurveNum">
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
  <aliases>
    <alias field="fid" index="0" name=""/>
    <alias field="Name" index="1" name=""/>
    <alias field="RainGage" index="2" name=""/>
    <alias field="Outlet" index="3" name=""/>
    <alias field="Area" index="4" name=""/>
    <alias field="Imperv" index="5" name=""/>
    <alias field="Width" index="6" name=""/>
    <alias field="Slope" index="7" name=""/>
    <alias field="CurbLen" index="8" name=""/>
    <alias field="SnowPack" index="9" name=""/>
    <alias field="N_Imperv" index="10" name=""/>
    <alias field="N_Perv" index="11" name=""/>
    <alias field="S_Imperv" index="12" name=""/>
    <alias field="S_Perv" index="13" name=""/>
    <alias field="PctZero" index="14" name=""/>
    <alias field="RouteTo" index="15" name=""/>
    <alias field="PctRouted" index="16" name=""/>
    <alias field="InfMethod" index="17" name=""/>
    <alias field="SuctHead" index="18" name=""/>
    <alias field="Conductiv" index="19" name=""/>
    <alias field="InitDef" index="20" name=""/>
    <alias field="MaxRate" index="21" name=""/>
    <alias field="MinRate" index="22" name=""/>
    <alias field="Decay" index="23" name=""/>
    <alias field="DryTime" index="24" name=""/>
    <alias field="MaxInf" index="25" name=""/>
    <alias field="CurveNum" index="26" name=""/>
  </aliases>
  <defaults>
    <default expression="" field="fid" applyOnUpdate="0"/>
    <default expression="" field="Name" applyOnUpdate="0"/>
    <default expression="" field="RainGage" applyOnUpdate="0"/>
    <default expression="" field="Outlet" applyOnUpdate="0"/>
    <default expression="" field="Area" applyOnUpdate="0"/>
    <default expression="" field="Imperv" applyOnUpdate="0"/>
    <default expression="" field="Width" applyOnUpdate="0"/>
    <default expression="" field="Slope" applyOnUpdate="0"/>
    <default expression="" field="CurbLen" applyOnUpdate="0"/>
    <default expression="" field="SnowPack" applyOnUpdate="0"/>
    <default expression="" field="N_Imperv" applyOnUpdate="0"/>
    <default expression="" field="N_Perv" applyOnUpdate="0"/>
    <default expression="" field="S_Imperv" applyOnUpdate="0"/>
    <default expression="" field="S_Perv" applyOnUpdate="0"/>
    <default expression="" field="PctZero" applyOnUpdate="0"/>
    <default expression="" field="RouteTo" applyOnUpdate="0"/>
    <default expression="" field="PctRouted" applyOnUpdate="0"/>
    <default expression="" field="InfMethod" applyOnUpdate="0"/>
    <default expression="" field="SuctHead" applyOnUpdate="0"/>
    <default expression="" field="Conductiv" applyOnUpdate="0"/>
    <default expression="" field="InitDef" applyOnUpdate="0"/>
    <default expression="" field="MaxRate" applyOnUpdate="0"/>
    <default expression="" field="MinRate" applyOnUpdate="0"/>
    <default expression="" field="Decay" applyOnUpdate="0"/>
    <default expression="" field="DryTime" applyOnUpdate="0"/>
    <default expression="" field="MaxInf" applyOnUpdate="0"/>
    <default expression="" field="CurveNum" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" field="fid" notnull_strength="1" constraints="3" exp_strength="0"/>
    <constraint unique_strength="1" field="Name" notnull_strength="0" constraints="2" exp_strength="0"/>
    <constraint unique_strength="0" field="RainGage" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Outlet" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Area" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Imperv" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Width" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Slope" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="CurbLen" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="SnowPack" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="N_Imperv" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="N_Perv" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="S_Imperv" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="S_Perv" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="PctZero" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="RouteTo" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="PctRouted" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="InfMethod" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="SuctHead" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Conductiv" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="InitDef" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="MaxRate" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="MinRate" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Decay" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="DryTime" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="MaxInf" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="CurveNum" notnull_strength="0" constraints="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="fid"/>
    <constraint desc="" exp="" field="Name"/>
    <constraint desc="" exp="" field="RainGage"/>
    <constraint desc="" exp="" field="Outlet"/>
    <constraint desc="" exp="" field="Area"/>
    <constraint desc="" exp="" field="Imperv"/>
    <constraint desc="" exp="" field="Width"/>
    <constraint desc="" exp="" field="Slope"/>
    <constraint desc="" exp="" field="CurbLen"/>
    <constraint desc="" exp="" field="SnowPack"/>
    <constraint desc="" exp="" field="N_Imperv"/>
    <constraint desc="" exp="" field="N_Perv"/>
    <constraint desc="" exp="" field="S_Imperv"/>
    <constraint desc="" exp="" field="S_Perv"/>
    <constraint desc="" exp="" field="PctZero"/>
    <constraint desc="" exp="" field="RouteTo"/>
    <constraint desc="" exp="" field="PctRouted"/>
    <constraint desc="" exp="" field="InfMethod"/>
    <constraint desc="" exp="" field="SuctHead"/>
    <constraint desc="" exp="" field="Conductiv"/>
    <constraint desc="" exp="" field="InitDef"/>
    <constraint desc="" exp="" field="MaxRate"/>
    <constraint desc="" exp="" field="MinRate"/>
    <constraint desc="" exp="" field="Decay"/>
    <constraint desc="" exp="" field="DryTime"/>
    <constraint desc="" exp="" field="MaxInf"/>
    <constraint desc="" exp="" field="CurveNum"/>
  </constraintExpressions>
  <expressionfields/>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column hidden="0" width="-1" type="field" name="fid"/>
      <column hidden="0" width="-1" type="field" name="Name"/>
      <column hidden="0" width="-1" type="field" name="RainGage"/>
      <column hidden="0" width="-1" type="field" name="Outlet"/>
      <column hidden="0" width="-1" type="field" name="Area"/>
      <column hidden="0" width="-1" type="field" name="Imperv"/>
      <column hidden="0" width="-1" type="field" name="Width"/>
      <column hidden="0" width="-1" type="field" name="Slope"/>
      <column hidden="0" width="-1" type="field" name="CurbLen"/>
      <column hidden="0" width="-1" type="field" name="SnowPack"/>
      <column hidden="0" width="-1" type="field" name="N_Imperv"/>
      <column hidden="0" width="-1" type="field" name="N_Perv"/>
      <column hidden="0" width="-1" type="field" name="S_Imperv"/>
      <column hidden="0" width="-1" type="field" name="S_Perv"/>
      <column hidden="0" width="-1" type="field" name="PctZero"/>
      <column hidden="0" width="-1" type="field" name="RouteTo"/>
      <column hidden="0" width="-1" type="field" name="PctRouted"/>
      <column hidden="0" width="-1" type="field" name="InfMethod"/>
      <column hidden="0" width="-1" type="field" name="SuctHead"/>
      <column hidden="0" width="-1" type="field" name="Conductiv"/>
      <column hidden="0" width="-1" type="field" name="InitDef"/>
      <column hidden="0" width="-1" type="field" name="MaxRate"/>
      <column hidden="0" width="-1" type="field" name="MinRate"/>
      <column hidden="0" width="-1" type="field" name="Decay"/>
      <column hidden="0" width="-1" type="field" name="DryTime"/>
      <column hidden="0" width="-1" type="field" name="MaxInf"/>
      <column hidden="0" width="-1" type="field" name="CurveNum"/>
      <column hidden="1" width="-1" type="actions"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
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
    <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
      <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
    </labelStyle>
    <attributeEditorContainer collapsedExpressionEnabled="0" columnCount="1" groupBox="0" visibilityExpressionEnabled="0" showLabel="1" collapsed="0" collapsedExpression="" name="General" visibilityExpression="">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
      <attributeEditorField index="1" showLabel="1" name="Name">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="2" showLabel="1" name="RainGage">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="3" showLabel="1" name="Outlet">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="4" showLabel="1" name="Area">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="5" showLabel="1" name="Imperv">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="6" showLabel="1" name="Width">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="7" showLabel="1" name="Slope">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="8" showLabel="1" name="CurbLen">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="9" showLabel="1" name="SnowPack">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="10" showLabel="1" name="N_Imperv">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="11" showLabel="1" name="N_Perv">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="12" showLabel="1" name="S_Imperv">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="13" showLabel="1" name="S_Perv">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="14" showLabel="1" name="PctZero">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="16" showLabel="1" name="PctRouted">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField index="15" showLabel="1" name="RouteTo">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
    </attributeEditorContainer>
    <attributeEditorContainer collapsedExpressionEnabled="0" columnCount="1" groupBox="0" visibilityExpressionEnabled="0" showLabel="1" backgroundColor="#e9e4fd" collapsed="0" collapsedExpression="" name="Infiltration" visibilityExpression="">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
      <attributeEditorField index="17" showLabel="1" name="InfMethod">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorContainer collapsedExpressionEnabled="0" columnCount="1" groupBox="1" visibilityExpressionEnabled="1" showLabel="0" backgroundColor="#e9e4fd" collapsed="0" collapsedExpression="" name="Horton/Modified Horton" visibilityExpression="&quot;InfMethod&quot; in ('HORTON' , 'MODIFIED_HORTON' )">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
        <attributeEditorField index="21" showLabel="1" name="MaxRate">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField index="22" showLabel="1" name="MinRate">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField index="23" showLabel="1" name="Decay">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField index="24" showLabel="1" name="DryTime">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField index="25" showLabel="1" name="MaxInf">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
      </attributeEditorContainer>
      <attributeEditorContainer collapsedExpressionEnabled="0" columnCount="1" groupBox="1" visibilityExpressionEnabled="1" showLabel="0" backgroundColor="#e9e4fd" collapsed="0" collapsedExpression="" name="Green_Ampt, Modified Green_Ampt" visibilityExpression="&quot;InfMethod&quot; in ( 'GREEN_AMPT' ,  'MODIFIED_GREEN_AMPT' )">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
        <attributeEditorField index="18" showLabel="1" name="SuctHead">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField index="19" showLabel="1" name="Conductiv">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField index="20" showLabel="1" name="InitDef">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
      </attributeEditorContainer>
      <attributeEditorContainer collapsedExpressionEnabled="0" columnCount="1" groupBox="1" visibilityExpressionEnabled="1" showLabel="0" backgroundColor="#e9e4fd" collapsed="0" collapsedExpression="" name="Curve Number" visibilityExpression="&quot;InfMethod&quot; =  'CURVE_NUMBER' ">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
        <attributeEditorField index="26" showLabel="1" name="CurveNum">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField index="19" showLabel="1" name="Conductiv">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField index="24" showLabel="1" name="DryTime">
          <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
            <labelFont bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
          </labelStyle>
        </attributeEditorField>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field name="Area" editable="1"/>
    <field name="Conductiv" editable="1"/>
    <field name="CurbLen" editable="1"/>
    <field name="CurveNum" editable="1"/>
    <field name="Decay" editable="1"/>
    <field name="DryTime" editable="1"/>
    <field name="Imperv" editable="1"/>
    <field name="InfMethod" editable="1"/>
    <field name="InitDef" editable="1"/>
    <field name="MaxInf" editable="1"/>
    <field name="MaxRate" editable="1"/>
    <field name="MinRate" editable="1"/>
    <field name="N_Imperv" editable="1"/>
    <field name="N_Perv" editable="1"/>
    <field name="Name" editable="1"/>
    <field name="Outlet" editable="1"/>
    <field name="PctRouted" editable="1"/>
    <field name="PctZero" editable="1"/>
    <field name="RainGage" editable="1"/>
    <field name="RouteTo" editable="1"/>
    <field name="S_Imperv" editable="1"/>
    <field name="S_Perv" editable="1"/>
    <field name="Slope" editable="1"/>
    <field name="SnowPack" editable="1"/>
    <field name="SuctHead" editable="1"/>
    <field name="Width" editable="1"/>
    <field name="fid" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="Area"/>
    <field labelOnTop="0" name="Conductiv"/>
    <field labelOnTop="0" name="CurbLen"/>
    <field labelOnTop="0" name="CurveNum"/>
    <field labelOnTop="0" name="Decay"/>
    <field labelOnTop="0" name="DryTime"/>
    <field labelOnTop="0" name="Imperv"/>
    <field labelOnTop="0" name="InfMethod"/>
    <field labelOnTop="0" name="InitDef"/>
    <field labelOnTop="0" name="MaxInf"/>
    <field labelOnTop="0" name="MaxRate"/>
    <field labelOnTop="0" name="MinRate"/>
    <field labelOnTop="0" name="N_Imperv"/>
    <field labelOnTop="0" name="N_Perv"/>
    <field labelOnTop="0" name="Name"/>
    <field labelOnTop="0" name="Outlet"/>
    <field labelOnTop="0" name="PctRouted"/>
    <field labelOnTop="0" name="PctZero"/>
    <field labelOnTop="0" name="RainGage"/>
    <field labelOnTop="0" name="RouteTo"/>
    <field labelOnTop="0" name="S_Imperv"/>
    <field labelOnTop="0" name="S_Perv"/>
    <field labelOnTop="0" name="Slope"/>
    <field labelOnTop="0" name="SnowPack"/>
    <field labelOnTop="0" name="SuctHead"/>
    <field labelOnTop="0" name="Width"/>
    <field labelOnTop="0" name="fid"/>
  </labelOnTop>
  <reuseLastValue>
    <field reuseLastValue="0" name="Area"/>
    <field reuseLastValue="0" name="Conductiv"/>
    <field reuseLastValue="0" name="CurbLen"/>
    <field reuseLastValue="0" name="CurveNum"/>
    <field reuseLastValue="0" name="Decay"/>
    <field reuseLastValue="0" name="DryTime"/>
    <field reuseLastValue="0" name="Imperv"/>
    <field reuseLastValue="0" name="InfMethod"/>
    <field reuseLastValue="0" name="InitDef"/>
    <field reuseLastValue="0" name="MaxInf"/>
    <field reuseLastValue="0" name="MaxRate"/>
    <field reuseLastValue="0" name="MinRate"/>
    <field reuseLastValue="0" name="N_Imperv"/>
    <field reuseLastValue="0" name="N_Perv"/>
    <field reuseLastValue="0" name="Name"/>
    <field reuseLastValue="0" name="Outlet"/>
    <field reuseLastValue="0" name="PctRouted"/>
    <field reuseLastValue="0" name="PctZero"/>
    <field reuseLastValue="0" name="RainGage"/>
    <field reuseLastValue="0" name="RouteTo"/>
    <field reuseLastValue="0" name="S_Imperv"/>
    <field reuseLastValue="0" name="S_Perv"/>
    <field reuseLastValue="0" name="Slope"/>
    <field reuseLastValue="0" name="SnowPack"/>
    <field reuseLastValue="0" name="SuctHead"/>
    <field reuseLastValue="0" name="Width"/>
    <field reuseLastValue="0" name="fid"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <layerGeometryType>2</layerGeometryType>
</qgis>

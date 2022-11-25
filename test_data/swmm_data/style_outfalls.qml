<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="0" labelsEnabled="0" simplifyDrawingHints="0" styleCategories="Symbology|Labeling|Fields|Forms|Actions|MapTips|Diagrams|AttributeTable|Rendering" simplifyMaxScale="1" version="3.28.0-Firenze" simplifyDrawingTol="1" simplifyLocal="1" simplifyAlgorithm="0" symbologyReferenceScale="-1" hasScaleBasedVisibilityFlag="0" maxScale="0">
  <renderer-v2 type="singleSymbol" symbollevels="0" referencescale="-1" forceraster="0" enableorderby="0">
    <symbols>
      <symbol frame_rate="10" alpha="1" clip_to_extent="1" is_animated="0" type="marker" force_rhr="0" name="0">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="180" type="QString" name="angle"/>
            <Option value="square" type="QString" name="cap_style"/>
            <Option value="113,113,113,255" type="QString" name="color"/>
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
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="offset">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="'0'|| ',' || tostring(0.166667*(if( @map_scale> 6000 ,max(4*6000/@map_scale,2),4)))" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
                <Option type="Map" name="size">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="if( @map_scale> 6000 ,max(4*6000/@map_scale,2),4)" type="QString" name="expression"/>
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
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory backgroundAlpha="255" penColor="#000000" labelPlacementMethod="XHeight" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" height="15" penAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" spacingUnit="MM" maxScaleDenominator="0" diagramOrientation="Up" sizeType="MM" sizeScale="3x:0,0,0,0,0,0" direction="0" minimumSize="0" spacing="5" rotationOffset="270" opacity="1" showAxis="1" minScaleDenominator="0" width="15" penWidth="0" barWidth="5" scaleBasedVisibility="0" enabled="0" lineSizeType="MM">
      <fontProperties bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      <attribute color="#000000" field="" colorOpacity="1" label=""/>
      <axisSymbol>
        <symbol frame_rate="10" alpha="1" clip_to_extent="1" is_animated="0" type="line" force_rhr="0" name="">
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
              <Option value="solid" type="QString" name="line_style"/>
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
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" obstacle="0" showAll="1" dist="0" zIndex="0" linePlacementFlags="18" placement="0">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
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
    <field configurationFlags="None" name="Type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="Map" name="map">
              <Option value="FIXED" type="QString" name="FIXED"/>
              <Option value="FREE" type="QString" name="FREE"/>
              <Option value="NORMAL" type="QString" name="NORMAL"/>
              <Option value="TIDAL" type="QString" name="TIDAL"/>
              <Option value="TIMESERIES" type="QString" name="TIMESERIES"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="FixedStage">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Curve_TS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" type="bool" name="IsMultiline"/>
            <Option value="false" type="bool" name="UseHtml"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="FlapGate">
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
    <field configurationFlags="None" name="RouteTo">
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
    <alias field="Elevation" index="2" name=""/>
    <alias field="Type" index="3" name=""/>
    <alias field="FixedStage" index="4" name=""/>
    <alias field="Curve_TS" index="5" name=""/>
    <alias field="FlapGate" index="6" name=""/>
    <alias field="RouteTo" index="7" name=""/>
  </aliases>
  <defaults>
    <default expression="" field="fid" applyOnUpdate="0"/>
    <default expression="" field="Name" applyOnUpdate="0"/>
    <default expression="" field="Elevation" applyOnUpdate="0"/>
    <default expression="" field="Type" applyOnUpdate="0"/>
    <default expression="" field="FixedStage" applyOnUpdate="0"/>
    <default expression="" field="Curve_TS" applyOnUpdate="0"/>
    <default expression="" field="FlapGate" applyOnUpdate="0"/>
    <default expression="" field="RouteTo" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" field="fid" notnull_strength="1" constraints="3" exp_strength="0"/>
    <constraint unique_strength="0" field="Name" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Elevation" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Type" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="FixedStage" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Curve_TS" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="FlapGate" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="RouteTo" notnull_strength="0" constraints="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="fid"/>
    <constraint desc="" exp="" field="Name"/>
    <constraint desc="" exp="" field="Elevation"/>
    <constraint desc="" exp="" field="Type"/>
    <constraint desc="" exp="" field="FixedStage"/>
    <constraint desc="" exp="" field="Curve_TS"/>
    <constraint desc="" exp="" field="FlapGate"/>
    <constraint desc="" exp="" field="RouteTo"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column hidden="0" width="-1" type="field" name="fid"/>
      <column hidden="0" width="-1" type="field" name="Name"/>
      <column hidden="0" width="-1" type="field" name="Elevation"/>
      <column hidden="0" width="-1" type="field" name="Type"/>
      <column hidden="0" width="-1" type="field" name="FixedStage"/>
      <column hidden="0" width="-1" type="field" name="Curve_TS"/>
      <column hidden="0" width="-1" type="field" name="FlapGate"/>
      <column hidden="0" width="-1" type="field" name="RouteTo"/>
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
    <attributeEditorField index="0" showLabel="1" name="fid">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField index="1" showLabel="1" name="Name">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField index="2" showLabel="1" name="Elevation">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField index="6" showLabel="1" name="FlapGate">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField index="7" showLabel="1" name="RouteTo">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField index="3" showLabel="1" name="Type">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorContainer collapsedExpressionEnabled="0" columnCount="1" groupBox="1" visibilityExpressionEnabled="1" showLabel="0" collapsed="0" collapsedExpression="" name="Tidal or Timeseries" visibilityExpression=" &quot;Type&quot; in ('TIDAL','TIMESERIES')">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
      <attributeEditorField index="5" showLabel="1" name="Curve_TS">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
    </attributeEditorContainer>
    <attributeEditorContainer collapsedExpressionEnabled="0" columnCount="1" groupBox="1" visibilityExpressionEnabled="1" showLabel="0" collapsed="0" collapsedExpression="" name="Fixed" visibilityExpression=" &quot;Type&quot; = 'FIXED'">
      <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
        <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
      </labelStyle>
      <attributeEditorField index="4" showLabel="1" name="FixedStage">
        <labelStyle overrideLabelFont="0" overrideLabelColor="0" labelColor="0,0,0,255">
          <labelFont bold="0" italic="0" strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" underline="0"/>
        </labelStyle>
      </attributeEditorField>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field name="Curve_TS" editable="1"/>
    <field name="Elevation" editable="1"/>
    <field name="FixedStage" editable="1"/>
    <field name="FlapGate" editable="1"/>
    <field name="Name" editable="1"/>
    <field name="RouteTo" editable="1"/>
    <field name="Type" editable="1"/>
    <field name="fid" editable="1"/>
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
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>

<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology|Symbology3D|Labeling|Fields|Forms|Actions|MapTips|Diagrams|AttributeTable|Rendering|CustomProperties|GeometryOptions|Relations" simplifyLocal="1" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" maxScale="0" symbologyReferenceScale="-1" simplifyDrawingHints="0" labelsEnabled="0" version="3.28.1-Firenze" simplifyAlgorithm="0" minScale="0" simplifyDrawingTol="1">
  <renderer-v2 forceraster="0" type="singleSymbol" referencescale="-1" enableorderby="0" symbollevels="0">
    <symbols>
      <symbol clip_to_extent="1" frame_rate="10" alpha="1" name="0" type="marker" is_animated="0" force_rhr="0">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" locked="0" class="SimpleMarker" enabled="1">
          <Option type="Map">
            <Option value="180" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="113,113,113,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="triangle" name="name" type="QString"/>
            <Option value="0,0.59999999999999998" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255" name="outline_color" type="QString"/>
            <Option value="no" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="3.6" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="offset" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="'0'|| ',' || tostring(0.166667*(if( @map_scale> 6000 ,max(4*6000/@map_scale,2),4)))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="if( @map_scale> 6000 ,max(4*6000/@map_scale,2),4)" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <Option type="Map">
      <Option value="0" name="embeddedWidgets/count" type="int"/>
      <Option name="variableNames"/>
      <Option name="variableValues"/>
    </Option>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory penColor="#000000" spacing="5" scaleDependency="Area" enabled="0" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" penAlpha="255" showAxis="1" opacity="1" minScaleDenominator="0" backgroundAlpha="255" minimumSize="0" penWidth="0" maxScaleDenominator="0" sizeScale="3x:0,0,0,0,0,0" rotationOffset="270" width="15" barWidth="5" direction="0" lineSizeType="MM" scaleBasedVisibility="0" spacingUnit="MM" height="15" lineSizeScale="3x:0,0,0,0,0,0" sizeType="MM" labelPlacementMethod="XHeight" diagramOrientation="Up">
      <fontProperties strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      <attribute colorOpacity="1" color="#000000" field="" label=""/>
      <axisSymbol>
        <symbol clip_to_extent="1" frame_rate="10" alpha="1" name="" type="line" is_animated="0" force_rhr="0">
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <layer pass="0" locked="0" class="SimpleLine" enabled="1">
            <Option type="Map">
              <Option value="0" name="align_dash_pattern" type="QString"/>
              <Option value="square" name="capstyle" type="QString"/>
              <Option value="5;2" name="customdash" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
              <Option value="MM" name="customdash_unit" type="QString"/>
              <Option value="0" name="dash_pattern_offset" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
              <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
              <Option value="0" name="draw_inside_polygon" type="QString"/>
              <Option value="bevel" name="joinstyle" type="QString"/>
              <Option value="35,35,35,255" name="line_color" type="QString"/>
              <Option value="solid" name="line_style" type="QString"/>
              <Option value="0.26" name="line_width" type="QString"/>
              <Option value="MM" name="line_width_unit" type="QString"/>
              <Option value="0" name="offset" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
              <Option value="MM" name="offset_unit" type="QString"/>
              <Option value="0" name="ring_filter" type="QString"/>
              <Option value="0" name="trim_distance_end" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
              <Option value="MM" name="trim_distance_end_unit" type="QString"/>
              <Option value="0" name="trim_distance_start" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
              <Option value="MM" name="trim_distance_start_unit" type="QString"/>
              <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
              <Option value="0" name="use_custom_dash" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
            </Option>
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" placement="0" showAll="1" zIndex="0" dist="0" linePlacementFlags="18" obstacle="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <referencedLayers/>
  <fieldConfiguration>
    <field name="fid" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Name" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Elevation" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Type" configurationFlags="None">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="Map">
              <Option value="FIXED" name="FIXED" type="QString"/>
              <Option value="FREE" name="FREE" type="QString"/>
              <Option value="NORMAL" name="NORMAL" type="QString"/>
              <Option value="TIDAL" name="TIDAL" type="QString"/>
              <Option value="TIMESERIES" name="TIMESERIES" type="QString"/>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="FixedStage" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Curve_TS" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="FlapGate" configurationFlags="None">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="NO" name="NO" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="YES" name="YES" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="RouteTo" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Annotation" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="true" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" index="0" field="fid"/>
    <alias name="" index="1" field="Name"/>
    <alias name="" index="2" field="Elevation"/>
    <alias name="" index="3" field="Type"/>
    <alias name="" index="4" field="FixedStage"/>
    <alias name="" index="5" field="Curve_TS"/>
    <alias name="" index="6" field="FlapGate"/>
    <alias name="" index="7" field="RouteTo"/>
    <alias name="" index="8" field="Annotation"/>
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
    <default expression="" field="Annotation" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" notnull_strength="1" constraints="3" unique_strength="1" field="fid"/>
    <constraint exp_strength="0" notnull_strength="1" constraints="3" unique_strength="1" field="Name"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Elevation"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Type"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="FixedStage"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Curve_TS"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="FlapGate"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="RouteTo"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Annotation"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="fid"/>
    <constraint exp="" desc="" field="Name"/>
    <constraint exp="" desc="" field="Elevation"/>
    <constraint exp="" desc="" field="Type"/>
    <constraint exp="" desc="" field="FixedStage"/>
    <constraint exp="" desc="" field="Curve_TS"/>
    <constraint exp="" desc="" field="FlapGate"/>
    <constraint exp="" desc="" field="RouteTo"/>
    <constraint exp="" desc="" field="Annotation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column name="fid" width="-1" type="field" hidden="0"/>
      <column name="Name" width="-1" type="field" hidden="0"/>
      <column name="Elevation" width="-1" type="field" hidden="0"/>
      <column name="Type" width="-1" type="field" hidden="0"/>
      <column name="FixedStage" width="-1" type="field" hidden="0"/>
      <column name="Curve_TS" width="-1" type="field" hidden="0"/>
      <column name="FlapGate" width="-1" type="field" hidden="0"/>
      <column name="RouteTo" width="-1" type="field" hidden="0"/>
      <column name="Annotation" width="-1" type="field" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
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
    <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
      <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
    </labelStyle>
    <attributeEditorField showLabel="1" name="Name" index="1">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField showLabel="1" name="Elevation" index="2">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField showLabel="1" name="FlapGate" index="6">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField showLabel="1" name="RouteTo" index="7">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField showLabel="1" name="Type" index="3">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorContainer showLabel="0" collapsed="0" groupBox="1" name="Tidal or Timeseries" visibilityExpressionEnabled="1" collapsedExpressionEnabled="0" visibilityExpression=" &quot;Type&quot; in ('TIDAL','TIMESERIES')" columnCount="1" collapsedExpression="">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
      <attributeEditorField showLabel="1" name="Curve_TS" index="5">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="0" collapsed="0" groupBox="1" name="Fixed" visibilityExpressionEnabled="1" collapsedExpressionEnabled="0" visibilityExpression=" &quot;Type&quot; = 'FIXED'" columnCount="1" collapsedExpression="">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
      <attributeEditorField showLabel="1" name="FixedStage" index="4">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
    </attributeEditorContainer>
    <attributeEditorField showLabel="1" name="Annotation" index="8">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
  </attributeEditorForm>
  <editable>
    <field name="Annotation" editable="1"/>
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
    <field labelOnTop="0" name="Annotation"/>
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
    <field name="Annotation" reuseLastValue="0"/>
    <field name="Curve_TS" reuseLastValue="0"/>
    <field name="Elevation" reuseLastValue="0"/>
    <field name="FixedStage" reuseLastValue="0"/>
    <field name="FlapGate" reuseLastValue="0"/>
    <field name="Name" reuseLastValue="0"/>
    <field name="RouteTo" reuseLastValue="0"/>
    <field name="Type" reuseLastValue="0"/>
    <field name="fid" reuseLastValue="0"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>

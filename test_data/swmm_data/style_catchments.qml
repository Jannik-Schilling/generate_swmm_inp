<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology|Symbology3D|Labeling|Fields|Forms|Actions|MapTips|Diagrams|AttributeTable|Rendering|CustomProperties|GeometryOptions|Relations" simplifyLocal="1" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" maxScale="0" symbologyReferenceScale="-1" simplifyDrawingHints="1" labelsEnabled="0" version="3.28.1-Firenze" simplifyAlgorithm="0" minScale="0" simplifyDrawingTol="1">
  <renderer-v2 forceraster="0" type="singleSymbol" referencescale="-1" enableorderby="0" symbollevels="0">
    <symbols>
      <symbol clip_to_extent="1" frame_rate="10" alpha="1" name="0" type="fill" is_animated="0" force_rhr="0">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" locked="0" class="SimpleFill" enabled="1">
          <Option type="Map">
            <Option value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale" type="QString"/>
            <Option value="0,0,0,255" name="color" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0.26" name="outline_width" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="f_diagonal" name="style" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="0" locked="0" class="GeometryGenerator" enabled="1">
          <Option type="Map">
            <Option value="Line" name="SymbolType" type="QString"/>
            <Option value="if ( @map_scale > 10000, NULL, make_line(centroid($geometry),geometry(get_feature( replace(@layer_name,'subcatchments','junctions' ), 'Name',&quot;Outlet&quot;))))" name="geometryModifier" type="QString"/>
            <Option value="MapUnit" name="units" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" frame_rate="10" alpha="1" name="@0@1" type="line" is_animated="0" force_rhr="0">
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
                <Option value="dot" name="line_style" type="QString"/>
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
  <DiagramLayerSettings priority="0" placement="1" showAll="1" zIndex="0" dist="0" linePlacementFlags="18" obstacle="0">
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
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option value="0" name="allowedGapsBuffer" type="double"/>
        <Option value="false" name="allowedGapsEnabled" type="bool"/>
        <Option value="" name="allowedGapsLayer" type="QString"/>
      </Option>
    </checkConfiguration>
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
    <field name="RainGage" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Outlet" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Area" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Imperv" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Width" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Slope" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="CurbLen" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="SnowPack" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="N_Imperv" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="N_Perv" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="S_Imperv" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="S_Perv" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="PctZero" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="RouteTo" configurationFlags="None">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="IMPERVIOUS" name="IMPERVIOUS" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="OUTLET" name="OUTLET" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PERVIOUS" name="PERVIOUS" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="PctRouted" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="InfMethod" configurationFlags="None">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="CURVE_NUMBER" name="CURVE_NUMBER" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="GREEN_AMPT" name="GREEN_AMPT" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="HORTON" name="HORTON" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MODIFIED_GREEN_AMPT" name="MODIFIED_GREEN_AMPT" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MODIFIED_HORTON" name="MODIFIED_HORTON" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="SuctHead" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Conductiv" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="InitDef" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="MaxRate" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="MinRate" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Decay" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="DryTime" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="MaxInf" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="false" name="IsMultiline" type="bool"/>
            <Option value="false" name="UseHtml" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="CurveNum" configurationFlags="None">
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
    <alias name="" index="2" field="RainGage"/>
    <alias name="" index="3" field="Outlet"/>
    <alias name="" index="4" field="Area"/>
    <alias name="" index="5" field="Imperv"/>
    <alias name="" index="6" field="Width"/>
    <alias name="" index="7" field="Slope"/>
    <alias name="" index="8" field="CurbLen"/>
    <alias name="" index="9" field="SnowPack"/>
    <alias name="" index="10" field="N_Imperv"/>
    <alias name="" index="11" field="N_Perv"/>
    <alias name="" index="12" field="S_Imperv"/>
    <alias name="" index="13" field="S_Perv"/>
    <alias name="" index="14" field="PctZero"/>
    <alias name="" index="15" field="RouteTo"/>
    <alias name="" index="16" field="PctRouted"/>
    <alias name="" index="17" field="InfMethod"/>
    <alias name="" index="18" field="SuctHead"/>
    <alias name="" index="19" field="Conductiv"/>
    <alias name="" index="20" field="InitDef"/>
    <alias name="" index="21" field="MaxRate"/>
    <alias name="" index="22" field="MinRate"/>
    <alias name="" index="23" field="Decay"/>
    <alias name="" index="24" field="DryTime"/>
    <alias name="" index="25" field="MaxInf"/>
    <alias name="" index="26" field="CurveNum"/>
    <alias name="" index="27" field="Annotation"/>
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
    <default expression="" field="Annotation" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" notnull_strength="1" constraints="3" unique_strength="1" field="fid"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="2" unique_strength="1" field="Name"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="RainGage"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Outlet"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Area"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Imperv"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Width"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Slope"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="CurbLen"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="SnowPack"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="N_Imperv"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="N_Perv"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="S_Imperv"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="S_Perv"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="PctZero"/>
    <constraint exp_strength="0" notnull_strength="1" constraints="1" unique_strength="0" field="RouteTo"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="PctRouted"/>
    <constraint exp_strength="0" notnull_strength="1" constraints="1" unique_strength="0" field="InfMethod"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="SuctHead"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Conductiv"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="InitDef"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="MaxRate"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="MinRate"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Decay"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="DryTime"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="MaxInf"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="CurveNum"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Annotation"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="fid"/>
    <constraint exp="" desc="" field="Name"/>
    <constraint exp="" desc="" field="RainGage"/>
    <constraint exp="" desc="" field="Outlet"/>
    <constraint exp="" desc="" field="Area"/>
    <constraint exp="" desc="" field="Imperv"/>
    <constraint exp="" desc="" field="Width"/>
    <constraint exp="" desc="" field="Slope"/>
    <constraint exp="" desc="" field="CurbLen"/>
    <constraint exp="" desc="" field="SnowPack"/>
    <constraint exp="" desc="" field="N_Imperv"/>
    <constraint exp="" desc="" field="N_Perv"/>
    <constraint exp="" desc="" field="S_Imperv"/>
    <constraint exp="" desc="" field="S_Perv"/>
    <constraint exp="" desc="" field="PctZero"/>
    <constraint exp="" desc="" field="RouteTo"/>
    <constraint exp="" desc="" field="PctRouted"/>
    <constraint exp="" desc="" field="InfMethod"/>
    <constraint exp="" desc="" field="SuctHead"/>
    <constraint exp="" desc="" field="Conductiv"/>
    <constraint exp="" desc="" field="InitDef"/>
    <constraint exp="" desc="" field="MaxRate"/>
    <constraint exp="" desc="" field="MinRate"/>
    <constraint exp="" desc="" field="Decay"/>
    <constraint exp="" desc="" field="DryTime"/>
    <constraint exp="" desc="" field="MaxInf"/>
    <constraint exp="" desc="" field="CurveNum"/>
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
      <column name="RainGage" width="-1" type="field" hidden="0"/>
      <column name="Outlet" width="-1" type="field" hidden="0"/>
      <column name="Area" width="-1" type="field" hidden="0"/>
      <column name="Imperv" width="-1" type="field" hidden="0"/>
      <column name="Width" width="-1" type="field" hidden="0"/>
      <column name="Slope" width="-1" type="field" hidden="0"/>
      <column name="CurbLen" width="-1" type="field" hidden="0"/>
      <column name="SnowPack" width="-1" type="field" hidden="0"/>
      <column name="N_Imperv" width="-1" type="field" hidden="0"/>
      <column name="N_Perv" width="-1" type="field" hidden="0"/>
      <column name="S_Imperv" width="-1" type="field" hidden="0"/>
      <column name="S_Perv" width="-1" type="field" hidden="0"/>
      <column name="PctZero" width="-1" type="field" hidden="0"/>
      <column name="RouteTo" width="-1" type="field" hidden="0"/>
      <column name="PctRouted" width="-1" type="field" hidden="0"/>
      <column name="InfMethod" width="-1" type="field" hidden="0"/>
      <column name="SuctHead" width="-1" type="field" hidden="0"/>
      <column name="Conductiv" width="-1" type="field" hidden="0"/>
      <column name="InitDef" width="-1" type="field" hidden="0"/>
      <column name="MaxRate" width="-1" type="field" hidden="0"/>
      <column name="MinRate" width="-1" type="field" hidden="0"/>
      <column name="Decay" width="-1" type="field" hidden="0"/>
      <column name="DryTime" width="-1" type="field" hidden="0"/>
      <column name="MaxInf" width="-1" type="field" hidden="0"/>
      <column name="CurveNum" width="-1" type="field" hidden="0"/>
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
    <attributeEditorContainer showLabel="1" collapsed="0" groupBox="0" name="General" visibilityExpressionEnabled="0" collapsedExpressionEnabled="0" visibilityExpression="" columnCount="1" collapsedExpression="">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
      <attributeEditorField showLabel="1" name="Name" index="1">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="RainGage" index="2">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="Outlet" index="3">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="Area" index="4">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="Imperv" index="5">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="Width" index="6">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="Slope" index="7">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="CurbLen" index="8">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="SnowPack" index="9">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="N_Imperv" index="10">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="N_Perv" index="11">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="S_Imperv" index="12">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="S_Perv" index="13">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="PctZero" index="14">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="PctRouted" index="16">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorField showLabel="1" name="RouteTo" index="15">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" collapsed="0" groupBox="0" name="Infiltration" backgroundColor="#e9e4fd" visibilityExpressionEnabled="0" collapsedExpressionEnabled="0" visibilityExpression="" columnCount="1" collapsedExpression="">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
      <attributeEditorField showLabel="1" name="InfMethod" index="17">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
      </attributeEditorField>
      <attributeEditorContainer showLabel="0" collapsed="0" groupBox="1" name="Horton/Modified Horton" backgroundColor="#e9e4fd" visibilityExpressionEnabled="1" collapsedExpressionEnabled="0" visibilityExpression="&quot;InfMethod&quot; in ('HORTON' , 'MODIFIED_HORTON' )" columnCount="1" collapsedExpression="">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
        <attributeEditorField showLabel="1" name="MaxRate" index="21">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField showLabel="1" name="MinRate" index="22">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField showLabel="1" name="Decay" index="23">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField showLabel="1" name="DryTime" index="24">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField showLabel="1" name="MaxInf" index="25">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="0" collapsed="0" groupBox="1" name="Green_Ampt, Modified Green_Ampt" backgroundColor="#e9e4fd" visibilityExpressionEnabled="1" collapsedExpressionEnabled="0" visibilityExpression="&quot;InfMethod&quot; in ( 'GREEN_AMPT' ,  'MODIFIED_GREEN_AMPT' )" columnCount="1" collapsedExpression="">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
        <attributeEditorField showLabel="1" name="SuctHead" index="18">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField showLabel="1" name="Conductiv" index="19">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField showLabel="1" name="InitDef" index="20">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="0" collapsed="0" groupBox="1" name="Curve Number" backgroundColor="#e9e4fd" visibilityExpressionEnabled="1" collapsedExpressionEnabled="0" visibilityExpression="&quot;InfMethod&quot; =  'CURVE_NUMBER' " columnCount="1" collapsedExpression="">
        <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
          <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
        </labelStyle>
        <attributeEditorField showLabel="1" name="CurveNum" index="26">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField showLabel="1" name="Conductiv" index="19">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
        <attributeEditorField showLabel="1" name="DryTime" index="24">
          <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
            <labelFont strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
          </labelStyle>
        </attributeEditorField>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorField showLabel="1" name="Annotation" index="27">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
  </attributeEditorForm>
  <editable>
    <field name="Annotation" editable="1"/>
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
    <field labelOnTop="0" name="Annotation"/>
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
    <field name="Annotation" reuseLastValue="0"/>
    <field name="Area" reuseLastValue="0"/>
    <field name="Conductiv" reuseLastValue="0"/>
    <field name="CurbLen" reuseLastValue="0"/>
    <field name="CurveNum" reuseLastValue="0"/>
    <field name="Decay" reuseLastValue="0"/>
    <field name="DryTime" reuseLastValue="0"/>
    <field name="Imperv" reuseLastValue="0"/>
    <field name="InfMethod" reuseLastValue="0"/>
    <field name="InitDef" reuseLastValue="0"/>
    <field name="MaxInf" reuseLastValue="0"/>
    <field name="MaxRate" reuseLastValue="0"/>
    <field name="MinRate" reuseLastValue="0"/>
    <field name="N_Imperv" reuseLastValue="0"/>
    <field name="N_Perv" reuseLastValue="0"/>
    <field name="Name" reuseLastValue="0"/>
    <field name="Outlet" reuseLastValue="0"/>
    <field name="PctRouted" reuseLastValue="0"/>
    <field name="PctZero" reuseLastValue="0"/>
    <field name="RainGage" reuseLastValue="0"/>
    <field name="RouteTo" reuseLastValue="0"/>
    <field name="S_Imperv" reuseLastValue="0"/>
    <field name="S_Perv" reuseLastValue="0"/>
    <field name="Slope" reuseLastValue="0"/>
    <field name="SnowPack" reuseLastValue="0"/>
    <field name="SuctHead" reuseLastValue="0"/>
    <field name="Width" reuseLastValue="0"/>
    <field name="fid" reuseLastValue="0"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>

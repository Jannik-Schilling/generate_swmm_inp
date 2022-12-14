<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology|Symbology3D|Labeling|Fields|Forms|Actions|MapTips|Diagrams|AttributeTable|Rendering|CustomProperties|GeometryOptions|Relations" simplifyLocal="1" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" maxScale="0" symbologyReferenceScale="-1" simplifyDrawingHints="0" labelsEnabled="1" version="3.28.1-Firenze" simplifyAlgorithm="0" minScale="100000000" simplifyDrawingTol="1">
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
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="0,0,0,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="255,255,255,255" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0.4" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="3" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="if( @map_scale> 4000 ,3*4000/@map_scale,3)" name="expression" type="QString"/>
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
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style previewBkgrdColor="255,255,255,255" fontItalic="0" fontFamily="Arial" namedStyle="Standard" fontSizeUnit="Point" allowHtml="0" forcedItalic="0" fontWordSpacing="0" fontWeight="50" multilineHeightUnit="Percentage" capitalization="0" textColor="255,255,255,255" forcedBold="0" fontKerning="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0" textOrientation="horizontal" isExpression="1" fontSize="10" textOpacity="1" fieldName="concat( &quot;Name&quot; ,'\nh=' ,&quot;Elevation&quot;, ' m' )" useSubstitutions="0" legendString="Aa" blendMode="0" fontUnderline="0" fontStrikeout="0" multilineHeight="1">
        <families/>
        <text-buffer bufferSize="1" bufferSizeUnits="MM" bufferNoFill="1" bufferJoinStyle="128" bufferDraw="0" bufferBlendMode="0" bufferColor="250,250,250,255" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <text-mask maskSizeUnits="MM" maskedSymbolLayers="" maskOpacity="1" maskSize="0" maskEnabled="0" maskType="0" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskJoinStyle="128"/>
        <background shapeOffsetUnit="Point" shapeRadiiUnit="Point" shapeBorderWidth="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="2" shapeSizeUnit="Point" shapeDraw="1" shapeRotation="0" shapeJoinStyle="64" shapeOpacity="1" shapeRadiiX="0" shapeBorderColor="128,128,128,255" shapeSVGFile="" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeSizeType="0" shapeRotationType="0" shapeOffsetX="0" shapeBlendMode="0" shapeSizeY="0" shapeRadiiY="0" shapeOffsetY="0" shapeBorderWidthUnit="Point" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0">
          <symbol clip_to_extent="1" frame_rate="10" alpha="1" name="markerSymbol" type="marker" is_animated="0" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" locked="0" class="SimpleMarker" enabled="1">
              <Option type="Map">
                <Option value="0" name="angle" type="QString"/>
                <Option value="square" name="cap_style" type="QString"/>
                <Option value="125,139,143,255" name="color" type="QString"/>
                <Option value="1" name="horizontal_anchor_point" type="QString"/>
                <Option value="bevel" name="joinstyle" type="QString"/>
                <Option value="circle" name="name" type="QString"/>
                <Option value="0,0" name="offset" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
                <Option value="MM" name="offset_unit" type="QString"/>
                <Option value="35,35,35,255" name="outline_color" type="QString"/>
                <Option value="solid" name="outline_style" type="QString"/>
                <Option value="0" name="outline_width" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
                <Option value="MM" name="outline_width_unit" type="QString"/>
                <Option value="diameter" name="scale_method" type="QString"/>
                <Option value="2" name="size" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
                <Option value="MM" name="size_unit" type="QString"/>
                <Option value="1" name="vertical_anchor_point" type="QString"/>
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
          <symbol clip_to_extent="1" frame_rate="10" alpha="1" name="fillSymbol" type="fill" is_animated="0" force_rhr="0">
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
                <Option value="42,42,42,255" name="color" type="QString"/>
                <Option value="bevel" name="joinstyle" type="QString"/>
                <Option value="0,0" name="offset" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
                <Option value="MM" name="offset_unit" type="QString"/>
                <Option value="247,247,247,255" name="outline_color" type="QString"/>
                <Option value="no" name="outline_style" type="QString"/>
                <Option value="0.26" name="outline_width" type="QString"/>
                <Option value="MM" name="outline_width_unit" type="QString"/>
                <Option value="solid" name="style" type="QString"/>
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
        </background>
        <shadow shadowOffsetGlobal="1" shadowOffsetDist="1" shadowScale="100" shadowOffsetUnit="MM" shadowRadius="1.5" shadowDraw="0" shadowColor="0,0,0,255" shadowBlendMode="6" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="MM" shadowOpacity="0.69999999999999996" shadowOffsetAngle="135" shadowRadiusAlphaOnly="0"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format leftDirectionSymbol="&lt;" plussign="0" placeDirectionSymbol="0" autoWrapLength="0" addDirectionSymbol="0" multilineAlign="3" decimals="3" useMaxLineLengthForAutoWrap="1" rightDirectionSymbol=">" wrapChar="" reverseDirectionSymbol="0" formatNumbers="0"/>
      <placement repeatDistanceUnits="MM" dist="0" placement="1" maxCurvedCharAngleOut="-25" priority="5" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" fitInPolygonOnly="0" offsetUnits="MM" overlapHandling="PreventOverlap" placementFlags="10" yOffset="-3" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" allowDegraded="0" centroidWhole="0" overrunDistanceUnit="MM" lineAnchorTextPoint="CenterOfText" distMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" distUnits="MM" preserveRotation="1" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" geometryGeneratorType="PointGeometry" repeatDistance="0" polygonPlacementFlags="2" maxCurvedCharAngleIn="25" lineAnchorPercent="0.5" lineAnchorType="0" geometryGenerator="" quadOffset="1" centroidInside="0" rotationAngle="0" lineAnchorClipping="0" rotationUnit="AngleDegrees" offsetType="1" xOffset="0" geometryGeneratorEnabled="0"/>
      <rendering upsidedownLabels="0" scaleMax="900" fontMinPixelSize="3" drawLabels="1" limitNumLabels="0" scaleVisibility="1" fontMaxPixelSize="10000" obstacle="1" minFeatureSize="0" mergeLines="0" obstacleFactor="1" zIndex="0" scaleMin="0" maxNumLabels="2000" obstacleType="1" labelPerPart="0" fontLimitPixelSize="0" unplacedVisibility="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties"/>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" name="anchorPoint" type="QString"/>
          <Option value="0" name="blendMode" type="int"/>
          <Option name="ddProperties" type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
          <Option value="false" name="drawToAllParts" type="bool"/>
          <Option value="1" name="enabled" type="QString"/>
          <Option value="point_on_exterior" name="labelAnchorPoint" type="QString"/>
          <Option value="&lt;symbol clip_to_extent=&quot;1&quot; frame_rate=&quot;10&quot; alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; is_animated=&quot;0&quot; force_rhr=&quot;0&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot; enabled=&quot;1&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;0&quot; name=&quot;align_dash_pattern&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;square&quot; name=&quot;capstyle&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;5;2&quot; name=&quot;customdash&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;customdash_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;customdash_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;dash_pattern_offset&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;dash_pattern_offset_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;draw_inside_polygon&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;bevel&quot; name=&quot;joinstyle&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;60,60,60,255&quot; name=&quot;line_color&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;solid&quot; name=&quot;line_style&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0.1&quot; name=&quot;line_width&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;line_width_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;offset&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;offset_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;offset_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;ring_filter&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;trim_distance_end&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_end_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;trim_distance_end_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;trim_distance_start&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_start_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;trim_distance_start_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;tweak_dash_pattern_on_corners&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;use_custom_dash&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;width_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
          <Option value="0" name="minLength" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale" type="QString"/>
          <Option value="MM" name="minLengthUnit" type="QString"/>
          <Option value="0" name="offsetFromAnchor" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromAnchorUnit" type="QString"/>
          <Option value="0" name="offsetFromLabel" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromLabelUnit" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
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
    <DiagramCategory penColor="#000000" spacing="5" scaleDependency="Area" enabled="0" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" penAlpha="255" showAxis="1" opacity="1" minScaleDenominator="0" backgroundAlpha="255" minimumSize="0" penWidth="0" maxScaleDenominator="1e+08" sizeScale="3x:0,0,0,0,0,0" rotationOffset="270" width="15" barWidth="5" direction="0" lineSizeType="MM" scaleBasedVisibility="0" spacingUnit="MM" height="15" lineSizeScale="3x:0,0,0,0,0,0" sizeType="MM" labelPlacementMethod="XHeight" diagramOrientation="Up">
      <fontProperties strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
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
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="MaxDepth" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="InitDepth" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SurDepth" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Aponded" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
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
    <alias name="" index="3" field="MaxDepth"/>
    <alias name="" index="4" field="InitDepth"/>
    <alias name="" index="5" field="SurDepth"/>
    <alias name="" index="6" field="Aponded"/>
    <alias name="" index="7" field="Annotation"/>
  </aliases>
  <defaults>
    <default expression="" field="fid" applyOnUpdate="0"/>
    <default expression="" field="Name" applyOnUpdate="0"/>
    <default expression="" field="Elevation" applyOnUpdate="0"/>
    <default expression="" field="MaxDepth" applyOnUpdate="0"/>
    <default expression="" field="InitDepth" applyOnUpdate="0"/>
    <default expression="" field="SurDepth" applyOnUpdate="0"/>
    <default expression="" field="Aponded" applyOnUpdate="0"/>
    <default expression="" field="Annotation" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" notnull_strength="1" constraints="3" unique_strength="1" field="fid"/>
    <constraint exp_strength="0" notnull_strength="1" constraints="3" unique_strength="1" field="Name"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Elevation"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="MaxDepth"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="InitDepth"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="SurDepth"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Aponded"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0" field="Annotation"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="fid"/>
    <constraint exp="" desc="" field="Name"/>
    <constraint exp="" desc="" field="Elevation"/>
    <constraint exp="" desc="" field="MaxDepth"/>
    <constraint exp="" desc="" field="InitDepth"/>
    <constraint exp="" desc="" field="SurDepth"/>
    <constraint exp="" desc="" field="Aponded"/>
    <constraint exp="" desc="" field="Annotation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column name="Name" width="-1" type="field" hidden="0"/>
      <column name="Elevation" width="-1" type="field" hidden="0"/>
      <column name="MaxDepth" width="-1" type="field" hidden="0"/>
      <column name="InitDepth" width="-1" type="field" hidden="0"/>
      <column name="SurDepth" width="-1" type="field" hidden="0"/>
      <column name="Aponded" width="-1" type="field" hidden="0"/>
      <column name="fid" width="-1" type="field" hidden="0"/>
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
QGIS-Formulare können eine Python-Funktion haben,, die aufgerufen wird, wenn sich das Formular öffnet

Diese Funktion kann verwendet werden um dem Formular Extralogik hinzuzufügen.

Der Name der Funktion wird im Feld "Python Init-Function" angegeben
Ein Beispiel folgt:
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
    <attributeEditorField showLabel="1" name="MaxDepth" index="3">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField showLabel="1" name="InitDepth" index="4">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField showLabel="1" name="SurDepth" index="5">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField showLabel="1" name="Aponded" index="6">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
    <attributeEditorField showLabel="1" name="Annotation" index="7">
      <labelStyle overrideLabelColor="0" overrideLabelFont="0" labelColor="0,0,0,255">
        <labelFont strikethrough="0" description="MS Shell Dlg 2,8,-1,5,50,0,0,0,0,0" style="" bold="0" underline="0" italic="0"/>
      </labelStyle>
    </attributeEditorField>
  </attributeEditorForm>
  <editable>
    <field name="Annotation" editable="1"/>
    <field name="Aponded" editable="1"/>
    <field name="BearbDatum" editable="1"/>
    <field name="Bearbeiter" editable="1"/>
    <field name="Elevation" editable="1"/>
    <field name="FehlerCode" editable="1"/>
    <field name="InitDepth" editable="1"/>
    <field name="Korrektur" editable="1"/>
    <field name="MaxDepth" editable="1"/>
    <field name="Name" editable="1"/>
    <field name="Sch_Art" editable="1"/>
    <field name="Sch_Verf" editable="1"/>
    <field name="SurDepth" editable="1"/>
    <field name="Weg_Art" editable="1"/>
    <field name="Weg_Verf" editable="1"/>
    <field name="Zu_Art" editable="1"/>
    <field name="Zu_Verf" editable="1"/>
    <field name="fid" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="Annotation"/>
    <field labelOnTop="0" name="Aponded"/>
    <field labelOnTop="0" name="BearbDatum"/>
    <field labelOnTop="0" name="Bearbeiter"/>
    <field labelOnTop="0" name="Elevation"/>
    <field labelOnTop="0" name="FehlerCode"/>
    <field labelOnTop="0" name="InitDepth"/>
    <field labelOnTop="0" name="Korrektur"/>
    <field labelOnTop="0" name="MaxDepth"/>
    <field labelOnTop="0" name="Name"/>
    <field labelOnTop="0" name="Sch_Art"/>
    <field labelOnTop="0" name="Sch_Verf"/>
    <field labelOnTop="0" name="SurDepth"/>
    <field labelOnTop="0" name="Weg_Art"/>
    <field labelOnTop="0" name="Weg_Verf"/>
    <field labelOnTop="0" name="Zu_Art"/>
    <field labelOnTop="0" name="Zu_Verf"/>
    <field labelOnTop="0" name="fid"/>
  </labelOnTop>
  <reuseLastValue>
    <field name="Annotation" reuseLastValue="0"/>
    <field name="Aponded" reuseLastValue="0"/>
    <field name="BearbDatum" reuseLastValue="0"/>
    <field name="Bearbeiter" reuseLastValue="0"/>
    <field name="Elevation" reuseLastValue="0"/>
    <field name="FehlerCode" reuseLastValue="0"/>
    <field name="InitDepth" reuseLastValue="0"/>
    <field name="Korrektur" reuseLastValue="0"/>
    <field name="MaxDepth" reuseLastValue="0"/>
    <field name="Name" reuseLastValue="0"/>
    <field name="Sch_Art" reuseLastValue="0"/>
    <field name="Sch_Verf" reuseLastValue="0"/>
    <field name="SurDepth" reuseLastValue="0"/>
    <field name="Weg_Art" reuseLastValue="0"/>
    <field name="Weg_Verf" reuseLastValue="0"/>
    <field name="Zu_Art" reuseLastValue="0"/>
    <field name="Zu_Verf" reuseLastValue="0"/>
    <field name="fid" reuseLastValue="0"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>

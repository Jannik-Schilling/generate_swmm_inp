<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="100000000" labelsEnabled="1" simplifyDrawingHints="0" styleCategories="Symbology|Labeling|Fields|Forms|MapTips|Diagrams|AttributeTable|Rendering" simplifyMaxScale="1" version="3.28.0-Firenze" simplifyDrawingTol="1" simplifyLocal="1" simplifyAlgorithm="0" symbologyReferenceScale="-1" hasScaleBasedVisibilityFlag="0" maxScale="0">
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
            <Option value="0" type="QString" name="angle"/>
            <Option value="square" type="QString" name="cap_style"/>
            <Option value="0,0,0,255" type="QString" name="color"/>
            <Option value="1" type="QString" name="horizontal_anchor_point"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="circle" type="QString" name="name"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="255,255,255,255" type="QString" name="outline_color"/>
            <Option value="solid" type="QString" name="outline_style"/>
            <Option value="0.4" type="QString" name="outline_width"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option value="diameter" type="QString" name="scale_method"/>
            <Option value="3" type="QString" name="size"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
            <Option value="MM" type="QString" name="size_unit"/>
            <Option value="1" type="QString" name="vertical_anchor_point"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="size">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="if( @map_scale> 4000 ,3*4000/@map_scale,3)" type="QString" name="expression"/>
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
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontWeight="50" fontLetterSpacing="0" fontFamily="Arial" fontSize="10" multilineHeightUnit="Percentage" fontStrikeout="0" allowHtml="0" forcedItalic="0" fontItalic="0" previewBkgrdColor="255,255,255,255" textOrientation="horizontal" useSubstitutions="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fieldName="concat( &quot;Name&quot; ,'\nh=' ,&quot;Elevation&quot;, ' m' )" fontUnderline="0" isExpression="1" textColor="255,255,255,255" textOpacity="1" legendString="Aa" fontSizeUnit="Point" fontKerning="1" blendMode="0" fontWordSpacing="0" capitalization="0" multilineHeight="1" forcedBold="0" namedStyle="Standard">
        <families/>
        <text-buffer bufferSize="1" bufferOpacity="1" bufferJoinStyle="128" bufferSizeUnits="MM" bufferNoFill="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferDraw="0" bufferColor="250,250,250,255"/>
        <text-mask maskedSymbolLayers="" maskSizeUnits="MM" maskOpacity="1" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskSize="0" maskJoinStyle="128" maskEnabled="0" maskType="0"/>
        <background shapeSizeX="2" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeRadiiY="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeRotation="0" shapeSizeUnit="Point" shapeType="0" shapeBorderWidth="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="1" shapeBlendMode="0" shapeOffsetUnit="Point" shapeRadiiUnit="Point" shapeFillColor="255,255,255,255" shapeRadiiX="0" shapeSizeY="0" shapeRotationType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeOffsetY="0" shapeSizeType="0" shapeBorderColor="128,128,128,255" shapeBorderWidthUnit="Point" shapeJoinStyle="64">
          <symbol frame_rate="10" alpha="1" clip_to_extent="1" is_animated="0" type="marker" force_rhr="0" name="markerSymbol">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" type="QString" name="name"/>
                <Option name="properties"/>
                <Option value="collection" type="QString" name="type"/>
              </Option>
            </data_defined_properties>
            <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="square" type="QString" name="cap_style"/>
                <Option value="125,139,143,255" type="QString" name="color"/>
                <Option value="1" type="QString" name="horizontal_anchor_point"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="circle" type="QString" name="name"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="35,35,35,255" type="QString" name="outline_color"/>
                <Option value="solid" type="QString" name="outline_style"/>
                <Option value="0" type="QString" name="outline_width"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="outline_width_map_unit_scale"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="diameter" type="QString" name="scale_method"/>
                <Option value="2" type="QString" name="size"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="size_map_unit_scale"/>
                <Option value="MM" type="QString" name="size_unit"/>
                <Option value="1" type="QString" name="vertical_anchor_point"/>
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
          <symbol frame_rate="10" alpha="1" clip_to_extent="1" is_animated="0" type="fill" force_rhr="0" name="fillSymbol">
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
                <Option value="42,42,42,255" type="QString" name="color"/>
                <Option value="bevel" type="QString" name="joinstyle"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
                <Option value="MM" type="QString" name="offset_unit"/>
                <Option value="247,247,247,255" type="QString" name="outline_color"/>
                <Option value="no" type="QString" name="outline_style"/>
                <Option value="0.26" type="QString" name="outline_width"/>
                <Option value="MM" type="QString" name="outline_width_unit"/>
                <Option value="solid" type="QString" name="style"/>
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
        </background>
        <shadow shadowRadiusUnit="MM" shadowBlendMode="6" shadowOffsetUnit="MM" shadowUnder="0" shadowOffsetGlobal="1" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.69999999999999996" shadowOffsetAngle="135" shadowRadius="1.5" shadowDraw="0" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format placeDirectionSymbol="0" decimals="3" plussign="0" formatNumbers="0" addDirectionSymbol="0" autoWrapLength="0" wrapChar="" reverseDirectionSymbol="0" leftDirectionSymbol="&lt;" useMaxLineLengthForAutoWrap="1" multilineAlign="3" rightDirectionSymbol=">"/>
      <placement centroidInside="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" preserveRotation="1" allowDegraded="0" lineAnchorTextPoint="CenterOfText" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" overrunDistance="0" placement="1" centroidWhole="0" layerType="PointGeometry" offsetUnits="MM" dist="0" quadOffset="1" yOffset="-3" distMapUnitScale="3x:0,0,0,0,0,0" lineAnchorPercent="0.5" maxCurvedCharAngleOut="-25" geometryGeneratorEnabled="0" offsetType="1" geometryGenerator="" overlapHandling="PreventOverlap" priority="5" lineAnchorClipping="0" overrunDistanceUnit="MM" polygonPlacementFlags="2" rotationAngle="0" repeatDistance="0" lineAnchorType="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" xOffset="0" distUnits="MM" maxCurvedCharAngleIn="25" rotationUnit="AngleDegrees" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="10" fitInPolygonOnly="0"/>
      <rendering obstacleFactor="1" zIndex="0" scaleMax="900" fontMinPixelSize="3" mergeLines="0" fontLimitPixelSize="0" unplacedVisibility="0" labelPerPart="0" minFeatureSize="0" obstacleType="1" scaleMin="0" drawLabels="1" fontMaxPixelSize="10000" maxNumLabels="2000" obstacle="1" scaleVisibility="1" upsidedownLabels="0" limitNumLabels="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option name="properties"/>
          <Option value="collection" type="QString" name="type"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" type="QString" name="anchorPoint"/>
          <Option value="0" type="int" name="blendMode"/>
          <Option type="Map" name="ddProperties">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
          <Option value="false" type="bool" name="drawToAllParts"/>
          <Option value="1" type="QString" name="enabled"/>
          <Option value="point_on_exterior" type="QString" name="labelAnchorPoint"/>
          <Option value="&lt;symbol frame_rate=&quot;10&quot; alpha=&quot;1&quot; clip_to_extent=&quot;1&quot; is_animated=&quot;0&quot; type=&quot;line&quot; force_rhr=&quot;0&quot; name=&quot;symbol&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; type=&quot;QString&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; type=&quot;QString&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;align_dash_pattern&quot;/>&lt;Option value=&quot;square&quot; type=&quot;QString&quot; name=&quot;capstyle&quot;/>&lt;Option value=&quot;5;2&quot; type=&quot;QString&quot; name=&quot;customdash&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;customdash_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;customdash_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;dash_pattern_offset_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;draw_inside_polygon&quot;/>&lt;Option value=&quot;bevel&quot; type=&quot;QString&quot; name=&quot;joinstyle&quot;/>&lt;Option value=&quot;60,60,60,255&quot; type=&quot;QString&quot; name=&quot;line_color&quot;/>&lt;Option value=&quot;solid&quot; type=&quot;QString&quot; name=&quot;line_style&quot;/>&lt;Option value=&quot;0.1&quot; type=&quot;QString&quot; name=&quot;line_width&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;line_width_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;offset&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;offset_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;offset_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;ring_filter&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;trim_distance_end&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;trim_distance_end_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;trim_distance_end_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;trim_distance_start&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;trim_distance_start_map_unit_scale&quot;/>&lt;Option value=&quot;MM&quot; type=&quot;QString&quot; name=&quot;trim_distance_start_unit&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;Option value=&quot;0&quot; type=&quot;QString&quot; name=&quot;use_custom_dash&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; type=&quot;QString&quot; name=&quot;width_map_unit_scale&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; type=&quot;QString&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; type=&quot;QString&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString" name="lineSymbol"/>
          <Option value="0" type="double" name="minLength"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="minLengthMapUnitScale"/>
          <Option value="MM" type="QString" name="minLengthUnit"/>
          <Option value="0" type="double" name="offsetFromAnchor"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromAnchorMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromAnchorUnit"/>
          <Option value="0" type="double" name="offsetFromLabel"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromLabelMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromLabelUnit"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory backgroundAlpha="255" penColor="#000000" labelPlacementMethod="XHeight" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" height="15" penAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" spacingUnit="MM" maxScaleDenominator="1e+08" diagramOrientation="Up" sizeType="MM" sizeScale="3x:0,0,0,0,0,0" direction="0" minimumSize="0" spacing="5" rotationOffset="270" opacity="1" showAxis="1" minScaleDenominator="0" width="15" penWidth="0" barWidth="5" scaleBasedVisibility="0" enabled="0" lineSizeType="MM">
      <fontProperties bold="0" italic="0" strikethrough="0" description="Ubuntu,11,-1,5,50,0,0,0,0,0" style="" underline="0"/>
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
    <field configurationFlags="None" name="Sch_Verf">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Sch_Art">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Korrektur">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Weg_Verf">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Weg_Art">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Zu_Verf">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Zu_Art">
      <editWidget type="TextEdit">
        <config>
          <Option/>
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
    <field configurationFlags="None" name="Elevation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Bearbeiter">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="BearbDatum">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="FehlerCode">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="Annotation">
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
    <alias field="InitDepth" index="2" name=""/>
    <alias field="SurDepth" index="3" name=""/>
    <alias field="Aponded" index="4" name=""/>
    <alias field="Sch_Verf" index="5" name=""/>
    <alias field="Sch_Art" index="6" name=""/>
    <alias field="Korrektur" index="7" name=""/>
    <alias field="Weg_Verf" index="8" name=""/>
    <alias field="Weg_Art" index="9" name=""/>
    <alias field="Zu_Verf" index="10" name=""/>
    <alias field="Zu_Art" index="11" name=""/>
    <alias field="MaxDepth" index="12" name=""/>
    <alias field="Elevation" index="13" name=""/>
    <alias field="Bearbeiter" index="14" name=""/>
    <alias field="BearbDatum" index="15" name=""/>
    <alias field="FehlerCode" index="16" name=""/>
    <alias field="Annotation" index="17" name=""/>
  </aliases>
  <defaults>
    <default expression="" field="fid" applyOnUpdate="0"/>
    <default expression="" field="Name" applyOnUpdate="0"/>
    <default expression="" field="InitDepth" applyOnUpdate="0"/>
    <default expression="" field="SurDepth" applyOnUpdate="0"/>
    <default expression="" field="Aponded" applyOnUpdate="0"/>
    <default expression="" field="Sch_Verf" applyOnUpdate="0"/>
    <default expression="" field="Sch_Art" applyOnUpdate="0"/>
    <default expression="" field="Korrektur" applyOnUpdate="0"/>
    <default expression="" field="Weg_Verf" applyOnUpdate="0"/>
    <default expression="" field="Weg_Art" applyOnUpdate="0"/>
    <default expression="" field="Zu_Verf" applyOnUpdate="0"/>
    <default expression="" field="Zu_Art" applyOnUpdate="0"/>
    <default expression="" field="MaxDepth" applyOnUpdate="0"/>
    <default expression="" field="Elevation" applyOnUpdate="0"/>
    <default expression="" field="Bearbeiter" applyOnUpdate="0"/>
    <default expression="" field="BearbDatum" applyOnUpdate="0"/>
    <default expression="" field="FehlerCode" applyOnUpdate="0"/>
    <default expression="" field="Annotation" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" field="fid" notnull_strength="1" constraints="3" exp_strength="0"/>
    <constraint unique_strength="0" field="Name" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="InitDepth" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="SurDepth" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Aponded" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Sch_Verf" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Sch_Art" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Korrektur" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Weg_Verf" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Weg_Art" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Zu_Verf" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Zu_Art" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="MaxDepth" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Elevation" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Bearbeiter" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="BearbDatum" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="FehlerCode" notnull_strength="0" constraints="0" exp_strength="0"/>
    <constraint unique_strength="0" field="Annotation" notnull_strength="0" constraints="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="fid"/>
    <constraint desc="" exp="" field="Name"/>
    <constraint desc="" exp="" field="InitDepth"/>
    <constraint desc="" exp="" field="SurDepth"/>
    <constraint desc="" exp="" field="Aponded"/>
    <constraint desc="" exp="" field="Sch_Verf"/>
    <constraint desc="" exp="" field="Sch_Art"/>
    <constraint desc="" exp="" field="Korrektur"/>
    <constraint desc="" exp="" field="Weg_Verf"/>
    <constraint desc="" exp="" field="Weg_Art"/>
    <constraint desc="" exp="" field="Zu_Verf"/>
    <constraint desc="" exp="" field="Zu_Art"/>
    <constraint desc="" exp="" field="MaxDepth"/>
    <constraint desc="" exp="" field="Elevation"/>
    <constraint desc="" exp="" field="Bearbeiter"/>
    <constraint desc="" exp="" field="BearbDatum"/>
    <constraint desc="" exp="" field="FehlerCode"/>
    <constraint desc="" exp="" field="Annotation"/>
  </constraintExpressions>
  <expressionfields/>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column hidden="0" width="-1" type="field" name="Name"/>
      <column hidden="0" width="-1" type="field" name="Elevation"/>
      <column hidden="0" width="-1" type="field" name="MaxDepth"/>
      <column hidden="0" width="-1" type="field" name="InitDepth"/>
      <column hidden="0" width="-1" type="field" name="SurDepth"/>
      <column hidden="0" width="-1" type="field" name="Aponded"/>
      <column hidden="0" width="-1" type="field" name="fid"/>
      <column hidden="0" width="-1" type="field" name="Sch_Verf"/>
      <column hidden="0" width="-1" type="field" name="Sch_Art"/>
      <column hidden="0" width="-1" type="field" name="Korrektur"/>
      <column hidden="0" width="-1" type="field" name="Weg_Verf"/>
      <column hidden="0" width="-1" type="field" name="Weg_Art"/>
      <column hidden="0" width="-1" type="field" name="Zu_Verf"/>
      <column hidden="0" width="-1" type="field" name="Zu_Art"/>
      <column hidden="0" width="-1" type="field" name="Bearbeiter"/>
      <column hidden="0" width="-1" type="field" name="BearbDatum"/>
      <column hidden="0" width="-1" type="field" name="FehlerCode"/>
      <column hidden="0" width="-1" type="field" name="Annotation"/>
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
  <editorlayout>generatedlayout</editorlayout>
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
    <field reuseLastValue="0" name="Annotation"/>
    <field reuseLastValue="0" name="Aponded"/>
    <field reuseLastValue="0" name="BearbDatum"/>
    <field reuseLastValue="0" name="Bearbeiter"/>
    <field reuseLastValue="0" name="Elevation"/>
    <field reuseLastValue="0" name="FehlerCode"/>
    <field reuseLastValue="0" name="InitDepth"/>
    <field reuseLastValue="0" name="Korrektur"/>
    <field reuseLastValue="0" name="MaxDepth"/>
    <field reuseLastValue="0" name="Name"/>
    <field reuseLastValue="0" name="Sch_Art"/>
    <field reuseLastValue="0" name="Sch_Verf"/>
    <field reuseLastValue="0" name="SurDepth"/>
    <field reuseLastValue="0" name="Weg_Art"/>
    <field reuseLastValue="0" name="Weg_Verf"/>
    <field reuseLastValue="0" name="Zu_Art"/>
    <field reuseLastValue="0" name="Zu_Verf"/>
    <field reuseLastValue="0" name="fid"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>

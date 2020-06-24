# 내가 편하게 보려고 번역(하고있는) Lanelet Primitives
원본 출처 : https://github.com/fzi-forschungszentrum-informatik/Lanelet2/blob/master/lanelet2_core/doc/LaneletPrimitives.md

Lanelet2는 세계를 6개의 다른 primitive로 되어있는 계층구조로 나눈다. (Points, linestrings, polygons, lanelets, areas, regulatory elements)

이 문서는 primitive들이 사용되는 방법, 가지고 있는 속성, 어떻게 사용되어지는지에 대해 집중하고 있다. 기술적인 측면을 알고 싶다면, [architecture](Architecture.md) 페이지를 참조해라. (링크 맞춰줘야 함)

## Primitives
모든 primitive들은 key/value(혹은 tag/value)의 형태로 공통적으로 고유한 ID와 속성을 가지고 있다. 일반적으로 사용되어질 수 있는 tag에는 제한이 없지만, 특정한 tag들은 특별한 의미를 갖고 있다. 또한, lanelet primitive에서 공통적인 tag들은 커스텀 tag들보다 효율적으로 접근이 가능하는 구조로 저장되어 있다.

Tag는 항상 소문자와 underscore로 쓰여진다. 어떤 value는 특별한 의미를 갖고 있다. 예를 들어, "yes"와 "no"는 bool로 변환할 수 있다 (yes->true, no->false).


어떤 tag는 모든 primitive에서 사용된다. :

* **type**은 primitive가 속한 카테고리를 나타낸다. 예를 들어, `curbstone`, `traffic_sign`, `line_thin` 등은 road marking을 위해 사용된다.
* **subtype**은 유형을 추가적으로 구분하는 데 사용된다. 예를 들어, `low`는 올라탈 수 있는 연석을 표시하는 것이고, `dashed`는 점선을 나타내는 것이다.
* **no_issue** (yes/no): *yes*인 경우 lanelet2_validation에 의해 report된 primitive에 대한 경고를 표시하지 않는다.


## Points

Point는 ID, 3D 좌표, 속성으로 구성되어 있다. ID는 point마다 고유해야한다. Point는 Lanelet2 자체에서 의미가 있는 것은 아니다. Point는 Lanelet2에서 다른 object들과 함께할 때 의미가 있다. 유일하게 개별 point가 의미 있을 때는 dashed line marking에서의 시작점과 끝 점에 tagging할 때 이다.


### Coordinate System
Lanelet2는 지도가 x-y 평면에 놓여있다고 가정한다. 따라서 도로 geometry는 보통 평평하다고 생각해도 어느정도 무방하기 때문에, 다른 좌표에 비해 z좌표는 덜 중요하다. 그러므로 point는 z좌표가 무시되는 2D point로 쉽게 변환될 수 있다. 그래도 두 도로가 실제로 교차하거나, 다른 높이에서 서로 교차하는지 판단할 수 있도록 하는 3D 정보는 중요하다. 높이 정보를 결정할 때, 일반적으로 높이는 미터법을 사용하고 WGS84 좌표계를 사용한다. Geometry 계산에 대한 더 많은 정보를얻고 싶다면 [여기](GeometryPrimer.md)를 봐라. (링크 x)

일반적으로 "2.5D"-Approach를 따를 수 있어서, 높이는 0이고 교량 혹은 터널을 구별할때만 0이 아니다. 이 방법을 사용하기 위해서는 routing graph를 다르게 구성해야한다. 따라서 높이 거리(height distance) 1(새 레이어를 뜻함)이 1**m**로 오해석되지 않는다. (이것은 두 개의 충돌되는 차선으로 해석됩니다.)

## Linestrings

![Linestring](images/linestring.png) (사진 박살)

Linestrings (also known as polylines or linestrips) are defined by an ordered list of points with linear interpolation in between. They are the basic building block of a lanelet map and used for any phisically observable part of the map.


Linestrings must consist of at least one point to be valid and must not self-intersect. They must not contain points repeatedly (i.e. p1->p2->p2->p3 is not allowed). Linestrings must always have a *type* so that their purpose can be determined.

The tags used to define the individual linestrings are explained [here](LinestringTagging.md).

## Polygon

Polygons are very similar to linestrings, but form an area. It is implicitly assumed that the first and the last point of the polygon are connected to close the shape.

Polygons, are rarely used to transport mapping information (except for e.g. traffic signs). Instead, they often serve as a means to add customized information about an area to the map (e.g. a region of interest).

## Lanelet

![Lanelet](images/lanelet.png) (사진 박살)

A lanelet represents one *atomic* section of a lane. Atomic means that along a lanelet, traffic rules (including possible lane changes to other lanelts) do not change.

A lanelet consists of exactly one left and exactly one right linestring. Together they form the drivable area of the lanelet. It is required that the linestrings point into the same direction. That can mean that for two neighbouring, opposing lanelets one of them has to hold an inverted linestring as its border. When loading map data from osm, the library will do the alignment for you. If possible, the bounds should have a physical motivation (i.e. reference actual markings, curbstones, etc). The type of the boundary is used by the library to determine if lane changes are possible here.

lanelets may have an additional centerline to guide the vehicle. This centerline must be within the area formed by the left and right bound and must not touch the boundaries. If no centerline is given, the library will calculate it for you.

By default, lanelets are one-directional. Only if they are tagged as bidirectional, they are treated as such. Adjacent lanelets have to share the same endpoints so that the Lanelet2 can determine their status of being adjacent. Lanelets can also *diverge* when two or more lanelets are successors of a lanelet. Lanelets that are reachable by a lane change must share one of their borders.

A lanelet can reference *regulatory elements* that represent traffic rules that apply to the lanelet. Multiple lanelets can reference the same regulatory element.

It must always be possible to determine the current speed limit of the lanelet directly from the lanelet. This can either be done by referencing a SpeedLimit regulatory element or by tagging the *location* of the lanelet. In this case the maximum speed for the type of road is assumed (e.g. max 50kph if the location is a german city).

It must also be possible to determine the *participants* that are able to use the lanelet.

For more details on the exact tags of a Lanelet, please read [here](LaneletAndAreaTagging.md).

## Area

![Area](images/area.png) (사진 박살)

An Area has similar properties like a Lanelet, but instead of representing *directed* traffic from entry to exit, an area represents *undirected* traffic within its surface. An Area can have multiple entry and exit points. A typical example of an area would be squares that are used by pedestrians or parking lots and emergency lanes for vehicles. Similar to lanelets, traffic rules must not change on the areas.

Geometrically, an Area is represented by an ordered list of linestrings that together form the shape of the area in *clockwise* orientation. Areas must share exactly one linestring with an other area to be considered adajacent. For lanelets they either have to share one Linestring (when the lanelet is parallel to the area) or the endpoints of the lanelet are also the endpoints of one of the linestrings of the area (when the lanelet leads into the area). The area of an Area must not be zero and the bounds must not self-intersect.

The type of the shared boundary determines whether it is possible to *pass* from/to an area.

Areas can also have *holes*, i.e. parts of the area that are not acessible. It is not allowed that another Lanelet/area is within the hole of a bigger area. In this case, the "outer" area has to be split in two along the hole. Holes are represented similar to the outer bound: each by an ordered list of linestrings that together form the shape of the hole. The points must be in *counter-clockwise* order.

Tags that are applicable to lanelets also apply to Areas (where it makes sense). See [here](LaneletAndAreaTagging.md) for more.

Similarly to lanelets, Areas can refer to regulatory elements. Also, it must be possible to determine the pupose of the Area as well as by which participants it is usable.

## Regulatory Elements

![Regulatory element](images/regulatory_element.png) (사진 박살)

Regulatory elements are a generic way to express traffic rules. They are referenced by lanelets or Areas for which they apply.

In general, Regulatory elements consist of tags that generally express the type of the rule (i.e. a *traffic light* regulatory element) and specific information about the observable things that have a certain *role* for this rule (e.g. the traffic light itself and the stop line). Other types of regulatory elements are *right of way* and *traffic sign* regulatory elements. The list ist not closed at all, it is up to you to plug in more regulatory elements when necessary.

For more information how to tag the build-in regulatory elements, please read on [here](RegulatoryElementTagging.md).



 

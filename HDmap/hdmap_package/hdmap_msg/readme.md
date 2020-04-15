### Custom Msg만들기   
ros1, ros2의 msg 만들기는 굉장히 유사하고 쉽다. 하지만 몇가지만 숙지하자

  1. msg안에서 기본적으로 제공하는 스탠다드 형을 제외하고 geometry_msg나 can_msg를 쓸 때는 CMakeList에 꼭 dependencies 추가를 하도록 하자.
  (https://answers.ros.org/question/326008/ros2-run-symbol-not-found-on-custom-msg/)
  2. ros2와 ros1는 msg의 종류가 서로 상이한 것이 있으니 단순한 msg를 제외하고는 호환이 안된다.  (ros1 header <-> Time)  
  
  

``` python
uint8 PERSON=0
uint8 CENTERLANE=1
uint8 CURB=2
uint8 WHITELINE=3
uint8 DASHEDLINE=4
uint8 GUIDELINE=5
uint8 TRAFFICLIGHT = 6
uint8 TRAFFICSIGN = 7
uint8 CROSS=8
uint8 CCTV=9
uint8 STOPLINE=10
uint8 BUMP=11
uint8 AREA = 12

# Default ADD
uint8 ADD=0
uint8 MODIFY=0
uint8 DELETE=2
uint8 DELETEALL=3
# Update marker if MODIFY is set



builtin_interfaces/Time stamp
string ns
int32 id

int32 type
int32 action

geometry_msgs/Pose pose
geometry_msgs/Vector3 scale

# If want to set specific color of element
std_msgs/ColorRGBA color

# LINEs or MultiLine
geometry_msgs/Point[] points
std_msgs/ColorRGBA[] colors

string text
```

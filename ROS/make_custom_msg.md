# Artiv만의 Custom message를 만들어보자. (for ROS1)
여호영 / 2020.05.15

Ros에서 정해준 타입 뿐만 아니라 우리가 원하는 형식의 message를 만들 순 없을까?    
ROS1, ROS2에 따라서 message를 어떻게 만드는지 알아보자!(현재 페이지는 ROS1을 기반으로 작성되었다.)    


## 1. msg파일 작성
Custom message를 사용하려면 당연히 msg 파일을 만들어야 한다.    
msg 파일들은 msg 폴더에 저장하게 되는데, ```[ros1_workspace]/src/[package]``` 폴더에 'msg'라는 이름의 폴더를 만든다.    
그 후에 msg 폴더 안에 들어가서 nano, vim 같은 것을 이용해 텍스트를 작성한다.    
아래 예시과 같이 원하는 메시지 타입(ex. uint16)과 이름(ex. aps_act_feedback)을 작성한다. (#은 주석을 의미)    
여기서 메시지 타입은 공식적으로 존재하는 [공식 Ros message타입](http://wiki.ros.org/msg)을 따라야하며 이름은 원하는 대로 지으면 된다.    
**단, 이름은 모두 영문으로 소문자로 작성할 것!**
```
#Artiv Message_ver3.0
#2020.04.28

std_msgs/Header header

uint16 aps_act_feedback         #APS Feedback
uint16 brake_act_feedback       #Brake ACT Feedback
uint8 gear_position_feedback    #Gear position Feedback
int16 steering_angle_feedback   #Steering angle Feedback

uint8 estop_switch              #Switch State/E-Stop
uint8 autostandby_switch        #Switch State/Auto-Standby
uint8 apm_switch                #Switch State/APM S/W
uint8 asm_switch                #Switch State/ASM S/W
uint8 agm_switch                #Switch State/AGM S/W

uint8 override_feedback         #Override Feedback

float32 avgspeed                #Vehicle Speed

uint8 lampsignal                #Turn_Sig_feed

uint8 bps_feedback              #BPS_Feed
uint8 aps_feedback              #APS_Feed

uint8 door_fl                   #Door_Front_Left
uint8 door_fr                   #Door_Front_Right
uint8 safety_belt_driver        #Safety_belt(Driver)
uint8 trunk                     #TRUNK
uint8 door_rl                   #Door_Rear_Left
uint8 door_rr                   #Door_Rear_Right

float32 ws_fl                   #Wheel Speed Front Left
float32 ws_fr                   #Wheel Speed Front Right
float32 ws_rl                   #Wheel Speed Rear Left
float32 ws_rr                   #Wheel Speed Rear Right
```
위 처럼 텍스트 작성후 이름은 '[원하는 이름].msg'로 저장한다.

## 2. 환경설정
Custom message를 이용하기 위한 환경설정이라 하믄 CMakeLists.txt, package.xml을 수정하는 것이다.    
복잡해보일 수 있는 파일이지만 천천히 따라오면 어렵지 않다!

### (1) CMakeLists.txt
CMakeLists.txt 파일을 먼저 수정해보자.    
```[ros1_workspace]/src/[package]``` 다음과 같은 디렉토리에 있는 CMakeLists.txt 파일을 수정해보자.    
아마 패키지를 새로 만든 상황이라면 주석을 포함해 엄청 많은 것들이 적혀있을 것이다.    
~~쫄지말고~~ 다음과 같은 예시에 있는 내용만 남겨놓자.    

```
cmake_minimum_required(VERSION 2.8.3)
project(candb)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

add_message_files(
  FILES
  Artivmsg.msg
  ERPmsg.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS 
  message_runtime
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
```
위 내용 중 'find_package', 'add_message_files'등 여러 함수(?)가 주석처리 되어 있을 것이다.    
주석을 다 지우고 'find_package'에는 'std_msgs', 'message_generation'을 추가.    
'add_message_files'에는 방금 작성한 '[원하는 이름].msg'을 추가.    
'generate_messages'에는 'std_msgs'를 추가.    
'catkin_package'에는 'std_msgs', 'message_runtime'을 추가.    
(모든 곳에 std_msgs는 이미 입력되어 있을 수도...)    

CMakeList.txt파일 수정은 끝!    

### (2) package.xml
다음으로는 비교적 ~~html같이~~ 만만해보이는 package.xml 파일을 수정해보자.    
이 파일도 CMakeList.txt 처럼 주석이 엄청 많을텐데 예시처럼 그냥 다 지우면 된다.    
이번에도 아래 예시를 먼저 보고 천천히 따라와보자.    
```
<?xml version="1.0"?>
<package format="2">
  <name>candb</name>
  <version>0.0.0</version>
  <description>The candb package</description>
  <maintainer email="hoyeong@dgist.ac.kr">hoyeong</maintainer>

  <license>TODO</license>
  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_depend>message_generation</build_depend>
  <build_export_depend>roscpp</build_export_depend>
  <build_export_depend>rospy</build_export_depend>
  <build_export_depend>std_msgs</build_export_depend>
  <exec_depend>roscpp</exec_depend>
  <exec_depend>rospy</exec_depend>
  <exec_depend>std_msgs</exec_depend>
  <exec_depend>message_runtime</exec_depend>
  <export>

  </export>
</package>
```
위에서부터 'xml version'~'buildtool_depend'까지는 있었던 대로 두면 될 것 같다.(잘 모름)    
'build_depend'에 'message_generation' 추가.    
'exec_depend'에 'message_runtime' 추가.    
('roscpp', 'rospy', 'std_msgs'는 기본적으로 입력되어 있을텐데 만약 없다면 입력하도록.)    

package.xml 파일도 수정 완료!    
이로써 Custom message를 이용하기 전에 필요한 제작 과정은 끝났다.
막상 수정해보니 별거 아니다~    
이제는 코드를 통해서 파이썬에서 어떻게 사용되는지 확인해보자.    

이는 ['Custom message는 어떻게 사용할까?'](https://github.com/shinkansan/ARTIV/edit/master/Comms/CAN/how_to_use_msg.md)페이지에서 확인해보자.

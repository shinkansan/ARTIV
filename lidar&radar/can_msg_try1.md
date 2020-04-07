# CAN 데이터 Publish 시도 1
날짜 : ~2020.04.06    
글쓴이 : 여호영

## rosbag에서 radar 관련된 topic은 무엇인가?
처음에 `rostopic list`를 입력했을 때, radar 혹은 모델명인 ars-308 같은 이름을 가진 topic이 없어서 당황.    
그래서 rosbag에 대해 자세한 정보를 주는 `rosbag info [bag file]`을 입력하였다.    
그 결과 radar 관련 topic으로 보이는 `/received_message` (맞나?)를 찾았고 이는 `can_msgs/frame`이라는 type으로 publish 되고 있었다.

## rosbag에서 radar 관련 topic를 출력해보자.
명령어 `rostopic echo -b [bag file] [topic name]` 을 입력해서 어떠한 정보가 나오는지 확인하였다.    
(여기서 조금 이상했던 것이 명령어 `rosmsg show /received_message can_msgs/frame` 은 되지 않았다.)    
그러니 header, uint32, uint8 등의 데이터 타입을 가지는 요소들이 출력되었다.    

## can_msgs는 ros의 표준(?) 타입인가?
can_msgs는 ros의 기본 폴더(?) `(/opt/ros/melodic)`에 있는 메시지 타입이 아니었기 때문에 ros 홈페이지에서 따로 다운 받아야 했었다.    
파일을 뜯어보니 `can_msgs/src` 폴더 안에 `Frame.msg`라는 것이 있었고 이는 topic에서 출력되는 형태가 텍스트로 저장되어있었다.    
근데 `can_msgs` 폴더 안에 있는 `CMakeList.txt` 파일과 `package.xml` 파일을 확인해봤는데 ros의 표준(?) 타입인 std_msgs만 dependency로 저장되어있다? 이전에는 `can_msgs/frame`이라는 ros 내에서 subscribe하고 publish 하기 위해서 관련 헤더파일을 include 해야했는데 `can_msgs`에는 없다. `can_msgs`는 msg일뿐 헤더파일도 없고 cpp 파일에서 include 할 수도 없는 타입의 메시지는 아닐까? 하는 생각이 들었다.    
단지 종속된 타입인 std_msgs만 이용하면 되는 것이다.(확실하진 않음.)    

# rosbag의 topic을 subscribe하는 cpp 파일을 만들어보자.
`[package_name]/src/print_radar.cpp` 의 code를 다음과 같이 작성했다.
```
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Header.h"
#include "std_msgs/UInt32.h"
#include "std_msgs/Bool.h"
#include "std_msgs/UInt8.h"
#include "std_msgs/UInt8MultiArray.h"

#include <vector>

void frameCallback(const std_msgs::Header::ConstPtr& msg)
{
  int x = msg->seq;
  ROS_INFO("The sequence is : %d", x);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "Print_rosbag_data");

  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("frame", 1000, frameCallback);
  ros::spin();

  return 0;
}
```

`[package_name]/CMakeLists.txt` 에는 다음과 같은 code를 추가했다.
```
add_executable(print_radar src/print_radar.cpp)
target_link_libraries(print_radar ${catkin_LIBRARIES})
add_dependencies(print_radar radar_data_generate_messages_cpp)
```

`[package_name]/package.xml` 에는 기본적으로 `std_msgs`가 포함되어있기 때문에 딱히 수정할 필요가 없었다.    
다음과 같은 code로 성공적으로 `catkin build`를 완료하고 rosbag을 킨 다음에 `print_radar.cpp` 파일을 실행했다.    
근데 아무 것도 출력되지 않았다 ㅠㅠ.

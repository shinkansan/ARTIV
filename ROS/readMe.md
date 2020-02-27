# ROS Repos A to Z
Author : Gwanjun Shin <br/>
date : 2020.02.04.

## How to install
 Goto [Link](https://index.ros.org/doc/ros2/Installation/Dashing/Linux-Install-Debians/#dashing-linux-ros1-add-pkgs) <br/>
 we use __ros2 dashing__ for our integrated SW. _Be aware that there are many version of ros2_
 
 
### installation final job
we need to assign setup.bash file to bashrc. so that we don't have to source it as we open terminal
```bash
# type below command
export source /opt/ros/dashing/setup.bash
```

## What's in Repos
### 1. [image_rclpy.py](./image_rclpy.py)
Connect ROS2 with Python
### 2. [ros2-ros1-bridge.md](./ros2-ros1-bridge.md)

### 3. [make-package-ros2.md](./make-package-ros2.md)

### 4. [make-publisher-package.md](./make-publisher-package.md)
Publisher/Subscriber for Sensor input with C++ or Python

### 5. [유용한 초반 ROS 공부 블로그](./start-ros-begin.md)   

###
__IMPORTANT__ require 1,2,3 courses


## 공부법
 1. pinkwink에 있는 블로그를 보면서 ROS 주요 용어를 익힌다.
 2. ROS1-melodic ROS2-dashing 를 설치한다. (설치법은 위에 있음)
 3. pinkwink에 있는 ROS2 관련 예제를 수행한다.
 4. ros2-ros1 bridge를 깔고, md에 있는 예제를 수행한다.
 5. ROS에서 C++ Python 둘다 패키지를 만들 수 있도록 예제로 만들어본다.
 6. Subscriber 프로그램을 만들어보자! (image_rclpy 는 Python이고 CPP로 만드는게 과제다.)
 7. Publisher를 만들어보면서 각 msg 타입은 뭔지, 어떤 식으로 검색하고 정보를 얻을 수 있는지 깨닫는다. (만들어보는게 과제다)
 8. RVIZ 시각화와 RQT를 공부한다. (RQT는 깊게 말고, 통합SW 팀이 주로한다.) (곧 통합 SW에서 RQT 관련 설치 매뉴얼을 배포할것이다.)
 9. ROS에 대해 감은 잡혔다 (1/100) 
 
이제 남이 올린 코드를 수정하면서 배워보자!



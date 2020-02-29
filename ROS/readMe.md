# ROS Repos A to Z
Author : Gwanjun Shin <br/>
date : 2020.02.04.

* 한국어와 영어가 섞여있는데, 중복되는 말도 있습니다. ubuntu가 영어밖에서 안되서 작성하고 개인 컴으로 한글화 하는거라 양해바랍니다!

## How to install
 
 * ROS2 install 하기
 
 Goto [Link](https://index.ros.org/doc/ros2/Installation/Dashing/Linux-Install-Debians/#dashing-linux-ros1-add-pkgs) <br/>
 we use __ros2 dashing__ for our integrated SW. _Be aware that there are many version of ros2_
 
 
### installation final job
we need to assign setup.bash file to bashrc. so that we don't have to source it as we open terminal

인스톨이 다 끝나면, 여기서 고려해야되는게 있다. ROS1도 깔고 2도 깔면 Terminal 창에서 그때그때 어떤 ROS를 사용할지는 골라줘야한다.

즉 ros1은 melodic이라고 한다. `source /opt/ros/melodic/setup.bash` 를 치면 이 명령어를 __타입한 터미널은 melodic 명령어가 들어간다.__   
그리고 ros2는 dashing 이라고 한다. `source /opt/ros/dashing/setup.bash`를 치면 이 명령어를 __타입한 터미널은 dashing 명령어가 들어간다.__ 

원래 하나만 쓰는거면 터미널을 킬 때마다 자동으로 저 명령어가 타입되도록 ~/.bashrc (환경변수 설정같은거다 윈도우 치면 시작프로그램 설정?) 
안에 기입해주면 된다. 

자기가 bashrc 라는거에 뭔가 복사해서 이미 넣은 것 같다면, 무서워 하지말고
`sudo nano ~/.bashrc`를 치면 무언가 많이 나올 것이다. 보통 `ALT+/` 를 치면 그 문서의 맨 아래로 내려가는데 거기에 위에 source ~ 뭐시기가 있는지 확인해보는 것도 좋고.. 바로 아래에 있는 명령어는 source ~ 뭐시기를 bashrc에 추가한다는 말이다. 

만약 본인이 bashrc를 수정했다면 수정본은 __새로운 터미널을 열때부터 적용된다__, 만약 같은 터미널에서 적용된 버전을 보고 싶으면 
   `source ~/.bashrc` 라고 치면된다.

설명하면 source는 따라오는 스크립트를 실행한 터미널에 적용한다 하는 뜻이다.
```
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
> 오류가 나면 echo 앞에 sudo를 붙여 권한을 높일 필요가 있다.   

그래서 위 명령어를 만약에 자기가 ROS1만 사용하겠다 라고 하면 저기다가 치면된다. 반대로 ros2면? melodic을 dashing 바꾸면 되겠죠?

여튼 앞으로 ROS1과 ROS2를 번갈아 가면서 사용할텐데 우리 팀원 여러분들은 필요에 따라 source /opt/ros.~~ 이런 명령어를 수없이 치면서 바꿔야한다.   
당연히 스크립트가 shortcut 있지만 기본적으로 언제나 먹히는 방법이니 외우자!

그리고 ros2로 bashrc에 적용했다해도, ros1으로 바꾸고 싶으면 그냥 터미널에 `source /opt/ros/melodic/setup.bash` 치면 바뀐다. 맘대로 설정하자.



## What's in Repos
### 1. [image_rclpy.py](./image_rclpy.py)
Connect ROS2 with Python .. (그냥 예제 코드 스킵가능)

### 2. [ros2-ros1-bridge.md](./ros2-ros1-bridge.md)
설치를 다했다면 ros1과 2를 연결하는 방법을 배워보자
 1. 예제 ros2로 webcam 띄우고, ros1의 rviz로 보기

### 3. [make-package-ros2.md](./make-package-ros2.md)
 패키지를 만들어보자, 기트허브에서 ros 전용으로 작성된 코드들을 이 챕터를 거치면 컴파일 해서 사용할 수 있다.

### 4. [make-publisher-package.md](./make-publisher-package.md)
Publisher/Subscriber for Sensor input with C++ or Python
 토픽의 발행과 구독?에 대한 코드를 작성하면서 ros와 cpp를 어떻게 연동하는지 알아보자   
 그런 김에 rosbag 사용법과 topic 활용에 유용한 명령어도 알아보자

__IMPORTANT__ require 1,2,3 courses

### 5. [유용한 ROS2 관련 사이트 및 블로그](./start-ros-begin.md)   
RTOS, RMW, RTPS 등 어려운 용어들이 많이 사용되는 ROS 설명글들과
service, msg등 다양한 타입의 예제를 다룬 ROS 사이트를 적어놓습니다. 각자 좋은 자료 찾으면 추가해주세요!



## 공부법
 1. pinkwink에 있는 블로그를 보면서 ROS 주요 용어를 익힌다.
 2. ROS1-melodic ROS2-dashing 를 설치한다. (설치법은 위에 있음)
 3. pinkwink에 있는 ROS2 관련 예제를 수행한다.
 4. ros2-ros1 bridge를 깔고, md에 있는 예제를 수행한다.
 5. ROS에서 C++ Python 둘다 패키지를 만들 수 있도록 예제로 만들어본다. __(예제를 따라서 만들어보기 (과제))__
 6. Subscriber 프로그램을 만들어보자! (image_rclpy 는 Python이고 CPP로 만드는게 과제다.) -> 필자가 깜빡하고 make-publisher-package.md에 다 해버렸다. 그래도 각자 코드를 하나하나 수정하고 넣어보면서 공부해도록 하자.
 
 7. Publisher를 만들어보면서 각 msg 타입은 뭔지, 어떤 식으로 검색하고 정보를 얻을 수 있는지 깨닫는다. __(만들어보는게 과제다)__
 8. RVIZ 시각화와 RQT를 공부한다. (RQT는 깊게 말고, 통합SW 팀이 주로한다.) (곧 통합 SW에서 RQT 관련 설치 매뉴얼을 배포할것이다.)
 9. ROS에 대해 감은 잡혔다 (1/100) 
 
이제 남이 올린 코드를 수정하면서 배워보자!

7번 퍼플리셔 과제 상세.
make-publisher-package.md에 joinst state에 보면 속도가 나오는데 KM/H 이다 이를 M/S를 바꿔서 새로 publish 해보자, 이경우 JointState 가 아닌 새로운 토픽 /ms_speed 로 만들어라 형은 Float64 type으로 진행하여라



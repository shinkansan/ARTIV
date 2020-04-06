#  독자적인 통합 UI 개발을 위한 RQT 벤치마킹

Author : Juho Song <br/>
date : 2020.04.05.

* 여러분의 UI 개발에서 느끼는 막막함을 조금이나마 해소해주길...

  ##

  ### Conditioning

  __먼저,__

  우리 깃허브의 __[ROS](https://github.com/shinkansan/ARTIV/tree/master/ROS)__ 를 통해 기본적인 ROS 설치 및 이용방법을 먼저 숙지하시고 와주세요.
  
  우리 깃허브의 __[QT Creator 매뉴얼](https://github.com/shinkansan/ARTIV/blob/master/Manual/QT%20Creator.md)__ 를 보고 QT Creator와 부가기능들을 설치하고 와주세요.
  
  ##
  
  ### step 1. RQT 설치
  
  아래의 코드를 터미널에 입력하여, 우리가 사용하는 ROS1 melodic version의 rqt와 해당 UI에서 띄울 수 있는 plugin 패키지들을 다운받습니다.
  
  코드 : `$ sudo apt-get install ros-melodic-rqt ros-melodic-rqt-common-plugins`
 
  ### step 2. RQT 실행
  
  기본 루틴 아시죠? `start_ros1` 또는 `source /opt/ros/melodic/setup.bash`하고 `roscore` 실행
  
  터미널 하나 더 열어서 `rqt` 실행합니다.
  
  처음 실행하면 아래 사진처럼, 아무것도 없는 Default-rqt 창이 뜹니다.
  
  ![Default-rqt](https://user-images.githubusercontent.com/59792475/78566793-b3f83780-785a-11ea-8963-7897e34b112d.png)

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
  
  코드 : `$ sudo apt-get install ros-melodic-rqt ros-melodic-rqt-common-plugins`
  
  기능 : 우리가 사용하는 ROS1 melodic version의 rqt와 해당 UI에서 띄울 수 있는 plugin 패키지들을 다운받습니다.

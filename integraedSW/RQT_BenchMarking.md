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
  
  ##
 
  ### step 2. RQT 실행
  
  기본 루틴 아시죠? `start_ros1` 또는 `source /opt/ros/melodic/setup.bash`하고 `roscore` 실행
  
  터미널 하나 더 열어서 `rqt` 실행합니다.
  
  처음 실행하면 아래 사진처럼, 아무것도 없는 Default-rqt 창이 뜹니다.
  
  ![Default-rqt](https://user-images.githubusercontent.com/59792475/78566793-b3f83780-785a-11ea-8963-7897e34b112d.png)
  
  상단의 왼쪽에서 두번째, Plugins를 클릭하면 아까 rqt와 함께 깔았던 각종 plugin을 창에 띄울 수 있습니다.
  
  default_rqt 창 위에 띄우는 것 말고도, 아래 사진처럼 `rqt_해당플러그인이름` 을 터미널에 입력하여 해당 UI만을 띄울 수도 있습니다.
  
  ![rqt_console](https://user-images.githubusercontent.com/59792475/78569655-e2781180-785e-11ea-94f6-de43b46cc604.png)
  
  ##
  
  ### 예제. turtlesim 노드의 log 확인하기 
  
  가장 기본 예제인, turtlesim 노드를 켜서 손으로 조작해보았습니다. 
  
  turtlesim 노드는 거북이가 처음 생성될 때 information의 형태로 좌표를 알려주고,
  
  벽에 부딛힐 때마다 warning을 합니다. 즉, turtlesim 노드에서 생성되는 log는 information과 warning으로 두 종류입니다.
  
  실행 사진을 첨부합니다.
  
  ![turtlesim_example](https://user-images.githubusercontent.com/59792475/78568758-895bae00-785d-11ea-984b-8cd63ff3e0ff.png)
  
  
  아래 사진은 제가 rqt의 logging 관련 plugin들을 창에 띄우고 turtlesim 노드를 이용하여, ROS log를 시각화해본 결과입니다.
  
  
  
  ![rqt2](https://user-images.githubusercontent.com/59792475/78568962-d93a7500-785d-11ea-85f8-af67a46ae777.png)
  
  부가 기능인, Exclude Messages를 통해 Warning을 제외하면, 가장 처음에 information의 형태로 초깃값이 주어졌다는 사실도 확인할 수 있었습니다.
  
  ![rqt1](https://user-images.githubusercontent.com/59792475/78569211-3c2c0c00-785e-11ea-8f01-2417f95f164c.png)

  
  ### 활용
  
  위의 예시에서, 제가 담당한 log 관련 UI가 있었듯이, 팀원 여러분들께서 맡은 분야들도 전부 찾을 수 있었습니다.
  
  먼저 저처럼 기본 예제부터 돌려보시면서 관심있는 UI의 작동을 한 번 확인해보세요.
  
  그 후, 아래 링크에서 해당 플러그인을 검색하면 rqt에 내장된 소스코드를 찾을 수 있습니다.
  
  완성되어있는 UI가 자체적으로 기능이 많다보니 다소 복잡하여 이해하기 어려울 수도 있지만, 해당 코드를 벤치마킹하거나 자신의 코드와 비교해보길 바랍니다.
  
  [rqt 소스코드](https://github.com/ros-visualization) 
  

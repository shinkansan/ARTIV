# VANGUARD

<p align="center"><img src="https://user-images.githubusercontent.com/59792475/85998620-01dd9f80-ba46-11ea-966c-e1af38672d25.png"></p>

<p align="center">Author : Juho Song</p>
<p align="center">date : 2020.06.29.</p>

## Environment & Dependencies

  * Developed with ROS2, Python3

  * Get Info : [dbw_ioniq_node](https://github.com/shinkansan/ARTIV/tree/master/Comms/Ioniq/dbw_ioniq/dbw_ioniq_node), /Joint_state (topic) <br>
  ![dbw_ioniq_rosbag_rqt](https://user-images.githubusercontent.com/59792475/81559090-ca4d6200-93c9-11ea-8c90-9aa113fa7ce5.png) <br>
  * Vehicle Control : [dbw_cmd_node](https://github.com/shinkansan/ARTIV/tree/master/Comms/Ioniq/dbw_ioniq/dbw_cmd_node)

## Motivation & Background
  
#### Starts from Fatal Break Issue    
  
<br>
  
개발 과정 중 아래와 같은 **치명적인 브레이크 초깃값 설정 ISSUE**를 발견하여 **자가진단 프로토콜의 필요성**을 느꼈다. 

##
##### ISSUE
  
`차량 시동을 걸기위해서는 운전자가 브레이크를 누르고 시동을 걸어야 한다.`
  
`이때, 동시에 자율주행 모드를 키면, 차량 제어에 사용되는 브레이크 액츄에이터가 브레이크 패널과 떨어진 상태로 시작된다.` 
  
`즉, 자율주행 모드를 시작하는 순간에 브레이크가 외부요인에 의해 눌려있었다면, 브레이크 제어가 제대로 되지 않는다.`
  
##
#### Discussion for Solution 

- [x] `기본적으로` __주행 매뉴얼__`을 제작하고, 새로운 Issue가 생길 때마다 추가하여 주의하도록 하는 방법.`

- [ ] ~~__하드웨어적인 접근__`으로 브레이크 액츄에이터를 포함한 차량 외적인 장치들을 관리하는 방법.`~~

- [x] `브레이크를 포함한 주요한` **차량 정보 토픽들의 발행상태를 주행 전에 진단**`하여 모든 진단이 끝나고 문제가 없을 때 주행을 시작하는 방법.`

<br>
  
논의 결과, 언맨사에서 제작한 장치들을 직접 관리하는 것은 불가능하고, 주행 매뉴얼 배포와 SW적인 접근으로 자가진단을 하는 방법이 채택되었다.
  
초기값 진단 프로그램을 Base로 **초기값 진단 및 Sensor State 및 차량 정보 Topic 발행에 대한 진단을 하는 프로그램, VANGUARD**를 구상하였다. 
  
## Intended Structure

* 개발 시작 단계에서 작성한 VANGUARD의 구조도

![vanguard v1](https://user-images.githubusercontent.com/59792475/86013499-2d6a8500-ba5a-11ea-9c2e-06cdae431fd8.png)

![vanguard v2](https://user-images.githubusercontent.com/59792475/86013595-496e2680-ba5a-11ea-9659-7adb48d7a2ce.png)
  
  
  #### 일련의 과정을 끝냈다면, 아래 매뉴얼을 참고하여 프로그램이 시작될 때 커맨드가 자동으로 실행되도록 설정해줍시다.
  
  __[우분투 시작 명령어 자동 실행 매뉴얼 (abt 한영키)](https://github.com/shinkansan/ARTIV/blob/master/Manual/Startup_Setting_Hangul.md)__
  
  ##
  ### 2. 사용자 비밀번호를 쉽게쉽게
  
   정말 사소할 수도 있지만, 우분투로 코딩 할 때 sudo를 많이 사용하고 그 때마다 사용자 비밀번호를 입력해야합니다.~~개귀찮음~~
   
  처음 설정했던 복잡한 비밀번호 대신 간단한 사용자 비밀번호를 통해 개발 속도를 조금이나마 향상시킬수 있어요 ㅎㅎ..


> 앞으로 추가해야 할 사항   
> **1. 현재 Play->Stop->다시 Play를 누를 경우 에러 발생, 수정해야 함**   
> 2. clear 버튼 추가하여 원할 경우에만 리스트 클리어 수행   
> 3. 특정 상태 메세지('No topic is playing' 등)는 계속 띄울 경우 current row에 계속 쓰여지도록   
> 4. ROS1 토픽도 띄우는거?   
> 5. ARTIV 로고 추가~   
> 6. 이쁜 디자인~   


#  VANGUARD

* 안전한 주행을 위한 초깃값 진단 및 주행 단계에서의 실시간 진단, 통합 프로그램 

![vanguard logo](https://user-images.githubusercontent.com/59792475/85998620-01dd9f80-ba46-11ea-966c-e1af38672d25.png)

Author : Juho Song<br>
date : 2020.06.29.

## Environment
  Python3
  
  ROS2

## Dependencies

  Get Info : __[dbw_ioniq_node](https://github.com/shinkansan/ARTIV/tree/master/Comms/Ioniq/dbw_ioniq/dbw_ioniq_node)__, /Joint_state (topic) <br>
  ![dbw_ioniq_rosbag_rqt](https://user-images.githubusercontent.com/59792475/81559090-ca4d6200-93c9-11ea-8c90-9aa113fa7ce5.png) <br>
  Vehicle Control : __[dbw_cmd_node](https://github.com/shinkansan/ARTIV/tree/master/Comms/Ioniq/dbw_ioniq/dbw_cmd_node)__

## Structure

* 개발 시작 단계에서 작성한 VANGUARD의 구조도

![VANGUARD](https://user-images.githubusercontent.com/59792475/85997591-a5c64b80-ba44-11ea-8fa3-6a98d010f002.png)

  ##
  ### VANGUARD 개발 배경 및 설계   
  
  개발 과정 중 치명적인 브레이크 초깃값 설정 Issue를 발견하여 자가진단 프로토콜의 필요성을 느꼈다. 
  
  차량 시동을 걸기위해서는 운전자가 브레이크를 누르고 시동을 걸어야 한다.
  이때, 동시에 자율주행 모드를 키면, 차량 제어에 사용되는 브레이크 액츄에이터가 브레이크 패널과 떨어진 상태로 시작되는 Issue이다. 
  
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


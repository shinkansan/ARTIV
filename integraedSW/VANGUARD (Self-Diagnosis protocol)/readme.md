#  VANGUARD

* 안전한 주행을 위한 초깃값 진단 및 주행 단계에서의 실시간 진단, 통합 프로그램 

![image](https://user-images.githubusercontent.com/59792475/85977239-2e2df780-ba17-11ea-978d-e3a861349755.png)

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
  ### 기능   
  
  우분투가 기본적으로 영어밖에 안되기에, 저또한 검색이나 깃허브 작성 등에 큰 어려움이 있었습니다.
   
  Ibus 한글판도 깔아보고, 커맨드도 고쳐보고 했지만 Ibus는 한영키를 지원하지 않아요..
  
  한글 입력에 성공하더라도 __`ㅎㅏㄴㄱㅡㄹ`__ 처럼 깨져서 입력되네? ㅋ
  
  결국, UIM 패키지와 시작 명령어를 통한 한영키 맵핑을 통해 해결할 수 있었습니다!
  
  __아래 링크에서 마지막 단계(특정 코드 터미널에 입력) 전까지만 하고 다시 여기로 돌아오세요!__
  
  __중간에 Global settings 탭, '벼루' 외에 사용안함으로 옮길 때 일일이 옮기지 마시고 CTRL + A 누르시면 편해요...__
  
  __[우분투 18.04 한영키 사용 및 한글 입력하기](https://pangtrue.tistory.com/70)__
  
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


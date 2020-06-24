# IONIQ DBW Communication Node
Authors : Hoyeong Yeo, Gwanjun Shin

## Condition
1. ROS2 Dashing Only!
2. Python3   
:warning: Execute them with `python3` command
3. 프로그램별 종속성은 프로그램 폴더안에 readme.md에 적혀있음.

## Contents
 1. ./canDB (deprecated) 사용하지 말기, ros1 버전임.
 
 2. [./dbw_ioniq](./dbw_ioniq) 차량 탑재용 버전   
    > __기본 프로그램__   
    1. dbw_ioniq_node : 차량 정보 수신 노드   
    2. dbw_cmd_node : 차량 정보 송신 노드   
    > __유틸리티__   
    3. KeyboardControl   
    4. JoystickControl
    
 ![img](pics.png)
 
 5. TODO
    1. 통신 에러 핸들링 및 ros fatal 출력
    2. transmit buffer 에러 발생 해결
    
 3. [./artiv_can](./artiv_can) Kvaser 전용 프로그램으로부터 독립.    
    1. 기존 linuxcan에서의 연결 오류를 socketcan으로 대체하면서 해결.    
    2. 현재 ROS1-melodic 버전이 개발되었고 추후 ROS2-dashing 버전도 개발 예정.    
    3. 사용 방법은 해당 폴더 내에 readme.md 파일을 참고 바람.

## rosbag

ROSbag 정리 [링크](https://github.com/shinkansan/ARTIV/blob/master/rosbag/rosbag_info.md).  
ARTIV rosbag data server [link](http://gofile.me/4o0Gn/k9ZL0YGhc)

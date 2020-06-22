# Kvaser 전용 프로그램 도움 없이 CAN 정보를 받아오자!
Date : 2020.06.23    
Author : 여호영

### 이전의 문제점
이전에는 Kvaser사의 linuxcan, kvlibsdk라는 파일을 다운 받아서 설치하는 과정을 거쳐 CAN 정보를 다룰 수 있었다.    
하지만 고질적인 문제점이 하나 있다면 가끔 가다가 개인 노트북을 인식하지 못한다는 것이다.    
다음 사진과 같이 Kvaser 케이블을 연결했음에도 device가 검색되지 않는 오류가 발생한다.    
![사진](run_example.png)    

## 해결책은 Socketcan!
Kvaser사의 전용 툴이 아닌 ROS Package를 이용한 CAN 통신을 함으로써 연결 오류를 없애고자 한다.    
그 해결책으로는 ROS 공식 Package인 ros_canopen을 사용하는 것이다.     
우선 ![사이트](https://github.com/ros-industrial/ros_canopen)에서 git 명령어로 패키지를 다운받자.

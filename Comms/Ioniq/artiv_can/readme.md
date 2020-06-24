# artiv_can 사용 설명서 for ros1-melodic

artiv_can package는 can raw data의 parsing 과정을 거쳐 사람이 이해하기 쉬운 데이터로 변환해준다.    
(ex. km/h, degree 등등)    
이는 ros1-melodic을 위한 프로그램이다.    
ros1 버전으로 개발한 이유는 rosbag을 당장 사용해야할 상황이기 때문이다.
아마 can_msgs는 ROS 표준 msg 규격이 아니기에 ros bridge로 통과되지 않을 것이다.(사실 확인 필요)    
그래서 ros1에서 rosbag을 통해서 데이터를 받고 bridge로 넘겨줄 수 있도록 parsing하는 과정이 필요하다.    

## 큰 흐름
차량 -> ROS내의 socketcan_bridge 예제를 통한 CAN 정보 publish -> artiv_can 내의 예제를 통해 data parsing 및 publish    

## 1. 프로그램 실행 전 준비
프로그램을 실행하기 전에 해당 폴더에 해당하는 artiv_can을 다운받자.    
artiv_can은 ros1-melodic 기반이므로 catkin_ws/src에 다운받아야 한다.    
여기서 artiv_can은 socketcan의 정보를 parsing하는 것이므로 ros_canopen package와 같은 workspace에 존재해야 한다!    

## 2. 컴퓨터와 차량 연결
이 단계는 [이전](https://github.com/shinkansan/ARTIV/blob/master/Comms/CAN/socket_can_connect.md)에 설명했던 방법으로 따라오면 된다.    
단지 해당 사이트에서 '2. 컴퓨터와 CAN 장치 연결'에서 ```sudo ifconfig can0 up``` 까지의 명령어만 입력하도록 하자.    
그 후에 '3. CAN raw data를 ros에 publish!'하는 단계를 거치면 컴퓨터와 차량이 연결된다.    
그러면 rostopic list 중에 /received_messages라는 topic이 보일 것이고 이는 차량의 raw_data이다.    

## 3. Parsing & Publish
이 단계가 가장 중요한 단계이다. 그렇지만 매우 쉽다!    
2번 단계에서 실행한 terminal 창 말고 다른 창을 새로 켜서 source 하자.    

```
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash
```

그 후에 아래 명령어 중에 하나를 택해서 python 파일을 실행하기만 하면 된다!    
Method 1.    
```
cd ~/catkin_ws/src/artiv_can/src
python can_parser.py
```

Method 2.    
```
rosrun artiv_can can_parser
```

rostopic list 중에 /Ioniq_Info, /JointState가 있으면 완료된 것이다.    
이는 ROS 표준 msg 규격이므로 ros bridge를 통해서 ros2에서도 사용할 수 있다.    

## 4. Complete
차량으로부터 데이터 수신 및 parsing이 완료되었다.    
이제는 원하는 데이터를 subscribe해서 이용하기만 하면 된다.    
참고로 데이터의 순서와 단위를 알고 싶다면 [여기](https://docs.google.com/document/d/1Mvyvs1Tt20U99uA4o_h4c2-KB7s64NOQz6vd_-SGwh4/edit)로!    

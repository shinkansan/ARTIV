# Rosbag 버전별 정보
현재 ARTIV만의 Rosbag이 많은데 버전별로 어떤 업데이트가 진행되었을까?    
각 버전의 특징을 알고 용도에 맞게 사용하자!    
버전이 의미하는 정보는 다음과 같다.
- 맨 앞 숫자 : 차 종류 (1 : 아이오닉, 2 : ERP42)
- 두 번째 숫자 : 대규모 업데이트
- 세 번째 숫자 : 소규모 업데이트    
예시 : 1.0.0 - 아이오닉 초기버전

---

## Rosbag ver1.0.0
아이오닉의 정보를 저장한 ARTIV만의 최초의 Rosbag이다.

### FILE NAME
artiv_ioniq_0426_1.bag

### DATE
2020.04.26

### INCLUDE TOPICS
/Ioniq_Info

### MSG TYPE
/Ioniq_Info : canDB/Artivmsg

---

## Rosbag ver1.0.1

### FILE NAME
artiv_ioniq_0426_2.bag

### DATE
2020.04.26

### INCLUDE TOPICS
/Ioniq_Info    
/Joint_state

### MSG TYPE
/Ioniq_Info : canDB/Artivmsg    
/Joint_state : sensor_msgs/JointState

### UPDATE
1. Add '/Joint_state' topic

---

## Rosbag ver1.0.2

### NAME
artiv_ioniq_0428.bag

### DATE
2020.04.28

### INCLUDE TOPICS
/Ioniq_Info    
/Joint_state

### MSG TYPE
/Ioniq_Info : canDB/Artivmsg    
/Joint_state : sensor_msgs/JointState

### UPDATE
None

---

## Rosbag ver1.1.0

### NAME
artiv_ioniq_0428_revised.bag

### DATE
2020.04.28

### INCLUDE TOPICS
/Ioniq_Info    
/Joint_state

### MSG TYPE
/Ioniq_Info : candb/Artivmsg    
/Joint_state : sensor_msgs/JointState

### UPDATE
1. Change package name : 'canDB' -> 'candb'
2. Add information : 'door_fl', 'door_fr', 'safety_belt_driver', 'trunk', 'door_rl', 'door_rr'

---

## Rosbag ver1.1.1

### NAME
artiv_ioniq_0428_revised_door.bag

### DATE
2020.04.28

### INCLUDE TOPICS
/Ioniq_Info    
/Joint_state

### MSG TYPE
/Ioniq_Info : candb/Artivmsg    
/Joint_state : sensor_msgs/JointState

### UPDATE
None

---

## Rosbag ver1.2.0

### NAME
test_bag_0502.bag

### DATE
2020.05.02

### INCLUDE TOPICS
/Float_Info    
/Int_Info    
/Joint_state

### MSG TYPE
/Float_Info : std_msg/Float32MultiArray    
/Int_Info : std_msgs/Int16MultiArray     
/Joint_state : sensor_msgs/JointState

### UPDATE
1. Delete '/Ioniq_Info' topic
2. Add '/Float_Info' topic
3. Add '/Int_Info' topic
4. Change msg type : 'Artivmsg' -> 'Float32MultiArray', 'Int16MultiArray' (for ros1-ros2 bridge)

---

## Rosbag ver1.3.0

Linuxcan 도움 없이 Ioniq에서 얻은 CAN raw frame이다.
모든 id의 frame이 들어있으므로 정제가 필요한 Rosbag이다.

### NAME
raw_can_ioniq_0622.bag

### DATE
2020.06.22

### INCLUDE TOPICS
/received_messages

### MSG TYPE
/received_messages : can_msgs/Frame

### UPDATE
1. All of CAN frame
2. No parsed data

---

## Rosbag ver2.0.0

ERP42의 최초 Rosbag이다.

### NAME
erp42_raw_0512_ver.2.0.0.bag

### DATE
2020.05.12

### INCLUDE TOPICS
/ERP42_Info

### MSG TYPE
/ERP42_Info : candb/ERPmsg

### UPDATE

---

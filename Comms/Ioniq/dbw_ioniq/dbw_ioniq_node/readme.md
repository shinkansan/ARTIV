# DBW Ioniq Node
아이오닉 차량 데이터 수신 노드

* ROS2 기반

* Publishing Topic
|Topic name|Topic Type|comment|
|---|---|---|
|/Header_Info | Header |
|/Joint_state | JointState | 4-Wheel 속도
|/Ioniq_info | Float32MultiArray | Header (rostime) 정보가 없음.

* Topic Sub 방법
  * JointState    
    `Avg, FL, FR, RL, RR` 의 순서로 속도가 .velocity에 리스트 형태로 저장되어 있음.
    * km/h 단위임 (float)
  * Ioniq_info   
    24개의 사이즈인 리스트임.
    |index|data|type|
    |---|---|---|
    |0|APS ACT Feedback|integer32|
    |1|Brake ACT Feedback|integer32|
    |2|Gear Position|integer|
    |3|Steering Angle|integer|
    |4|ESTOP Switch|bool(int)|
    |5|Auto Standby Switch|bool(int)|
    |6|APM Switch|bool(int)|
    |7|ASM Switch|bool(int)|
    |8|AGM Switch|bool(int)|
    |9|Override Feedback|integer|
    |10|Turn Signal|integer|
    |11|BPS Feedback|integer8|
    |12|APS Feedback|integer8|
    |13|Driver Belt|bool(int)|
    |14|Trunk|bool(int)|
    |15|DoorFL|bool(int)|
    |16|DoorFR|bool(int)|
    |17|DoorRL|bool(int)|
    |18|DoorRR|bool(int)|
    |19|Average Speed|float|
    |20|Wheel FL|float|
    |21|Wheel FR|float|
    |22|Wheel RL|float|
    |23|Wheel RR|float|


  값의 Max 및 경험적 의미는 참
    [아이오닉 차량 ROS 통신 프로토콜 매뉴얼](https://docs.google.com/document/d/1Mvyvs1Tt20U99uA4o_h4c2-KB7s64NOQz6vd_-SGwh4/edit?usp=sharing)


## 참고사항
  * 본 노드 실행 후 차량으로 부터 24개의 값이 모두 들어와야만 node publish 진행


## Issue 및 TODO
  * CAN 연결 실패 or 연결 도중 에러 시 roslog 로 pub 안함.
  * 값이 끊겼다 다시 들어오면 노드 재실행 필요 (CAN선을 뽑았다 다시 끼우면, 노드도 재시작 필요)

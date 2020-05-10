# DBW CMD Node
아이오닉 차량 제어 송신 노드

### 종속성
  * ROS2
  * Python3
  * KvaserCan SDK [Installation Guide](/Comms/CAN/kvaserCan_installation.md)


### 주의 사항
 * 이 코드는 현재 (2020.05.11.) 다음 항목에 대한 최대값 필터가 적용되어 있습니다.   
 
  |항목이름|최대값|사유|설계상 최대값|   
  |---|---|---|---|   
  |Accel|2000|급발진 방지|3000|   
  |Brake|30000|하드웨어 로드 방지|35000|   
  |Steer|+-440|경험적 동작 범위, <br/>__Issue 등록됨__|570|   
  |Gear|0,5,6,7|기어값|0,5,6,7   
  |Angular|255||255|   



### 항상 조심하자...

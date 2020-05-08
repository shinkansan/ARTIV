## ROS Log 관련 정리
---
통합 소프트웨어팀에서는 효율적인 디버깅과 후에 규모가 커질 자율주행 소프트웨어의 오류 관리와 통합 프로그램의 Time Sensitive 오류 감지/대처 능력을 위해서
ROS에서 자체적으로 제공하는 로그기능을 사용하기 위한 방안을 마련함.

### 예상 시나리오 
  
  1. Info   
> 연산 완료 결과 및 프로그램의 동작 확인용

    차량 인식 및 전방 물체 인식 후 특정 Action으로 이동 -> log level INFO로 log발행   
    경로 계산 후 안내 시작 -> log level INFO 로 "경로 생성 완료" 발행
    
  2. Warning   
> 연산이나 구동에 문제 없는 간헐적 오류 try~except 문으로 핸들이 가능하고 프로그램 동작 혹은 성능에 영향을 미치지 않을 정도의 오류      

  Null data 혹은 0 으로 사칙연산 시도   
  list혹은 정보 조회 도중 없는 데이터, 조회 실패등,, 데이터 로딩 중에 조회 등 wait 혹은 재시도로 해결이 가능한 수준의 오류들 알림용
  
  3. Error
> Try~catch 에서 잡히지 않는 예상가능한 오류 하지만 프로그램 동작에 중대한 영향을 미치나 제어가 가능한 수준, 개발자가 try except에서 잡아도 선언 가능

  경로 계산 실패, 객체 검출 불가, 연산 최대 시간 초과, 
  
  4. FATAL
> 중대한 결함으로, 운전자 오버라이딩 전환 및 시/청각 경고음 동반, 즉시 조치가 필요한 오류   

  제어 실패 (모터 피드백 오류), 주행 관련 주요 노드의 무응답(강제 종료등), 주행 중 PC-VCU 연결 해제
  
  
  
  ### 동작 개념
  ROS 기본 기능을 이용하기 때문에, 별다른 패키지를 설치할 필요 없이 `print` 커맨드 사용하듯이 사용, 다만 결과 출력이 `/rosout` 토픽으로 발행되고
  발동 위치 (소스코드 몇번 째 줄까지 나옴), 통합 SW 팀 모니터링 프로그램이 에러를 한 화면으로 출력 및 로그 심각도에 따른 적절한 Action을 취함
  
  Action 은 다음과 같음.   
      1. 시/청각 경고 및 다이얼로그 발행   
      2. 사고 리포트 (txt 파일 출력)   
      3. FATAL 수준 발생시 자동 감속 후 운전자 강제 오버라이딩으로 전개   
    
    


![Screenshot from 2020-05-09 02-11-56](https://user-images.githubusercontent.com/25432456/81433125-0650af00-919f-11ea-975c-80431b7f19d0.png)
C++ 코드와 예시 동작 화면
![Screenshot from 2020-05-09 01-44-30](https://user-images.githubusercontent.com/25432456/81433140-0cdf2680-919f-11ea-876c-db100771d717.png)
Python 코드와 예시 동작 화면
![Screenshot from 2020-05-09 02-13-01](https://user-images.githubusercontent.com/25432456/81433156-12d50780-919f-11ea-8e42-7417078aebd5.png)
RQT 내에서 Log 정보 처리 예시

### 참고

ros1, ros2간 오류 공유는 ros1_bridge를 통해 공유는 되지만 
rqt내에서는
```
Traceback (most recent call last):
  File "/opt/ros/melodic/lib/python2.7/dist-packages/rqt_console/message_proxy_model.py", line 103, in data
    return self._source_model.data(index, role)
  File "/opt/ros/melodic/lib/python2.7/dist-packages/rqt_console/message_data_model.py", line 113, in data
    'Unknown severity type: %s' % msg.severity
AssertionError: Unknown severity type: 40
```
오류가 발생됨

이유는 ROS1과 ROS2간 오류 Level를 표기한 Enum정의가 다르기 때문

ros1의 경우
```python
    DEBUG = 1
    INFO = 2
    WARN = 4
    ERROR = 8
    FATAL = 16
    ```
ros2의 경우
```python
DEBUG = 10
ERROR = 40
FATAL = 50
INFO = 20
UNSET = 0
WARN = 30
```
코드 작성시 or 문으로 둘다 처리하도록 코딩하면 될듯

### todo 
ros1 부분 발행 예시 만들기


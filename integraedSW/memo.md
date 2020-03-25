## 아이디어 공모

* 키워드 : ROS, Real-Time,유용하게 쓰는것, UI UX, simulation 만들기 (동시다발적으로 핸들링), 데이터 가공!!!, 안전(리미트)
 
 **통합소프트웨어에 어떤 프로그램이 담기는가!**
 
 현재차량 속도, GPS 위치, 속도 Vector, 카메라 전면부 인지, HD Map의 정보 유용화, HD Map 시각화, 기어, 기름량, 연비, (차량 제어) Estop switch,
 Multimaster(통신할 때 매우 유용), log 띄우기, 주행 상태 status, 차량 속도계 + 엔코더, 최대속도제한(topic filtering), 
 autoware 및 apollo 벤치마킹,시각화 - 핸들 값, 속도, setting값과 실제 값의 차이(delay + error), 모듈 선택(perception, 주행 등), 센서의 연결 상태, 센서의 딜레이, 각 모듈의 상태 (e.g. 비전의 전처리 상태), 현재 차의 제어상태 출력 (auto or manual), cpu memory gpu 사용량 등 컴퓨터 상태, 각 센서의 power issue (optional), 빅데이터 효율적 관리(rosbag recording + flag button- error, 고라니, 등등 주요 이벤트), 차량 내부의 소리와 영상 녹화 기능, program의 frame 체크(ros timestamp 처리), sensor fusion (optional?!)  
 
 ### 큰 틀
 
 센서의 값을 보는 창, 차량의 상태 보여주는 창, 디버깅용 ...

# 비전팀 논문 리뷰 및 구현 아카이브
> 지금은 논문의 핵심부분과 구현부분을 매칭과 구현 스킬을 익히는데 집중

1인당 4논문 2구현 1개선 / 1주

7일
1-2일. 논문 2개 -> 택 1 구현본 찾아놓고 실행 (2개 중 하나)   
3-4일. 논문 2개 -> 택 1 구현본 찾아놓고 실행 (3개 중 하나)   
5일. 각 논문 성능 평가 및 Implementation 용이도 평가 후 택 2 - 논문 관련 사항 및 매뉴얼, 리뷰 작성 후 기트허브 업로드   
6일-7일 구조 개선 작업 (구조와 방식을 나열하고 변경 혹은 Conv 계산량 축소 등 다양한 방법) 기록 후 기트허브 업로드   
발표 자료는 기트허브로 대체   

## 각 논문 성능 평가 및 Implementation 용이도
속도, 정확도
Implementation시 언어 (Pyhton, CPP) Native로 지원되는거 말고, 다른 사람들이 구현해놓은 것도 포함
학습이 편리한지, Train과 각종 Util의 공개 여부
프레임워크별 점수
  1. Keras, Torch - (각종 프레임웤과 전환 용이, 각종 유틸 존재) 5

  2. TF - 정보량, 지원 유틸이 기본적으로 후함

  3. ONNX 쓰는 놈이 이상함, 하지만 다른 프레임웤으로 변환 가능

  4. Darknet 친절하지 않지만 네이버, 국문 설명등 존재함, 다른 프레임워크들이랑 안친함

  5. Caffe - 버려

위로 갈수록 좋은 걸로

폴더에는 각 Fork한 코드 및 돌리기 위해 작성한 유틸, 및 코드 수정한 부분이 있으면 작성
성능평가 Markdown 파일

### 5월 계획
ㅇ 원내 주간 / 야간 주행영상 수집 필요

ㅇ 2020/05/08(금)~ 05/12(화): 카메라 사용을 위한 코드 및 이미지 ROS publisher 작성

ㅇ 2020/05/13(수)~ 05/17(일): 객체 인식, 차선 인식 네트워크 실행 및 성능분석 (fps, GPU 사용량, 소비전력, 사용하는 메모리 기록) 

ㅇ 2020/05/18(월): 객체 인식, 차선 인식 각각의 baseline 정하기

ㅇ 2020/05/19(화): 원내 주행영상 중 인식해야 할 객체 선정 

ㅇ 2020/05/20(수) ~ 05/27(수): 인식한 정보에 대한 ros publish할 message type 결정 및 publisher 작성 

ㅇ 2020/05/28(화) ~ 05/31(일) : ROS darknet build 하는 법 알아보기

ㅇ Baseline 정한 후 ~ : Dataset 형식 및 labeling 방법 조사

### 오늘의 할 일. 
#### 5/21(목)
0. ~~Simple Screen Recoder ppt랑 호환되는 포멧 찾기  > container mp4, audio codec AAC  
0. ~~원내주행영상 정리   
0. ~~Key Points Estimation and Point Instance Segmentation Approach for Lane Detection 실행 영상 기록   
0. ~~차선 인식 하나 더 돌려보기~~  > 다른 버전의 CUDA 이용할 수 있는지 확인   
0. Key Points Estimation and Point Instance Segmentation Approach for Lane Detection 메모리 사용량 줄이고, 성능 평가 
0. yolo 메모리 변화에 따른 fps 변화 확인  
0. 베이스라인 정하기

#### 5/22(금)
0. ~~원내주행영상에서 인식해야할 객체 선정~~   

  > 교내 객체:   
  
     - 차   
     - 사람   
     - 킥보드   
     - 세그웨이   
     - 자전거   
     - 야생동물(?)   
     
  > 표지판 종류:   
  
     - 로터리 표지판   
     - 양보 표지판   
     - 횡단보도 표지판   
     - 주차금지 표지판   
     - 과속방지턱 표지판   
     - 좌회전 금지 표지판   
     - 30 제한 속도 표지판   
     
  > 기타:   
  
     - 노면표시   
     - 정지선   
0. ~~다른 버전의 CUDA 사용 가능한지 확인, 사용법 정리~~ > Vision/이구/switch-cuda
0. ~~노트북에 CUDA 9.0 설치~~ > cudnn 설치해야함
0. 머신러닝용 pc에 CUDA 9.0, cudnn 설치 (설치파일 노트북에 있음)
0. PolyLaneNet 실행
0. Key Points Estimation and Point Instance Segmentation Approach for Lane Detection 메모리 사용량 줄이고, 성능 평가   
0. ~~yolo 메모리 변화에 따른 fps 변화 확인~~
0. 베이스라인 정하기

#### 5/23(토)

### 6월 계획(미정)
ㅇ FCN을 이용한 steering 결정   
ㅇ stereo camera -> depth map을 이용한 객체 인식 및 물체 회피기능 

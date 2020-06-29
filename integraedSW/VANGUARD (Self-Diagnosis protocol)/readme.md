# VANGUARD

<p align="center"><img src="https://user-images.githubusercontent.com/59792475/85998620-01dd9f80-ba46-11ea-966c-e1af38672d25.png"></p>

<p align="center">Author : Juho Song</p>
<p align="center">date : 2020.06.29.</p>

## Environment & Dependencies

  * Developed with ROS2, Python3

  * Get Info : [dbw_ioniq_node](https://github.com/shinkansan/ARTIV/tree/master/Comms/Ioniq/dbw_ioniq/dbw_ioniq_node), /Joint_state (topic) <br>
  ![dbw_ioniq_rosbag_rqt](https://user-images.githubusercontent.com/59792475/81559090-ca4d6200-93c9-11ea-8c90-9aa113fa7ce5.png) <br>
  * Vehicle Control : [dbw_cmd_node](https://github.com/shinkansan/ARTIV/tree/master/Comms/Ioniq/dbw_ioniq/dbw_cmd_node)

## Motivation & Background
  
#### Starts from Fatal Break Issue    
  
<br>
  
개발 과정 중 아래와 같은 **치명적인 브레이크 초깃값 설정 ISSUE**를 발견하여 **자가진단 프로토콜의 필요성**을 느꼈다. 

##
##### ISSUE
  
`차량 시동을 걸기위해서는 운전자가 브레이크를 누르고 시동을 걸어야 한다.`
  
`이때, 동시에 자율주행 모드를 키면, 차량 제어에 사용되는 브레이크 액츄에이터가 브레이크 패널과 떨어진 상태로 시작된다.` 
  
`즉, 자율주행 모드를 시작하는 순간에 브레이크가 외부요인에 의해 눌려있었다면, 브레이크 제어가 제대로 되지 않는다.`
  
##
#### Discussion for Solution 

- [x] `기본적으로` __주행 매뉴얼__`을 제작하고, 새로운 Issue가 생길 때마다 추가하여 주의하도록 하는 방법.`

- [ ] ~~__하드웨어적인 접근__`으로 브레이크 액츄에이터를 포함한 차량 외적인 장치들을 관리하는 방법.`~~

- [x] `브레이크를 포함한 주요한` **차량 정보 토픽들의 발행상태를 주행 전에 진단**`하여 모든 진단이 끝나고 문제가 없을 때 주행을 시작하는 방법.`

<br>
  
논의 결과, 언맨사에서 제작한 장치들을 직접 관리하는 것은 불가능하고, 주행 매뉴얼 배포와 SW적인 접근으로 자가진단을 하는 방법이 채택되었다.
  
초기값 진단 프로그램을 Base로 **초기값 진단 및 Sensor State 및 차량 정보 Topic 발행에 대한 진단을 하는 프로그램, VANGUARD**를 구상하였다. 
  
## Intended Structure

* __개발 시작 단계에서 작성한 VANGUARD의 구조도 (version 1.)__

![vanguard v1](https://user-images.githubusercontent.com/59792475/86013499-2d6a8500-ba5a-11ea-9c2e-06cdae431fd8.png)

처음에는 dbw_cmd_node와 dbw_ioniq_node에서 publish되는 양방향의 topic들을 통합 SW에서 개발중인

매개노드(Mediating Node)를 사용하여 일괄 publish하려고 하였다.

<br>

이 방법의 장점은, 매개노드에 있는 기능을 그대로 사용하기에 구현 방법이 훨씬 간단해지고, 명확해진다는 점이다. 

하지만, 매개노드를 VANGUARD에 도입하면 의도한 자가진단 프로토콜의 정체성에 부합하지 않기에 **version 2**를 구상하였다.

##

* __매개노드를 제거한 VANGUARD의 구조도 (version 2.)__

![vanguard v2](https://user-images.githubusercontent.com/59792475/86013595-496e2680-ba5a-11ea-9659-7adb48d7a2ce.png)

VANGUARD는 실시간 감시를 한다. 즉, 다른 프로세스가 오류나 접촉불량 등으로 꺼지더라도 VANGUARD는 항상 살아있어야한다. 

그렇기에, __최종적으로 VANGUARD는 매개노드보다 전위에 위치할 필요성이 있고, 최우선에 위치한 독립적인 프로그램으로 설계했다.__
  
## Development Process

* __VANGUARD의 개발은 크게 아래의 3가지 영역으로 나뉜다. 상세 내용은 링크를 통해 각 repository를 참고하자.__

##
 __1. Initializing Diagnosis__
 
 Test Case : 초깃값 진단의 기준이 될 신뢰성 높은 차량 정보 Dataset을 확보한다.
 
 __[Test Case](https://github.com/shinkansan/ARTIV/tree/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/TestCase)__
 
 Initializing Diagnosis : Test Case를 기반으로 자율주행을 시작하기 전 1차 진단
 
 __[Initializing Diagnosis](https://github.com/shinkansan/ARTIV/tree/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/Initializing%20Diagnosis)__
 
##

 __2. Real-Time Diagnosis__
 
Real-Time Diagnosis : 1차 진단을 통과하고, 자율주행에 돌입했을 때 실시간으로 차량의 모든 주요 상태 진단

__[Real-Time Diagnosis](https://github.com/shinkansan/ARTIV/tree/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/Real-Time%20Diagnosis)__

##

 __3. Sensor State Diagnosis__
 
Sensor State Diagnosis : 1과 2에서 vehicle info와 함께, sensor state에 대한 진단도 필요하다. 
 
기존에 존재하는 ros_diagnotics 패키지를 참고하여 Vision팀의 Sensor state를 시작으로 모든 sensor의 state를 점검한다. (이구 담당)

 __[Sensor State Diagnosis](https://github.com/shinkansan/ARTIV/tree/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/Sensor%20State%20Diagnosis)__

##

### Note (abt. Python3 Concurrency Programming)
  
  TestCase 확보 과정부터 시작해, cmd node를 통한 차량제어와 동시에 ioniq node를 통한 정보를 실시간으로 받기 위해서는 동시성 프로그램이 필수적이다.
  
  현재까지 개발 과정에서는 thread를 사용하였는데, multiprocessing 모듈의 process로도 변경하여 동시성 프로그래밍을 할 수 있다.
  
  아래 링크에서는 VANGUARD 개발 과정에서 사용된 동시성 프로그래밍을 다루었다.
  
  __[Concurrency Programming (Thread VS Multiprocessing)](https://github.com/shinkansan/ARTIV/tree/master/integraedSW/VANGUARD%20(Self-Diagnosis%20protocol)/Concurrency%20Programming%20(Thread%20VS%20Multiprocessing))__
 

> 앞으로 추가해야 할 사항   
> **1. 현재 Play->Stop->다시 Play를 누를 경우 에러 발생, 수정해야 함**   
> 2. clear 버튼 추가하여 원할 경우에만 리스트 클리어 수행   
> 3. 특정 상태 메세지('No topic is playing' 등)는 계속 띄울 경우 current row에 계속 쓰여지도록   
> 4. ROS1 토픽도 띄우는거?   
> 5. ARTIV 로고 추가~   
> 6. 이쁜 디자인~   


# 차량과 컴퓨터를 연결해보자! part1
여호영 / 2020.03.04

## Hardware
#### 차량 내 케이블
CAN 통신을 이용해서 차량에서 컴퓨터로 데이터를 가져오기 위해선 어떤 디바이스와 케이블이 필요한지 알아보았다.    
우리가 받은 베뉴 차량에 OBD2 케이블이 있는 것을 확인했다. 총 OBD2 케이블은 총 두 개로 하나는 FUSE 박스에 있고, 하나는 선으로 연결돼서 밖으로 나와있다.    
아마 따로 선으로 하나 나와있는 것은 현대 측에서 연구하기 편하라고 만들어준 것이지 않았을까 싶다.
그러면 OBD2 케이블을 USB로 연결할 방법을 찾아야겠지?

#### National Instrument (YOUTUBE)
차량과 컴퓨터를 연결하는 케이블을 구할때 National Instrument korea사의 도움을 많이 받았다. ~~National Geographic이 아닌^^~~    
CAN 통신과 관련된 hardware, software(data 수신, simulation 등)를 이해하기 위해서 도움이 될 것이다.    
(참고 : [NI YOUTUBE](https://www.youtube.com/watch?v=B4iKB7Tx6b4&list=PLFEQP5FItT4NTB1eiAKeYteb6DPJC43fQ, "youtube link"))
특히 하드웨어 팀은 꼭 보도록...    
하여튼 알아본 결과 OBD2-9Pin(CAN) 케이블과 9Pin-9Pin(CAN) 케이블 그리고 마지막으로 CAN 컨트롤러(USB 포트가 있음)가 필요하다.    
그림으로 그리면 다음과 같다.    
![사진](./media/diagram0.jpg)


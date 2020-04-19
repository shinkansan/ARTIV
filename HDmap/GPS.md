GPS를 연결해봅시다.
================
작성자 : 류준상
-------------
데스크탑에서 어느정도 마무리하고, 실제 차량에서 테스트예정!
어차피 랩탑에다가 다시 설치해야돼서, 정리할 겸 깃헙에 끄적여봅니다..

테스트 모델 : 씨너렉스 MRP-2000

ROS-melodic 기준

# ROS Package Install

## [nmea_navsat_driver][nmealink]

[nmealink]: http://wiki.ros.org/nmea_navsat_driver

NMEA는 시간, 위치, 방위 등의 정보를 전달하는 규격 중 하나이다.
우리가 사용하는 MRP-2000은 NMEA를 출력하기 때문에 위 패키지를 이용한다.

### How to install

    $ sudo apt-get install ros-melodic-nmea-navsat-driver
  
### How to run

    $ rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyUSB0 _baud:=115200
    #MRP-2000이 지원하는 bandrate가 115200임.
    #당연히 다른 터미널에서 roscore부터 해야겠죠?
    
### 아마 에러가 날 것이다.

    [FATAL] [1587321012.247533]: Could not open serial port: I/O error(13): could not open port /dev/ttyUSB0: [Errno 13] Permission denied: '/dev/ttyUSB0'

이딴 에러가 뜬다.

    $ sudo chmod 666 /dev/ttyUSB0

이걸 입력 후 다시 rosrun해보자.

근데 사실 나는




실행시키고 나면 몇가지의 토픽들이 있는데, 자세한건 위키에서 살펴보시고 우리가 사용할건 /fix 임.

### 한 번 볼까?

다른 터미널에서 아래의 구문 실행

    $ rostopic echo /fix
    
살펴보면 latitude, longitude, altitude가 보이는데 당연히 요걸로 위치를 파악할 수 있다.
3개는 전부 float64 타입이다.

근데 저 숫자들을 보고 우리가 어디에 있는지 상상할 수 있는가?
개인적으로 불-편해서 점 찍어주는 방법을 찾아봤다.

그 해답은

## [mapviz][mapvizlink]

[mapvizlink]: http://wiki.ros.org/mapviz/Plugins

Mapviz는 ROS 기반의 visualization tool이다.

### How to install

    $ sudo apt-get install ros-melodic-mapviz ros-melodic-mapviz-plugins ros-melodic-tile-map ros-melodic-multires-image
    
빌딩해야되는지 테스트 후,,추가 예정

### How to run

    $ roslaunch mapviz mapviz.launch



참고자료
https://wiki.ros.org/nmea_navsat_driver
https://autoware.readthedocs.io/en/feature-documentation_rtd/DevelopersGuide/PackagesAPI/sensing/scripts.html
http://wiki.ros.org/mapviz/Plugins
https://github.com/swri-robotics/mapviz/blob/master/README.md


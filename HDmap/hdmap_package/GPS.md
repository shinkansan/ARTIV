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
    #MRP-2000이 지원하는 baudrate가 115200임.
    #당연히 다른 터미널에서 roscore부터 해야겠죠?
    
### 아마 에러가 날 것이다.

    [FATAL] [1587321012.247533]: Could not open serial port: I/O error(13): could not open port /dev/ttyUSB0: [Errno 13] Permission denied: '/dev/ttyUSB0'

이딴 에러가 뜬다.

    $ sudo chmod 666 /dev/ttyUSB0

이걸 입력 후 다시 rosrun해보자.

근데 사실 나는

    $ sudo usermod -a -G dialout $USER
    
이걸로 해결했다.

실행시키고 나서 rostopic list를 보면, 몇 가지가 있다. 자세한건 위키에서 살펴보시고 우리가 사용할건 /fix임.

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
    
### How to run

    $ roslaunch mapviz mapviz.launch

창이 하나 떴을 것이다.

하단의 Add를 눌러서, tile_map을 추가하자.
말 그대로, tile map을 띄워주는 것인데 기본값은 Stamen (terrain)이다. 근데 이게 한국에서만 그런지 몰라도, 일정 수준 이상으로 확대하면 네트워크 에러를 뿜으며 작동하지 않는다. 나중에 구글 위성지도로 교체할 것이다.
일단 테스트만 해보자.

또 Add를 눌러서, navsat를 불러오자.
Topic 옆에 Select를 눌러서 /fix를 추가한다.

Draw Style을 points로 바꾸고, 지도를 열심히 옮겨 대한민국을 찾고 대구를 찾아 현풍으로 확대해보자.
아까도 말했듯이 일정수준 이상으로 확대를 못한다... 대충 된다는 것만 보자.
점이 영롱하게 현풍에 찍힌다!

### 구글 위성지도로 교체(optional)

Mapviz에서는 WMTS를 이용하는데, 더 좋은 지도가 있으면 그걸 쓸거다.
일단 지금으로써는 구글 위성지도만 작동을 확인해서 이걸로 했다.

#### STEP 1

    $ mkdir ~/mapproxy
    $ sudo docker run -p 8080:8080 -d -t -v ~/mapproxy:/mapproxy danielsnider/mapproxy
    
아, 근데 Docker가 설치되어 있어야한다.
없으면 설치하고 오자. 나는 [이거][thislink]보고 깔았다.

[thislink]: https://blog.cosmosfarm.com/archives/248/%EC%9A%B0%EB%B6%84%ED%88%AC-18-04-%EB%8F%84%EC%BB%A4-docker-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95/

#### STEP 2

Mapviz를 열고, tile_map의 Sources에서 Custom WMTS Source...를 누르자.
Base URL에 아래의 구문을 입력 후, Max Zoom은 19로 설정한 뒤 Save한다.

    http://localhost:8080/wmts/gm_layer/gm_grid/{level}/{x}/{y}.png

쨘! 그럼 구글 위성지도가 뜨고 확대도 아주 잘 된다~


#### 참고자료

https://wiki.ros.org/nmea_navsat_driver

https://autoware.readthedocs.io/en/feature-documentation_rtd/DevelopersGuide/PackagesAPI/sensing/scripts.html

https://www.youtube.com/watch?v=zTrzr5BhH-8

https://blog.naver.com/chandong83/220780876639

http://wiki.ros.org/mapviz/Plugins

https://github.com/swri-robotics/mapviz/blob/master/README.md

https://github.com/solosito/MapViz-Tile-Map-Google-Maps-Satellite

https://blog.cosmosfarm.com/archives/248/%EC%9A%B0%EB%B6%84%ED%88%AC-18-04-%EB%8F%84%EC%BB%A4-docker-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95/



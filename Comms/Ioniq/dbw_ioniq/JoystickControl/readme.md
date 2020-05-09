# JoystickControl
Author : Gwanjun Shin

***
스팀 컨트롤러 기반 조이스틱 차량 제어 알고리즘


### 사용법

![control](https://www.gamingonlinux.com/uploads/articles/tagline_images/1873805354id13040gol.png)


차량 동작을 위해서는 __LT RT 버튼을 딸칵 소리가 날 때 까지 꾹 누르면서 제어해야함.__

둘 중 하나라도 조건에 부합하지 않으면 Brake ACT 14000 으로 긴급 정지 발동


차량 스티어링, 브레이크, 악셀 모두 L Stick 하나로 조정


### 종속성

1. steamcontroller [설치 방법](./steamcontroller/artiv_install.md)

2. sox 라이브러리, 경고음 플레이용 `sudo apt-get install sox`

2. kvaser linux can 드라이버 및 sdk

2. python3, ros2 기반

## ARTIV Steam Controller Setting
차량 제어용 스팀 컨트롤러 드라이버 설치 방법
***

### Steam Controller 파이썬 라이브러리 설치
원본 리포짓토리 "https://github.com/ynsta/steamcontroller"

이미 이 파일을 올려놓았다.

디렉토리 안에서
  1. `sudo python3 setup.py install`
  2. `sudo python setup.py install`

  설치 후 테스트 해봐서 안되면 sudo를 빼고도 해보자
  리눅스는 sudo가 붙으면 python 경로가 달라진다.

  /usr/local/python에서 /lib/local/python 등으로 달라지긴 한다.

### 권한 설정
스팀 컨트롤러를 일반적인 파이썬 프로그램이 접근할려면 아래 내용을
` /etc/udev/rules.d/99-steam-controller.rules` 에 기입해야한다.

```
SUBSYSTEM=="usb", ATTRS{idVendor}=="28de", GROUP="plugdev", MODE="0660"

# Steam controller gamepad mode
KERNEL=="uinput", MODE="0660", GROUP="plugdev", OPTIONS+="static_node=uinput"

```

* 여기서 Group에 plugdev는 플러그 장치를 관리하는 우분투 시스템 그룹 이름이다.
* 위 내용은 usb 기본 권한을 plugdev 부여한다는 의미임.
* 그 후에 plugdev 그룹에 로그인 사용자를 넣어놓으면 스팀 컨트롤러를 별다른 권한 상승 없이 사용할 수 있다.

`sudo nano` 로 기입 후 `sudo udevadm control --reload` 을 통해 동작

`sudo usermod -G plugdev {사용자계정명}`를 통해 plugdev 그룹에 동작중인 계정을 추가하면 plugdev에 적용된 스팀 컨트롤러를 `sudo` 명령없이 사용할 수 있다.

재부팅.

이러면 artiv joystickControl.py 프로그램을 동작할 수 있다.

# KvaserCAN 라이브러리 설치 

설치 파일 모음 (artiv 자료서버) http://gofile.me/4o0Gn/pth9Xxdkt   
공식 사이트 kavser -> download 가도 있음.
  
  1. Kvaser CANlib SDK -> exe 파일이어서 깔 필요 없음
  2. Kvaser Linux Driver SDK
  3. Python Module.  
    ** 안에 있는 .whl 파일을 pip3 install <.whl 파일> 로 설치해야됨 **
  4. Linux SDK Library
  5. Kvaser SocketCan Device Driver -> Kvaser Linux Driver SDK와 충돌하므로 설치할 필요 없음.  
  
  따라서 설치해야 할 것은 2번, 3번, 4번 입니다.

위 3개를 다운받고 설치
> 안에 있는 readme.md 나 주로 `make` 치고 `sudo make install` 치면 다 설치됨.   
> :warning: install kvlibsdk at last



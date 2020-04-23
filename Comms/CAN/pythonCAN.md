# Python으로 can 받아오기


Kvaser의 CAN Python lib을 이용하여 개발할 것이다.
Kvaser Download page [canlib](https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130981911&utm_status=latest)
`pip install *.whl` 의 명령어를 이용하여 설치하면 된다.

이 것 뿐만 아니라 각각의 드라이버도 설치해줘야한다.

Windows
On Windows, first install the canlib32.dll by downloading and installing __“Kvaser Drivers for Windows”__ which can be found on the Kvaser Download page (kvaser_drivers_setup.exe) This will also install kvrlib.dll, irisdll.dll, irisflash.dll and libxml2.dll used by kvrlib.

The “__Kvaser CANlib SDK__” also needs to be downloaded from the same place (canlib.exe) and installed if more than just CANlib will be used. This will install the rest of the supported library dll’s.

The two packages, “Kvaser Drivers for Windows” and “Kvaser CANlib SDK”, contains both 32 and 64 bit versions of the included dll’s.

Linux
On Linux, first install the libcanlib.so by downloading and installing “Kvaser LINUX Driver and SDK” which can be found on the Kvaser Download page (linuxcan.tar.gz).

If more than just CANlib will be used, the rest of the supported libraries will be available by downloading and installing “Linux SDK library” (kvlibsdk.tar.gz).


하여튼 드라이버와 Lib이 필요하다, 운영체재에 맞추어 다운받아보자.

다음에는 python lib zip 폴더 docs에 있는 index.html로 우선 기본기를 닦아보자.

#### 나중에 Python과 C++의 전송 딜레이가 클 경우에는 C++로 넘어가자,  우선은 조작하기 쉬운 파이썬을 이용하여 데이터와 처리에 대해 익혀둘 필요가 있다.

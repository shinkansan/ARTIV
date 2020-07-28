UBUNTU에 연결되어 있는 device에 이름 부여하기
==========================================

#### 작성자 : 류준상


PC에 USB 혹은 다른 포트들을 꽂을 때마다 어떻게 인식될지 몰라 짜증나셨죠?

그럼 이 글을 보고 특별한 이름을 부여해주세요!
#
### 무슨 소린지 요약해봅시다

저는 GPS와 IMU를 다루고 있는데요, 둘다 USB로 연결하는데 어쩔땐 GPS가 ttyUSB0, 어쩔땐 IMU가 ttyUSB0여서 포트번호 맞추기가 너무 어려웠습니다.

만약 GPS를 연결하면 무조건 'artivGPS'로 인식하고, IMU를 연결하면 무조건 'artivIMU'로 인식한다면 너무나도 편하겠죠?
#
### 그럼 이제 따라해봅시다

기본적으로 udev에 rules.d를 추가함으로써 위에서 말한 프로세스를 실행할 수 있는데요, 귀찮으니까 자동화화는 sh파일을 만들어봅시다.

**STEP 1. device_setting.sh 파일을 다운로드하세요.**
#
**STEP 2. 원하는 device를 컴퓨터와 연결하세요.**
#
**STEP 3. device의 고유값들을 찾아봅시다.**

우리가 필요한 정보는 ```SUBSYSTEM```, ```idVendor```, ```idProducts```, ```serial``` 입니다.

우리의 친구 terminal을 켜고, ```udevadm info -a -n /dev/<device>```를 입력해봅시다.

이때 ```<device>```는 현재 컴퓨터에서 인식하고 있는 기기 번호입니다. 만약 USB라면 ```ttyUSB0```, ```ttyUSB1```, etc. 이겠죠?

만약 모르겠으면 ```<device>```에 ```ttyUSB*```등을 입력해서 만족하는 조건을 모두다 찾을 수도 있어요.

```ls /dev```를 통해서 연결되어 있는 기기 목록들을 대충 볼 수도 있답니다 ^_^~

우리가 봐야할 정보는 뭐냐! 당연히 바로 위에서 말한 ```SUBSYSTEM```, ```idVendor```, ```idProducts```, ```serial```입니다.

같은게 너무 많이 떠서 힘들면 ```idVendor```, ```idProducts```, ```serial```이 있는 구간을 찾아서 거기에 있는 ```SUBSYSTEM```을 입력하면 됩니다 ㅎㅎ

* 위에서 말한 idVendor, idProducts, serial이 ```udevadm info -a -n /dev/<device>``` 를 입력해도 보이지 않는 경우, ```udevadm info --query=all --attribute-walk --name=/dev/video0 | grep -E "idVendor|serial|idProduct"``` 를 입력하면 볼 수 있다.
#
**STEP 4. device_setting.sh 파일을 여세요.**

```sudo echo``` 해놓고 뒤에 주저리주저리 적어놓은 문장이 있죠? 그걸 복사해서 아래에 붙여넣읍시다.

대충 느낌이 오시죠? 위에서 찾은 ```SUBSYSTEM```, ```idVendor```, ```idProducts```, ```serial```을 알맞게 입력하고, ```SYMLINK```에는 만들고 싶은 이름을 지정하시면 됩니다.

*제가 제안하는 컨벤션은 ```artivDEVICE_NAME```입니다. 지키기 싫으면 안지켜셔도 되는데, 그냥 모두 비슷하면 보기에 좋을거 같지 않나요?*

```MODE```는 권한을 부여하고 싶으시면 입력하시면 됩니다. 필요없다면 과감히 삭제!

> 이후에 써있는 것은 파일 이름입니다. 원래 규칙이 있는거 같은데...저도 잘 모르겠어요... ```적당한 숫자-SUBSYSTEMS-적당한 이름.rules```로 해볼까요?

다 했으면 저장^_^
#
**STEP 5. sh 파일을 실행합시다.**

터미널을 열고 위에서 만든 sh파일이 있는 곳을 찾아간 뒤에, 아래의 코드를 입력해봅시다!

```sudo sh device_setting.sh```
#
**STEP 6. 재부팅을 합시다.**
#
만약 진짜 rules파일이 잘 적용됐는지 보고 싶으시다면 ```/etc/udev/rules.d```에서 확인해보세요 :)

그럼 20000.
#
참고
<https://m.blog.naver.com/rlackd93/221312677996>

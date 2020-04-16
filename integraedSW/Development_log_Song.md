## ROS catkin package를 QT Creator로 생성하고 작성하기

* 작성일 : 2020/04/13
* 작성자 

##

github를 자주 검색하면서 느낀 점은, 대부분의 ROS 개발은 catkin으로 빌드한 package 형태로 이루어진다는 것이다.

하지만, 막상 QT Creator에는 ROS package의 형태로 프로젝트를 시작하는 기능이 없었다.

검색을 통해 찾아보니, QT Creator에 ROS Plugin을 도입한 사이트를 찾을 수 있었다.

__[ROS QT Creator Plug-in](https://ros-qtc-plugin.readthedocs.io/en/latest/_source/How-to-Install-Users.html)__

위의 링크에서 18.04 버전을 다운받았다. 다운로드 후에 막상 패키지를 만들고 실행해봐도 패키지 빌드가 제대로 되지 않았는데 사소한 실수가 있었다.

어플리케이션에 권한이 없었다. 아래 사진처럼 경로를 찾아 우클릭 후 properties에서 파일 executing 권한을 체크해서 해결할 수 있었다.

![image](https://user-images.githubusercontent.com/59792475/79322377-b7b94780-7f47-11ea-8551-d3964025fbaa.png)

![image](https://user-images.githubusercontent.com/59792475/79322478-d8819d00-7f47-11ea-94be-94896f1ac5ca.png)

##

QT Creator 실행을 해보면 기존의 QT Creator에는 없던 ROS WORKOUT이 생겼다. 

![image](https://user-images.githubusercontent.com/59792475/79330077-d9203080-7f53-11ea-9d58-a4f7ed5d41e2.png)



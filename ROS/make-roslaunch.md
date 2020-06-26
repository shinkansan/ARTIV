# Making ROSlaunch file
ROSlauch makes your execution speed faster!
## What is ROSlaunch file?
 launch 파일은 원하는 메커니즘을 일일이 하나씩 셀에 타이핑해서 실행시킬 필요 없이
launch 파일 원클릭으로 알아서 다 실행해준다.  
즉, launch 파일은 원클릭으로 원하는 일련의 과정을 수행하게하여 실행시간을 단축시켜준다.  
마찬가지 맥락으로 ROSlaunch 파일은 여러개의 노드를 동시에 실행시키며, 각 노드에 해당되는 파라미터 값도 동시에 적용시킬 수 있는 등, 원하는 ROS 기반
작업 실행을 한문장으로 수행하게 해준다.  
그러니까 roscore 실행하고 ros1-ros2 bridge 실행하고 등등 셀을 여럿 띄워 일일이 입력하는 추줍은 짓은 그만하고
이제부터 ROSlaunch 파일을 사용하여 스마트하게 작업하자.  
(일일이 터미널에 치고 있는 사람 옆에서 이걸 쓰면 간지나는 모습을 보여줄 수 있다.)  

## How to make ROSlaunch file?  
그렇다면 ROSlaunch file은 어떻게 만들 수 있을까?  
우선 roslaunch 기능을 수행하기 위해선 패키지 안에 launch 파일이 포함되어 있어야 한다. 해당 패키지 내에 `/launch` 디렉토리를 만들고 그곳에 launch파일을 생성하자.
launch파일은 XML 포맷으로 작성하며, 내부엔 어떤 노드를 어떻게 실행시켜야 하는지에 대한 정보가 포함되어 있다.

우선 `<launch>`, `</launch>` 태그를 작성하여 launch 파일의 시작과 끝을 표시하자.(XML 포맷은 `<*>`, `</*>`으로 `*`의 시작과 끝을 알린다)  
launch 파일의 내부를 아래 나열된 태그 중 필요한 것으로 채워 넣으면 된다.

### 1. __`<node>`__  
 ###### More details at [wiki.ros.org/roslaunch/XML/node](wiki.ros.org/roslaunch/XML/node)  
 특정 노드를 bring up하거나 take down할 때 사용하는 태그다. 노드의 실행 순서는 __랜덤이다.__  
 해당 태그에선 아래의 attributes 및 elements를 사용한다.
 * Attributes  
 > - `pkg="mypackage"`  
 >   node의 package를 지정  
 > - `type="nodetype"`  
 >   node 실행 파일 이름을 기입한다  
 > - `name="nodename"`  
 >   node 이름을 지정. 노드 내부에서 설정한 이름보다 우선순위가 높다.  
 > - `args="arg1 arg2 ..."` _(optional)_  
 >   node에 argument를 전달한다.  
 > - `machine="mahine-name"` _(optional)_  
 >   지정한 기기에서 노드를 실행한다.  
 > - `respawn="true"` _(optional)_  
 >   true : 노드가 종료될 때 자동으로 재시작  
 > - `respawn_delay="seconds"` _(optional)_  
 >   노드에 failure가 발견되는 경우 재시작 전까지 지정된 시간 동안 대기  
 > - `output="log|screen"` _(optional)_  
 >   값이 screen일 때 노드의 stdout/stderr를 화면에 출력. log인 경우 stderr를 화면에 출력하고 로그 파일을 $ROS_HOME/log 경로에 생성한다.  
 > 그 외 attributes는 위의 위키 문서 참조
  
 * Elements  
 > - `<env>`  
 >   node의 environment variable을 세팅한다.  
 > - `<remap>`  
 >   node의 remapping argument를 세팅한다.  
 > - `<rosparam>`  
 >   node의 ~/local namespace에 rosparam 파일을 로드한다.  
 > - `<param>`  
 >   node의 ~/local namespace에 parameter을 세팅한다.  
 
 __Examples__
 ```
 <node name="listener1" pkg="rospy_tutorials" type="listener.py" args="--test" respawn="true" />
 ``` 
 ```
 <node pkg="nodelet" type="nodelet" name="$(arg manager)_driver" args="load velodyne_drvier/DriverNodelet $(arg manager)" >
   <param name="device_ip" value="$(arg device_ip)" />
   <param name="frame_id" value="$(arg frame_id)"/>
   ...
   
 </node>
 ```
 
### 2. __`<machine>`__  
 ###### More details at [wiki.ros.org/roslaunch/XML/machine](wiki.ros.org/roslaunch/XML/machine)  
 Ros node를 실행시킬 machine을 지정하는 태그다. _모든 노드를 local하게 실행할 경우 이 태그를 사용할 필요없다._  
 이 태그를 사용할 경우, machine 태그로 기기를 먼저 지정해준 다음 node 태그를 작성하여 원하는 기기에서 node를 실행한다.
 해당 태그에선 다음의 attributes 및 element를 사용한다.
 * Attributes  
 > - name="machine-name"  
 >   machine에 이름을 할당한다.  
 >   `<node>` 태그에 사용되는 machine attribute와 일치한다.  
 > - address="blah.willowgarage.com"  
 >   기기의 네트워크 주소/호스트이름 을 기재한다.  
 > - env-loader="/opt/ros/fuerte/env.sh"  
 >   원격 기기의 환경 파일을 지정. 환경 파일은 shell script여야 하며 필요한 모든 환경 변수가 설정되어 있어야 한다.  
 > - default="true|false|never" _(optional)_  
 >   해당 기기가 모든 노드들의 기본 실행 기기가 될 것인지 설정한다. 기본 기기가 없으면 로컬 기기가 기본 기기로 작동한다.  
 > - timeout="10.0" _(optional)_  
 >   설정한 시간동안(초단위) 해당 기기로부터 응답이 없으면 연결 실패로 간주한다.  
   
 * Element  
 > `<env>`  
 >   기기에서 실행되는 모든 프로세스의 환경 변수를 설정한다.  
 
 __Examples__
 ```
 <machine name="foo" address="foo-address" ros-root="/u/user/ros/ros/" ros-package-path="/u/user/ros/ros-pkg" user="someone">
   <env name="LUCKY_NUMBER" value="13" />
 </machine>

 <node machine="foo" name="footalker" pkg="test_ros" type="talker.py" />
 ```
 
### 3. __`<include>`__
 ###### More details at [wiki.ros.org/roslaunch/XML/include](wiki.ros.org/roslaunch/XML/include)  
 `<include>` 태그는 현재 launch 파일에서 다른 roslaunch XML 파일을 불러올 수 있게 한다.  
 해당 태그에선 다음의 attributes 및 element를 사용한다.
 * Attributes  
 > - `file="$(find pkg-name)/path/filename.xml"`  
 >   불러올 file의 이름을 기재한다.  
 > - `ns="foo"` _(optional)_
 >   파일을 'foo' namespace에 대해 불러온다.  
 > - `clear_params="true|false` _(optional)_
 >   launch 수행 전에 <include>의 네임스페이스 파라미터를 전부 제거한다. true인 경우 반드시 ns attribute와 같이 사용해야하며 기본값은 false다.
   
 * Element  
 > `<env>`  
 >   include한 파일의 환경 변수를 설정한다.  
 > `<arg>`  
 >   include한 파일에 argument를 전달한다.  


이외에도 `<rosparam>, <group>, <param>` 등 사양할 수 있는 태그가 많다.
다른 태그에 대한 설명은 [여기](https://enssionaut.com/board_robotics/974)나 [로스 위키 roslaunch/XML](wiki.ros.org/roslaunch/XML)의 4번 항목(Tag Reference)을 참고하라.  

## How to execute ROSlaunch file?  
이제 만든 roslaunch file을 실행시켜 보자.  
launch 파일을 실행하는 구문 포맷은 패키지로 launch 파일을 특정짓는 방법과 파일의 절대경로로 특정짓는 방법, 이 두 가지로 볼 수 있다.
```
$ roslaunch <package-name> <launch-filename>
```
or
```
$ roslaunch <launch-file-paths...>
```
단순히 실행하는 명령어에 몇가지 옵션을 추가하여 실행할 수도 있는데, 이에 관해선 [여기](http://wiki.ros.org/roslaunch/Commandline%20Tools)의 1항목을 참조하라. 
roslaunch는 roslaunch.launch(XML format)를 뿐만이아니라그외 관련 기능들을 수행할 수 있는 명령어를 포함하고 있는 __ROS1__ 패키지이다.  
다른 명령어대한 설명은 [여기](http://wiki.ros.org/roslaunch/Commandline%20Tools)를 참조하자.


## 참고하면 좋을 링크들  
1. wiki.ros.org/roslaunch
2. https://enssionaut.com/board_robotics/974
3. http://hrepository.blogspot.com/2017/03/roslaunchfile.html  



 


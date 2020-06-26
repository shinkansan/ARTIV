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

1. __`<node>`__  
 특정 노드를 bring up하거나 take down할 때 사용하는 태그다. 노드의 실행 순서는 __랜덤이다.__  
 다음 attributes를 사용하여 node를 특정지을 수 있다.
 > * pkg="mypackage"  
 >   node의 package를 지정  
 > * type="nodetype"  
 >   node 실행 파일 이름을 기입한다  
 > * name="nodename"  
 >   node 이름을 지정. 노드 내부에서 설정한 이름보다 우선순위가 높다.  
 > * args="arg1 arg2 ..." _(optional)_  
 >   node에 argument를 전달한다.  
 > * machine="mahine-name" _(optional)_  
 >   지정한 기기에서 노드를 실행한다.  
 > * respawn="true" _(optional)_  
 >   true : 노드가 종료될 때 자동으로 재시작  
 > * respawn_delay="seconds" _(optional)_  
 >   노드에 failure가 발견되는 경우 재시작 전까지 지정된 시간 동안 대기  
 > * output="log|screen" _(optional)_  
 >   값이 screen일 때 노드의 stdout/stderr를 화면에 출력. log인 경우 stderr를 화면에 출력하고 로그 파일을 $ROS_HOME/log 경로에 생성한다.  
 
 __Examples__
 ```
 <node name="listener1" pkg="rospy_tutorials" type="listener.py" args="--test" respawn="true" />
 ```
 "listenr1" 노드를 listener.py를 사용하여 실행한다.  
 이 때 "listener1"노드는 rospy_tutorials 패키지의 노드이며, command line에서 argument --test 를 받아온다.  
 만약 노드가 죽으면 자동으로 재시작된다.
 
 
 
2. __<machine>__
3. __<include>__
4. __<remap>__

## How to execute ROSlaunch file?  
A라는 패키지의 B라는 launch 파일을 실행시키는 코맨드는 다음과 같다.  
```
$ roslaunch A B
```

To be continued...

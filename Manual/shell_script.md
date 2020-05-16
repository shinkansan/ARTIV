## 쉘스크립트 .sh 파일로 다 실행해보기

초반에 roscore, ros1_bridge, sourcing, dbw_node 등 실행하는 것이 너무 많아 귀찮다면 shell script를 써보는 것이 좋다.

### .sh
shell scipt는 터미널에 치는 한줄 한줄 치는 명령어를 쭉 적어놓은 파일입니다.
그리고 기본적인 변수나 For, If도 있긴합니다.


만드는 방법은 그냥 에디터에서 파일을 .sh 형식으로 저장하면 됩니다.

실행은 터미널에서 sh <파일.sh> 하거나, .sh 파일을 chmod로 executable 형식으로 바꾸면 `chmod +x <file.sh>`
 `./<파일이름>` 으로도 실행이 가능하다.


### sh 예시

```bash
 #! /bin/bash
xterm -hold -e "source /opt/ros/melodic/setup.bash; roscore" &
sleep 2;
xterm -hold -e "source /opt/ros/melodic/setup.bash; source /opt/ros/dashing/setup.bash; ros2 run ros1_bridge dynamic_bridge --brdige-all-topics" &
xterm -hold -e "source /opt/ros/dashing/setup.bash; cd dbw_ioniq_node; python3 dbw_ioniq_node.py" &
xterm -hold -e "source /opt/ros/dashing/setup.bash; cd dbw_cmd_node; python3 dbw_cmd_node.py" &
```

* xterm은 작은 터미널 창으로 항상 켜져있어야하는 roscore나 병렬적으로 실행할 필요가 있는 명령어를 위해서

 sh 상에서 그 명령어만 처리하는 새로운 터미널 창을 열어서 동작하게 하는 전략이다! 동시에 각 명령어 뒤에 &는 명령어를 실행한 순간 shell과 분리시켜 동작시켜서 유사 병렬 처리를 하게 만드는 커맨드이다.   


 * ; 세미콜론은 명령어와 명령어를 구분짓는 표시이다. 그래서 쓴다. &&를 써도되지만 ;를 추천한다.

 * 절대경로 사용 추천
 sh를 키면 sh이 있는 위치에서 실행된다 그래서 다른 위치에서의 파일을 실행할려면 절대경로를 입력해야한다. cd를 잘 이용하자.


### sh를 클릭하면 편집창이 뜬다! 이걸 실행하게 만들려면?

우선 .sh 파일을 실행가능한 파일로 만들어야한다.
`chmod +x <파일>`

그리고  
`gsettings set org.gnome.nautilus.preferences executable-text-activation ask`
터미널에 치면

![Screenshot from 2020-05-16 16-30-05](https://user-images.githubusercontent.com/25432456/82113643-8e801700-9792-11ea-81a0-5792b76f4693.png)


물어본다. 물어보는 것도 싫으면 뒤 부분 ask를 launch로 바꾸면 된다.

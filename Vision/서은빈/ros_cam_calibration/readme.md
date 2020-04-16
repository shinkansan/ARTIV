# Ros camera calibration
> reference: http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration

### setting
1. intstall uvc-camera pkg
~~~(bash)
sudo apt-get install ros-melodic-uvc-camera
sudo apt-get install ros-melodic-image-*
sudo apt-get install ros-melodic-image-view
~~~
2. OpenCV camera calibration
OpenCV를 설치하자. 다음 링크를 참고한다. https://sunkyoo.github.io/opencv4cvml/OpenCV4Linux.html
3. camera가 잘 연결되는지 확인해보자.
~~~(bash)
lsusb
ls -ltr /dev/video*
~~~
잘 연결되었을 시에 다음과 같은 메시지가 출력될 것이다.
<img src="./media/idea_record_log.png" width="80%" height="80%" title="idea_record_log.png" >

### Run!
1. ros1을 키고, roscore를 켜준다.(모두가 알죠? source /opt/ros/melodic/setup.bash 모르면 이 [링크](/ROS/readMe.md)타고 들어가서 공부해오세요.)
2. 또 다른 창에 ros1을 키고, 다음 명령어 입력
~~~(bash)
rosrun uvc_camera uvc_camera_node 
~~~
3. 노드를 실행시키면 camera calibration file이 없다는 내용으로 warning이 뜬다. camera.yaml 파일을 생성하자
4. 

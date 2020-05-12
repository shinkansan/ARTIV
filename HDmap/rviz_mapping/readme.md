# rviz mapping

작성일 : 2020/05/12

작성자 : 송주호

조건 : ros1의 rviz

설명 : 차량운행을 통해 gps정보를 녹화한 rosbag에서 위도/경도/고도에 해당하는 정보를 rostopic /fix에서 받아와서 rviz 상에 매핑

![매핑](https://user-images.githubusercontent.com/59792475/81654343-78abe280-9470-11ea-8520-1480df1629b2.png)

![매핑2](https://user-images.githubusercontent.com/59792475/81654381-7f3a5a00-9470-11ea-9917-cd36613f818a.png)

rosbag의 정보 중 원하는 토픽을 txt 파일로 받아오고, 해당 정보를 rviz에 plotting하는 노드를 구성하여 모든 점을 plotting하는 기능을 구현함.

`rostopic echo -b file.bag -p /topic > data.txt` 사용하면 rostopic의 원하는 topic의 data를 txt파일에 적을 수 있음

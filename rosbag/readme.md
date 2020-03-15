# 외부 공개 Dataset
rosbag이란 node와 node간의 topic의 통신을 시계열로 모두 수집한 것으로   
차량 주행 시 센서에서 수집된 모든 데이터를 저장할 수 있다.

그래서 실제 차량에서 실시간으로 맵핑이 어려운 - SLAM의 경우에는 bag파일로 녹화 후 고성능 PC로 연산을 돌린다.

이러한 bag파일은 공유도 쉽고 단일 파일로 관리가 쉬운데, 여러 연구 단체에서 해당 파일을 연구성과로 제출하기도한다.
https://epan-utbm.github.io/utbm_robocar_dataset/

아래 링크에 들어가서 `rosbag play` 명령을 인터넷에서 찾아서 돌려보자

---
# ROSBAG dedicate server

Since rosbag is large and hard to download (most of server is not good as dedicate server)   
We collect ROSBAG from open dataset web or our Autonomous Car platform

Dedicate Server address
> [ktk1501.synology.me:5000](http://ktk1501.synology.me:5000)

### Server saving guideline

#### Folder Structure
```
/Non-image
..../lidar
..../radar
..../All-in-one
........{order}-{lengthOfFile}.bag
........{order}-bagInfo.txt
/Imgae
```

#### baginfo
Scrap terminal text by `rosbag info` to text file   
and add links to original opensource dataset link for copyright issue


![example](https://i.imgur.com/ArmzfZ6.png)

## PCL(PointCloud Library) 및 PCD(PointCloud Data) 사용법 공부
Lidar에서 받아오는 점군을 시각화하기 위해 PCL을 사용함.

Point cloud란 3차원 공간상에 퍼져 있는 여러 포인트(Point)의 집합(set cloud)을 의미. 점군은 3D 데이터이므로 x,y,z축 정보를 가지고 있기 때문에 기본적으로 N x 3 Numpy 배열로 표현된다. 
Point Cloud는 기본적으로는 x,y,z 세개의 정보로만 표현 가능하지만 RGB-D에는 Color정보같이 추가 정보가 있을경우 N x 4Numpy 배열로도 표현 가능하다.

PCL은 Point cloud의 파일 저장, 읽기, 잡음제거, 정합, 군집화, 분류, Feature계산 등의 기능을 제공한다.

PDC는 헤더와 데이터 정보를 가진 파일이다. 아래 사진을 보면 헤더에는 version ~ points 까지 있다. 데이터는 x,y,z 값과 센서가 보내는 부가 정보를 나타낸다. 여기서 가장 중요한건 데이터가 어떻게 저장되어있는지 알려주는 FIELDS 다.

![Screenshot from 2020-04-08 18-25-31](https://user-images.githubusercontent.com/59762212/78768149-83351100-79c6-11ea-87a1-9c37a1b2544d.png)

[참고 사이트(한글)](https://pcl.gitbook.io/tutorial/)

##

### PCL 설치 방법
#### PCL-C++ 
> `sudo apt-get update && sudo apt-get install -y software-properties-common git`

> `sudo apt-get install -y libpcl-dev #ubuntu 18 (PCL 1.8)`

> `sudo apt-get update -qq`

> `sudo apt-get install -y --no-install-recommends make cmake cmake-gui build-essential git libeigen3-dev libflann-dev libusb-1.0-0-dev libboost-all-dev`

> `sudo rm -rf /var/lib/apt/lists/*`

> `git clone https://github.com/PointCloudLibrary/pcl.git`

> `cd pcl && mkdir release && cd release`

> `cmake -DCMAKE_BUILD_TYPE=None -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_GPU=ON -DBUILD_apps=ON -DBUILD_examples=ON -DCMAKE_INSTALL_PREFIX=/usr ..`

> `make -j8` 
한참걸림

> `sudo make install`



#### PCL-Python

[[1](https://pcl.gitbook.io/tutorial/)] PCL 튜토리얼

[[2](http://pointclouds.org/documentation/tutorials/pcd_file_format.php)] PCL & PCD 사이트

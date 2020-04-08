## PCL(PointCloud Library) 및 PCD(PointCloud Data) 사용법 공부
Lidar에서 받아오는 점군을 시각화하기 위해 PCL을 사용함.

포인트 클라우드(Point cloud)란 3차원 공간상에 퍼져 있는 여러 포인트(Point)의 집합(set cloud)을 의미. 점군은 3D 데이터이므로 x,y,z축 정보를 가지고 있기 때문에 기본적으로 N x 3 Numpy 배열로 표현된다. 
Point Cloud는 기본적으로는 x,y,z 세개의 정보로만 표현 가능하지만 RGB-D에는 Color정보같이 추가 정보가 있을경우 N x 4Numpy 배열로도 표현 가능하다.

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

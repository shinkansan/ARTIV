## PCL(PointCloud Library) 및 PCD(PointCloud Data) 사용법 공부
Author : 양재승
---

Lidar에서 받아오는 점군을 시각화하기 위해 PCL을 사용함.

Point cloud란 3차원 공간상에 퍼져 있는 여러 포인트(Point)의 집합(set cloud)을 의미. 점군은 3D 데이터이므로 x,y,z축 정보를 가지고 있기 때문에 기본적으로 N x 3 Numpy 배열로 표현된다. 
Point Cloud는 기본적으로는 x,y,z 세개의 정보로만 표현 가능하지만 RGB-D에는 Color정보같이 추가 정보가 있을경우 N x 4Numpy 배열로도 표현 가능하다.

PCL은 Point cloud의 파일 저장, 읽기, 잡음제거, 정합, 군집화, 분류, Feature계산 등의 기능을 제공한다.

PDC는 헤더와 데이터 정보를 가진 파일이다. 아래 사진을 보면 헤더에는 version ~ points 까지 있다. 데이터는 x,y,z 값과 센서가 보내는 부가 정보를 나타낸다. 여기서 가장 중요한건 데이터가 어떻게 저장되어있는지 알려주는 FIELDS 다.

![Screenshot from 2020-04-08 18-25-31](https://user-images.githubusercontent.com/59762212/78768149-83351100-79c6-11ea-87a1-9c37a1b2544d.png)
##

[참고 사이트(한글)](https://pcl.gitbook.io/tutorial/)

[참고 사이트(영어)](http://pointclouds.org/documentation/)

##

### PCL 설치 방법
#### PCL-C++ 

> `sudo apt-get update && sudo apt-get install -y software-properties-common git`

> `sudo apt-get install -y libpcl-dev`

> `sudo apt-get update -qq`

> `sudo apt-get install -y --no-install-recommends make cmake cmake-gui build-essential git libeigen3-dev libflann-dev libusb-1.0-0-dev libboost-all-dev`

> `sudo rm -rf /var/lib/apt/lists/*`

> `git clone https://github.com/PointCloudLibrary/pcl.git`

> `cd pcl && mkdir release && cd release`

> `cmake -DCMAKE_BUILD_TYPE=None -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_GPU=ON -DBUILD_apps=ON -DBUILD_examples=ON -DCMAKE_INSTALL_PREFIX=/usr ..`

> `make -j8` 
  한참걸림

> `sudo make install`

> `sudo apt-get install ros-melodic-pcl-conversions ros-melodic-pcl-ros`
  ros 뒤의 melodic은 ros 버전을 맞춰서 적어주면 된다.

설치 끝. 
####

참고 사이트[한글]에 들어가서 
> `sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl -y && sudo apt-get update`
치지마라 sudo apt update 할 때 에러난다.
만약 모르고 쳤다면 
> `cd /etc/apt/sources.list.d`
치고 들어가서 
> `sudo rm -r v-launchpad-jochen-sprickerhof-de/pcl`
해서 비슷하게 생긴 두 줄을 지운 후 아래 차례를 따라가면 된다.
####


##

#### PCL-Python
우분투 18.04에서 지원 안함.



### PCL 사용

#### File 생성 및 입출력

##### PCD 파일 데이터 읽어오기
파일 위치가 중요하다. CMakeLists.txt 는 pcd_read.cpp 의 바로 상위파일에 존재해야한다. (그래야 build가 가능하다)

//CMakeLists.txt

~~~
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(pcd_read)

find_package(PCL 1.2 REQUIRED)
include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})


add_executable (pcd_read pcd_read.cpp)
target_link_libraries (pcd_read ${PCL_LIBRARIES})
~~~

##

//pcd_read.cpp (코드 내 test_pcd.pcd를 내가 저장한 pcd 파일로 바꿔주자!)

~~~
#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>

int main (int argc, char** argv)
{
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>);

  if (pcl::io::loadPCDFile<pcl::PointXYZ> ("test_pcd.pcd", *cloud) == -1) //* load the file
  {
    PCL_ERROR ("Couldn't read file test_pcd.pcd \n");
    return (-1);
  }
  std::cout << "Loaded "
            << cloud->width * cloud->height
            << " data points from test_pcd.pcd with the following fields: "
            << std::endl;
  for (std::size_t i = 0; i < cloud->points.size (); ++i)
    std::cout << "    " << cloud->points[i].x
              << " "    << cloud->points[i].y
              << " "    << cloud->points[i].z << std::endl;

  return (0);
}
~~~
##

실행 방법 (pcd 파일을 pcd_read.cpp 와 같은 폴더에 넣어주면 된다. - 아니면 파일 위치를 정확히 코드 내에 기재해라!)

cpp파일이 있는 폴더에서 
> `cmake .. && make`

> `./pcd_read`

실행 예시

![Screenshot from 2020-04-08 20-31-21](https://user-images.githubusercontent.com/59762212/78779467-f8f5a880-79d7-11ea-935f-16beda0b90b8.png)

#### ROI(Region of Interesting) 설정
관심 영역을 설정하여 LIDAR 데이터 중 자율 주행에 필요없는 점군을 제거하거나 차량 근처 위험반경을 관심영역으로 만들어 예의주시할 수 있다.

//CMakeLists.txt

위에서 한 pcd_read를 위해 CMakeLists.txt 파일을 만들어놨다면 
~~~
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(pcd_read)
+project(pcd_roi)

find_package(PCL 1.2 REQUIRED)
include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})


add_executable (pcd_read pcd_read.cpp)
+add_executable (pcd_roi pcd_roi.cpp)
target_link_libraries (pcd_read ${PCL_LIBRARIES})
+target_link_libraries (pcd_roi ${PCL_LIBRARIES})
~~~
이런 식으로 +부분만 추가해주면 된다.(pcl을 사용하기 떄문)
##

//pcd_roi.cpp (코드 내 tabletop.pcd를 내가 저장한 pcd 파일로 바꿔주자!)
~~~
#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/passthrough.h>

int
 main (int argc, char** argv)
{
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGB>);
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_filtered (new pcl::PointCloud<pcl::PointXYZRGB>);


  pcl::io::loadPCDFile<pcl::PointXYZRGB> ("tabletop.pcd", *cloud);

  std::cout << "Loaded :" << cloud->width * cloud->height  << std::endl;

  // Create the filtering object
  pcl::PassThrough<pcl::PointXYZRGB> pass;
  pass.setInputCloud (cloud);
  pass.setFilterFieldName ("x");
  pass.setFilterLimits (0.70, 1.5);
  //pass.setFilterLimitsNegative (true);
  pass.filter (*cloud_filtered);

  std::cout << "Filtered :" << cloud_filtered->width * cloud_filtered->height  << std::endl;
  
  
  

  pcl::io::savePCDFile<pcl::PointXYZRGB>("tabletop_passthrough.pcd", *cloud_filtered); //Default binary mode save

  return (0);
}
~~~
 
실행 방법 (pcd_read.cpp 와 같은 방식으로 파일 배치 후)

> `cmake .. && make`

> `./pcd_roi`

실행 예시

![Screenshot from 2020-04-08 21-00-28](https://user-images.githubusercontent.com/59762212/78781913-0f9dfe80-79dc-11ea-8a4a-42e2f1300d9c.png)

// passthrough.pcd 파일이 생성된것을 알 수 있다.

![Screenshot from 2020-04-08 21-00-49](https://user-images.githubusercontent.com/59762212/78782130-78857680-79dc-11ea-9feb-41b319b7c79e.png)

시각화 방법 (cpp 파일이 있는 폴더에서 실행)
> `pcl_viewer tabletop.pcd`

> `pcl_viewer tabletop_passthrough.pcd`

실행하면 새로운 창이 뜨면서 점이 보인다!

점군을 적게하면 아무것도 안보일 수 있으니 pcd파일을 잘 구해보자! (내가 기준으로 잡은 pcd파일은 점 개수가 너무 적다.)

##

#### Noise 제거 (확률적인 방법 or 거리에 중점을 둔 방법) ---- 논문 읽고 알고리즘 따올 필요

#### Ransac (주변 구조물을 확신할 수 있는 방법? - 어떤 방식으로 이용할지 공부 필요)








[[1](https://pcl.gitbook.io/tutorial/)] PCL 튜토리얼

[[2](http://pointclouds.org/documentation/tutorials/pcd_file_format.php)] PCL & PCD 사이트

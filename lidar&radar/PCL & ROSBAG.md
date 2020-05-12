### 우분투 18.04에서 python-pcl이 지원 안되므로 cpp로 진행.
catkin 파일 내에서 진행.  idar rosbag의 값을 subscribe하여 진행.

cpp파일은 input, sampling, ROI 로 이루어진다. 코드의 내용이 궁금하면 주석을 읽어라.(CMakeList.txt , package.xml 포함)

### 0. Rosbag rviz

![Screenshot from 2020-05-12 21-51-05](https://user-images.githubusercontent.com/59762212/81695021-06052c00-949d-11ea-9474-3d1800145b8c.png)

rosbag을 rviz로 시각화한 사진
###
### 방법
1. roscore 를 킨다.

2. rosbag play -l [rosbag file] 을 새 터미널에 입력

3. 새 터미널에 rviz 입력 (Fixed_Frame = velodyne)

4. Add -> By topic -> velodyne_points의 PointCloud2 추가.


### 1. Input

![Screenshot from 2020-05-12 22-02-42](https://user-images.githubusercontent.com/59762212/81694592-7b243180-949c-11ea-8a47-c9c75907ef64.png)

rosrun 을 이용하여 rosbag 데이터를 받아오고 있는 사진
###

![Screenshot from 2020-05-12 22-03-39](https://user-images.githubusercontent.com/59762212/81694617-824b3f80-949c-11ea-851d-f43bd7e9e924.png)

rviz를 이용하여 시각화한 사진

### 방법
1. roscore를 킨다.

2. rosbag play -l [rosbag file] 을 새 터미널에 입력

3. rosrun [CMakeLists.txt가 있는 파일] input

4. 새 터미널에 rviz 입력 (Fixed_Frame = velodyne)

5. Add -> By topic -> output의 PointCloud2 추가.

###


### 2. Sampling

![Screenshot from 2020-05-12 21-51-08](https://user-images.githubusercontent.com/59762212/81696267-a3149480-949e-11ea-939c-0bfc389c9016.png)

rviz를 이용하여 시각화한 사진

### 방법
1. roscore를 킨다.

2. rosbag play -l [rosbag file] 을 새 터미널에 입력

3. rosrun [CMakeLists.txt가 있는 파일] sampling

4. 새 터미널에 rviz 입력 (Fixed_Frame = velodyne)

5. Add -> By topic -> velodyne_points_sampling의 PointCloud2 추가.

###

### 3. ROI

![Screenshot from 2020-05-12 21-51-13](https://user-images.githubusercontent.com/59762212/81696493-ec64e400-949e-11ea-9511-566ce25c22ee.png)

rviz를 이용하여 시각화한 사진

### 방법
1. roscore를 킨다.

2. rosbag play -l [rosbag file] 을 새 터미널에 입력

3. rosrun [CMakeLists.txt가 있는 파일] sampling

4. rosrun [CMakeLists.txt가 있는 파일] ROI_

5. 새 터미널에 rviz 입력 (Fixed_Frame = velodyne)

6. Add -> By topic -> velodyne_points_roi의 PointCloud2 추가.

###

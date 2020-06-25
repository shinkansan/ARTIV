# ROS yolo v3 with usb camera
Author: 이  구
Date: 2020.06.25
> reference: https://github.com/yehengchen/Object-Grasp-Detection-ROS/tree/master/yolov3_pytorch_ros

## 사용법
catkin_ws로 이동 후, catkin_make, source

### usb camera에서 영상 받아오기

```(bash) 
rosrun usb_cam usb_cam_node
```

### yolo 실행

```(bash) 
roslaunch yolov3_pytorch_ros detector.launch 
```

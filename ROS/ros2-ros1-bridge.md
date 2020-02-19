# ROS2-ROS1 Bridge Installation & Test Guide
Author : GWANJUN SHIN

After install ros1 & ros2, we've to establish inter connection solution called /ros1_bridge dynamic_bridge



## Pre-condition 
0. You need to finish ROS1 & ROS2 Install via [index.ros.org](https://index.ros.org/doc/ros2/Installation/Dashing/Linux-Install-Debians/)
1. our development environment is based on Ubuntu 18.04 LTS
2. Install bridge package by `sudo apt install ros-dashing-ros1-bridge`
3. ROS2 must be default ROS system on Terminal --> `source /opt/ros/dashing/setup.bash' must be on ./bashrc

## Add shortcut command to Activate ros1 and Bridge

> 1. `echo 'alias start_ros1_bridge"=( source /opt/ros/melodic/setup.bash && ( roscore & source ~/ros1_bridge_ws/install/setup.bash && sleep 1 && ros2 run ros1_bridge dynamic_bridge --bridge-all-topics ) && killall roscore ) || killall roscore"' >> ~/.bashrc `   
   
> 2. ` echo 'alias start_ros1"=( source /opt/ros/melodic/setup.bash )"' >> ~/.bashrc `   

Then, you can simply activate ros1 and bridge with simple command `start_ros1_bridge` 
And only for ros1 environment by `start_ros1`


or You can just type manually (works everytime)
> `source /opt/ros/melodic/setup.bash `
> `roscore`   
> `source /opt/ros/dashing/setup.bash`       
> `ros2 run ros1_bridge dynamic_bridge --bridge-all-topics`   

note that melodic is stand for ros1 and dashing is stand for ros2


## Test
### ROS2 for broadcasting Webcam feed, ROS1 for visualizing
> `ros2 run ros1_bridge dynamic_bridge --bridge-all-topics`    You can pass if you already execute this.
> `ros2 run image_tools cam2image`   
> `rviz` and add topic image

Tip : You can try vice versa


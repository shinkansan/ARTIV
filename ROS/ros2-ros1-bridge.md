# ROS2-ROS1 Bridge Installation & Test Guide
Author : GWANJUN SHIN

After install ros1 & ros2, we've to establish inter connection solution called /ros1_bridge dynamic_bridge



## Pre-condition 
0. You need to finish ROS1 & ROS2 Install via [index.ros.org](https://index.ros.org/doc/ros2/Installation/Dashing/Linux-Install-Debians/)
1. our development environment is based on Ubuntu 18.04 LTS
2. Install bridge package by `sudo apt install ros-dashing-ros1-bridge`
3. ROS2 must be default ROS system on Terminal --> `source /opt/ros/dashing/setup.bash' must be on ./bashrc

## Add short command to activate ros1 or ros2 (optional)
> `echo "alias start_ros1='source /opt/ros/melodic/setup.bash'" >> ~/.bashrc`   
> `echo "alias start_ros2='source /opt/ros/dashing/setup.bash'" >> ~/.bashrc`   

Now you can activate ros1 or ros2 without sourcing. Just type `'start_ros1'` or `'start_ros2'`!   
Remember for applying changes of bashrc, open new terminal or type `source ~/.bashrc`      

### Type these commands manually (works everytime)
> `start_ros1`  or `source /opt/ros/melodic/setup.bash`   
> `roscore`   종료하지 말기   
> 다른 터미널 실행!   
> `start_ros1`    
> `start_ros2`   or `source /opt/ros/dashing/setup.bash`          
> `ros2 run ros1_bridge dynamic_bridge --bridge-all-topics`      

 _잠깐! 같은 터미널에서 두개의 환경을 왜 나란히 쳐요? --> ros1_bridge 패키지 안에는 ros1과 2를 둘다 사용하기 때문에 나란히 실행하는 걸 추천합니다._
 

note that melodic is stand for ros1 and dashing is stand for ros2


## Test
### ROS2 for broadcasting Webcam feed, ROS1 for visualizing
> `ros2 run ros1_bridge dynamic_bridge --bridge-all-topics`    You can pass if you already execute this.
> `ros2 run image_tools cam2image`   
> 다른 터미널 실행 후 멜로딕    
> `rviz` and add topic image

Tip : You can try vice versa


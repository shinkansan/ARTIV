# LGSVL Simulator
Simulation software to accelerate safe autonomous vehicle development


[Link](https://github.com/lgsvl/simulator)

## Important
  __if lgsvl terminate after click start__ <br/>
  There is a issue on Ubuntu 18.04, We need to install libvulkan1
  ```bash
  sudo apt-get install libvulkan1
  ```
  and reboot

## Pre-condition
  1. ros2-dashing
  2. python3
  3. tensorflow
  4. keras 
 
## How we use it
  1. Install it 
  2. Download ros2-web-bridge [link](https://github.com/RobotWebTools/ros2-web-bridge) <br/>
    1. install nvm <br/>
    ```bash
    nvm install 10.18
    ```
    2. install rclnodejs 
    ```bash
    npm i rclnodejs
    ```
    3. download ros2-web-bridge and goto its folder directory
    ```bash
    npm install
    ```
    4. done
   
  3. Now you can use it by ```node bin/rosbridge.js``` in ros2-web-bridge folder <br/>
   __you should not close that terminal while node js is running__ <br/>
   it working as server, so it must be opened while using LGSVL
  

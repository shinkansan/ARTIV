# dbw_ioniq for receive and send data
Date : 2020.07.02

### 0. install tools
1. go to [manual](https://github.com/shinkansan/ARTIV/blob/master/Comms/CAN/socket_can_connect.md)    
2. ```touch first_setup.bash``` (in /dbw_ioniq_v2_release)     

### 1. Start launch
1. ```catkin_make``` (in ros1 workspace)    
2. ```source devel.setup.bash```    
3. ```roslaunch dbw_ioniq_bridge dbw_ioniq_bridge.launch```    

### 2. node list
1. /dbw_cmd_node    
2. /dbw_ioniq_node    

### 3. topic list
1. /Ioniq_info       -> std_msgs/Float32Multiarray    
2. /Joint_state      -> sensor_msgs/JointState    
3. /dbw_cmd/Accel    -> std_msgs/Int16    
4. /dbw_cmd/Angular  -> std_msgs/Int16    
5. /dbw_cmd/Brake    -> std_msgs/Int16    
6. /dbw_cmd/Gear     -> std_msgs/Int16    
7. /dbw_cmd/Steer    -> std_msgs/Int16    
8. /received_messages-> can_msgs/Frame    
9. /sent_messages    -> can_msgs/Frame    

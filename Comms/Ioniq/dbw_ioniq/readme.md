### DBW_IONIQ_NODE HOWTO   

1. 이 디렉토리에 있는 파일을 한 곳에 넣어놓고 com_start.sh 실행하면 `sh ./com_start.sh`      
    1. ros1 - roscore   
    2. ros2 - ros1_bridge dynamic_bridge --bridge-all-topcis   
    3. ros2 - dbw_ioniq_cmd, dbw_cmd_node 를 실행   
    
 이게 한번에 실행된다.
 

### Problem : '/dbw_cmd/~' command in ros1 was not sent to ros1-ros2 bridge
-> Solution : Create publisher named '/dbw_cmd/~' in ros2

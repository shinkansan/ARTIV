#! /bin/bash
xterm -hold -e "source /opt/ros/melodic/setup.bash; roscore" &
sleep 2;
xterm -hold -e "source /opt/ros/melodic/setup.bash; source /opt/ros/dashing/setup.bash; ros2 run ros1_bridge dynamic_bridge --brdige-all-topics" &
xterm -hold -e "source /opt/ros/dashing/setup.bash; python3 dbw_ioniq_node/dbw_ioniq_node.py" &
xterm -hold -e "source /opt/ros/dashing/setup.bash; python3 dbw_cmd_node/dbw_cmd_node.py" &

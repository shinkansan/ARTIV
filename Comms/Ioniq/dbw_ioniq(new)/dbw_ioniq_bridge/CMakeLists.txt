cmake_minimum_required(VERSION 3.0.2)
project(dbw_ioniq_bridge)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

install(FILES
  scripts/dbw_ioniq_bridge.launch
  scripts/run_modprobe.sh	
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/dbw_ioniq_bridge
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

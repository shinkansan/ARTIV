cmake_minimum_required(VERSION 3.0.2)
project(dbw_ioniq_node)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

catkin_install_python(PROGRAMS
  scripts/dbw_ioniq_node.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/dbw_ioniq_node
)

install(FILES
  scripts/dbw_ioniq.launch
  scripts/run_modprobe.sh	
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/dbw_ioniq_node
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

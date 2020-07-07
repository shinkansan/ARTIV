cmake_minimum_required(VERSION 3.0.2)
project(dbw_erp42_node)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

catkin_install_python(PROGRAMS
  scripts/dbw_erp42_node.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/dbw_erp42_node
)

install(FILES
  scripts/dbw_erp42_node.py	
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/dbe_erp42_node
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

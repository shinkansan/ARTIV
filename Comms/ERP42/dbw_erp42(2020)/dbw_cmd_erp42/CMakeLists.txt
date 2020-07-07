cmake_minimum_required(VERSION 3.0.2)
project(dbw_cmd_erp42)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

catkin_install_python(PROGRAMS
  scripts/dbw_cmd_erp42.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/dbw_cmd_erp42
)

install(FILES
  scripts/dbw_cmd_erp42.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/dbw_cmd_erp42
)

generate_messages(
  DEPENDENCIES
  std_msgs
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)

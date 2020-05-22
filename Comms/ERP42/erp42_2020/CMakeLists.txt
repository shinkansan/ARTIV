cmake_minimum_required(VERSION 3.0.2)
project(erp42_2020)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

add_message_files(
  FILES
  ERPmsg.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS 
  message_runtime
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
cmake_minimum_required(VERSION 3.0.2)
project(artiv_can)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
  Artivmsg.msg
  Frame.msg
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
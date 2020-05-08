#include <cstdio>
#include <unistd.h>


#include "rclcpp/rclcpp.hpp"



int main(int argc, char ** argv)
{
  (void) argc;
  (void) argv;

  rclcpp::init(argc, argv);

  auto node = std::make_shared<rclcpp::Node>("rclcpp_log_Test");

  while(1){
  RCLCPP_DEBUG(node->get_logger(), "test log debug");
  sleep(1);
  RCLCPP_INFO(node->get_logger(), "test log info");
  sleep(1);
  RCLCPP_WARN(node->get_logger(), "test log warn");
  sleep(1);
  RCLCPP_ERROR(node->get_logger(), "test log error");
  sleep(1);
  RCLCPP_FATAL(node->get_logger(), "test log fatal");
  sleep(1);}







return 0;
}

#include <memory>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

//ROS_relations
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_components/register_node_macro.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "std_msgs/msg/float64.hpp"
#include "sensor_msgs/msg/joint_state.hpp"
#include "std_msgs/msg/bool.hpp"

using namespace std;

float currentSpeed;
rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr pub;

void joint_callback(const sensor_msgs::msg::JointState::SharedPtr msg){
 currentSpeed = msg->velocity[0];
 auto pub_message = std::make_shared<std_msgs::msg::Float64>();
 pub_message->data = currentSpeed*3.6;
 pub->publish(pub_message);

 cout << "Got " << currentSpeed << " in km/h -> Publish " << to_string(pub_message->data) << " in m/s" << endl;
}


int main(int argc, char** argv){

  rclcpp::init(argc, argv);

  setvbuf(stdout, NULL, _IONBF, BUFSIZ);

  auto node = rclcpp::Node::make_shared("speed_ms_echo");
  auto sub2 = node->create_subscription<sensor_msgs::msg::JointState>("/vehicle/joint_states", joint_callback);
  pub = node->create_publisher<std_msgs::msg::Float64>("/ms_speed");


  rclcpp::spin(node);
  rclcpp::shutdown();

  return 0;

}


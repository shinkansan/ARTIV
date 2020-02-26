#include <memory>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

//OpenCV
#include "opencv2/opencv.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

//ROS_relations
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_components/register_node_macro.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "std_msgs/msg/float64.hpp"
#include "sensor_msgs/msg/joint_state.hpp"
#include "std_msgs/msg/bool.hpp"

using namespace std;
using namespace cv;

int  encoding2mat_type(const string & encoding);
string mat_type2encoding(int mat_type);
float currentSpeed = 0.0;

void image_show(const sensor_msgs::msg::Image::SharedPtr msg)
{ 
 cout << "Image Recieved" << msg->header.frame_id.c_str() << endl;
 
 cv::Mat frame(msg->height, msg->width, encoding2mat_type(msg->encoding),
	const_cast<unsigned char *>(msg->data.data()), msg->step);

 cv::Mat cvframe;
 if (msg->encoding == "rgb8") {
 cv::Mat frame2;
 cv::cvtColor(frame, frame2, cv::COLOR_RGB2BGR);
 cvframe = frame2;}
 else {
 cvframe = frame;}
 int height;
 height = cvframe.rows;
 cv::putText(cvframe, "Speed: " + to_string(currentSpeed), cv::Point(20, height-30), 1, 1.8, Scalar(0, 255, 0));

 cv::imshow("Image", cvframe);
 if(cv::waitKey(10)==27) exit(1);

}
 

int encoding2mat_type(const string & encoding) {
  if (encoding == "mono8") {
    return CV_8UC1;
  } else if (encoding == "bgr8") {
    return CV_8UC3;
  } else if (encoding == "mono16") {
    return CV_16SC1;
  } else if (encoding == "rgba8") {
    return CV_8UC4;
  } else if (encoding == "bgra8") {
    return CV_8UC4;
  } else if (encoding == "32FC1") {
    return CV_32FC1;
  } else if (encoding == "rgb8") {
    return CV_8UC3;
  } else {
    throw std::runtime_error("Unsupported encoding type");
  }
}

string mat_type2encoding(int mat_type) {
  switch (mat_type) {
    case CV_8UC1:
      return "mono8";
    case CV_8UC3:
      return "bgr8";
    case CV_16SC1:
      return "mono16";
    case CV_8UC4:
      return "rgba8";
    default:
      throw std::runtime_error("Unsupported encoding type");
  }
}


void image_callback(const sensor_msgs::msg::Image::SharedPtr msg){
 image_show(msg);
}

void joint_callback(const sensor_msgs::msg::JointState::SharedPtr msg){
 currentSpeed = msg->velocity[0];
 //cout << currentSpeed << endl;
}


int main(int argc, char** argv){

  rclcpp::init(argc, argv);

  setvbuf(stdout, NULL, _IONBF, BUFSIZ);
  
  auto node = rclcpp::Node::make_shared("sub_image_sample");
  
  auto sub = node->create_subscription<sensor_msgs::msg::Image>("/center_camera/image_color", image_callback);
  auto sub2 = node->create_subscription<sensor_msgs::msg::JointState>("/vehicle/joint_states", joint_callback);


  rclcpp::spin(node);
  rclcpp::shutdown();

  return 0;



}


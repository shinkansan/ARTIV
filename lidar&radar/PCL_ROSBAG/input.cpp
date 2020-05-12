#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
// PCL specific includes
#include <pcl/conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>

#include <iostream>       // std::cout
#include <typeinfo>       // operator typeid

ros::Publisher pub;

typedef pcl::PointXYZ              PointXYZ;

void callback (const sensor_msgs::PointCloud2 msg)
{
  std::cout << "msg is: " << typeid(msg).name() << '\n';

  //ros_pcl2 to pcl2
  pcl::PCLPointCloud2 pcl_pc;
  pcl_conversions::toPCL(msg, pcl_pc);
  std::cout << "cloud is: " << typeid(msg).name() << '\n';

  //pcl2 to pclxyzrgba
  pcl::PointCloud<PointXYZ> input_cloud;
  pcl::fromPCLPointCloud2(pcl_pc, input_cloud);

  // Publish the data
  sensor_msgs::PointCloud2 output;
  output = msg;
  pub.publish (output);
}

int main (int argc, char** argv)
{
  // Initialize ROS
  ros::init (argc, argv, "pcl_input");
  ros::NodeHandle nh;

  // Create a ROS subscriber for the input point cloud
  ros::Subscriber sub = nh.subscribe ("/velodyne_points", 1, callback);

  // Create a ROS publisher for the output point cloud
  pub = nh.advertise<sensor_msgs::PointCloud2> ("output", 1);

  // Spin
  ros::spin ();
}

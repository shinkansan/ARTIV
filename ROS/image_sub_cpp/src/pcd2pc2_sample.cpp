#include <iostream>
#include <string>

#include "rclcpp/rclcpp.hpp"

#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl_ros/io/pcd_io.h>

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;
using namespace std;

int main(int argc, char** argv)
{
  double x_cloud; double y_cloud; double z_cloud;
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>);
  rclcpp::init (argc, argv, "my_pcl_tutorial");
  rclcpp::NodeHandle nh;
  rclcpp::Publisher pub = nh.advertise<PointCloud> ("points2", 1);
  pcl::io::loadPCDFile<pcl::PointXYZ> ("test.pcd", *cloud);

  PointCloud::Ptr msg (new PointCloud);
  msg->header.frame_id = "frame1";
  msg->height = cloud->height;
  msg->width = cloud->width;

  for (size_t i = 0; i < cloud->size (); i++) {
  x_cloud = cloud->points[i].x;
  y_cloud = cloud->points[i].y;
  z_cloud = cloud->points[i].z;
  msg->points.push_back (pcl::PointXYZ (x_cloud, y_cloud, z_cloud));
  }

  rclcpp::Rate loop_rate(4);


  while (nh.ok())
  {
    //msg->header.stamp = ros::Time::now().toNSec();
    pub.publish (msg);
    rclcpp::spinOnce ();
    loop_rate.sleep ();
  }
}

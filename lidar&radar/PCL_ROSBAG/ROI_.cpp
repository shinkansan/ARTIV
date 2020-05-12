#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>

#include <iostream>
#include <pcl/conversions.h>
#include <pcl/io/pcd_io.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/point_types.h>
#include <pcl/filters/passthrough.h>
#include <pcl/point_cloud.h>

//Filtering a PointCloud using a PassThrough filter

ros::Publisher pub;

typedef pcl::PointCloud<pcl::PointXYZ> point_cloud_t;

void cloud_cb (const sensor_msgs::PointCloud2& ros_pc)
{

    pcl::PCLPointCloud2 pcl_pc; // temporary PointCloud2 intermediary
    pcl_conversions::toPCL(ros_pc, pcl_pc);

    // Convert point cloud to PCL native point cloud
    point_cloud_t::Ptr input_ptr(new point_cloud_t());
    pcl::fromPCLPointCloud2(pcl_pc, *input_ptr);

    // ROI 만들기
    pcl::PassThrough<pcl::PointXYZ> sor;
    sor.setInputCloud(input_ptr);
    sor.setFilterFieldName ("y");
    sor.setFilterLimits (-1,1);
    
    point_cloud_t::Ptr cut_ptr(new point_cloud_t());
    sor.filter(*cut_ptr);
    
    // 다른 축 ROI 만들기
    pcl::PassThrough<pcl::PointXYZ> cut_;
    cut_.setInputCloud(cut_ptr);
    cut_.setFilterFieldName ("x");
    cut_.setFilterLimits (0,30);
    
    // Create output point cloud
    point_cloud_t::Ptr output_ptr(new point_cloud_t());

    // Run filter
    cut_.filter(*output_ptr);
    
    // Now covert output back from PCL native type to ROS
    sensor_msgs::PointCloud2 ros_output;
    pcl::toPCLPointCloud2(*output_ptr, pcl_pc);
    pcl_conversions::fromPCL(pcl_pc, ros_output);
    
    // Publish the data
    pub.publish(ros_output);
}


int main (int argc, char** argv)
{
    // Initialize ROS
    ros::init (argc, argv, "pcl_roi");
    ros::NodeHandle nh;

    // Create a ROS subscriber for the input point cloud
    ros::Subscriber sub = nh.subscribe("/velodyne_points_sampling", 1, cloud_cb);

    // Create a ROS publisher for the output point cloud
    pub = nh.advertise<sensor_msgs::PointCloud2>("/velodyne_points_roi", 1);

    // Spin
    ros::spin ();
}

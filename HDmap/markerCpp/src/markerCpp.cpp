#include <cstdio>
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "visualization_msgs/msg/marker.hpp"
#include "visualization_msgs/msg/marker_array.hpp"
#include "std_msgs/msg/color_rgba.hpp"
#include "geometry_msgs/msg/point.hpp"

#include <math.h>
#include <unistd.h>

using namespace std;

#define PI 3.14169265358979
#define num 101

double *linspace(double, double, int);

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  auto node = rclcpp::Node::make_shared("markerCpp");

  auto makerPub = node->create_publisher<visualization_msgs::msg::MarkerArray>("/cirMarker");    

  visualization_msgs::msg::MarkerArray viz_array_msg;
  visualization_msgs::msg::Marker marker_msg;
  visualization_msgs::msg::Marker text_marker_msg;

  	marker_msg.type = visualization_msgs::msg::Marker::CUBE;

	marker_msg.color.r = 0;
	marker_msg.color.g = 255;
	marker_msg.color.b = 0;
	marker_msg.color.a = 1.0;
	marker_msg.scale.x = 0.1;
	marker_msg.scale.y = 0.1;
	marker_msg.scale.z = 0.1;

	text_marker_msg.type = visualization_msgs::msg::Marker::TEXT_VIEW_FACING;
	text_marker_msg.header.frame_id = "map";
	text_marker_msg.color.r = 255;
	text_marker_msg.color.g = 255;
	text_marker_msg.color.b = 255;
	text_marker_msg.color.a = 1.0;

  //Sin wave plotter
	rclcpp::Rate rate(150000);
  double *theta;
  theta = linspace(0, 2*PI, num);
  double domain_x = 0.0;


	viz_array_msg.markers.clear();

  for (int iter = 0; iter < num; iter++){
  	double i = sin(theta[iter]);
  	cout << i << " " <<domain_x <<endl;
  	
  	marker_msg.header.frame_id = "map";
  	marker_msg.id = domain_x;
  	marker_msg.pose.position.x = domain_x/20;
  	marker_msg.pose.position.y = (double)i;
  	marker_msg.pose.position.z = 0.05;

  	string msg = to_string((int)domain_x);
  	
  	text_marker_msg.id =  domain_x + 1000;
  	text_marker_msg.text = msg;
  	text_marker_msg.scale.z = 0.09;
  	text_marker_msg.pose.position = marker_msg.pose.position;
  	text_marker_msg.pose.position.z += 0.06;

  	marker_msg.header.stamp = rclcpp::Clock().now();
  	text_marker_msg.header.stamp = marker_msg.header.stamp;

  	viz_array_msg.markers.push_back(marker_msg);
  	viz_array_msg.markers.push_back(text_marker_msg);



  	domain_x++;
  	rate.sleep();
  	sleep(1);
  	makerPub->publish(viz_array_msg);


  }
  viz_array_msg.markers.clear();

 
  }
  



  



double *linspace(double d0, double d1, int n)
{
 double *vetor,passo;

 vetor =(double*)calloc(n,sizeof(double));
 passo = (double)((d1-d0)/(n-1));

 for(int i=0;i<=n-2;++i)
 {
  vetor[i] = ( d0 + (i*passo) );
 }
 vetor[n-1] = d1;
 return(vetor);
}

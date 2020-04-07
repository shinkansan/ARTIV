#!/usr/bin/env python

import rclpy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

rclpy.init()
node = rclpy.create_node('OSMDrawer')
pub_line_min_dist =  node.create_publisher(Marker, 'mapPub3')


while rclpy.ok():
    marker = Marker()
    marker.header.frame_id = "osmMap"
    marker.type = marker.LINE_STRIP
    marker.action = marker.ADD

    # marker scale
    marker.scale.x = 1.

    # marker color
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 1.0
    marker.color.b = 0.0

    # marker orientaiton
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 0.0

    # marker position
    marker.pose.position.x = 0.0
    marker.pose.position.y = 0.0
    marker.pose.position.z = 0.0

    # marker line points
    marker.points = []
    # first point
    first_line_point = Point()
    first_line_point.x = 6720409.658899381
    first_line_point.y = 12574038.720874444
    first_line_point.z = 0.0
    marker.points.append(first_line_point)
    '''
    # second point
    second_line_point = Point()
    second_line_point.x = 6720411.658899381
    second_line_point.y = 12574039.720874444
    second_line_point.z = 0.0
	'''
    for i in range(0, 4):
    	first_line_point = Point()
    	first_line_point.x = 6720409.+i
    	first_line_point.y = 12574038.
    	first_line_point.z = 0.0
    	marker.points.append(first_line_point)

    '''
     first point
    first_line_point = Point()
    first_line_point.x = 6720409.658899381
    first_line_point.y = 12574038.720874444
    first_line_point.z = 0.0
    marker.points.append(first_line_point)
    # second point
    second_line_point = Point()
    second_line_point.x = 6720410.658899381
    second_line_point.y = 12574038.720874444
    second_line_point.z = 0.0
    marker.points.append(second_line_point)
    '''

    # Publish the Marker
    pub_line_min_dist.publish(marker)

    
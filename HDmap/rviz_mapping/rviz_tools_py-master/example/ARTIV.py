#! /usr/bin/python
# -*- coding: utf-8 -*-

# Python includes
import numpy
import random

# ROS includes
import roslib
import rospy
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3, Polygon
from tf import transformations # rotation_matrix(), concatenate_matrices()

import rviz_tools_py as rviz_tools


# Initialize the ROS Node
rospy.init_node('test', anonymous=False, log_level=rospy.INFO, disable_signals=False)

# Define exit handler
def cleanup_node():
    print("Shutting down node")
    markers.deleteAllMarkers()

rospy.on_shutdown(cleanup_node)


markers = rviz_tools.RvizMarkers('/map', 'visualization_marker')

#0. 디폴트 좌표계 (x, y, z축 보기 편하게)

def default_Axis():

    # Publish an axis using a numpy transform matrix
    T = transformations.translation_matrix((0,0,0))
    axis_length = 0.4
    axis_radius = 0.05
    markers.publishAxis(T, axis_length, axis_radius, 5.0) # pose, axis length, radius, lifetime

    P = Pose(Point(0.5,0,0),Quaternion(0,0,0,1))
    scale = Vector3(0.2,0.2,0.2)
    markers.publishText(P, 'x', 'white', scale, 5.0) # pose, text, color, scale, lifetime

    P = Pose(Point(0,0.5,0),Quaternion(0,0,0,1))
    scale = Vector3(0.2,0.2,0.2)
    markers.publishText(P, 'y', 'white', scale, 5.0) # pose, text, color, scale, lifetime

    P = Pose(Point(0,0,0.5),Quaternion(0,0,0,1))
    scale = Vector3(0.2,0.2,0.2)
    markers.publishText(P, 'z', 'white', scale, 5.0) # pose, text, color, scale, lifetime

#1. 사각형 어린이보호구역 (4개의 좌표값을 시계방향이나 반시계방향으로 입력해주세요.)

def rectangle_child_protected_area(a,b,c,d):

    # Publish a polygon using a ROS Polygon Msg
    polygon = Polygon()
    polygon.points.append(a)
    polygon.points.append(b)
    polygon.points.append(c)
    polygon.points.append(d)
    markers.publishPolygon(polygon, 'red', 0.02, 5.0) # path, color, width, lifetime

    center_x = (a.x + b.x + c.x + d.x) / 4.0
    center_y = (a.y + b.y + c.y + d.y) / 4.0
    center = Point(center_x, center_y, 0.3)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'Child Protection Area', markers.getRandomColor(), scale, 5.0) # pose, text, color, scale, lifetime 

#2. x축 방향으로 도로 만들기 (2차선 도로)
def make_x_direction_road(start,end):

    # Publish a rectangle between two points (thin, planar surface)
    # If the z-values are different, this will produce a cuboid
    markers.publishRectangle(start, end, 'black', 5.0)
	
    line_x1 = start.x
    line_x2 = end.x
    line_y = (start.y + end.y) / 2.0

    point1 = Point(line_x1,line_y,0)
    point2 = Point(line_x2,line_y,0) 
    width = 0.02
    markers.publishLine(point1, point2, 'yellow', width, 5.0)

#3. y축 방향으로 도로 만들기 (2차선 도로)
def make_y_direction_road(start,end):

    # Publish a rectangle between two points (thin, planar surface)
    # If the z-values are different, this will produce a cuboid
    markers.publishRectangle(start, end, 'grey', 5.0)
	
    line_y1 = start.y
    line_y2 = end.y
    line_x = (start.x + end.x) / 2.0

    point1 = Point(line_x,line_y1,0)
    point2 = Point(line_x,line_y2,0) 
    width = 0.02
    markers.publishLine(point1, point2, 'yellow', width, 5.0)

#4. x축 방향으로 만든 도로에 대한 과속방지턱 (2차선 도로) - 이 항목은 실제 도로에 대한 과속방지턱의 크기에 따라 함수 안의 depth값만 조정하면 실제 크기에 근사할 수 있음.
def speed_bump_x(point):

    # Publish a rotated plane using a numpy transform matrix
    radian = 0.523599 # 30도
    sin = 0.5
    cos = 0.866
    depth = 0.3
    width = 2.0

    R_y_1 = transformations.rotation_matrix(radian, (0,1,0)) # Rotate around y-axis by 0.3 radians
    T0_1 = transformations.translation_matrix((point.x + 0.5*cos*depth,point.y,0.5*sin*depth))
    T_1 = transformations.concatenate_matrices(T0_1, R_y_1)
    markers.publishPlane(T_1, depth, width, 'yellow', 5.0) # pose, depth, width, color, lifetime

    R_y_2 = transformations.rotation_matrix(-1*radian, (0,1,0)) # Rotate around y-axis by 0.3 radians
    T0_2 = transformations.translation_matrix((point.x - 0.5*cos*depth,point.y,0.5*sin*depth))
    T_2 = transformations.concatenate_matrices(T0_2, R_y_2)
    markers.publishPlane(T_2, depth, width, 'yellow', 5.0) # pose, depth, width, color, lifetime

    center = Point(point.x, point.y, sin*depth + 0.1)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'Speed Bump', 'white', scale, 5.0) # pose, text, color, scale, lifetime

#5. y축 방향으로 만든 도로에 대한 과속방지턱 (2차선 도로) - 색깔이 무조건 검은색으로 나오는 이슈 해결해야함.
def speed_bump_y(point):

    # Publish a rotated plane using a numpy transform matrix
    radian = 0.523599 # 30도
    sin = 0.5
    cos = 0.866
    depth = 0.3
    width = 2.0

    R_x_1 = transformations.rotation_matrix(radian, (1,0,0)) # Rotate around y-axis by 0.3 radians
    T0_1 = transformations.translation_matrix((point.x, point.y-0.5*cos*depth,0.5*sin*depth))
    T_1 = transformations.concatenate_matrices(T0_1, R_x_1)
    markers.publishPlane(T_1, width, depth, 'yellow', 5.0) # pose, width, depth, color, lifetime

    R_x_2 = transformations.rotation_matrix(-1*radian, (1,0,0)) # Rotate around y-axis by 0.3 radians
    T0_2 = transformations.translation_matrix((point.x,point.y+ 0.5*cos*depth,0.5*sin*depth))
    T_2 = transformations.concatenate_matrices(T0_2, R_x_2)
    markers.publishPlane(T_2, width, depth, 'yellow', 5.0) # pose, width, depth, color, lifetime

    center = Point(point.x, point.y, sin*depth + 0.1)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'Speed Bump', 'white', scale, 5.0) # pose, text, color, scale, lifetime

#6. 신호등
def traffic_light(point):

    # Publish a cylinder using a numpy transform matrix
    T = transformations.translation_matrix((point.x,point.y,point.z+0.5))
    markers.publishCylinder(T, 'white', 1.0, 0.2, 5.0) # pose, color, height, radius, lifetime

    center = Point(point.x, point.y, 1.1)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'Traffic Light', 'white', scale, 5.0) # pose, text, color, scale, lifetime

#7. 속도 측정기
def speed_meter(point):


    # Publish a sphere using a numpy transform matrix
    T = transformations.translation_matrix((point.x,point.y,point.z+0.5))
    scale = Vector3(0.5,0.5,0.5) # diameter
    color = [1,0,0] # list of RGB values (red)
    markers.publishSphere(T, color, scale, 5.0) # pose, color, scale, lifetime

    center = Point(point.x, point.y, 0.8)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, '30km/h Speed Limit!', 'red', scale, 5.0) # pose, text, color, scale, lifetime


# 실행예제

while not rospy.is_shutdown():


    default_Axis() #0.
    
    a = Point(1.0,-2.0,0.0)
    b = Point(-1.0,-2.0,0.0)
    c = Point(-1.0,-4.0,0.0)
    d = Point(1.0,-4.0,0.0)
    rectangle_child_protected_area(a,b,c,d) #1.

    start = Point(-3.0,-2.0,0.0)
    end = Point(7.0,-4.0,0.0)
    make_x_direction_road(start,end) #2.

    start = Point(-3.0,1.0,0.0)
    end = Point(-5.0,-2.0,0.0)
    make_y_direction_road(start,end) #3.

    point = Point(-2.5,-3.0,0.0)
    speed_bump_x(point) #4.

    point = Point(-4.0,-0.5,0.0)
    speed_bump_y(point) #5.

    point = Point(-5.5,-1.5,0.0)
    traffic_light(point) #6.

    point = Point(4.0,-1.7,0.0)
    speed_meter(point) #7.

    # Line:

    # Publish a line between two ROS Point Msgs
    point1 = Point(-2,-0.5,0)
    point2 = Point(-1.8,-0.5,0) 
    width = 0.02
    markers.publishLine(point1, point2, 'white', width, 5.0) # point1, point2, color, width, lifetime

    point1 = Point(-1.6,-0.5,0)
    point2 = Point(-1.4,-0.5,0) 
    width = 0.02
    markers.publishLine(point1, point2, 'white', width, 5.0) # point1, point2, color, width, lifetime

    point1 = Point(-1.2,-0.5,0)
    point2 = Point(-1,-0.5,0) 
    width = 0.02
    markers.publishLine(point1, point2, 'white', width, 5.0) # point1, point2, color, width, lifetime

    # Publish a line between two ROS Poses
    P1 = Pose(Point(-2,1.1,0),Quaternion(0,0,0,1))
    P2 = Pose(Point(2,1.1,0),Quaternion(0,0,0,1))
    width = 0.02
    markers.publishLine(P1, P2, 'red', width, 5.0) # point1, point2, color, width, lifetime

    # Publish a line between two numpy transform matrices
    T1 = transformations.translation_matrix((-2,1.2,0))
    T2 = transformations.translation_matrix((2,1.2,0))
    width = 0.02
    markers.publishLine(T1, T2, 'blue', width, 5.0) # point1, point2, color, width, lifetime


    # Path:

    # Publish a path using a list of ROS Point Msgs
    path = []
    path.append( Point(0,-0.5,0) )
    path.append( Point(1,-0.5,0) )
    path.append( Point(1.5,-0.2,0) )
    path.append( Point(2,-0.5,0) )
    path.append( Point(2.5,-0.2,0) )
    path.append( Point(3,-0.5,0) )
    path.append( Point(4,-0.5,0) )
    width = 0.02
    markers.publishPath(path, 'orange', width, 5.0) # path, color, width, lifetime


    # Plane / Rectangle:

    # Publish a rectangle between two points (thin, planar surface)
    # If the z-values are different, this will produce a cuboid
    point1 = Point(-1,0,0)
    point2 = Point(-2,-1,0) 
    markers.publishRectangle(point1, point2, 'black', 5.0)

    # Text:

    # Publish some text using a ROS Pose Msg
    P = Pose(Point(0,4,0),Quaternion(0,0,0,1))
    scale = Vector3(1,1,1)
    markers.publishText(P, 'ARTIV Visualization', 'white', scale, 5.0) # pose, text, color, scale, lifetime


    # Cube / Cuboid:

    # Publish a cube using a numpy transform matrix
    T = transformations.translation_matrix((-3,2.2,0))
    cube_width = 0.5 # cube is 0.5x0.5x0.5
    markers.publishCube(T, 'green', cube_width, 5.0) # pose, color, cube_width, lifetime

    center = Point(-3,2.2, 0.5)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'E1', 'white', scale, 5.0) # pose, text, color, scale, lifetime

    # Publish a cube using a ROS Pose Msg
    P = Pose(Point(-2,2.2,0),Quaternion(0,0,0,1))
    cube_width = 0.6
    markers.publishCube(P, 'blue', cube_width, 5.0) # pose, color, cube_width, lifetime

    center = Point(-2,2.2, 0.5)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'E2', 'white', scale, 5.0) # pose, text, color, scale, lifetime

    # Publish a cube using wrapper function publishBlock()
    P = Pose(Point(-1,2.2,0),Quaternion(0,0,0,1))
    cube_width = 0.7
    markers.publishBlock(P, 'orange', cube_width, 5.0) # pose, color, cube_width, lifetime

    center = Point(-1,2.2, 0.5)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'E3', 'white', scale, 5.0) # pose, text, color, scale, lifetime

    # Publish a cuboid using a numpy transform matrix
    T = transformations.translation_matrix((0.6,2.2,0))
    scale = Vector3(1.5,0.2,0.2)
    markers.publishCube(T, 'yellow', scale, 5.0) # pose, color, scale, lifetime

    center = Point(0.6,2.2, 0.5)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'E4', 'white', scale, 5.0) # pose, text, color, scale, lifetime


    # Publish a cuboid using a ROS Pose Msg
    P = Pose(Point(2.2,2.2,0),Quaternion(0,0,0,1))
    scale = Vector3(1.1,0.2,0.8)
    markers.publishCube(P, 'brown', scale, 5.0) # pose, color, scale, lifetime

    center = Point(2.2,2.2, 0.7)
    P = Pose(center,Quaternion(0,0,0,1))
    scale = Vector3(0.15,0.15,0.2)
    markers.publishText(P, 'E5', 'white', scale, 5.0) # pose, text, color, scale, lifetime

    # List of cubes:

    # Publish a set of cubes using a list of ROS Point Msgs
    points = []
    z_height = 0.1
    points.append(Point(3.5+0*0.2, 0.5, z_height)) # row 1
    points.append(Point(3.5+1*0.2, 0.5, z_height))
    points.append(Point(3.5+2*0.2, 0.5, z_height))
    points.append(Point(3.5+0*0.2, 0.5+1*0.2, z_height)) # row 2
    points.append(Point(3.5+1*0.2, 0.5+1*0.2, z_height))
    points.append(Point(3.5+2*0.2, 0.5+1*0.2, z_height))
    points.append(Point(3.5+0*0.2, 0.5+2*0.2, z_height)) # row 3
    points.append(Point(3.5+1*0.2, 0.5+2*0.2, z_height))
    points.append(Point(3.5+2*0.2, 0.5+2*0.2, z_height))
    points.append(Point(3.5+0*0.2, 0.5+2*0.2, z_height+0.2)) # 2nd layer
    diameter = 0.2-0.005
    markers.publishCubes(points, 'red', diameter, 5.0) # path, color, diameter, lifetime


    # Model mesh:

    # Publish STL mesh of box, colored green
    T = transformations.translation_matrix((3,1,0))
    scale = Vector3(1.5,1.5,1.5)
    mesh_file1 = "package://rviz_tools_py/meshes/box_mesh.stl"
    markers.publishMesh(T, mesh_file1, 'lime_green', scale, 5.0) # pose, mesh_file_name, color, mesh_scale, lifetime

    # Display STL mesh of bottle, re-scaled to smaller size
    P = Pose(Point(4,1,0),Quaternion(0,0,0,1))
    scale = Vector3(0.6,0.6,0.6)
    mesh_file2 = "package://rviz_tools_py/meshes/fuze_bottle_collision.stl"
    markers.publishMesh(P, mesh_file2, 'blue', scale, 5.0) # pose, mesh_file_name, color, mesh_scale, lifetime

    # Display collada model with original texture (no coloring)
    P = Pose(Point(5,1,0),Quaternion(0,0,0,1))
    mesh_file3 = "package://rviz_tools_py/meshes/fuze_bottle_visual.dae"
    mesh_scale = 4.0
    markers.publishMesh(P, mesh_file3, None, mesh_scale, 5.0) # pose, mesh_file_name, color, mesh_scale, lifetime


    rospy.Rate(1).sleep() #1 Hz

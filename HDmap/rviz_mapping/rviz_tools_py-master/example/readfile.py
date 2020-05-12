# Python includes
import numpy
import random
import math

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

# Publish a cube using a ROS Pose Msg
def unitCube(p):
    P = Pose(p, Quaternion(0,0,0,1))
    cube_width = 0.1
    markers.publishCube(P, 'red', cube_width, 5.0) # pose, color, cube_width, lifetime

class CordinatePoint():
	
	_latitude = 0.0
	_longitude = 0.0

	def __init__(self, latitude, longitude):
			self._latitude = latitude
			self._longitude = longitude

def read_data(file_name):

	data_list = []

	with open(file_name, "rt") as f:
		file_contents = f.read()

	data = file_contents.splitlines()
	n = len(data)
	for i in range(1,n):
		temp_list = data[i].split(",")
		temp_list1 = temp_list[6:9]
		data_list.append(temp_list1)
	return data_list
#		if i == 1:
#			relativeNullPoint = Point(latitude, longitude)
#		else:
#			temp_Point = Point(latitude, longitude)

def asRadians(degrees):
	return degrees * math.pi / 180

def getXYpos(relativeNullPoint, p):
	deltaLatitude = p._latitude - relativeNullPoint._latitude
	deltaLongitude = p._longitude - relativeNullPoint._longitude
	latitudeCircumference = 40075160 * math.cos(asRadians(relativeNullPoint._latitude))
	resultX = deltaLongitude * latitudeCircumference / 360
	resultY = deltaLatitude * 40008000 / 360
	return resultX, resultY

data = read_data('cordinate.txt')
relativeNullPoint = CordinatePoint(float(data[0][0]), float(data[0][1]))
z0 = float(data[0][2])
Point_list = []
for i in range(len(data)):
	if i ==0:
		x, y = getXYpos(relativeNullPoint, relativeNullPoint)
		z = float(data[i][2]) - z0
		temp_Point = Point(x,y,z)
		Point_list.append(temp_Point)
	else:
		P = CordinatePoint(float(data[i][0]), float(data[i][1]))
		x, y = getXYpos(relativeNullPoint, P)
		z = float(data[i][2]) - z0
		temp_Point = Point(x,y,z)
		Point_list.append(temp_Point)			

for i in range(len(Point_list)):
	print(Point_list[i])

while not rospy.is_shutdown():
	for i in range(len(Point_list)):
		unitCube(Point_list[i])


	rospy.Rate(1).sleep() #1 Hz




#!/usr/bin/env python

# CAN Listener : ROS Sub -> Processing -> Show data(easy data)
# Date : 2020.05.12

import rospy
import os
import time
import threading
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

from candb.msg import ERPmsg

old_rot = 0.0
new_rot = 0.0

data_enc0 = 0
data_enc1 = 0
data_enc2 = 0
data_enc3 = 0

cur_vel = 0.0

count = 1
x_vals = []
old_rots = []
new_rots = []
cur_vels = []


def callback(data):
	global old_time, old_rot, cur_vel, data_enc0, data_enc1, data_enc2, data_enc3

	data_enc0 = data.enc0
	data_enc1 = data.enc1
	data_enc2 = data.enc2
	data_enc3 = data.enc3

	os.system('clear')
	print("------------------------")
	print("ERP42 Information Table")
	print("Desired Speed : %.1f km/h" %(float(data.speed0)/10))
	printSteer(data.steer0, data.steer1)
	printEnc(new_rot)
	print("Real Velocity : %.1f km/h" %(cur_vel))
	print("Brake : %d percent" %((data.brake)/2))
	printGear(data.gear)
	print("------------------------")

def return_Rot_per_seconds():
	global old_rot, new_rot, cur_vel, data_enc0, data_enc1, data_enc2, data_enc3
	global count, x_vals, old_rots, new_rots, cur_vels
	timer = threading.Timer(0.1, return_Rot_per_seconds)
	timer.start()
	new_rot = returnRot(data_enc0, data_enc1, data_enc2, data_enc3)
	cur_vel = (new_rot - old_rot)*6/0.1
	old_rot = new_rot

def printSteer(st0, st1):
	if 230<=st1<=255:
		data = (255-st1)*256 + st0
		data = data/71
		print("Steer : -%d deg" %(data)) # Right Steer
	elif 0<=st1<100:
		data = st1*256 + st0
		data = data/71
		print("Steer : +%d deg" %(data)) # Left Steer

def printEnc(data):
	data = round(data, 1)
	if data < 0:
		print("Rotation : %.1f rot (Backward)" %(data))
	elif data >= 0:
		print("Rotation : %.1f rot (Forward)" %(data))


def returnRot(enc0, enc1, enc2, enc3):    # Required to be modified!!!! : Conditions are not certain
	if enc2 == 255 and enc3 == 255:
		data = (255-enc1)*256 + (256-enc0)
		data = -float(data)/100
	elif enc2 == 0 and enc3 == 0:
		data = enc1*256 + enc0
		data = float(data)/100
	return data   # return The number of rotation of wheel

def printGear(gear):
	A = ["Forward", "Neutral", "Backward"]
	print("Gear : %s" %(A[gear]))

def listener():
	return_Rot_per_seconds()
	rospy.init_node("ERP_info_print", anonymous=True)
	rospy.Subscriber("ERP42_Info", ERPmsg, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()

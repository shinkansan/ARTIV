#!/usr/bin/env python

# CAN Listener : ROS Sub -> Processing -> Show data
# DAta : 2020.05.12

import rospy
import os
import time
import threading
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

from candb.msg import ERPmsg

import time

class PID:
    def __init__(self, P=0.2, I=0.0, D=0.0, current_time=None):

        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.sample_time = 0.00
        self.current_time = current_time if current_time is not None else time.time()
        self.prev_time = self.current_time

        self.clear()

    def clear(self):
        # PID error와 계수 초기화
        self.SetPoint = 0.0

        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.prev_error = 0.0

        # Windup Guard
        '''
        self.int_error = 0.0
        self.windup_guard = 20.0
	'''
        self.output = 0.0

    def update(self, feedback_value, current_time=None):
        error = self.SetPoint - feedback_value

        self.current_time = current_time if current_time is not None else time.time()
        delta_time = self.current_time - self.prev_time
        delta_error = error - self.prev_error

        if (delta_time >= self.sample_time):
            self.PTerm = self.Kp * error
            self.ITerm += error * delta_time
            
            # Windup
            '''  
            if (self.ITerm < -self.windup_guard):
                self.ITerm = -self.windup_guard
            elif (self.ITerm > self.windup_guard):
                self.ITerm = self.windup_guard
            '''

            self.DTerm = 0.0
            if delta_time > 0:
                self.DTerm = delta_error / delta_time

            # Feedback current_time, error
            self.prev_time = self.current_time
            self.prev_error = error

            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)

    def setKp(self, p_gain):
        self.Kp = p_gain

    def setKi(self, i_gain):
        self.Ki = i_gain

    def setKd(self, d_gain):
        self.Kd = d_gain

    def setWindup(self, windup):
        self.windup_guard = windup

    def setSampleTime(self, sample_time):
        self.sample_time = sample_time

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
        desired = (float(data.speed0)/10)
	print("Desired Speed : %.1f km/h" %(desired))
	printSteer(data.steer0, data.steer1)
	printEnc(new_rot)
	print("Real Velocity : %.1f km/h" %(cur_vel))
	print("Brake : %d percent" %((data.brake)/2))
	printGear(data.gear)
	print("------------------------")
        pid = PID()
        pid.setSetPoint(desired)
        pid.update(cur_vel)

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

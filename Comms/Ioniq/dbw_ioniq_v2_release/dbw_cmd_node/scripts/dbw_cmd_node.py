#!/usr/bin/env python
import rospy
import can_communication
import os

from std_msgs.msg import String
from can_msgs.msg import Frame
from time import sleep
from std_msgs.msg import Int16


NODENAME = "dbw_cmd"
rootname = '/dbw_cmd'

subAccel = '/Accel'
subAngular = '/Angular'
subBrake = '/Brake'
subSteer = '/Steer'
subGear = '/Gear'


class subNode():
	def __init__(self):
		rospy.init_node(NODENAME, anonymous = True)
		rospy.Subscriber(rootname+subAccel, Int16, self.accelCallback)
		rospy.Subscriber(rootname+subAngular, Int16, self.angularCallback)
		rospy.Subscriber(rootname+subBrake, Int16, self.brakeCallback)
		rospy.Subscriber(rootname+subSteer, Int16, self.steerCallback)
		rospy.Subscriber(rootname+subGear, Int16, self.gearCallback)

		self.canSender = can_communication.rosPub()

		print("Command Node Subscriber is Ready...")

		try:
			rospy.spin()
		finally:
			rospy.shutdown()


	def accelCallback(self, msg):
		self.canSender.setAccelCMD(int(msg.data))
		pass

	def angularCallback(self, msg):
		self.canSender.setAngularSpeed(int(msg.data))
		pass

	def brakeCallback(self, msg):
		self.canSender.setBrakeCMD(int(msg.data))
		pass

	def steerCallback(self, msg):
		self.canSender.setSteerCMD(int(msg.data))
		pass

	def gearCallback(self, msg):
		self.canSender.setGearCMD(int(msg.data))
		pass

if __name__ == "__main__":
	dbw_control = subNode()
	dbw_control.canSender.data_pub()

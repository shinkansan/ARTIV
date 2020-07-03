#!/usr/bin/env python
import rospy
import copy
import threading

from std_msgs.msg import String
from can_msgs.msg import Frame
from time import sleep

class rosPub():
	def __init__(self):
		#rospy.init_node("Send_to_ioniq", anonymous=True)
		self.FramePub = rospy.Publisher('sent_messages', Frame, queue_size = 8)
		self.cmd_data = [0, 0, 0, 0]
		self.cmd_0 = 0
		self.cmd_1 = 0
		self.cmd_2 = 0
		self.cmd_3 = 0
		self.cmd_4 = 0
		self.cmd_5 = 0
		self.cmd_6 = 0
		self.cmd_7 = 0

		self.cmD_angularSpeed = 0
		self.cmD_1 = 0
		self.cmD_5 = 0

		self.framemsg = Frame()
		self.alive_cnt = 0
		
		dataThread = threading.Thread(target=self.data_pub)
		dataThread.start()


	def alive_update(self):  # for cmd : 0x150
		if self.alive_cnt == 256:
			self.alive_cnt = 0
		self.cmD_1 = self.alive_cnt
		self.cmD_5 = self.cmD_angularSpeed
		self.alive_cnt += 1


	def data_parser(self, data): # for cmd : 0x152
		self.cmd_0 = data[0]%256
		self.cmd_1 = data[0]/256
		self.cmd_2 = data[1]%256
		self.cmd_3 = data[1]/256
		self.cmd_4 = data[2]%256
		self.cmd_5 = data[2]/256
		self.cmd_6 = data[3]
		self.cmd_7 = 0


	def setAngularSpeed(self, value):
		if value > 255:
			value = 255
		elif value < 0:
			value = 0

		self.cmD_angularSpeed = value


	def setAccelCMD(self, value):
		if value > 2000:
			value = 2000
		if value < 650:
			value = 650

		self.cmd_data[0] = value


	def setBrakeCMD(self, value):
		if value > 25000:
			value = 25000
		if value < 0:
			value = 0

		self.cmd_data[1] = value 


	def setSteerCMD(self, value):
		if value > 440:
			value = 440
		elif value < -440:
			value = -440

		if value < 0:
			value = value & 0xffff

		self.cmd_data[2] = value
			

	def setGearCMD(self, value):
		if value in [0, 5, 6, 7]:
			self.cmd_data[3] = value


	def data_pub(self):
		while not rospy.is_shutdown():

			self.alive_update()
			#print("Hi!", self.cmD_1)
			self.framemsg.id = 0x150
			self.framemsg.is_rtr = 0
			self.framemsg.is_extended = 0
			self.framemsg.is_error = 0
			self.framemsg.dlc = 8
			bl = bytearray([0, self.cmD_1, 0, 0, 0, self.cmD_5, 0, 0])
			self.framemsg.data = str(bl)
			self.FramePub.publish(self.framemsg)

			self.data_parser(self.cmd_data)
			self.framemsg.id = 0x152
			self.framemsg.is_rtr = 0
			self.framemsg.is_extended = 0
			self.framemsg.is_error = 0
			self.framemsg.dlc = 8
			bl = bytearray([self.cmd_0, self.cmd_1, self.cmd_2, self.cmd_3, self.cmd_4, self.cmd_5, self.cmd_6, self.cmd_7])
			self.framemsg.data = str(bl)
			self.FramePub.publish(self.framemsg)
			sleep(0.001)


if __name__ == "__main__":
	rospub = rosPub()
	rospub.data_pub()

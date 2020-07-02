#!/usr/bin/env python
import rospy

from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from can_msgs.msg import Frame
from time import sleep


class rosSub():
	def __init__(self):
		rospy.init_node("dbw_ioniq_node", anonymous=True)
		self.frame_ok = 0.0
		self.JointPub = rospy.Publisher('Joint_state', JointState)
		self.FloatPub = rospy.Publisher('Ioniq_info', Float32MultiArray)
		self.aps_feedback = 0.0
		self.brake_act_feedback = 0.0 
		self.gear_position = 0.0
		self.steering_angle = 0.0
		self.estop_sw = 0.0
		self.auto_standby = 0.0
		self.apm_sw = 0.0
		self.asm_Sw = 0.0
		self.agm_sw = 0.0
		self.override_feedback = 0.0
		self.turn_sig = 0.0
		self.bps_feed = 0.0
		self.aps_feed = 0.0
		self.driver_belt = 0.0
		self.trunk = 0.0
		self.door_fl = 0.0
		self.door_fr = 0.0
		self.door_rl = 0.0
		self.door_rr = 0.0
		self.wheel_fl = 0.0
		self.wheel_fr = 0.0
		self.wheel_rl = 0.0
		self.wheel_rr = 0.0
		self.jointmsg = JointState()
		self.floatmsg = Float32MultiArray()
		self.floatmsg.data = [0.0]*24


	def filt_data(self, data1, data2):
		if data1 > 200:
			result = 0
		else:
			result = data1*255 + data2
		return result


	def data_parser(self, data):
		if data.dlc == 8:
			if data.id == 0x51:
				self.frame_ok = 1.0
				self.frame_data = bytearray(data.data)
				self.aps_feedback = self.filt_data(self.frame_data[1], self.frame_data[0])
				self.brake_act_feedback = self.filt_data(self.frame_data[3], self.frame_data[2])
				self.gear_position = self.frame_data[4]

				if self.frame_data[6] > 120:
					filtered_data = (255-self.frame_data[6])*255 + (255-self.frame_data[5])
				else:
					filtered_data = -(self.frame_data[6]*255 + self.frame_data[5])

				self.steering_angle = filtered_data/10
				sw_st = bin(self.frame_data[7])
				sw_st_list = [0]*8

				for i in range(len(sw_st)-2):
					sw_st_list[-1-i] = sw_st[-1-i]

				self.estop_sw = sw_st_list[-1]
				self.auto_standby = sw_st_list[-2]
				self.apm_sw = sw_st_list[-3]
				self.asm_Sw = sw_st_list[-4]
				self.agm_sw = sw_st_list[-6]

			elif data.id == 0x52:
				self.frame_ok = 1
				self.frame_data = bytearray(data.data)
				self.override_feedback = self.frame_data[0]
				self.turn_sig = self.frame_data[3]
				self.bps_feed = self.frame_data[4]
				self.aps_feed = self.frame_data[5]
				st = bin(self.frame_data[6])
				st_list = [0]*8

				for i in range(len(st)-2):
					st_list[-1-i] = st[-1-i]

				self.driver_belt = st_list[-3]
				self.trunk = st_list[-4]
				self.door_fl = st_list[-1]
				self.door_fr = st_list[-2]
				self.door_rl = st_list[-5]
				self.door_rr = st_list[-6]

			elif data.id == 0x54:
				self.frame_ok = 1
				self.frame_data = bytearray(data.data)
				self.wheel_fl = self.filt_data(self.frame_data[1], self.frame_data[0])/10
				self.wheel_fr = self.filt_data(self.frame_data[3], self.frame_data[2])/10
				self.wheel_rl = self.filt_data(self.frame_data[5], self.frame_data[4])/10
				self.wheel_rr = self.filt_data(self.frame_data[7], self.frame_data[6])/10

			else:
				self.frame_ok = 0


	def data_pub(self, data):
		self.data_parser(data)

		if self.frame_ok == 1:
			self.floatmsg.data[0] = self.aps_feedback         # default value = 630
			self.floatmsg.data[1] = self.brake_act_feedback
			self.floatmsg.data[2] = self.gear_position
			self.floatmsg.data[3] = self.steering_angle
			self.floatmsg.data[4] = self.estop_sw
			self.floatmsg.data[5] = self.auto_standby
			self.floatmsg.data[6] = self.apm_sw
			self.floatmsg.data[7] = self.asm_Sw
			self.floatmsg.data[8] = self.agm_sw
			self.floatmsg.data[9] = self.override_feedback
			self.floatmsg.data[10] = self.turn_sig
			self.floatmsg.data[11] = self.bps_feed
			self.floatmsg.data[12] = self.aps_feed
			self.floatmsg.data[13] = self.driver_belt
			self.floatmsg.data[14] = self.trunk
			self.floatmsg.data[15] = self.door_fl
			self.floatmsg.data[16] = self.door_fr
			self.floatmsg.data[17] = self.door_rl
			self.floatmsg.data[18] = self.door_rr
			self.floatmsg.data[19] = max([self.wheel_fl, self.wheel_fr, self.wheel_rl, self.wheel_rr])
			self.floatmsg.data[20] = self.wheel_fl
			self.floatmsg.data[21] = self.wheel_fr
			self.floatmsg.data[22] = self.wheel_rl
			self.floatmsg.data[23] = self.wheel_rr

			for i in range(0, 24):
				self.floatmsg.data[i] = float(self.floatmsg.data[i])

			self.jointmsg.name = ["Avg", "FL", "FR", "RL", "RR"]
			self.jointmsg.velocity = [max([self.wheel_fl, self.wheel_fr, self.wheel_rl, self.wheel_rr]), self.wheel_fl, self.wheel_fr, self.wheel_rl, self.wheel_rr]
		self.JointPub.publish(self.jointmsg)
		self.FloatPub.publish(self.floatmsg)


	def listener(self):
		rospy.Subscriber("/received_messages", Frame, self.data_pub)
		rospy.spin()


if __name__ == '__main__':
	rossub = rosSub()
	rossub.listener()

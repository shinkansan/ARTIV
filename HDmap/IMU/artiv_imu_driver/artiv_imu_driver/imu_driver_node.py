#!/usr/bin/env python3

#THANKS TO SHINKANSAN!!

import time
import rclpy
import numpy as np
import numpy
import math
from geometry_msgs.msg import Quaternion, Twist
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64
#from mav_msgs.msg import RollPitchYawrateThrust
#from auv_msgs.msg import RPY

from tf2_msgs.msg import TFMessage

import artiv_imu_driver.imu_driver as imu_driver

class ImuPublisherNode:
    def __init__(self):
        
        self.node = rclpy.create_node("imu_pub_node")
        
        #TODO 만약, imu 인식 실패시 roslog error 출력하기!
        # https://github.com/shinkansan/ARTIV/tree/master/integraedSW/log_example
        self.imuInst = imu_driver.GrabIMU380Data()
        self.imuInst.connect()

        #print(self.imuInst.data)

        #Params
        self.topic_name = "/imu"
        self.static_transform = [0, 0, 0, 0, 0, 0]
        self.frame_id = "base_imu_link"
        self.pub_imu = self.node.create_publisher(Imu, self.topic_name)

        self.imu_msg = Imu()
        self.imu_msg.orientation_covariance[0] = -1
        self.imu_msg.angular_velocity_covariance[0] = -1
        self.imu_msg.linear_acceleration_covariance[0] = -1

        self.rpy_roll = Float64()
        self.rpy_pitch = Float64()
        #self.rpy_yaw = Float64()

        self.pub_roll = self.node.create_publisher(Float64, "/roll")
        self.pub_pitch = self.node.create_publisher(Float64, "/pitch")
        #self.pub_yaw = self.node.create_publisher(Float64, "/yaw")

        self.current_time = self.node.get_clock().now()
        self.last_time = self.node.get_clock().now()

        self.seq = 0

        self.node.get_logger().info("Ready for publishing imu")

        self.degrees2rad = math.pi/180.0

        # Main while loop.
        while True:
            self.current_time = self.node.get_clock().now()
            self.imu = self.imuInst.get_packet()      

            if dict != type(self.imu):
                continue

            # publish imu message
            self.publish_info(self.imu, self.node)

            ''' tf 관계 및 tf를 출력해주는 static transform임, 
            if self.publish_transform:
                quaternion = self.quaternion_from_euler(self.static_transform[3]*self.degrees2rad,
                                                            self.static_transform[4]*self.degrees2rad,
                                                            self.static_transform[5]*self.degrees2rad)

                # send static transformation tf between imu and fixed frame
                self.odomBroadcaster_imu.sendTransform(
                    (self.static_transform[0], self.static_transform[1], self.static_transform[2]),
                    (quaternion[0], quaternion[1], quaternion[2], quaternion[3]),
                    rclpy.Time.now(), self.frame_name, self.fixed_frame
                )
		    '''

    def publish_info(self, imu, node):
        self.imu_msg.linear_acceleration.x = imu['xAccel']
        self.imu_msg.linear_acceleration.y = imu['yAccel']
        self.imu_msg.linear_acceleration.z = imu['zAccel']

        self.imu_msg.angular_velocity.x = imu['xRate']
        self.imu_msg.angular_velocity.y = imu['yRate']
        self.imu_msg.angular_velocity.z = imu['zRate']
        
        self.imu_msg.header.stamp =  node.get_clock().now().to_msg()
        self.imu_msg.header.frame_id = self.frame_id

        self.pub_imu.publish(self.imu_msg)

        deg_xRate = imu['xRate'] * 180 / math.pi
        deg_yRate = imu['yRate'] * 180 / math.pi
        deg_zRate = imu['zRate'] * 180 / math.pi

        R = math.atan(imu['yAccel']/math.sqrt(imu['xAccel']**2 + imu['zAccel']**2)) * 180 / math.pi
        P = math.atan(imu['xAccel']/math.sqrt(imu['yAccel']**2 + imu['zAccel']**2)) * 180 / math.pi
        Y = 0
        
        filtered_roll = R
        filtered_pitch = P

        alpha = 0.95

        filtered_roll = (alpha * (filtered_roll + (deg_yRate * 0.001))) + ((1-alpha) * R)
        filtered_pitch = (alpha * (filtered_pitch + (deg_xRate * 0.001))) + ((1-alpha) * P)
     
        self.rpy_roll.data = filtered_roll
        self.rpy_pitch.data = filtered_pitch

        self.pub_roll.publish(self.rpy_roll)
        self.pub_pitch.publish(self.rpy_pitch)

        q = self.quaternion_from_euler(self.rpy_roll.data, self.rpy_pitch.data, 0)
        self.imu_msg.orientation.x = q[0]
        self.imu_msg.orientation.y = q[1]
        self.imu_msg.orientation.z = q[2]
        self.imu_msg.orientation.w = q[3]

    def shutdown_node(self):
        rclpy.loginfo("Turning off node: robot_imu_publisher")

    def quaternion_from_euler(self, ai, aj, ak, axes='sxyz'):
        """Return quaternion from Euler angles and axis sequence.
        ai, aj, ak : Euler's roll, pitch and yaw angles
        axes : One of 24 axis sequences as string or encoded tuple
        
        Source: ROS tf transformations
        https://github.com/ros/geometry        
        """
        # axis sequences for Euler angles
        _NEXT_AXIS = [1, 2, 0, 1]

        # map axes strings to/from tuples of inner axis, parity, repetition, frame
        _AXES2TUPLE = {
            'sxyz': (0, 0, 0, 0), 'sxyx': (0, 0, 1, 0), 'sxzy': (0, 1, 0, 0),
            'sxzx': (0, 1, 1, 0), 'syzx': (1, 0, 0, 0), 'syzy': (1, 0, 1, 0),
            'syxz': (1, 1, 0, 0), 'syxy': (1, 1, 1, 0), 'szxy': (2, 0, 0, 0),
            'szxz': (2, 0, 1, 0), 'szyx': (2, 1, 0, 0), 'szyz': (2, 1, 1, 0),
            'rzyx': (0, 0, 0, 1), 'rxyx': (0, 0, 1, 1), 'ryzx': (0, 1, 0, 1),
            'rxzx': (0, 1, 1, 1), 'rxzy': (1, 0, 0, 1), 'ryzy': (1, 0, 1, 1),
            'rzxy': (1, 1, 0, 1), 'ryxy': (1, 1, 1, 1), 'ryxz': (2, 0, 0, 1),
            'rzxz': (2, 0, 1, 1), 'rxyz': (2, 1, 0, 1), 'rzyz': (2, 1, 1, 1)}

        _TUPLE2AXES = dict((v, k) for k, v in _AXES2TUPLE.items())

        try:
            firstaxis, parity, repetition, frame = _AXES2TUPLE[axes.lower()]
        except (AttributeError, KeyError):
            _ = _TUPLE2AXES[axes]
            firstaxis, parity, repetition, frame = axes

        i = firstaxis
        j = _NEXT_AXIS[i+parity]
        k = _NEXT_AXIS[i-parity+1]

        if frame:
            ai, ak = ak, ai
        if parity:
            aj = -aj

        ai /= 2.0
        aj /= 2.0
        ak /= 2.0
        ci = math.cos(ai)
        si = math.sin(ai)
        cj = math.cos(aj)
        sj = math.sin(aj)
        ck = math.cos(ak)
        sk = math.sin(ak)
        cc = ci*ck
        cs = ci*sk
        sc = si*ck
        ss = si*sk

        quaternion = numpy.empty((4, ), dtype=numpy.float64)
        if repetition:
            quaternion[i] = cj*(cs + sc)
            quaternion[j] = sj*(cc + ss)
            quaternion[k] = sj*(cs - sc)
            quaternion[3] = cj*(cc - ss)
        else:
            quaternion[i] = cj*sc - sj*cs
            quaternion[j] = cj*ss + sj*cc
            quaternion[k] = cj*cs - sj*sc
            quaternion[3] = cj*cc + sj*ss
        if parity:
            quaternion[j] *= -1

        return quaternion


def main():
    rclpy.init()
    start = ImuPublisherNode()

    #if error == "connection error" :
    #    start.node.get_logger().error("imu fuck")


if __name__ == '__main__':
    main()

   

#ros2 versio 
# CAN Listener : ROS Pub -> Show data
# Date : 2020.05.02

import rclpy
import os

from std_msgs.msg import String, Header, Float32MultiArray, MultiArrayDimension
from sensor_msgs.msg import JointState

def callback(data):
    t = ["APS Feedback", "Brake ACT Feedback", "Gear position Feedback", 
        "Steering angle Feedback", "Estop_sw", 
        "Auto-Standby", "APM S/W", "ASM S/W", "AGM S/W", 
        "Override Feedback", "Turn_Sig_Feed", "BPS_Feed", "APS_Feed",
        "Safety_belt(Driver)", "TRUNK", "Door_Front_Left", "Door_Front_Right", 
        "Door_Rear_Left", "Door_Rear_Right", "Avg_Speed",
        "Wheel_Speed_Front_Left", "Wheel_Speed_Front_Right", 
        "Wheel_Speed_Rear_Left", "Wheel_Speed_Rear_Right"]

    l = list(data.data)
    print("--------------------------------------")
    for i in range(len(t)):
        print('{0} : {1}'.format(t[i], l[i]))

    clear = lambda: os.system('clear')
    clear()


def listener():
    rclpy.init()
    node = rclpy.create_node('ioniq_sub_example')

    node.create_subscription(Float32MultiArray, 'Ioniq_info', callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

#!/usr/bin/env python

# CAN Listener : Serial Comms -> Processing -> Ros Pub
# Author : Yeo Ho Yeong (ARTIV), hoyeong23@dgist.ac.kr
# Date : 2020.07.07



import rospy
import serial

from serial import Serial
from std_msgs.msg import Float32MultiArray


class Car():
    def __init__(self, port):
        self.ser = Serial(port = port, baudrate = 115200)
        self.data_list = []

    def read_until(self, data):
        self.data_list = []
        while True:
            temp = self.ser.read()
            self.data_list.append(temp)
            if temp == "\n":
                val = bytearray(self.data_list)
                if len(val) == 18:
                    #print(len(val))
                    return val
                else:
                    pass


class control():
    def __init__(self, port_num):
        S = 83
        T = 84
        X = 88
        AorM = 1
        ESTOP = 0
        ETX0 = 13
        ETX1 = 10
        ALIVE = 0
        self.port_num = port_num
        self.DATA = bytearray(14)
        self.DATA[0] = S
        self.DATA[1] = T
        self.DATA[2] = X
        self.DATA[3] = AorM
        self.DATA[4] = ESTOP
        self.DATA[12] = ETX0
        self.DATA[13] = ETX1
        self.ALIVE = ALIVE
        self.car = Car(self.port_num)

    def open_serial(self):
        self.ser = serial.Serial(
            port = self.port_num,
            baudrate = 115200,
        )

    def send_data(self, SPEED, STEER, BRAKE, GEAR):
        if STEER >= 0:
            self.DATA[8] = STEER // 256
            print("DATA[8] :",self.DATA[8])
            self.DATA[9] = STEER % 256
            print("DATA[9]:", self.DATA[9])
        else:
            self.STEER = -STEER
            self.DATA[8] = 255 - self.STEER // 256
            self.DATA[9] = 255 - self.STEER % 256

        self.DATA[5] = GEAR
        self.DATA[6] = SPEED // 256
        self.DATA[7] = SPEED % 256
        self.DATA[10] = BRAKE
        self.DATA[11] = self.ALIVE
        self.ser.write(bytes(self.DATA))
        self.ALIVE = self.ALIVE + 1
        if self.ALIVE is 256:
            self.ALIVE = 0

    def receive_data(self):
        self.rx_DATA = self.car.read_until(self.DATA[13])
        return self.rx_DATA


class rosPub:
    def __init__(self):
        rospy.init_node('dbw_erp42_node')
        self.erppub = rospy.Publisher('ERP42_info', Float32MultiArray, queue_size = 7)
        self.estop = 0.0
        self.gear = 0.0
        self.speed = 0.0
        self.steer = 0.0
        self.brake = 0.0
        self.rotation = 0.0
        self.erpmsg = Float32MultiArray()
        self.erpmsg.data = [0.0]*7


    def data_parser(self, data):
    	data = bytearray(data)
        self.a_or_m = data[3]
        self.estop = data[4]
        self.gear = data[5]
        self.speed0 = data[6]
        self.speed1 = data[7]
        self.steer0 = data[8]
        self.steer1 = data[9]
        self.brake = data[10]
        self.enc0 = data[11]
        self.enc1 = data[12]
        self.enc2 = data[13]
        self.enc3 = data[14]

        if 120 < self.speed1 <= 255: # reverse speed (need /10 for km/h value)
            speed_val = (255-self.speed1)*256 + (255-self.speed0)
        elif 0 <= self.speed1 <= 120: # forward speed
            speed_val = self.speed1*256 + self.speed0

        self.speed = speed_val

        if 120 < self.steer1 <= 255: # right steer (need /71 for degree value)
            steer_val = (255-self.steer1)*256 + (255-self.steer0)
            steer_val = -steer_val
        elif 0 <= self.steer1 <= 120: # left steer
            steer_val = self.steer1*256 + self.steer0
            steer_val = steer_val
        self.steer = steer_val

        if 120 < self.enc3 <= 255: # reverse rotation (need /100 for rotation value)
            rot_val = (255-self.enc3)*256*256*256 + (255-self.enc2)*256*256 + (256-self.enc1)*256 + (256-self.enc0)
            rot_val = -rot_val
        elif 0 <= self.enc3 <= 120: # forward rotation
            rot_val = self.enc3*256*256*256 + self.enc2*256*256 + self.enc1*256 + self.enc0
        self.rot_val = round(rot_val/100.0, 1)


    def data_pub(self, data):
        self.data_parser(data)
        self.erpmsg.data[0] = self.a_or_m
        self.erpmsg.data[1] = self.estop
        self.erpmsg.data[2] = self.gear
        self.erpmsg.data[3] = self.speed
        self.erpmsg.data[4] = self.brake
        self.erpmsg.data[5] = self.steer
        self.erpmsg.data[6] = self.rot_val
        self.erppub.publish(self.erpmsg)

if __name__ == "__main__":
    erp = control("/dev/ttyUSB0")
    erp.open_serial()
    ErpPub = rosPub()
    while True:
        erp_data = erp.receive_data()
        try:
            ErpPub.data_pub(erp_data)
        except KeyboardInterrupt:
            print("You Put the Ctrl + C keys")
            break

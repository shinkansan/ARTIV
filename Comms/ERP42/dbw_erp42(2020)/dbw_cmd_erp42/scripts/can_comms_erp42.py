#!/usr/bin/env python

# Main file : dbw_cmd_erp42.py
# CAN Command Processor : Ros Sub -> Processing -> dbw_cmd_erp42.py
# Author : Yeo Ho Yeong (ARTIV), hoyeong23@dgist.ac.kr
# Date : 2020.07.07

import serial
import rospy
import threading

class Car():
    def __init__(self, port):
        self.ser = serial.Serial(port = port, baudrate = 115200)
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
        self.cmd_accel = 0
        self.cmd_brake = 0
        self.cmd_steer = 0
        self.cmd_gear = 0
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

        dataThread = threading.Thread(target=self.data_send)
        dataThread.start()

    def open_serial(self):
        self.ser = serial.Serial(
            port = self.port_num,
            baudrate = 115200,
        )

    def alive_update(self):
        self.ALIVE += 1
        if self.ALIVE == 256:
            self.ALIVE = 0

    def data_parser(self):
        if self.cmd_steer >= 0:
            self.DATA[8] = self.cmd_steer // 256
            self.DATA[9] = self.cmd_steer % 256
        else: # self.des_steer < 0
            self.cmd_steer = self.cmd_steer & 0xffff
            self.DATA[8] = self.cmd_steer // 256
            self.DATA[9] = self.cmd_steer % 256

        self.DATA[5] = self.cmd_gear
        self.DATA[6] = self.cmd_accel // 256
        self.DATA[7] = self.cmd_accel % 256
        self.DATA[10] = self.cmd_brake
        self.DATA[11] = self.ALIVE

    def data_send(self):
        while not rospy.is_shutdown():
            self.alive_update()
            self.data_parser()
            self.car.ser.write(bytes(self.DATA))

    def setAccelCMD(self, value):
        if value > 200:
            value = 200
        elif value < 0:
            value = 0

        self.cmd_accel = value

    def setBrakeCMD(self, value):
        if value > 200:
            value = 200
        elif value < 0:
            value = 0

        self.cmd_brake = value

    def setSteerCMD(self, value):
        if value > 2000:
            value = 2000
        elif value < -2000:
            value = -2000

        self.cmd_steer = value

    def setGearCMD(self, value): # 0 : forward, 1 : neutral, 2 : backward
        if value in [0, 1, 2]:
            self.cmd_gear = value

    def receive_data(self):
        self.rx_DATA = self.car.read_until(self.DATA[13])
        return self.rx_DATA


if __name__ == "__main__":
    erp = control("/dev/ttyUSB0")
    erp.open_serial()
    while True:
        erp_data = erp.receive_data()
        try:
            ErpPub.data_pub(erp_data)
        except:
            print("try again")

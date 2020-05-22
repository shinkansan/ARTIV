# CAN Listener : ROS Sub -> Processing -> Show data
# DAta : 2020.05.20

import serial
import threading
import keyboard
import os
from time import sleep

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

        self.des_vel = 0
        self.des_st = 0
        self.des_br = 0
        self.des_ge = 0

    def open_serial(self):
        self.ser = serial.Serial(
            port = self.port_num,
            baudrate = 115200,
        )

    def send_data(self, SPEED, STEER, BRAKE, GEAR):
        if STEER >= 0:
            self.DATA[8] = STEER // 256
            self.DATA[9] = STEER % 256
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

        #print((DATA))

    def receive_data(self):
        self.rx_DATA = self.car.read_until(self.DATA[13])
        #self.rx_SPEED = self.rx_DATA[6] + self.rx_DATA[7]
        #self.rx_STEER = self.rx_DATA[8] + (self.rx_DATA[9] * 256)
        #if self.rx_STEER > 32768:
        #    self.rx_STEER = self.rx_STEER - 65537
        return self.rx_DATA


    def keyboard_con(self):
        while True:
            if keyboard.is_pressed('w'):
                self.des_vel += 5
                self.des_br = 0
            elif keyboard.is_pressed('s'):
                self.des_br += 20
                self.des_vel -= 10
                if self.des_vel <= 0:
                    self.des_vel = 0
                if self.des_br >= 200:
                    self.des_br = 200
            elif keyboard.is_pressed('d'):
                self.des_st += 100
                if self.des_st >= 2000:
                    self.des_st = 2000
            elif keyboard.is_pressed('a'):
                self.des_st -= 100
                if self.des_st <= -2000:
                    self.des_st == -2000
            elif keyboard.is_pressed('n'):
                self.des_vel = 0
                self.des_st = 0
                self.des_br = 100
                self.des_ge = 0
            elif keyboard.is_pressed('m'):
                self.des_vel = 0
                self.des_st = 0
                self.des_br = 100
                self.des_ge = 2
            elif keyboard.is_pressed('q'):
                break
            sleep(0.1)



    def send_const(self):
        while True:
            try:
                
                os.system('clear')
                print('-----------------------------------------')
                print("Desired Velocity : %d" %(self.des_vel))
                print("Desired Steering : %d" %(self.des_st))
                print("Desired Brake : %d" %(self.des_br))
                print("Desired Gear : %d" %(self.des_ge))
                print('-----------------------------------------')
                self.send_data(self.des_vel, self.des_st, self.des_br, self.des_ge)
                if keyboard.is_pressed('q'):
                    break
            except:
                break



if __name__ == "__main__":
    erp = control("/dev/ttyUSB0")
    erp.open_serial()
    t1 = threading.Thread(target=erp.send_const)
    t2 = threading.Thread(target=erp.keyboard_con)
    t1.start()
    t2.start()
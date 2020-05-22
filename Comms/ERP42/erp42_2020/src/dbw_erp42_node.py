# CAN Listener : ERP42 -> Computer -> Ros Pub
# Date : 2020.05.11

import serial
import rospy
from candb.msg import ERPmsg


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
        rospy.init_node('ERP42_info')
        self.erppub = rospy.Publisher('ERP42_Info', ERPmsg)

    def data_parser(self, data):
        self.S_val = data[0]
        self.T_val = data[1]
        self.X_val = data[2]
        self.AorM = data[3]
        self.Estop = data[4]
        self.Gear = data[5]
        self.Speed0 = data[6]
        self.Speed1 = data[7]
        self.Steer0 = data[8]
        self.Steer1 = data[9]
        self.Brake = data[10]
        self.Enc0 = data[11]
        self.Enc1 = data[12]
        self.Enc2 = data[13]
        self.Enc3 = data[14]
        self.Alive = data[15]
        self.Etx0 = data[16]
        self.Etx1 = data[17]

    def data_pub(self, data):
        erpmsg = ERPmsg()

        self.data_parser(data)

        erpmsg.s_value = int(self.S_val) == 83
        erpmsg.t_value = int(self.T_val) == 84
        erpmsg.x_value = int(self.X_val) == 88
        erpmsg.aorm = int(self.AorM)
        erpmsg.e_stop = int(self.Estop) == 1
        erpmsg.gear = int(self.Gear)
        erpmsg.speed0 = int(self.Speed0)
        erpmsg.speed1 = int(self.Speed1)
        erpmsg.steer0 = int(self.Steer0)
        erpmsg.steer1 = int(self.Steer1)
        erpmsg.brake = int(self.Brake)
        erpmsg.enc0 = int(self.Enc0)
        erpmsg.enc1 = int(self.Enc1)
        erpmsg.enc2 = int(self.Enc2)
        erpmsg.enc3 = int(self.Enc3)
        erpmsg.alive = int(self.Alive)
        erpmsg.etx0 = int(self.Etx0) == 13
        erpmsg.etx1 = int(self.Etx1) == 10

        self.erppub.publish(erpmsg)

if __name__ == "__main__":
    des_vel = 0
    des_st = 0
    des_ge = 0
    des_br = 0
    erp = control("/dev/ttyUSB0")
    erp.open_serial()
    ErpPub = rosPub()
    while True:
        erp_data = erp.receive_data()
        try:
            ErpPub.data_pub(erp_data)
        except:
            print("try again")

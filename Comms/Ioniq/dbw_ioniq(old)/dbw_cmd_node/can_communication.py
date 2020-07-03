from canlib import canlib
from canlib import kvadblib
from canlib import Frame
import ctypes
import threading
import time
import rclpy

class sender():
    def __init__(self, ch, node):
        self.ch = ch

	## slot for 0x150 frame
        self.angular = 0
        self.data_150 = 0

	## Slot for CMD data, 0x152 frame
        self.accel = 500
        self.brake = 0
        self.gear = 0
        self.steer = 0
        self.data_152 = 0


        self.node = node


        print("Init Connection... send Alive CMD, Check Interface!")
        heartbeat = threading.Thread(target = self.AliveSender)
        heartbeat.start()


    def AliveSender(self):
        aliveVar = 0
        while True:
            try:
                if aliveVar == 256: aliveVar = 0
                self.data_150 += (aliveVar << 8)
                self.data_150 += (self.angular)


                frame = Frame(id_ = 0x150, data = (self.data_150).to_bytes(8, byteorder="little", signed=False))
                self.ch.write(frame)
                time.sleep(0.001)
                aliveVar += 1
                #print(frame)
                self.data_150 = 0
            except:
                self.node.get_logger().fatal("dbw_cmd_node : alive send failed!")
                exit(0);

    def setAngularSpeed(self, value):
        value = value if value < 255 else 255
        self.angular = value << 40
        #self.data = self.andbytes(self.data, (aliveVar << 40).to_bytes(8, byteorder="little", signed=False))

        frame = Frame(id_ = 0x150, data = (self.angular).to_bytes(8, byteorder="little", signed=False))
        #print(frame)
        try:
            self.ch.write(frame)
        except:
            self.node.get_logger().fatal("dbw_cmd_node : can send failed")
        time.sleep(0.001)


    def frame152(self):
        self.data_152 +=  self.accel
        self.data_152 +=  self.brake << 16
        #print('!', (self.steer & 0xffff) << 32)
        self.data_152 +=  (self.steer & 0xffff) << 32

        self.data_152 +=  self.gear << 48
        returnVal = self.data_152
        self.data_152 = 0
        #print(returnVal)
        return(returnVal)



    def setAccelCMD(self, value):
        value = value if value < 2000 else 2000
        self.accel = value
        frame = Frame(id_ = 0x152, data = (self.frame152()).to_bytes(8, byteorder="little", signed=False))
        #print(frame)
        try:
            self.ch.write(frame)
        except:
            self.node.get_logger().fatal("dbw_cmd_node : can send failed")
        time.sleep(0.001)

    def setBrakeCMD(self, value):
        value = value if value < 30000 else 30000
        self.brake = value
        frame = Frame(id_ = 0x152, data = (self.frame152()).to_bytes(8, byteorder="little", signed=False))
        try:
            self.ch.write(frame)
        except:
            self.node.get_logger().fatal("dbw_cmd_node : can send failed")
        time.sleep(0.001)

    def setSteerCMD(self, value):
        if abs(value) >= 440:
            Hsigned = -1 if value < 0 else 1
            value = Hsigned * 440
        self.steer = value
        frame = Frame(id_ = 0x152, data = (self.frame152()).to_bytes(8, byteorder="little", signed=False))
        try:
            self.ch.write(frame)
        except:
            self.node.get_logger().fatal("dbw_cmd_node : can send failed")
        time.sleep(0.001)

    def setGearCMD(self, value):
        cmd = [0, 5 ,6 ,7]
        if not value in cmd:
            #Rogue Data
            return -1
        #print(value)

        self.gear = value

        frame = Frame(id_ = 0x152, data = (self.frame152()).to_bytes(8, byteorder="little", signed=False))
        try:
            self.ch.write(frame)
        except:
            self.node.get_logger().fatal("dbw_cmd_node : can send failed")
        time.sleep(0.001)


if __name__ == "__main__":
    __CH_NUM__ = 0
    __BITRATE__ =  canlib.canBITRATE_500K

    try:
        ch = canlib.openChannel(__CH_NUM__, canlib.canOPEN_ACCEPT_VIRTUAL)
        ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
        ch.setBusParams(__BITRATE__)
        ch.setBusOutputControl(canlib.Driver.NORMAL)
        ch.busOn()
    except Exception as ex:
        print("Error occured", ex)

    test = sender(ch)
    test.setSteerCMD(500)

import rclpy
import os
import pprint
import threading

from std_msgs.msg import Int16MultiArray, Float32MultiArray, MultiArrayDimension
from sensor_msgs.msg import JointState
from canlib import canlib, kvadblib


__DB_NAME__ = 'ioniq_can_v6.dbc'
__CH_NUM__ = 0
__BITRATE__ = canlib.canBITRATE_500K
__TICK_TIME__ = 0


bitrates = {
    '1M': canlib.canBITRATE_1M,
    '500K': canlib.canBITRATE_500K,
    '250K': canlib.canBITRATE_250K,
    '125K': canlib.canBITRATE_125K,
    '100K': canlib.canBITRATE_100K,
    '62K': canlib.canBITRATE_62K,
    '50K': canlib.canBITRATE_50K,
    '83K': canlib.canBITRATE_83K,
    '10K': canlib.canBITRATE_10K,
}

class rosPub:
    def __init__(self):
        rclpy.init()
        self.node = rclpy.create_node("dbw_ioniq_node")
        self.JointPub = self.node.create_publisher(JointState, 'Joint_state')
        self.FloatPub = self.node.create_publisher(Float32MultiArray, 'Ioniq_info')


    def data_parser(self, data):
        self.AGMsw = data['AGMsw']
        self.APMsw = data['APMsw']
        self.APSFeedBack = data['APSFeedBack'] #APS Actuator
        self.APS_Feed = data['APS_Feed']
        self.ASMsw = data['ASMsw']
        self.AutoStandby = data['AutoStandby']
        self.BPS_Feed = data['BPS_Feed']
        self.BrakeACTFeedback = data['BrakeACTFeedback']
        self.Estop_sw = data['Estop']
        self.GearPosition = data['GearPostition']
        self.SteeringAngle = data['SteeringAngle']
        self.turnSig = data['TurnSig']
        self.VehicleSpeed = data['VehicleSpeed']
        self.WheelFL = data['WheelFL']
        self.WheelFR = data['WheelFR']
        self.WheelRL = data['WheelRL']
        self.WheelRR = data['WheelRR']
        self.overrideFeedback = data['overrideFeedback']
        self.DoorFL = data['DoorFL']
        self.DoorFR = data['DoorFR']
        self.DriverBelt = data['DriverBelt']
        self.Trunk = data['Trunk']
        self.DoorRL = data['DoorRL']
        self.DoorRR = data['DoorRR']


    def data_pub(self, data):
        if (len(data) < 24):
            print ("Vehicle Data is not ready... {%d}/24 set" %(len(data)))
            print("Wait...")
            return

        jointmsg = JointState()
        floatmsg = Float32MultiArray()
        floatmsg.data = [0]*24

        self.data_parser(data)
        floatmsg.data[0] = int(self.APSFeedBack)
        floatmsg.data[1] = int(self.BrakeACTFeedback)
        floatmsg.data[2] = int(self.GearPosition)
        floatmsg.data[3] = int(self.SteeringAngle)
        floatmsg.data[4] = int(self.Estop_sw)
        floatmsg.data[5] = int(self.AutoStandby)
        floatmsg.data[6] = int(self.APMsw)
        floatmsg.data[7] = int(self.ASMsw)
        floatmsg.data[8] = int(self.AGMsw)
        floatmsg.data[9] = int(self.overrideFeedback)
        floatmsg.data[10] = int(self.turnSig)
        floatmsg.data[11] = int(self.BPS_Feed)
        floatmsg.data[12] = int(self.APS_Feed)
        floatmsg.data[13] = int(self.DriverBelt)
        floatmsg.data[14] = int(self.Trunk)
        floatmsg.data[15] = int(self.DoorFL)
        floatmsg.data[16] = int(self.DoorFR)
        floatmsg.data[17] = int(self.DoorRL)
        floatmsg.data[18] = int(self.DoorRR)
        floatmsg.data[19] = max([self.WheelRR, self.WheelFR, self.WheelRL, self.WheelFL])/10
        floatmsg.data[20] = self.WheelFL/10
        floatmsg.data[21] = self.WheelFR/10
        floatmsg.data[22] = self.WheelRL/10
        floatmsg.data[23] = self.WheelRR/10

        jointmsg.name = ["Avg", "FL", "FR", "RL", "RR"]
        jointmsg.velocity = [floatmsg.data[0], self.WheelFL/10, self.WheelFR/10, self.WheelRL/10, self.WheelRR/10]
        # This for JointPub with JointState type
        self.JointPub.publish(jointmsg)
        self.FloatPub.publish(floatmsg)



class capsule:
    def __init__(self):
        self.dataCapsule = {}


    def manual_update(self, key, value):
        self.dataCapsule.update({str(key) : value})

    def db_update(self, db, frame):
        try:
            bmsg = db.interpret(frame)
        except kvadblib.KvdNoMessage:
            return
        for signal in bmsg:
            if signal.name == 'SteeringAngle':
                self.manual_update(signal.name, float(signal.value)/10)
            else:
                self.manual_update(signal.name, signal.value)


    def pprint(self):
        if (len(self.dataCapsule) <= 2): return
        pprint.pprint(self.dataCapsule)

    def __str__(self):
        return pprint.pfromat(dataCapsule)
    def __repr__(self):
        return pprint.pfromat(dataCapsule)


class canUtil:
    def __init__(self):
        self.rosPubClass = rosPub()
        if not self.setupCan():
            return

    def setupCan(self):
        try:
            self.db = kvadblib.Dbc(filename=__DB_NAME__)
            self.dbCap = capsule()
            self.ch = canlib.openChannel(__CH_NUM__, canlib.canOPEN_ACCEPT_VIRTUAL)
            self.ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
            self.ch.setBusParams(__BITRATE__)
            self.ch.busOn()
        except Exception as ex:
            self.rosPubClass.node.get_logger().fatal("dbw_ioniq_node : CAN Device Connect Fail!")
            print(ex)
            return 0

        return 1

    def receiveCan(self):
        ticktime = __TICK_TIME__
        timeout = 0.5
        tick_countup = 0
        if ticktime <= 0:
            ticktime = None
        elif ticktime < timeout:
            timeout = ticktime

        print("Working...")

        while True:
            try:

                frame = self.ch.read(timeout=int(timeout * 1000))
                #printframe(db, frame)
                self.dbCap.db_update(self.db, frame)
                #self.dbCap.pprint()
            except canlib.CanNoMsg:
                if ticktime is not None:
                    tick_countup += timeout
                    while tick_countup > ticktime:
                        print("tick")
                        tick_countup -= ticktime
            except KeyboardInterrupt:
                print("Stop.")
                break


            self.rosPubClass.data_pub(self.dbCap.dataCapsule)


    def printframe(self, db, frame):
        try:
            bmsg = db.interpret(frame)
        except kvadblib.KvdNoMessage:
            #print("<<< No message found for frame with id %s >>>" % frame.id)
            return
            pass

        msg = bmsg._message
        print(msg.name)
        if msg.comment:
            print(msg.comment)
        for bsig in bmsg:
            print(bsig.name + ':', bsig.value, bsig.unit)





if __name__ == "__main__":
    node = canUtil()
    nodeThread = threading.Thread(target = node.receiveCan)
    nodeThread.start()

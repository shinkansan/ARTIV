#!/usr/bin/env python
import rospy

from std_msgs.msg import String
from sensor_msgs.msg import JointState

from canDB.msg import Artivmsg
import os
from canlib import canlib, kvadblib
import pprint
import threading

__DB_NAME__ = 'cankingDB_ioniq_dgist_mod6.dbc'
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
        rospy.init_node('Ioniq_info')
        self.Artpub = rospy.Publisher('Ioniq_Info', Artivmsg)
        self.JointPub = rospy.Publisher('Joint_state', JointState)


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

    def data_pub(self, data):
        if (len(data) < 24):
            print ("Vehicle Data is not ready... {%d}/24 set" %(len(data)))
            print("Wait...")
            return


    	jointmsg = JointState()
    	artmsg = Artivmsg()

        self.data_parser(data)

        artmsg.AGM_Switch = int(self.AGMsw)
        artmsg.ASM_Switch = int(self.ASMsw)
        artmsg.APM_Switch = int(self.APMsw)
        artmsg.Estop_Switch = int(self.Estop_sw)
        artmsg.AutoStandby_Switch = int(self.AutoStandby)

        artmsg.Override_Feed = int(self.overrideFeedback)

        artmsg.APS_Feedback = self.APSFeedBack
        artmsg.Brake_ACT_Feedback = self.BrakeACTFeedback
        artmsg.Gear_position_Feedback = int(self.GearPosition)
        artmsg.Steering_angle_Feedback = self.SteeringAngle

        #artmsg.avgSpeed = (self.WheelRR + self.WheelRL + self.WheelFR + self.WheelRR)/4
        artmsg.avgSpeed = max([self.WheelRR, self.WheelFR, self.WheelRL, self.WheelFL])*0.1

        artmsg.lampSignal = int(self.turnSig)

        artmsg.BPS_Feed = self.BPS_Feed
        artmsg.APS_Feed = self.APS_Feed

        jointmsg.name = ["Avg", "FL", "FR", "RL", "RR"]
        jointmsg.velocity = [artmsg.avgSpeed, self.WheelFL*0.1, self.WheelFR*0.1, self.WheelRL*0.1, self.WheelRR*0.1]
        # This for JointPub with JointState type
        self.Artpub.publish(artmsg)
        self.JointPub.publish(jointmsg)



class capsule:
    def __init__(self):
        self.dataCapsule = {}
        

    def manual_update(self, key, value):
        self.dataCapsule.update({str(key) : value})

    def db_update(self, db, frame):
        try:
            bmsg = db.interpret(frame)
        except kvadblib.KvdNoMessage:
            #print("<<< No message found for frame with id %s >>>" % frame.id)
            return
        for signal in bmsg:
            if signal.name == 'SteeringAngle':
                self.manual_update(signal.name, float(signal.value)*-0.1)
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
            # give ROS param flag
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
            # ROS ERROR LOG
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

            except:
                pass
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

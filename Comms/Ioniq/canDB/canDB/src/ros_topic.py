#!/usr/bin/env python
import rospy

from std_msgs.msg import String
from sensor_msgs.msg import JointState
from can_msgs.msg import Frame
from canDB.msg import Artivmsg
import os
from canlib import canlib, kvadblib
import pprint
import ros_topic

__DB_NAME__ = 'artiv_canDB_Ioniq_v1.dbc'
__CH_NUM__ = 0
__BITRATE__ = canlib.canBITRATE_500K


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


def data_pub():
	rospy.init_node('Ioniq_info')
	Artpub = rospy.Publisher('Ioniq_Info', Artivmsg)
	JointPub = rospy.Publisher('Joint_state', JointState)

	jointmsg = JointState()
	artmsg = Artivmsg()

	while not rospy.is_shutdown():
		str = "something msg written in string"
		# This for infoPub whith String msg type
		# artmsg.WS_FL = 

		artmsg.avgSpeed = (artmsg.WS_FL + artmsg.WS_FR + artmsg.WS_RL + artmsg.WS_RR)/4

		jointmsg.name = [Avg, FL, FR, RL, RR]
		jointmsg.position = []
		jointmsg.velociy = [artmsg.avgSpeed, artmsg.WS_FL, artmsg.WS_FR, artmsg.WS_RL, artmsg.WS_RR]
		jointmsg.effort = []
		# This for JointPub with JointState type
		Artpub.publish(msg)

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


def setupCan():
    try:
        db = kvadblib.Dbc(filename=__DB_NAME__)
        dbCap = capsule()
        ch = canlib.openChannel(__CH_NUM__, canlib.canOPEN_ACCEPT_VIRTUAL)
        ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
        ch.setBusParams(__BITRATE__)
        ch.busOn()
    except Exception as ex:
        # ROS ERROR LOG
        print(ex)
        return 0

    return 1


if __name__ == "__main__":
	setupCan()
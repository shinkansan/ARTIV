from canlib import canlib
from canlib import kvadblib
from canlib import Frame
import threading
import rclpy, os
from rclpy.logging import LoggingSeverity
from std_msgs.msg import Float32
from std_msgs.msg import Int16
import can_communication


NODENAME = "dbw_cmd"
rootname = '/dbw_cmd'

subAccel = '/Accel'
subAngular = '/Angular'
subBrake = '/Brake'
subSteer = '/Steer'
subGear = '/Gear'

class subNode():
    def __init__(self):

        __CH_NUM__ = 0
        __BITRATE__ =  canlib.canBITRATE_500K

        rclpy.init()
        node = rclpy.create_node(NODENAME)

        try:
            ch = canlib.openChannel(__CH_NUM__, canlib.canOPEN_ACCEPT_VIRTUAL)
            ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
            ch.setBusParams(__BITRATE__)
            ch.setBusOutputControl(canlib.Driver.NORMAL)
            ch.busOn()
        except Exception as ex:
            node.get_logger().fatal("dbw_cmd_node : CAN Device Connect Error!!")
            print("Error occured :: ", ex, '\nprogram terminated')
            return

        accelSub = node.create_subscription(Int16,
        rootname+subAccel,
            self.accelCallback)
        angluarSub = node.create_subscription(Int16,
            rootname+subAngular,
            self.angularCallback)
        gearSub = node.create_subscription(Int16,
            rootname + subGear,
            self.gearCallback)
        steerSub = node.create_subscription(Int16,
            rootname + subSteer,
            self.steerCallback)
        brakeSub = node.create_subscription(Int16,
        rootname + subBrake,
            self.brakeCallback)

        self.canSender = can_communication.sender(ch)

        print("Node Sub ready")
        try:
            rclpy.spin(node)
        finally:
            node.destroy_node()
            rclpy.shutdown()


    def accelCallback(self, msg):
        #print('accel', msg.data, type(msg.data))
        self.canSender.setAccelCMD(int(msg.data))
        pass
    def angularCallback(self, msg):
        #print('angular', msg.data)
        self.canSender.setAngularSpeed(int(msg.data))
        pass
    def brakeCallback(self, msg):
        #print('brake', msg.data)
        self.canSender.setBrakeCMD(int(msg.data))
        pass
    def steerCallback(self, msg):
        #print('steer', msg.data, type(msg.data))
        self.canSender.setSteerCMD(int(msg.data))
        pass
    def gearCallback(self, msg):
        #print('gear', msg.data)
        self.canSender.setGearCMD(int(msg.data))
        pass



if __name__ == "__main__":
    dbw_control = subNode()

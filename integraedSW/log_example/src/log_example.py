## Log Test

'''
DEBUG = 10
ERROR = 40
FATAL = 50
INFO = 20
UNSET = 0
WARN = 30


You can get this enum from rqt /rosout topic
'''



import rclpy
import time

rclpy.init()
node = rclpy.create_node("rclpy_log_test")

while(1):
    node.get_logger().info("Info flagged")
    time.sleep(1)
    node.get_logger().debug("debug flagged")
    time.sleep(1)
    node.get_logger().warning("warning flagged")
    time.sleep(1)
    node.get_logger().error("error flagged")
    time.sleep(1)
    node.get_logger().fatal("fatal flagged")
    time.sleep(1)

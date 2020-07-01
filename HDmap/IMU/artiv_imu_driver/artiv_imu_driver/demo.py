"""
Demo for IMU380 Python driver
To use first connect an Aceinna 380 series product to computer with USB serial adaptor.
Created on 2017-12-31
@author: m5horton
"""
from imu380 import *

# Create driver instance 
imu = GrabIMU380Data()

# Start local log file
imu.start_log()

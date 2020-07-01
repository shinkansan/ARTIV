"""
Device Manager
Created 04/26/2018
@author: m5horton
"""

"""

"""

import serial
import string
import time
import sys
import glob
import imu380
import threading


class DeviceManager:
    def __init__(self, ws=False):
        '''Initialize and then start ports search and autobaud process
        '''
        self.imus = []
    
    def start(self):
        while 1:
            ports = self.find_ports()
            for port in ports:
                print(port)
                imu = imu380.GrabIMU380Data(ws=True)
                imu.port = port
                imu.autobaud([port])
                print('no success')            

    def find_ports(self):
        ''' Lists serial port names. Code from
            https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
            Successfully tested on Windows 8.1 x64, Windows 10 x64, Mac OS X 10.9.x / 10.10.x / 10.11.x and Ubuntu 14.04 / 14.10 / 15.04 / 15.10 with both Python 2 and Python 3.
            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        '''
        print('scanning ports')
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                print('Trying: ' + port)
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result


   

        

if __name__ == "__main__":
    manager = DeviceManager()
    manager.start()
    

#-*- coding:utf-8 -*-
# ====================================================== #
# Yonsei University - Seamless Transportation Laboratory #
# Ho Suk                                                 #
# sukho93@yonsei.ac.kr                                   #
# ====================================================== #

import threading
import serial # library download is needed, https://pypi.org/project/pyserial/

PORT = '/dev/ttyUSB0'
BAUD_RATE = 115200
PARITY = serial.PARITY_NONE
STOP_BITS = serial.STOPBITS_ONE

class SerialCommunicator(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = serial.Serial(port=PORT, baudrate=BAUD_RATE, parity=PARITY, stopbits=STOP_BITS)
        
        self.UTC_time = 0.0
        self.activity_status = ""
        self.latitude = 0.0
        self.latitude_NS_indicator = ""
        self.longitude = 0.0
        self.longitude_EW_indicator = ""
        self.speed_knot = 0.0
        self.compass_degree = None
        self.UTC_date = 0
        self.magnetic_variation = None
        self.magnetic_variation_EW_indicator = None
        
    def run(self):
        self._readPartialGNRMCData(self.ser)
        
    def _readEntireGNRMCData(self, ser):
        while True:
            try:
                line = str(ser.readline())
                line = line[2:] # discard b' at start and ' at end
                item_list = line.split(',')
                if item_list[0] == '$GNRMC':
                    self.UTC_time = float(item_list[1]) # hhmmss.sss
                    self.activity_status = item_list[2] # A : Active , V : Void
                    self.latitude = float(item_list[3]) # ddmm.mmmm
                    self.latitude_NS_indicator = item_list[4] # N : North, S : South
                    self.longitude = float(item_list[5]) # dddmm.mmmm
                    self.longitude_EW_indicator = item_list[6] # E : East, W : West
                    self.speed_knot = float(item_list[7]) # 1knot = 1.852km/h
                    if item_list[8] != '':
                        self.compass_degree = float(item_list[8]) # WGS-84 standard
                    else:
                        self.compass_degree = None
                    self.UTC_date = int(item_list[9]) # ddmmyy
                    if item_list[10] != '':
                        self.magnetic_variation = float(item_list[10]) # angle difference
                    else:
                        self.magnetic_variation = None
                    if item_list[11] != '':
                        self.magnetic_variation_EW_indicator = item_list[11]
                    else:
                        self.magnetic_variation_EW_indicator = None
            except (ValueError, IndexError):
                pass
            
    def _readPartialGNRMCData(self, ser):
        while True:
            try:
                line = str(ser.readline())
                line = line[2:] # discard b' at start and ' at end # -1
                item_list = line.split(',')
                if item_list[0] == '$GNRMC':
                    self.UTC_time = float(item_list[1]) # hhmmss.sss
                    self.activity_status = item_list[2] # A : Active , V : Void
                    self.latitude = float(item_list[3]) # ddmm.mmmm
                    self.longitude = float(item_list[5]) # dddmm.mmmm
                    self.speed_knot = float(item_list[7]) # 1knot = 1.852km/h
                    if item_list[8] != '':
                        self.compass_degree = float(item_list[8]) # WGS-84 standard
                    else:
                        self.compass_degree = None
                    self.UTC_date = int(item_list[9]) # ddmmyy
            except (ValueError, IndexError):
                pass
            
    # ================================================== #
    
    def getEntireGNRMCData(self):
        return self.UTC_time, self.activity_status, self.latitude, self.latitude_NS_indicator, self.longitude, self.longitude_EW_indicator, \
        self.speed_knot, self.compass_degree, self.UTC_date, self.magnetic_variation, self.magnetic_variation_EW_indicator
        
    def getPartialGNRMCData(self):
        return self.UTC_time, self.activity_status, self.latitude, self.longitude, self.speed_knot, self.compass_degree, self.UTC_date

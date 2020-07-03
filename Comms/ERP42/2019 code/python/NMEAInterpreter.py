#-*- coding:utf-8 -*-
# ====================================================== #
# Yonsei University - Seamless Transportation Laboratory #
# Ho Suk                                                 #
# sukho93@yonsei.ac.kr                                   #
# ====================================================== #

from SerialCommunicator import*

import math
import utm # library download is needed, https://pypi.org/project/utm/
import numpy as np

class NMEAInterpreter():
    def __init__(self):
        self.MySerialCommunicator = SerialCommunicator()
        self.MySerialCommunicator.start()
        
        self.index = -1
        
        self.status = None
        
        self.year = None
        self.month = None
        self.date = None
        
        self.hour = None
        self.minute = None
        self.second = None
        
        self.coordinate_x = None
        self.coordinate_y = None
        
        self.velocity_kmph = None
        self.velocity_mps = None
        
        self.compass_degree = None
        self.previous_compass_degree = 0.0
        self.compass_radian = None
        self.previous_compass_radian = 0.0
        
    # ================================================== #
        
    def convertDataUnit(self):
        UTC_time, activity_status, latitude, longitude, speed_knot, compass_degree, UTC_date = self.MySerialCommunicator.getPartialGNRMCData()
        self.status = self._convertActivityStatus(activity_status)
        self.year, self.month, self.date = self._convertDate(UTC_date)
        self.hour, self.minute, self.second = self._convertTime(UTC_time)
        self.coordinate_x, self.coordinate_y = self._convert2UTM(latitude, longitude)
        self.velocity_kmph, self.velocity_mps = self._convertVelocity(speed_knot)
        self.compass_degree = self._convert2Degree(compass_degree)
        
    # ================================================== #
        
    def _convertActivityStatus(self, activity_status):
        if activity_status == 'A':
            status = True
        else:
            status = False
        return status
        
    def _convertDate(self, UTC_date):
        date = int(UTC_date/10000)
        month = int((UTC_date - date * 10000)/100)
        year = UTC_date - date * 10000 - month * 100
        return year, month, date

    def _convertTime(self, UTC_time):    
        hour = int(UTC_time/10000)
        minute = int((UTC_time - hour * 10000)/100)
        second = UTC_time - hour * 10000 - minute * 100        
        return hour, minute, second
    
    def _convertLatitudeNLongitude(self, latitude, longitude):
        converted_latitude = int(latitude/100) + (latitude/100 - int(latitude/100))/0.6
        converted_longitude = int(longitude/100) + (longitude/100 - int(longitude/100))/0.6
        return converted_latitude, converted_longitude
        
    def _convert2UTM(self, latitude, longitude):
        converted_latitude = int(latitude/100) + (latitude/100 - int(latitude/100))/0.6
        converted_longitude = int(longitude/100) + (longitude/100 - int(longitude/100))/0.6
        UTM_x, UTM_y, _, _ = utm.from_latlon(converted_latitude, converted_longitude) # (x, y, zone number, zone letter)
        return UTM_x, UTM_y
        
    def _convertVelocity(self, speed_knot):
        velocity_kmph = speed_knot * 1.8520
        velocity_mps = speed_knot * 0.5144        
        return velocity_kmph, velocity_mps
        
    def _convert2Degree(self, compass_degree):
        if compass_degree == None:
            converted_compass_degree = self.previous_compass_degree
        else:
            converted_compass_degree = compass_degree
            self.previous_compass_degree = compass_degree
        return converted_compass_degree
        
    def _convert2Radian(self, compass_degree):
        if compass_degree == None:
            compass_radian = self.previous_compass_radian
        else:
            compass_radian = compass_degree * math.pi/180
            self.previous_compass_radian = compass_radian
        return compass_radian
        
    # ================================================== #
        
    def getConvertedDateNTime(self):
        return np.array([self.year, self.month, self.date, self.hour, self.minute, self.second], copy=False)

    def getConvertedData(self):
        return np.array([self.status, self.coordinate_x, self.coordinate_y, self.velocity_kmph, self.velocity_mps, self.compass_degree, self.compass_radian], copy=False)

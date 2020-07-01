"""
Logger for Aceinna 380/381 Series Products
Based on Azure Python SDK https://github.com/pyserial/pyserial
Created on 2017-11-01
@author: m5horton
"""

import io
import os
import random
import time
import uuid
import datetime
import json

from azure.storage.blob import AppendBlobService
from azure.storage.blob import ContentSettings

class LogIMU380Data:    
    def __init__(self):
        '''Initialize and create a blob with CSV extension
        '''
        self.name = 'data-' + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.csv'
        self.append_blob_service = AppendBlobService(account_name='navview', account_key='+roYuNmQbtLvq2Tn227ELmb6s1hzavh0qVQwhLORkUpM0DN7gxFc4j+DF/rEla1EsTN2goHEA1J92moOM/lfxg==', protocol='http')
        self.append_blob_service.create_blob(container_name='data', blob_name=self.name,  content_settings=ContentSettings(content_type='text/plain'))
        self.first_row = 0
        self.write_str = ''

    def log(self,data,odr_setting): 
        '''Buffers and then stores stream based on ODR.  Must buffer due to cloud write time.  
            Uses dictionary keys for column titles
        '''
        odr_rates = { 0: 0, 1 : 100, 2 : 50, 5 : 25, 10 : 20, 20 : 10, 25 : 5, 50 : 2 };
        delta_t = 1.0 / odr_rates[odr_setting]

        if not self.first_row:
            self.first_row = 1
            header = ''.join('{0:s},'.format(key) for key in data)
            header = header[:-1]
            header = 'sample,' + header
            header = header + '\r\n'
        else:
            header = ''
            self.first_row += 1

        
        str = ''
        for key in data:
            if key == 'BITstatus' or key == 'GPSITOW' or key == 'counter' or key == 'timeITOW':
                    str += '{0:d},'.format(data[key])
            else:
                    str += '{0:3.5f},'.format(data[key])

        str = str[:-1]
        str = '{0:5.2f},'.format(delta_t * (self.first_row - 1)) + str
        str = str + '\r\n'
        self.write_str = self.write_str + header + str

        if (self.first_row % 100 == 0):
            self.write_to_azure()

    def write_to_azure(self):
        '''Appends buffered CSV string to current Azure blob
        '''
        self.append_blob_service.append_blob_from_text('data',self.name, self.write_str)
        self.write_str = ''


    def close(self):
        '''Closes blob
        '''
        self.write_to_azure()
        self.name = ''

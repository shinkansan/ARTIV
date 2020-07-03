#-*- coding:utf-8 -*-
# ====================================================== #
# Yonsei University - Seamless Transportation Laboratory #
# Ho Suk                                                 #
# sukho93@yonsei.ac.kr                                   #
# ====================================================== #

from NMEAInterpreter import*

import time

def main():
    try:
        MyNMEAInterpreter = NMEAInterpreter()
            
        while True:
            MyNMEAInterpreter.convertDataUnit()
            time.sleep(0.01)
            print(MyNMEAInterpreter.getConvertedData())
    except Exception as ex:
        print(ex)
    finally:
        MyNMEAInterpreter.MySerialCommunicator.ser.close()
    
if __name__ == "__main__":
    main()

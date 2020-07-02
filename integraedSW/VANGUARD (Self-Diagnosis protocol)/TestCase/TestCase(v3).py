### 2020.06.26
"""
1. changed Thread to multiprocessing.Process
2. dealing with starting and ending point with duration
3. dealing with real-time plotting method of data 
"""

#TODO
'''
1. 시작과 종결 조건을 cmd_pub에 값이 들어올 때 부터로 바꾸기
2. writer timeout을 duration으로
'''
#import module

### ROS2 module
import rclpy
from rclpy.qos import qos_profile_default
from std_msgs.msg import Int16, String, Header, Float32MultiArray, MultiArrayDimension
from sensor_msgs.msg import JointState

### real-time concurrency module
import os
from multiprocessing import Process
import threading

### python module
import matplotlib.pyplot as plt
from datetime import datetime
import time


# 
###
callbackData = 0
current = 0

accelPub = 0
brakePub = 0
steerPub = 0 #not using now
gearPub = 0 #not using now

### TestCase Setting
testCase = 5
Loginterval = 0.00001
duration = 2 #(sec)
accelTestValMax = 2000
brakeTestValMax = 27000

##### subscribing dbw_ioniq topic
def callback(subscribed_topic):
    global callbackData, current
    current = time.time()
    callbackData = list(subscribed_topic.data)   

def listener(node):
    node.create_subscription(Float32MultiArray, '/Ioniq_info', callback)
    rclpy.spin(node)

##### publising dbw_cmd topic
def create_dbw_cmd_topic_publisher(target_node):
    global accelPub, brakePub, steerPub, gearPub
    accelPub = target_node.create_publisher(Int16, '/dbw_cmd/Accel', qos_profile_default)
    brakePub  = target_node.create_publisher(Int16, '/dbw_cmd/Brake', qos_profile_default)
    steerPub = target_node.create_publisher(Int16, '/dbw_cmd/Steer', qos_profile_default)
    gearPub = target_node.create_publisher(Int16, '/dbw_cmd/Gear', qos_profile_default)

##### writing the target topic of dbw_ioniq_node 
def FeedbackWriter(fobject, desiredVal, val='accel'):
    global callbackData, Loginterval, duration, current
    while(True):
        
        if current != 0 and type(callbackData) == list:
            break

    end = time.time() + duration
    
    if val=='accel':
        start = time.time()
        #while(int(callbackData[0]) <= desiredVal):
        while time.time() <= end:
            print(int(callbackData[0]), desiredVal)
            resultStr = f'{time.time()-start},{callbackData[0]},{callbackData[12]},{desiredVal}\n'
            fobject.write(resultStr)

            time.sleep(Loginterval)
        print('value reached!')
        fobject.close()

    elif val=='brake':
        start = time.time()
        while time.time() <= end:
        #while(int(callbackData[1]) <= desiredVal//10):
            print(int(callbackData[1]), desiredVal//10)
            resultStr = f'{time.time()-start},{callbackData[1]},{callbackData[11]},{desiredVal}\n'
            fobject.write(resultStr)

            time.sleep(Loginterval)
        print('value reached!')
        fobject.close()

# test each val at one time
def test(duration, val='accel', accel_val=0, brake_val=0, steer_val = 0, gear_val = 0):
 
    global current
    global accelPub
    global brakePub
    global steerPub
    global gearPub
    accel = Int16()
    brake = Int16()
    steer = Int16()
    gear = Int16()
    accel.data = 0
    brake.data = 0
    steer.data = 0
    gear.data = 0
    max_time_end = time.time() + duration
    if val == 'accel' or val == 'reset':  
        accelACT = int(accel_val)
        accel.data = accelACT
    if val == 'brake'or val == 'reset':
        brakeACT = int(brake_val)
        brake.data = brakeACT

    print('accelPub:', accel.data, 'brakePub:', brake.data)
    while True:
        if val == 'accel' or val == 'reset':
            accelPub.publish(accel)        
        if val == 'brake' or val == 'reset':
            brakePub.publish(brake)
        if val == 'steer' or val == 'reset':   
            steerPub.publish(steer)
        if val == 'gear' or val == 'reset':
            gearPub.publish(gear)
        	#current = time.time()
        #print(int(max_time_end - current), end = '-')
        if time.time() > max_time_end:
            break

    if val == 'reset':
        print('reset is done')
    else:
        print(f'Publishing {val} for test is Done')

    return 0
    '''
    brakeACT = int(brake_val)
    handle_set = int(steer_val)
    gear_set = int(gear_val)


    brake = Int16()
    steer = Int16()
    gear = Int16()

    accel.data = accelACT
    brake.data = brakeACT
    steer.data = handle_set
    gear.data = gear_set
    

    while True:
        brakePub.publish(brake)
        steerPub.publish(steer)
        accelPub.publish(accel)
        gearPub.publish(gear)
        current = time.time()
        if time.time() > max_time_end:
            break
    '''

def doTest():
    global testCase
    global duration
    global accelTestValMax
    global brakeTestValMax
    global callbackData
    # First Test Accel

    today = datetime.today().strftime("%Y.%m.%d.%H:%M:%S")        
    newDirectory = f"testCase.{today}"
    os.makedirs(newDirectory) 
    for tc in range(testCase):
        ### Give Input Commands on Thread!
        # test(duration, val='accel', accel_val=0, brake_val=0, steer_val = 0, gear_val = 0):

        print("Test Accel @", tc)
        testThread = threading.Thread(target = test, args=(duration, 'accel', accelTestValMax, 0, 0, 0,))
        testThread.daemon = True
        #testThread = Process(target = test, args=(duration, 'accel', accelTestValMax, 0, 0, 0,))
        testThread.start()
    
        # FeedbackWriter(fobject, testCase, desiredVal, val='accel'):
        
        fileWrite = open(f"{newDirectory}/accel_"+str(tc), 'w')
        FeedbackWriter(fileWrite, accelTestValMax, 'accel')
        testThread.join()


        # Reset
        test(0.1, 'reset')
        print('reset')
        time.sleep(0.5)

    # Second Test Brake
    for tc in range(testCase):
        ### Give Input Commands on Thread!
        # test(duration, val='accel', accel_val=0, brake_val=0, steer_val = 0, gear_val = 0):
    
        print("Test Brake @", tc)
        testThread = threading.Thread(target = test, args=(duration, 'brake', 0, brakeTestValMax ,0,0,))
        #testThread = Process(target = test, args=(duration, 'brake', 0, brakeTestValMax ,0,0,))
        testThread.daemon = True
        testThread.start()
    
        # FeedbackWriter(fobject, testCase, desiredVal, val='accel'):

        fileWrite = open(f"{newDirectory}/brake_"+str(tc), 'w')
        FeedbackWriter(fileWrite, brakeTestValMax, 'brake')
        testThread.join()

        # Reset
        test(0.1, 'reset')
        print('reset')
        time.sleep(0.5)



def main(target_node):

    global current
    global accelPub
    global brakePub
    global steerPub
    global gearPub
    global duration

    max_of_Accel = 2000
    max_of_Brake = 27000
    #max_of_Steer = 400
    #min_of_Steer = -400

    create_dbw_cmd_topic_publisher(target_node)

    ''' 
    time_interval = 0.1
    time_demand = 10 # second
    number_of_data = int(time_demand / time_interval)

    Accel_increase = int(max_of_Accel / number_of_data)
    Brake_increase = int(max_of_Brake / number_of_data)
    Steer_increase = int((max_of_Steer - min_of_Steer) / number_of_data)

    for i in range(number_of_data):
        test(time_interval, i * Accel_increase, i * Brake_increase)

    end = time.time()
    '''

    ### TestSection
    test(0.1, 'reset')
    time.sleep(1)
    doTest()

        



if __name__ == "__main__":
    rclpy.init()
    node = rclpy.create_node('self_diagnosis_testcase')

    listenThread = threading.Thread(target = listener, args = (node,))
    #listenThread = Process(target = listener, args = (node,))
    listenThread.daemon = True
    listenThread.start()

    os.system('cls' if os.name == 'nt' else 'clear') #clear screen in real time
    main(node)
    exit(2)

import rclpy
from rclpy.qos import qos_profile_default
import os
from geometry_msgs.msg import Twist
from std_msgs.msg import  Int16

from steamcontroller import SteamController
import sys, select, termios, tty

import threading

settings = termios.tcgetattr(sys.stdin)

msg = """
2020 ARTIV Ioniq Keyboard Drving Assist by Gwanjun Shin
---------------------------
Accel : 'w'
brake : 's'
fastBrake : 'x' More fast & Impact brake
Steer : Left : 'a' | Right : 'd'

Cruise Function Toggle : 'k'
Set +0.1km/h () : 'i'
Set -0.5km/h () : 'm'


anything else : emergency Stop

CTRL-C to quit

WARNING! Must operate with driver and more than one assist!
"""

joyBinding = {
    'accel' : (0),
    'brake' : (8500),
    'steer' : (0),
    'safetyTrig' : (0),
    'estop' : (0)

}


handle_set = 0
accelACT = 650

brakeACT = 8500
status = 0

accelACT_MAX = 1500
brakeACT_MAX = 20000
handle_set_MAX = 440

globalAngular = 0

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


def vels(speed,turn, accel, brake):
	return (f"currently:\tpropulsion rate {speed}\t handle set {turn}\n \t\t aceel : {accel}, brake { brake}")

def joyParse(_, callmsg):

    Angular_Speed = Int16()
    Angular_Speed.data = 50
    global joyBinding, globalAngular


    if callmsg.buttons != 134218496:
        if callmsg.buttons == 25166592:
            #Micro Control Mode
            
            accelACT_MAX = 1300
            brakeACT_MAX = 16000
            handle_set_MAX = 380
            Angular_Speed.data = 30
            globalAngular.publish(Angular_Speed)

            print('Micro Control Mode')
        else:
            accelACT_MAX = 1500
            brakeACT_MAX = 20000
            handle_set_MAX = 440
            print('Normal Control Mode')
            Angular_Speed.data = 90
            globalAngular.publish(Angular_Speed)

        if callmsg.lpad_y > 0:
            joyBinding['accel'] = (callmsg.lpad_y/32767) * accelACT_MAX
        else:
            joyBinding['brake'] = (callmsg.lpad_y/32767) * brakeACT_MAX * -1

        if callmsg.lpad_y == 0:
            joyBinding['accel'] = 0
            joyBinding['brake'] = 0

  
        joyBinding['steer'] = (callmsg.lpad_x/32767) * handle_set_MAX
        if joyBinding['brake'] > 12000 and abs(joyBinding['steer']) < 80:
            joyBinding['steer'] = 0


    if callmsg.ltrig == 255 and callmsg.rtrig == 255:
        joyBinding['safetyTrig'] = 1
    else:
        joyBinding['safetyTrig'] = 0
    
   

   
        

def joythread():
    sc = SteamController(callback=joyParse)
    sc.run()

def main(args=None):
    global accelACT, accelACT_MAX, brakeACT, brakeACT_MAX, joyBinding, handle_set, status, globalAngular

    rclpy.init()
    node = rclpy.create_node('teleop_twist_keyboard')
    accelPub = node.create_publisher(Int16, '/dbw_cmd/Accel', qos_profile_default)
    brakePub  = node.create_publisher(Int16, '/dbw_cmd/Brake', qos_profile_default)
    steerPub = node.create_publisher(Int16, '/dbw_cmd/Steer', qos_profile_default)
    angularPub = node.create_publisher(Int16, '/dbw_cmd/Angular', qos_profile_default)

    joystickThread = threading.Thread(target = joythread)
    joystickThread.start()

    Angular_Speed = Int16()
    Angular_Speed.data = 90
    angularPub.publish(Angular_Speed)
    
    globalAngular = angularPub


    just_toggle = 0
    cruise_speed = 0.0
    cruise_mode = 0
    propulsion_rate = ((accelACT/accelACT_MAX)-(brakeACT/brakeACT_MAX))/(2)*100

    try:
        print(msg)
        print(vels(propulsion_rate,handle_set, accelACT, brakeACT))
        while(1):
            accelACT = accelACT if accelACT <= accelACT_MAX else accelACT_MAX
            brakeACT = brakeACT if brakeACT <= brakeACT_MAX else brakeACT_MAX

            if abs(handle_set) >= handle_set_MAX:
                Hsigned = -1 if handle_set < 0 else 1
                handle_set = Hsigned * handle_set_MAX

            propulsion_rate = ((accelACT/accelACT_MAX)-(brakeACT/brakeACT_MAX))/(1)*100


            print('','='*30, sep='')
            if joyBinding['safetyTrig']:
                print("Joystick Override Mode!\n"*3)
                if just_toggle : 
                    os.system('play music_marimba_chord.wav &')
                    just_toggle = 0
                brakeACT = int(joyBinding['brake'])
                accelACT = int(joyBinding['accel'])
                handle_set = int(joyBinding['steer'])


            else:
                print("BRACE!! EMERGENCY STOP!!!\n"*3)
                just_toggle = 1
                if(brakeACT < 8400):
                    ###MUST be ON THREAD!!!!
                    os.system('''for k in {1..3};
                    do
                    play -nq -t alsa synth 0.2 sine 544;
                    sleep 0.03;
                    play -nq -t alsa synth 0.2 sine 544;
                    sleep 0.03;
                    play -nq -t alsa synth 0.2 sine 544;
                    sleep 0.03;
                    play -nq -t alsa synth 0.2 sine 544;
                    sleep 0.03;
                    done &''')
                brakeACT = 14000
                accelACT = 0

            print(vels(propulsion_rate,handle_set, accelACT, brakeACT))
            accel = Int16()
            brake = Int16()
            steer = Int16()

            accel.data = accelACT
            brake.data = brakeACT

            steer.data = handle_set
    
            brakePub.publish(brake)
            steerPub.publish(steer)
            accelPub.publish(accel)

            print('='*30)

            os.system('cls' if os.name == 'nt' else 'clear')
        
            
            
    except Exception as e:
        raise Exception(e)
        print(e)

    finally:
        accel = Int16()
        brake = Int16()
        steer = Int16()

        accel.data = 0
        brake.data = 8500
        steer = 0
	
	
        brakePub.publish(brake)
        accelPub.publish(accel)
        steerPub.publish(steer)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()

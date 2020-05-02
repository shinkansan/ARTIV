import rclpy
from rclpy.qos import qos_profile_default
import os
from geometry_msgs.msg import Twist
from std_msgs.msg import  Int16

import sys, select, termios, tty

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

moveBindings = {
		'a' : (-5), #deg
        'd' : (5), #deg
        'q' : (0)
	       }

speedBindings={
		'w' : (50), #APS_ACT Feedback
        's' : (1500), #Brake_ACT Feedback ~20000
        'x' : (5000), #Brake_ACT Feedback ~20000 (HIGH)
        'i' : (0.1), #km/h
        'm' : (-0.5) #km/h
	      }

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


def vels(speed,turn, accel, brake):
	return (f"currently:\tpropulsion rate {speed}\t handle set {turn}\n \t\t aceel : {accel}, brake { brake}")

def main(args=None):

    rclpy.init()
    node = rclpy.create_node('teleop_twist_keyboard')
    accelPub = node.create_publisher(Int16, '/dbw_cmd/Accel', qos_profile_default)
    brakePub  = node.create_publisher(Int16, '/dbw_cmd/Brake', qos_profile_default)
    steerPub = node.create_publisher(Int16, '/dbw_cmd/Steer', qos_profile_default)

   
    cruise_speed = 0.0
    cruise_mode = 0



    handle_set = 0
    accelACT = 650

    brakeACT = 8500
    status = 0

    accelACT_MAX = 4000
    brakeACT_MAX = 20000
    handle_set_MAX = 440

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

            print('='*30)
            key = getKey()
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\n\n\n\n','='*30, sep='')
            if key in moveBindings.keys():
                if key == "q" :
                    handle_set = 0
                handle_set += moveBindings[key]

            elif key in speedBindings.keys():
                if key == "w" :
                    brakeACT = 0
                    accelACT += speedBindings[key]
                if key == "s" :
                    accelACT = 650
                    brakeACT += speedBindings[key]
                if key == "x" :
                    accelACT = 0
                    brakeACT += speedBindings[key]

                if (status == 14):
                    print(msg)
                    status = (status + 1) % 15
            else:
                print("BRACE!! EMERGENCY STOP!!!\n"*3)
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
                brakeACT = brakeACT_MAX

                if (key == '\x03'):
                	break

            print(vels(propulsion_rate,handle_set, accelACT, brakeACT))
            accel = Int16()
            brake = Int16()
            steer = Int16()

            accel.data = accelACT
            brake.data = brakeACT

            steer.data = handle_set
            print(steer.data)
            brakePub.publish(brake)
            steerPub.publish(steer)
            accelPub.publish(accel)
            
    except Exception as e:
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

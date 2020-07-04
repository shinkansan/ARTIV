import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

import rclpy
from rclpy.qos import qos_profile_default
import os
from geometry_msgs.msg import Twist
from std_msgs.msg import  Int16
from sensor_msgs.msg import JointState
import threading
import time
import termios
import sys
import tty
import select

settings = termios.tcgetattr(sys.stdin)

velocity = 0


def velCallback(msg):
    global velocity
    print("execute")
    #print('velocity', msg.velocity[0])
    velocity = msg.velocity[0]
    print(velocity)
    pass

def execute(node_):
    print("execute")
    velSub = node_.create_subscription(JointState,
            "/Joint_state",
            velCallback)
    rclpy.spin(node_)



def main(args=None):
    global velocity
    
    rclpy.init()
    node = rclpy.create_node('PID_visual')

    thread_velo = threading.Thread(target=execute, args=(node,))
    thread_velo.start()
    print("thread start")

# y축에 표현할 값을 반환해야하고 scope 객체 선언 전 선언해야함.
def insert():
    global velocity
    value = velocity
    return value 


class Scope(object):
    
    def __init__(self,
                 ax,fn,
                 xmax=10,ymax =10,
                 xstart=0, ystart=0,
                 title='Title',xlabel='X value',ylabel='Y value'):
        
        self.xmax = xmax #x축 길이
        self.xstart = xstart #x축 시작점
        self.ymax = ymax #y축 길이
        self.ystart = ystart #y축 시작점

        # 그래프 설정
        self.ax = ax 
        #self.ax.set_xlim((self.xstart,self.xmax))
        #self.ax.set_ylim((self.ystart,self.ymax))
        self.ax.set_xlim((self.xstart,self.xmax))
        self.ax.set_ylim((self.ystart, 1000))
        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

        self.x = [0] # x축 정보 
        self.y = [0] # y축 정보
        self.value = 0 # 축 값
        self.fn = fn
        self.line, = ax.plot([],[])

        self.ti = time.time() #현재시각
        print("초기화 완료")

    # 그래프 설정
    def update(self, i):
        # 시간차
        tempo = time.time()-self.ti
        self.ti = time.time() #시간 업데이트
        
        # 값 넣기
        self.value = insert()# y값 함수 불러오기
        self.y.append(self.value) #y값 넣기
        self.x.append(tempo + self.x[-1]) #x값 넣기
        self.line.set_data(self.x,self.y)

        # 화면에 나타낼 x축 범위 업데이트
        if self.x[-1] >= self.xstart + self.xmax :
            #전체 x값중 반을 화면 옆으로 밀기
            self.xstart = self.xstart + self.xmax/2
            self.ax.set_xlim(self.xstart,self.xstart + self.xmax)

            self.ax.figure.canvas.draw()

        return (self.line, )


fig, ax = plt.subplots()
ax.grid(True)


# 객체 생성
scope = Scope(ax,insert, ystart = 0, ymax = 10)
main()
# update 매소드 호출
ani = animation.FuncAnimation(fig, scope.update,interval=10,blit=True)
plt.show()

import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from subprocess import Popen, PIPE
import threading
import rclpy  #run this file in python3
from std_msgs.msg import *

form_class = uic.loadUiType("ROSTopicViewer.ui")[0]

rclpy.init()
node = rclpy.create_node('list_all_topics')



class rosTopicInfo(QThread):
    def __init__(self, selectedItem, sec=0, parent=None):
        QThread.__init__(self)
        self.main = parent
        self.isRun = True
        self.item = rclpy.create_node('topic_pub')
        self.selectedItem = selectedItem.split(' ')
    
    def __del__(self):
        print("Command Job Done")
        self.wait()

    @pyqtSlot()
    def run(self):
        if self.isRun:
            self.sub = self.item.create_subscription(
                eval(str(eval(self.selectedItem[1])[0]).split('/')[-1]),       ### sensormsg . eval 
                self.selectedItem[0],
                self.sub_callback)
            rclpy.spin(self.item)
        else:
            pass

    def sub_callback(self, msg):
        myWindow.echoTopic.addItem(msg.data)


class MyWindow(QMainWindow, form_class):
    send_comm_request = pyqtSignal(str)
    proc_kill=pyqtSignal()

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.viewTopics.clicked.connect(self.viewTopicList)
        self.playBtn.clicked.connect(self.playTopic)
        self.stopBtn.clicked.connect(self.stopTopic)      
        

    def viewTopicList(self):
        global node
        self.topicList.clear()
        topics = node.get_topic_names_and_types()
        for topic in topics:
            if topic[0]!='/rosout' and topic[0]!='/parameter_events':
                self.topicList.addItem(topic[0] +' ' + str(topic[1]))
    
    @pyqtSlot()
    def playTopic(self):
        if self.topicList.currentItem()==None:
            self.echoTopic.clear()
            self.echoTopic.addItem("Select Topic First!")
        else:
            self.echoTopic.clear()
            selectedItem = self.topicList.currentItem().text()
            print(selectedItem)

            self.rosTopicInfo_class = rosTopicInfo(selectedItem)
            self.rosTopicInfo_class.isRun = True
            self.rosTopicInfo_class.start()

    @pyqtSlot()
    def stopTopic(self):
        try:
        if self.rosTopicInfo_class.isRunning():
            self.rosTopicInfo_class.isRun = False
            self.rosTopicInfo_class.item.destroy_node()
            self.rosTopicInfo_class.quit()
            self.echoTopic.addItem("\nThreding is Finished")
        except:
            self.echoTopic.clear()
            self.echoTopic.addItem('No topic is playing')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    global myWindow
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import PyQt5
from PyQt5 import *
import rclpy
from rcl_interfaces.msg import Log
from PyQt5.QtWidgets import * #PyQt import
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5 import QtMultimedia
from PyQt5.QtCore import Qt, QUrl
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import datetime
import threading
import time

form_window = uic.loadUiType("logalert.ui")[0]
alert_window = uic.loadUiType("alertScreen.ui")[0]

header_serverity = 0
header_comment = 1
header_time = 2
header_loc = 3
blank_toggle = 1
fatalList = []
aSshow = 1

class Stack(list):
    push = list.append

    def is_empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        return self[-1]
fatalList = Stack()

class alertScreen(QMainWindow, alert_window):

    def center(self): #for load ui at center of screen
        frameGm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.pushButton.clicked.connect(self._exit)

        self.setStyleSheet("background-color:  #efefef;"
                      "border-style: solid;"
                      "border-width: 9px;"
                      "border-color: #ff4444;"
                      "border-radius: 3px")

        self.label.setStyleSheet("color: black;"
                      "border-style: None;"
                      "border-width: 2px;"
                      "border-color: #FA8072;"
                      "border-radius: 3px")

        self.listWidget.setStyleSheet("color: balck;"
                      "border-style: solid;"
                      "border-width: 2px;"
                      "border-color: #000000;"
                      "border-radius: 3px")
        self.pushButton.setStyleSheet("color: balck;"
                      "border-style: solid;"
                      "border-width: 2px;"
                      "border-color: #000000;"
                      "border-radius: 3px")

        timer = QtCore.QTimer(self)
        timer.setInterval(500)
        timer.timeout.connect(self.blank)

        timer.start()


    def blank(self):
        global blank_toggle
        if(blank_toggle):
            self.setStyleSheet("background-color:  #efefef;"
                          "border-style: solid;"
                          "border-width: 20px;"
                          "border-color: #ff4444;"
                          "border-radius: 2px")
            blank_toggle = 0
        else:
            self.setStyleSheet("background-color:  #efefef;"
                          "border-style: solid;"
                          "border-width: 20px;"
                          "border-color: #ffbb33;"
                          "border-radius: 2px")
            blank_toggle = 1
        self.updateList()

    def updateList(self):
        global fatalList
        if fatalList:
            item = fatalList.pop()
            self.listWidget.addItem(str(item[1]) + " : " + str(item[3]))

    def _exit(self):
        global aSshow
        aSshow = 1
        self.hide()



class logAlert(QMainWindow, form_window):
    def center(self): #for load ui at center of screen
        frameGm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['내용', '심각도', '발생', '시간'])

        self.rosSub_class = rosSub()
        self.rosSub_class.start()
        self.rosSub_class.data.connect(self.addRowandSet)

        '''
        playlist = QMediaPlaylist()
        print(os.path.join(os.getcwd(), "warning_fx.mp3"))
        url = QUrl.fromLocalFile(os.path.join(os.getcwd(), "warning_fx.mp3"))
        playlist.addMedia(QMediaContent(url))
        #playlist.setPlaybackMode(QMediaPlaylist.Loop)

        player = QMediaPlayer()
        player.setVolume(100)
        player.setPlaylist(playlist)

        self.pushButton_2.clicked.connect(player.play)

        player.play()
        '''
        filename = 'warning_fx.mp3'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        media = QtCore.QUrl.fromLocalFile(fullpath)
        content = QtMultimedia.QMediaContent(media)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        self.pushButton_2.clicked.connect(player.play)

        #header_item = QTableWidgetItem("추가")
        #header_item.setBackground(Qt.red) # 헤더 배경색 설정 --> app.setStyle() 설정해야만 작동한다. self.table.setHorizontalHeaderItem(2, header_item)
        #self.tableWidget.setHorizontalHeaderItem(2, header_item)
    def putIcon(self, severity):
        iconList = ['SP_MessageBoxCritical',
                    'SP_MessageBoxInformation',
                    'SP_MessageBoxQuestion',
                    'SP_MessageBoxWarning',
                    ]
        if severity == 1 or severity == 10:
            #Debug
            return self.style().standardIcon(getattr(QStyle, iconList[2])), "DEBUG", Qt.white
            pass
        elif severity == 2 or severity == 20:
            #INFO
            return self.style().standardIcon(getattr(QStyle, iconList[1])), "INFO", Qt.white
            pass
        elif severity == 4 or severity == 30:
            #WARN
            return self.style().standardIcon(getattr(QStyle, iconList[3])), "WARNING", Qt.yellow
            pass
        elif severity == 8 or severity == 40:
            #ERROR
            return self.style().standardIcon(getattr(QStyle, iconList[0])), "ERROR", Qt.darkRed
            pass
        elif severity == 16 or severity == 50:
            #FATAL
            return  self.style().standardIcon(getattr(QStyle, iconList[0])), "FATAL", Qt.magenta
            pass
        elif severity == 0:
            #UNSET
            return ""
            pass


    def addRowandSet(self, _data):
        global aSshow
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count+1)
        serverity = self.putIcon(_data[0])[1]
        _data[2] = serverity

        if _data[2] == "FATAL":
            global aSshow
            self.fatalCollector(_data)
            if aSshow:

                self.aS = alertScreen()
                self.aS.show()
                aSshow = 0

        meesage = QTableWidgetItem(_data[1])
        meesage.setIcon(self.putIcon(_data[0])[0])
        serverity = QTableWidgetItem(_data[2])
        serverity.setBackground(self.putIcon(_data[0])[2])
        self.tableWidget.setItem(row_count, 0, meesage)
        self.tableWidget.setItem(row_count, 1, serverity)
        self.tableWidget.setItem(row_count, 2, QTableWidgetItem(_data[3]))
        self.tableWidget.setItem(row_count, 3, QTableWidgetItem(_data[4]))


        #
        #self.tableWidget.setColumnWidth(1, 380)
        #self.tableWidget.setColumnWidth(2, 150)
        #self.tableWidget.setColumnWidth(3, 320)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setColumnWidth(0, 635)
        self.tableWidget.scrollToBottom()

    def fatalCollector(self, data):
        global fatalList
        fatalList.append(data)



class rosSub(QThread):
    data = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        rclpy.init()
        self.node = rclpy.create_node("log_alert")

    def run(self):
        self.node.create_subscription(Log, '/rosout', self.callback)

        rclpy.spin(self.node)



    def callback(self, msg):

        temp_data = [None] * 5
        temp_data[0] = msg.level
        temp_data[1] = msg.msg
        #temp_data[2] = str(msg.stamp)
        temp_data[4] = str(datetime.datetime.now())[5:]
        temp_data[3] = str(msg.name) + ":" +str(msg.line)

        self.data.emit(temp_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    logAlert_form = logAlert()
    logAlert_form.show()
    app.exec_()

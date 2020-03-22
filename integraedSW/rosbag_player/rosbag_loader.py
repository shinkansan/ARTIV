import sys
import os
import subprocess
from select import select
from subprocess import Popen, PIPE
import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import *
import threading
import time

form_class = uic.loadUiType("rosbag.ui")[0]

class getCommand(QObject):
    term_output = pyqtSignal(str)
    
    def __init__(self, sec=0, parent=None):
        super(getCommand, self).__init__()
        self.main = parent
        self.working = True
        self.comms = ""
    
    def __del__(self):
        print("Command Job Done")
       
    def run(self):
        pass
        
    def getComms(self, command):
        self.process = Popen(command, stdout=PIPE, shell = True, executable="/bin/bash", bufsize=1)
        self.lineCount =0
        while self.working:
            line = self.process.stdout.readline().rstrip().decode("utf-8")     
            if not line:
                print('Blank')
                self.lineCount -= 1
                if self.lineCount <= -3:
                    self.term_output.emit("EOL")
                    print("Killed")
                    print(self.process.pid)
                    self.process.kill()
                    break
            else:           
                self.lineCount += 1
                self.term_output.emit(line)
            print(line)
        self.process.kill()    
    

    @pyqtSlot(str)
    def request(self, msg):
        self.comms = msg
        print('get request' ,msg)
        self.getComms(self.comms)

    @pyqtSlot()
    def killProc(self):
        print("Killed", self.process.pid)
        self.process.kill()

class getCpuUsage(QThread):
    commands = "grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }'"
    commands2 = """awk '/MemFree/ { print $2/1024/1024 }' /proc/meminfo"""
    cpu_output = pyqtSignal(float)
    mem_output = pyqtSignal(float)
    
    def __init__(self, sec=0, parent=None):
        QThread.__init__(self)
        self.main = parent
        self.working = True
        self.comms = ""
        
    
    def __del__(self):
        print("Command Job Done")
        self.wait()
       
    @pyqtSlot()
    def run(self):
        while True:
            pipe = subprocess.Popen(self.commands, shell=True, executable="/bin/bash", stdout=subprocess.PIPE).stdout
            output = pipe.read().decode("utf-8")     
            self.cpu_output.emit(float(output))

            pipe2 = subprocess.Popen(self.commands2, shell=True, executable="/bin/bash", stdout=subprocess.PIPE).stdout
            output2 = pipe2.read().decode("utf-8")   
   
            self.mem_output.emit(float(output2))
        pass
        

class rosBagInfo(QObject):
    sig_data = pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        
    @pyqtSlot()
    def getRosInfo(self, command):
        pipe = subprocess.Popen(command, shell=True, executable="/bin/bash", stdout=subprocess.PIPE).stdout
        output = pipe.read().decode("utf-8")
        self.sig_data.emit(output)


class TimerMessageBox(QMessageBox):
    def __init__(self, timeout=3, parent=None):
        super(TimerMessageBox, self).__init__(parent)
        self.setWindowTitle("Opening ROSBAG File")
        self.time_to_wait = timeout
        self.setText("This task can take few seconds...")
        self.setStandardButtons(QMessageBox.NoButton)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()

    def changeContent(self):
        self.setText("This task can take few seconds...")
        self.time_to_wait -= 1
        if self.time_to_wait <= 0:
            self.close()

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()

class MyWindow(QMainWindow, form_class):
    send_comm_request = pyqtSignal(str)
    proc_kill = pyqtSignal()

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.aboutbox)
        self.pushButton.clicked.connect(self.openFileNamesDialog)
        self.listWidget.itemSelectionChanged.connect(self.bagSelect)
        self.playBtn.clicked.connect(self.playBag)
        self.stopBtn.clicked.connect(self.stopPlay)

        self.Bagworker = rosBagInfo()
        self.worker_thread = QThread()
        self.Bagworker.moveToThread(self.worker_thread)
        self.worker_thread.start()


        self.commTh = getCommand(parent=self)
        self.commTh.term_output.connect(self.textBrowser_2.append)
        self.send_comm_request.connect(self.commTh.request)
        self.proc_kill.connect(self.commTh.killProc)        
        self.commThread = QThread()
        self.commTh.moveToThread(self.commThread)
        self.commThread.start()

        self.getCpuUsage_class = getCpuUsage()
        self.getCpuUsage_class.start()
        self.getCpuUsage_class.cpu_output.connect(self.progressBar.setValue)
        self.getCpuUsage_class.mem_output.connect(self.progressBar_2.setValue)
        
    def aboutbox(self):
        QMessageBox.about(self, "About", "DGIST ARTIV ROSBAG Player - Shinkansan")

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            for fileN in files:
                self.listWidget.addItem(fileN)

    def bagSelect(self):
        bagDir = [bag.text() for bag in self.listWidget.selectedItems()][0]
        command = "source /opt/ros/melodic/setup.bash && rosbag info " + str(bagDir)
       
        print(bagDir) #http://kyounan-kim.blogspot.com/2012/04/qlistwidget-item-python.html
        
        self.Bagworker.sig_data.connect(self.updateRosInfo)
        self.Bagworker.getRosInfo(command)
        

        waitDialog = TimerMessageBox()
        waitDialog.show()
    
    @pyqtSlot()
    def playBag(self):
        bagDir = [bag.text() for bag in self.listWidget.selectedItems()][0]
        commands = "source /opt/ros/melodic/setup.bash && rosbag play -q " + bagDir

        self.send_comm_request.emit(str(commands))

    @pyqtSlot()
    def stopPlay(self):
        self.proc_kill.emit()
              
    @pyqtSlot(str)
    def updateRosInfo(self, infoStr):
        self.textBrowser.setPlainText(infoStr)

    @pyqtSlot(str)
    def updateTermOutput(self, msg):
        self.textBrowser_2.append(msg)  

        
        
        
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


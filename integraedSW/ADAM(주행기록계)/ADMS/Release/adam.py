import sys
from PyQt5.QtWidgets import * #PyQt import
from PyQt5.QtGui import *
from PyQt5 import uic
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import pics_rc
import cryptography
from cryptography.fernet import Fernet
import rclpy
from std_msgs.msg import String
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Image
import numpy as np
login_form = uic.loadUiType("adam-login2.ui")[0]
main_form = uic.loadUiType("adam-main.ui")[0]



class loginWindow(QMainWindow, login_form):

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
		self.setWindowFlags(Qt.WindowStaysOnTopHint)

		self.commandLinkButton.clicked.connect(self.loginBtn)
		self.lineEdit_2.returnPressed.connect(self.credentialCheck)
		


	def loginBtn(self):
		self.credentialCheck()
			
			

	def credentialCheck(self, id=None, pwd=None):
		self.id = id if id else self.lineEdit.text()
		self.pwd = pws if pwd else self.lineEdit_2.text()
		credDb = {"201811093" : ["gwanjunshin", "신관준", "201811093"]}
		try:
			if credDb.get(self.id)[0] == self.pwd:
				self.mW = mainWidnow(credDb.get(self.id))
				self.mW.show()
				self.hide()
				return 1
			else:
				self.label_7.setText("Wrong Passwords")
				return 0
		except Exception as ex:
			self.label_7.setText(f"Invalid Input\n{ex}")
			return 0

	



class mainWidnow(QMainWindow, main_form):

	def center(self): #for load ui at center of screen
		frameGm = self.frameGeometry()
		screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
		centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

	def __init__(self, userInfo):    
		super().__init__() 
		self.setupUi(self)
		self.center()
		self.saveDialog.clicked.connect(self.saveFileDialog)
		self.logout.clicked.connect(self.logoutBtn)
		self.label.setText(self.label.text() + userInfo[1])
		self.label_5.setText(self.label_5.text() + userInfo[2])

		self.adms_subscriber_class = adms_subscriber()
		self.adms_subscriber_class.start()
		self.adms_subscriber_class.sig_wheel.connect(self.wheel_speed)

	def saveFileDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
		if fileName:
		    print(fileName)

	def logoutBtn(self):
		'''
		TODO
		1. is it recording? (is it driving?)
		'''
		self.logWin = loginWindow()
		self.logWin.show()
		self.adms_subscriber_class.quit()
		
		self.hide()

	@pyqtSlot(list)
	def wheel_speed(self, msg):
		tot_speed = np.mean(msg[:4])
		fl, fr, rl, rr, _, _ = msg
		self.rl_speed.setText("RL :" + str(round(rl, 2)))
		self.fl_speed.setText("FL :" + str(round(fl, 2)))
		self.fr_speed.setText("FR :" + str(round(fr, 2)))
		self.rr_speed.setText("RR :" + str(round(rr, 2)))
		self.lcdNumber.display(int(tot_speed))



	
class adms_subscriber(QThread):
	sig_wheel = pyqtSignal(list)

	def __init__(self):
		super().__init__()
		try:
			rclpy.init(args=None)
		except:
			raise Exception("Init 실패, 다시시도 해주세요")

		self.node = rclpy.create_node("ADMS")
		

	def __del__(self):
		print("Command Job Done")
		rclpy.shutdown()
		self.wait()
		self.quit()
		self.wait()
		self.quit()

    
	def run(self):
			sub2 = self.node.create_subscription(
				JointState, 
				'/vehicle/joint_states', 
				self.joint_callback)

			rclpy.spin(self.node)

	def joint_callback(self, msg : JointState):
		self.sig_wheel.emit(list(msg.velocity))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    logWin = loginWindow()
    logWin.show()
    app.exec_()
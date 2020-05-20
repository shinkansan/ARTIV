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
from authManager import authentication_server
login_form = uic.loadUiType("adam-login2.ui")[0]
main_form = uic.loadUiType("adam-main.ui")[0]

glNode = 0

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
		self.lineEdit_2.textChanged.connect(self.autoCheck)

		self.update_auth.clicked.connect(self.updateAuth)
		self.authManager = authentication_server()

		self.pushButton_1.clicked.connect(self.btn_1)
		self.pushButton_2.clicked.connect(self.btn_2)
		self.pushButton_3.clicked.connect(self.btn_3)
		self.pushButton_4.clicked.connect(self.btn_4)
		self.pushButton_5.clicked.connect(self.btn_5)
		self.pushButton_6.clicked.connect(self.btn_6)
		self.pushButton_7.clicked.connect(self.btn_7)
		self.pushButton_8.clicked.connect(self.btn_8)
		self.pushButton_9.clicked.connect(self.btn_9)
		self.pushButton_0.clicked.connect(self.btn_0)
		self.pushButton_10.clicked.connect(self.btn_b)


		try:

			temp = np.load('./adms_user_db.npz', allow_pickle=True)
			self.userDB = temp['db'].item()

		except Exception:
			QMessageBox.warning(self, "인증 DB 가져오기 실패", "로그인을 하기위해서는 인증DB 갱신을 꼭 해주세요.", QMessageBox.Ok)


	def loginBtn(self):
		self.credentialCheck()

	def btn_1(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '1')
	def btn_2(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '2')
	def btn_3(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '3')
	def btn_4(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '4')
	def btn_5(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '5')
	def btn_6(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '6')
	def btn_7(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '7')
	def btn_8(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '8')
	def btn_9(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '9')
	def btn_0(self):
		self.lineEdit_2.setText(self.lineEdit_2.text() + '0')
	def btn_b(self):
		self.lineEdit_2.setText(self.lineEdit_2.text()[:-1])

	def autoCheck(self):
		if len(self.lineEdit_2.text())>2:
			self.credentialCheck()


	#test 용 0Vyk090ARPaeXe20mRvv
	def updateAuth(self):
		buttonReply=QMessageBox.question(self, '인증 서버 DB 갱신', "이 작업은 되돌릴 수 없습니다. \n1. KeyPair를 제대로 확인해주세요\n2. 조회 후 업데이트된 DB 적용까지 시간이 걸릴 수 있습니다.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if buttonReply == QMessageBox.Yes:
			keyPair = self.lineEdit_3.text()
			try:
				self.authManager.update(keyPair)
			except Exception as ex:
				buttonReply=QMessageBox.warning(self, "서버에서 가져오기 실패", "서버에서 조회를 실패하였습니다.\nKey Pair를 확인해주세요", QMessageBox.Ok)
				return;

			temp = np.load('./adms_user_db.npz', allow_pickle=True)
			self.userDB = temp['db'].item()
			QMessageBox.information(self, "인증 DB 갱신 성공", "프로그램 재시작 후 로그인 해주세요.", QMessageBox.Ok)


		else:
			return;




	def credentialCheck(self, id=None, pwd=None):
		global glNode
		#self.id = id if id else self.lineEdit.text()
		self.pwd = pws if pwd else self.lineEdit_2.text()

		try:
			returnVal = self.userDB.idValidation(self.lineEdit_2.text())
			print(returnVal)
			if returnVal:

				self.mW = mainWidnow(self.userDB.retrieve(returnVal, 'all'))
				self.mW.show()
				self.hide()
				return 1
			else:
				self.label_7.setText("Wrong Passwords")
				return 0
			pass
		except Exception as ex:
			raise Exception(ex)
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

		name = userInfo[0]
		sid = userInfo[3]

		self.label.setText(self.label.text() + name)
		self.label_5.setText(self.label_5.text() + sid)

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
		self.node.get_logger().info("ADMS : ADMS Initialize")


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

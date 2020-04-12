import sys
from PyQt5.QtWidgets import * #PyQt import
from PyQt5.QtGui import *
from PyQt5 import uic
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import cryptography
from cryptography.fernet import Fernet
import cv2
import numpy as np
from capsule import capsule
import pprint
from authManager import authentication_server

main_form = uic.loadUiType("userRegister.ui")[0]

class imagethread(QThread):
	image_pixmap = pyqtSignal(QtGui.QPixmap)


	def __init__(self):
		QThread.__init__(self, parent=None)
		self.cap = cv2.VideoCapture(0)
		pass

	def __del__(self):
		print("Command Job Done")
		exit(0)




	def run(self):
		while True:
			ret, img = self.cap.read()
			if ret:
				self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
				h,w,c = img.shape
				qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
				p = qImg.scaled(301, 240, Qt.KeepAspectRatio)
				pixmap = QtGui.QPixmap.fromImage(p)
				self.image_pixmap.emit(pixmap)
			else:
				print("cannot read frame.")
				

		cap.release()
		print("Thread end.")
		pass


class mainWidnow(QMainWindow, main_form):
	

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
		
		
		self.imgTh = imagethread()
		self.imgTh.image_pixmap.connect(self.setImage)
		self.imgTh.start()

		self.pushButton.clicked.connect(self.registerBtn)
		self.pushButton_2.clicked.connect(self.adminBtn)
		self.pushButton_3.clicked.connect(self.uploadData)

		self.auth_db = capsule()

		self.pushButton_3.setEnabled(False)

	@pyqtSlot(QtGui.QPixmap)
	def setImage(self, image):
		self.image_data = image
		self.label.setPixmap(image)

	def registerBtn(self):
		name = self.lineEdit.text()
		sid = self.lineEdit_2.text()
		if not self.lineEdit_3.text() == self.lineEdit_4.text():
			QMessageBox.information(self, 'Password Verification Failed', "비밀번호 불일치 오류" ,QMessageBox.Ok )
			return;
		policy = str(self.comboBox.currentText())
		image = self.image_data

		self.auth_db.add(name, sid, self.lineEdit_3.text(), self.imgTh.img, policy)
		return QMessageBox.information(self, "Register 성공" ,f"{name}님 정상적으로 등록되었습니다.", QMessageBox.Ok)

	def adminBtn(self):
		passwd = self.lineEdit_5.text()

		if not passwd == "kansan":
			return;

		self.textBrowser.setText(pprint.pformat(self.auth_db.getCapsule()))
		self.pushButton_3.setEnabled(True)


	
	def uploadData(self):
		self.pushButton_3.setEnabled(False)
		np.savez_compressed('./user_auth_db.npz', db = self.auth_db)
		server = authentication_server()
		#fileID = server.new('./user_auth_db.npz')
		QMessageBox.information(self, "DB Update 성공" ,f"DB 업데이트 성공, Key Pair를 반드시 백업하세요", QMessageBox.Ok)
		fileID = str('14yhyg n2f3ot')
		self.textEdit.setText(str(fileID))
		pass









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWidnow()
    window.show()
    app.exec_()
	


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
		


	def loginBtn(self):
		if self.credentialCheck():
			self.mW = mainWidnow()
			self.mW.show()
			self.hide()
		else:
			self.label_7.setText("Wrong Passwords")

	def credentialCheck(self, id=None, pwd=None):
		self.id = id if id else self.lineEdit.text()
		self.pwd = pws if pwd else self.lineEdit_2.text()
		credDb = {"201811093" : "GwanjunShin"}
		if credDb.get(self.id) == "GwanjunShin":
			return 1
		else:
			return 0

	



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
		self.saveDialog.clicked.connect(self.saveFileDialog)
		self.logout.clicked.connect(self.logoutBtn)

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
		self.hide()
	

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logWin = loginWindow()
    logWin.show()
    app.exec_()
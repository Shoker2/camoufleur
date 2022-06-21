from shifr import Ui_Shifr

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import os
import sys

def messageBox(title, text, icon=None): # Окно ошибки
	msgBox = QMessageBox()
	if icon != None:
		msgBox.setIcon(icon)
	msgBox.setWindowTitle(title)
	msgBox.setText(text)
	try:
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
		msgBox.setWindowIcon(icon)
	except:
		pass
	msgBox.setStandardButtons(QMessageBox.Ok)
	msgBox.exec()

class main(Ui_Shifr):
	def setupUi(self, main):
		Ui_Shifr.setupUi(self, main)
		MainWindow.setMinimumSize(QtCore.QSize(MainWindow.size().width(), MainWindow.size().height()))
		MainWindow.setMaximumSize(QtCore.QSize(MainWindow.size().width(), MainWindow.size().height()))

		self.retranslateUi(main)
		self.ImageButton.clicked.connect(lambda: self.select_img())
		self.RarButton.clicked.connect(lambda: self.select_rar())

		self.radioButton1.clicked.connect(lambda: self.rb1())
		self.radioButton2.clicked.connect(lambda: self.rb2())

		self.DoneButton.clicked.connect(lambda: self.Done())

		global style

		try:
			f = open("style.css", "r", encoding="utf")
			style = f.read()
			f.close()
		except:
			pass

		MainWindow.setStyleSheet(style)
		try:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
			MainWindow.setWindowIcon(icon)
		except:
			pass

	def retranslateUi(self, main):
		Ui_Shifr.retranslateUi(self, main)
		MainWindow.setWindowTitle("Окно выбора действия")

	def pips_setup(self):
		os.system('pip install PyQt5 pyqt5-tools pyinstaller & pause')

	def select_img(self):
		file, _ = QFileDialog.getOpenFileName(None, 'Выбрать файл', './', "Image (*.*)")
		if file != '':
			self.ImageLineEdit.setText(file)

	def select_rar(self):
		file, _ = QFileDialog.getOpenFileName(None, 'Выбрать файл', './', "Image (*.rar)")
		if file != '':
			self.RarLineEdit.setText(file)

	def rb1(self):
		self.CodeLineEdit.setEnabled(True)
		self.RarButton.setEnabled(False)
		self.RarLineEdit.setEnabled(False)
		self.RarLineEditName.setEnabled(False)
		self.labelName.setEnabled(False)

	def rb2(self):
		self.CodeLineEdit.setEnabled(False)
		self.RarButton.setEnabled(True)
		self.RarLineEdit.setEnabled(True)
		self.RarLineEditName.setEnabled(True)
		self.labelName.setEnabled(True)

	def Complete(self):
		messageBox("Успех", "Операция прошла успешно", QMessageBox.Information)

	def Failure(self):
		messageBox("Ошибка", "Операция прошла неудачно", QMessageBox.Critical)

	def Done(self):
		if self.ImageLineEdit.text() != "":
			try:
				way = str(self.ImageLineEdit.text())
				name = way[way.rfind('/')+1:]

				if way.rfind('/') == -1:
					raise ValueError('Неверный путь')

				dot = way[way.rfind('.'):]

				way_rar = str(self.RarLineEdit.text())
				name_rar = way_rar[way_rar.rfind('/')+1:]

				if self.radioButton1.isChecked() and str(self.CodeLineEdit.text()) != "":
					os.system('cd "' + way[:way.rfind('/')+1] +'" &' + 'echo "' + str(self.CodeLineEdit.text()) + '">>"' + name + '"')
					self.Complete()
				elif self.radioButton2.isChecked() and str(self.RarLineEdit.text()) != "":
					if str(self.RarLineEditName.text()) == "":
						os.system('cd "' + way[:way.rfind('/')+1] +'" &' + 'copy /b ' + name + ' + "' + way_rar + '" "' + "shifr_" + name +'"')
						self.Complete()
					else:
						os.system('cd "' + way[:way.rfind('/')+1] +'" &' + 'copy /b ' + name + ' + "' + way_rar + '" "' + str(self.RarLineEditName.text()) + dot +'"')
						self.Complete()
			except:
				self.Failure()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = main()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
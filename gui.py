# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from info import Ui_MainWindow1
import multinb as mn
class Ui_MainWindow(object):
    def Analysis(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setupinfo(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 310, 181, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(270, 320, 91, 23))
        self.quit.setObjectName("quit")
        self.analysis = QtWidgets.QPushButton(self.centralwidget)
        self.analysis.setGeometry(QtCore.QRect(260, 270, 121, 23))
        self.analysis.setObjectName("analysis")
        self.analysis.clicked.connect(self.Analysis)
        self.classify = QtWidgets.QPushButton(self.centralwidget)
        self.classify.setGeometry(QtCore.QRect(20, 270, 151, 23))
        self.classify.setObjectName("classify")
        self.email = QtWidgets.QTextEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(20, 60, 361, 201))
        self.email.setObjectName("email")
        self.msg = QtWidgets.QLabel(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(20, 20, 361, 31))
        self.msg.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.msg.setTextFormat(QtCore.Qt.RichText)
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.connectActions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.analysis.setText(_translate("MainWindow", "Analysis"))
        self.classify.setText(_translate("MainWindow", "Identify The message"))
        self.msg.setText(_translate("MainWindow", "Enter your message here"))

    def connectActions(self):
        self.classify.clicked.connect(self.identify)
        self.quit.clicked.connect(self.EXIT)

    def EXIT(self):
        import sys
        sys.exit()

    def identify(self):
        data=self.email.toPlainText()
        m=mn.test_data(data)
        m=("Message is : {}".format(m))
        print(m)
        self.label.setText((m))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


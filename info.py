# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import analysis as an
from confusion import Ui_Confusion
from hamcloud import Ui_Hamcloud
from spamcloud import Ui_Spamcloud
class Ui_MainWindow1(object):
    def Confusion(self):
         self.MainWindow = QtWidgets.QMainWindow()
         self.ui = Ui_Confusion()
         self.ui.setupconfusion(self.MainWindow)
         self.MainWindow.show()
         
    def Hamcloud(self):
         self.MainWindow = QtWidgets.QMainWindow()
         self.ui = Ui_Hamcloud()
         self.ui.setuphamcloud(self.MainWindow)
         self.MainWindow.show()
         
    def Spamcloud(self):
         self.MainWindow = QtWidgets.QMainWindow()
         self.ui = Ui_Spamcloud()
         self.ui.setupspamcloud(self.MainWindow)
         self.MainWindow.show()
         
    def setupinfo(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 170, 71, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.spamcloud = QtWidgets.QPushButton(self.centralwidget)
        self.spamcloud.setGeometry(QtCore.QRect(210, 250, 111, 23))
        self.spamcloud.setObjectName("spamcloud")
        self.spamcloud.clicked.connect(self.Spamcloud)
        self.precision = QtWidgets.QLabel(self.centralwidget)
        self.precision.setGeometry(QtCore.QRect(280, 90, 131, 16))
        self.precision.setText("")
        self.precision.setAlignment(QtCore.Qt.AlignCenter)
        self.precision.setObjectName("precision")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(220, 290, 75, 23))
        self.Quit.setObjectName("Quit")
        self.Quit.clicked.connect(self.EXIT)
        self.recall = QtWidgets.QLabel(self.centralwidget)
        self.recall.setGeometry(QtCore.QRect(280, 130, 131, 16))
        self.recall.setText("")
        self.recall.setAlignment(QtCore.Qt.AlignCenter)
        self.recall.setObjectName("recall")
        self.hamcloud = QtWidgets.QPushButton(self.centralwidget)
        self.hamcloud.setGeometry(QtCore.QRect(20, 250, 111, 21))
        self.hamcloud.setObjectName("hamcloud")
        self.hamcloud.clicked.connect(self.Hamcloud)
        self.Analyse = QtWidgets.QPushButton(self.centralwidget)
        self.Analyse.setGeometry(QtCore.QRect(420, 10, 75, 23))
        self.Analyse.setObjectName("Analyse")
        self.tag = QtWidgets.QLineEdit(self.centralwidget)
        self.tag.setGeometry(QtCore.QRect(280, 10, 113, 20))
        self.tag.setObjectName("tag")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 90, 71, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 251, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.confusion = QtWidgets.QPushButton(self.centralwidget)
        self.confusion.setGeometry(QtCore.QRect(384, 250, 111, 23))
        self.confusion.setObjectName("confusion")
        self.confusion.clicked.connect(self.Confusion)
        self.Fscore = QtWidgets.QLabel(self.centralwidget)
        self.Fscore.setGeometry(QtCore.QRect(280, 170, 131, 16))
        self.Fscore.setText("")
        self.Fscore.setAlignment(QtCore.Qt.AlignCenter)
        self.Fscore.setObjectName("Fscore")
        self.accuracy = QtWidgets.QLabel(self.centralwidget)
        self.accuracy.setGeometry(QtCore.QRect(280, 50, 131, 16))
        self.accuracy.setText("")
        self.accuracy.setAlignment(QtCore.Qt.AlignCenter)
        self.accuracy.setObjectName("accuracy")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 91, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 130, 71, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
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
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">F-score</span></p></body></html>"))
        self.spamcloud.setText(_translate("MainWindow", "Get Spam wordcloud"))
        self.Quit.setText(_translate("MainWindow", "Quit"))
        self.hamcloud.setText(_translate("MainWindow", "Get Ham worldcloud"))
        self.Analyse.setText(_translate("MainWindow", "Analyse"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Precision</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Enter the label you want to analyse</span></p></body></html>"))
        self.confusion.setText(_translate("MainWindow", "Confusion Metrix"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Accuracy</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Recall</span></p></body></html>"))

    def connectActions(self):
        self.Analyse.clicked.connect(self.gettag)
        self.Quit.clicked.connect(self.EXIT)

    def EXIT(self):
        import sys
        sys.exit()
        
    def gettag(self):
        t=self.tag.text()
        a,p,r,f=an.getinfo(t)
        a='{0:0.5f}'.format(a)
        p='{0:0.5f}'.format(p)
        r='{0:0.5f}'.format(r)
        f='{0:0.5f}'.format(f)
        self.accuracy.setText(a)
        self.precision.setText(p)
        self.recall.setText(r)
        self.Fscore.setText(f)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupinfo(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


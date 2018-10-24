# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confusion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Confusion(object):
    def setupconfusion(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 461, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/conf_mat.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(210, 400, 75, 23))
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(self.closeit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.connectactions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def connectactions(self):
        self.quit.clicked.connect(self.Quitit)
        
    def Quitit(self):
        import sys
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        
    def closeit(self):
       import sys 
       sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Confusion()
    ui.setupconfusion(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


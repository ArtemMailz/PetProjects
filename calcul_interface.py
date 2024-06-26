# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(360, 380)
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(26)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 118, 118);\n"
"border-radius: 10px;\n"
"background-color: rgb(0, 17, 76);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.displai = QtWidgets.QLabel(self.centralwidget)
        self.displai.setEnabled(True)
        self.displai.setGeometry(QtCore.QRect(10, 10, 341, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.displai.setFont(font)
        self.displai.setStyleSheet("background-color: rgb(0, 69, 95);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0, stop:0.102273 rgba(0, 111, 111, 255), stop:1 rgba(0, 45, 135, 255));\n"
"border-radius: 10px;")
        self.displai.setScaledContents(False)
        self.displai.setObjectName("displai")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setEnabled(True)
        self.btn_0.setGeometry(QtCore.QRect(10, 290, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setItalic(False)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));\n"
"border-radius: 10px;")
        self.btn_0.setObjectName("btn_0")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_1.setObjectName("btn_1")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(150, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_3.setObjectName("btn_3")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(80, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_2.setObjectName("btn_2")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(80, 150, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_5.setObjectName("btn_5")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 150, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_4.setObjectName("btn_4")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(150, 150, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_6.setObjectName("btn_6")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(80, 220, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(150, 220, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_9.setObjectName("btn_9")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 220, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_7.setObjectName("btn_7")
        self.btn_toch = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toch.setGeometry(QtCore.QRect(150, 290, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_toch.setFont(font)
        self.btn_toch.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_toch.setObjectName("btn_toch")
        self.btn_00 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_00.setGeometry(QtCore.QRect(80, 290, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_00.setFont(font)
        self.btn_00.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_00.setObjectName("btn_00")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(220, 150, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(220, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_umnog = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umnog.setGeometry(QtCore.QRect(220, 220, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_umnog.setFont(font)
        self.btn_umnog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_umnog.setObjectName("btn_umnog")
        self.btn_delenie = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delenie.setGeometry(QtCore.QRect(220, 290, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_delenie.setFont(font)
        self.btn_delenie.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_delenie.setObjectName("btn_delenie")
        self.btn_rovno = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rovno.setGeometry(QtCore.QRect(290, 149, 61, 201))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_rovno.setFont(font)
        self.btn_rovno.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_rovno.setObjectName("btn_rovno")
        self.btn_ochist = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ochist.setGeometry(QtCore.QRect(290, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_ochist.setFont(font)
        self.btn_ochist.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 100, 100, 255), stop:1 rgba(0, 37, 112, 255));")
        self.btn_ochist.setObjectName("btn_ochist")
        self.btn_0.raise_()
        self.displai.raise_()
        self.btn_1.raise_()
        self.btn_3.raise_()
        self.btn_2.raise_()
        self.btn_5.raise_()
        self.btn_4.raise_()
        self.btn_6.raise_()
        self.btn_8.raise_()
        self.btn_9.raise_()
        self.btn_7.raise_()
        self.btn_toch.raise_()
        self.btn_00.raise_()
        self.btn_minus.raise_()
        self.btn_plus.raise_()
        self.btn_umnog.raise_()
        self.btn_delenie.raise_()
        self.btn_rovno.raise_()
        self.btn_ochist.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.add_logic()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мой первый кулькулятор"))
        self.displai.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_toch.setText(_translate("MainWindow", "."))
        self.btn_00.setText(_translate("MainWindow", "00"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_umnog.setText(_translate("MainWindow", "*"))
        self.btn_delenie.setText(_translate("MainWindow", "/"))
        self.btn_rovno.setText(_translate("MainWindow", "="))
        self.btn_ochist.setText(_translate("MainWindow", "C"))
        
        
    def add_logic(self):
            self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
            self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
            self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
            self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
            self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
            self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
            self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
            self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
            self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
            self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
            self.btn_00.clicked.connect(lambda: self.write_number(self.btn_00.text()))
            
            self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
            self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
            self.btn_umnog.clicked.connect(lambda: self.write_number(self.btn_umnog.text()))
            self.btn_delenie.clicked.connect(lambda: self.write_number(self.btn_delenie.text()))
            self.btn_toch.clicked.connect(lambda: self.write_number(self.btn_toch.text()))
            
            self.btn_ochist.clicked.connect(lambda: self.write_zero())
            self.btn_rovno.clicked.connect(lambda: self.write_rovno())
            
    def write_number(self, number):
                if self.displai.text() == "0" or self.displai.text() == "00":
                        self.displai.setText(number)
                else:
                    self.displai.setText(self.displai.text() + number)
                    
    def write_zero(self):
            self.displai.setText("0")
            
    def write_rovno(self):
            res = eval(self.displai.text())
            self.displai.setText(str(res))
                    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

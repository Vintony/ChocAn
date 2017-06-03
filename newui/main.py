# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 284)
        MainWindow.setStyleSheet("#QmainWindow\n"
"{\n"
"    border-image:url(:/新前缀/timg (7).jpg);\n"
"    background-color:rgb(0, 255, 255)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 491, 301))
        self.frame.setStyleSheet("QFrame{\n"
" border-image:url(:/新前缀/bg.jpg);\n"
"}\n"
"    \n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.admin_button = QtWidgets.QPushButton(self.frame)
        self.admin_button.setGeometry(QtCore.QRect(230, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.admin_button.setFont(font)
        self.admin_button.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.admin_button.setAutoDefault(False)
        self.admin_button.setDefault(False)
        self.admin_button.setObjectName("admin_button")
        self.user_button = QtWidgets.QPushButton(self.frame)
        self.user_button.setEnabled(True)
        self.user_button.setGeometry(QtCore.QRect(230, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.user_button.setFont(font)
        self.user_button.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.user_button.setObjectName("user_button")
        self.admin_button.raise_()
        self.admin_button.raise_()
        self.user_button.raise_()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChocAn"))
        self.admin_button.setText(_translate("MainWindow", "Admin"))
        self.user_button.setText(_translate("MainWindow", "User"))
        self.label.setText(_translate("MainWindow", "Welcome to use ChocAn !"))

import image_rc

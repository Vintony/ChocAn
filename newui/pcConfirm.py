# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pcConfirm.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pcform(object):
    def setupUi(self, pcform):
        pcform.setObjectName("pcform")
        pcform.resize(419, 235)
        self.frame = QtWidgets.QFrame(pcform)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 451, 261))
        self.frame.setStyleSheet("QFrame{\n"
" border-image:url(:/新前缀/timg (6).jpg)\n"
"}\n"
"    \n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pcText = QtWidgets.QLineEdit(self.frame)
        self.pcText.setGeometry(QtCore.QRect(30, 110, 191, 20))
        self.pcText.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.pcText.setObjectName("pcText")
        self.confirmPC = QtWidgets.QPushButton(self.frame)
        self.confirmPC.setGeometry(QtCore.QRect(280, 110, 81, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.confirmPC.setFont(font)
        self.confirmPC.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.confirmPC.setObjectName("confirmPC")
        self.toMainUI = QtWidgets.QPushButton(self.frame)
        self.toMainUI.setGeometry(QtCore.QRect(280, 160, 81, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toMainUI.setFont(font)
        self.toMainUI.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toMainUI.setObjectName("toMainUI")
        self.label = QtWidgets.QLabel(pcform)
        self.label.setGeometry(QtCore.QRect(20, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")

        self.retranslateUi(pcform)
        self.toMainUI.clicked.connect(pcform.toMainUI)
        QtCore.QMetaObject.connectSlotsByName(pcform)

    def retranslateUi(self, pcform):
        _translate = QtCore.QCoreApplication.translate
        pcform.setWindowTitle(_translate("pcform", "Provider Confirm"))
        self.confirmPC.setText(_translate("pcform", "enter"))
        self.toMainUI.setText(_translate("pcform", "return"))
        self.label.setText(_translate("pcform", "Please enter the provider code:"))

import image_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mcConfirm.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mcForm(object):
    def setupUi(self, mcForm):
        mcForm.setObjectName("mcForm")
        mcForm.resize(418, 234)
        self.frame = QtWidgets.QFrame(mcForm)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 441, 261))
        self.frame.setStyleSheet("QFrame{\n"
" border-image:url(:/新前缀/timg (6).jpg)\n"
"}\n"
"    \n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(280, 120, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.mcText = QtWidgets.QLineEdit(self.frame)
        self.mcText.setGeometry(QtCore.QRect(30, 120, 191, 20))
        self.mcText.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.mcText.setText("")
        self.mcText.setObjectName("mcText")
        self.toProviderConfirmUI = QtWidgets.QPushButton(self.frame)
        self.toProviderConfirmUI.setGeometry(QtCore.QRect(280, 170, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toProviderConfirmUI.setFont(font)
        self.toProviderConfirmUI.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toProviderConfirmUI.setObjectName("toProviderConfirmUI")
        self.label = QtWidgets.QLabel(mcForm)
        self.label.setGeometry(QtCore.QRect(20, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")

        self.retranslateUi(mcForm)
        QtCore.QMetaObject.connectSlotsByName(mcForm)

    def retranslateUi(self, mcForm):
        _translate = QtCore.QCoreApplication.translate
        mcForm.setWindowTitle(_translate("mcForm", "Member Confirm"))
        self.pushButton.setText(_translate("mcForm", "enter"))
        self.toProviderConfirmUI.setText(_translate("mcForm", "return"))
        self.label.setText(_translate("mcForm", "Please enter the member code:"))

import image_rc

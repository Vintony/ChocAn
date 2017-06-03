# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usercontrol.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, ucForm):
        ucForm.setObjectName("Form")
        ucForm.resize(512, 288)
        self.frame = QtWidgets.QFrame(ucForm)
        self.frame.setGeometry(QtCore.QRect(0, -10, 511, 301))
        self.frame.setStyleSheet("QFrame{\n"
" border-image:url(:/img/bg.jpg)\n"
"}\n"
"    ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.getSL = QtWidgets.QPushButton(self.frame)
        self.getSL.setGeometry(QtCore.QRect(350, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.getSL.setFont(font)
        self.getSL.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.getSL.setObjectName("getSL")
        self.toSRUI = QtWidgets.QPushButton(self.frame)
        self.toSRUI.setGeometry(QtCore.QRect(350, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toSRUI.setFont(font)
        self.toSRUI.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toSRUI.setObjectName("toSRUI")
        self.toMCUI = QtWidgets.QPushButton(self.frame)
        self.toMCUI.setGeometry(QtCore.QRect(350, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toMCUI.setFont(font)
        self.toMCUI.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toMCUI.setObjectName("toMCUI")
        self.getSL.raise_()
        self.toSRUI.raise_()
        self.toMCUI.raise_()
        self.getSL = QtWidgets.QPlainTextEdit(ucForm)
        self.getSL.setGeometry(QtCore.QRect(40, 40, 256, 192))
        self.getSL.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.getSL.setObjectName("serviceListText_2")

        self.retranslateUi(ucForm)
        QtCore.QMetaObject.connectSlotsByName(ucForm)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Control"))
        self.getSL.setText(_translate("Form", "getServiceList"))
        self.toSRUI.setText(_translate("Form", "addServiceRecord"))
        self.toMCUI.setText(_translate("Form", "return"))

import image_rc

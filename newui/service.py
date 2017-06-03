# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, serviceForm):
        serviceForm.setObjectName("Form")
        serviceForm.resize(380, 194)
        self.frame = QtWidgets.QFrame(serviceForm)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 461, 291))
        self.frame.setStyleSheet("QFrame{\n"
" border-image:url(:/img/bg.jpg)\n"
"}\n"
"    \n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addService = QtWidgets.QPushButton(self.frame)
        self.addService.setGeometry(QtCore.QRect(280, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.addService.setFont(font)
        self.addService.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.addService.setObjectName("pushButton_2")
        self.toAdminUI = QtWidgets.QPushButton(self.frame)
        self.toAdminUI.setGeometry(QtCore.QRect(280, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toAdminUI.setFont(font)
        self.toAdminUI.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toAdminUI.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 133, 20))
        self.lineEdit.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 133, 20))
        self.lineEdit_2.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 160, 133, 20))
        self.lineEdit_3.setStyleSheet("border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.addService.raise_()
        self.toAdminUI.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label = QtWidgets.QLabel(serviceForm)
        self.label.setGeometry(QtCore.QRect(10, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(serviceForm)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(serviceForm)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(serviceForm)
        QtCore.QMetaObject.connectSlotsByName(serviceForm)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Service"))
        self.addService.setText(_translate("Form", "add service"))
        self.toAdminUI.setText(_translate("Form", "return"))
        self.label.setText(_translate("Form", "Code:"))
        self.label_2.setText(_translate("Form", "Name:"))
        self.label_3.setText(_translate("Form", "Fee:"))

import image_rc

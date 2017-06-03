# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from functions import *
from image import *

# class Ui_userForm(object):
#     def setupUi(self, userForm):
#
#         def toMainUI(self):
#             userForm.hide()
#             widget.show()
#
#         userForm.setObjectName("userForm")
#         userForm.resize(400, 300)
#         self.verticalLayout = QtWidgets.QVBoxLayout(userForm)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.textArea = QtWidgets.QPlainTextEdit(userForm)
#         self.textArea.setObjectName("textArea")
#         self.verticalLayout.addWidget(self.textArea)
#         self.startButton = QtWidgets.QPushButton(userForm)
#         self.startButton.setObjectName("startButton")
#         self.verticalLayout.addWidget(self.startButton)
#         self.returnButton = QtWidgets.QPushButton(userForm)
#         self.returnButton.setObjectName("returnButton")
#         self.verticalLayout.addWidget(self.returnButton)
#
#         self.retranslateUserUi(userForm)
#         self.returnButton.clicked.connect(toMainUI)
#         QtCore.QMetaObject.connectSlotsByName(userForm)
#
#     def retranslateUserUi(self, userForm):
#         _translate = QtCore.QCoreApplication.translate
#         userForm.setWindowTitle(_translate("userForm", "User"))
#         self.textArea.setPlainText(_translate("userForm", "Enter your Member Number and click the button below to start."))
#         self.startButton.setText(_translate("userForm", "start"))
#         self.returnButton.setText(_translate("userForm", "return"))


class Ui_serviceForm(object):
    def setupUi(self, serviceForm):
        def toAdminUI():
            serviceForm.hide()
            adWidget.show()

        def addService():
            # addServiceInPD("100008","asd","$156.33")
            addServiceInPD(self.codeText.text(), self.nameText.text(), self.feeText.text())

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
        self.addService.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.addService.setObjectName("pushButton_2")
        self.toAdminUI = QtWidgets.QPushButton(self.frame)
        self.toAdminUI.setGeometry(QtCore.QRect(280, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toAdminUI.setFont(font)
        self.toAdminUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toAdminUI.setObjectName("pushButton")
        self.codeText = QtWidgets.QLineEdit(self.frame)
        self.codeText.setGeometry(QtCore.QRect(20, 50, 133, 20))
        self.codeText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.codeText.setObjectName("lineEdit")
        self.nameText = QtWidgets.QLineEdit(self.frame)
        self.nameText.setGeometry(QtCore.QRect(20, 100, 133, 20))
        self.nameText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.nameText.setObjectName("lineEdit_2")
        self.feeText = QtWidgets.QLineEdit(self.frame)
        self.feeText.setGeometry(QtCore.QRect(20, 160, 133, 20))
        self.feeText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.feeText.setObjectName("lineEdit_3")
        self.addService.raise_()
        self.toAdminUI.raise_()
        self.codeText.raise_()
        self.nameText.raise_()
        self.feeText.raise_()
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

        self.retranslateserviceUi(serviceForm)
        self.addService.clicked.connect(addService)
        self.toAdminUI.clicked.connect(toAdminUI)
        QtCore.QMetaObject.connectSlotsByName(serviceForm)

    def retranslateserviceUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Service"))
        self.addService.setText(_translate("Form", "add service"))
        self.toAdminUI.setText(_translate("Form", "return"))
        self.label.setText(_translate("Form", "Code:"))
        self.label_2.setText(_translate("Form", "Name:"))
        self.label_3.setText(_translate("Form", "Fee:"))


class Ui_provForm(object):
    def setupUi(self, proForm):
        def toAdminUI():
            proForm.hide()
            adWidget.show()

        def modify():
            updateProvider(self.numberText.text(),
                         {
                             "Provider name": self.nameText.text(),
                             "Provider number": self.numberText.text(),
                             "Provider street address": self.sdText.text(),
                             "Provider city": self.cityText.text(),
                             "Provider state": self.sText.text(),
                             "Provider ZIP code": self.zcText.text()
                         }
                         )

        def add():
            addProvider({
                "Provider name": self.nameText.text(),
                "Provider number": self.numberText.text(),
                "Provider street address": self.sdText.text(),
                "Provider city": self.cityText.text(),
                "Provider state": self.sText.text(),
                "Provider ZIP code": self.zcText.text()
            })

        def delete():
            delProvider(self.numberText.text())

        proForm.setObjectName("Form")
        proForm.resize(507, 304)
        self.frame = QtWidgets.QFrame(proForm)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 681, 501))
        self.frame.setStyleSheet("QFrame{\n"
                                 " border-image:url(:/img/bg.jpg)\n"
                                 "}\n"
                                 "    \n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.modify = QtWidgets.QPushButton(self.frame)
        self.modify.setGeometry(QtCore.QRect(230, 210, 141, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.modify.setFont(font)
        self.modify.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.modify.setObjectName("search")
        self.delete = QtWidgets.QPushButton(self.frame)
        self.delete.setGeometry(QtCore.QRect(50, 210, 131, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.delete.setFont(font)
        self.delete.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.delete.setObjectName("delete_2")
        self.add = QtWidgets.QPushButton(self.frame)
        self.add.setGeometry(QtCore.QRect(50, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.add.setObjectName("add")
        self.toAdminUI = QtWidgets.QPushButton(self.frame)
        self.toAdminUI.setGeometry(QtCore.QRect(230, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toAdminUI.setFont(font)
        self.toAdminUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toAdminUI.setObjectName("toAdminUI")
        self.nameText = QtWidgets.QLineEdit(self.frame)
        self.nameText.setGeometry(QtCore.QRect(50, 40, 133, 20))
        self.nameText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.nameText.setObjectName("nameText")
        self.numberText = QtWidgets.QLineEdit(self.frame)
        self.numberText.setGeometry(QtCore.QRect(230, 40, 141, 20))
        self.numberText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.numberText.setObjectName("numberText")
        self.sdText = QtWidgets.QLineEdit(self.frame)
        self.sdText.setGeometry(QtCore.QRect(50, 100, 133, 20))
        self.sdText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.sdText.setObjectName("sdText")
        self.cityText = QtWidgets.QLineEdit(self.frame)
        self.cityText.setGeometry(QtCore.QRect(230, 100, 141, 20))
        self.cityText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.cityText.setObjectName("cityText")
        self.sText = QtWidgets.QLineEdit(self.frame)
        self.sText.setGeometry(QtCore.QRect(50, 160, 133, 20))
        self.sText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.sText.setObjectName("sText")
        self.zcText = QtWidgets.QLineEdit(self.frame)
        self.zcText.setGeometry(QtCore.QRect(230, 160, 141, 20))
        self.zcText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.zcText.setObjectName("zcText")
        self.modify.raise_()
        self.delete.raise_()
        self.add.raise_()
        self.toAdminUI.raise_()
        self.nameText.raise_()
        self.numberText.raise_()
        self.sdText.raise_()
        self.cityText.raise_()
        self.sText.raise_()
        self.zcText.raise_()
        self.label_8 = QtWidgets.QLabel(proForm)
        self.label_8.setGeometry(QtCore.QRect(30, 0, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(proForm)
        self.label_9.setGeometry(QtCore.QRect(210, 0, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(proForm)
        self.label_10.setGeometry(QtCore.QRect(30, 60, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(proForm)
        self.label_11.setGeometry(QtCore.QRect(210, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(proForm)
        self.label_12.setGeometry(QtCore.QRect(30, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(proForm)
        self.label_13.setGeometry(QtCore.QRect(210, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_13.setObjectName("label_13")

        self.retranslateProviderUi(proForm)
        self.add.clicked.connect(add)
        self.modify.clicked.connect(modify)
        self.delete.clicked.connect(delete)
        self.toAdminUI.clicked.connect(toAdminUI)
        QtCore.QMetaObject.connectSlotsByName(proForm)

    def retranslateProviderUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Provider"))
        self.modify.setText(_translate("Form", "search by number"))
        self.delete.setText(_translate("Form", "delete by number"))
        self.add.setText(_translate("Form", "add"))
        self.toAdminUI.setText(_translate("Form", "return"))
        self.label_8.setText(_translate("Form", "Provider name:"))
        self.label_9.setText(_translate("Form", "Provider number:"))
        self.label_10.setText(_translate("Form", "Provider street address:"))
        self.label_11.setText(_translate("Form", "Provider city:"))
        self.label_12.setText(_translate("Form", "Provider state:"))
        self.label_13.setText(_translate("Form", "Provider ZIP code:"))


class Ui_memForm(object):
    def setupUi(self, memForm):
        def toAdminUI():
            memForm.hide()
            adWidget.show()

        def modify():
            updateMember(self.numberText.text(),
                         {
                             "Member name": self.nameText.text(),
                             "Member number": self.numberText.text(),
                             "Member street address": self.sdText.text(),
                             "Member city": self.cityText.text(),
                             "Member state": self.sText.text(),
                             "Member ZIP code": self.zcText.text()
                         }
                         )

        def add():
            addMember({
                "Member name": self.nameText.text(),
                "Member number": self.numberText.text(),
                "Member street address": self.sdText.text(),
                "Member city": self.cityText.text(),
                "Member state": self.sText.text(),
                "Member ZIP code": self.zcText.text()
            })

        def delete():
            delMember(self.numberText.text())

        memForm.setObjectName("Form")
        memForm.resize(507, 304)
        self.frame = QtWidgets.QFrame(memForm)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 681, 501))
        self.frame.setStyleSheet("QFrame{\n"
                                 " border-image:url(:/img/bg.jpg)\n"
                                 "}\n"
                                 "    \n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.modify = QtWidgets.QPushButton(self.frame)
        self.modify.setGeometry(QtCore.QRect(230, 210, 141, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.modify.setFont(font)
        self.modify.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.modify.setObjectName("search")
        self.delete = QtWidgets.QPushButton(self.frame)
        self.delete.setGeometry(QtCore.QRect(50, 210, 131, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.delete.setFont(font)
        self.delete.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.delete.setObjectName("delete_2")
        self.add = QtWidgets.QPushButton(self.frame)
        self.add.setGeometry(QtCore.QRect(50, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.add.setObjectName("add")
        self.toAdminUI = QtWidgets.QPushButton(self.frame)
        self.toAdminUI.setGeometry(QtCore.QRect(230, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toAdminUI.setFont(font)
        self.toAdminUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toAdminUI.setObjectName("toAdminUI")
        self.nameText = QtWidgets.QLineEdit(self.frame)
        self.nameText.setGeometry(QtCore.QRect(50, 40, 133, 20))
        self.nameText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.nameText.setObjectName("nameText")
        self.numberText = QtWidgets.QLineEdit(self.frame)
        self.numberText.setGeometry(QtCore.QRect(230, 40, 141, 20))
        self.numberText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.numberText.setObjectName("numberText")
        self.sdText = QtWidgets.QLineEdit(self.frame)
        self.sdText.setGeometry(QtCore.QRect(50, 100, 133, 20))
        self.sdText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.sdText.setObjectName("sdText")
        self.cityText = QtWidgets.QLineEdit(self.frame)
        self.cityText.setGeometry(QtCore.QRect(230, 100, 141, 20))
        self.cityText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.cityText.setObjectName("cityText")
        self.sText = QtWidgets.QLineEdit(self.frame)
        self.sText.setGeometry(QtCore.QRect(50, 160, 133, 20))
        self.sText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.sText.setObjectName("sText")
        self.zcText = QtWidgets.QLineEdit(self.frame)
        self.zcText.setGeometry(QtCore.QRect(230, 160, 141, 20))
        self.zcText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.zcText.setObjectName("zcText")
        self.modify.raise_()
        self.delete.raise_()
        self.add.raise_()
        self.toAdminUI.raise_()
        self.nameText.raise_()
        self.numberText.raise_()
        self.sdText.raise_()
        self.cityText.raise_()
        self.sText.raise_()
        self.zcText.raise_()
        self.label_8 = QtWidgets.QLabel(memForm)
        self.label_8.setGeometry(QtCore.QRect(30, 0, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(memForm)
        self.label_9.setGeometry(QtCore.QRect(210, 0, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(memForm)
        self.label_10.setGeometry(QtCore.QRect(30, 60, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(memForm)
        self.label_11.setGeometry(QtCore.QRect(210, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(memForm)
        self.label_12.setGeometry(QtCore.QRect(30, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(memForm)
        self.label_13.setGeometry(QtCore.QRect(210, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_13.setObjectName("label_13")

        self.retranslateMemberUi(memForm)
        self.add.clicked.connect(add)
        self.modify.clicked.connect(modify)
        self.delete.clicked.connect(delete)
        self.toAdminUI.clicked.connect(toAdminUI)
        QtCore.QMetaObject.connectSlotsByName(memForm)

    def retranslateMemberUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Member"))
        self.modify.setText(_translate("Form", "modify by number"))
        self.delete.setText(_translate("Form", "delete by number"))
        self.add.setText(_translate("Form", "add"))
        self.toAdminUI.setText(_translate("Form", "return"))
        self.label_8.setText(_translate("Form", "Member name:"))
        self.label_9.setText(_translate("Form", "Member number:"))
        self.label_10.setText(_translate("Form", "Member street address:"))
        self.label_11.setText(_translate("Form", "Member city:"))
        self.label_12.setText(_translate("Form", "Member state:"))
        self.label_13.setText(_translate("Form", "Member ZIP code:"))


class Ui_AdminForm(object):
    def setupUi(self, AdminForm):
        def toMainUI():
            AdminForm.hide()
            widget.show()

        def toMUI():
            AdminForm.hide()
            memWidget.show()

        def toPUI():
            AdminForm.hide()
            proWidget.show()

        def toSUI():
            AdminForm.hide()
            serWidget.show()

        def storeB():
            storeBill()

        def storeManR():
            storeManagerReport()

        def storeMemR():
            storeMemberReport(self.lineEdit.text())

        def storePR():
            storeProviderReport(self.lineEdit.text())

        AdminForm.setObjectName("AdminForm")
        AdminForm.resize(552, 455)
        self.frame = QtWidgets.QFrame(AdminForm)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 591, 471))
        self.frame.setStyleSheet("QFrame{\n"
                                 " border-image:url(:/img/bg.jpg);\n"
                                 "}\n"
                                 "    \n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toSUI = QtWidgets.QPushButton(self.frame)
        self.toSUI.setEnabled(True)
        self.toSUI.setGeometry(QtCore.QRect(40, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.toSUI.setFont(font)
        self.toSUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toSUI.setObjectName("toSUI")
        self.toPUI = QtWidgets.QPushButton(self.frame)
        self.toPUI.setGeometry(QtCore.QRect(220, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toPUI.setFont(font)
        self.toPUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toPUI.setObjectName("toPUI")
        self.toMUI = QtWidgets.QPushButton(self.frame)
        self.toMUI.setGeometry(QtCore.QRect(390, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toMUI.setFont(font)
        self.toMUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toMUI.setObjectName("toMUI")
        self.storeManR = QtWidgets.QPushButton(self.frame)
        self.storeManR.setGeometry(QtCore.QRect(220, 180, 139, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.storeManR.setFont(font)
        self.storeManR.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.storeManR.setObjectName("storeManR")
        self.storeB = QtWidgets.QPushButton(self.frame)
        self.storeB.setGeometry(QtCore.QRect(400, 180, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.storeB.setFont(font)
        self.storeB.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.storeB.setObjectName("storeB")
        self.storePR = QtWidgets.QPushButton(self.frame)
        self.storePR.setGeometry(QtCore.QRect(220, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.storePR.setFont(font)
        self.storePR.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.storePR.setObjectName("storePR")
        self.storeMemR = QtWidgets.QPushButton(self.frame)
        self.storeMemR.setGeometry(QtCore.QRect(400, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.storeMemR.setFont(font)
        self.storeMemR.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.storeMemR.setObjectName("storeMemR")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(50, 300, 133, 20))
        self.lineEdit.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.toMainUI = QtWidgets.QPushButton(self.frame)
        self.toMainUI.setGeometry(QtCore.QRect(470, 400, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toMainUI.setFont(font)
        self.toMainUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toMainUI.setObjectName("toMainUI")

        self.retranslateAdminUi(AdminForm)
        self.toMainUI.clicked.connect(toMainUI)
        self.toMUI.clicked.connect(toMUI)
        self.toPUI.clicked.connect(toPUI)
        self.toSUI.clicked.connect(toSUI)
        self.storeB.clicked.connect(storeB)
        self.storeManR.clicked.connect(storeManR)
        self.storeMemR.clicked.connect(storeMemR)
        self.storePR.clicked.connect(storePR)
        QtCore.QMetaObject.connectSlotsByName(AdminForm)

    def retranslateAdminUi(self, AdminForm):
        _translate = QtCore.QCoreApplication.translate
        AdminForm.setWindowTitle(_translate("AdminForm", "Admin"))
        self.toSUI.setText(_translate("AdminForm", "Service"))
        self.toPUI.setText(_translate("AdminForm", "Provider"))
        self.toMUI.setText(_translate("AdminForm", "Member"))
        self.storeManR.setText(_translate("AdminForm", "StoreManagerReport"))
        self.storeB.setText(_translate("AdminForm", "StoreBill"))
        self.storePR.setText(_translate("AdminForm", "StoreProviderRecord"))
        self.storeMemR.setText(_translate("AdminForm", "StoreMemberRecord"))
        self.toMainUI.setText(_translate("AdminForm", "Return"))


class Ui_sdForm(object):
    def setupUi(self, sdForm):
        def addSR():
            # addServiceRecord({
            # "Current date and time":"5-27-2017 11:11:11",
            #         "Service date":"5-22-2017",
            #          "Provider number":"000000004",
            #         "Member number":"000000007",
            #         "Service code":"100008",
            #          "Comments":"that's good."
            # })
            addServiceRecord(
                {
                    "Current date and time": self.cdatText.text(),
                    "Service date": self.sdText.text(),
                    "Provider number": self.pnText.text(),
                    "Member number": self.mnText.text(),
                    "Service code": self.scText.text(),
                    "Comments": self.cText.text()
                }
            )
            sdForm.hide()
            ucWidget.show()

        def toUCUI():
            sdForm.hide()
            ucWidget.show()

        sdForm.setObjectName("srForm")
        sdForm.resize(383, 288)
        self.frame = QtWidgets.QFrame(sdForm)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 421, 371))
        self.frame.setStyleSheet("QFrame{\n"
                                 " border-image:url(:/img/bg.jpg)\n"
                                 "}\n"
                                 "    \n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mnText = QtWidgets.QLineEdit(self.frame)
        self.mnText.setGeometry(QtCore.QRect(220, 130, 133, 20))
        self.mnText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.mnText.setObjectName("mnText")
        self.pnText = QtWidgets.QLineEdit(self.frame)
        self.pnText.setGeometry(QtCore.QRect(30, 130, 133, 20))
        self.pnText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.pnText.setObjectName("pnText")
        self.scText = QtWidgets.QLineEdit(self.frame)
        self.scText.setGeometry(QtCore.QRect(30, 200, 133, 20))
        self.scText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.scText.setObjectName("scText")
        self.cText = QtWidgets.QLineEdit(self.frame)
        self.cText.setGeometry(QtCore.QRect(220, 200, 133, 20))
        self.cText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.cText.setObjectName("cText")
        self.addServiceRecord = QtWidgets.QPushButton(self.frame)
        self.addServiceRecord.setGeometry(QtCore.QRect(30, 250, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.addServiceRecord.setFont(font)
        self.addServiceRecord.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.addServiceRecord.setObjectName("addServiceRecord")
        self.toUserConUI = QtWidgets.QPushButton(self.frame)
        self.toUserConUI.setGeometry(QtCore.QRect(220, 250, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toUserConUI.setFont(font)
        self.toUserConUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toUserConUI.setObjectName("toUserConUI")
        self.mnText.raise_()
        self.pnText.raise_()
        self.scText.raise_()
        self.cText.raise_()
        self.addServiceRecord.raise_()
        self.toUserConUI.raise_()
        self.label_7 = QtWidgets.QLabel(sdForm)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(sdForm)
        self.label_3.setGeometry(QtCore.QRect(210, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(sdForm)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(sdForm)
        self.label.setGeometry(QtCore.QRect(210, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(sdForm)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(sdForm)
        self.label_5.setGeometry(QtCore.QRect(210, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.cdatText = QtWidgets.QLineEdit(sdForm)
        self.cdatText.setGeometry(QtCore.QRect(20, 60, 133, 20))
        self.cdatText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.cdatText.setObjectName("cdatText")
        self.sdText = QtWidgets.QLineEdit(sdForm)
        self.sdText.setGeometry(QtCore.QRect(210, 60, 133, 20))
        self.sdText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.sdText.setObjectName("sdText")

        self.retranslateSdUi(sdForm)
        self.addServiceRecord.clicked.connect(addSR)
        self.toUserConUI.clicked.connect(toUCUI)
        QtCore.QMetaObject.connectSlotsByName(sdForm)

    def retranslateSdUi(self, srForm):
        _translate = QtCore.QCoreApplication.translate
        srForm.setWindowTitle(_translate("srForm", "Service Detail"))
        self.addServiceRecord.setText(_translate("srForm", "add"))
        self.toUserConUI.setText(_translate("srForm", "return"))
        self.label_7.setText(_translate("srForm", "Current date and time:"))
        self.label_3.setText(_translate("srForm", "Service date:"))
        self.label_4.setText(_translate("srForm", "Provider number:"))
        self.label.setText(_translate("srForm", "Member number:"))
        self.label_2.setText(_translate("srForm", "Service code:"))
        self.label_5.setText(_translate("srForm", "Comments:"))


class Ui_ucForm(object):
    def setupUi(self, ucForm):
        def getSL():
            self.serviceListText.setPlainText(str(printPD()))

        def toSDUI():
            ucForm.hide()
            sdWidget.show()

        def toMCUI():
            ucForm.hide()
            mcConfirmwidget.show()

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
        self.getSL.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.getSL.setObjectName("getSL")
        self.toSRUI = QtWidgets.QPushButton(self.frame)
        self.toSRUI.setGeometry(QtCore.QRect(350, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toSRUI.setFont(font)
        self.toSRUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toSRUI.setObjectName("toSRUI")
        self.toMCUI = QtWidgets.QPushButton(self.frame)
        self.toMCUI.setGeometry(QtCore.QRect(350, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toMCUI.setFont(font)
        self.toMCUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.toMCUI.setObjectName("toMCUI")
        self.getSL.raise_()
        self.toSRUI.raise_()
        self.toMCUI.raise_()
        self.serviceListText = QtWidgets.QPlainTextEdit(ucForm)
        self.serviceListText.setGeometry(QtCore.QRect(40, 40, 256, 192))
        self.serviceListText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.serviceListText.setObjectName("serviceListText_2")

        self.retranslateUserControlUi(ucForm)
        self.getSL.clicked.connect(getSL)
        self.toSRUI.clicked.connect(toSDUI)
        self.toMCUI.clicked.connect(toMCUI)
        QtCore.QMetaObject.connectSlotsByName(ucForm)

    def retranslateUserControlUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Control"))
        self.getSL.setText(_translate("Form", "getServiceList"))
        self.toSRUI.setText(_translate("Form", "addServiceRecord"))
        self.toMCUI.setText(_translate("Form", "return"))


class Ui_mcForm(object):
    def setupUi(self, mcForm):
        def mcConfirm():
            if validMemberNumber(self.mcText.text()):
                mcForm.hide()
                ucWidget.show()

            else:
                mcForm.show()

        def toPCUI():
            mcForm.hide()
            pcConfirmwidget.show()

        mcForm.setObjectName("mcForm")
        mcForm.resize(418, 230)
        self.frame = QtWidgets.QFrame(mcForm)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 441, 261))
        self.frame.setStyleSheet("QFrame{\n"
                                 " border-image:url(:/img/bg.jpg)\n"
                                 "}\n"
                                 "    \n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.confirmMC = QtWidgets.QPushButton(self.frame)
        self.confirmMC.setGeometry(QtCore.QRect(280, 120, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.confirmMC.setFont(font)
        self.confirmMC.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.confirmMC.setObjectName("confirmMC")
        self.mcText = QtWidgets.QLineEdit(self.frame)
        self.mcText.setGeometry(QtCore.QRect(30, 120, 191, 20))
        self.mcText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.mcText.setText("")
        self.mcText.setObjectName("mcText")
        self.toProviderConfirmUI = QtWidgets.QPushButton(self.frame)
        self.toProviderConfirmUI.setGeometry(QtCore.QRect(280, 170, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toProviderConfirmUI.setFont(font)
        self.toProviderConfirmUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
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

        self.retranslateMcConfirmUi(mcForm)
        self.confirmMC.clicked.connect(mcConfirm)
        self.toProviderConfirmUI.clicked.connect(toPCUI)
        QtCore.QMetaObject.connectSlotsByName(mcForm)

    def retranslateMcConfirmUi(self, mcForm):
        _translate = QtCore.QCoreApplication.translate
        mcForm.setWindowTitle(_translate("mcForm", "Member Confirm"))
        self.label.setText(_translate("mcForm", "                       Enter  member code"))
        self.confirmMC.setText(_translate("mcForm", "enter"))
        self.toProviderConfirmUI.setText(_translate("mcForm", "return"))


class Ui_pcform(object):
    def setupUi(self, pcform):
        def pcConfirm():
            if validProviderNumber(self.pcText.text()):
                pcform.hide()
                mcConfirmwidget.show()
            else:
                pcform.show()

        def toMainUI(self):
            pcform.hide()
            widget.show()

        pcform.setObjectName("pcform")
        pcform.resize(419, 230)
        self.frame = QtWidgets.QFrame(pcform)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 451, 261))
        self.frame.setStyleSheet("QFrame{\n"
                                 " border-image:url(:/img/bg.jpg)\n"
                                 "}\n"
                                 "    \n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pcText = QtWidgets.QLineEdit(self.frame)
        self.pcText.setGeometry(QtCore.QRect(30, 110, 191, 20))
        self.pcText.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(255, 255, 255);")
        self.pcText.setObjectName("pcText")
        self.confirmPC = QtWidgets.QPushButton(self.frame)
        self.confirmPC.setGeometry(QtCore.QRect(280, 110, 81, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.confirmPC.setFont(font)
        self.confirmPC.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
        self.confirmPC.setObjectName("confirmPC")
        self.toMainUI = QtWidgets.QPushButton(self.frame)
        self.toMainUI.setGeometry(QtCore.QRect(280, 160, 81, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.toMainUI.setFont(font)
        self.toMainUI.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
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

        self.retranslatePcConfirmUi(pcform)
        self.confirmPC.clicked.connect(pcConfirm)
        self.toMainUI.clicked.connect(toMainUI)
        QtCore.QMetaObject.connectSlotsByName(pcform)

    def retranslatePcConfirmUi(self, pcform):
        _translate = QtCore.QCoreApplication.translate
        pcform.setWindowTitle(_translate("pcform", "Provider Confirm"))
        self.label.setText(_translate("pcform", "                      Enter provider code"))
        self.confirmPC.setText(_translate("pcform", "enter"))
        self.toMainUI.setText(_translate("pcform", "return"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        def topcConfirmUI(self):
            MainWindow.hide()
            pcConfirmwidget.show()
            # userwidget.show()

        def toAdminUI(self):
            MainWindow.hide()
            adWidget.show()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 284)
        MainWindow.setStyleSheet("#QmainWindow\n"
                                 "{\n"
                                 "    border-image:url(:/img/timg (7).jpg);\n"
                                 "    background-color:rgb(0, 255, 255)\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 491, 301))
        self.frame.setStyleSheet("QFrame{\n"
                                 " border-image:url(:/img/bg.jpg);\n"
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
        self.admin_button.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
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
        self.user_button.setStyleSheet(
            "border:2px rgb(85, 85, 255);border-radius:10px;padding:2px 4px;background-color:rgb(85, 85, 255);color: rgb(255, 255, 255);")
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

        self.retranslateMainUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.admin_button.clicked.connect(toAdminUI)
        self.user_button.clicked.connect(topcConfirmUI)

    def retranslateMainUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChocAn"))
        self.admin_button.setText(_translate("MainWindow", "Admin"))
        self.user_button.setText(_translate("MainWindow", "User"))
        self.label.setText(_translate("MainWindow", "Welcome to use ChocAn !"))


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()

    pcConfirmwidget = QtWidgets.QWidget()
    pcConfirmui = Ui_pcform()
    pcConfirmui.setupUi(pcConfirmwidget)

    mcConfirmwidget = QtWidgets.QWidget()
    mcConfirmui = Ui_mcForm()
    mcConfirmui.setupUi(mcConfirmwidget)

    ucWidget = QtWidgets.QWidget()
    ucUi=Ui_ucForm()
    ucUi.setupUi(ucWidget)

    sdWidget = QtWidgets.QWidget()
    sdUi = Ui_sdForm()
    sdUi.setupUi(sdWidget)

    adWidget = QtWidgets.QWidget()
    adUi = Ui_AdminForm()
    adUi.setupUi(adWidget)

    memWidget = QtWidgets.QWidget()
    memUi = Ui_memForm()
    memUi.setupUi(memWidget)

    proWidget = QtWidgets.QWidget()
    proUi = Ui_provForm()
    proUi.setupUi(proWidget)

    serWidget = QtWidgets.QWidget()
    serUi = Ui_serviceForm()
    serUi.setupUi(serWidget)
    # userwidget = QtWidgets.QWidget()
    # userui = Ui_userForm()
    # userui.setupUi(userwidget)

    sys.exit(app.exec_())
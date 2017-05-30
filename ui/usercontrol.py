# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usercontrol.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        def getSL():


        def toSDUI():


        def toMCUI():



        Form.setObjectName("Form")
        Form.resize(400, 485)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.serviceListText = QtWidgets.QPlainTextEdit(Form)
        self.serviceListText.setObjectName("serviceListText")
        self.verticalLayout.addWidget(self.serviceListText)
        self.getSL = QtWidgets.QPushButton(Form)
        self.getSL.setObjectName("getSL")
        self.verticalLayout.addWidget(self.getSL)
        self.toSDUI = QtWidgets.QPushButton(Form)
        self.toSDUI.setObjectName("toSRUI")
        self.verticalLayout.addWidget(self.toSDUI)
        self.toMCUI = QtWidgets.QPushButton(Form)
        self.toMCUI.setObjectName("toMCUI")
        self.verticalLayout.addWidget(self.toMCUI)

        self.retranslateUserControlUi(Form)
        self.getSL.clicked.connect(getSL)
        self.toSDUI.clicked.connect(toSDUI)
        self.toMCUI.clicked.connect(toMCUI)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUserControlUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Control"))
        self.getSL.setText(_translate("Form", "getServiceList"))
        self.toSDUI.setText(_translate("Form", "addServiceRecord"))
        self.toMCUI.setText(_translate("Form", "return"))


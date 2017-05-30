# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_serviceForm(object):
    def setupUi(self, serviceForm):
        def toAdminUI():

        def addService():

        serviceForm.setObjectName("Form")
        serviceForm.resize(400, 202)
        self.verticalLayout = QtWidgets.QVBoxLayout(serviceForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(serviceForm)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.codeText = QtWidgets.QLineEdit(serviceForm)
        self.codeText.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.codeText)
        self.label_2 = QtWidgets.QLabel(serviceForm)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.nameText = QtWidgets.QLineEdit(serviceForm)
        self.nameText.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.nameText)
        self.label_3 = QtWidgets.QLabel(serviceForm)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.feeText = QtWidgets.QLineEdit(serviceForm)
        self.feeText.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.feeText)
        self.addService = QtWidgets.QPushButton(serviceForm)
        self.addService.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.addService)
        self.toAdminUI = QtWidgets.QPushButton(serviceForm)
        self.toAdminUI.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.toAdminUI)

        self.retranslateserviceUi(serviceForm)
        self.addService.clicked.connect(addService)
        self.toAdminUI.clicked.connect(toAdminUI)
        QtCore.QMetaObject.connectSlotsByName(serviceForm)

    def retranslateserviceUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Service"))
        self.label.setText(_translate("Form", "code"))
        self.label_2.setText(_translate("Form", "name"))
        self.label_3.setText(_translate("Form", "fee"))
        self.addService.setText(_translate("Form", "add service"))
        self.toAdminUI.setText(_translate("Form", "return"))


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
        pcform.resize(400, 114)
        self.verticalLayout = QtWidgets.QVBoxLayout(pcform)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(pcform)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pcText = QtWidgets.QLineEdit(pcform)
        self.pcText.setObjectName("pcText")
        self.verticalLayout.addWidget(self.pcText)
        self.confirmPC = QtWidgets.QPushButton(pcform)
        self.confirmPC.setObjectName("confirmPC")
        self.verticalLayout.addWidget(self.confirmPC)
        self.toMainUI = QtWidgets.QPushButton(pcform)
        self.toMainUI.setObjectName("toMainUI")
        self.verticalLayout.addWidget(self.toMainUI)

        self.retranslatePcConfirmUi(pcform)
        self.toMainUI.clicked.connect(pcform.toMainUI)
        QtCore.QMetaObject.connectSlotsByName(pcform)

    def retranslatePcConfirmUi(self, pcform):
        _translate = QtCore.QCoreApplication.translate
        pcform.setWindowTitle(_translate("pcform", "Provider Confirm"))
        self.label.setText(_translate("pcform", "                      Enter provider code"))
        self.confirmPC.setText(_translate("pcform", "enter"))
        self.toMainUI.setText(_translate("pcform", "return"))


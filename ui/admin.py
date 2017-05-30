# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminForm(object):
    def setupUi(self, AdminForm):
        AdminForm.setObjectName("AdminForm")
        AdminForm.resize(453, 130)
        self.verticalLayout = QtWidgets.QVBoxLayout(AdminForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.toSUI = QtWidgets.QPushButton(AdminForm)
        self.toSUI.setObjectName("toSUI")
        self.gridLayout.addWidget(self.toSUI, 0, 0, 1, 1)
        self.storeManR = QtWidgets.QPushButton(AdminForm)
        self.storeManR.setObjectName("storeManR")
        self.gridLayout.addWidget(self.storeManR, 1, 0, 1, 1)
        self.storeMemR = QtWidgets.QPushButton(AdminForm)
        self.storeMemR.setObjectName("storeMemR")
        self.gridLayout.addWidget(self.storeMemR, 5, 2, 1, 1)
        self.toMainUI = QtWidgets.QPushButton(AdminForm)
        self.toMainUI.setObjectName("toMainUI")
        self.gridLayout.addWidget(self.toMainUI, 6, 0, 1, 3)
        self.toMUI = QtWidgets.QPushButton(AdminForm)
        self.toMUI.setObjectName("toMUI")
        self.gridLayout.addWidget(self.toMUI, 0, 2, 1, 1)
        self.toPUI = QtWidgets.QPushButton(AdminForm)
        self.toPUI.setObjectName("toPUI")
        self.gridLayout.addWidget(self.toPUI, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(AdminForm)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 1)
        self.storePR = QtWidgets.QPushButton(AdminForm)
        self.storePR.setObjectName("storePR")
        self.gridLayout.addWidget(self.storePR, 5, 1, 1, 1)
        self.storeB = QtWidgets.QPushButton(AdminForm)
        self.storeB.setObjectName("storeB")
        self.gridLayout.addWidget(self.storeB, 1, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(AdminForm)
        QtCore.QMetaObject.connectSlotsByName(AdminForm)

    def retranslateUi(self, AdminForm):
        _translate = QtCore.QCoreApplication.translate
        AdminForm.setWindowTitle(_translate("AdminForm", "Admin"))
        self.toSUI.setText(_translate("AdminForm", "service"))
        self.storeManR.setText(_translate("AdminForm", "storeManagerReport"))
        self.storeMemR.setText(_translate("AdminForm", "storeMemberRecord"))
        self.toMainUI.setText(_translate("AdminForm", "return"))
        self.toMUI.setText(_translate("AdminForm", "member"))
        self.toPUI.setText(_translate("AdminForm", "provider"))
        self.storePR.setText(_translate("AdminForm", "storeProviderRecord"))
        self.storeB.setText(_translate("AdminForm", "storeBill"))


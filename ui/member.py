# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'member.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 230)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 451, 215))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nameText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.nameText.setObjectName("nameText")
        self.gridLayout.addWidget(self.nameText, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.zcText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.zcText.setObjectName("zcText")
        self.gridLayout.addWidget(self.zcText, 5, 1, 1, 1)
        self.numberText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.numberText.setObjectName("numberText")
        self.gridLayout.addWidget(self.numberText, 1, 1, 1, 1)
        self.cityText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cityText.setObjectName("cityText")
        self.gridLayout.addWidget(self.cityText, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.sdText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sdText.setObjectName("sdText")
        self.gridLayout.addWidget(self.sdText, 3, 0, 1, 1)
        self.sText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sText.setObjectName("sText")
        self.gridLayout.addWidget(self.sText, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.search = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 6, 1, 1, 1)
        self.toAdminUI = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.toAdminUI.setObjectName("toAdminUI")
        self.gridLayout.addWidget(self.toAdminUI, 8, 0, 1, 2)
        self.delete_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete_2.setObjectName("delete_2")
        self.gridLayout.addWidget(self.delete_2, 6, 0, 1, 1)
        self.add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 7, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Member"))
        self.label.setText(_translate("Form", "Member street address"))
        self.label_3.setText(_translate("Form", "Member name"))
        self.label_6.setText(_translate("Form", "Member ZIP code"))
        self.label_2.setText(_translate("Form", "Member city"))
        self.label_4.setText(_translate("Form", "Member number"))
        self.label_5.setText(_translate("Form", "Member state"))
        self.search.setText(_translate("Form", "search by number"))
        self.toAdminUI.setText(_translate("Form", "return"))
        self.delete_2.setText(_translate("Form", "delete by number"))
        self.add.setText(_translate("Form", "add"))


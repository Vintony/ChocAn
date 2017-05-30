# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serviceDetail.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sdForm(object):
    def setupUi(self, sdForm):
        def addSR():



        def toUCUI():


        sdForm.setObjectName("srForm")
        sdForm.resize(400, 171)
        self.gridLayoutWidget = QtWidgets.QWidget(sdForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cdatText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cdatText.setObjectName("cdatText")
        self.gridLayout.addWidget(self.cdatText, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.sdText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sdText.setObjectName("sdText")
        self.gridLayout.addWidget(self.sdText, 1, 1, 1, 1)
        self.mnText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.mnText.setObjectName("mnText")
        self.gridLayout.addWidget(self.mnText, 3, 1, 1, 1)
        self.addServiceRecord = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addServiceRecord.setObjectName("addServiceRecord")
        self.gridLayout.addWidget(self.addServiceRecord, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.pnText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pnText.setObjectName("pnText")
        self.gridLayout.addWidget(self.pnText, 3, 0, 1, 1)
        self.toUserConUI = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.toUserConUI.setObjectName("toUserConUI")
        self.gridLayout.addWidget(self.toUserConUI, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.scText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.scText.setObjectName("scText")
        self.gridLayout.addWidget(self.scText, 5, 0, 1, 1)
        self.cText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cText.setObjectName("cText")
        self.gridLayout.addWidget(self.cText, 5, 1, 1, 1)

        self.retranslateSdUi(sdForm)
        self.addServiceRecord.clicked.connect(addSR)
        self.toUserConUI.clicked.connect(toUCUI)
        QtCore.QMetaObject.connectSlotsByName(sdForm)

    def retranslateSdUi(self, srForm):
        _translate = QtCore.QCoreApplication.translate
        srForm.setWindowTitle(_translate("srForm", "Service Detail"))
        self.label.setText(_translate("srForm", "Provider number"))
        self.label_3.setText(_translate("srForm", "Current date and time"))
        self.addServiceRecord.setText(_translate("srForm", "add"))
        self.label_4.setText(_translate("srForm", "Service date"))
        self.toUserConUI.setText(_translate("srForm", "return"))
        self.label_2.setText(_translate("srForm", "Member number"))
        self.label_5.setText(_translate("srForm", "Service code"))
        self.label_6.setText(_translate("srForm", "Comments"))


# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from functions import *

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
        proForm.resize(454, 230)
        self.gridLayoutWidget = QtWidgets.QWidget(proForm)
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
        self.modify = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.modify.setObjectName("search")
        self.gridLayout.addWidget(self.modify, 6, 1, 1, 1)
        self.toAdminUI = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.toAdminUI.setObjectName("toAdminUI")
        self.gridLayout.addWidget(self.toAdminUI, 8, 0, 1, 2)
        self.delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete.setObjectName("delete")
        self.gridLayout.addWidget(self.delete, 6, 0, 1, 1)
        self.add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 7, 0, 1, 2)

        self.retranslateProviderUi(proForm)
        self.add.clicked.connect(add)
        self.modify.clicked.connect(modify)
        self.delete.clicked.connect(delete)
        self.toAdminUI.clicked.connect(toAdminUI)
        QtCore.QMetaObject.connectSlotsByName(proForm)

    def retranslateProviderUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Provider"))
        self.label.setText(_translate("Form", "Provider street address"))
        self.label_3.setText(_translate("Form", "Provider name"))
        self.label_6.setText(_translate("Form", "Provider ZIP code"))
        self.label_2.setText(_translate("Form", "Provider city"))
        self.label_4.setText(_translate("Form", "Provider number"))
        self.label_5.setText(_translate("Form", "Provider state"))
        self.delete.setText(_translate("Form", "delete by number"))
        self.add.setText(_translate("Form", "add"))
        self.modify.setText(_translate("Form", "modify by number"))
        self.toAdminUI.setText(_translate("Form", "return"))


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
        memForm.resize(454, 230)
        self.gridLayoutWidget = QtWidgets.QWidget(memForm)
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
        self.modify = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.modify.setObjectName("search")
        self.gridLayout.addWidget(self.modify, 6, 1, 1, 1)
        self.toAdminUI = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.toAdminUI.setObjectName("toAdminUI")
        self.gridLayout.addWidget(self.toAdminUI, 8, 0, 1, 2)
        self.delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete.setObjectName("delete")
        self.gridLayout.addWidget(self.delete, 6, 0, 1, 1)
        self.add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 7, 0, 1, 2)

        self.retranslateMemberUi(memForm)
        self.add.clicked.connect(add)
        self.modify.clicked.connect(modify)
        self.delete.clicked.connect(delete)
        self.toAdminUI.clicked.connect(toAdminUI)
        QtCore.QMetaObject.connectSlotsByName(memForm)

    def retranslateMemberUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Member"))
        self.label.setText(_translate("Form", "Member street address"))
        self.label_3.setText(_translate("Form", "Member name"))
        self.label_6.setText(_translate("Form", "Member ZIP code"))
        self.label_2.setText(_translate("Form", "Member city"))
        self.label_4.setText(_translate("Form", "Member number"))
        self.label_5.setText(_translate("Form", "Member state"))
        self.delete.setText(_translate("Form", "delete by number"))
        self.add.setText(_translate("Form", "add"))
        self.modify.setText(_translate("Form", "modify by number"))
        self.toAdminUI.setText(_translate("Form", "return"))


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
        self.toMUI.setText(_translate("AdminForm", "member"))
        self.toSUI.setText(_translate("AdminForm", "service"))
        self.storePR.setText(_translate("AdminForm", "storeProviderRecord"))
        self.storeMemR.setText(_translate("AdminForm", "storeMemberRecord"))
        self.storeB.setText(_translate("AdminForm", "storeBill"))
        self.storeManR.setText(_translate("AdminForm", "storeManagerReport"))
        self.toMainUI.setText(_translate("AdminForm", "return"))
        self.toPUI.setText(_translate("AdminForm", "provider"))


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
        ucForm.resize(400, 485)
        self.verticalLayout = QtWidgets.QVBoxLayout(ucForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.serviceListText = QtWidgets.QPlainTextEdit(ucForm)
        self.serviceListText.setObjectName("serviceListText")
        self.verticalLayout.addWidget(self.serviceListText)
        self.getSL = QtWidgets.QPushButton(ucForm)
        self.getSL.setObjectName("getSL")
        self.verticalLayout.addWidget(self.getSL)
        self.toSDUI = QtWidgets.QPushButton(ucForm)
        self.toSDUI.setObjectName("toSRUI")
        self.verticalLayout.addWidget(self.toSDUI)
        self.toMCUI = QtWidgets.QPushButton(ucForm)
        self.toMCUI.setObjectName("toMCUI")
        self.verticalLayout.addWidget(self.toMCUI)

        self.retranslateUserControlUi(ucForm)
        self.getSL.clicked.connect(getSL)
        self.toSDUI.clicked.connect(toSDUI)
        self.toMCUI.clicked.connect(toMCUI)
        QtCore.QMetaObject.connectSlotsByName(ucForm)

    def retranslateUserControlUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Control"))
        self.getSL.setText(_translate("Form", "getServiceList"))
        self.toSDUI.setText(_translate("Form", "addServiceRecord"))
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
        mcForm.resize(400, 114)
        self.verticalLayout = QtWidgets.QVBoxLayout(mcForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(mcForm)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.mcText = QtWidgets.QLineEdit(mcForm)
        self.mcText.setObjectName("mcText")
        self.verticalLayout.addWidget(self.mcText)
        self.confirmMC = QtWidgets.QPushButton(mcForm)
        self.confirmMC.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.confirmMC)
        self.toProviderConfirmUI = QtWidgets.QPushButton(mcForm)
        self.toProviderConfirmUI.setObjectName("toProviderConfirmUI")
        self.verticalLayout.addWidget(self.toProviderConfirmUI)

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
        MainWindow.resize(400, 115)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.admin_button = QtWidgets.QPushButton(MainWindow)
        self.admin_button.setObjectName("admin_button")
        self.verticalLayout.addWidget(self.admin_button)
        self.user_button = QtWidgets.QPushButton(MainWindow)
        self.user_button.setEnabled(True)
        self.user_button.setObjectName("user_button")
        self.verticalLayout.addWidget(self.user_button)

        self.retranslateMainUi(MainWindow)
        self.admin_button.clicked.connect(toAdminUI)
        self.user_button.clicked.connect(topcConfirmUI)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateMainUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChocAn"))
        self.admin_button.setText(_translate("MainWindow", "Admin"))
        self.user_button.setText(_translate("MainWindow", "User"))


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
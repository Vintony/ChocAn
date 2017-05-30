# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 115)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.admin_button = QtWidgets.QPushButton(self.centralwidget)
        self.admin_button.setObjectName("admin_button")
        self.verticalLayout.addWidget(self.admin_button)
        self.user_button = QtWidgets.QPushButton(self.centralwidget)
        self.user_button.setEnabled(True)
        self.user_button.setObjectName("user_button")
        self.verticalLayout.addWidget(self.user_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChocAn"))
        self.admin_button.setText(_translate("MainWindow", "Admin"))
        self.user_button.setText(_translate("MainWindow", "User"))


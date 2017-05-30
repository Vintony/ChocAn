from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mcForm(object):
    def setupUi(self, mcForm):
        def mcConfirm():
            if validMemberNumber(self.mcText.text()):
                mcform.hide()
            else:
                mcForm.show()

        def toPCUI():
            mcForm.hide()
            pcform.show()

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
        self.toProviderConfirmUI.clicked(toPCUI)
        QtCore.QMetaObject.connectSlotsByName(mcForm)

    def retranslateMcConfirmUi(self, mcForm):
        _translate = QtCore.QCoreApplication.translate
        mcForm.setWindowTitle(_translate("mcForm", "Member Confirm"))
        self.label.setText(_translate("mcForm", "                       Enter  member code"))
        self.confirmMC.setText(_translate("mcForm", "enter"))
        self.toProviderConfirmUI.setText(_translate("mcForm", "return"))


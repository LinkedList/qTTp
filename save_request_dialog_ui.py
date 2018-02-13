# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_request_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(186, 108)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.saveRequestDialogLabel = QtWidgets.QLabel(Dialog)
        self.saveRequestDialogLabel.setObjectName("saveRequestDialogLabel")
        self.verticalLayout.addWidget(self.saveRequestDialogLabel)
        self.collections = QtWidgets.QComboBox(Dialog)
        self.collections.setEditable(True)
        self.collections.setObjectName("collections")
        self.verticalLayout.addWidget(self.collections)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Save to collection"))
        self.saveRequestDialogLabel.setText(_translate("Dialog", "Save request"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_request_dialog.ui',
# licensing of 'save_request_dialog.ui' applies.
#
# Created: Sun Feb 17 10:16:47 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

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
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Save to collection", None, -1))
        self.saveRequestDialogLabel.setText(QtWidgets.QApplication.translate("Dialog", "Save request", None, -1))


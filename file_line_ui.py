# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileLine.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FileLine(object):
    def setupUi(self, FileLine):
        FileLine.setObjectName("FileLine")
        FileLine.resize(241, 46)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FileLine)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileName = QtWidgets.QLineEdit(FileLine)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout.addWidget(self.fileName)
        self.browseButton = QtWidgets.QPushButton(FileLine)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)

        self.retranslateUi(FileLine)
        QtCore.QMetaObject.connectSlotsByName(FileLine)

    def retranslateUi(self, FileLine):
        _translate = QtCore.QCoreApplication.translate
        FileLine.setWindowTitle(_translate("FileLine", "Form"))
        self.browseButton.setText(_translate("FileLine", "Browse"))


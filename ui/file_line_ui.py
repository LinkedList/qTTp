# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileLine.ui',
# licensing of 'fileLine.ui' applies.
#
# Created: Sun Feb 17 10:15:32 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

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
        FileLine.setWindowTitle(QtWidgets.QApplication.translate("FileLine", "Form", None, -1))
        self.browseButton.setText(QtWidgets.QApplication.translate("FileLine", "Browse", None, -1))


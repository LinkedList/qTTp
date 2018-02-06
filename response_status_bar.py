# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'response_status_bar.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResponseStatusBar(object):
    def setupUi(self, ResponseStatusBar):
        ResponseStatusBar.setObjectName("ResponseStatusBar")
        self.reqStatusLayout = QtWidgets.QHBoxLayout(ResponseStatusBar)
        self.reqStatusLayout.setContentsMargins(6, -1, -1, -1)
        self.reqStatusLayout.setObjectName("reqStatusLayout")
        self.statusCode = QtWidgets.QLabel(ResponseStatusBar)
        self.statusCode.setText("")
        self.statusCode.setObjectName("statusCode")
        self.reqStatusLayout.addWidget(self.statusCode)
        self.time = QtWidgets.QLabel(ResponseStatusBar)
        self.time.setText("")
        self.time.setObjectName("time")
        self.reqStatusLayout.addWidget(self.time)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reqStatusLayout.addItem(spacerItem)

        self.retranslateUi(ResponseStatusBar)
        QtCore.QMetaObject.connectSlotsByName(ResponseStatusBar)

    def retranslateUi(self, ResponseStatusBar):
        pass


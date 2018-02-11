# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'response_info.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResponseInfo(object):
    def setupUi(self, ResponseInfo):
        ResponseInfo.setObjectName("ResponseInfo")
        ResponseInfo.resize(102, 28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResponseInfo.sizePolicy().hasHeightForWidth())
        ResponseInfo.setSizePolicy(sizePolicy)
        self.reqStatusLayout = QtWidgets.QHBoxLayout(ResponseInfo)
        self.reqStatusLayout.setContentsMargins(6, 0, -1, 0)
        self.reqStatusLayout.setSpacing(5)
        self.reqStatusLayout.setObjectName("reqStatusLayout")
        self.statusCode = QtWidgets.QLabel(ResponseInfo)
        self.statusCode.setStyleSheet("")
        self.statusCode.setText("")
        self.statusCode.setObjectName("statusCode")
        self.reqStatusLayout.addWidget(self.statusCode)
        self.time = QtWidgets.QLabel(ResponseInfo)
        self.time.setText("")
        self.time.setObjectName("time")
        self.reqStatusLayout.addWidget(self.time)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reqStatusLayout.addItem(spacerItem)

        self.retranslateUi(ResponseInfo)
        QtCore.QMetaObject.connectSlotsByName(ResponseInfo)

    def retranslateUi(self, ResponseInfo):
        pass


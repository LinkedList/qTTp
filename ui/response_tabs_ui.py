# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'response_tabs.ui',
# licensing of 'response_tabs.ui' applies.
#
# Created: Sun Feb 17 10:16:33 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ResponseTabs(object):
    def setupUi(self, ResponseStatusBar):
        ResponseStatusBar.setObjectName("ResponseStatusBar")
        self.responseTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responseTab.sizePolicy().hasHeightForWidth())
        self.responseTab.setSizePolicy(sizePolicy)
        self.responseTab.setObjectName("responseTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.responseTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.responseText = QtWidgets.QTextBrowser(self.responseTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responseText.sizePolicy().hasHeightForWidth())
        self.responseText.setSizePolicy(sizePolicy)
        self.responseText.setObjectName("responseText")
        self.verticalLayout_2.addWidget(self.responseText)
        ResponseStatusBar.addTab(self.responseTab, "")
        self.headersTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headersTab.sizePolicy().hasHeightForWidth())
        self.headersTab.setSizePolicy(sizePolicy)
        self.headersTab.setObjectName("headersTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.headersTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headersText = QtWidgets.QTextBrowser(self.headersTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headersText.sizePolicy().hasHeightForWidth())
        self.headersText.setSizePolicy(sizePolicy)
        self.headersText.setObjectName("headersText")
        self.verticalLayout_3.addWidget(self.headersText)
        ResponseStatusBar.addTab(self.headersTab, "")

        self.retranslateUi(ResponseStatusBar)
        ResponseStatusBar.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ResponseStatusBar)

    def retranslateUi(self, ResponseStatusBar):
        ResponseStatusBar.setTabText(ResponseStatusBar.indexOf(self.responseTab), QtWidgets.QApplication.translate("ResponseTabs", "Response", None, -1))
        ResponseStatusBar.setTabText(ResponseStatusBar.indexOf(self.headersTab), QtWidgets.QApplication.translate("ResponseTabs", "Headers", None, -1))


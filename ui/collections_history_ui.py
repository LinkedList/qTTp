# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collections_history.ui',
# licensing of 'collections_history.ui' applies.
#
# Created: Sun Feb 17 10:14:38 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CollectionsHistoryTabs(object):
    def setupUi(self, tabWidget):
        tabWidget.setObjectName("tabWidget")
        self.collectionsTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collectionsTab.sizePolicy().hasHeightForWidth())
        self.collectionsTab.setSizePolicy(sizePolicy)
        self.collectionsTab.setObjectName("collectionsTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.collectionsTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.collectionsTree = QtWidgets.QTreeView(self.collectionsTab)
        self.collectionsTree.setObjectName("collectionsTree")
        self.verticalLayout_2.addWidget(self.collectionsTree)
        tabWidget.addTab(self.collectionsTab, "")
        self.historyTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyTab.sizePolicy().hasHeightForWidth())
        self.historyTab.setSizePolicy(sizePolicy)
        self.historyTab.setObjectName("historyTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.historyTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.historyList = QtWidgets.QTreeView(self.historyTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyList.sizePolicy().hasHeightForWidth())
        self.historyList.setSizePolicy(sizePolicy)
        self.historyList.setObjectName("historyList")
        self.verticalLayout_3.addWidget(self.historyList)
        tabWidget.addTab(self.historyTab, "")

        self.retranslateUi(tabWidget)
        tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabWidget)

    def retranslateUi(self, tabWidget):
        tabWidget.setTabText(tabWidget.indexOf(self.collectionsTab), QtWidgets.QApplication.translate("CollectionsHistoryTabs", "Collections", None, -1))
        tabWidget.setTabText(tabWidget.indexOf(self.historyTab), QtWidgets.QApplication.translate("CollectionsHistoryTabs", "History", None, -1))


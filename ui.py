# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 1014)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(2)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.collectionsTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collectionsTab.sizePolicy().hasHeightForWidth())
        self.collectionsTab.setSizePolicy(sizePolicy)
        self.collectionsTab.setObjectName("collectionsTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.collectionsTab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.collectionsTree = QtWidgets.QTreeView(self.collectionsTab)
        self.collectionsTree.setObjectName("collectionsTree")
        self.verticalLayout_2.addWidget(self.collectionsTree)
        self.tabWidget.addTab(self.collectionsTab, "")
        self.historyTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyTab.sizePolicy().hasHeightForWidth())
        self.historyTab.setSizePolicy(sizePolicy)
        self.historyTab.setObjectName("historyTab")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.historyTab)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.historyList = QtWidgets.QListWidget(self.historyTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyList.sizePolicy().hasHeightForWidth())
        self.historyList.setSizePolicy(sizePolicy)
        self.historyList.setObjectName("historyList")
        self.verticalLayout_31.addWidget(self.historyList)
        self.tabWidget.addTab(self.historyTab, "")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.method = QtWidgets.QComboBox(self.layoutWidget)
        self.method.setObjectName("method")
        self.method.addItem("")
        self.method.addItem("")
        self.horizontalLayout.addWidget(self.method)
        self.url = QtWidgets.QLineEdit(self.layoutWidget)
        self.url.setObjectName("url")
        self.horizontalLayout.addWidget(self.url)
        self.sendButton = QtWidgets.QPushButton(self.layoutWidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget1 = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget1.setObjectName("tabWidget1")
        self.responseTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responseTab.sizePolicy().hasHeightForWidth())
        self.responseTab.setSizePolicy(sizePolicy)
        self.responseTab.setObjectName("responseTab")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.responseTab)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.responseText = QtWidgets.QTextBrowser(self.responseTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responseText.sizePolicy().hasHeightForWidth())
        self.responseText.setSizePolicy(sizePolicy)
        self.responseText.setObjectName("responseText")
        self.verticalLayout_21.addWidget(self.responseText)
        self.tabWidget1.addTab(self.responseTab, "")
        self.headersTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headersTab.sizePolicy().hasHeightForWidth())
        self.headersTab.setSizePolicy(sizePolicy)
        self.headersTab.setObjectName("headersTab")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.headersTab)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.headersText = QtWidgets.QTextBrowser(self.headersTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headersText.sizePolicy().hasHeightForWidth())
        self.headersText.setSizePolicy(sizePolicy)
        self.headersText.setObjectName("headersText")
        self.verticalLayout_32.addWidget(self.headersText)
        self.tabWidget1.addTab(self.headersTab, "")
        self.verticalLayout.addWidget(self.tabWidget1)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.collectionsTab), _translate("MainWindow", "Collections"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.historyTab), _translate("MainWindow", "History"))
        self.method.setItemText(0, _translate("MainWindow", "GET"))
        self.method.setItemText(1, _translate("MainWindow", "POST"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.responseTab), _translate("MainWindow", "Response"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.headersTab), _translate("MainWindow", "Headers"))


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
        MainWindow.resize(1384, 609)
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
        self.collectionsSplitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collectionsSplitter.sizePolicy().hasHeightForWidth())
        self.collectionsSplitter.setSizePolicy(sizePolicy)
        self.collectionsSplitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.collectionsSplitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.collectionsSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.collectionsSplitter.setHandleWidth(2)
        self.collectionsSplitter.setObjectName("collectionsSplitter")
        self.collectionsHistoryLayoutWidget = QtWidgets.QWidget(self.collectionsSplitter)
        self.collectionsHistoryLayoutWidget.setObjectName("collectionsHistoryLayoutWidget")
        self.collectionsHistoryLayout = QtWidgets.QVBoxLayout(self.collectionsHistoryLayoutWidget)
        self.collectionsHistoryLayout.setContentsMargins(0, 0, 0, 0)
        self.collectionsHistoryLayout.setObjectName("collectionsHistoryLayout")
        self.requestSplitter = QtWidgets.QSplitter(self.collectionsSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requestSplitter.sizePolicy().hasHeightForWidth())
        self.requestSplitter.setSizePolicy(sizePolicy)
        self.requestSplitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.requestSplitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.requestSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.requestSplitter.setHandleWidth(2)
        self.requestSplitter.setObjectName("requestSplitter")
        self.layoutWidget = QtWidgets.QWidget(self.requestSplitter)
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
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.horizontalLayout.addWidget(self.method)
        self.url = QtWidgets.QLineEdit(self.layoutWidget)
        self.url.setClearButtonEnabled(True)
        self.url.setObjectName("url")
        self.horizontalLayout.addWidget(self.url)
        self.sendButton = QtWidgets.QPushButton(self.layoutWidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.saveButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.inputHeadersTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputHeadersTab.sizePolicy().hasHeightForWidth())
        self.inputHeadersTab.setSizePolicy(sizePolicy)
        self.inputHeadersTab.setObjectName("inputHeadersTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.inputHeadersTab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputHeaders = QtWidgets.QTableWidget(self.inputHeadersTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputHeaders.sizePolicy().hasHeightForWidth())
        self.inputHeaders.setSizePolicy(sizePolicy)
        self.inputHeaders.setRowCount(0)
        self.inputHeaders.setColumnCount(2)
        self.inputHeaders.setObjectName("inputHeaders")
        item = QtWidgets.QTableWidgetItem()
        self.inputHeaders.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inputHeaders.setHorizontalHeaderItem(1, item)
        self.inputHeaders.horizontalHeader().setVisible(False)
        self.inputHeaders.horizontalHeader().setCascadingSectionResizes(True)
        self.inputHeaders.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.inputHeaders)
        self.tabWidget.addTab(self.inputHeadersTab, "")
        self.reqBodyTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqBodyTab.sizePolicy().hasHeightForWidth())
        self.reqBodyTab.setSizePolicy(sizePolicy)
        self.reqBodyTab.setObjectName("reqBodyTab")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.reqBodyTab)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formDataButton = QtWidgets.QRadioButton(self.reqBodyTab)
        self.formDataButton.setObjectName("formDataButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.formDataButton)
        self.horizontalLayout_2.addWidget(self.formDataButton)
        self.formUrlEncodedButton = QtWidgets.QRadioButton(self.reqBodyTab)
        self.formUrlEncodedButton.setObjectName("formUrlEncodedButton")
        self.buttonGroup.addButton(self.formUrlEncodedButton)
        self.horizontalLayout_2.addWidget(self.formUrlEncodedButton)
        self.rawButton = QtWidgets.QRadioButton(self.reqBodyTab)
        self.rawButton.setObjectName("rawButton")
        self.buttonGroup.addButton(self.rawButton)
        self.horizontalLayout_2.addWidget(self.rawButton)
        self.binaryButton = QtWidgets.QRadioButton(self.reqBodyTab)
        self.binaryButton.setObjectName("binaryButton")
        self.buttonGroup.addButton(self.binaryButton)
        self.horizontalLayout_2.addWidget(self.binaryButton)
        self.comboBox = QtWidgets.QComboBox(self.reqBodyTab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_21.addLayout(self.horizontalLayout_2)
        self.requestBody = QtWidgets.QTextEdit(self.reqBodyTab)
        self.requestBody.setObjectName("requestBody")
        self.verticalLayout_21.addWidget(self.requestBody)
        self.tabWidget.addTab(self.reqBodyTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.layoutWidget2 = QtWidgets.QWidget(self.requestSplitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.responseLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.responseLayout.setContentsMargins(0, 5, 0, 5)
        self.responseLayout.setObjectName("responseLayout")
        self.verticalLayout_3.addWidget(self.collectionsSplitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1384, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "qTTp"))
        self.method.setItemText(0, _translate("MainWindow", "GET"))
        self.method.setItemText(1, _translate("MainWindow", "POST"))
        self.method.setItemText(2, _translate("MainWindow", "PUT"))
        self.method.setItemText(3, _translate("MainWindow", "PATCH"))
        self.method.setItemText(4, _translate("MainWindow", "DELETE"))
        self.method.setItemText(5, _translate("MainWindow", "COPY"))
        self.method.setItemText(6, _translate("MainWindow", "HEAD"))
        self.method.setItemText(7, _translate("MainWindow", "OPTIONS"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        item = self.inputHeaders.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Key"))
        item = self.inputHeaders.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inputHeadersTab), _translate("MainWindow", "Headers"))
        self.formDataButton.setText(_translate("MainWindow", "form-data"))
        self.formUrlEncodedButton.setText(_translate("MainWindow", "&x-www-form-urlencoded"))
        self.rawButton.setText(_translate("MainWindow", "raw"))
        self.binaryButton.setText(_translate("MainWindow", "binar&y"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Text"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Text (text/plain)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "JSON (application/json)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Javascript (application/javascript)"))
        self.comboBox.setItemText(4, _translate("MainWindow", "XML (application/xml)"))
        self.comboBox.setItemText(5, _translate("MainWindow", "XML (text/xml)"))
        self.comboBox.setItemText(6, _translate("MainWindow", "HTML (text/html)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reqBodyTab), _translate("MainWindow", "Request body"))


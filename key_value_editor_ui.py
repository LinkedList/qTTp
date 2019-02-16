# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_value_editor.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_keyValueEditor(object):
    def setupUi(self, keyValueEditor):
        keyValueEditor.setObjectName("keyValueEditor")
        keyValueEditor.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(keyValueEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.keyValueEditorTable = QtWidgets.QTableWidget(keyValueEditor)
        self.keyValueEditorTable.setShowGrid(True)
        self.keyValueEditorTable.setRowCount(1)
        self.keyValueEditorTable.setColumnCount(3)
        self.keyValueEditorTable.setObjectName("keyValueEditorTable")
        self.keyValueEditorTable.horizontalHeader().setVisible(False)
        self.keyValueEditorTable.horizontalHeader().setCascadingSectionResizes(False)
        self.keyValueEditorTable.horizontalHeader().setDefaultSectionSize(100)
        self.keyValueEditorTable.horizontalHeader().setStretchLastSection(True)
        self.keyValueEditorTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.keyValueEditorTable)

        self.retranslateUi(keyValueEditor)
        QtCore.QMetaObject.connectSlotsByName(keyValueEditor)

    def retranslateUi(self, keyValueEditor):
        _translate = QtCore.QCoreApplication.translate
        keyValueEditor.setWindowTitle(_translate("keyValueEditor", "KeyValueEditor"))


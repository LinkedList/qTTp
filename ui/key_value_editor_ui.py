# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_value_editor.ui',
# licensing of 'key_value_editor.ui' applies.
#
# Created: Sun Feb 17 10:15:49 2019
#      by: pyside2-uic  running on PySide2 5.12.1
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
        self.keyValueEditorTable.setColumnCount(3)
        self.keyValueEditorTable.setRowCount(1)
        self.keyValueEditorTable.horizontalHeader().setVisible(False)
        self.keyValueEditorTable.horizontalHeader().setCascadingSectionResizes(False)
        self.keyValueEditorTable.horizontalHeader().setDefaultSectionSize(100)
        self.keyValueEditorTable.horizontalHeader().setStretchLastSection(True)
        self.keyValueEditorTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.keyValueEditorTable)

        self.retranslateUi(keyValueEditor)
        QtCore.QMetaObject.connectSlotsByName(keyValueEditor)

    def retranslateUi(self, keyValueEditor):
        keyValueEditor.setWindowTitle(QtWidgets.QApplication.translate("keyValueEditor", "KeyValueEditor", None, -1))


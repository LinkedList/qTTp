# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enironment.ui',
# licensing of 'enironment.ui' applies.
#
# Created: Sun Feb 17 10:15:13 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_environmentForm(object):
    def setupUi(self, environmentForm):
        environmentForm.setObjectName("environmentForm")
        environmentForm.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(environmentForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.environmentCombo = QtWidgets.QComboBox(environmentForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.environmentCombo.sizePolicy().hasHeightForWidth())
        self.environmentCombo.setSizePolicy(sizePolicy)
        self.environmentCombo.setEditable(True)
        self.environmentCombo.setObjectName("environmentCombo")
        self.horizontalLayout.addWidget(self.environmentCombo)
        self.environmentEdit = QtWidgets.QPushButton(environmentForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.environmentEdit.sizePolicy().hasHeightForWidth())
        self.environmentEdit.setSizePolicy(sizePolicy)
        self.environmentEdit.setObjectName("environmentEdit")
        self.horizontalLayout.addWidget(self.environmentEdit)

        self.retranslateUi(environmentForm)
        QtCore.QMetaObject.connectSlotsByName(environmentForm)

    def retranslateUi(self, environmentForm):
        environmentForm.setWindowTitle(QtWidgets.QApplication.translate("environmentForm", "Form", None, -1))
        self.environmentEdit.setText(QtWidgets.QApplication.translate("environmentForm", "Edit Env.", None, -1))


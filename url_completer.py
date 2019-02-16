from PySide2.QtCore import Qt
from PySide2.QtWidgets import QStyledItemDelegate, QLineEdit, QCompleter
from PySide2.QtGui import QStandardItemModel, QStandardItem


class UrlCompleter(QCompleter):
    def __init__(self, parent=None):
        super(UrlCompleter, self).__init__(parent)
        self.model = QStandardItemModel()
        self.setModel(self.model)
        self.setCompletionRole(Qt.EditRole)
        self.setCaseSensitivity(Qt.CaseInsensitive)

    def addItem(self, reqObject):
        self.model.appendRow(QStandardItem(reqObject.url))
        self.model.appendRow(QStandardItem(reqObject.buildUrl()))

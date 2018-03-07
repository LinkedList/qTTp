from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from key_value_editor_ui import Ui_keyValueEditor


class KeyValueEditor(QWidget, Ui_keyValueEditor):

    def __init__(self):
        super(KeyValueEditor, self).__init__()
        self.setupUi(self)

        self.table = self.keyValueEditorTable
        self.table.setColumnWidth(0, 28)
        self.table.setItem(0, 0, self.createCheckBoxItem())
        self.table.cellChanged.connect(self.maybeAddRow)

    def createCheckBoxItem(self):
        checkbox = QTableWidgetItem(True)
        checkbox.setCheckState(Qt.Checked)
        return checkbox

    def maybeAddRow(self):
        count = self.table.rowCount()
        if count == self.countRowsWithKeys():
            self.table.insertRow(count)
            self.table.setItem(count, 0, self.createCheckBoxItem())

    def countRowsWithKeys(self):
        rowCount = 0
        for row in range(0, self.table.rowCount()):
            item = self.table.item(row, 1)
            if item != None and item.text() != "":
                rowCount += 1

        return rowCount


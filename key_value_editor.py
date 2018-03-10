from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMenu
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

        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.menu)

    def rowEmpty(self, row):
        key = self.table.item(row, 1)
        value = self.table.item(row, 2)
        return key == None or value == None or key.text() == "" or value.text() == ""

    def menu(self, position):
        menu = QMenu()
        item = self.table.itemAt(position)
        if item:
            deleteAction = menu.addAction("Delete")
            action = menu.exec_(self.table.mapToGlobal(position))
            if action == deleteAction:
                self.removeRow(item)

    def removeRow(self, item):
        self.table.removeRow(item.row())
        self.maybeAddRow()

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

    def getData(self):
        data = {}
        for row in range(0, self.table.rowCount()):
            checked = self.table.item(row, 0)
            key = self.table.item(row, 1)
            value = self.table.item(row, 2)
            if key != None and key.text() != "" and value != None and value.text() != "":
                data[key.text()] = {}
                data[key.text()]['value'] = value.text()
                data[key.text()]['active'] = checked.checkState() == Qt.Checked

        return data


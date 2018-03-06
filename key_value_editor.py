from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from key_value_editor_ui import Ui_keyValueEditor


class KeyValueEditor(QWidget, Ui_keyValueEditor):

    def __init__(self):
        super(KeyValueEditor, self).__init__()
        self.setupUi(self)

        self.table = self.keyValueEditorTable

        checkbox = QTableWidgetItem(True)
        checkbox.setCheckState(Qt.Checked)
        self.table.setItem(0, 0, checkbox)
        self.table.setColumnWidth(0, 28)


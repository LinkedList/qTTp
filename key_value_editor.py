from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from key_value_editor_ui import Ui_keyValueEditor


class KeyValueEditor(QWidget, Ui_keyValueEditor):

    def __init__(self):
        super(KeyValueEditor, self).__init__()
        self.setupUi(self)

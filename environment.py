from environment_ui import Ui_environmentForm
from PyQt5.QtWidgets import QWidget, QDialog
from key_value_editor import KeyValueEditor


class EnvironmentSwitcher(QWidget, Ui_environmentForm):
    def __init__(self):
        super(EnvironmentSwitcher, self).__init__()
        self.setupUi(self)
        
        self.environmentEdit.clicked.connect(self.editCurrEnvironment)

    def editCurrEnvironment(self):
        self.dialog = QDialog()
        self.dialog.exec_()
        kv = KeyValueEditor()
        self.dialog.addWidget(kv)
        self.dialog.show()

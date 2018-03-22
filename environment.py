from environment_ui import Ui_environmentForm
from PyQt5.QtWidgets import QWidget


class EnvironmentSwitcher(QWidget, Ui_environmentForm):
    def __init__(self):
        super(EnvironmentSwitcher, self).__init__()
        self.setupUi(self)

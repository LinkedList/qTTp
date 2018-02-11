from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from status_bar_ui import Ui_StatusBar

class StatusBar(QWidget, Ui_StatusBar):

    cancel_request = pyqtSignal()

    def __init__(self):
        super(StatusBar, self).__init__()
        self.setupUi(self)
        self.cancelButton.clicked.connect(self.onCancel)
        self.disable()

    def onCancel(self):
        self.cancel_request.emit()
        self.disable()

    def enable(self):
        self.cancelButton.setEnabled(True)
        self.requestProgress.setRange(0, 0)

    def disable(self):
        self.cancelButton.setEnabled(False)
        self.requestProgress.setRange(0, 1)

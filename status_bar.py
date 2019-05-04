from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from ui.status_bar_ui import Ui_StatusBar


class StatusBar(QWidget, Ui_StatusBar):

    cancel_request = Signal()

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

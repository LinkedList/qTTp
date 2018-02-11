from http.client import responses
from response_info_ui import Ui_ResponseInfo
from PyQt5.QtWidgets import QWidget

class ResponseInfo(QWidget, Ui_ResponseInfo):
    def __init__(self):
        super(ResponseInfo, self).__init__()
        self.setupUi(self)

    def translateStatus(self, code):
        self.statusCode.setText(str(code) + " " + responses[code])
        if 100 <= code < 200:
            stylesheet = "QLabel { background-color : #0074D9; color : white; padding: 5px}"
        elif 200 <= code < 300:
            stylesheet = "QLabel { background-color : #2ECC40; color : white; padding: 5px}"
        elif 300 <= code < 400:
            stylesheet = "QLabel { background-color : #FF851B; color : white; padding: 5px}"
        else:
            stylesheet = "QLabel { background-color : #FF4136; color : white; padding: 5px}"
        self.statusCode.setStyleSheet(stylesheet)

    def reset(self):
        self.statusCode.setStyleSheet("QLabel { background-color : none}")
        self.statusCode.setText("")
        self.time.setText("")

    def setTime(self, elapsed_seconds):
        self.time.setText(str(int(elapsed_seconds * 1000)) + " ms")

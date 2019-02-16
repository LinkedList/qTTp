from http.client import responses
from response_info_ui import Ui_ResponseInfo
from PySide2.QtWidgets import QWidget


class ResponseInfo(QWidget, Ui_ResponseInfo):
    def __init__(self):
        super(ResponseInfo, self).__init__()
        self.setupUi(self)

    def translateStatus(self, code):
        self.statusCode.setText(str(code) + " " + responses[code])
        if 100 <= code < 200:
            stylesheet = self.stylesheet("#0074D9")
        elif 200 <= code < 300:
            stylesheet = self.stylesheet("#2ECC40")
        elif 300 <= code < 400:
            stylesheet = self.stylesheet("#FF851B")
        else:
            stylesheet = self.stylesheet("#FF4136")
        self.statusCode.setStyleSheet(stylesheet)

    def reset(self):
        self.statusCode.setStyleSheet("QLabel { background-color : none}")
        self.statusCode.setText("")
        self.time.setText("")
        self.contentType.setText("")

    def setTime(self, elapsed_seconds):
        self.time.setText(str(int(elapsed_seconds * 1000)) + " ms")

    def setContentType(self, contentType):
        self.contentType.setText(contentType)

    def stylesheet(self, color):
        return "QLabel { background-color: " + color + "; color: white; padding: 4px}"

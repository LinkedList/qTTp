import requests
from req import Req
from requests import Response
from PyQt5.QtCore import QThread, pyqtSignal

class ReqThread(QThread):

    request_done = pyqtSignal(Response, Req)
    request_stopped = pyqtSignal()

    def __init__(self, reqObject):
        QThread.__init__(self)
        self.reqObject = reqObject

    def run(self):
        if self.reqObject.isBinary():
            data = open(self.reqObject.file, 'rb').read()
        else:
            data = self.reqObject.body

        response = requests.request(
                method=self.reqObject.method,
                url=self.reqObject.buildUrl(),
                headers=self.reqObject.headers,
                data=data)
        self.request_done.emit(response, self.reqObject)

    def stop(self):
        self.exit()
        self.request_stopped.emit()

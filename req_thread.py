import requests
from req import Req
from requests import Response
from PySide2.QtCore import QThread, Signal


class ReqThread(QThread):

    request_done = Signal(Response, Req)
    request_stopped = Signal()

    def __init__(self, reqObject):
        QThread.__init__(self)
        self.reqObject = reqObject

    def run(self):
        response = self.reqObject.buildRequestAndCall()
        self.request_done.emit(response, self.reqObject)

    def stop(self):
        self.exit()
        self.request_stopped.emit()

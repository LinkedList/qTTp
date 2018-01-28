#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json

import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow)

from ui import Ui_MainWindow


class Qttp(Ui_MainWindow):
    def __init__(self, w):
        Ui_MainWindow.__init__(self)
        self.setupUi(w)
        self.url.setFocus()

        self.sendButton.clicked.connect(self.request)
        self.url.returnPressed.connect(self.request)

    def request(self):
        r = requests.get('https://' + self.url.text())
        headers = r.headers
        headersText = ""
        for key in headers:
            headersText += "<b>" + key +"</b>" + ": " + headers[key] + "<br />"
        j = r.text
        parse = json.loads(j)
        dump = json.dumps(obj = parse, indent=4).replace(" ", "&nbsp;").replace("\n", "<br />")
        self.responseText.setHtml(dump)
        self.headersText.setHtml(headersText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    prog = Qttp(window)
    window.show()
    sys.exit(app.exec_())

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow)
from json2html import *

from ui import Ui_MainWindow


class Qttp(Ui_MainWindow):
    def __init__(self, w):
        Ui_MainWindow.__init__(self)
        self.setupUi(w)

        self.sendButton.clicked.connect(self.request)
        self.url.returnPressed.connect(self.request)

    def request(self):
        r = requests.get('https://' + self.url.text())
        j = r.text
        parse = json.loads(j)
        self.responseText.setHtml(json2html.convert(json=parse))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    prog = Qttp(window)
    window.show()
    sys.exit(app.exec_())

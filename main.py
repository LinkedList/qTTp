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

        self.sendButton.clicked.connect(self.request)
        self.url.returnPressed.connect(self.request)

    def request(self):
        r = requests.get('https://' + self.url.text())
        j = r.text
        parse = json.loads(j)
        dump = json.dumps(obj = parse, indent=4).replace(" ", "&nbsp;").replace("\n", "<br />")
        print(dump)
        self.responseText.setHtml(dump)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    prog = Qttp(window)
    window.show()
    sys.exit(app.exec_())

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import requests
import json
from json2html import *

from ui import Ui_MainWindow

from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QApplication, QPushButton, QTextBrowser, QDialog, QMainWindow)

class Qttp(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)
        self.setupUi(window)

        self.sendButton.clicked.connect(self.request)
        self.url.returnPressed.connect(self.request)

    def request(self):
        r = requests.get('https://' + self.url.text())
        j = r.text
        parse = json.loads(j)
        self.responseText.setHtml(json2html.convert(json = parse))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    prog = Qttp(window)
    window.show()
    sys.exit(app.exec_())

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()

#         def initUI(self):

#             self.qle = QLineEdit(self)
#             button = QPushButton("Send", self)
#             button.move(0, 50)
#             button.clicked.connect(self.buttonClicked)

#             self.browser = QTextBrowser(self)
#             self.browser.move(0, 100)

#             self.qle.move(0, 0)

#             self.setGeometry(300, 300, 280, 170)
#             self.setWindowTitle('QLineEdit')
#             self.show()

#         def buttonClicked(self):
#             print(self.qle.text())
#             r = requests.get('https://' + self.qle.text())
#             print(r.text)
#             self.browser.setPlainText(r.text)


# if __name__ == '__main__':

#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

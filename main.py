#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows text which 
is entered in a QLineEdit
in a QLabel widget.
 
Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
import requests
import urllib.request

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication, QPushButton, QTextBrowser)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.qle = QLineEdit(self)
        button = QPushButton("Send", self)
        button.move(0, 50)
        button.clicked.connect(self.buttonClicked)

        self.browser = QTextBrowser(self)
        self.browser.move(0, 100)
        
        self.qle.move(0, 0)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()
        
        
    def buttonClicked(self):
        print(self.qle.text())
        r = requests.get('https://' + self.qle.text())
        print(r.text)
        self.browser.setPlainText(r.text)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

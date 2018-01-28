#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json

import requests
from PyQt5 import QtCore
from PyQt5.QtGui import (QStandardItemModel, QStandardItem)
from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QListWidgetItem, QMenu)

from ui import Ui_MainWindow

class Req(object):
    def __init__(self, method, protocol, url):
        super(Req, self).__init__()               
        self.method = method
        self.url = url

class Qttp(Ui_MainWindow):
    def __init__(self, w):
        Ui_MainWindow.__init__(self)
        self.setupUi(w)
        self.url.setFocus()

        self.sendButton.clicked.connect(self.request)
        self.url.returnPressed.connect(self.request)
        self.historyList.doubleClicked.connect(self.setFromHistory)
        self.historyList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.historyList.customContextMenuRequested.connect(self.historyMenu)
        self.splitter.setSizes([1, 3])

        self.collectionsModel = QStandardItemModel()
        self.collectionsModel.appendRow(QStandardItem("Default"))
        self.collectionsTree.setModel(self.collectionsModel)
        self.collectionsTree.header().hide()

    def addCollectionItem(self, collection, item):
        items = self.collectionsModel.findItems(collection)
        parent = None
        if not items:
            parent = QStandardItem(collection)
        else:
            parent = items.pop(0)

        parent.appendRow(QStandardItem(item.method + " " + item.url))

    def request(self):
        method = self.method.currentText()
        url = self.url.text()
        protocol = 'https'
        r = requests.request(method=method, url=protocol+"://"+url)
        historyItem = QListWidgetItem()
        historyItem.setText(method + " " + url)
        historyItem.setData(QtCore.Qt.UserRole, Req(method, protocol, url))
        self.historyList.insertItem(0, historyItem)
        headers = r.headers
        headersText = ""
        for key in headers:
            headersText += "<b>" + key +"</b>"+ ": " + headers[key] + "<br />"
        j = r.text
        parse = json.loads(j)
        dump = json.dumps(obj = parse, indent=4).replace(" ", "&nbsp;").replace("\n", "<br />")
        self.responseText.setHtml(dump)
        self.headersText.setHtml(headersText)

    def setFromHistory(self, item):
        req = item.data(QtCore.Qt.UserRole)
        self.url.setText(req.url)
        index = self.method.findText(req.method)
        self.method.setCurrentIndex(index)

    def historyMenu(self, position):
        menu = QMenu()
        saveAction = menu.addAction("Save")
        action = menu.exec_(self.historyList.mapToGlobal(position))
        if action == saveAction:
            item = self.historyList.itemAt(position)
            self.addCollectionItem("Default", item.data(QtCore.Qt.UserRole))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    prog = Qttp(window)
    window.show()
    sys.exit(app.exec_())

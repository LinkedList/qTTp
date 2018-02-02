#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json

import requests
from http.client import responses
from urllib.parse import urlparse
from PyQt5 import QtCore
from PyQt5.QtGui import (QStandardItemModel, QStandardItem)
from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QListWidgetItem, QMenu, QHeaderView, QTableWidgetItem)

from ui import Ui_MainWindow

class Req(object):
    def __init__(self, method, protocol, url, headers):
        super(Req, self).__init__()               
        self.method = method
        self.protocol = protocol
        self.url = url
        self.headers = headers

    def buildUrl(self):
        return self.protocol + "://" + self.url

    def buildTextRepresentation(self):
        return self.method + " " + self.url

class Qttp(Ui_MainWindow):
    def __init__(self, w):
        Ui_MainWindow.__init__(self)
        self.setupUi(w)
        self.url.setFocus()

        self.sendButton.clicked.connect(self.request)
        self.saveButton.clicked.connect(self.saveRequest)
        self.url.returnPressed.connect(self.request)
        self.historyList.doubleClicked.connect(self.setFromHistory)
        self.historyList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.historyList.customContextMenuRequested.connect(self.historyMenu)
        self.resizeInputHeadersHeader()
        self.inputHeaders.setColumnCount(2)
        self.inputHeaders.setRowCount(1)
        self.inputHeaders.setHorizontalHeaderLabels(["Key", "Value"])
        self.inputHeaders.cellDoubleClicked.connect(self.addHeaderRow)
        self.splitter.setSizes([1, 3])

        self.collectionsModel = QStandardItemModel()
        self.collectionsModel.appendRow(QStandardItem("Default"))
        self.collectionsTree.setModel(self.collectionsModel)
        self.collectionsTree.header().hide()
        self.collectionsTree.doubleClicked.connect(self.setFromHistory)

    def resizeInputHeadersHeader(self):
        header = self.inputHeaders.horizontalHeader()
        for column in range(header.count()):
            header.setSectionResizeMode(column, QHeaderView.Stretch)

    def addHeaderRow(self):
        count = self.inputHeaders.rowCount()
        item = self.inputHeaders.item(count -1, 0)
        if item:
            self.inputHeaders.setRowCount(count + 1)

    def addCollectionItem(self, collection, item):
        items = self.collectionsModel.findItems(collection)
        parent = None
        if not items:
            parent = QStandardItem(collection)
        else:
            parent = items.pop(0)

        newItem = QStandardItem(item.method + " " + item.url)
        newItem.setData(item, QtCore.Qt.UserRole)
        parent.appendRow(newItem)

    def getInputHeaders(self):
        returnDict = {}
        rows = self.inputHeaders.rowCount()
        for row in range(0, rows):
            key = self.inputHeaders.item(row, 0)
            value = self.inputHeaders.item(row, 1)
            if key and value and key.text() and value.text():
                returnDict[key.text()] = value.text()
        return returnDict
            

    def buildReqObject(self):
        method = self.method.currentText()
        parsedUrl = urlparse(self.url.text())
        protocol = parsedUrl.scheme or "https"
        url = parsedUrl.netloc + parsedUrl.path
        headers = self.getInputHeaders()
        return Req(method, protocol, url, headers)

    def request(self):
        self.reset()
        reqObject = self.buildReqObject()
        r = requests.request(method=reqObject.method, url=reqObject.buildUrl(), headers=reqObject.headers)
        historyItem = QListWidgetItem()
        historyItem.setText(reqObject.buildTextRepresentation())
        historyItem.setData(QtCore.Qt.UserRole, reqObject)
        self.historyList.insertItem(0, historyItem)
        headers = r.headers
        headersText = ""
        self.translateStatus(r.status_code)
        self.setTime(r.elapsed.total_seconds())
        for key in sorted(headers):
            headersText += "<b>" + key +"</b>"+ ": " + headers[key] + "<br />"
        j = r.text
        parse = json.loads(j)
        dump = json.dumps(obj = parse, indent=4).replace(" ", "&nbsp;").replace("\n", "<br />")
        self.responseText.setHtml(dump)
        self.headersText.setHtml(headersText)

    def reset(self):
        self.statusCode.setText("")
        self.time.setText("")

    def saveRequest(self):
        item = self.buildReqObject()
        self.addCollectionItem("Default", item)

    def setFromHistory(self, item):
        req = item.data(QtCore.Qt.UserRole)
        self.url.setText(req.buildUrl())
        index = self.method.findText(req.method)
        self.method.setCurrentIndex(index)
        self.setInputHeadersFromHistory(req.headers)

    def setInputHeadersFromHistory(self, headers):
        self.inputHeaders.setRowCount(0)
        for key, value in headers.items():
            rowCount = self.inputHeaders.rowCount()
            self.inputHeaders.insertRow(rowCount)
            self.inputHeaders.setItem(rowCount, 0, QTableWidgetItem(key))
            self.inputHeaders.setItem(rowCount, 1, QTableWidgetItem(value))
        self.inputHeaders.insertRow(self.inputHeaders.rowCount())

    def historyMenu(self, position):
        menu = QMenu()
        saveAction = menu.addAction("Save")
        action = menu.exec_(self.historyList.mapToGlobal(position))
        if action == saveAction:
            item = self.historyList.itemAt(position)
            self.addCollectionItem("Default", item.data(QtCore.Qt.UserRole))

    def translateStatus(self, code):
        self.statusCode.setText(str(code) + " " + responses[code])
        if code >= 100 and code < 200:
            self.statusCode.setStyleSheet("QLabel { background-color : #0074D9; color : white; padding: 5px}")
        elif code >= 200 and code < 300:
            self.statusCode.setStyleSheet("QLabel { background-color : #2ECC40; color : white; padding: 5px}")
        elif code >= 300 and code < 400:
            self.statusCode.setStyleSheet("QLabel { background-color : #FF851B; color : white; padding: 5px}")
        else:
            self.statusCode.setStyleSheet("QLabel { background-color : #FF4136; color : white; padding: 5px}")

    def setTime(self, elapsed_seconds):
        self.time.setText(str(int(elapsed_seconds * 1000)) + " ms")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    prog = Qttp(window)
    window.show()
    sys.exit(app.exec_())

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from builtins import staticmethod

import requests
from response_status_bar import Ui_ResponseStatusBar
from response_tabs import Ui_ResponseTabs
from req import Req
from requests import Response
from http.client import responses
from urllib.parse import urlparse
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import (QStandardItemModel, QStandardItem)
from PyQt5.QtWidgets import (
        QWidget, QProgressBar, QTabWidget, QPushButton,
        QApplication, QMainWindow, QListWidgetItem, QMenu, QHeaderView, QTableWidgetItem)

from ui import Ui_MainWindow

class CancelRequest(QPushButton):

    cancel_request = pyqtSignal()

    def __init__(self):
        super(CancelRequest, self).__init__()
        self.setText("Cancel")
        self.clicked.connect(self.onCancel)

    def onCancel(self):
        self.cancel_request.emit()


class StatusBarProgress(QProgressBar):
    def __init__(self):
        super(StatusBarProgress, self).__init__()
        self.setRange(0, 1)

    def start(self):
        self.setRange(0, 0)

    def end(self):
        self.setRange(0, 1)


class ResponseStatusBarWidget(QWidget, Ui_ResponseStatusBar):
    def __init__(self):
        super(ResponseStatusBarWidget, self).__init__()
        self.setupUi(self)

    def translateStatus(self, code):
        self.statusCode.setText(str(code) + " " + responses[code])
        if 100 <= code < 200:
            stylesheet = "QLabel { background-color : #0074D9; color : white; padding: 5px}"
        elif 200 <= code < 300:
            stylesheet = "QLabel { background-color : #2ECC40; color : white; padding: 5px}"
        elif 300 <= code < 400:
            stylesheet = "QLabel { background-color : #FF851B; color : white; padding: 5px}"
        else:
            stylesheet = "QLabel { background-color : #FF4136; color : white; padding: 5px}"
        self.statusCode.setStyleSheet(stylesheet)

    def reset(self):
        self.statusCode.setStyleSheet("QLabel { background-color : none}")
        self.statusCode.setText("")
        self.time.setText("")

    def setTime(self, elapsed_seconds):
        self.time.setText(str(int(elapsed_seconds * 1000)) + " ms")

class ResponseTabsWidget(QTabWidget, Ui_ResponseTabs):
    def __init__(self):
        super(ResponseTabsWidget, self).__init__()
        self.setupUi(self)

    def setHeaders(self, headers):
        headersText = ""
        for key in sorted(headers):
            headersText += "<b>" + key +"</b>"+ ": " + headers[key] + "<br />"
        self.headersText.setHtml(headersText)

    def setResponseBody(self, response):
        if 'application/json' in response.headers['content-type']:
            body = self.parseJson(response)
            self.responseText.setHtml(body)
        else:
            body = response.text
            self.responseText.setPlainText(body)

    @staticmethod
    def parseJson(response):
        try:
            response.json()
            j = response.text
            parse = json.loads(j)
            dump = json.dumps(obj = parse, indent=4).replace(" ", "&nbsp;").replace("\n", "<br />")
            return dump
        except ValueError:
            return ""


class ReqThread(QThread):

    request_done = pyqtSignal(Response, Req)
    request_stopped = pyqtSignal()

    def __init__(self, reqObject):
        QThread.__init__(self)
        self.reqObject = reqObject

    def run(self):
        response = requests.request(method=self.reqObject.method, url=self.reqObject.buildUrl(), headers=self.reqObject.headers)
        self.request_done.emit(response, self.reqObject)

    def stop(self):
        self.exit()
        self.request_stopped.emit()

class Qttp(Ui_MainWindow):
    def __init__(self, w):
        Ui_MainWindow.__init__(self)
        self.setupUi(w)
        w.setWindowTitle("qTTp")

        self.progress = StatusBarProgress()
        self.cancelButton = CancelRequest()
        self.statusbar.addPermanentWidget(self.progress)
        self.statusbar.addPermanentWidget(self.cancelButton)

        self.responseStatus = ResponseStatusBarWidget()
        self.responseLayout.addWidget(self.responseStatus)

        self.responseTabs = ResponseTabsWidget()
        self.responseLayout.addWidget(self.responseTabs)

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
        self.inputHeaders.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.inputHeaders.customContextMenuRequested.connect(self.headersMenu)
        self.collectionsSplitter.setSizes([100, 500])

        self.historyModel = QStandardItemModel()
        self.historyList.setModel(self.historyModel)
        self.historyList.header().hide()
        self.historyList.expandToDepth(0)
        self.historyList.doubleClicked.connect(self.setFromHistory)

        self.collectionsModel = QStandardItemModel()
        self.collectionsModel.appendRow(QStandardItem("Default"))
        self.collectionsTree.setModel(self.collectionsModel)
        self.collectionsTree.header().hide()
        self.collectionsTree.expandToDepth(0)
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

    def removeHeaderRow(self, item):
        self.inputHeaders.removeRow(item.row())

    def addCollectionItem(self, collection, item):
        items = self.collectionsModel.findItems(collection)
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
        self.responseStatus.reset()
        reqObject = self.buildReqObject()
        self.thread = ReqThread(reqObject)
        self.thread.request_done.connect(self.afterRequest)
        self.thread.request_stopped.connect(self.afterStoppedRequest)
        self.cancelButton.cancel_request.connect(self.thread.stop)
        self.progress.start()
        self.thread.start()

    def afterStoppedRequest(self):
        self.progress.end()

    def afterRequest(self, response, reqObject):
        self.progress.end()
        self.insertToHistory(response, reqObject)
        self.responseStatus.translateStatus(response.status_code)
        self.responseStatus.setTime(response.elapsed.total_seconds())
        self.responseTabs.setHeaders(response.headers)
        self.responseTabs.setResponseBody(response)

    def insertToHistory(self, response, reqObject):
        parents = self.historyModel.findItems(str(reqObject.date))
        if not parents:
            parent = QStandardItem(str(reqObject.date))
            self.historyModel.appendRow(parent)
        else:
            parent = parents.pop()

        historyItem = QStandardItem(reqObject.buildTextRepresentation())
        historyItem.setData(reqObject, QtCore.Qt.UserRole)
        parent.insertRow(0, historyItem)

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
            index = self.historyList.indexAt(position)
            item = self.historyModel.itemFromIndex(index)
            self.addCollectionItem("Default", item.data(QtCore.Qt.UserRole))

    def headersMenu(self, position):
        menu = QMenu()
        deleteAction = menu.addAction("Delete")
        action = menu.exec_(self.inputHeaders.mapToGlobal(position))
        if action == deleteAction:
            item = self.inputHeaders.itemAt(position)
            if item:
                self.removeHeaderRow(item)



    def setTime(self, elapsed_seconds):
        self.time.setText(str(int(elapsed_seconds * 1000)) + " ms")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    prog = Qttp(window)
    window.show()
    sys.exit(app.exec_())

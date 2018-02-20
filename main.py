#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from configparser import ConfigParser
from builtins import staticmethod

import requests
from req_thread import ReqThread
from collections_history_tabs import CollectionsHistoryTabs
from headers_completer import HeadersCompleter
from url_completer import UrlCompleter
from response_info import ResponseInfo
from response_tabs import Ui_ResponseTabs
from status_bar import StatusBar
from req import Req
from requests import Response
from http.client import responses
from urllib.parse import urlparse
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import (QStandardItemModel, QStandardItem, QIcon)
from PyQt5.QtWidgets import (
        QWidget, QProgressBar, QTabWidget, QPushButton, QCompleter, QStyledItemDelegate, QLineEdit,
        QApplication, QMainWindow, QListWidgetItem, QMenu, QHeaderView, QTableWidgetItem)


from ui import Ui_MainWindow

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

class Qttp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Qttp, self).__init__()
        self.setupUi(self)

        self.prepareConfig()

        self.statusBar = StatusBar()
        self.statusbar.addPermanentWidget(self.statusBar)

        self.responseInfo = ResponseInfo()
        self.responseLayout.addWidget(self.responseInfo)

        self.responseTabs = ResponseTabsWidget()
        self.responseLayout.addWidget(self.responseTabs)

        self.url.setFocus()
        self.sendButton.clicked.connect(self.request)
        self.saveButton.clicked.connect(self.saveRequest)
        self.url.returnPressed.connect(self.request)
        self.resizeInputHeadersHeader()
        self.inputHeaders.setColumnCount(2)
        self.inputHeaders.setRowCount(1)
        self.inputHeaders.setHorizontalHeaderLabels(["Key", "Value"])
        self.inputHeaders.cellDoubleClicked.connect(self.addHeaderRow)
        self.inputHeaders.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.inputHeaders.customContextMenuRequested.connect(self.headersMenu)

        headersDelegate = HeadersCompleter(self.inputHeaders)
        self.inputHeaders.setItemDelegateForColumn(0, headersDelegate) 

        self.urlCompleter = UrlCompleter(self.url)
        self.url.setCompleter(self.urlCompleter)

        self.collectionsHistoryTabs = CollectionsHistoryTabs()
        self.collectionsHistoryTabs.set_item.connect(self.setFromHistory)
        self.collectionsHistoryLayout.addWidget(self.collectionsHistoryTabs)

        self.mainSplitter.setSizes(self.getMainSplitterSizes())

        self.disableRequestBody()

        self.method.currentTextChanged.connect(self.onMethodChange)

    def getMainSplitterSizes(self):
        config = self.config
        config.read('config.ini')
        sizes = config['splitter']['sizes']
        if sizes:
            return map(int, sizes.split(","))

        return []

    def prepareConfig(self):
        config = ConfigParser()
        config.read('config.ini')
        if not config.has_section('splitter'):
            config['splitter'] = {}

        if not config.has_option('splitter', 'sizes'):
            config['splitter']['sizes'] = ",".join(map(str, [200, 400, 400]))

        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        self.config = config

    def enableRequestBody(self):
        bodyTabIndex = self.tabWidget.indexOf(self.reqBodyTab)
        self.tabWidget.setTabEnabled(bodyTabIndex, True)

    def disableRequestBody(self):
        bodyTabIndex = self.tabWidget.indexOf(self.reqBodyTab)
        self.tabWidget.setTabEnabled(bodyTabIndex, False)

    def onMethodChange(self, httpMethod):
        if httpMethod == "GET":
            self.disableRequestBody()
        else:
            self.enableRequestBody()

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
        body =  self.requestBody.toPlainText()
        return Req(method, protocol, url, headers, body)

    def request(self):
        self.responseInfo.reset()
        reqObject = self.buildReqObject()
        self.thread = ReqThread(reqObject)
        self.thread.request_done.connect(self.afterRequest)
        self.thread.request_stopped.connect(self.afterStoppedRequest)
        self.statusBar.cancel_request.connect(self.thread.stop)
        self.statusBar.enable()
        self.thread.start()

    def afterStoppedRequest(self):
        self.statusBar.disable()

    def afterRequest(self, response, reqObject):
        self.statusBar.disable()
        self.urlCompleter.addItem(reqObject)
        self.collectionsHistoryTabs.insertToHistory(response, reqObject)
        self.responseInfo.translateStatus(response.status_code)
        self.responseInfo.setTime(response.elapsed.total_seconds())
        self.responseInfo.setContentType(response.headers["content-type"])
        self.responseTabs.setHeaders(response.headers)
        self.responseTabs.setResponseBody(response)

    def saveRequest(self):
        item = self.buildReqObject()
        self.collectionsHistoryTabs._saveRequest(item)

    def setFromHistory(self, req):
        self.url.setText(req.buildUrl())
        index = self.method.findText(req.method)
        self.method.setCurrentIndex(index)
        self.setInputHeadersFromHistory(req.headers)
        self.requestBody.setText(req.body)

    def setInputHeadersFromHistory(self, headers):
        self.inputHeaders.setRowCount(0)
        for key, value in headers.items():
            rowCount = self.inputHeaders.rowCount()
            self.inputHeaders.insertRow(rowCount)
            self.inputHeaders.setItem(rowCount, 0, QTableWidgetItem(key))
            self.inputHeaders.setItem(rowCount, 1, QTableWidgetItem(value))
        self.inputHeaders.insertRow(self.inputHeaders.rowCount())

    def headersMenu(self, position):
        menu = QMenu()
        deleteAction = menu.addAction("Delete")
        action = menu.exec_(self.inputHeaders.mapToGlobal(position))
        if action == deleteAction:
            item = self.inputHeaders.itemAt(position)
            if item:
                self.removeHeaderRow(item)

    def closeEvent(self, event):
        config = self.config
        config['splitter']['sizes'] =  ",".join(map(str, self.mainSplitter.sizes()))
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def setTime(self, elapsed_seconds):
        self.time.setText(str(int(elapsed_seconds * 1000)) + " ms")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Qttp()
    prog.show()
    sys.exit(app.exec_())

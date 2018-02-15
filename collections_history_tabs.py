from collections_history_ui import Ui_CollectionsHistoryTabs
from save_to_collection_dialog import SaveToCollectionDialog
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QTabWidget, QMenu
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from req import Req

class CollectionsHistoryTabs(QTabWidget, Ui_CollectionsHistoryTabs):
        
    set_item = pyqtSignal(Req)

    def __init__(self):
        super(CollectionsHistoryTabs, self).__init__()
        self.setupUi(self)

        self.historyList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.historyList.customContextMenuRequested.connect(self.historyMenu)
    
        self.historyModel = QStandardItemModel()
        self.historyList.setModel(self.historyModel)
        self.historyList.header().hide()
        self.historyList.expandToDepth(0)
        self.historyList.doubleClicked.connect(self.emitItem)

        self.collectionsModel = QStandardItemModel()
        default = QStandardItem("Default")
        default.setIcon(QIcon("folder.svg"))
        self.collectionsModel.appendRow(default)
        self.collectionsTree.setModel(self.collectionsModel)
        self.collectionsTree.header().hide()
        self.collectionsTree.expandToDepth(0)
        self.collectionsTree.doubleClicked.connect(self.emitItem)
        self.collectionsTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.collectionsTree.customContextMenuRequested.connect(self.collectionsMenu)

    def emitItem(self, item):
        req = item.data(Qt.UserRole)
        self.set_item.emit(req)

    def getCollections(self):
        collections = []
        for row in range(0, self.collectionsModel.rowCount()):
            collections.append(self.collectionsModel.item(row).text())
        return collections

    def collectionsMenu(self, position):
        menu = QMenu()
        deleteAction = menu.addAction("Delete")
        action = menu.exec_(self.historyList.mapToGlobal(position))
        if action == deleteAction:
            index = self.collectionsTree.indexAt(position)
            item = self.collectionsModel.itemFromIndex(index)
            if item:
                parent = item.parent()
                parent.removeRow(index.row())

    def historyMenu(self, position):
        menu = QMenu()
        saveAction = menu.addAction("Save")
        deleteAction = menu.addAction("Delete")
        action = menu.exec_(self.historyList.mapToGlobal(position))
        if action == saveAction:
            index = self.historyList.indexAt(position)
            item = self.historyModel.itemFromIndex(index)
            self._saveRequest(item.data(Qt.UserRole))
        elif action == deleteAction:
            index = self.historyList.indexAt(position)
            item = self.historyModel.itemFromIndex(index)
            if item:
                parent = item.parent()
                parent.removeRow(index.row())

    def _saveRequest(self, item):
        self.saveDialog = SaveToCollectionDialog(self.getCollections())
        self.saveDialog.exec_()
        collection = self.saveDialog.collections.currentText()
        if collection:
            self.addCollectionItem(collection, item)

    def insertToHistory(self, response, reqObject):
        parents = self.historyModel.findItems(str(reqObject.date))
        if not parents:
            parent = QStandardItem(str(reqObject.date))
            self.historyModel.appendRow(parent)
        else:
            parent = parents.pop()

        historyItem = QStandardItem(reqObject.buildTextRepresentation())
        historyItem.setData(reqObject, Qt.UserRole)
        parent.insertRow(0, historyItem)

    def addCollectionItem(self, collection, item):
        items = self.collectionsModel.findItems(collection)
        if not items:
            parent = QStandardItem(collection)
            parent.setIcon(QIcon('folder.svg'))
            self.collectionsModel.appendRow(parent)
        else:
            parent = items.pop(0)

        newItem = QStandardItem(item.method + " " + item.url)
        newItem.setData(item, Qt.UserRole)
        parent.appendRow(newItem)

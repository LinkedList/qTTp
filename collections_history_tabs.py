from ui.collections_history_ui import Ui_CollectionsHistoryTabs
from save_to_collection_dialog import SaveToCollectionDialog
from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QTabWidget, QMenu
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
from req import Req


class CollectionsHistoryTabs(QTabWidget, Ui_CollectionsHistoryTabs):

    set_item = Signal(Req)

    folder_icon = QIcon("folder.svg")

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
        default.setEditable(False)
        default.setIcon(self.folder_icon)
        self.collectionsModel.appendRow(default)
        self.collectionsTree.setModel(self.collectionsModel)
        self.collectionsTree.header().hide()
        self.collectionsTree.expandToDepth(0)
        self.collectionsTree.doubleClicked.connect(self.emitItem)
        self.collectionsTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.collectionsTree.customContextMenuRequested.connect(
            self.collectionsMenu)

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
        maybeSelected = self.collectionsTree.selectedIndexes()
        if maybeSelected:
            collection = self.collectionsModel.item(
                maybeSelected[0].row()).text()
        else:
            self.saveDialog = SaveToCollectionDialog(self.getCollections())
            self.saveDialog.exec_()
            collection = self.saveDialog.collections.currentText()
        if collection:
            self.addCollectionItem(collection, item)

    def insertToHistory(self, response, reqObject):
        parents = self.historyModel.findItems(str(reqObject.date))
        if not parents:
            parent = QStandardItem(str(reqObject.date))
            parent.setEditable(False)
            self.historyModel.appendRow(parent)
        else:
            parent = parents.pop()

        historyItem = QStandardItem()
        historyItem.setText(reqObject.buildTextRepresentation())
        historyItem.setEditable(False)
        historyItem.setData(reqObject, Qt.UserRole)
        parent.insertRow(0, [historyItem]) #seems like a hack inserting list here, possilby report

    def addCollectionItem(self, collection, item):
        items = self.collectionsModel.findItems(collection)
        if not items:
            parent = QStandardItem(collection)
            parent.setEditable(False)
            parent.setIcon(self.folder_icon)
            self.collectionsModel.appendRow(parent)
        else:
            parent = items.pop(0)

        newItem = QStandardItem()
        newItem.setText(item.method + " " + item.url)
        newItem.setEditable(False)
        newItem.setData(item, Qt.UserRole)
        parent.appendRow(newItem)

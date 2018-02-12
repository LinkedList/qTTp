from save_request_dialog_ui import Ui_Dialog
from PyQt5.QtWidgets import QDialog

class SaveToCollectionDialog(Ui_Dialog, QDialog):
    def __init__(self, collections=None):
        super(SaveToCollectionDialog, self).__init__()
        self.setupUi(self)
        self.collections.addItem("")
        for collection in collections:
            self.collections.addItem(collection)

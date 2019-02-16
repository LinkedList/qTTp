from file_line_ui import Ui_FileLine
from PySide2.QtWidgets import QWidget, QFileDialog


class FileLine(QWidget, Ui_FileLine):
    def __init__(self):
        super(FileLine, self).__init__()
        self.setupUi(self)
        self.browseButton.clicked.connect(self.selectFile)

    def selectFile(self):
        selectedFile = QFileDialog.getOpenFileName()
        self.fileName.setText(selectedFile[0])

    def getFile(self):
        return self.fileName.text().strip()

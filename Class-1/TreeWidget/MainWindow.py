###
# PyQt6 tree widget main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTreeView
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'TreeWidget'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainlayout = QVBoxLayout()

        self.infoLabel = QLabel("Selected Item: None", self)
        self.infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.treeView = QTreeView(self)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Items'])

        # Add some data.
        rootItem = self.model.invisibleRootItem()

        # Add first level menu.
        item1 = QStandardItem('Item 1')
        item2 = QStandardItem('Item 2')
        item3 = QStandardItem('Item 3')

        # Add second level menu.
        item1_1 = QStandardItem('Item 1.1')
        item1_2 = QStandardItem('Item 1.2')
        item2_1 = QStandardItem('Item 2.1')

        # Add item to model.
        rootItem.appendRow(item1)
        rootItem.appendRow(item2)
        rootItem.appendRow(item3)

        item1.appendRow(item1_1)
        item1.appendRow(item1_2)
        item2.appendRow(item2_1)

        self.treeView.setModel(self.model)

        self.button = QPushButton("Show Selected Item", self)
        self.button.clicked.connect(self.showSelectedItem)

        mainlayout.addWidget(self.infoLabel)
        mainlayout.addWidget(self.treeView)
        mainlayout.addWidget(self.button)

        self.setLayout(mainlayout)
    # }

    def showSelectedItem(self):
    # {
        # Get current selected item.
        index = self.treeView.currentIndex()

        if index.isValid():
            item = self.model.itemFromIndex(index)
            self.infoLabel.setText(f"Selected Item: {item.text()}")
        else:
            self.infoLabel.setText("Selected Item: None")
    # }
# }

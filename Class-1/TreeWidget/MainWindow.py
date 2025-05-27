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

        mainLayout = QVBoxLayout()

        self.labelInfo = QLabel("Selected Item: None", self)
        self.labelInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.treeView = QTreeView(self)
        self.itemModel = QStandardItemModel()
        self.itemModel.setHorizontalHeaderLabels(['Items'])

        # Add some data.
        rootItem = self.itemModel.invisibleRootItem()

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

        self.treeView.setModel(self.itemModel)

        self.btnShow = QPushButton("Show Selected Item", self)
        self.btnShow.clicked.connect(self.showSelectedItem)

        mainLayout.addWidget(self.labelInfo)
        mainLayout.addWidget(self.treeView)
        mainLayout.addWidget(self.btnShow)

        self.setLayout(mainLayout)
    # }

    def showSelectedItem(self):
    # {
        # Get current selected item.
        index = self.treeView.currentIndex()

        if index.isValid():
            item = self.itemModel.itemFromIndex(index)
            self.labelInfo.setText(f"Selected Item: {item.text()}")
        else:
            self.labelInfo.setText("Selected Item: None")
    # }
# }

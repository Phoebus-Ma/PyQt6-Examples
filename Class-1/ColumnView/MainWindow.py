###
# PyQt6 ColumnView main window.
#
# License - MIT.
###

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QColumnView
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ColumnView'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        layout = QVBoxLayout()

        # Create a QColumnView.
        self.columnView = QColumnView()

        # Create a QStandardItemModel to provide data.
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Description'])

        # Add some data to model.
        self.populateModel()

        # ColumnView setup model.
        self.columnView.setModel(self.model)

        layout.addWidget(self.columnView)
        self.setLayout(layout)
    # }

    def populateModel(self):
    # {
        # Create root node.
        rootItem = self.model.invisibleRootItem()

        # Add data.
        for i in range(3):
            # Create parent item.
            parentItem = QStandardItem(f'Parent {i}')

            # Create parent description.
            parentDescription = QStandardItem(f'Description for Parent {i}')

            # Add child item.
            for j in range(2):
                # Create child item.
                childItem = QStandardItem(f'Child {i}-{j}')

                # Create child description.
                childDescription = QStandardItem(f'Description for Child {i}-{j}')

                # Add child item to parent.
                parentItem.appendRow([childItem, childDescription])

            # Add parent item to root node.
            rootItem.appendRow([parentItem, parentDescription])
    # }
# }

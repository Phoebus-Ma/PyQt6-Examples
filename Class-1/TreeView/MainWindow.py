###
# PyQt6 TreeView main window.
#
# License - MIT.
###

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTreeView
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'TreeView'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        layout = QVBoxLayout()

        # Create QTreeView.
        self.treeView = QTreeView()

        # Create a QStandardItemModel, used to provide data.
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Description'])

        # Add some data to model.
        self.populateModel()

        # TreeView setup model.
        self.treeView.setModel(self.model)

        layout.addWidget(self.treeView)
        self.setLayout(layout)
    # }

    def populateModel(self):
    # {
        # Create root node.
        rootItem = self.model.invisibleRootItem()

        # Add data architecture.
        for i in range(3):
            # Create parent item.
            parentItem = QStandardItem(f'Parent {i}')

            # Create description item.
            parentDescription = QStandardItem(f'Hello P-{i}')

            # Add child item to parent item.
            for j in range(2):
                childItem = QStandardItem(f'Child {i}-{j}')
                childItem.setToolTip(f'This is child {i}-{j}')

                # Create description item.
                childDescription = QStandardItem(f'Hello C-{i}-{j}')

                parentItem.appendRow([childItem, childDescription])

            # Add parent item to root node.
            rootItem.appendRow([parentItem, parentDescription])

        # Expand all item.
        self.treeView.expandAll()
    # }
# }

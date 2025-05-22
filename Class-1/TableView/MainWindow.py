###
# PyQt6 TableView main window.
#
# License - MIT.
###

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableView
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'TableView'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        layout = QVBoxLayout()

        # Create a QTableView.
        self.tableView = QTableView()

        # Create a QStandardItemModel for data.
        self.model = QStandardItemModel(4, 3)       # 4 lines, 3 columns.
        self.model.setHorizontalHeaderLabels(['Name', 'Age', 'Occupation'])

        # Add data to mode.
        self.populateModel()

        # TableView setup the model.
        self.tableView.setModel(self.model)

        layout.addWidget(self.tableView)
        self.setLayout(layout)
    # }

    def populateModel(self):
    # {
        # Add data.
        data = [
            ['Alice'  , '24', 'Engineer'],
            ['Bob'    , '30', 'Designer'],
            ['Charlie', '28', 'Teacher' ],
            ['Diana'  , '35', 'Doctor'  ]
        ]

        for row in range(len(data)):
            for col in range(len(data[row])):
                item = QStandardItem(data[row][col])
                self.model.setItem(row, col, item)
    # }
# }

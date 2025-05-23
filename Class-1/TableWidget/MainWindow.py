###
# PyQt6 table widget main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QLabel,
    QPushButton
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'TableWidget'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainlayout = QVBoxLayout()

        self.infoLabel = QLabel("Selected Cell: None", self)
        self.infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a table widget.
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(3)             # lines.
        self.tableWidget.setColumnCount(3)          # columns.
        self.tableWidget.setHorizontalHeaderLabels(
            ['Column 1', 'Column 2', 'Column 3'])   # Header.

        # Add data to table.
        for row in range(3):
            for column in range(3):
                item = QTableWidgetItem(f"Item {row+1}-{column+1}")
                self.tableWidget.setItem(row, column, item)

        self.button = QPushButton("Show Selected Cell", self)
        self.button.clicked.connect(self.showSelectedCell)

        mainlayout.addWidget(self.infoLabel)
        mainlayout.addWidget(self.tableWidget)
        mainlayout.addWidget(self.button)

        self.setLayout(mainlayout)
    # }

    def showSelectedCell(self):
    # {
        # Get current selected item.
        selectedItems = self.tableWidget.selectedItems()

        if selectedItems:
            # Get the contents of the first selected cell.
            selectedItem = selectedItems[0]
            self.infoLabel.setText(f"Selected Cell: {selectedItem.text()}")
        else:
            self.infoLabel.setText("Selected Cell: None")
    # }
# }

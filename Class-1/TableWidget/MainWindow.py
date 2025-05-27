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

        mainLayout = QVBoxLayout()

        self.labelInfo = QLabel("Selected Cell: None", self)
        self.labelInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.btnShow = QPushButton("Show Selected Cell", self)
        self.btnShow.clicked.connect(self.showSelectedCell)

        mainLayout.addWidget(self.labelInfo)
        mainLayout.addWidget(self.tableWidget)
        mainLayout.addWidget(self.btnShow)

        self.setLayout(mainLayout)
    # }

    def showSelectedCell(self):
    # {
        # Get current selected item.
        selectedItems = self.tableWidget.selectedItems()

        if selectedItems:
            # Get the contents of the first selected cell.
            selectedItem = selectedItems[0]
            self.labelInfo.setText(f"Selected Cell: {selectedItem.text()}")
        else:
            self.labelInfo.setText("Selected Cell: None")
    # }
# }

###
# PyQt6 list widget main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QListWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ListWidget'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QVBoxLayout()

        # Create label for show selected item.
        self.labelInfo = QLabel("Selected Item: None", self)
        self.labelInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create list widget.
        self.listWidget = QListWidget(self)
        self.listWidget.addItems(
            ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        )

        # Create button for get selected item.
        self.btnSelect = QPushButton("Show Selected Item", self)
        self.btnSelect.clicked.connect(self.showSelectedItem)

        mainLayout.addWidget(self.labelInfo)
        mainLayout.addWidget(self.listWidget)
        mainLayout.addWidget(self.btnSelect)

        self.setLayout(mainLayout)
    # }

    def showSelectedItem(self):
    # {
        # Get current selected item.
        selectedItem = self.listWidget.currentItem()

        if selectedItem:
            self.labelInfo.setText(f"Selected Item: {selectedItem.text()}")
        else:
            self.labelInfo.setText("Selected Item: None")
    # }
# }

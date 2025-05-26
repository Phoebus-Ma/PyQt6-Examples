###
# PyQt6 input dialog window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QInputDialog
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'InputDialog'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create layout.
        mainlayout = QVBoxLayout()

        btnText = QPushButton("Get Text")
        btnText.clicked.connect(self.getText)
        mainlayout.addWidget(btnText)

        btnInt = QPushButton("Get Integer")
        btnInt.clicked.connect(self.getInt)
        mainlayout.addWidget(btnInt)

        btnDouble = QPushButton("Get Float")
        btnDouble.clicked.connect(self.getDouble)
        mainlayout.addWidget(btnDouble)

        btnItem = QPushButton("Select Item")
        btnItem.clicked.connect(self.getItem)
        mainlayout.addWidget(btnItem)

        btnMulti = QPushButton("Multi-Line Text")
        btnMulti.clicked.connect(self.getMultiLineText)
        mainlayout.addWidget(btnMulti)

        container = QWidget()
        container.setLayout(mainlayout)
        self.setCentralWidget(container)
    # }

    def getText(self):
    # {
        text, ok = QInputDialog.getText(
            self,
            "Text input",
            "Input name:",
        )

        if ok:
            self.statusBar().showMessage(f"Input text: {text}")
            print(f"Text: {text}")
    # }

    def getInt(self):
    # {
        num, ok = QInputDialog.getInt(
            self,
            "Integer input",
            "Input age (0-150):",
            min=0,
            max=150,
            step=1
        )

        if ok:
            self.statusBar().showMessage(f"Input integer: {num}")
            print(f"Integer: {num}")
    # }

    def getDouble(self):
    # {
        num, ok = QInputDialog.getDouble(
            self,
            "Float input",
            "Enter weight (Kg):",
            min=0.0,
            max=300.0,
            decimals=1
        )

        if ok:
            self.statusBar().showMessage(f"Input double float: {num}")
            print(f"Double: {num}")
    # }

    def getItem(self):
    # {
        items = ["Python", "Java", "C++", "JavaScript"]
        item, ok = QInputDialog.getItem(
            self,
            "Select item",
            "Select program:",
            items,
            editable=False
        )

        if ok:
            self.statusBar().showMessage(f"Select item: {item}")
            print(f"Item: {item}")
    # }

    def getMultiLineText(self):
    # {
        text, ok = QInputDialog.getMultiLineText(
            self,
            "Multi-Line Text",
            "Address:",
            "Default address..."
        )

        if ok:
            self.statusBar().showMessage(f"Input multi-line text: {text}")
            print(f"Multi-line Text: {text}")
    # }
# }

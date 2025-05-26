###
# PyQt6 table window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QTabWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'TabWindow'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create QTabWidget.
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Crate 3 tab window.
        self.createTab1()
        self.createTab2()
        self.createTab3()
    # }

    """First table page"""
    def createTab1(self):
    # {
        tab = QWidget()
        firstLayout = QVBoxLayout()

        label = QLabel("This is first page.")
        button = QPushButton("Click Test")
        button.clicked.connect(lambda: print("Clicked page 1."))

        firstLayout.addWidget(label)
        firstLayout.addWidget(button)
        tab.setLayout(firstLayout)

        self.tabs.addTab(tab, "Tab1")
    # }

    """Second table page"""
    def createTab2(self):
    # {
        tab = QWidget()
        secondLayout = QVBoxLayout()

        # Control.
        self.input = QLineEdit()
        button = QPushButton("Show input content")
        button.clicked.connect(self.showInputContent)

        secondLayout.addWidget(QLabel("input:"))
        secondLayout.addWidget(self.input)
        secondLayout.addWidget(button)
        tab.setLayout(secondLayout)

        self.tabs.addTab(tab, "Tab2")
    # }

    """Third table page"""
    def createTab3(self):
    # {
        tab = QWidget()

        thirdLayout = QVBoxLayout()
        thirdLayout.addWidget(QLabel("This is page 3."))
        tab.setLayout(thirdLayout)

        self.tabs.addTab(tab, "Tab3")
    # }

    def showInputContent(self):
    # {
        content = self.input.text()
        print(f"Input: {content}")
        self.input.clear()
    # }
# }

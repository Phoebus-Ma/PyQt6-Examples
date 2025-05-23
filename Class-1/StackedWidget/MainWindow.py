###
# PyQt6 stacked widget main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'StackedWidget'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainlayout = QVBoxLayout()

        # Create a stacked widget.
        self.stackedWidget = QStackedWidget(self)

        # Create 3 pages.
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()

        # Add label for every page.
        label1 = QLabel("This is Page 1", self.page1)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label2 = QLabel("This is Page 2", self.page2)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label3 = QLabel("This is Page 3", self.page3)
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add pages to stacked widget.
        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)
        self.stackedWidget.addWidget(self.page3)

        # Create button for switch page.
        self.button1 = QPushButton("Show Page 1", self)
        self.button2 = QPushButton("Show Page 2", self)
        self.button3 = QPushButton("Show Page 3", self)

        # Button slot.
        self.button1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.button2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.button3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        mainlayout.addWidget(self.stackedWidget)
        mainlayout.addWidget(self.button1)
        mainlayout.addWidget(self.button2)
        mainlayout.addWidget(self.button3)

        self.setLayout(mainlayout)
    # }
# }

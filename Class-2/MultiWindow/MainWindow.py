###
# PyQt6 main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QPushButton
)

from AboutWindow import AboutWindow


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'MainWindow'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create laytou.
        mainLayout = QVBoxLayout()

        # Create button.
        self.btnOpen = QPushButton("Go to about window", self)
        self.btnOpen.clicked.connect(self.openChildWindow)
        mainLayout.addWidget(self.btnOpen)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)
    # }

    def openChildWindow(self):
    # {
        # Hide main window.
        self.hide()

        # Create about window and passes main windows parameters.
        self.childWindow = AboutWindow(self)
        self.childWindow.show()
    # }
# }

###
# PyQt6 about window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QPushButton
)


class AboutWindow(QMainWindow):
# {
    def __init__(self, parentWindow):
    # {
        super().__init__()

        self.title     = 'AboutWindow'
        self.winWidth  = 320
        self.winHeight = 240

        self.parentWindow = parentWindow  # Save parent window reference.
        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create layout.
        aboutLayout = QVBoxLayout()

        self.labelText = QLabel('This is about window.')
        aboutLayout.addWidget(self.labelText)

        self.btnReturn = QPushButton("Return main window", self)
        self.btnReturn.clicked.connect(self.returnToMain)
        aboutLayout.addWidget(self.btnReturn)

        container = QWidget()
        container.setLayout(aboutLayout)
        self.setCentralWidget(container)
    # }

    def returnToMain(self):
    # {
        self.parentWindow.show()    # Show parent window.
        self.close()                # Close about window.
    # }
# }

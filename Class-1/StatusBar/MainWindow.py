###
# PyQt6 StatusBar main window.
#
# License - MIT.
###

from datetime import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QStatusBar
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'StatusBar'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setFixedSize(self.winWidth, self.winHeight)

        mainWidget = QWidget()
        layout = QVBoxLayout()

        # Create status bar（auto add to bottom).
        self.statusBar = QStatusBar()
        self.statusLabel = QLabel('Ready')
        self.statusBar.addPermanentWidget(self.statusLabel)

        self.setStatusBar(self.statusBar)

        # Create button.
        btn = QPushButton('Update', self)
        btn.clicked.connect(self.updateStatus)

        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)

        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)

        # Initilize display information.
        self.statusBar.showMessage('Welcome', 3000)
    # }

    '''Button slot handler'''
    def updateStatus(self):
    # {
        self.statusBar.showMessage('Status: ' + self.getCurrentTime())

        self.statusLabel.setText('Last: ' + self.getCurrentTime())
    # }
    
    '''Get current time'''
    def getCurrentTime(self):
    # {
        return datetime.now().strftime('%H:%M:%S')
    # }
# }

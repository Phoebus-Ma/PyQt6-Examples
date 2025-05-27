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
        mainLayout = QVBoxLayout()

        # Create status bar（auto add to bottom).
        self.statusBar = QStatusBar()
        self.labelStatus = QLabel('Ready')
        self.statusBar.addPermanentWidget(self.labelStatus)

        self.setStatusBar(self.statusBar)

        # Create button.
        btnUpdate = QPushButton('Update', self)
        btnUpdate.clicked.connect(self.updateStatus)

        mainLayout.addWidget(btnUpdate, alignment=Qt.AlignmentFlag.AlignCenter)

        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        # Initilize display information.
        self.statusBar.showMessage('Welcome', 3000)
    # }

    '''Button slot handler'''
    def updateStatus(self):
    # {
        self.statusBar.showMessage('Status: ' + self.getCurrentTime())

        self.labelStatus.setText('Last: ' + self.getCurrentTime())
    # }
    
    '''Get current time'''
    def getCurrentTime(self):
    # {
        return datetime.now().strftime('%H:%M:%S')
    # }
# }

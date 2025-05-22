###
# PyQt6 main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QWidget, \
    QVBoxLayout, QMessageBox, QCommandLinkButton
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'CmdLinkButton'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        layout = self.createLayout()

        self.setLayout(layout)
    # }

    def createLayout(self) -> QVBoxLayout:
    # {
        vLayout = QVBoxLayout()

        # Open button.
        btnOpen = QCommandLinkButton('Open', 'Click here for open file', self)
        btnOpen.setIcon(QIcon.fromTheme('document-open'))
        btnOpen.clicked.connect(lambda: self.showMessage('open'))

        vLayout.addWidget(btnOpen)

        # Save button.
        btnSave = QCommandLinkButton('Save', 'click here for save file', self)
        btnSave.setIcon(QIcon.fromTheme('document-save'))
        btnSave.clicked.connect(lambda: self.showMessage('save'))

        vLayout.addWidget(btnSave)

        return vLayout
    # }

    def showMessage(self, text):
    # {
        QMessageBox.information(self, 'Tips', f'You click: {text}')
    # }
# }

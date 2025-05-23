###
# PyQt6 main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QToolButton,
    QMenu,
    QMessageBox
)
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ToolButton'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QVBoxLayout()

        # Create button.
        toolBtn = QToolButton(self)
        toolBtn.setGeometry(50, 50, 100, 40)
        toolBtn.setText('Menu')
        toolBtn.setIcon(QIcon.fromTheme('document-open'))
        toolBtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        toolBtn.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)

        # Create menu.
        menu = QMenu(self)

        # Add menu list.
        openAction = QAction('Open', self)
        openAction.triggered.connect(lambda: self.showMessage('Open'))
        menu.addAction(openAction)

        saveAction = QAction('Save', self)
        saveAction.triggered.connect(lambda: self.showMessage('Save'))
        menu.addAction(saveAction)

        # Set button menu.
        toolBtn.setMenu(menu)

        # Add click callback (When press 'menu' button).
        toolBtn.clicked.connect(lambda: self.showMessage('Button pressed'))

        mainLayout.addWidget(toolBtn)

        self.setLayout(mainLayout)
    # }

    def showMessage(self, text):
    # {
        QMessageBox.information(self, 'Tips', f'You click: {text}')
    # }
# }

###
# PyQt6 font combo box window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QFontComboBox
)
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'FontComboBox'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create layout.
        mainWidget = QWidget()
        mainLayout = QVBoxLayout()

        # Create font combo box.
        self.fontCombo = QFontComboBox()

        # Triggered when font changes.
        self.fontCombo.currentFontChanged.connect(self.updateFont)

        # Create label.
        self.labelDemo = QLabel("Hello World!")
        self.labelDemo.setFont(QFont("Arial", 16))  # Initial font.

        # Add layout.
        mainLayout.addWidget(self.fontCombo)
        mainLayout.addWidget(self.labelDemo)

        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
    # }

    """Update label font"""
    def updateFont(self):
    # {
        selectedFont = self.fontCombo.currentFont()
        selectedFont.setPointSize(16)  # Keep fixed size.
        self.labelDemo.setFont(selectedFont)

        print(f"Current font: {selectedFont.family()}")
    # }
# }

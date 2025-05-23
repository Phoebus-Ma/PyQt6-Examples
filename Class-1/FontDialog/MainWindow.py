###
# PyQt6 font dialog main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFontDialog
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'FontDialog'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        layout = QVBoxLayout()

        # Create label for display font.
        self.fontLabel = QLabel("Selected Font: None", self)
        self.fontLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create button for font dialog.
        self.fontButton = QPushButton("Choose Font", self)
        self.fontButton.clicked.connect(self.showFontDialog)

        layout.addWidget(self.fontLabel)
        layout.addWidget(self.fontButton)

        self.setLayout(layout)
    # }

    def showFontDialog(self):
    # {
        # Create a font dialog.
        fontDialog = QFontDialog(self)

        if fontDialog.exec() == QFontDialog.DialogCode.Accepted:
            # Get user selected font.
            font = fontDialog.selectedFont()

            # Updates the label to display information for the font.
            self.fontLabel.setText(f"Selected Font: {font.family()}, Size: {font.pointSize()}")

            # Set label font to user-selected font.
            self.fontLabel.setFont(font)
    # }
# }

###
# PyQt6 color dialog main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QColorDialog
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ColorDialog'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainlayout = QVBoxLayout()

        # Create label for display color.
        self.colorLabel = QLabel("Selected Color: None", self)
        self.colorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create button for open color dialog.
        self.colorButton = QPushButton("Choose Color", self)
        self.colorButton.clicked.connect(self.showColorDialog)

        mainlayout.addWidget(self.colorLabel)
        mainlayout.addWidget(self.colorButton)

        self.setLayout(mainlayout)
    # }

    def showColorDialog(self):
    # {
        # Create a color dialog.
        colorDialog = QColorDialog(self)

        if colorDialog.exec() == QColorDialog.DialogCode.Accepted:
            # Get user selected color.
            color = colorDialog.selectedColor()

            # Updates the label to display information for the color.
            self.colorLabel.setText(f"Selected Color: {color.name()}")

            # Set the background color for label.
            self.colorLabel.setStyleSheet(f"background-color: {color.name()};")
    # }
# }

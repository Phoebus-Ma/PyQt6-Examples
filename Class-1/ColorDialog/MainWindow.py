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

        mainLayout = QVBoxLayout()

        # Create label for display color.
        self.labelColor = QLabel("Selected Color: None", self)
        self.labelColor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create button for open color dialog.
        self.btnColor = QPushButton("Choose Color", self)
        self.btnColor.clicked.connect(self.showColorDialog)

        mainLayout.addWidget(self.labelColor)
        mainLayout.addWidget(self.btnColor)

        self.setLayout(mainLayout)
    # }

    def showColorDialog(self):
    # {
        # Create a color dialog.
        colorDialog = QColorDialog(self)

        if colorDialog.exec() == QColorDialog.DialogCode.Accepted:
            # Get user selected color.
            color = colorDialog.selectedColor()

            # Updates the label to display information for the color.
            self.labelColor.setText(f"Selected Color: {color.name()}")

            # Set the background color for label.
            self.labelColor.setStyleSheet(f"background-color: {color.name()};")
    # }
# }

###
# PyQt6 horizontal scroll area main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFrame,
    QScrollArea
)

class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'HorizontalScrollArea'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create scroll area container.
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # Create wide domain content.
        contentWidget = QFrame()
        contentLayout = QHBoxLayout(contentWidget)

        # Increase left and right margins.
        contentLayout.setContentsMargins(50, 0, 50, 0)

        # Add extension content.
        contentLayout.addWidget(self.createColoredBlock("red", 400))
        contentLayout.addWidget(self.createColoredBlock("green", 400))
        contentLayout.addWidget(self.createColoredBlock("blue", 400))

        scrollArea.setWidget(contentWidget)

        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(scrollArea)

        self.setLayout(mainLayout)
    # }

    def createColoredBlock(self, color, width):
    # {
        block = QWidget()
        block.setStyleSheet(f"background-color: {color};")
        block.setFixedSize(width, 80)   # Set extra width dimension.
        return block
    # }
# }

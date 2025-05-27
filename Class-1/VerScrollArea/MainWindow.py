###
# PyQt6 VerticalScrollArea main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea
)

class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'VerticalScrollArea'
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

        # Allow content adaptation.
        scrollArea.setWidgetResizable(True)

        # Auto display vertical scroll bar.
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # Create content control.
        contentWidget = QWidget()
        contentLayout = QVBoxLayout()

        # Add a lot of content.
        for i in range(50):
            contentLayout.addWidget(QLabel(f"Item {i + 1}", self))

        # Place content in scroll area.
        contentWidget.setLayout(contentLayout)
        scrollArea.setWidget(contentWidget)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(scrollArea)
        self.setLayout(mainLayout)
    # }
# }

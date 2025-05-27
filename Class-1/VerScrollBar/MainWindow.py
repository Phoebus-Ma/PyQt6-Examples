###
# PyQt6 vertical scroll bar main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollBar
)

class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'VerticalScrollBar'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QVBoxLayout()

        # Create value label.
        self.labelValue = QLabel("Value: 0", self)
        mainLayout.addWidget(self.labelValue)

        # Create vertical scroll bar.
        self.scrollbar = QScrollBar(Qt.Orientation.Vertical)
        self.scrollbar.setRange(0, 100)  # range 0-100.
        self.scrollbar.setValue(50)      # default value.
        self.scrollbar.valueChanged.connect(self.updateValue)

        mainLayout.addWidget(self.scrollbar)
        self.setLayout(mainLayout)
    # }

    def updateValue(self, value):
    # {
        self.labelValue.setText(f"Value: {value}")
    # }
# }

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

        layout = QVBoxLayout(self)

        # Create value label.
        self.valueLabel = QLabel("Value: 0", self)
        layout.addWidget(self.valueLabel)

        # Create vertical scroll bar.
        self.scrollbar = QScrollBar(Qt.Orientation.Vertical)
        self.scrollbar.setRange(0, 100)  # range 0-100.
        self.scrollbar.setValue(50)      # default value.
        self.scrollbar.valueChanged.connect(self.updateValue)

        layout.addWidget(self.scrollbar)
    # }

    def updateValue(self, value):
    # {
        self.valueLabel.setText(f"Value: {value}")
    # }
# }

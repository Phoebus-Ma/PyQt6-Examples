###
# PyQt6 HorizontalSlider main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSlider
)

class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'HorizontalSlider'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainlayout = QVBoxLayout()

        # Create label for show slider value.
        self.label = QLabel("Value: 0", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create horizontal slider.
        self.scrollBar = QSlider(Qt.Orientation.Horizontal, self)
        self.scrollBar.setMinimum(0)
        self.scrollBar.setMaximum(100)
        self.scrollBar.setValue(0)

        # Slider connect slot.
        self.scrollBar.valueChanged.connect(self.updateLabel)

        mainlayout.addWidget(self.label)
        mainlayout.addWidget(self.scrollBar)

        self.setLayout(mainlayout)
    # }

    def updateLabel(self, value):
    # {
        # Update label value.
        self.label.setText(f"Value: {value}")
    # }
# }

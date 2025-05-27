###
# PyQt6 VerticalSlider main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QSlider
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'VerticalSlider'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QHBoxLayout()

        # Create label for show slider value.
        self.labelValue = QLabel("Value: 0", self)
        self.labelValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create vertical slider.
        self.scrollBar = QSlider(Qt.Orientation.Vertical, self)
        self.scrollBar.setMinimum(0)
        self.scrollBar.setMaximum(100)
        self.scrollBar.setValue(0)

        # Slider connect slot.
        self.scrollBar.valueChanged.connect(self.updateLabel)

        mainLayout.addWidget(self.labelValue)
        mainLayout.addWidget(self.scrollBar)

        self.setLayout(mainLayout)
    # }

    def updateLabel(self, value):
    # {
        # Update label value.
        self.labelValue.setText(f"Value: {value}")
    # }
# }

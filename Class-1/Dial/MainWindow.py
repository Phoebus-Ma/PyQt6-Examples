###
# PyQt6 QDial main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QDial
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Dial'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QVBoxLayout()

        # Label.
        self.labelValue = QLabel('Current value: 0', alignment = Qt.AlignmentFlag.AlignCenter)
        self.labelValue.setStyleSheet('font-size: 24px;')

        mainLayout.addWidget(self.labelValue)

        # Time Edit.
        self.dialKnob  = QDial()
        self.dialKnob.setRange(0, 100)
        self.dialKnob.setValue(0)
        self.dialKnob.setNotchesVisible(True)
        self.dialKnob.setWrapping(False)
        self.dialKnob.setPageStep(10)
        self.dialKnob.valueChanged.connect(self.updateLabel)

        mainLayout.addWidget(self.dialKnob)

        self.setLayout(mainLayout)
    # }

    def updateLabel(self, value):
    # {
        self.labelValue.setText(f"Current value: {value}")
        
        if value < 33:
            self.labelValue.setStyleSheet("color: blue; font-size: 24px;")
        elif value < 66:
            self.labelValue.setStyleSheet("color: green; font-size: 24px;")
        else:
            self.labelValue.setStyleSheet("color: red; font-size: 24px;")
    # }
# }

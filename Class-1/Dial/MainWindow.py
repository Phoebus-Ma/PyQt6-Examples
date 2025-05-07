###
# PyQt6 QDial main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, \
    QVBoxLayout, QLabel, QDial


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Dial'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setBaseSize(self.winWidth, self.winHeight)

        self.dial  = QDial()
        self.label = QLabel('Current value: 0', alignment = Qt.AlignmentFlag.AlignCenter)

        layout = self.createLayout()

        self.setLayout(layout)
    # }

    def createLayout(self) -> QVBoxLayout:
    # {
        vLayout = QVBoxLayout()

        # Label.
        self.label.setStyleSheet('font-size: 24px;')

        vLayout.addWidget(self.label)

        # Time Edit.
        self.dial.setRange(0, 100)
        self.dial.setValue(0)
        self.dial.setNotchesVisible(True)
        self.dial.setWrapping(False)
        self.dial.setPageStep(10)
        self.dial.valueChanged.connect(self.updateLabel)

        vLayout.addWidget(self.dial)

        return vLayout
    # }

    def updateLabel(self, value):
    # {
        self.label.setText(f"Current value: {value}")
        
        if value < 33:
            self.label.setStyleSheet("color: blue; font-size: 24px;")
        elif value < 66:
            self.label.setStyleSheet("color: green; font-size: 24px;")
        else:
            self.label.setStyleSheet("color: red; font-size: 24px;")
    # }
# }

###
# PyQt6 QLCDNumber main window.
#
# License - MIT.
###

from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLCDNumber
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'DigitalLCD'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create layout.
        mainLayout = QVBoxLayout()

        # Create QLCDNumber.
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)                                # Set display bits.
        self.lcd.setMode(QLCDNumber.Mode.Dec)                    # Set to decimal.
        self.lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Filled) # Set segment style.

        mainLayout.addWidget(self.lcd)
        self.setLayout(mainLayout)

        # Create a timer, Time updated every second.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # 1000 ms.
    # }

    def updateTime(self):
    # {
        # Get current local time.
        currentTime = QTime.currentTime()

        # Format time to HH:MM:SS.
        timeText = currentTime.toString('hh:mm:ss')

        # Update LCD content.
        self.lcd.display(timeText)
    # }
# }

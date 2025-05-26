###
# PyQt6 analog clock window.
#
# License - MIT.
###

import math
from PyQt6.QtCore import (
    Qt,
    QTime,
    QTimer,
    
)
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QFont
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'AnalogClock'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create timer.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
    # }

    def paintEvent(self, event):
    # {
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        diameter = min(self.width(), self.height())
        radius = diameter // 2 - 20

        painter.translate(self.width() / 2, self.height() / 2)

        self.drawFace(painter, radius)
        self.drawMarks(painter, radius)
        self.drawHourNumbers(painter, radius)
        self.drawHands(painter, radius)
    # }

    def drawFace(self, painter, radius):
    # {
        painter.save()
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(245, 245, 245))
        painter.drawEllipse(-radius, -radius, 2 * radius, 2 * radius)
        painter.restore()
    # }

    def drawMarks(self, painter, radius):
    # {
        # Hour scale (coarse).
        painter.save()
        painter.setPen(QPen(Qt.GlobalColor.black, 3))

        for i in range(12):
            angle = math.radians(30 * i - 90)
            x = radius * 0.85 * math.cos(angle)
            y = radius * 0.85 * math.sin(angle)

            painter.drawLine(
                int(x * 0.85),
                int(y * 0.85),
                int(x * 0.95),
                int(y * 0.95)
            )

        painter.restore()

        # Minute scale (fine).
        painter.save()
        painter.setPen(QPen(Qt.GlobalColor.gray, 1))

        for j in range(60):
            if j % 5 == 0:
                continue

            angle = math.radians(6 * j - 90)
            x = radius * 0.88 * math.cos(angle)
            y = radius * 0.88 * math.sin(angle)

            painter.drawLine(
                int(x * 0.92),
                int(y * 0.92),
                int(x * 0.97),
                int(y * 0.97)
            )

        painter.restore()
    # }

    def drawHourNumbers(self, painter, radius):
    # {
        painter.save()
        painter.setPen(Qt.GlobalColor.black)
        font = QFont("Arial", 12, QFont.Weight.Bold)
        painter.setFont(font)

        # Digital position adjustment parameters.
        textRadius = radius * 0.90  # Distance of digit from center.
        textSize   = 20             # Text area size.

        for i in range(1, 13):
            angle = math.radians(30 * i - 90)

            # Calculate digit position.
            x = textRadius * math.cos(angle) - textSize / 2
            y = textRadius * math.sin(angle) - textSize / 2

            painter.drawText(
                int(x),
                int(y),
                textSize,
                textSize,
                Qt.AlignmentFlag.AlignCenter,
                str(i)
            )

        painter.restore()
    # }

    def drawHands(self, painter, radius):
    # {
        time = QTime.currentTime()

        # Hour hand.
        hourAngle = math.radians(30 * (time.hour() % 12) + time.minute() * 0.5 - 90)
        self.drawHand(painter, hourAngle, radius * 0.5, 8, Qt.GlobalColor.darkGray)

        # Minute hand.
        minuteAngle = math.radians(6 * time.minute() + time.second() * 0.1 - 90)
        self.drawHand(painter, minuteAngle, radius * 0.7, 5, Qt.GlobalColor.darkBlue)

        # Second hand.
        secondAngle = math.radians(6 * time.second() - 90)
        self.drawHand(painter, secondAngle, radius * 0.85, 2, Qt.GlobalColor.red)
    # }

    def drawHand(self, painter, angle, length, width, color):
    # {
        painter.save()
        painter.setPen(QPen(color, width))
        painter.setBrush(color)

        endX = length * math.cos(angle)
        endY = length * math.sin(angle)
        painter.drawLine(0, 0, int(endX), int(endY))

        # Draw pointer end dot.
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(int(endX) - 3, int(endY) - 3, 6, 6)
        painter.restore()
    # }
# }

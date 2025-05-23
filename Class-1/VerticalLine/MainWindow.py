###
# PyQt6 VerticalLine main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QFrame
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'VerticalLine'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        layout = QHBoxLayout()

        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')

        hLine = QFrame()
        hLine.setFrameShape(QFrame.Shape.VLine)

        layout.addWidget(btn1)
        layout.addWidget(hLine)
        layout.addWidget(btn2)

        self.setLayout(layout)
    # }
# }

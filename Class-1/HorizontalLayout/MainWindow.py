###
# PyQt6 QHBoxLayout main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel
)


'''
QHBoxLayout
API: <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHBoxLayout.html>
'''
class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        # Proprities.
        self.title = 'Horizontal Layout'
        self.winWidth  = 320
        self.winHeight = 240

        # Initilaze.
        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        colors = [
            'background-color: red',
            'background-color: green',
            'background-color: blue'
        ]

        self.hboxLayout = QHBoxLayout(self)

        for i, color in enumerate(colors, start = 1):
            label = QLabel()
            label.setText("Label " + str(i))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet(color)
            label.setFixedSize(100, 30)

            self.hboxLayout.addWidget(label)
    # }
# }

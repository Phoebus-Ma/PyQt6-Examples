###
# PyQt6 QVBoxLayout main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)


'''
QVBoxLayout API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QVBoxLayout.html>
'''
class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        # Proprities.
        self.title = 'Vertical Layout'
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

        self.mainLayout = QVBoxLayout()

        for i, color in enumerate(colors, start = 1):
            label = QLabel()
            label.setText("Label " + str(i))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet(color)
            label.setFixedSize(100, 30)

            self.mainLayout.addWidget(label)
            self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.setLayout(self.mainLayout)
    # }
# }

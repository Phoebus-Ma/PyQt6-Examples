###
# PyQt6 QVBoxLayout main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


# QVBoxLayout API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QVBoxLayout.html>
class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        # Proprities.
        self.title = 'Vertical Layout'

        # Initilaze.
        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.createLayout()
    # }

    def createLayout(self):
    # {
        colors = [
            'background-color: red',
            'background-color: green',
            'background-color: blue'
        ]

        self.vboxLayout = QVBoxLayout(self)

        for i, color in enumerate(colors, start = 1):
            label = QLabel()
            label.setText("Label " + str(i))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet(color)
            label.setFixedSize(100, 30)

            self.vboxLayout.addWidget(label)
            self.vboxLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    # }
# }

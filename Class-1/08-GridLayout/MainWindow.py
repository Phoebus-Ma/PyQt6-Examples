###
# PyQt6 QGridLayout main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title = 'Grid Layout'

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setBaseSize(300, 200)

        mainlayout = QVBoxLayout()

        # Add Widget.
        lineEdit = QLineEdit()
        lineEdit.setReadOnly(True)
        mainlayout.addWidget(lineEdit)

        # Add Layout.
        layout = self.createLayout()
        mainlayout.addLayout(layout)

        self.setLayout(mainlayout)
    # }

    def createLayout(self) -> QGridLayout:
    # {
        # index:
        # AC - (0, 0)
        # 9  - (1, 2)
        # 0  - (4, 1)
        keys = [
            'AC', '<-', '/',
            '7',  '8',  '9',
            '4',  '5',  '6',
            '1',  '2',  '3',
            '%',  '0',  '.'
        ]

        keysLayout  = QGridLayout()
        leftLayout  = QGridLayout()
        rightLayout = QVBoxLayout()

        # Left layout.
        # Snapshot example: QGridLayout.addWidget(QPushButton('6'), 2, 2) .
        for i, key in enumerate(keys, start = 0):
            leftLayout.addWidget(QPushButton(key), (int)((i - (i % 3)) / 3), i % 3)

        # Right layout.
        rightLayout.addWidget(QPushButton('*'))
        rightLayout.addWidget(QPushButton('-'))
        rightLayout.addWidget(QPushButton('+'))
        rightLayout.addWidget(QPushButton('\n=\n'))

        # # Main layout.
        keysLayout.addLayout(leftLayout,  0, 0)
        keysLayout.addLayout(rightLayout, 0, 4)

        return keysLayout
    # }
# }

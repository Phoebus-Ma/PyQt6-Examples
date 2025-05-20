###
# PyQt6 ComboBox main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QComboBox,
    QVBoxLayout,
    QLabel
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ComboBox'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create main layout.
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # Create QComboBox.
        self.combo = QComboBox()

        # Add options (2 ways).
        self.combo.addItems(['Apple', 'Banana', 'Orange', 'Pear'])
        self.combo.addItem('Grape')

        # Create label.
        self.label = QLabel('Select: ')

        # Add widget.
        layout.addWidget(self.combo)
        layout.addWidget(self.label)

        # Select slot.
        self.combo.currentTextChanged.connect(self.updateLabel)
    # }

    def updateLabel(self, text):
    # {
        self.label.setText(f'Select: {text}')
    # }
# }

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
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create main layout.
        centralWidget = QWidget()
        mainLayout = QVBoxLayout()

        # Create QComboBox.
        self.comboFruits = QComboBox()

        # Add options (2 ways).
        self.comboFruits.addItems(['Apple', 'Banana', 'Orange', 'Pear'])
        self.comboFruits.addItem('Grape')

        # Create label.
        self.labelSelect = QLabel('Select: ')

        # Add widget.
        mainLayout.addWidget(self.comboFruits)
        mainLayout.addWidget(self.labelSelect)

        # Select slot.
        self.comboFruits.currentTextChanged.connect(self.updateLabel)

        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)
    # }

    def updateLabel(self, text):
    # {
        self.labelSelect.setText(f'Select: {text}')
    # }
# }

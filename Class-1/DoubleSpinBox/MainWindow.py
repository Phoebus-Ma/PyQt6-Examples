###
# PyQt6 double spin box window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QDoubleSpinBox,
    QLabel,
    QPushButton
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'DoubleSpinBox'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create layout.
        mainWidget = QWidget()
        mainLayout = QVBoxLayout()

        # Create QDoubleSpinBox.
        self.spinbox = QDoubleSpinBox()
        self.spinbox.setRange(0.0, 100.0)     # Set range.
        self.spinbox.setSingleStep(0.5)       # Step.
        self.spinbox.setDecimals(2)           # Decimal places.
        self.spinbox.setPrefix("$ ")          # Prefix.
        self.spinbox.setSuffix(" dollar(s)")  # Suffix.
        self.spinbox.valueChanged.connect(self.onValueChanged)  # Connect signal.

        # Create label.
        self.labelValue = QLabel("Current: $ 0.00 dollar")
        
        # Create button.
        btnGet = QPushButton("Get value")
        btnGet.clicked.connect(self.getValue)

        mainLayout.addWidget(self.spinbox)
        mainLayout.addWidget(self.labelValue)
        mainLayout.addWidget(btnGet)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
    # }

    """Update label when value changes"""
    def onValueChanged(self, value):
    # {
        self.labelValue.setText(f"Current value: $ {value:.2f} dollar(s)")
        print(f"Value changed: {value:.2f}")
    # }

    """Click the button to obtain the current value"""
    def getValue(self):
    # {
        currentValue = self.spinbox.value()
        print(f"Value obtained: {currentValue:.2f}")
        self.statusBar().showMessage(f"Current value: {currentValue:.2f}")
    # }
# }

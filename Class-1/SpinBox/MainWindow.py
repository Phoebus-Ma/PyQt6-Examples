###
# PyQt6 SpinBox main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QMainWindow,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QLabel
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'SpinBox'
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
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # Create QSpinBox.
        self.spinbox = QSpinBox()

        # Configure SpinBox.
        self.spinbox.setRange(0, 100)           # Set value range.
        self.spinbox.setValue(50)               # Set default value.
        self.spinbox.setSingleStep(5)           # Set step.
        self.spinbox.setPrefix("Temperature: ") # Set prefix.
        self.spinbox.setSuffix(" °C")           # Set suffix.

        # Create label.
        self.label = QLabel("Value: 50 °C")
        
        # Add widget to layout.s
        layout.addWidget(self.spinbox)
        layout.addWidget(self.label)

        # Connect signal (Triggered when the page is switched).
        self.spinbox.valueChanged.connect(self.updateLabel)
    # }

    def updateLabel(self, value):
    # {
        self.label.setText(f"Value: {value} °C")
    # }
# }

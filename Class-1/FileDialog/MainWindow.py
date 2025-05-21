###
# PyQt6 QDial main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Dial'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create layout and control.
        layout = QVBoxLayout()

        self.btn = QPushButton('Select', self)
        self.btn.clicked.connect(self.showFileDialog)

        self.label = QLabel('Path: ', self)

        layout.addWidget(self.btn)
        layout.addWidget(self.label)
        self.setLayout(layout)
    # }

    def showFileDialog(self):
    # {
        # Display file dialog.
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select",           # Title.
            "",                 # Base directory (default directory).
            "All Files (*);;Text Files (*.txt)",            # File filter.
            options=QFileDialog.Option.DontUseNativeDialog  # Optional.
        )

        if filename:
            self.label.setText(f"File: {filename}")
    # }
# }

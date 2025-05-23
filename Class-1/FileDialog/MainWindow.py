###
# PyQt6 FileDialog main window.
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

        self.title     = 'FileDialog'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create layout and control.
        mainlayout = QVBoxLayout()

        self.btn = QPushButton('Select', self)
        self.btn.clicked.connect(self.showFileDialog)

        self.label = QLabel('Path: ', self)

        mainlayout.addWidget(self.btn)
        mainlayout.addWidget(self.label)
        self.setLayout(mainlayout)
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

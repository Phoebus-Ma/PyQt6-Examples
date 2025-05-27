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
        mainLayout = QVBoxLayout()

        self.btnSelect = QPushButton('Select', self)
        self.btnSelect.clicked.connect(self.showFileDialog)

        self.labelPath = QLabel('Path: ', self)

        mainLayout.addWidget(self.btnSelect)
        mainLayout.addWidget(self.labelPath)
        self.setLayout(mainLayout)
    # }

    def showFileDialog(self):
    # {
        # Display file dialog.
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select",           # Title.
            "",                 # Base directory (default directory).
            "All Files (*);;Text Files (*.txt)",            # File filter.
            options = QFileDialog.Option.DontUseNativeDialog  # Optional.
        )

        if filename:
            self.labelPath.setText(f"File: {filename}")
    # }
# }

###
# PyQt6 dialog button box window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QDialog,
    QDialogButtonBox
)


class MainWindow(QDialog):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'DialogButtonBox'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create layout.
        mainLayout = QVBoxLayout(self)

        # Create label.
        label = QLabel("This is an example dialog box", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(label)

        # Create DialogButtonBox.
        buttonBox = QDialogButtonBox()

        # Add standard button.
        buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Ok     |
            QDialogButtonBox.StandardButton.Cancel |
            QDialogButtonBox.StandardButton.Save
        )

        # Connect signal.
        buttonBox.accepted.connect(self.onAccept)
        buttonBox.rejected.connect(self.onReject)
        buttonBox.button(
            QDialogButtonBox.StandardButton.Save).clicked.connect(self.onSave)

        mainLayout.addWidget(buttonBox)
    # }

    def onAccept(self):
    # {
        print("Confirm button clicked")
        self.accept()
    # }

    def onReject(self):
    # {
        print("Cancel button clicked")
        self.reject()
    # }

    def onSave(self):
    # {
        print("Save button clicked")
    # }
# }

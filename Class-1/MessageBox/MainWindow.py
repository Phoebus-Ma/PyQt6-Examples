###
# PyQt6 MessageBox window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'MessageBox'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create Layout.
        widget = QWidget()
        layout = QVBoxLayout()

        buttons = [
            ("Hi-Information", self.showInfo),
            ("Hi-Warning"    , self.showWarning),
            ("Hi-Critical"   , self.showCritical),
            ("Hi-Question"   , self.showQuestion),
            ("Hi-Custom"     , self.showCustom)
        ]

        for text, slot in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(slot)
            layout.addWidget(btn)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
    # }

    def showInfo(self):
    # {
        QMessageBox.information(
            self,
            "Information",
            "This is a information tip."
        )
    # }

    def showWarning(self):
    # {
        reply = QMessageBox.warning(
            self,
            "Warning",
            "Out of disk space !",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )

        if reply == QMessageBox.StandardButton.Ok:
            print("User confirmation warning.")
    # }

    def showCritical(self):
    # {
        QMessageBox.critical(
            self,
            "Critical",
            "A serious error has occurred !",
            buttons=QMessageBox.StandardButton.Ok,
            defaultButton=QMessageBox.StandardButton.Ok
        )
    # }

    def showQuestion(self):
    # {
        reply = QMessageBox.question(
            self,
            "Confirm",
            "Are you sure delete this file ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            print("User select Yes.")
        else:
            print("User select No.")
    # }

    def showCustom(self):
    # {
        msg = QMessageBox()
        msg.setWindowTitle("Custom MessageBox")
        msg.setText("Main tip")
        msg.setInformativeText("Additional information (optional)")
        msg.setDetailedText("This is contents...\nMultiple lines display.")
        msg.setIcon(QMessageBox.Icon.Warning)
        
        # Add custom button.
        btnHelp = msg.addButton("Help", QMessageBox.ButtonRole.HelpRole)
        msg.addButton(QMessageBox.StandardButton.Close)
        
        msg.exec()
        
        if msg.clickedButton() == btnHelp:
            QMessageBox.information(self, "Help", "This is help information.")
    # }
# }

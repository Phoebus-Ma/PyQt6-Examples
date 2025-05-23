###
# PyQt6 QPlainTextEdit main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPlainTextEdit,
    QPushButton
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title = 'QPlainTextEdit'
        self.file  = 'hello.txt'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QVBoxLayout()

        # Text edit.
        self.plainTextEdit = QPlainTextEdit()
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

        mainLayout.addWidget(self.plainTextEdit)

        # Open
        btnOpen = QPushButton()
        btnOpen.setText('Open')
        btnOpen.clicked.connect(self.btnOpenClicked)

        mainLayout.addWidget(btnOpen)

        # Save.
        btnSave = QPushButton()
        btnSave.setText('Save')
        btnSave.clicked.connect(self.btnSaveClicked)

        mainLayout.addWidget(btnSave)

        self.setLayout(mainLayout)
    # }

    def btnOpenClicked(self):
    # {
        with open(self.file, 'r') as file:
            self.plainTextEdit.setPlainText(file.read())
    # }

    def btnSaveClicked(self):
    # {
        with open(self.file, 'w') as file:
            file.write(self.plainTextEdit.toPlainText())
    # }
# }

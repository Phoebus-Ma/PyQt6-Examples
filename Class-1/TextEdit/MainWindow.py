###
# PyQt6 QTextEdit main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QPushButton
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title = 'QTextEdit'
        self.file  = 'hello.txt'    # Current path text file.
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
        self.textEdit = QTextEdit()
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        mainLayout.addWidget(self.textEdit)

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
            self.textEdit.setPlainText(file.read())
    # }

    def btnSaveClicked(self):
    # {
        with open(self.file, 'w') as file:
            file.write(self.textEdit.toPlainText())
    # }
# }

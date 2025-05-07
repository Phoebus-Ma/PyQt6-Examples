###
# PyQt6 QTextEdit main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QWidget, \
    QVBoxLayout, QTextEdit, QPushButton


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title = 'QTextEdit'
        self.file  = 'hello.txt'    # Current path text file.
        self.winWidth  = 300
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setBaseSize(self.winWidth, self.winHeight)

        self.textEdit = QTextEdit()

        layout = self.createLayout()

        self.setLayout(layout)
    # }

    def createLayout(self) -> QVBoxLayout:
    # {
        vlayout = QVBoxLayout()

        # Text edit.
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        vlayout.addWidget(self.textEdit)

        # Open
        btnOpen = QPushButton()
        btnOpen.setText('Open')
        btnOpen.clicked.connect(self.btnOpenClicked)

        vlayout.addWidget(btnOpen)

        # Save.
        btnSave = QPushButton()
        btnSave.setText('Save')
        btnSave.clicked.connect(self.btnSaveClicked)

        vlayout.addWidget(btnSave)

        return vlayout
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

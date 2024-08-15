###
# PyQt6 QFormLayout main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QWidget,       \
    QFormLayout, QHBoxLayout, QVBoxLayout, \
    QLabel, QLineEdit, QRadioButton, QPushButton


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Form Layout'
        self.winWidth  = 300
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setBaseSize(self.winWidth, self.winHeight)

        layout = self.createLayout()

        self.setLayout(layout)
    # }

    def createLayout(self) -> QFormLayout:
    # {
        infoLayout = QFormLayout()

        # Control 1.
        infoLayout.addRow(QLabel('Name'), QLineEdit())

        # Control 2.
        sexLayout = QHBoxLayout()

        sexLayout.addWidget(QRadioButton('Male'))
        sexLayout.addWidget(QRadioButton('Female'))
        infoLayout.addRow('Sex', sexLayout)

        # Control 3.
        addrLayout = QVBoxLayout()

        addrLayout.addWidget(QLineEdit())
        addrLayout.addWidget(QLineEdit())
        infoLayout.addRow('Address', addrLayout)

        # Control 4.
        infoLayout.addRow(QPushButton('Yes'), QPushButton('No'))

        return infoLayout
    # }
# }

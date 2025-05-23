###
# PyQt6 QFormLayout main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QFormLayout,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QRadioButton,
    QPushButton
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Form Layout'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QFormLayout()

        # Control 1.
        mainLayout.addRow(QLabel('Name'), QLineEdit())

        # Control 2.
        sexLayout = QHBoxLayout()

        sexLayout.addWidget(QRadioButton('Male'))
        sexLayout.addWidget(QRadioButton('Female'))
        mainLayout.addRow('Sex', sexLayout)

        # Control 3.
        addrLayout = QVBoxLayout()

        addrLayout.addWidget(QLineEdit())
        addrLayout.addWidget(QLineEdit())
        mainLayout.addRow('Address', addrLayout)

        # Control 4.
        mainLayout.addRow(QPushButton('Yes'), QPushButton('No'))

        self.setLayout(mainLayout)
    # }
# }

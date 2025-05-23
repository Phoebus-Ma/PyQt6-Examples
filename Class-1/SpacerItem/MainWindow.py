###
# PyQt6 QSpacerItem main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QSpacerItem,
    QSizePolicy
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'SpacerItem'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        hLayout = self.createHLayout()
        vLayout = self.createVLayout()

        mainlayout = QVBoxLayout()
        mainlayout.addLayout(hLayout)
        mainlayout.addLayout(vLayout)

        self.setLayout(mainlayout)
    # }

    def createHLayout(self) -> QHBoxLayout:
    # {
        hLayout = QHBoxLayout()

        hLayout.addWidget(QPushButton('OK'))
        hLayout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.Expanding))
        hLayout.addWidget(QPushButton('Cancel'))

        return hLayout
    # }

    def createVLayout(self) -> QVBoxLayout:
    # {
        vLayout = QVBoxLayout()

        vLayout.addWidget(QPushButton('OK'))
        vLayout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.Expanding))
        vLayout.addWidget(QPushButton('Cancel'))

        return vLayout
    # }
# }

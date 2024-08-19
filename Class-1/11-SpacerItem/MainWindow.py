###
# PyQt6 QSpacerItem main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QWidget,    \
    QHBoxLayout, QVBoxLayout,           \
    QPushButton, QSpacerItem, QSizePolicy


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'SpacerItem'
        self.winWidth  = 300
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setBaseSize(self.winWidth, self.winHeight)

        hLayout = self.createHLayout()
        vLayout = self.createVLayout()

        layout = QVBoxLayout()
        layout.addLayout(hLayout)
        layout.addLayout(vLayout)

        self.setLayout(layout)
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

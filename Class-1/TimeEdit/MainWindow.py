###
# PyQt6 QTimeEdit main window.
#
# License - MIT.
###

from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QTimeEdit,
    QPushButton,
    QMessageBox
)

class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'QTimeEdit'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QHBoxLayout()

        # Time Edit.
        self.timeEdit = QTimeEdit()
        self.timeEdit.setMinimumTime(QTime(0, 0, 0))
        self.timeEdit.setMaximumTime(QTime(23, 59, 59))
        self.timeEdit.setTime(QTime(2, 11, 1))
        self.timeEdit.setDisplayFormat('HH:mm')
        self.timeEdit.setMinimumWidth(150)

        mainLayout.addWidget(self.timeEdit)

        # Get.
        btnGet = QPushButton()
        btnGet.setText('Print')
        btnGet.clicked.connect(self.btnGetClicked)

        mainLayout.addWidget(btnGet)

        self.setLayout(mainLayout)
    # }

    '''Slot'''
    def btnGetClicked(self):
    # {
        QMessageBox.information(
            self,
            'QTimeEdit',
            str(self.timeEdit.time().toPyTime()))
    # }
# }

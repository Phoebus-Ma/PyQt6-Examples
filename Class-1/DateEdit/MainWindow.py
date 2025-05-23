###
# PyQt6 QDateEdit main window.
#
# License - MIT.
###

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QMessageBox,
    QDateEdit,
    QPushButton
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'DateEdit'
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
        self.dateEdit = QDateEdit()
        self.dateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setDisplayFormat('yyyy/MM/dd')
        self.dateEdit.setMinimumWidth(150)

        mainLayout.addWidget(self.dateEdit)

        # Get.
        btnGet = QPushButton()
        btnGet.setText('Print')
        btnGet.clicked.connect(self.btnGetClicked)

        mainLayout.addWidget(btnGet)

        self.setLayout(mainLayout)
    # }

    def btnGetClicked(self):
    # {
        QMessageBox.information(
            self,
            'QTimeEdit',
            str(self.dateEdit.date().toPyDate()))
    # }
# }

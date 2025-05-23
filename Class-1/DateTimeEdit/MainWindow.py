###
# PyQt6 QDateTimeEdit main window.
#
# License - MIT.
###

from PyQt6.QtCore import (
    QDate,
    QTime,
    QDateTime
)

from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QMessageBox,
    QDateTimeEdit
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'DateTimeEdit'
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
        self.dateTimeEdit = QDateTimeEdit()
        self.dateTimeEdit.setMinimumDate(QDate(2000, 1, 1))
        self.dateTimeEdit.setMinimumTime(QTime(0, 0, 0))
        self.dateTimeEdit.setMaximumTime(QTime(23, 59, 59))

        self.dateTimeEdit.setDateTime(QDateTime(2025, 1, 12, 2, 11, 1))
        self.dateTimeEdit.setDisplayFormat('yyyy/MM/dd - hh:mm')
        self.dateTimeEdit.setMinimumWidth(200)

        mainLayout.addWidget(self.dateTimeEdit)

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
            str(self.dateTimeEdit.dateTime().toPyDateTime()))
    # }
# }

###
# PyQt6 QLineEdit main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QMessageBox
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'QLineEdit'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    #{
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QFormLayout()

        # Normal.
        self.lineNormal = QLineEdit()
        self.lineNormal.setEchoMode(QLineEdit.EchoMode.Normal)

        btnName = QPushButton()
        btnName.setText('Name')
        btnName.clicked.connect(lambda: self.btnShowContent('Name'))

        mainLayout.addRow(self.lineNormal, btnName)

        # Right.
        self.lineRight = QLineEdit()
        self.lineRight.setAlignment(Qt.AlignmentFlag.AlignRight)

        btnRight = QPushButton()
        btnRight.setText('Right')
        btnRight.clicked.connect(lambda: self.btnShowContent('Right'))

        mainLayout.addRow(self.lineRight, btnRight)

        # No echo.
        self.lineNoEcho = QLineEdit()
        self.lineNoEcho.setEchoMode(QLineEdit.EchoMode.NoEcho)

        btnNoEcho = QPushButton()
        btnNoEcho.setText('NoEcho')
        btnNoEcho.clicked.connect(lambda: self.btnShowContent('NoEcho'))
        
        mainLayout.addRow(self.lineNoEcho, btnNoEcho)

        # Password.
        self.linePwd = QLineEdit()
        self.linePwd.setEchoMode(QLineEdit.EchoMode.Password)

        btnPwd = QPushButton()
        btnPwd.setText('Password')
        btnPwd.clicked.connect(lambda: self.btnShowContent('Password'))
        
        mainLayout.addRow(self.linePwd, btnPwd)

        # Password echo on edit.
        self.linePwdEcho = QLineEdit()
        self.linePwdEcho.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        btnPwdEcho = QPushButton()
        btnPwdEcho.setText('PwdEcho')
        btnPwdEcho.clicked.connect(lambda: self.btnShowContent('PwdEcho'))
        
        mainLayout.addRow(self.linePwdEcho, btnPwdEcho)

        self.setLayout(mainLayout)
    # }

    '''Common slot'''
    def btnShowContent(self, btnType: str):
    # {
        match btnType:
            case 'Name':
                QMessageBox.information(self, 'Name', str(self.lineNormal.text()))

            case 'Right':
                QMessageBox.information(self, 'Calculate', str(self.lineRight.text()))

            case 'NoEcho':
                QMessageBox.information(self, 'NoEcho', str(self.lineNoEcho.text()))

            case 'Password':
                QMessageBox.information(self, 'Password', str(self.linePwd.text()))

            case 'PwdEcho':
                QMessageBox.information(self, 'PwdEcho', str(self.linePwdEcho.text()))

            case _:
                pass
    # }
# }

###
# PyQt6 QLineEdit main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QWidget, \
    QFormLayout, QLineEdit, QPushButton, QMessageBox

from PyQt6.QtCore import Qt


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'QLineEdit'
        self.winWidth  = 300
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    #{
        self.setWindowTitle(self.title)
        self.setBaseSize(self.winWidth, self.winHeight)

        self.lineNormal  = QLineEdit()
        self.lineNoEcho  = QLineEdit()
        self.linePwd     = QLineEdit()
        self.linePwdEcho = QLineEdit()
        self.lineRight   = QLineEdit()

        layout = self.createLayout()

        self.setLayout(layout)
    # }

    def createLayout(self) -> QFormLayout:
    # {
        formLayout = QFormLayout()

        # Normal.
        self.lineNormal.setEchoMode(QLineEdit.EchoMode.Normal)

        btnName = QPushButton()
        btnName.setText('Name')
        btnName.clicked.connect(lambda: self.btnShowContent('Name'))

        formLayout.addRow(self.lineNormal, btnName)

        # Right.
        self.lineRight.setAlignment(Qt.AlignmentFlag.AlignRight)

        btnRight = QPushButton()
        btnRight.setText('Right')
        btnRight.clicked.connect(lambda: self.btnShowContent('Right'))

        formLayout.addRow(self.lineRight, btnRight)

        # No echo.
        self.lineNoEcho.setEchoMode(QLineEdit.EchoMode.NoEcho)

        btnNoEcho = QPushButton()
        btnNoEcho.setText('NoEcho')
        btnNoEcho.clicked.connect(lambda: self.btnShowContent('NoEcho'))
        
        formLayout.addRow(self.lineNoEcho, btnNoEcho)

        # Password.
        self.linePwd.setEchoMode(QLineEdit.EchoMode.Password)

        btnPwd = QPushButton()
        btnPwd.setText('Password')
        btnPwd.clicked.connect(lambda: self.btnShowContent('Password'))
        
        formLayout.addRow(self.linePwd, btnPwd)

        # Password echo on edit.
        self.linePwdEcho.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        btnPwdEcho = QPushButton()
        btnPwdEcho.setText('PwdEcho')
        btnPwdEcho.clicked.connect(lambda: self.btnShowContent('PwdEcho'))
        
        formLayout.addRow(self.linePwdEcho, btnPwdEcho)

        return formLayout
    # }

    # Common slot.
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
    # }
# }

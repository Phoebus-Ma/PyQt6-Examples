###
# PyQt6 QStackedLayout main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QWidget,                        \
    QHBoxLayout, QVBoxLayout, QFormLayout, QStackedLayout,  \
    QLabel, QPushButton, QRadioButton, QLineEdit, QComboBox


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Stacked Layout'
        self.winWidth  = 300
        self.winHeight = 500

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setBaseSize(self.winWidth, self.winHeight)

        # ComboBox.
        self.selectCombox = QComboBox()

        self.selectCombox.addItem('Name')
        self.selectCombox.addItem('Contact')
        self.selectCombox.addItem('Address')

        # Pages widget.
        nameWidget    = self.createNamePage()
        contactWidget = self.createContactPage()
        addressWidget = self.createAddressPage()

        self.pageLayout = QStackedLayout()
        self.pageLayout.addWidget(nameWidget)
        self.pageLayout.addWidget(contactWidget)
        self.pageLayout.addWidget(addressWidget)

        # Main layout.
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.selectCombox)
        mainLayout.addLayout(self.pageLayout)

        self.selectCombox.currentIndexChanged.connect(self.switchPage)
        self.setLayout(mainLayout)
    # }

    def createNamePage(self) -> QWidget:
    # {
        nameLayout = QFormLayout()

        # Control 1.
        nameLayout.addRow('Name', QLineEdit())

        # Control 2.
        sexLayout = QHBoxLayout()

        sexLayout.addWidget(QRadioButton('Male'))
        sexLayout.addWidget(QRadioButton('Female'))
        nameLayout.addRow('Sex', sexLayout)

        widget = QWidget()
        widget.setLayout(nameLayout)

        return widget
    # }

    def createContactPage(self) -> QWidget:
    # {
        contactLayout = QHBoxLayout()

        # Control 1.
        contactLayout.addWidget(QLabel('TEL: '))

        # Control 2.
        codeLineEdit = QLineEdit()
        codeLineEdit.setFixedWidth(50)
        contactLayout.addWidget(codeLineEdit)

        # Control 3.
        contactLayout.addWidget(QLabel(' - '))

        # Control 4.
        numberLineEdit = QLineEdit()
        numberLineEdit.setFixedWidth(150)
        contactLayout.addWidget(numberLineEdit)

        widget = QWidget()
        widget.setLayout(contactLayout)

        return widget
    # }

    def createAddressPage(self) -> QWidget:
    # {
        addrLayout = QFormLayout()

        # Control 1.
        textLayout = QVBoxLayout()

        textLayout.addWidget(QLineEdit())
        textLayout.addWidget(QLineEdit())
        addrLayout.addRow('Address: ', textLayout)

        # Control 2.
        addrLayout.addRow(QPushButton('Calcel'), QPushButton('Submit'))

        widget = QWidget()
        widget.setLayout(addrLayout)

        return widget
    # }

    def switchPage(self, i):
    # {
        self.pageLayout.setCurrentIndex(i)
    # }
# }

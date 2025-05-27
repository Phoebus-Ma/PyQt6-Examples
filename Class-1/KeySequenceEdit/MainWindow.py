###
# PyQt6 QKeySequenceEdit main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QKeySequenceEdit
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'keySquenceEdit'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QVBoxLayout()

        # Label.
        self.labelTip = QLabel("Please input ShortKey:")
        mainLayout.addWidget(self.labelTip)

        # Key squence edit.
        self.keySquenceEdit = QKeySequenceEdit()
        self.keySquenceEdit.setClearButtonEnabled(True)

        mainLayout.addWidget(self.keySquenceEdit)

        # Get.
        btnGet = QPushButton()
        btnGet.setText('Get ShortKey')
        btnGet.clicked.connect(self.btnGetClicked)

        mainLayout.addWidget(btnGet)

        self.keySquenceEdit.keySequenceChanged.connect(self.update_label)

        self.setLayout(mainLayout)
    # }

    '''Real-time update label'''
    def update_label(self, key_sequence):
    # {
        self.labelTip.setText(f'Current shortcuts key: {key_sequence.toString()}')
    # }

    '''Display current key squence'''
    def btnGetClicked(self):
    # {
        sequence = self.keySquenceEdit.keySequence()
        print(f'Current shortcuts key: {sequence.toString()}')
        self.labelTip.setText(f'Shortcut keys confirmed: {sequence.toString()}')
    # }
# }

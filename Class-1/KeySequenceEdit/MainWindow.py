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
        self.winWidth  = 640
        self.winHeight = 320

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        self.label = QLabel("Please input ShortKey:")
        self.keySquenceEdit = QKeySequenceEdit()

        layout = self.createLayout()

        self.setLayout(layout)
    # }

    def createLayout(self) -> QVBoxLayout:
    # {
        vLayout = QVBoxLayout()

        # Label.
        vLayout.addWidget(self.label)

        # Key squence edit.
        self.keySquenceEdit.setClearButtonEnabled(True)

        vLayout.addWidget(self.keySquenceEdit)

        # Get.
        btnGet = QPushButton()
        btnGet.setText('Get ShortKey')
        btnGet.clicked.connect(self.btnGetClicked)

        vLayout.addWidget(btnGet)

        self.keySquenceEdit.keySequenceChanged.connect(self.update_label)

        return vLayout
    # }

    '''Real-time update label'''
    def update_label(self, key_sequence):
    # {
        self.label.setText(f'Current shortcuts key: {key_sequence.toString()}')
    # }

    '''Display current key squence'''
    def btnGetClicked(self):
    # {
        sequence = self.keySquenceEdit.keySequence()
        print(f'Current shortcuts key: {sequence.toString()}')
        self.label.setText(f'Shortcut keys confirmed: {sequence.toString()}')
    # }
# }

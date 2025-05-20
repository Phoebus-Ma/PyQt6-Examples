###
# PyQt6 GroupBox main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QGroupBox,
    QRadioButton,
    QCheckBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QMessageBox
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'GroupBox'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setBaseSize(self.winWidth, self.winHeight)

        # Create main layout.
        mainWidget = QWidget()
        mainLayout = QVBoxLayout()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        # Create first GroupBox (radio button group).
        self.createRadioGroupbox()
        mainLayout.addWidget(self.radioGroupbox)

        # Create second GroupBox (check box group).
        self.createCheckboxGroupbox()
        mainLayout.addWidget(self.checkboxGroupbox)

        # Create bottom button.
        self.createBottomControls(mainLayout)
    # }

    '''Create radio button group'''
    def createRadioGroupbox(self):
    # {
        self.radioGroupbox = QGroupBox('Select OS')
        layout = QVBoxLayout()

        # Create radio button.
        self.radioWin   = QRadioButton('Windows')
        self.radioMac   = QRadioButton('macOS')
        self.radioLinux = QRadioButton('Linux')

        # Create default option.
        self.radioWin.setChecked(True)

        # Add button layout.
        layout.addWidget(self.radioWin)
        layout.addWidget(self.radioMac)
        layout.addWidget(self.radioLinux)

        # Add a divider.
        layout.addWidget(QLabel('Select: '))
        self.selectedOsLabel = QLabel('Windows')
        layout.addWidget(self.selectedOsLabel)

        # Connect signal.
        self.radioWin.toggled.connect(lambda: self.updateOsLabel('Windows'))
        self.radioMac.toggled.connect(lambda: self.updateOsLabel('macOS'))
        self.radioLinux.toggled.connect(lambda: self.updateOsLabel('Linux'))

        self.radioGroupbox.setLayout(layout)
    # }

    '''Create check box group'''
    def createCheckboxGroupbox(self):
    # {
        self.checkboxGroupbox = QGroupBox('Select Program Language')
        layout = QHBoxLayout()

        # Create check box.
        self.cbPython = QCheckBox('Python')
        self.cbJava   = QCheckBox('Java')
        self.cbCpp    = QCheckBox('C++')
        self.cbJs     = QCheckBox('JavaScript')

        # Set default option.
        self.cbPython.setChecked(True)

        # Add control to layout.
        layout.addWidget(self.cbPython)
        layout.addWidget(self.cbJava)
        layout.addWidget(self.cbCpp)
        layout.addWidget(self.cbJs)

        self.checkboxGroupbox.setLayout(layout)
    # }

    '''Create bottom button'''
    def createBottomControls(self, mainLayout):
    # {
        btnLayout = QHBoxLayout()

        # Create submit button.
        self.btnSubmit = QPushButton('Submit')
        self.btnSubmit.clicked.connect(self.showSelections)

        # Create hide button.
        self.btnToggle = QPushButton('Hide')
        self.btnToggle.clicked.connect(self.toggleGroupboxes)

        # Create style button.
        self.btnStyle = QPushButton('Style')
        self.btnStyle.clicked.connect(self.toggleStyle)

        btnLayout.addWidget(self.btnSubmit)
        btnLayout.addWidget(self.btnToggle)
        btnLayout.addWidget(self.btnStyle)

        mainLayout.addLayout(btnLayout)
    # }

    '''Update OS Selection Label'''
    def updateOsLabel(self, text):
    # {
        if self.sender().isChecked():
            self.selectedOsLabel.setText(text)
    # }

    '''Show all selections'''
    def showSelections(self):
    # {
        os = self.selectedOsLabel.text()
        langs = []

        if self.cbPython.isChecked():
            langs.append('Python')

        if self.cbJava.isChecked():
            langs.append('Java')

        if self.cbCpp.isChecked():
            langs.append('C++')

        if self.cbJs.isChecked():
            langs.append('JavaScript')

        result = f'OS: {os}\nProgram Language: {", ".join(langs)}'
        QMessageBox.information(self, 'Select Results', result)
    # }

    '''Toggle group box visibility'''
    def toggleGroupboxes(self):
    # {
        visible = self.radioGroupbox.isVisible()
        self.radioGroupbox.setVisible(not visible)
        self.checkboxGroupbox.setVisible(not visible)
        self.btnToggle.setText('Display options' if visible else 'Hide options')
    # }

    '''Change GroupBox style'''
    def toggleStyle(self):
    # {
        if self.radioGroupbox.styleSheet():
            self.radioGroupbox.setStyleSheet('')
            self.checkboxGroupbox.setStyleSheet('')
        else:
            style = '''
            QGroupBox {
                border: 2px solid #3498db;
                border-radius: 5px;
                margin-top: 1ex;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
                color: #2980b9;
            }
            '''

            self.radioGroupbox.setStyleSheet(style)
            self.checkboxGroupbox.setStyleSheet(style)
    # }
# }

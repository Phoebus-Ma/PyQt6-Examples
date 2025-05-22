###
# PyQt6 ToolBox main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBox,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ToolBox'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create main layout.
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # Creaete ToolBox.
        self.toolbox = QToolBox()

        # Create 3 pages.
        self.createPage1()
        self.createPage2()
        self.createPage3()

        # Add ToolBox to main layout.
        layout.addWidget(self.toolbox)

        # Connect signal (Triggered when the page is switched).
        self.toolbox.currentChanged.connect(self.pageChanged)
    # }

    '''Create first tool page'''
    def createPage1(self):
    # {
        page = QWidget()
        layout = QVBoxLayout(page)

        # Add widget.
        layout.addWidget(QLabel('User Login'))
        layout.addWidget(QLineEdit(placeholderText='User'))
        layout.addWidget(QLineEdit(placeholderText='Password'))
        layout.addWidget(QPushButton('Login'))

        # Add page to ToolBox and set icon, text.
        self.toolbox.addItem(page, ' Login Page')
    # }

    '''Create second tool page'''
    def createPage2(self):
    # {
        page = QWidget()
        layout = QVBoxLayout(page)

        layout.addWidget(QLabel('Setting Options'))
        layout.addWidget(QPushButton('Theme'))
        layout.addWidget(QPushButton('Notice'))
        layout.addWidget(QPushButton('Advanced'))

        self.toolbox.addItem(page, 'Setting Page')
    # }

    '''Create third tool page'''
    def createPage3(self):
    # {
        page = QWidget()
        layout = QVBoxLayout(page)

        layout.addWidget(QLabel('Help'))
        layout.addWidget(QLabel('Version: 1.0.0'))
        layout.addWidget(QPushButton('Docs'))
        layout.addWidget(QPushButton('Contact'))

        self.toolbox.addItem(page, ' Help Page')
    # }

    '''Page switch handler'''
    def pageChanged(self, index):
    # {
        print(f'Switch Page {index} - {self.toolbox.itemText(index)}')
    # }
# }

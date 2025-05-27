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
        mainLayout = QVBoxLayout()

        # Creaete ToolBox.
        self.toolbox = QToolBox()

        # Create 3 pages.
        self.createPage1()
        self.createPage2()
        self.createPage3()

        # Add ToolBox to main layout.
        mainLayout.addWidget(self.toolbox)

        # Connect signal (Triggered when the page is switched).
        self.toolbox.currentChanged.connect(self.pageChanged)

        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)
    # }

    '''Create first tool page'''
    def createPage1(self):
    # {
        page = QWidget()
        pageLayout1 = QVBoxLayout()

        # Add widget.
        pageLayout1.addWidget(QLabel('User Login'))
        pageLayout1.addWidget(QLineEdit(placeholderText='User'))
        pageLayout1.addWidget(QLineEdit(placeholderText='Password'))
        pageLayout1.addWidget(QPushButton('Login'))

        # Add page to ToolBox and set icon, text.
        page.setLayout(pageLayout1)
        self.toolbox.addItem(page, ' Login Page')
    # }

    '''Create second tool page'''
    def createPage2(self):
    # {
        page = QWidget()
        pageLayout2 = QVBoxLayout()

        pageLayout2.addWidget(QLabel('Setting Options'))
        pageLayout2.addWidget(QPushButton('Theme'))
        pageLayout2.addWidget(QPushButton('Notice'))
        pageLayout2.addWidget(QPushButton('Advanced'))

        page.setLayout(pageLayout2)
        self.toolbox.addItem(page, 'Setting Page')
    # }

    '''Create third tool page'''
    def createPage3(self):
    # {
        page = QWidget()
        pageLayout3 = QVBoxLayout()

        pageLayout3.addWidget(QLabel('Help'))
        pageLayout3.addWidget(QLabel('Version: 1.0.0'))
        pageLayout3.addWidget(QPushButton('Docs'))
        pageLayout3.addWidget(QPushButton('Contact'))

        page.setLayout(pageLayout3)
        self.toolbox.addItem(page, ' Help Page')
    # }

    '''Page switch handler'''
    def pageChanged(self, index):
    # {
        print(f'Switch Page {index} - {self.toolbox.itemText(index)}')
    # }
# }

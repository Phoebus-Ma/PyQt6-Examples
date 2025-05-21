###
# PyQt6 MenuBar main window.
#
# License - MIT.
###

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QMainWindow,
    QMenuBar,
    QTextEdit
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Menubar'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create text edit.
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Create menu.
        self.createMenuBar()
    # }

    '''Create menu and items'''
    def createMenuBar(self):
    # {
        # Create menu object.
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        # File menu.
        fileMenu = menubar.addMenu('File(&F)')

        # New action.
        newAction = QAction(QIcon(), 'New(&N)', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)

        # Open action.
        openAction = QAction(QIcon(), 'Open(&O)', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        # Save option.
        saveAction = QAction(QIcon(), 'Save(&S)', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        # Add divider.
        fileMenu.addSeparator()

        # Quit action.
        exitAction = QAction(QIcon(), 'Quit(&Q)', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Edit menu.
        editMenu = menubar.addMenu('Edit(&E)')

        # Copy action.
        copyAction = QAction('Copy(&C)', self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.triggered.connect(self.textEdit.copy)
        editMenu.addAction(copyAction)

        # Paste action.
        pasteAction = QAction('Paste(&V)', self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.triggered.connect(self.textEdit.paste)
        editMenu.addAction(pasteAction)

        # Help menu.
        helpMenu = menubar.addMenu('Help(&H)')
        aboutAction = QAction('About', self)
        aboutAction.triggered.connect(self.showAbout)
        helpMenu.addAction(aboutAction)
    # }

    '''New file slot'''
    def newFile(self):
    # {
        self.textEdit.clear()
        self.statusBar().showMessage('New File', 2000)
    # }

    '''Open file slot'''
    def openFile(self):
    # {
        self.statusBar().showMessage('Open File...', 2000)

        # Add open file function.
        pass
    # }

    '''Save file slot'''
    def saveFile(self):
    # {
        self.statusBar().showMessage('Save File...', 2000)

        # Add save file function.
        pass
    # }

    '''Show about slot'''
    def showAbout(self):
    # {
        self.statusBar().showMessage('PyQt6 MenuBar example v1.0', 3000)
    # }
# }

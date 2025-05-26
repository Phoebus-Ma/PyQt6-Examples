###
# PyQt6 notepad main window.
#
# License - MIT.
###

import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QStatusBar,
    QFileDialog
)
from PyQt6.QtGui import QAction
from EditorStyle import CodeEditor


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Notepad'
        self.winWidth  = 640
        self.winHeight = 480

        self.editor = CodeEditor()
        self.currentFile = None

        self.setCentralWidget(self.editor)
        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        menuBar = self.menuBar()

        # File menu.
        fileMenu = menuBar.addMenu("File")

        newAction = QAction("New File", self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)

        openAction = QAction("Open File...", self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        saveAction = QAction("Save", self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        saveAsAction = QAction("Save as...", self)
        saveAsAction.triggered.connect(self.saveAsFile)
        fileMenu.addAction(saveAsAction)

        # Edit menu.
        editMenu = menuBar.addMenu("Edit")
        undoAction = QAction("Undo", self)
        undoAction.triggered.connect(self.editor.undo)
        editMenu.addAction(undoAction)

        redoAction = QAction("Redo", self)
        redoAction.triggered.connect(self.editor.redo)
        editMenu.addAction(redoAction)

        # Status bar.
        self.statusBar = QStatusBar()
        self.statusLabel = QLabel(sys.platform)
        self.statusBar.addPermanentWidget(self.statusLabel)
        self.setStatusBar(self.statusBar)
    # }

    def newFile(self):
    # {
        self.editor.clear()
        self.currentFile = None
        self.setWindowTitle('Untitled')
    # }

    def openFile(self):
    # {
        fileName, _ = QFileDialog.getOpenFileName(self)
        if fileName:
            with open(fileName, 'r') as f:
                self.editor.setPlainText(f.read())

            self.currentFile = fileName
            self.setWindowTitle(fileName)
    # }

    def saveFile(self):
    # {
        if self.currentFile is None:
            return self.saveAsFile()

        with open(self.currentFile, 'w') as f:
            f.write(self.editor.toPlainText())

        self.setWindowTitle(self.currentFile)
        self.statusBar.showMessage('Saved', 3000)
    # }

    def saveAsFile(self):
    # {
        fileName, _ = QFileDialog.getSaveFileName(self)
        if fileName:
            self.currentFile = fileName
            self.saveFile()
    # }
# }

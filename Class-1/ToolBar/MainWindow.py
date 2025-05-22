###
# PyQt6 ToolBar main window.
#
# License - MIT.
###

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QStyle
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ToolBar'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create toolbar.
        toolbar = QToolBar("Main toolbar")
        self.addToolBar(toolbar)

        # Create actions with icon.
        newIcon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        self.newAction = QAction(newIcon, "New", self)
        self.newAction.triggered.connect(self.onNew)
        self.newAction.setStatusTip("New File")

        openIcon = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogOpenButton)
        self.openAction = QAction(openIcon, "Open", self)
        self.openAction.triggered.connect(self.onOpen)
        self.openAction.setStatusTip("Open File")

        saveIcon = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton)
        self.saveAction = QAction(saveIcon, "Save", self)
        self.saveAction.triggered.connect(self.onSave)
        self.saveAction.setStatusTip("Save File")

        # Add action to toolbar.
        toolbar.addAction(self.newAction)
        toolbar.addAction(self.openAction)
        toolbar.addAction(self.saveAction)

        # Add divider.
        toolbar.addSeparator()

        # Add other types of controls (Exp: switch button).
        self.toggleAction = QAction("Switch", self)
        self.toggleAction.setCheckable(True)
        self.toggleAction.toggled.connect(self.onToggle)
        toolbar.addAction(self.toggleAction)

        # Initilize status bar.
        self.statusBar().showMessage("Ready")
    # }

    def onNew(self):
    # {
        self.statusBar().showMessage("New file action.", 3000)
        print("Execute new file.")
    # }

    def onOpen(self):
    # {
        self.statusBar().showMessage("Open file aciton.", 3000)
        print("Execute open file.")
    # }

    def onSave(self):
    # {
        self.statusBar().showMessage("Save file action.", 3000)
        print("Execute save file.")
    # }

    def onToggle(self, state):
    # {
        message = "Swtich: " + ("True" if state else "False")
        self.statusBar().showMessage(message, 3000)
        print(f"Status: {state}")
    # }
# }

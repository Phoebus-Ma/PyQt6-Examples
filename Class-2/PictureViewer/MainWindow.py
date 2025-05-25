###
# PyQt6 picture viewer main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QScrollArea,
    QFileDialog,
    QToolBar
)
from PyQt6.QtGui import (
    QPixmap,
    QAction,
    QKeySequence,
    QPalette
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title      = 'Picture Viewer'
        self.winWidth   = 320
        self.winHeight  = 240
        self.maxPositon = 0

        self.currentImage = None
        self.imageFiles   = []
        self.currentIndex = 0
        self.scaleFactor  = 1.0

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create control.
        self.scrollArea = QScrollArea()
        self.labelImage = QLabel()
        self.labelImage.setBackgroundRole(QPalette.ColorRole.Dark)
        self.labelImage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelImage.setScaledContents(True)

        # Set scroll area.
        self.scrollArea.setWidget(self.labelImage)
        self.scrollArea.setVisible(True)
        self.setCentralWidget(self.scrollArea)

        # Create tool bar.
        toolbar = QToolBar("MainToolBar")
        toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(toolbar)

        # Create action.
        actionOpen = QAction("Open", self)
        actionOpen.setShortcut(QKeySequence.StandardKey.Open)
        actionOpen.triggered.connect(self.openImage)

        actionZoomIn = QAction("ZoomIn", self)
        actionZoomIn.setShortcut(QKeySequence.StandardKey.ZoomIn)
        actionZoomIn.triggered.connect(self.zoomIn)

        actionZoomOut = QAction("ZoomOut", self)
        actionZoomOut.setShortcut(QKeySequence.StandardKey.ZoomOut)
        actionZoomOut.triggered.connect(self.zoomOut)

        actionPrev = QAction("Prev", self)
        actionPrev.setShortcut("Left")
        actionPrev.triggered.connect(self.prevImage)

        actionNext = QAction("Next", self)
        actionNext.setShortcut("Right")
        actionNext.triggered.connect(self.nextImage)

        # Add toolbar button.
        toolbar.addAction(actionOpen)
        toolbar.addAction(actionZoomIn)
        toolbar.addAction(actionZoomOut)
        toolbar.addAction(actionPrev)
        toolbar.addAction(actionNext)

        # Status bar.
        self.statusBar().showMessage("Ready")
    # }
        
    def openImage(self):
    # {
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open picture file", "", 
            "Picture file (*.jpg *.jpeg *.png *.bmp *.gif)"
        )

        if fileName:
            self.loadImage(fileName)
            self.imageFiles = [fileName]
            self.currentIndex = 0
    # }

    def loadImage(self, filePath):
    # {
        self.currentImage = QPixmap(filePath)

        if self.currentImage.isNull():
            self.statusBar().showMessage("Unable to load picture")
            return

        self.labelImage.setPixmap(self.currentImage)
        self.scaleFactor = 1.0
        self.labelImage.resize(self.scaleFactor * self.currentImage.size())
        self.statusBar().showMessage(filePath)
        self.setWindowTitle(f"Picture Viewer - {filePath.split('/')[-1]}")
    # }

    def zoomIn(self):
    # {
        self.scaleImage(1.25)
    # }

    def zoomOut(self):
    # {
        self.scaleImage(0.8)
    # }

    def scaleImage(self, factor):
    # {
        self.scaleFactor *= factor
        self.labelImage.resize(self.scaleFactor * self.labelImage.pixmap().size())
        self.adjustScrollbar()
    # }

    def adjustScrollbar(self):
    # {
        self.scrollArea.horizontalScrollBar().setValue(
            int(self.scaleFactor * self.scrollArea.horizontalScrollBar().value())
        )

        self.scrollArea.verticalScrollBar().setValue(
            int(self.scaleFactor * self.scrollArea.verticalScrollBar().value())
        )
    # }

    def prevImage(self):
    # {
        if self.currentIndex > 0:
            self.currentIndex -= 1
            self.loadImage(self.imageFiles[self.currentIndex])
    # }

    def nextImage(self):
    # {
        if self.currentIndex < len(self.imageFiles) - 1:
            self.currentIndex += 1
            self.loadImage(self.imageFiles[self.currentIndex])
    # }

    def keyPressEvent(self, event):
    # {
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        super().keyPressEvent(event)
    # }
# }

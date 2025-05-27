###
# PyQt6 OpenGL main window.
#
# License - MIT.
###

from PyQt6.QtWidgets import QMainWindow
from Triangle import Triangle


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'OpenGL'
        self.winWidth  = 640
        self.winHeight = 480

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        self.glWidget = Triangle(self)
        self.setCentralWidget(self.glWidget)
    # }
# }

###
# PyQt6 ProgressBar main window.
#
# License - MIT.
###

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QProgressBar
)


class WorkerThread(QThread):
# {
    # Custom signal to update progress.
    progressUpdated = pyqtSignal(int)

    '''Simulate long task.'''
    def run(self):
    # {
        for i in range(101):
            # Signal progress value.
            self.progressUpdated.emit(i)

            # Simulation task.
            self.msleep(50)
    # }
# }


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ProgressBar'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create control.
        self.progressBar = QProgressBar()
        self.btnStart    = QPushButton('Start')
        self.btnStart.clicked.connect(self.startTask)

        # Set layout.
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        layout.addWidget(self.btnStart)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Initialize progress bar.
        self.progressBar.setValue(0)
        self.progressBar.setRange(0, 100)
    # }

    '''Start worker thread.'''
    def startTask(self):
    # {
        self.btnStart.setEnabled(False)
        self.worker = WorkerThread()
        self.worker.progressUpdated.connect(self.updateProgress)
        self.worker.finished.connect(self.taskFinished)
        self.worker.start()
    # }

    '''Update progress.'''
    def updateProgress(self, value):
    # {
        self.progressBar.setValue(value)
    # }

    '''Called when task is complete.'''
    def taskFinished(self):
    # {
        self.btnStart.setEnabled(True)
        self.progressBar.setValue(0)
    # }
# }

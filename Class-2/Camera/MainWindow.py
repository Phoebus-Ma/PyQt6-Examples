###
# PyQt6 camera app main window.
#
# License - MIT.
###

import os
from datetime import datetime
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
)
from PyQt6.QtMultimedia import (
    QMediaDevices,
    QCamera,
    QImageCapture,
    QMediaCaptureSession
)
from PyQt6.QtMultimediaWidgets import QVideoWidget


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title      = 'Camera'
        self.winWidth   = 640
        self.winHeight  = 480
        self.maxPositon = 0

        self._captureSession = QMediaCaptureSession()

        self.initUI()
        self.initCamera()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # Use QVideoWidget for video output.
        self.videoWidget = QVideoWidget()
        layout.addWidget(self.videoWidget)

        # Photo button.
        self.btnCapture = QPushButton('Photo')
        self.btnCapture.clicked.connect(self.captureImage)
        layout.addWidget(self.btnCapture)
    # }

    def initCamera(self):
    # {
        # Get camera device.
        cameras = QMediaDevices.videoInputs()
        if not cameras:
            print('Camera device not found.')
            return

        # Configure camera.
        self.camera = QCamera(cameras[0])
        self._captureSession.setCamera(self.camera)  #  Bind camera to session.

        # Configure video output.
        self._captureSession.setVideoOutput(self.videoWidget)

        # Configure image capture.
        self.imageCapture = QImageCapture(self.camera)
        self._captureSession.setImageCapture(self.imageCapture)  # Bind image capture.
        self.imageCapture.imageCaptured.connect(self.imageCaptured)
        self.imageCapture.errorOccurred.connect(self.captureError)

        # Start camera.
        self.camera.start()
    # }

    def captureImage(self):
    # {
        filename = os.getcwd() + '/' + str(datetime.now()) + '.jpg'
        self.imageCapture.captureToFile(filename)
    # }

    def imageCaptured(self, id, preview):
    # {
        print(f'Picture captured, ID: {id}')
    # }

    def imagSaved(self, id, path):
    # {
        print(f'Picture saved to path: {path}')
    # }

    def captureError(self, id, error, errorStr):
    # {
        print(f'Capture error: {errorStr}')
    # }

    def closeEvent(self, event):
    # {
        if self.camera.isActive():
            self.camera.stop()
        event.accept()
    # }
# }

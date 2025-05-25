###
# PyQt6 video player main window.
#
# License - MIT.
###

import os
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QFileDialog
)
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title      = 'Video Player'
        self.winWidth   = 640
        self.winHeight  = 480
        self.maxPositon = 0

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Initialize video player.
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)

        # Connect signal.
        self.player.positionChanged.connect(self.updatePosition)
        self.player.durationChanged.connect(self.updateDuration)
        self.player.playbackStateChanged.connect(self.updateButtons)

        # Create control.
        self.videoWidget = QVideoWidget()
        self.btnPlay = QPushButton('Play')
        self.btnStop = QPushButton('Stop')
        self.btnOpen = QPushButton('Open')

        # Volumn control.
        self.sliderVolume = QSlider(Qt.Orientation.Horizontal)
        self.sliderVolume.setRange(0, 100)
        self.sliderVolume.setValue(50)
        self.sliderVolume.valueChanged.connect(self.setVolume)

        # Slider.
        self.sliderPosition = QSlider(Qt.Orientation.Horizontal)
        self.sliderPosition.setMinimum(0)
        self.sliderPosition.sliderMoved.connect(self.setPosition)

        # Show time.
        self.labelTime = QLabel('00:00 / 00:00')
        self.labelTime.setMaximumHeight(20)

        # Layout.
        progressLayout = QHBoxLayout()
        progressLayout.addWidget(self.sliderPosition)
        progressLayout.addWidget(self.labelTime)

        controlLayout = QHBoxLayout()
        controlLayout.addWidget(self.btnOpen)
        controlLayout.addWidget(self.btnPlay)
        controlLayout.addWidget(self.btnStop)
        controlLayout.addWidget(self.sliderVolume)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.videoWidget)
        mainLayout.addLayout(progressLayout)
        mainLayout.addLayout(controlLayout)

        self.setLayout(mainLayout)

        # Initial state disable control button.
        self.btnPlay.setEnabled(False)
        self.btnStop.setEnabled(False)

        # Connect button signal.
        self.btnOpen.clicked.connect(self.openFile)
        self.btnPlay.clicked.connect(self.togglePlay)
        self.btnStop.clicked.connect(self.stop)
    # }

    def openFile(self):
    # {
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open video file', '',
                                                  'Video file (*.mp4 *.avi *.mkv *.mov)')
        if fileName:
            self.player.setVideoOutput(self.videoWidget)
            self.player.setSource(QUrl.fromLocalFile(fileName))
            self.btnPlay.setEnabled(True)
            self.btnStop.setEnabled(True)
    # }

    def togglePlay(self):
    # {
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()
    # }

    def stop(self):
    # {
        self.player.stop()
    # }

    def setVolume(self, value):
    # {
        self.audioOutput.setVolume(value / 100)
    # }

    def updatePosition(self, position):
    # {
        self.sliderPosition.setValue(position)
        self.updateTimeDisplay()
    # }

    def updateDuration(self, duration):
    # {
        self.sliderPosition.setRange(0, duration)
        self.updateTimeDisplay()
    # }

    def setPosition(self, position):
    # {
        self.player.setPosition(position)
    # }

    def updateTimeDisplay(self):
    # {
        duration = self.player.duration()
        position = self.player.position()

        # Time format (mm:ss).
        durationTime = self.formatTime(duration)
        positionTime = self.formatTime(position)
        self.labelTime.setText(f'{positionTime} / {durationTime}')
    # }

    def formatTime(self, ms):
    # {
        seconds = (ms // 1000) % 60
        minutes = (ms // (1000 * 60)) % 60
        return f'{minutes:02d}:{seconds:02d}'
    # }

    def updateButtons(self):
    # {
        state = self.player.playbackState()
        self.btnPlay.setText('Pause'
                             if state == QMediaPlayer.PlaybackState.PlayingState
                             else 'Play')
    # }
# }

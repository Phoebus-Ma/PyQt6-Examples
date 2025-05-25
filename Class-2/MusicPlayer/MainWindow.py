###
# PyQt6 music player main window.
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
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title      = 'Music Player'
        self.winWidth   = 320
        self.winHeight  = 240
        self.maxPositon = 0

        self.initUI()
    # }

    def initUI(self):
    # {
         # Initialize music player.
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)

        # connect signal.
        self.player.positionChanged.connect(self.updatePosition)
        self.player.durationChanged.connect(self.updateDuration)

        # Create control.
        self.lblName = QLabel('File: None')

        self.btnPlay = QPushButton('Play')
        self.btnStop = QPushButton('Stop')
        self.btnOpen = QPushButton('Open')

        self.volumeSlider = QSlider(Qt.Orientation.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(50)
        self.volumeSlider.valueChanged.connect(self.setVolume)

        self.positionSlider = QSlider(Qt.Orientation.Horizontal)
        self.positionSlider.setMinimum(0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        # Layout.
        controlLayout = QHBoxLayout()
        controlLayout.addWidget(self.btnOpen)
        controlLayout.addWidget(self.btnPlay)
        controlLayout.addWidget(self.btnStop)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.lblName)
        mainLayout.addLayout(controlLayout)
        mainLayout.addWidget(self.positionSlider)
        mainLayout.addWidget(self.volumeSlider)

        self.setLayout(mainLayout)

        # Connect button signal.
        self.btnOpen.clicked.connect(self.openFile)
        self.btnPlay.clicked.connect(self.togglePlay)
        self.btnStop.clicked.connect(self.stop)
    # }

    def openFile(self):
    # {
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open audio file', '', 
                                                 'Audio file (*.mp3 *.wav *.ogg)')
        if fileName:
            self.lblName.setText('File: ' + os.path.basename(fileName))
            self.player.setSource(QUrl.fromLocalFile(fileName))
            self.btnPlay.setEnabled(True)
            self.btnStop.setEnabled(True)
    # }

    def togglePlay(self):
    # {
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.btnPlay.setText('Play')
        else:
            self.player.play()
            self.btnPlay.setText('Pause')
    # }

    def stop(self):
    # {
        self.player.stop()
        self.btnPlay.setText('Play')
    # }

    def setVolume(self, value):
    # {
        self.audioOutput.setVolume(value / 100)
    # }

    '''Update progress bar when position changes (millisecondss)'''
    def updatePosition(self, position):
    # {
        self.positionSlider.setValue(position)
        
        if (position >= self.maxPositon):
            self.btnPlay.setText('Play')
    # }

    '''Set the progress bar range when the file change (millisecondss)'''
    def updateDuration(self, duration):
    # {
        self.positionSlider.setRange(0, duration)

        # duration == self.positionSlider.maximum().
        self.maxPositon = self.positionSlider.maximum()
    # }

    '''Set playback position when the user drags'''
    def setPosition(self, position):
    # {
        self.player.setPosition(position)
    # }
# }

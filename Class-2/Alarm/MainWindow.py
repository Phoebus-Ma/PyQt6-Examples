###
# PyQt6 alarm main window.
#
# License - MIT.
###

from PyQt6.QtCore import (
    Qt,
    QTimer,
    QDateTime
)
from PyQt6.QtWidgets import (
    QWidget,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
    QTimeEdit
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'Alarm'
        self.winWidth  = 320
        self.winHeight = 240

        self.checkTime = 10     # Check alarm every 10 seconds.
        self.alarmTime = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkAlarm)

        self.oneshotTimer = QTimer()
        self.oneshotTimer.setSingleShot(True)
        self.oneshotTimer.timeout.connect(self.startTimer)

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Create control.
        self.timeEdit = QTimeEdit()
        self.timeEdit.setDisplayFormat("HH:mm")
        self.timeEdit.setTime(QDateTime.currentDateTime().time())
        
        self.btnSet      = QPushButton("Set")
        self.btnStop     = QPushButton("Stop")

        self.labelTitle  = QLabel("Set alarm time:")
        self.labelStatus = QLabel("Status: Not set")
        self.labelStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create layout.
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.labelTitle)
        mainLayout.addWidget(self.timeEdit)
        mainLayout.addWidget(self.btnSet)
        mainLayout.addWidget(self.btnStop)
        mainLayout.addWidget(self.labelStatus)

        self.setLayout(mainLayout)

        # Connect signal.
        self.btnSet.clicked.connect(self.setAlarm)
        self.btnStop.clicked.connect(self.stopAlarm)
    # }

    def setAlarm(self):
    # {
        # Get current time, and set alarm time (hh:mm:00)
        currentTime  = QDateTime.currentDateTime()
        selectedTime = self.timeEdit.time()
        selectedTime = selectedTime.addSecs(-selectedTime.second())

        # Calculate alarm time.
        self.alarmTime = QDateTime(currentTime.date(), selectedTime)

        # If the alarm time is less than the current time,
        # Increase the alarm by one day.
        if self.alarmTime <= currentTime:
            self.alarmTime = self.alarmTime.addDays(1)

        self.labelStatus.setText(
            f"Status: alarm - {self.alarmTime.toString('yyyy-MM-dd HH:mm')}")

        # Seconds alignment.
        currentSec = self.timeEdit.time().second()
        self.oneshotTimer.start(self.checkTime - (currentSec % self.checkTime))
    # }

    def checkAlarm(self):
    # {
        currentTime = QDateTime.currentDateTime()
        if currentTime >= self.alarmTime:
            self.timer.stop()
            self.showAlarm()
            self.labelStatus.setText("Status: Alarm triggered!")
    # }

    def showAlarm(self):
    # {
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Time is up!")
        msg.setWindowTitle(self.title)
        msg.exec()
    # }

    def stopAlarm(self):
    # {
        self.timer.stop()
        self.labelStatus.setText("Status: Stopped")
    # }

    def startTimer(self):
    # {
        # seconds to milliseconds (x1000).
        self.timer.start(self.checkTime * 1000)
    # }
# }

###
# PyQt6 calendar widget main window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QCalendarWidget,
    QVBoxLayout,
    QLabel
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'CalendarWidget'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QVBoxLayout()

        # Creaete label for show selected item.
        self.labelInfo = QLabel("Selected Date: None", self)
        self.labelInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a calendar widget.
        self.calendarWidget = QCalendarWidget(self)
        self.calendarWidget.setGridVisible(True)  # Display Grid.

        # Calendar widget slot.
        self.calendarWidget.clicked.connect(self.onDateChanged)

        mainLayout.addWidget(self.labelInfo)
        mainLayout.addWidget(self.calendarWidget)

        self.setLayout(mainLayout)
    # }

    def onDateChanged(self, date):
    # {
        # Update label content when date changes.
        self.labelInfo.setText(f"Selected Date: {date.toString(Qt.DateFormat.ISODate)}")

        print(f"Selected Date: {date.toString(Qt.DateFormat.ISODate)}")
    # }
# }

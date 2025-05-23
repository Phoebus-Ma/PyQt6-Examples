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

        mainlayout = QVBoxLayout()

        # Creaete label for show selected item.
        self.info_label = QLabel("Selected Date: None", self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a calendar widget.
        self.calendar_widget = QCalendarWidget(self)
        self.calendar_widget.setGridVisible(True)  # Display Grid.

        # Calendar widget slot.
        self.calendar_widget.clicked.connect(self.on_date_changed)

        mainlayout.addWidget(self.info_label)
        mainlayout.addWidget(self.calendar_widget)

        self.setLayout(mainlayout)
    # }

    def on_date_changed(self, date):
    # {
        # Update label content when date changes.
        self.info_label.setText(f"Selected Date: {date.toString(Qt.DateFormat.ISODate)}")

        print(f"Selected Date: {date.toString(Qt.DateFormat.ISODate)}")
    # }
# }

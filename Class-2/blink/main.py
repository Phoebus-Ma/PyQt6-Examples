###
# PyQt6 QPushButton example.
#
# License - MIT.
###


import sys
from gpiozero import LED
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, \
    QWidget, QVBoxLayout, QPushButton


def toggleClicked(button: QPushButton):
# {
    if button.isChecked():
        led.value = 1
        print('LED on.')
    else:
        led.value = 0
        print('LED off.')
# }


def createToggleButton() -> QPushButton:
# {
    button = QPushButton()

    button.setText('OFF')
    button.setFixedSize(100, 30)
    button.setCheckable(True)
    button.setStyleSheet('background-color: red')

    return button
# }


# QPushButton API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html>
def main():
# {
    app    = QApplication([])
    widget = QWidget()

    # Create toggle button.
    btnToggle = createToggleButton()
    btnToggle.clicked.connect(lambda: toggleClicked(btnToggle))

    # Layout.
    layout = QVBoxLayout()
    layout.addWidget(btnToggle)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Widget.
    widget.setLayout(layout)
    widget.setFixedSize(300, 200)
    widget.show()

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    # Create global led device.
    led = LED(3)

    main()

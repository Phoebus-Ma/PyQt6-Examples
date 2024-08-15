###
# PyQt6 QPushButton example.
#
# License - MIT.
###

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, \
    QWidget, QVBoxLayout, QPushButton, QMessageBox


def toggleClicked(button: QPushButton):
# {
    if button.isChecked():
        button.setText('ON')
    else:
        button.setText('OFF')
# }


def buttonClicked(widget: QWidget):
# {
    print('---- Button clicked. ----')

    # message = QMessageBox()
    # message.setText('Button clicked.')
    # message.show()

    QMessageBox.information(widget, 'Test', 'Button clicked.')
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


def createPushButton() -> QPushButton:
# {
    button = QPushButton()

    button.setText('OK')
    button.setFixedSize(100, 30)

    return button
# }

# QPushButton API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html>
# QMessageBox API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html>
def main():
# {
    app    = QApplication([])
    widget = QWidget()

    # Controls.
    btnMessage = createPushButton()
    btnMessage.clicked.connect(lambda: buttonClicked(widget))

    btnToggle = createToggleButton()
    btnToggle.clicked.connect(lambda: toggleClicked(btnToggle))

    # Layout.
    layout = QVBoxLayout()

    layout.addWidget(btnMessage)
    layout.addWidget(btnToggle)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Widget.
    widget.setLayout(layout)
    widget.setFixedSize(300, 200)
    widget.show()

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    main()

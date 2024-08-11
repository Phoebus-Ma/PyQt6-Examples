###
# PyQt6 QPushButton example.
#
# License - MIT.
###

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import Qt


def buttonClick(widget: QWidget):
# {
    print('---- Button clicked. ----')

    # message = QMessageBox()
    # message.setText('Button clicked.')
    # message.show()

    QMessageBox.information(widget, 'Test', 'Button clicked.')
# }


# QPushButton API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html>
# QMessageBox API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html>
def main():
# {
    app = QApplication([])
    widget = QWidget()

    # Controls.
    button = QPushButton()

    button.setText('OK')
    button.setFixedSize(100, 30)
    button.clicked.connect(lambda: buttonClick(widget))

    # Layout.
    layout = QVBoxLayout()

    layout.addWidget(button)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Widget.
    widget.setLayout(layout)
    widget.setFixedSize(300, 200)
    widget.show()

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    main()

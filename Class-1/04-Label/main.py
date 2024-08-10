###
# PyQt6 QLabel example.
#
# License - MIT.
###

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer


def updateLabel(label: QLabel):
# {
    label.setText('Niubility !')
# }


# QWidget API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html>
# QLabel  API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html>
# QTimer  API : <https://doc.qt.io/qtforpython-6/PySide6/QtCore/QTimer.html>
def main():
# {
    app = QApplication([])

    # Controls.
    # English: hello.
    # Chinese: nihao.
    label1 = QLabel()
    label1.setText('hello world.')

    label2 = QLabel()
    label2.setText('nihao world.')

    label3 = QLabel()
    label3.setText('Great !')

    # Layout.
    layout = QVBoxLayout()

    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Widget.
    widget = QWidget()

    widget.setLayout(layout)
    widget.resize(300, 200)
    widget.show()

    # Change label context.
    QTimer.singleShot(3000, lambda: updateLabel(label3))

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    main()

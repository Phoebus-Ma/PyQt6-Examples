###
# PyQt6 QLabel example.
#
# License - MIT.
###

import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap


# Slot.
def updateLabel(label: QLabel):
# {
    # English: hello.
    # Chinese: nihao.
    label.setText('nihao world.')
# }


def createUpdateTimer(label: QLabel):
# {
    # Change label context.
    QTimer.singleShot(3000, lambda: updateLabel(label))
# }


def createImageLabel() -> QLabel:
# {
    imgLabel = QLabel()
    imgLabel.setPixmap(QPixmap('test.jpg'))

    return imgLabel
# }


def createLinkLabel() -> QLabel:
# {
    urlLink = '<a href="http://www.bing.com"> Bing </a>'

    linkLabel = QLabel()
    linkLabel.setText(urlLink)
    linkLabel.setOpenExternalLinks(True)

    return linkLabel
# }


def createTextLabel() -> QLabel:
# {
    textLabel = QLabel()
    textLabel.setText('hello world.')

    return textLabel
# }


# QWidget API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html>
# QVBoxLayout : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QVBoxLayout.html>
# QLabel  API : <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html>
# QTimer  API : <https://doc.qt.io/qtforpython-6/PySide6/QtCore/QTimer.html>
def main():
# {
    app    = QApplication([])
    layout = QVBoxLayout()
    widget = QWidget()

    # Controls.
    label1 = createTextLabel()
    label2 = createLinkLabel()
    label3 = createImageLabel()

    # Layout.
    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Widget.
    widget.setLayout(layout)
    widget.resize(300, 200)
    widget.show()

    # Timer.
    createUpdateTimer(label1)

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    main()

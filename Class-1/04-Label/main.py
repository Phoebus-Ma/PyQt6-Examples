###
# PyQt6 QLabel example.
#
# License - MIT.
###

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap


# Slot.
def updateLabel(label: QLabel):
# {
    # English: hello.
    # Chinese: nihao.
    label.setText('nihao world.')
# }


def changeText(label: QLabel):
# {
    # Change label context.
    QTimer.singleShot(3000, lambda: updateLabel(label))
# }


def showImage() -> QLabel:
# {
    imgLabel = QLabel()
    imgLabel.setPixmap(QPixmap('test.jpg'))

    return imgLabel
# }


def showLink() -> QLabel:
# {
    urlLink = '<a href="http://www.bing.com"> Bing </a>'

    linkLabel = QLabel()
    linkLabel.setText(urlLink)
    linkLabel.setOpenExternalLinks(True)

    return linkLabel
# }


def showText() -> QLabel:
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
    app = QApplication([])

    # Controls.
    label1 = showText()
    label2 = showLink()
    label3 = showImage()

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

    # Timer.
    changeText(label1)

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    main()

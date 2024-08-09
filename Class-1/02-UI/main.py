###
# PyQt6 QLabel UI example.
#
# License - MIT.
###

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication


def main():
# {
    app = QApplication([])

    ui = uic.loadUi('hello.ui')
    ui.show()

    print(ui.label.text())

    app.exec()
# }

if '__main__' == __name__:
    main()

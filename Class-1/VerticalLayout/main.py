###
# PyQt6 QVBoxLayout example.
#
# License - MIT.
###

import sys
from PyQt6.QtWidgets import QApplication

from MainWindow import MainWindow


def main():
# {
    app = QApplication([])

    window = MainWindow()

    window.resize(300, 200)
    window.show()

    # Access class variable.
    print(window.title)

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    main()

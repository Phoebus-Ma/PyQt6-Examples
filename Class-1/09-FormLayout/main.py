###
# PyQt6 QFormLayout example.
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
    window.show()

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    main()

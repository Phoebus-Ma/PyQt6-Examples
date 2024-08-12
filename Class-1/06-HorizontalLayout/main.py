###
# PyQt6 QHBoxLayout example.
#
# License - MIT.
###

import sys
from PyQt6.QtWidgets import QApplication

# Locals
from MainWindow import MainWindow


def main():
# {
    app = QApplication([])

    window = MainWindow()
    window.show()

    # Access class variable.
    print(window.title)

    sys.exit(app.exec())
# }


if '__main__' == __name__:
    main()

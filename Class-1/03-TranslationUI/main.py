###
# PyQt6 QLabel UI example.
#
# License - MIT.
###

from PyQt6.QtWidgets import QApplication, QWidget

# Locals
from hello_ui import Ui_Form


def main():
# {
    app    = QApplication([])
    widget = QWidget()

    ui     = Ui_Form()
    ui.setupUi(widget)

    widget.show()

    print(ui.label.text())

    app.exec()
# }


if '__main__' == __name__:
    main()

###
# PyQt6 QLabel example.
#
# License - MIT.
###

from PyQt6.QtWidgets import *


def main():
# {
    # Create application.
    app   = QApplication([])

    # Create Label.
    label = QLabel('Hello World!')

    # Display Window.
    label.show()

    # Running and loop.
    app.exec()
# }


'''
1. (__name__   == '__main__') : is OK.
2. ('__main__' == __name__  ) : is OK.

When you lose a "=", such as:

3. (__name__   = '__main__')  : No error information.
4. ('__main__' = __name__)    : Generate error information.

So, we should prefer style 2.
'''

if '__main__' == __name__:
    main()

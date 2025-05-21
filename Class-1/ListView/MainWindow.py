###
# PyQt6 QListView main window.
#
# License - MIT.
###

from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QListView,
    QWidget
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'ListView'
        self.winWidth  = 350
        self.winHeight = 200

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        # Creeate layout and control.
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        # Create layout.
        layout = QVBoxLayout()

        # Create QListView.
        self.listView = QListView()

        # Create data model.
        self.model = QStringListModel()
        self.dataList = ['apple', 'banana', 'grape', 'mongon', 'orange', 'watermelon']
        self.model.setStringList(self.dataList)

        # Set model to list view.
        self.listView.setModel(self.model)

        # Set connect slot.
        self.listView.clicked.connect(self.onItemClicked)

        # Add list view to widget.
        layout.addWidget(self.listView)

        # Add layout.
        mainWidget.setLayout(layout)
    # }

    def onItemClicked(self, index):
    # {
        item = self.model.data(index, 0)
        print(f'You clicked: {item}')
    # }
# }

###
# PyQt6 QRadioButton window.
#
# License - MIT.
###

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QRadioButton,
    QGroupBox,
    QLabel,
    QButtonGroup
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'RadioButton'
        self.winWidth  = 320
        self.winHeight = 300

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.winWidth, self.winHeight)

        # Main layout.
        mainWidget = QWidget()
        layout = QVBoxLayout()

        self.setCentralWidget(mainWidget)
        mainWidget.setLayout(layout)

        # Example 1: basic radio button group.
        self.createBasicRadioButtons(layout)

        # Example 2: visual group.
        self.createGroupBox(layout)

        # Example 3: dynamic update.
        self.createDynamicExample(layout)

        # Display result label.
        self.resultLabel = QLabel('Select: None')
        layout.addWidget(self.resultLabel)
    # }

    '''Create basic radio button group (Use QButtonGroup)'''
    def createBasicRadioButtons(self, layout):
    # {
        groupBox = QGroupBox('Color select')
        vbox = QVBoxLayout()

        # Create button group.
        self.colorGroup = QButtonGroup(self)

        # Create radio button.
        colors = ['Red', 'Green', 'Blue']
        self.radioButtons = []
        for i, color in enumerate(colors):
            rb = QRadioButton(color)
            vbox.addWidget(rb)
            self.colorGroup.addButton(rb, i)  # Set ID.
            rb.toggled.connect(self.updateColorSelection)

        groupBox.setLayout(vbox)
        layout.addWidget(groupBox)
    # }

    '''Create visual group (Use QGroupBox)'''
    def createGroupBox(self, layout):
    # {
        groupBox = QGroupBox('OS Preference')
        hbox = QHBoxLayout()

        # Group 1.
        vbox1 = QVBoxLayout()
        osGroup1 = QButtonGroup(self)
        osList1 = ['Windows', 'macOS', 'Linux']
        for os in osList1:
            rb = QRadioButton(os)
            vbox1.addWidget(rb)
            osGroup1.addButton(rb)
        hbox.addLayout(vbox1)

        # Group 2.
        vbox2 = QVBoxLayout()
        osGroup2 = QButtonGroup(self)
        osList2 = ['Android', 'iOS']
        for os in osList2:
            rb = QRadioButton(os)
            vbox2.addWidget(rb)
            osGroup2.addButton(rb)
        hbox.addLayout(vbox2)

        groupBox.setLayout(hbox)
        layout.addWidget(groupBox)
    # }

    '''Create dynamic update example'''
    def createDynamicExample(self, layout):
    # {
        self.dynamicGroup = QGroupBox('Dynamic Contents')
        self.dynamicLayout = QVBoxLayout()

        # Trigger selection.
        self.triggerRadio = QRadioButton('Advanced option')
        self.triggerRadio.toggled.connect(self.toggleAdvancedOptions)

        # Advanced options container.
        self.advancedOptions = QWidget()
        advancedLayout = QVBoxLayout()
        self.option1 = QRadioButton('Advanced option 1')
        self.option2 = QRadioButton('Advanced option 2')
        advancedLayout.addWidget(self.option1)
        advancedLayout.addWidget(self.option2)
        self.advancedOptions.setLayout(advancedLayout)
        self.advancedOptions.hide()

        self.dynamicLayout.addWidget(self.triggerRadio)
        self.dynamicLayout.addWidget(self.advancedOptions)
        self.dynamicGroup.setLayout(self.dynamicLayout)
        layout.addWidget(self.dynamicGroup)
    # }

    '''Update color selection results'''
    def updateColorSelection(self):
    # {
        checkedButton = self.colorGroup.checkedButton()
        if checkedButton:
            self.resultLabel.setText(f'Color: {checkedButton.text()}')
    # }

    '''Toggle display of advanced options'''
    def toggleAdvancedOptions(self, checked):
    # {
        self.advancedOptions.setVisible(checked)
        if not checked:
            self.option1.setChecked(False)
            self.option2.setChecked(False)
    # }
# }

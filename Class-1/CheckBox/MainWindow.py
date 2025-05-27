###
# PyQt6 QCheckBox window.
#
# License - MIT.
###

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QGroupBox,
    QLabel,
    QPushButton,
    QButtonGroup
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'CheckBox'
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
        self.setCentralWidget(mainWidget)
        layout = QVBoxLayout()
        mainWidget.setLayout(layout)

        # Create control.
        self.createBasicCheckboxes(layout)
        self.createTristateCheckbox(layout)
        self.createGroupedCheckboxes(layout)
        self.createDynamicSection(layout)

        # Create result label.
        self.labelResult = QLabel('Select: ')
        layout.addWidget(self.labelResult)

        # Add reset button.
        btnReset = QPushButton('reset all selections')
        btnReset.clicked.connect(self.resetAll)
        layout.addWidget(btnReset)
    # }

    '''Basic checkbox'''
    def createBasicCheckboxes(self, layout):
    # {
        group = QGroupBox('Base checkbox')
        vbox  = QVBoxLayout()

        self.checkbox1 = QCheckBox('Item 1')
        self.checkbox2 = QCheckBox('Item 2')
        self.checkbox3 = QCheckBox('Item 3')

        # Set to single radio mode (mutual exclusion).
        self.exclusiveGroup = QButtonGroup(self)
        self.exclusiveGroup.setExclusive(True)

        for cb in [self.checkbox1, self.checkbox2, self.checkbox3]:
            self.exclusiveGroup.addButton(cb)
            cb.toggled.connect(self.updateSelection)

        vbox.addWidget(self.checkbox1)
        vbox.addWidget(self.checkbox2)
        vbox.addWidget(self.checkbox3)
        group.setLayout(vbox)
        layout.addWidget(group)
    # }

    '''Tri-state checkbox'''
    def createTristateCheckbox(self, layout):
    # {
        group = QGroupBox('Tri-state checkbox')
        vbox  = QVBoxLayout()

        self.cBoxTristate = QCheckBox('Tri-state option')
        self.cBoxTristate.setTristate(True)
        self.cBoxTristate.stateChanged.connect(self.handleTristate)

        self.stateLabel = QLabel('Status: No Selected')
        vbox.addWidget(self.cBoxTristate)
        vbox.addWidget(self.stateLabel)
        group.setLayout(vbox)
        layout.addWidget(group)
    # }

    '''Create group checkbox (multi-select)'''
    def createGroupedCheckboxes(self, layout):
    # {
        group = QGroupBox('Multi-select group')
        hbox  = QHBoxLayout()

        # First column.
        vbox1 = QVBoxLayout()
        self.langPython = QCheckBox('Python')
        self.langJava   = QCheckBox('Java')
        vbox1.addWidget(self.langPython)
        vbox1.addWidget(self.langJava)

        # Second column.
        vbox2 = QVBoxLayout()
        self.langCpp = QCheckBox('C++')
        self.langJS  = QCheckBox('JavaScript')
        vbox2.addWidget(self.langCpp)
        vbox2.addWidget(self.langJS)

        # Third column.
        for cb in [self.langPython, self.langJava, self.langCpp, self.langJS]:
            cb.toggled.connect(self.updateSelection)

        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        group.setLayout(hbox)
        layout.addWidget(group)
    # }

    '''Dynamic content control'''
    def createDynamicSection(self, layout):
    # {
        self.dynamicGroup = QGroupBox('Dynamic content control')
        vbox = QVBoxLayout()

        # Main checkbox.
        self.cboxEnableExtra = QCheckBox('Advanced option')
        self.cboxEnableExtra.toggled.connect(self.toggleAdvanced)

        # Advanced options container.
        self.advancedWidget  = QWidget()
        advancedLayout       = QVBoxLayout()
        self.advancedOption1 = QCheckBox('Item 1')
        self.advancedOption2 = QCheckBox('Item 2')
        advancedLayout.addWidget(self.advancedOption1)
        advancedLayout.addWidget(self.advancedOption2)
        self.advancedWidget.setLayout(advancedLayout)
        self.advancedWidget.hide()

        vbox.addWidget(self.cboxEnableExtra)
        vbox.addWidget(self.advancedWidget)
        self.dynamicGroup.setLayout(vbox)
        layout.addWidget(self.dynamicGroup)
    # }

    '''Update selection results'''
    def updateSelection(self):
    # {
        selected = []

        # Base options.
        if self.checkbox1.isChecked():
            selected.append('Item 1')

        if self.checkbox2.isChecked():
            selected.append('Item 2')

        if self.checkbox3.isChecked():
            selected.append('Item 3')

        # Programming language.
        langSelected = []
        if self.langPython.isChecked():
            langSelected.append('Python')

        if self.langJava.isChecked():
            langSelected.append('Java')

        if self.langCpp.isChecked():
            langSelected.append('C++')

        if self.langJS.isChecked():
            langSelected.append('JavaScript')

        if langSelected:
            selected.append('Language: ' + ', '.join(langSelected))

        # Advanced option.
        if self.advancedOption1.isChecked():
            selected.append('Advanced item 1')

        if self.advancedOption2.isChecked():
            selected.append('Advanced item 2')

        self.labelResult.setText('Select: ' + ' | '.join(selected) if selected else 'Select: None')
    # }

    '''Processing tri-state checkbox'''
    def handleTristate(self, state):
    # {
        stateMap = {
            0: 'No Selected',
            1: 'Partially Selected',
            2: 'Fully Selected'
        }

        self.stateLabel.setText(f'Status: {stateMap.get(state, "Unknown")}')
    # }

    '''Toggle display of advanced options'''
    def toggleAdvanced(self, checked):
    # {
        self.advancedWidget.setVisible(checked)
        if not checked:
            self.advancedOption1.setChecked(False)
            self.advancedOption2.setChecked(False)
    # }

    '''Reset all selections'''
    def resetAll(self):
    # {
        # Reset basic options.
        for cb in [self.checkbox1, self.checkbox2, self.checkbox3]:
            cb.setChecked(False)

        # Reset language options.
        for cb in [self.langPython, self.langJava, self.langCpp, self.langJS]:
            cb.setChecked(False)

        # Reset tri-state options.
        self.cBoxTristate.setCheckState(Qt.CheckState.PartiallyChecked)

        # Reset dynamic options.
        self.cboxEnableExtra.setChecked(False)
        self.advancedOption1.setChecked(False)
        self.advancedOption2.setChecked(False)

        self.labelResult.setText('Select: Reset')
    # }
# }

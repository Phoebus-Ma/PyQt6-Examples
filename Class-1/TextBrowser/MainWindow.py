###
# PyQt6 text browser window.
#
# License - MIT.
###

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QTextBrowser
)


class MainWindow(QMainWindow):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'TextBrowser'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        mainLayout = QVBoxLayout()

        # Create QTextBrowser.
        self.text_browser = QTextBrowser()

        # Set HTML content.
        html_content = '''
            <h1 style='color: blue;'>Welcom use QTextBrowser</h1>
            <p>This is a <strong>rich text browser</strong> example</p >
            <ul>
                <li>Support HTML format</li>
                <li>Click<a href=' '>Link</a >test hyperlinks</li>
                <li>Support<a href='#anchor'>Anchor jump</a ></li>
            </ul>
            <p id='anchor' style='color: green;'>This is the anchor location</p >
        '''

        # Set HTML to QTextBrowser.
        self.text_browser.setHtml(html_content)

        # Add normal text to QTextBrowser.
        self.text_browser.append('\nNormal text content:')
        self.text_browser.append('hello world.')

        # Connect signal.
        self.text_browser.anchorClicked.connect(self.on_link_clicked)

        # Set some attribute.
        self.text_browser.setOpenExternalLinks(False)  # Disable auto open link.
        self.text_browser.setLineWrapMode(QTextBrowser.LineWrapMode.WidgetWidth)  # Wrap line.

        mainLayout.addWidget(self.text_browser)

        central_widget = QWidget()
        central_widget.setLayout(mainLayout)
        self.setCentralWidget(central_widget)
    # }

    '''Link click event'''
    def on_link_clicked(self, url: QUrl):
    # {
        if url.toString().startswith('#'):
            # Anchor jump event.
            print(f'Jump anchor: {url.toString()}')
        else:
            # External link (also can use QDesktopServices.openUrl).
            print(f'Clicked external link: {url.toString()}')
    # }
# }

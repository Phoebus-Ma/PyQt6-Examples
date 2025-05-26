###
# PyQt6 editor style.
#
# License - MIT.
###

from PyQt6.QtCore import (
    Qt,
    QSize,
    QRect
)
from PyQt6.QtWidgets import (
    QWidget,
    QPlainTextEdit,
)
from PyQt6.QtGui import (
    QFont,
    QPainter,
    QColor,
)


class LineNumberArea(QWidget):
# {
    def __init__(self, editor):
    # {
        super().__init__(editor)
        self.editor = editor
    # }

    def sizeHint(self):
    # {
        return QSize(self.editor.lineNumberAreaWidth(), 0)
    # }

    def paintEvent(self, event):
    # {
        self.editor.lineNumberAreaPaintEvent(event)
    # }
# }


class CodeEditor(QPlainTextEdit):
# {
    def __init__(self):
    # {
        super().__init__()
        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.updateLineNumberAreaWidth(0)

        self.setFont(QFont("Courier New", 12))
    # }

    def updateLineNumberAreaWidth(self, _):
    # {
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)
    # }

    def lineNumberAreaWidth(self):
    # {
        digits = len(str(max(1, self.blockCount())))
        space = 10 + self.fontMetrics().horizontalAdvance('9') * digits
        return space
    # }

    def updateLineNumberArea(self, rect, dy):
    # {
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(),
                self.lineNumberArea.width(), rect.height())
    # }

    def resizeEvent(self, e):
    # {
        super().resizeEvent(e)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), 
                self.lineNumberAreaWidth(), cr.height()))
    # }

    def lineNumberAreaPaintEvent(self, event):
    # {
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), QColor(240, 240, 240))

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(
                    self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(Qt.GlobalColor.darkGray)
                painter.drawText(0, int(top), self.lineNumberArea.width()-5,
                        self.fontMetrics().height(), Qt.AlignmentFlag.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1
    # }
# }

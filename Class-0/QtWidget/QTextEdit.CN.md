
[English doc](QTextEdit.md)

# class QTextEdit

QTextEdit 类提供了一个用于编辑和显示纯文本和富文本的小部件。


# Synopsis

## Properties

- [acceptRichText](#property-acceptrichtext--bool)

    文本编辑是否接受用户插入富文本。

- [autoFormatting](#property-autoformatting--combination-of-qtexteditautoformattingflag)

    已启用的自动格式化功能集。

- [cursorWidth](#property-cursorwidth--int)

- [document](#property-document--qtextdocument)

    文本编辑器的底层文档。

- [documentTitle](#property-documenttitle--str)

    从文本中解析出的文档的标题。

- [html](#property-html--str)

- [lineWrapColumnOrWidth](#property-linewrapcolumnorwidth--int)

    文本换行的位置（以像素或列为单位，取决于换行模式）。

- [lineWrapMode](#property-linewrapmode--qtexteditlinewrapmode)

    换行模式。

- [markdown](#property-markdown--str)

- [overwriteMode](#property-overwritemode--bool)

    用户输入的文本是否会覆盖现有文本。

- [placeholderText](#property-placeholdertext--str)

    编辑器占位符文本。

- [plainText](#property-plaintext--str)

    文本编辑器的内容为纯文本。

- [readOnly](#property-readonly--bool)

    文本编辑是否是只读的。

- [tabChangesFocus](#property-tabchangesfocus--bool)

    Tab 是否改变焦点或被接受为输入。

- [tabStopDistance](#property-tabstopdistance--float)

    制表位距离（以像素为单位）。

- [textInteractionFlags](#property-textinteractionflags--combination-of-qttextinteractionflag)

- [undoRedoEnabled](#property-undoredoenabled--bool)

    是否启用撤消和重做。


## Methods

- [def \_\_init__()](#initparentnone)

- [def acceptRichText()](#acceptrichtext)

- [def alignment()](#alignment)

- [def anchorAt()](#anchoratpos)

- [def autoFormatting()](#autoformatting)

- [def canPaste()](#canpaste)

- [def createStandardContextMenu()](#createstandardcontextmenu)

- [def currentCharFormat()](#currentcharformat)

- [def currentFont()](#currentfont)

- [def cursorForPosition()](#cursorforpositionpos)

- [def cursorRect()](#cursorrect)

- [def cursorWidth()](#cursorwidth)

- [def document()](#document)

- [def documentTitle()](#documenttitle)

- [def ensureCursorVisible()](#ensurecursorvisible)

- [def extraSelections()](#extraselections)

- [def find()](#findexp-optionsqtextdocumentfindflags)

- [def fontFamily()](#fontfamily)

- [def fontItalic()](#fontitalic)

- [def fontPointSize()](#fontpointsize)

- [def fontUnderline()](#fontunderline)

- [def fontWeight()](#fontweight)

- [def inputMethodQuery()](#inputmethodqueryquery-argument)

- [def isReadOnly()](#isreadonly)

- [def isUndoRedoEnabled()](#isundoredoenabled)

- [def lineWrapColumnOrWidth()](#linewrapcolumnorwidth)

- [def lineWrapMode()](#linewrapmode)

- [def mergeCurrentCharFormat()](#mergecurrentcharformatmodifier)

- [def moveCursor()](#movecursoroperation-modeqtextcursormoveanchor)

- [def overwriteMode()](#overwritemode)

- [def placeholderText()](#placeholdertext)

- [def print_()](#print_printer)

- [def setAcceptRichText()](#setacceptrichtextaccept)

- [def setAutoFormatting()](#setautoformattingfeatures)

- [def setCurrentCharFormat()](#setcurrentcharformatformat)

- [def setCursorWidth()](#setcursorwidthwidth)

- [def setDocument()](#setdocumentdocument)

- [def setDocumentTitle()](#setdocumenttitletitle)

- [def setExtraSelections()](#setextraselectionsselections)

- [def setLineWrapColumnOrWidth()](#setlinewrapcolumnorwidthw)

- [def setLineWrapMode()](#setlinewrapmodemode)

- [def setOverwriteMode()](#setoverwritemodeoverwrite)

- [def setPlaceholderText()](#setplaceholdertextplaceholdertext)

- [def setReadOnly()](#setreadonlyro)

- [def setTabChangesFocus()](#settabchangesfocusb)

- [def setTabStopDistance()](#settabstopdistancedistance)

- [def setTextCursor()](#settextcursorcursor)

- [def setTextInteractionFlags()](#settextinteractionflagsflags)

- [def setUndoRedoEnabled()](#setundoredoenabledenable)

- [def setWordWrapMode()](#setwordwrapmodepolicy)

- [def tabChangesFocus()](#tabchangesfocus)

- [def tabStopDistance()](#tabstopdistance)

- [def textBackgroundColor()](#textbackgroundcolor)

- [def textColor()](#textcolor)

- [def textCursor()](#textcursor)

- [def textInteractionFlags()](#textinteractionflags)

- [def toHtml()](#tohtml)

- [def toMarkdown()](#tomarkdownfeaturesqtextdocumentmarkdowndialectgithub)

- [def toPlainText()](#toplaintext)

- [def wordWrapMode()](#wordwrapmode)

- [def zoomInF()](#zoominfrange)


## Virtual methods

- [def canInsertFromMimeData()](#caninsertfrommimedatasource)

- [def createMimeDataFromSelection()](#createmimedatafromselection)

- [def doSetTextCursor()](#dosettextcursorcursor)

- [def insertFromMimeData()](#insertfrommimedatasource)

- [def loadResource()](#loadresourcetype-name)


## Slots

- [def append()](#appendtext)

- [def clear()](#clear)

- [def copy()](#copy)

- [def cut()](#cut)

- [def insertHtml()](#inserthtmltext)

- [def insertPlainText()](#insertplaintexttext)

- [def paste()](#paste)

- [def redo()](#redo)

- [def scrollToAnchor()](#scrolltoanchorname)

- [def selectAll()](#selectall)

- [def setAlignment()](#setalignmenta)

- [def setCurrentFont()](#setcurrentfontf)

- [def setFontFamily()](#setfontfamilyfontfamily)

- [def setFontItalic()](#setfontitalicb)

- [def setFontPointSize()](#setfontpointsizes)

- [def setFontUnderline()](#setfontunderlineb)

- [def setFontWeight()](#setfontweightw)

- [def setHtml()](#sethtmltext)

- [def setMarkdown()](#setmarkdownmarkdown)

- [def setPlainText()](#setplaintexttext)

- [def setText()](#settextcolorc)

- [def setTextBackgroundColor()](#settextbackgroundcolorc)

- [def setTextColor()](#settextcolorc)

- [def undo()](#undo)

- [def zoomIn()](#zoominrange1)

- [def zoomOut()](#zoomoutrange1)


## Signals

- [def copyAvailable()](#copyavailableb)

- [def currentCharFormatChanged()](#currentcharformatchangedformat)

- [def cursorPositionChanged()](#cursorpositionchanged)

- [def redoAvailable()](#redoavailableb)

- [def selectionChanged()](#selectionchanged)

- [def textChanged()](#textchanged)

- [def undoAvailable()](#undoavailableb)


# Detailed Description

## Introduction and Concepts

QTextEdit 是一个高级所见即所得的查看器/编辑器，支持使用 HTML 样式标签或 Markdown 格式的富文本格式。它经过优化，可以处理大型文档并快速响应用户输入。

QTextEdit 适用于段落和字符。段落是一个格式化的字符串，它会自动换行以适应小部件的宽度。默认情况下，在阅读纯文本时，一个换行符表示一个段落。文档由零个或多个段落组成。段落中的单词根据段落的对齐方式对齐。段落由硬换行符分隔。段落中的每个字符都有自己的属性，例如字体和颜色。

QTextEdit 可以显示图像、列表和表格。如果文本太大而无法在文本编辑的视口中查看，则会出现滚动条。文本编辑可以加载纯文本和富文本文件。富文本可以使用 HTML 4 标记的子集来描述；有关更多信息，请参阅支持的 HTML 子集页面。

如果您只需要显示一小段富文本，请使用 QLabel 。

Qt 中的富文本支持旨在提供一种快速、便携且高效的方式，为应用程序添加合理的在线帮助功能，并为富文本编辑器提供基础。如果您发现 HTML 支持不足以满足您的需求，您可以考虑使用 Qt WebKit，它提供了一个功能齐全的 Web 浏览器小部件。

QTextEdit 上的鼠标光标形状默认为 Qt::IBeamCursor。它可以通过 viewport() 的 cursor 属性进行更改。


## Using QTextEdit as a Display Widget

QTextEdit 可以显示大量 HTML 子集，包括表格和图像。

可以使用 setHtml() 设置或替换文本，该方法会删除任何现有文本并将其替换为 setHtml() 调用中传递的文本。如果您使用旧版 HTML 调用 setHtml()，然后调用 toHtml()，则返回的文本可能具有不同的标记，但会呈现相同的内容。可以使用 clear() 删除整个文本。

还可以使用 setMarkdown() 设置或替换文本，并且适用相同的注意事项：如果您随后调用 toMarkdown()，则返回的文本可能不同，但含义会尽可能保留。可以解析带有一些嵌入 HTML 的 Markdown，其限制与 setHtml() 相同；但 toMarkdown() 仅写入“纯”Markdown，没有任何嵌入的 HTML。

可以使用 QTextCursor 类或使用便捷函数 insertHtml() 、 insertPlainText() 、 append() 或 paste() 插入文本本身。 QTextCursor 还能够将表格或列表等复杂对象插入文档，并处理创建选择并将更改应用于选定文本。

默认情况下，文本编辑会在空白处换行以适合文本编辑小部件。setLineWrapMode() 函数用于指定所需的换行类型，如果您不想要任何换行，则使用 NoWrap。调用 setLineWrapMode() 以设置固定像素宽度 FixedPixelWidth 或字符列（例如 80 列） FixedColumnWidth，并使用 setLineWrapColumnOrWidth() 指定的像素或列。如果您对小部件的宽度 WidgetWidth 使用自动换行，则可以使用 setWordWrapMode() 指定是在空白处还是在任何地方换行。

find() 函数可用于在文本中查找和选择给定的字符串。

如果您想限制 QTextEdit 中的段落总数，例如它在日志查看器中经常有用，那么您可以使用 QTextDocument 的 maximumBlockCount 属性来实现。


## Read-only Key Bindings

当 QTextEdit 以只读方式使用时，键绑定仅限于导航，并且只能使用鼠标选择文本：

| Keypresses | Action                               |
| ---------- | ------------------------------------ |
| Up         | 向上移动一行。                        |
| Down       | 向下移动一行。                        |
| Left       | 向左移动一个字符。                    |
| Right      | 向右移动一个字符。                    |
| PageUp     | 向上移动一页（视口）。                 |
| PageDown   | 向下移动一页（视口）。                 |
| Home       | 移至文本开头。                        |
| End        | 移至文本末尾。                        |
| Alt+Wheel  | 水平滚动页面（滚轮是鼠标滚轮）。        |
| Ctrl+Wheel | 缩放文本。                            |
| Ctrl+A     | 选择所有文本。                        |

文本编辑可能能够提供一些元信息。例如，documentTitle() 函数将返回 HTML <title> 标签内的文本。


## Using QTextEdit as an Editor

有关使用 QTextEdit 作为显示小部件的所有信息也适用于此处。

当前字符格式的属性使用 setFontItalic() 、 setFontWeight() 、 setFontUnderline() 、 setFontFamily() 、 setFontPointSize() 、 setTextColor() 和 setCurrentFont() 设置。当前段落的对齐方式使用 setAlignment() 设置。

文本选择由 QTextCursor 类处理，该类提供创建选择、检索文本内容或删除选择的功能。您可以使用 textCursor() 方法检索与用户可见光标相对应的对象。如果您想在 QTextEdit 中设置选择，只需在 QTextCursor 对象上创建一个，然后使用 setTextCursor() 使该光标成为可见光标。可以使用 copy() 将选择复制到剪贴板，或使用 cut() 剪切到剪贴板。可以使用 selectAll() 选择整个文本。

当光标移动并且底层格式属性发生变化时，将发出 currentCharFormatChanged() 信号以反映新光标位置的新属性。

每当文本发生变化时（作为 setText() 的结果或通过编辑器本身），都会发出 textChanged() 信号。

QTextEdit 包含一个 QTextDocument 对象，可以使用 document() 方法检索该对象。您还可以使用 setDocument() 设置自己的文档对象。

QTextDocument 提供了一个 isModified() 函数，如果文本自加载以来或自上次使用 false 作为参数调用 setModified 以来已被修改，则该函数将返回 true。此外，它还提供了撤消和重做的方法。


## Drag and Drop

QTextEdit 还支持自定义拖放行为。默认情况下，当用户将这些 MIME 类型的数据拖放到文档上时，QTextEdit 将插入纯文本、HTML 和富文本。重新实现 canInsertFromMimeData() 和 insertFromMimeData() 以添加对其他 MIME 类型的支持。

例如，要允许用户将图像拖放到 QTextEdit 上，您可以按以下方式实现这些函数：

```python
def canInsertFromMimeData(self, QMimeData source ):

    if source.hasImage():
        return True
else:
        return QTextEdit.canInsertFromMimeData(source)
```

我们通过返回 true 来添加对图像 MIME 类型的支持。对于所有其他 MIME 类型，我们使用默认实现。

```bash
def insertFromMimeData(self, source):

    if source.hasImage():

        image = QImage(source.imageData())
        cursor = self.textCursor()
        document = self.document()
        document.addResource(QTextDocument.ImageResource, QUrl("image"), image)
        cursor.insertImage("image")
```

我们从 MIME 源持有的 QVariant 中解压图像并将其作为资源插入到文档中。


## Editing Key Bindings

为编辑而实现的键绑定列表：

| Keypresses   | Action                         |
| ------------ | ------------------------------ |
| Backspace    | 删除光标左边的字符。             |
| Delete       | 删除光标右侧的字符。             |
| Ctrl+C       | 将选定的文本复制到剪贴板。        |
| Ctrl+Insert  | 将选定的文本复制到剪贴板。        |
| Ctrl+K       | 删除至行末。                     |
| Ctrl+V       | 将剪贴板文本粘贴到文本编辑中。     |
| Shift+Insert | 将剪贴板文本粘贴到文本编辑中。     |
| Ctrl+X       | 删除选定的文本并将其复制到剪贴板。 |
| Shift+Delete | 删除选定的文本并将其复制到剪贴板。 |
| Ctrl+Z       | 撤消上一个操作。                 |
| Ctrl+Y       | 重做上一个操作。                 |
| Left         | 将光标向左移动一个字符。          |
| Ctrl+Left    | 将光标向左移动一个单词。          |
| Right        | 将光标向右移动一个字符。          |
| Ctrl+Right   | 将光标向右移动一个单词。          |
| Up           | 将光标向上移动一行。              |
| Down         | 将光标向下移动一行。              |
| PageUp       | 将光标向上移动一页。              |
| PageDown     | 将光标向下移动一页。              |
| Home         | 将光标移至行首。                  |
| Ctrl+Home    | 将光标移动到文本的开头。          |
| End          | 将光标移动到行尾。                |
| Ctrl+End     | 将光标移动到文本末尾。            |
| Alt+Wheel    | 水平滚动页面（滚轮是鼠标滚轮）。   |

要选择（标记）文本，请按住 Shift 键并按下某个移动键，例如，Shift+Right 将选择右侧的字符，Shift+Ctrl+Right 将选择右侧的单词，等等。


--------------------------------
## class LineWrapMode

| Constant                   | Description |
| -------------------------- | ----------- |
| QTextEdit.NoWrap           |             |
| QTextEdit.WidgetWidth      |             |
| QTextEdit.FixedPixelWidth  |             |
| QTextEdit.FixedColumnWidth |             |


--------------------------------
## class AutoFormattingFlag

| Constant                 | Description |
| ------------------------ | ----------- |
| QTextEdit.AutoNone       | （继承 enum.Flag）不进行任何自动格式化。 |
| QTextEdit.AutoBulletList | 自动创建项目符号列表，例如当用户在最左边的列中输入星号（“*”）或在现有列表项中按下 Enter 键时。 |
| QTextEdit.AutoAll        | 应用所有自动格式。目前仅支持自动项目符号列表。 |


--------------------------------
## property acceptRichText : bool

此属性保存文本编辑是否接受用户的富文本插入。

当此属性设置为 false 时，文本编辑将仅接受用户的纯文本输入。例如通过剪贴板或拖放。

此属性的默认值为 true。

访问函数：

- acceptRichText()
- setAcceptRichText()


--------------------------------
## property autoFormatting : Combination of QTextEdit.AutoFormattingFlag

此属性保存已启用的自动格式化功能集。

该值可以是 AutoFormattingFlag 枚举中的值的任意组合。默认值为 AutoNone 。选择 AutoAll 可启用所有自动格式化。

目前，提供的唯一自动格式化功能是 AutoBulletList ；Qt 的未来版本可能会提供更多功能。

访问函数：

- autoFormatting()
- setAutoFormatting()


--------------------------------
## property cursorWidth : int

此属性指定光标的宽度（以像素为单位）。默认值为 1。

访问函数：

- cursorWidth()
- setCursorWidth()


--------------------------------
## property document : QTextDocument

此属性保存文本编辑器的底层文档。

访问函数：

- document()
- setDocument()


--------------------------------
## property documentTitle : str

此属性保存从文本解析出的文档的标题。

默认情况下，对于新创建的空文档，此属性包含一个空字符串。

访问函数：

- documentTitle()
- setDocumentTitle()


--------------------------------
## property html : str

此属性为文本编辑的文本提供 HTML 界面。

toHtml() 将文本编辑的文本作为 html 返回。

setHtml() 更改文本编辑的文本。任何先前的文本都将被删除，撤消/重做历史记录将被清除。输入文本将被解释为 html 格式的富文本。除非 textCursor() 已位于文档开头，否则 currentCharFormat() 也会被重置。

默认情况下，对于新创建的空文档，此属性包含用于描述没有正文的 HTML 4.0 文档的文本。

访问函数：

- toHtml()
- setHtml()
- Signal textChanged()


--------------------------------
## property lineWrapColumnOrWidth : int

此属性保存文本换行的位置（以像素或列为单位，具体取决于换行模式）。

如果换行模式为 FixedPixelWidth ，则该值是从文本编辑左边缘开始的文本应换行的像素数。 如果换行模式为 FixedColumnWidth ，则该值是从文本编辑左边缘开始的文本应换行的列数（以字符列为单位）。

默认情况下，此属性包含 0 值。

访问函数：

- lineWrapColumnOrWidth()
- setLineWrapColumnOrWidth()


--------------------------------
## property lineWrapMode : QTextEdit.LineWrapMode

此属性保存换行模式。

默认模式为 WidgetWidth，这会导致单词在文本编辑的右边缘换行。换行发生在空白处，保持整个单词完整。如果您希望在单词内换行，请使用 setWordWrapMode() 。如果您设置了 FixedPixelWidth 或 FixedColumnWidth 的换行模式，您还应该使用所需的宽度调用 setLineWrapColumnOrWidth()。

访问函数：

- lineWrapMode()
- setLineWrapMode()


--------------------------------
## property markdown : str

此属性为文本编辑的文本提供 Markdown 接口。

toMarkdown() 将文本编辑的文本作为“纯”Markdown 返回，不包含任何嵌入的 HTML 格式。QTextDocument 支持的某些功能（例如使用特定颜色和命名字体）无法在“纯”Markdown 中表达，因此将被省略。

setMarkdown() 更改文本编辑的文本。任何先前的文本都将被删除，撤消/重做历史记录将被清除。输入文本被解释为 Markdown 格式的富文本。

markdown 字符串中包含的 HTML 的解析方式与 setHtml 相同；但是，不支持 HTML 块内的 Markdown 格式。

可以通过 features 参数启用或禁用解析器的某些功能：

- MarkdownNoHTML
- Any HTML tags in the Markdown text will be discarded

默认是MarkdownDialectGitHub。

访问函数：

- toMarkdown()
- setMarkdown()
- Signal textChanged()


--------------------------------
## property overwriteMode : bool

此属性用于控制用户输入的文本是否会覆盖现有文本。

与许多文本编辑器一样，文本编辑器小部件可以配置为插入或用用户输入的新文本覆盖现有文本。

如果此属性为 true，则现有文本将被新文本逐个字符地覆盖；否则，文本将插入到光标位置，取代现有文本。

默认情况下，此属性为 false（新文本不会覆盖现有文本）。

访问函数：

- overwriteMode()
- setOverwriteMode()


--------------------------------
## property placeholderText : str

此属性保存编辑器占位符文本。

设置此属性会使编辑器在 document() 为空时显示灰色占位符文本。

默认情况下，此属性包含一个空字符串。

访问函数：

- placeholderText()
- setPlaceholderText()


--------------------------------
## property plainText : str

此属性将文本编辑器的内容保存为纯文本。

设置此属性后，将删除先前的内容并重置撤消/重做历史记录。除非 textCursor() 已位于文档开头，否则 currentCharFormat() 也会重置。

如果文本编辑具有其他内容类型，则调用 toPlainText() 时不会将其替换为纯文本。唯一的例外是非中断空格，nbsp;，它将转换为标准空格。

默认情况下，对于没有内容的编辑器，此属性包含一个空字符串。

访问函数：

- toPlainText()
- setPlainText()


--------------------------------
## property readOnly : bool

此属性保存文本编辑是否为只读。

在只读文本编辑中，用户只能浏览文本并选择文本；无法修改文本。

此属性的默认值为 false。

访问函数：

- isReadOnly()
- setReadOnly()


--------------------------------
## property tabChangesFocus : bool

此属性保存 Tab 键是否改变焦点或被接受为输入。
​​
在某些情况下，文本编辑不应允许用户使用 Tab 键输入制表符或更改缩进，因为这会破坏焦点链。默认值为 false。

访问函数：

- tabChangesFocus()
- setTabChangesFocus()


--------------------------------
## property tabStopDistance : float

此属性保存制表位距离（以像素为单位）。

默认情况下，此属性包含 80 像素的值。

请勿设置小于 QChar::VisualTabCharacter 字符的 Horizo​​ntalAdvance() 的值，否则制表符将绘制不完整。

访问函数：

- tabStopDistance()
- setTabStopDistance()


--------------------------------
## property textInteractionFlags : Combination of Qt.TextInteractionFlag

指定小部件应如何与用户输入交互。

默认值取决于 QTextEdit 是只读的还是可编辑的，以及它是否是 QTextBrowser。

访问函数：

- textInteractionFlags()
- setTextInteractionFlags()


--------------------------------
## property undoRedoEnabled : bool

此属性保存是否启用了撤消和重做。

仅当此属性为真，并且存在可以撤消（或重做）的操作时，用户才可以撤消或重做操作。

访问函数：

- isUndoRedoEnabled()
- setUndoRedoEnabled()


--------------------------------
## __init__(text[, parent=None])

参数：

- text – str
- parent – QWidget

构造一个具有父级parent的QTextEdit。文本编辑将显示文本text。文本被解释为html。


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

构造一个具有父级parent的空的QTextEdit。


--------------------------------
## acceptRichText()

返回值：bool

属性 acceptRichText 的获取器。


--------------------------------
## alignment()

返回值：Combination of AlignmentFlag

返回当前段落的对齐方式。


--------------------------------
## anchorAt(pos)

参数：

- pos – QPoint

返回值：str

返回位置 pos 处锚点的引用，如果该点不存在锚点，则返回空字符串。


--------------------------------
## append(text)

参数：

- text – str

将包含文本的新段落附加到文本编辑的末尾。


--------------------------------
## autoFormatting()

返回值：Combination of AutoFormattingFlag

属性 autoFormatting 的获取器。


--------------------------------
## canInsertFromMimeData(source)

参数：

- source – QMimeData

返回值：bool

如果源指定的 MIME 数据对象的内容可以解码并插入文档，则此函数返回 true。例如，在拖动操作期间鼠标进入此小部件时，会调用此函数，并且需要确定是否可以接受拖放操作。

重新实现此函数以启用对其他 MIME 类型的拖放支持。


--------------------------------
## canPaste()

返回值：bool

返回是否可以将文本从剪贴板粘贴到文本编辑中。


--------------------------------
## clear()

删除文本编辑中的所有文本。


--------------------------------
## copy()

将任何选定的文本复制到剪贴板。


--------------------------------
## copyAvailable(b)

参数：

- b – bool

当在文本编辑中选择或取消选择文本时，将发出此信号。

当选择文本时，将发出此信号，并将 yes 设置为 true。 如果未选择任何文本或取消选择所选文本，则将发出此信号，并将 yes 设置为 false。

如果 yes 为 true，则可以使用 copy() 将所选内容复制到剪贴板。 如果 yes 为 false，则 copy() 不执行任何操作。


--------------------------------
## createMimeDataFromSelection()

返回值：QMimeData

此函数返回一个新的 MIME 数据对象，以表示文本编辑的当前选择的内容。当需要将选择封装到新的 QMimeData 对象中时，会调用此函数；例如，当启动拖放操作时，或者当将数据复制到剪贴板时。

如果您重新实现此函数，请注意，返回的 QMimeData 对象的所有权将传递给调用者。可以使用 textCursor() 函数检索选择。


--------------------------------
## createStandardContextMenu()

返回值：QMenu

此函数创建标准上下文菜单，当用户用鼠标右键单击文本编辑时，将显示该菜单。它从默认 contextMenuEvent() 处理程序调用。弹出菜单的所有权将转移给调用者。

我们建议您改用 createStandardContextMenu(QPoint) 版本，它将启用对用户单击位置敏感的操作。


--------------------------------
## createStandardContextMenu(position)

参数：

- position – QPoint

返回值：QMenu

此函数创建标准上下文菜单，当用户用鼠标右键单击文本编辑时，将显示该菜单。它由默认的 contextMenuEvent() 处理程序调用，并获取鼠标单击在文档坐标中的位置。这可以启用对用户单击位置敏感的操作。弹出菜单的所有权将转移给调用者。


--------------------------------
## currentCharFormat()

返回值：QTextCharFormat

返回插入新文本时使用的字符格式。


--------------------------------
## currentCharFormatChanged(format)

参数：

- format – QTextCharFormat

如果当前字符格式发生变化（例如由于光标位置发生变化），则会发出此信号。

新格式为 f。


--------------------------------
## currentFont()

返回值：QFont

返回当前格式的字体。


--------------------------------
## cursorForPosition(pos)

参数：

- pos – QPoint

返回值：QTextCursor

返回位于位置 pos（在视口坐标中）的 QTextCursor。


--------------------------------
## cursorPositionChanged()

只要光标位置改变就会发出此信号。


--------------------------------
## cursorRect()

返回值：QRect

返回一个包含文本编辑光标的矩形（在视口坐标中）。


--------------------------------
## cursorRect(cursor)

参数：

- cursor – QTextCursor

返回值：QRect

返回一个包含光标的矩形（在视口坐标中）。


--------------------------------
## cursorWidth()

返回值：int

属性 cursorWidth 的获取器。


--------------------------------
## cut()

将选定的文本复制到剪贴板并从文本编辑中删除。

如果没有选定的文本，则不会发生任何事情。


--------------------------------
## doSetTextCursor(cursor)

参数：

- cursor – QTextCursor


--------------------------------
## document()

返回值：QTextDocument

属性文档的获取器。


--------------------------------
## documentTitle()

返回值：str

属性 documentTitle 的获取器。


--------------------------------
## ensureCursorVisible()

如有必要，通过滚动文本编辑来确保光标可见。


--------------------------------
## extraSelections()

返回值：list of QTextEdit.ExtraSelection

返回先前设置的额外选择。


--------------------------------
## find(exp[, options=QTextDocument.FindFlags()])

参数：

- exp – QRegularExpression
- options – Combination of FindFlag

返回值：bool

这是一个重载函数。

使用给定的选项查找下一个与正则表达式 exp 匹配的出现情况。

如果找到匹配项，则返回 true 并更改光标以选择匹配项；否则返回 false。


--------------------------------
## find(exp[, options=QTextDocument.FindFlags()])

参数：

- exp – str
- options – Combination of FindFlag

返回值：bool

使用给定的选项查找字符串 exp 的下一个出现位置。如果找到 exp，则返回 true，并更改光标以选择匹配项；否则返回 false。


--------------------------------
## fontFamily()

返回值：str

返回当前格式的字体系列。


--------------------------------
## fontItalic()

返回值：bool

如果当前格式的字体为斜体，则返回 true；否则返回 false。


--------------------------------
## fontPointSize()

返回值：float

返回当前格式的字体的点大小。


--------------------------------
## fontUnderline()

返回值：bool

如果当前格式的字体带下划线则返回 true，否则返回 false。


--------------------------------
## fontWeight()

返回值：int

返回当前格式的字体粗细。


--------------------------------
## inputMethodQuery(query, argument)

参数：

- query – InputMethodQuery
- argument – object

返回值：object


--------------------------------
## insertFromMimeData(source)

参数：

- source – QMimeData

此函数将源指定的 MIME 数据对象的内容插入到当前光标位置的文本编辑中。每当文本作为剪贴板粘贴操作的结果插入时，或者当文本编辑接受来自拖放操作的数据时，都会调用此函数。

重新实现此函数以启用对其他 MIME 类型的拖放支持。


--------------------------------
## insertHtml(text)

参数：

- text – str

便利槽，用于在当前光标位置插入假定为 html 格式的文本。

它相当于：

```python
edit.textCursor().insertHtml(fragment)
```


--------------------------------
## insertPlainText(text)

参数：

- text – str

在当前光标位置插入文本的便利插槽。

相当于：

```python
edit.textCursor().insertText(text)
```


--------------------------------
## isReadOnly()

返回值：bool

属性 readOnly 的获取器。


--------------------------------
## isUndoRedoEnabled()

返回值：bool

属性 undoRedoEnabled 的获取器。


--------------------------------
## lineWrapColumnOrWidth()

返回值：int

属性 lineWrapColumnOrWidth 的获取器。


--------------------------------
## lineWrapMode()

返回值：LineWrapMode

属性 lineWrapMode 的获取器。


--------------------------------
## loadResource(type, name)

参数：

- type – int
- name – QUrl

返回值：object

加载给定类型和名称指定的资源。

此函数是 QTextDocument::loadResource() 的扩展。


--------------------------------
## mergeCurrentCharFormat(modifier)

参数：

- modifier – QTextCharFormat

通过在编辑器光标上调用 QTextCursor::mergeCharFormat 将 modifier 中指定的属性合并到当前字符格式中。如果编辑器有选择，则 modifier 的属性将直接应用于选择。


--------------------------------
## moveCursor(operation[, mode=QTextCursor.MoveAnchor])

参数：

- operation – MoveOperation
- mode – MoveMode

通过执行给定的操作来移动光标。

如果模式为 QTextCursor::KeepAnchor，则光标会选择它移动到的文本。这与用户按住 Shift 键并使用光标键移动光标时实现的效果相同。


--------------------------------
## overwriteMode()

返回值：bool

属性 overwriteMode 的获取器。


--------------------------------
## paste()

将剪贴板中的文本粘贴到当前光标位置的文本编辑中。

如果剪贴板中没有文本，则不会发生任何事情。

要更改此函数的行为，即修改 QTextEdit 可以粘贴的内容及其粘贴方式，请重新实现虚拟 canInsertFromMimeData() 和 insertFromMimeData() 函数。


--------------------------------
## placeholderText()

返回值：str

属性 placeholderText 的获取方法。


--------------------------------
## print_(printer)

参数：

- printer – QPagedPaintDevice


--------------------------------
## redo()

重做上一个操作。

如果没有要重做的操作，即撤消/重做历史记录中没有重做步骤，则不会发生任何事情。


--------------------------------
## redoAvailable(b)

参数：

- b – bool

每当重做操作可用（可用为真）或不可用（可用为假）时，就会发出此信号。


--------------------------------
## scrollToAnchor(name)

参数：

- name – str

滚动文本编辑，以便具有给定名称的锚点可见；如果名称为空、已经可见或者未找到，则不执行任何操作。


--------------------------------
## selectAll()

选择所有文本。


--------------------------------
## selectionChanged()

每当选择改变时就会发射此信号。


--------------------------------
## setAcceptRichText(accept)

参数：

- accept – bool

属性 acceptRichText 的设置方法。


--------------------------------
## setAlignment(a)

参数：

- a – Combination of AlignmentFlag

将当前段落的对齐方式设置为 a。有效的对齐方式是 Qt::AlignLeft、Qt::AlignRight、Qt::AlignJustify 和 Qt::AlignCenter（水平居中）。


--------------------------------
## setAutoFormatting(features)

参数：

- features – Combination of AutoFormattingFlag

属性 autoFormatting 的设置器。


--------------------------------
## setCurrentCharFormat(format)

参数：

- format – QTextCharFormat

通过在编辑器光标上调用 QTextCursor::setCharFormat() 来设置插入新文本时使用的字符格式。如果编辑器有选择，则字符格式将直接应用于选择。


--------------------------------
## setCurrentFont(f)

参数：

- f – QFont

将当前格式的字体设置为f。


--------------------------------
## setCursorWidth(width)

参数：

- width – int

属性 cursorWidth 的设置器。


--------------------------------
## setDocument(document)

参数：

- document – QTextDocument

财产文件的设定者。


--------------------------------
## setDocumentTitle(title)

参数：

- title – str

属性 documentTitle 的设置者。


--------------------------------
## setExtraSelections(selections)

参数：

- selections – .list of QTextEdit.ExtraSelection

此功能允许暂时用指定颜色标记文档中的某些区域（指定为选择）。这在编程编辑器中很有用，例如，用给定的背景颜色标记整行文本以指示断点的存在。


--------------------------------
## setFontFamily(fontFamily)

参数：

- fontFamily – str

将当前格式的字体系列设置为 fontFamily。


--------------------------------
## setFontItalic(b)

参数：

- b – bool

如果 italic 为真，则将当前格式设置为斜体；否则将当前格式设置为非斜体。


--------------------------------
## setFontPointSize(s)

参数：

- s – float

将当前格式的点大小设置为 s。

请注意，如果 s 为零或负数，则此函数的行为未定义。


--------------------------------
## setFontUnderline(b)

参数：

- b – bool

如果下划线为真，则将当前格式设置为下划线；否则将当前格式设置为非下划线。


--------------------------------
## setFontWeight(w)

参数：

- w – int

将当前格式的字体粗细设置为给定的粗细，其中使用的值在 QFont::Weight 枚举定义的范围内。


--------------------------------
## setHtml(text)

参数：

- text – str

属性 html 的设置器。


--------------------------------
## setLineWrapColumnOrWidth(w)

参数：

- w – int

属性 lineWrapColumnOrWidth 的设置器。


--------------------------------
## setLineWrapMode(mode)

参数：

- mode – LineWrapMode

属性 lineWrapMode 的设置器。


--------------------------------
## setMarkdown(markdown)

参数：

- markdown – str

属性 markdown 的设置者。


--------------------------------
## setOverwriteMode(overwrite)

参数：

- overwrite – bool

属性 overwriteMode 的设置者。


--------------------------------
## setPlaceholderText(placeholderText)

参数：

- placeholderText – str

属性 placeholderText 的设置者。


--------------------------------
## setPlainText(text)

参数：

- text – str

将文本编辑的文本更改为字符串文本。任何先前的文本都将被删除。

属性 plainText 的设置器。


--------------------------------
## setReadOnly(ro)

参数：

- ro – bool

属性 readOnly 的设置者。


--------------------------------
## setTabChangesFocus(b)

参数：

- b – bool

属性 tabChangesFocus 的设置者。


--------------------------------
## setTabStopDistance(distance)

参数：

- distance – float

属性 tabStopDistance 的设置者。


--------------------------------
setText(text)

参数：

- text – str

设置文本编辑的文本。文本可以是纯文本或 HTML，文本编辑将尝试猜测正确的格式。

直接使用 setHtml() 或 setPlainText() 可避免文本编辑的猜测。


--------------------------------
## setTextBackgroundColor(c)

参数：

- c – QColor

将当前格式的文本背景颜色设置为 c。


--------------------------------
## setTextColor(c)

参数：

- c – QColor

将当前格式的文本颜色设置为 c。


--------------------------------
## setTextCursor(cursor)

参数：

- cursor – QTextCursor

设置可见光标。


--------------------------------
## setTextInteractionFlags(flags)

参数：

- flags – Combination of TextInteractionFlag

属性 textInteractionFlags 的设置者。


--------------------------------
## setUndoRedoEnabled(enable)

参数：

- enable – bool

属性 undoRedoEnabled 的设置者。


--------------------------------
## setWordWrapMode(policy)

参数：

- policy – WrapMode


--------------------------------
## tabChangesFocus()

返回值：bool

属性 tabChangesFocus 的获取器。


--------------------------------
## tabStopDistance()

返回值：float

属性 tabStopDistance 的获取器。


--------------------------------
## textBackgroundColor()

返回值：QColor

返回当前格式的文本背景颜色。


--------------------------------
## textChanged()

每当文档内容发生变化时，都会发出此信号；例如，插入或删除文本时，或者应用格式时。

属性 markdown 的通知信号。


--------------------------------
## textColor()

返回值：QColor

返回当前格式的文本颜色。


--------------------------------
## textCursor()

Return type: QTextCursor

返回代表当前可见光标的 QTextCursor 的副本。请注意，返回光标上的更改不会影响 QTextEdit 的光标；使用 setTextCursor() 来更新可见光标。


--------------------------------
## textInteractionFlags()

返回值：Combination of TextInteractionFlag

属性 textInteractionFlags 的获取器。


--------------------------------
## toHtml()

返回值：str

Getter of property html  .


--------------------------------
## toMarkdown([features=QTextDocument.MarkdownDialectGitHub])

参数：

- features – Combination of MarkdownFeature

返回值：str


--------------------------------
## toPlainText()

返回值：str


--------------------------------
## QString QTextEdit::toPlainText() const

将文本编辑的文本作为纯文本返回。

属性 plainText 的获取器。


--------------------------------
## undo()

撤消上一个操作。

如果没有要撤消的操作，即撤消/重做历史记录中没有撤消步骤，则不会发生任何事情。


--------------------------------
## undoAvailable(b)

参数：

- b – bool

每当撤消操作可用（可用为真）或不可用（可用为假）时就会发射此信号。


--------------------------------
## wordWrapMode()

返回值：WrapMode


--------------------------------
## zoomIn([range=1])

参数：

- range – int

通过使基本字体大小范围点变大并重新计算所有字体大小为新大小来放大文本。这不会改变任何图像的大小。


--------------------------------
## zoomInF(range)

参数：

- range – float


--------------------------------
## zoomOut([range=1])

参数：

- range – int

通过缩小基本字体大小范围点并重新计算所有字体大小为新大小来缩小文本。这不会改变任何图像的大小。


[Chinese doc](QTextEdit.CN.md)

# class QTextEdit

The QTextEdit class provides a widget that is used to edit and display both plain and rich text.


# Synopsis

## Properties

- [acceptRichText](#property-acceptrichtext--bool)

    Whether the text edit accepts rich text insertions by the user

- [autoFormatting](#property-autoformatting--combination-of-qtexteditautoformattingflag)

    The enabled set of auto formatting features

- [cursorWidth](#property-cursorwidth--int)

- [document](#property-document--qtextdocument)

    The underlying document of the text editor

- [documentTitle](#property-documenttitle--str)

    The title of the document parsed from the text

- [html](#property-html--str)

- [lineWrapColumnOrWidth](#property-linewrapcolumnorwidth--int)

    The position (in pixels or columns depending on the wrap mode) where text will be wrapped

- [lineWrapMode](#property-linewrapmode--qtexteditlinewrapmode)

    The line wrap mode

- [markdown](#property-markdown--str)

- [overwriteMode](#property-overwritemode--bool)

    Whether text entered by the user will overwrite existing text

- [placeholderText](#property-placeholdertext--str)

    The editor placeholder text

- [plainText](#property-plaintext--str)

    The text editor’s contents as plain text

- [readOnly](#property-readonly--bool)

    Whether the text edit is read-only

- [tabChangesFocus](#property-tabchangesfocus--bool)

    Whether Tab changes focus or is accepted as input

- [tabStopDistance](#property-tabstopdistance--float)

    The tab stop distance in pixels

- [textInteractionFlags](#property-textinteractionflags--combination-of-qttextinteractionflag)

- [undoRedoEnabled](#property-undoredoenabled--bool)

    Whether undo and redo are enabled


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

QTextEdit is an advanced WYSIWYG viewer/editor supporting rich text formatting using HTML-style tags, or Markdown format. It is optimized to handle large documents and to respond quickly to user input.

QTextEdit works on paragraphs and characters. A paragraph is a formatted string which is word-wrapped to fit into the width of the widget. By default when reading plain text, one newline signifies a paragraph. A document consists of zero or more paragraphs. The words in the paragraph are aligned in accordance with the paragraph’s alignment. Paragraphs are separated by hard line breaks. Each character within a paragraph has its own attributes, for example, font and color.

QTextEdit can display images, lists and tables. If the text is too large to view within the text edit’s viewport, scroll bars will appear. The text edit can load both plain text and rich text files. Rich text can be described using a subset of HTML 4 markup; refer to the Supported HTML Subset page for more information.

If you just need to display a small piece of rich text use QLabel .

The rich text support in Qt is designed to provide a fast, portable and efficient way to add reasonable online help facilities to applications, and to provide a basis for rich text editors. If you find the HTML support insufficient for your needs you may consider the use of Qt WebKit, which provides a full-featured web browser widget.

The shape of the mouse cursor on a QTextEdit is Qt::IBeamCursor by default. It can be changed through the viewport() ‘s cursor property.


## Using QTextEdit as a Display Widget

QTextEdit can display a large HTML subset, including tables and images.

The text can be set or replaced using setHtml() which deletes any existing text and replaces it with the text passed in the setHtml() call. If you call setHtml() with legacy HTML, and then call toHtml() , the text that is returned may have different markup, but will render the same. The entire text can be deleted with clear() .

Text can also be set or replaced using setMarkdown() , and the same caveats apply: if you then call toMarkdown() , the text that is returned may be different, but the meaning is preserved as much as possible. Markdown with some embedded HTML can be parsed, with the same limitations that setHtml() has; but toMarkdown() only writes “pure” Markdown, without any embedded HTML.

Text itself can be inserted using the QTextCursor class or using the convenience functions insertHtml() , insertPlainText() , append() or paste() . QTextCursor is also able to insert complex objects like tables or lists into the document, and it deals with creating selections and applying changes to selected text.

By default the text edit wraps words at whitespace to fit within the text edit widget. The setLineWrapMode() function is used to specify the kind of line wrap you want, or NoWrap if you don’t want any wrapping. Call setLineWrapMode() to set a fixed pixel width FixedPixelWidth , or character column (e.g. 80 column) FixedColumnWidth with the pixels or columns specified with setLineWrapColumnOrWidth() . If you use word wrap to the widget’s width WidgetWidth , you can specify whether to break on whitespace or anywhere with setWordWrapMode() .

The find() function can be used to find and select a given string within the text.

If you want to limit the total number of paragraphs in a QTextEdit , as for example it is often useful in a log viewer, then you can use QTextDocument’s maximumBlockCount property for that.


## Read-only Key Bindings

When QTextEdit is used read-only the key bindings are limited to navigation, and text may only be selected with the mouse:

| Keypresses | Action                               |
| ---------- | ------------------------------------ |
| Up         | Moves one line up.                   |
| Down       | Moves one line down.                 |
| Left       | Moves one character to the left.     |
| Right      | Moves one character to the right.    |
| PageUp     | Moves one (viewport) page up.        |
| PageDown   | Moves one (viewport) page down.      |
| Home       | Moves to the beginning of the text.  |
| End        | Moves to the end of the text.        |
| Alt+Wheel  | Scrolls the page horizontally (the Wheel is the mouse wheel). |
| Ctrl+Wheel | Zooms the text.                      |
| Ctrl+A     | Selects all text.                    |

The text edit may be able to provide some meta-information. For example, the documentTitle() function will return the text from within HTML <title> tags.


## Using QTextEdit as an Editor

All the information about using QTextEdit as a display widget also applies here.

The current char format’s attributes are set with setFontItalic() , setFontWeight() , setFontUnderline() , setFontFamily() , setFontPointSize() , setTextColor() and setCurrentFont() . The current paragraph’s alignment is set with setAlignment() .

Selection of text is handled by the QTextCursor class, which provides functionality for creating selections, retrieving the text contents or deleting selections. You can retrieve the object that corresponds with the user-visible cursor using the textCursor() method. If you want to set a selection in QTextEdit just create one on a QTextCursor object and then make that cursor the visible cursor using setTextCursor() . The selection can be copied to the clipboard with copy() , or cut to the clipboard with cut() . The entire text can be selected using selectAll() .

When the cursor is moved and the underlying formatting attributes change, the currentCharFormatChanged() signal is emitted to reflect the new attributes at the new cursor position.

The textChanged() signal is emitted whenever the text changes (as a result of setText() or through the editor itself).

QTextEdit holds a QTextDocument object which can be retrieved using the document() method. You can also set your own document object using setDocument() .

QTextDocument provides an isModified() function which will return true if the text has been modified since it was either loaded or since the last call to setModified with false as argument. In addition it provides methods for undo and redo.


## Drag and Drop

QTextEdit also supports custom drag and drop behavior. By default, QTextEdit will insert plain text, HTML and rich text when the user drops data of these MIME types onto a document. Reimplement canInsertFromMimeData() and insertFromMimeData() to add support for additional MIME types.

For example, to allow the user to drag and drop an image onto a QTextEdit , you could the implement these functions in the following way:

```python
def canInsertFromMimeData(self, QMimeData source ):

    if source.hasImage():
        return True
else:
        return QTextEdit.canInsertFromMimeData(source)
```

We add support for image MIME types by returning true. For all other MIME types, we use the default implementation.

```bash
def insertFromMimeData(self, source):

    if source.hasImage():

        image = QImage(source.imageData())
        cursor = self.textCursor()
        document = self.document()
        document.addResource(QTextDocument.ImageResource, QUrl("image"), image)
        cursor.insertImage("image")
```

We unpack the image from the QVariant held by the MIME source and insert it into the document as a resource.


## Editing Key Bindings

The list of key bindings which are implemented for editing:

| Keypresses   | Action                                            |
| ------------ | ------------------------------------------------- |
| Backspace    | Deletes the character to the left of the cursor.  |
| Delete       | Deletes the character to the right of the cursor. |
| Ctrl+C       | Copy the selected text to the clipboard.          |
| Ctrl+Insert  | Copy the selected text to the clipboard.          |
| Ctrl+K       | Deletes to the end of the line.                   |
| Ctrl+V       | Pastes the clipboard text into text edit.         |
| Shift+Insert | Pastes the clipboard text into text edit.         |
| Ctrl+X       | Deletes the selected text and copies it to the clipboard. |
| Shift+Delete | Deletes the selected text and copies it to the clipboard. |
| Ctrl+Z       | Undoes the last operation.                        |
| Ctrl+Y       | Redoes the last operation.                        |
| Left         | Moves the cursor one character to the left.       |
| Ctrl+Left    | Moves the cursor one word to the left.            |
| Right        | Moves the cursor one character to the right.      |
| Ctrl+Right   | Moves the cursor one word to the right.           |
| Up           | Moves the cursor one line up.                     |
| Down         | Moves the cursor one line down.                   |
| PageUp       | Moves the cursor one page up.                     |
| PageDown     | Moves the cursor one page down.                   |
| Home         | Moves the cursor to the beginning of the line.    |
| Ctrl+Home    | Moves the cursor to the beginning of the text.    |
| End          | Moves the cursor to the end of the line.          |
| Ctrl+End     | Moves the cursor to the end of the text.          |
| Alt+Wheel    | Scrolls the page horizontally (the Wheel is the mouse wheel). |

To select (mark) text hold down the Shift key whilst pressing one of the movement keystrokes, for example, Shift+Right will select the character to the right, and Shift+Ctrl+Right will select the word to the right, etc.


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
| QTextEdit.AutoNone       | (inherits enum.Flag) Don’t do any automatic formatting. |
| QTextEdit.AutoBulletList | Automatically create bullet lists e.g. when the user enters an asterisk (’*’) in the left most column, or presses Enter in an existing list item. |
| QTextEdit.AutoAll        | Apply all automatic formatting. Currently only automatic bullet lists are supported. |


--------------------------------
## property acceptRichText : bool

This property holds whether the text edit accepts rich text insertions by the user.

When this property is set to false text edit will accept only plain text input from the user. For example through clipboard or drag and drop.

This property’s default is true.

Access functions:

- acceptRichText()
- setAcceptRichText()


--------------------------------
## property autoFormatting : Combination of QTextEdit.AutoFormattingFlag

This property holds the enabled set of auto formatting features.

The value can be any combination of the values in the AutoFormattingFlag enum. The default is AutoNone . Choose AutoAll to enable all automatic formatting.

Currently, the only automatic formatting feature provided is AutoBulletList ; future versions of Qt may offer more.

Access functions:

- autoFormatting()
- setAutoFormatting()


--------------------------------
## property cursorWidth : int

This property specifies the width of the cursor in pixels. The default value is 1.

Access functions:

- cursorWidth()
- setCursorWidth()


--------------------------------
## property document : QTextDocument

This property holds the underlying document of the text editor..

Access functions:

- document()
- setDocument()


--------------------------------
## property documentTitle : str

This property holds the title of the document parsed from the text..

By default, for a newly-created, empty document, this property contains an empty string.

Access functions:

- documentTitle()
- setDocumentTitle()


--------------------------------
## property html : str

This property provides an HTML interface to the text of the text edit.

toHtml() returns the text of the text edit as html.

setHtml() changes the text of the text edit. Any previous text is removed and the undo/redo history is cleared. The input text is interpreted as rich text in html format. currentCharFormat() is also reset, unless textCursor() is already at the beginning of the document.

By default, for a newly-created, empty document, this property contains text to describe an HTML 4.0 document with no body text.

Access functions:

- toHtml()
- setHtml()
- Signal textChanged()


--------------------------------
## property lineWrapColumnOrWidth : int

This property holds the position (in pixels or columns depending on the wrap mode) where text will be wrapped.

If the wrap mode is FixedPixelWidth , the value is the number of pixels from the left edge of the text edit at which text should be wrapped. If the wrap mode is FixedColumnWidth , the value is the column number (in character columns) from the left edge of the text edit at which text should be wrapped.

By default, this property contains a value of 0.

Access functions:

- lineWrapColumnOrWidth()
- setLineWrapColumnOrWidth()


--------------------------------
## property lineWrapMode : QTextEdit.LineWrapMode

This property holds the line wrap mode.

The default mode is WidgetWidth which causes words to be wrapped at the right edge of the text edit. Wrapping occurs at whitespace, keeping whole words intact. If you want wrapping to occur within words use setWordWrapMode() . If you set a wrap mode of FixedPixelWidth or FixedColumnWidth you should also call setLineWrapColumnOrWidth() with the width you want.

Access functions:

- lineWrapMode()
- setLineWrapMode()


--------------------------------
## property markdown : str

This property provides a Markdown interface to the text of the text edit.

toMarkdown() returns the text of the text edit as “pure” Markdown, without any embedded HTML formatting. Some features that QTextDocument supports (such as the use of specific colors and named fonts) cannot be expressed in “pure” Markdown, and they will be omitted.

setMarkdown() changes the text of the text edit. Any previous text is removed and the undo/redo history is cleared. The input text is interpreted as rich text in Markdown format.

Parsing of HTML included in the markdown string is handled in the same way as in setHtml ; however, Markdown formatting inside HTML blocks is not supported.

Some features of the parser can be enabled or disabled via the features argument:

- MarkdownNoHTML
- Any HTML tags in the Markdown text will be discarded

The default is MarkdownDialectGitHub.

Access functions:

- toMarkdown()
- setMarkdown()
- Signal textChanged()


--------------------------------
## property overwriteMode : bool

This property holds whether text entered by the user will overwrite existing text.

As with many text editors, the text editor widget can be configured to insert or overwrite existing text with new text entered by the user.

If this property is true, existing text is overwritten, character-for-character by new text; otherwise, text is inserted at the cursor position, displacing existing text.

By default, this property is false (new text does not overwrite existing text).

Access functions:

- overwriteMode()
- setOverwriteMode()


--------------------------------
## property placeholderText : str

This property holds the editor placeholder text.

Setting this property makes the editor display a grayed-out placeholder text as long as the document() is empty.

By default, this property contains an empty string.

Access functions:

- placeholderText()
- setPlaceholderText()


--------------------------------
## property plainText : str

This property holds the text editor’s contents as plain text..

Previous contents are removed and undo/redo history is reset when the property is set. currentCharFormat() is also reset, unless textCursor() is already at the beginning of the document.

If the text edit has another content type, it will not be replaced by plain text if you call toPlainText() . The only exception to this is the non-break space, nbsp;, that will be converted into standard space.

By default, for an editor with no contents, this property contains an empty string.

Access functions:

- toPlainText()
- setPlainText()


--------------------------------
## property readOnly : bool

This property holds whether the text edit is read-only.

In a read-only text edit the user can only navigate through the text and select text; modifying the text is not possible.

This property’s default is false.

Access functions:

- isReadOnly()
- setReadOnly()


--------------------------------
## property tabChangesFocus : bool

This property holds whether Tab changes focus or is accepted as input.

In some occasions text edits should not allow the user to input tabulators or change indentation using the Tab key, as this breaks the focus chain. The default is false.

Access functions:

- tabChangesFocus()
- setTabChangesFocus()


--------------------------------
## property tabStopDistance : float

This property holds the tab stop distance in pixels.

By default, this property contains a value of 80 pixels.

Do not set a value less than the horizontalAdvance() of the QChar::VisualTabCharacter character, otherwise the tab-character will be drawn incompletely.

Access functions:

- tabStopDistance()
- setTabStopDistance()


--------------------------------
## property textInteractionFlags : Combination of Qt.TextInteractionFlag

Specifies how the widget should interact with user input.

The default value depends on whether the QTextEdit is read-only or editable, and whether it is a QTextBrowser or not.

Access functions:

- textInteractionFlags()
- setTextInteractionFlags()


--------------------------------
## property undoRedoEnabled : bool

This property holds whether undo and redo are enabled..

Users are only able to undo or redo actions if this property is true, and if there is an action that can be undone (or redone).

Access functions:

- isUndoRedoEnabled()
- setUndoRedoEnabled()


--------------------------------
## __init__(text[, parent=None])

Parameters:

- text – str
- parent – QWidget

Constructs a QTextEdit with parent parent. The text edit will display the text text. The text is interpreted as html.


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs an empty QTextEdit with parent parent.


--------------------------------
## acceptRichText()

Return type: bool

Getter of property acceptRichText  .


--------------------------------
## alignment()

Return type: Combination of AlignmentFlag

Returns the alignment of the current paragraph.


--------------------------------
## anchorAt(pos)

Parameters:

- pos – QPoint

Return type: str

Returns the reference of the anchor at position pos, or an empty string if no anchor exists at that point.


--------------------------------
## append(text)

Parameters:

- text – str

Appends a new paragraph with text to the end of the text edit.


--------------------------------
## autoFormatting()

Return type: Combination of AutoFormattingFlag

Getter of property autoFormatting  .


--------------------------------
## canInsertFromMimeData(source)

Parameters:

- source – QMimeData

Return type: bool

This function returns true if the contents of the MIME data object, specified by source, can be decoded and inserted into the document. It is called for example when during a drag operation the mouse enters this widget and it is necessary to determine whether it is possible to accept the drag and drop operation.

Reimplement this function to enable drag and drop support for additional MIME types.


--------------------------------
## canPaste()

Return type: bool

Returns whether text can be pasted from the clipboard into the textedit.


--------------------------------
## clear()

Deletes all the text in the text edit.


--------------------------------
## copy()

Copies any selected text to the clipboard.


--------------------------------
## copyAvailable(b)

Parameters:

- b – bool

This signal is emitted when text is selected or de-selected in the text edit.

When text is selected this signal will be emitted with yes set to true. If no text has been selected or if the selected text is de-selected this signal is emitted with yes set to false.

If yes is true then copy() can be used to copy the selection to the clipboard. If yes is false then copy() does nothing.


--------------------------------
## createMimeDataFromSelection()

Return type: QMimeData

This function returns a new MIME data object to represent the contents of the text edit’s current selection. It is called when the selection needs to be encapsulated into a new QMimeData object; for example, when a drag and drop operation is started, or when data is copied to the clipboard.

If you reimplement this function, note that the ownership of the returned QMimeData object is passed to the caller. The selection can be retrieved by using the textCursor() function.


--------------------------------
## createStandardContextMenu()

Return type: QMenu

This function creates the standard context menu which is shown when the user clicks on the text edit with the right mouse button. It is called from the default contextMenuEvent() handler. The popup menu’s ownership is transferred to the caller.

We recommend that you use the createStandardContextMenu(QPoint) version instead which will enable the actions that are sensitive to where the user clicked.


--------------------------------
## createStandardContextMenu(position)

Parameters:

- position – QPoint

Return type: QMenu

This function creates the standard context menu which is shown when the user clicks on the text edit with the right mouse button. It is called from the default contextMenuEvent() handler and it takes the position in document coordinates where the mouse click was. This can enable actions that are sensitive to the position where the user clicked. The popup menu’s ownership is transferred to the caller.


--------------------------------
## currentCharFormat()

Return type: QTextCharFormat

Returns the char format that is used when inserting new text.


--------------------------------
## currentCharFormatChanged(format)

Parameters:

- format – QTextCharFormat

This signal is emitted if the current character format has changed, for example caused by a change of the cursor position.

The new format is f.


--------------------------------
## currentFont()

Return type: QFont

Returns the font of the current format.


--------------------------------
## cursorForPosition(pos)

Parameters:

- pos – QPoint

Return type: QTextCursor

returns a QTextCursor at position pos (in viewport coordinates).


--------------------------------
## cursorPositionChanged()

This signal is emitted whenever the position of the cursor changed.


--------------------------------
## cursorRect()

Return type: QRect

returns a rectangle (in viewport coordinates) that includes the cursor of the text edit.


--------------------------------
## cursorRect(cursor)

Parameters:

- cursor – QTextCursor

Return type: QRect

returns a rectangle (in viewport coordinates) that includes the cursor.


--------------------------------
## cursorWidth()

Return type: int

Getter of property cursorWidth  .


--------------------------------
## cut()

Copies the selected text to the clipboard and deletes it from the text edit.

If there is no selected text nothing happens.


--------------------------------
## doSetTextCursor(cursor)

Parameters:

- cursor – QTextCursor


--------------------------------
## document()

Return type: QTextDocument

Getter of property document  .


--------------------------------
## documentTitle()

Return type: str

Getter of property documentTitle  .


--------------------------------
## ensureCursorVisible()

Ensures that the cursor is visible by scrolling the text edit if necessary.


--------------------------------
## extraSelections()

Return type: list of QTextEdit.ExtraSelection

Returns previously set extra selections.


--------------------------------
## find(exp[, options=QTextDocument.FindFlags()])

Parameters:

- exp – QRegularExpression
- options – Combination of FindFlag

Return type: bool

This is an overloaded function.

Finds the next occurrence, matching the regular expression, exp, using the given options.

Returns true if a match was found and changes the cursor to select the match; otherwise returns false.


--------------------------------
## find(exp[, options=QTextDocument.FindFlags()])

Parameters:

- exp – str
- options – Combination of FindFlag

Return type: bool

Finds the next occurrence of the string, exp, using the given options. Returns true if exp was found and changes the cursor to select the match; otherwise returns false.


--------------------------------
## fontFamily()

Return type: str

Returns the font family of the current format.


--------------------------------
## fontItalic()

Return type: bool

Returns true if the font of the current format is italic; otherwise returns false.


--------------------------------
## fontPointSize()

Return type: float

Returns the point size of the font of the current format.


--------------------------------
## fontUnderline()

Return type: bool

Returns true if the font of the current format is underlined; otherwise returns false.


--------------------------------
## fontWeight()

Return type: int

Returns the font weight of the current format.


--------------------------------
## inputMethodQuery(query, argument)

Parameters:

- query – InputMethodQuery
- argument – object

Return type: object


--------------------------------
## insertFromMimeData(source)

Parameters:

- source – QMimeData

This function inserts the contents of the MIME data object, specified by source, into the text edit at the current cursor position. It is called whenever text is inserted as the result of a clipboard paste operation, or when the text edit accepts data from a drag and drop operation.

Reimplement this function to enable drag and drop support for additional MIME types.


--------------------------------
## insertHtml(text)

Parameters:

- text – str

Convenience slot that inserts text which is assumed to be of html formatting at the current cursor position.

It is equivalent to:

```python
edit.textCursor().insertHtml(fragment)
```


--------------------------------
## insertPlainText(text)

Parameters:

- text – str

Convenience slot that inserts text at the current cursor position.

It is equivalent to

```python
edit.textCursor().insertText(text)
```


--------------------------------
## isReadOnly()

Return type: bool

Getter of property readOnly  .


--------------------------------
## isUndoRedoEnabled()

Return type: bool

Getter of property undoRedoEnabled  .


--------------------------------
## lineWrapColumnOrWidth()

Return type: int

Getter of property lineWrapColumnOrWidth  .


--------------------------------
## lineWrapMode()

Return type: LineWrapMode

Getter of property lineWrapMode  .


--------------------------------
## loadResource(type, name)

Parameters:

- type – int
- name – QUrl

Return type: object

Loads the resource specified by the given type and name.

This function is an extension of QTextDocument::loadResource().


--------------------------------
## mergeCurrentCharFormat(modifier)

Parameters:

- modifier – QTextCharFormat

Merges the properties specified in modifier into the current character format by calling QTextCursor::mergeCharFormat on the editor’s cursor. If the editor has a selection then the properties of modifier are directly applied to the selection.


--------------------------------
## moveCursor(operation[, mode=QTextCursor.MoveAnchor])

Parameters:

- operation – MoveOperation
- mode – MoveMode

Moves the cursor by performing the given operation.

If mode is QTextCursor::KeepAnchor, the cursor selects the text it moves over. This is the same effect that the user achieves when they hold down the Shift key and move the cursor with the cursor keys.


--------------------------------
## overwriteMode()

Return type: bool

Getter of property overwriteMode  .


--------------------------------
## paste()

Pastes the text from the clipboard into the text edit at the current cursor position.

If there is no text in the clipboard nothing happens.

To change the behavior of this function, i.e. to modify what QTextEdit can paste and how it is being pasted, reimplement the virtual canInsertFromMimeData() and insertFromMimeData() functions.


--------------------------------
## placeholderText()

Return type: str

Getter of property placeholderText  .


--------------------------------
## print_(printer)

Parameters:

- printer – QPagedPaintDevice


--------------------------------
## redo()

Redoes the last operation.

If there is no operation to redo, i.e. there is no redo step in the undo/redo history, nothing happens.


--------------------------------
## redoAvailable(b)

Parameters:

- b – bool

This signal is emitted whenever redo operations become available (available is true) or unavailable (available is false).


--------------------------------
## scrollToAnchor(name)

Parameters:

- name – str

Scrolls the text edit so that the anchor with the given name is visible; does nothing if the name is empty, or is already visible, or isn’t found.


--------------------------------
## selectAll()

Selects all text.


--------------------------------
## selectionChanged()

This signal is emitted whenever the selection changes.


--------------------------------
## setAcceptRichText(accept)

Parameters:

- accept – bool

Setter of property acceptRichText  .


--------------------------------
## setAlignment(a)

Parameters:

- a – Combination of AlignmentFlag

Sets the alignment of the current paragraph to a. Valid alignments are Qt::AlignLeft, Qt::AlignRight, Qt::AlignJustify and Qt::AlignCenter (which centers horizontally).


--------------------------------
## setAutoFormatting(features)

Parameters:

- features – Combination of AutoFormattingFlag

Setter of property autoFormatting  .


--------------------------------
## setCurrentCharFormat(format)

Parameters:

- format – QTextCharFormat

Sets the char format that is be used when inserting new text to format by calling QTextCursor::setCharFormat() on the editor’s cursor. If the editor has a selection then the char format is directly applied to the selection.


--------------------------------
## setCurrentFont(f)

Parameters:

- f – QFont

Sets the font of the current format to f.


--------------------------------
## setCursorWidth(width)

Parameters:

- width – int

Setter of property cursorWidth  .


--------------------------------
## setDocument(document)

Parameters:

- document – QTextDocument

Setter of property document  .


--------------------------------
## setDocumentTitle(title)

Parameters:

- title – str

Setter of property documentTitle  .


--------------------------------
## setExtraSelections(selections)

Parameters:

- selections – .list of QTextEdit.ExtraSelection

This function allows temporarily marking certain regions in the document with a given color, specified as selections. This can be useful for example in a programming editor to mark a whole line of text with a given background color to indicate the existence of a breakpoint.


--------------------------------
## setFontFamily(fontFamily)

Parameters:

- fontFamily – str

Sets the font family of the current format to fontFamily.


--------------------------------
## setFontItalic(b)

Parameters:

- b – bool

If italic is true, sets the current format to italic; otherwise sets the current format to non-italic.


--------------------------------
## setFontPointSize(s)

Parameters:

- s – float

Sets the point size of the current format to s.

Note that if s is zero or negative, the behavior of this function is not defined.


--------------------------------
## setFontUnderline(b)

Parameters:

- b – bool

If underline is true, sets the current format to underline; otherwise sets the current format to non-underline.


--------------------------------
## setFontWeight(w)

Parameters:

- w – int

Sets the font weight of the current format to the given weight, where the value used is in the range defined by the QFont::Weight enum.


--------------------------------
## setHtml(text)

Parameters:

- text – str

Setter of property html  .


--------------------------------
## setLineWrapColumnOrWidth(w)

Parameters:

- w – int

Setter of property lineWrapColumnOrWidth  .


--------------------------------
## setLineWrapMode(mode)

Parameters:

- mode – LineWrapMode

Setter of property lineWrapMode  .


--------------------------------
## setMarkdown(markdown)

Parameters:

- markdown – str

Setter of property markdown  .


--------------------------------
## setOverwriteMode(overwrite)

Parameters:

- overwrite – bool

Setter of property overwriteMode  .


--------------------------------
## setPlaceholderText(placeholderText)

Parameters:

- placeholderText – str

Setter of property placeholderText  .


--------------------------------
## setPlainText(text)

Parameters:

- text – str

Changes the text of the text edit to the string text. Any previous text is removed.

Setter of property plainText  .


--------------------------------
## setReadOnly(ro)

Parameters:

- ro – bool

Setter of property readOnly  .


--------------------------------
## setTabChangesFocus(b)

Parameters:

- b – bool

Setter of property tabChangesFocus  .


--------------------------------
## setTabStopDistance(distance)

Parameters:

- distance – float

Setter of property tabStopDistance  .


--------------------------------
setText(text)

Parameters:

- text – str

Sets the text edit’s text. The text can be plain text or HTML and the text edit will try to guess the right format.

Use setHtml() or setPlainText() directly to avoid text edit’s guessing.


--------------------------------
## setTextBackgroundColor(c)

Parameters:

- c – QColor

Sets the text background color of the current format to c.


--------------------------------
## setTextColor(c)

Parameters:

- c – QColor

Sets the text color of the current format to c.


--------------------------------
## setTextCursor(cursor)

Parameters:

- cursor – QTextCursor

Sets the visible cursor.


--------------------------------
## setTextInteractionFlags(flags)

Parameters:

- flags – Combination of TextInteractionFlag

Setter of property textInteractionFlags  .


--------------------------------
## setUndoRedoEnabled(enable)

Parameters:

- enable – bool

Setter of property undoRedoEnabled  .


--------------------------------
## setWordWrapMode(policy)

Parameters:

- policy – WrapMode


--------------------------------
## tabChangesFocus()

Return type: bool

Getter of property tabChangesFocus  .


--------------------------------
## tabStopDistance()

Return type: float

Getter of property tabStopDistance  .


--------------------------------
## textBackgroundColor()

Return type: QColor

Returns the text background color of the current format.


--------------------------------
## textChanged()

This signal is emitted whenever the document’s content changes; for example, when text is inserted or deleted, or when formatting is applied.

Notification signal of property markdown  .


--------------------------------
## textColor()

Return type: QColor

Returns the text color of the current format.


--------------------------------
## textCursor()

Return type: QTextCursor

Returns a copy of the QTextCursor that represents the currently visible cursor. Note that changes on the returned cursor do not affect QTextEdit ‘s cursor; use setTextCursor() to update the visible cursor.


--------------------------------
## textInteractionFlags()

Return type: Combination of TextInteractionFlag

Getter of property textInteractionFlags  .


--------------------------------
## toHtml()

Return type: str

Getter of property html  .


--------------------------------
## toMarkdown([features=QTextDocument.MarkdownDialectGitHub])

Parameters:

- features – Combination of MarkdownFeature

Return type: str


--------------------------------
## toPlainText()

Return type: str


--------------------------------
## QString QTextEdit::toPlainText() const

Returns the text of the text edit as plain text.

Getter of property plainText  .


--------------------------------
## undo()

Undoes the last operation.

If there is no operation to undo, i.e. there is no undo step in the undo/redo history, nothing happens.


--------------------------------
## undoAvailable(b)

Parameters:

- b – bool

This signal is emitted whenever undo operations become available (available is true) or unavailable (available is false).


--------------------------------
## wordWrapMode()

Return type: WrapMode


--------------------------------
## zoomIn([range=1])

Parameters:

- range – int

Zooms in on the text by making the base font size range points larger and recalculating all font sizes to be the new size. This does not change the size of any images.


--------------------------------
## zoomInF(range)

Parameters:

- range – float


--------------------------------
## zoomOut([range=1])

Parameters:

- range – int

Zooms out on the text by making the base font size range points smaller and recalculating all font sizes to be the new size. This does not change the size of any images.

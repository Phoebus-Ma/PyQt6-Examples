
[Chinese Doc](QLabel.CN.md)

# class QLabel

The QLabel widget provides a text or image display.


# Synopsis

## Properties

- [alignment](#property-alignment--combination-of-qtalignmentflag)

    The alignment of the label’s contents

- [hasSelectedText](#property-hasselectedtext--bool)

    Whether there is any text selected

- [indent](#property-indent--int)

    The label’s text indent in pixels

- [margin](#property-margin--int)

    The width of the margin

- [openExternalLinks](#property-openexternallinks--bool)

- [pixmap](#property-pixmap--qpixmap)

    The label’s pixmap

- [scaledContents](#property-scaledcontents--bool)

    Whether the label will scale its contents to fill all available space

- [selectedText](#property-selectedtext--str)

    The selected text

- [text](#property-text--str)

    The label’s text

- [textFormat](#property-textformat--qttextformat)

    The label’s text format

- [textInteractionFlags](#property-textinteractionflags--combination-of-qttextinteractionflag)

- [wordWrap](#property-wordwrap--bool)

    The label’s word-wrapping policy


## Methods

- [def \_\_init__()](#__init__text-parentnone-fqtwindowflags)

- [def alignment()](#alignment)

- [def buddy()](#buddy)

- [def hasScaledContents()](#hasScaledContents)

- [def hasSelectedText()](#hasselectedtext)

- [def indent()](#indent)

- [def margin()](#margin)

- [def movie()](#movie)

- [def openExternalLinks()](#openexternallinks)

- [def picture()](#picture)

- [def pixmap()](#pixmap)

- [def selectedText()](#selectedtext)

- [def selectionStart()](#selectionstart)

- [def setAlignment()](#setalignmentarg__1)

- [def setBuddy()](#setbuddyarg__1)

- [def setIndent()](#setindentarg__1)

- [def setMargin()](#setmarginarg__1)

- [def setOpenExternalLinks()](#setopenexternallinksopen)

- [def setScaledContents()](#setscaledcontentsarg__1)

- [def setSelection()](#setselectionarg__1-arg__2)

- [def setTextFormat()](#settextformatarg__1)

- [def setTextInteractionFlags()](#settextinteractionflagsflags)

- [def setWordWrap()](#setwordwrapon)

- [def text()](#text)

- [def textFormat()](#textformat)

- [def textInteractionFlags()](#textinteractionflags)

- [def wordWrap()](#wordwrap)


## Slots

- [def clear()](#clear)

- [def setMovie()](#setmoviemovie)

- [def setNum()](#setnumarg__1)

- [def setPicture()](#setpicturearg__1)

- [def setPixmap()](#setpixmaparg__1)

- [def setText()](#settextarg__1)


## Signals

- [def linkActivated()](#linkactivatedlink)

- [def linkHovered()](#linkhoveredlink)


# Detailed Description

QLabel is used for displaying text or an image. No user interaction functionality is provided. The visual appearance of the label can be configured in various ways, and it can be used for specifying a focus mnemonic key for another widget.

A QLabel can contain any of the following content types:

| Content    | Setting                                                                       |
| ---------- | ----------------------------------------------------------------------------- |
| Plain text | Pass a QString to setText()                                                   |
| Rich text  | Pass a QString that contains rich text to setText()                           |
| A pixmap   | Pass a QPixmap to setPixmap()                                                 |
| A movie    | Pass a QMovie to setMovie()                                                   |
| A number   | Pass an int or a double to setNum() , which converts the number to plain text |
| Nothing    | The same as an empty plain text. This is the default. Set by clear()          |

When the content is changed using any of these functions, any previous content is cleared.

By default, labels display left-aligned, vertically-centered text and images, where any tabs in the text to be displayed are automatically expanded. However, the look of a QLabel can be adjusted and fine-tuned in several ways.

The positioning of the content within the QLabel widget area can be tuned with setAlignment() and setIndent() . Text content can also wrap lines along word boundaries with setWordWrap() . For example, this code sets up a sunken panel with a two-line text in the bottom right corner (both lines being flush with the right side of the label):

```python
label = QLabel(self)
label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
label.setText("first line\nsecond line")
label.setAlignment(Qt.AlignBottom | Qt.AlignRight)
```

The properties and functions QLabel inherits from QFrame can also be used to specify the widget frame to be used for any given label.

A QLabel is often used as a label for an interactive widget. For this use QLabel provides a useful mechanism for adding an mnemonic (see QKeySequence) that will set the keyboard focus to the other widget (called the QLabel ‘s “buddy”). For example:

```python
phoneEdit = QLineEdit(self)
phoneLabel = QLabel("Phone:", self)
phoneLabel.setBuddy(phoneEdit)
```

In this example, keyboard focus is transferred to the label’s buddy (the QLineEdit ) when the user presses Alt+P. If the buddy was a button (inheriting from QAbstractButton ), triggering the mnemonic would emulate a button click.

--------------------------------
## `property alignment` : Combination of Qt.AlignmentFlag

This property holds the alignment of the label’s contents.

By default, the contents of the label are left-aligned and vertically-centered.

Access functions:

- alignment()
- setAlignment()

--------------------------------
## `property hasSelectedText` : bool

This property holds whether there is any text selected.

hasSelectedText() returns true if some or all of the text has been selected by the user; otherwise returns false.

By default, this property is false.

Access functions:

- hasSelectedText()

--------------------------------
## `property indent` : int

This property holds the label’s text indent in pixels.

If a label displays text, the indent applies to the left edge if alignment() is Qt::AlignLeft, to the right edge if alignment() is Qt::AlignRight, to the top edge if alignment() is Qt::AlignTop, and to the bottom edge if alignment() is Qt::AlignBottom.

If indent is negative, or if no indent has been set, the label computes the effective indent as follows: If frameWidth() is 0, the effective indent becomes 0. If frameWidth() is greater than 0, the effective indent becomes half the width of the “x” character of the widget’s current font() .

By default, the indent is -1, meaning that an effective indent is calculating in the manner described above.

Access functions:

- indent()
- setIndent()

--------------------------------
## `property margin` : int

This property holds the width of the margin.

The margin is the distance between the innermost pixel of the frame and the outermost pixel of contents.

The default margin is 0.

Access functions:

- margin()
- setMargin()

--------------------------------
## `property openExternalLinks` : bool

Specifies whether QLabel should automatically open links using QDesktopServices::openUrl() instead of emitting the linkActivated() signal.

The default value is false.

Access functions:

- openExternalLinks()
- setOpenExternalLinks()

--------------------------------
## `property pixmap` : QPixmap

This property holds the label’s pixmap..

Setting the pixmap clears any previous content. The buddy shortcut, if any, is disabled.

Access functions:

- pixmap()
- setPixmap()

--------------------------------
## `property scaledContents` : bool

This property holds whether the label will scale its contents to fill all available space..

When enabled and the label shows a pixmap, it will scale the pixmap to fill the available space.

This property’s default is false.

Access functions:

- hasScaledContents()
- setScaledContents()

--------------------------------
## `property selectedText` : str

This property holds the selected text.

If there is no selected text this property’s value is an empty string.

By default, this property contains an empty string.

Access functions:

- selectedText()

--------------------------------
## `property text` : str

This property holds the label’s text.

If no text has been set this will return an empty string. Setting the text clears any previous content.

The text will be interpreted either as plain text or as rich text, depending on the text format setting; see setTextFormat() . The default setting is Qt::AutoText; i.e. QLabel will try to auto-detect the format of the text set. See Supported HTML Subset for the definition of rich text.

If a buddy has been set, the buddy mnemonic key is updated from the new text.

Note that QLabel is well-suited to display small rich text documents, such as small documents that get their document specific settings (font, text color, link color) from the label’s palette and font properties. For large documents, use QTextEdit in read-only mode instead. QTextEdit can also provide a scroll bar when necessary.

Access functions:

- text()
- setText()

--------------------------------
## `property textFormat` : Qt.TextFormat

This property holds the label’s text format.

See the Qt::TextFormat enum for an explanation of the possible options.

The default format is Qt::AutoText.

Access functions:

- textFormat()
- setTextFormat()

--------------------------------
## `property textInteractionFlags` : Combination of Qt.TextInteractionFlag

Specifies how the label should interact with user input if it displays text.

If the flags contain Qt::LinksAccessibleByKeyboard the focus policy is also automatically set to Qt::StrongFocus. If Qt::TextSelectableByKeyboard is set then the focus policy is set to Qt::ClickFocus.

The default value is Qt::LinksAccessibleByMouse.

Access functions:

- textInteractionFlags()
- setTextInteractionFlags()

--------------------------------
## `property wordWrap` : bool

This property holds the label’s word-wrapping policy.

If this property is true then label text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all.

By default, word wrap is disabled.

Access functions:

- wordWrap()
- setWordWrap()

--------------------------------
## `__init__(text[, parent=None[, f=Qt.WindowFlags()]])`

PARAMETERS:

- text – str
- parent – QWidget
- f – Combination of WindowType

Constructs a label that displays the text, text.

The parent and widget flag f, arguments are passed to the QFrame constructor.

--------------------------------
## `__init__([parent=None[, f=Qt.WindowFlags()]])`

PARAMETERS:

- parent – QWidget
- f – Combination of WindowType

Constructs an empty label.

The parent and widget flag f, arguments are passed to the QFrame constructor.

--------------------------------
## `alignment()`

RETURN TYPE: Combination of AlignmentFlag

Getter of property alignment.

--------------------------------
## `buddy()`

RETURN TYPE: QWidget

Returns this label’s buddy, or nullptr if no buddy is currently set.

--------------------------------
## `clear()`

Clears any label contents.

--------------------------------
## `hasScaledContents()`

RETURN TYPE: bool

Getter of property scaledContents.

--------------------------------
## `hasSelectedText()`

RETURN TYPE: bool

Getter of property hasSelectedText.

--------------------------------
## `indent()`

RETURN TYPE: int

Getter of property indent.

--------------------------------
## `linkActivated(link)`

PARAMETERS:

- link – str

This signal is emitted when the user clicks a link. The URL referred to by the anchor is passed in link.

--------------------------------
## `linkHovered(link)`

PARAMETERS:

- link – str

This signal is emitted when the user hovers over a link. The URL referred to by the anchor is passed in link.

--------------------------------
## `margin()`

RETURN TYPE: int

Getter of property margin.

--------------------------------
## `movie()`

RETURN TYPE: QMovie

Returns a pointer to the label’s movie, or nullptr if no movie has been set.

--------------------------------
## `openExternalLinks()`

RETURN TYPE: bool

Getter of property openExternalLinks.

--------------------------------
## `picture()`

RETURN TYPE: QPicture

Returns the label’s picture.

--------------------------------
## `pixmap()`

RETURN TYPE: QPixmap

Getter of property pixmap.

--------------------------------
## `selectedText()`

RETURN TYPE: str

Getter of property selectedText.

--------------------------------
## `selectionStart()`

RETURN TYPE: int

selectionStart() returns the index of the first selected character in the label or -1 if no text is selected.

--------------------------------
## `setAlignment(arg__1)`

PARAMETERS:

- arg__1 – Combination of AlignmentFlag

Setter of property alignment.

--------------------------------
## `setBuddy(arg__1)`

PARAMETERS:

- arg__1 – QWidget

Sets this label’s buddy to buddy.

When the user presses the shortcut key indicated by this label, the keyboard focus is transferred to the label’s buddy widget.

The buddy mechanism is only available for QLabels that contain text in which one character is prefixed with an ampersand, ‘&’. This character is set as the shortcut key. See the QKeySequence::mnemonic() documentation for details (to display an actual ampersand, use ‘&&’).

In a dialog, you might create two data entry widgets and a label for each, and set up the geometry layout so each label is just to the left of its data entry widget (its “buddy”), for example:

```python
nameEdit = QLineEdit(self)
QLabel nameLabel = QLabel("Name:", self)
nameLabel.setBuddy(nameEdit)
phoneEdit = QLineEdit(self)
QLabel phoneLabel = QLabel("Phone:", self)
phoneLabel.setBuddy(phoneEdit)
# (layout setup not shown)
```

With the code above, the focus jumps to the Name field when the user presses Alt+N, and to the Phone field when the user presses Alt+P.

To unset a previously set buddy, call this function with buddy set to nullptr.

--------------------------------
## `setIndent(arg__1)`

PARAMETERS:

- arg__1 – int

Setter of property indent.

--------------------------------
## `setMargin(arg__1)`

PARAMETERS:

- arg__1 – int

Setter of property margin.

--------------------------------
## `setMovie(movie)`

PARAMETERS:

- movie – QMovie

Sets the label contents to movie. Any previous content is cleared. The label does NOT take ownership of the movie.

The buddy shortcut, if any, is disabled.

--------------------------------
## `setNum(arg__1)`

PARAMETERS:

- arg__1 – float

This is an overloaded function.

Sets the label contents to plain text containing the textual representation of double num. Any previous content is cleared. Does nothing if the double’s string representation is the same as the current contents of the label.

The buddy shortcut, if any, is disabled.

--------------------------------
## `setNum(arg__1)`

PARAMETERS:

- arg__1 – int

Sets the label contents to plain text containing the textual representation of integer num. Any previous content is cleared. Does nothing if the integer’s string representation is the same as the current contents of the label.

The buddy shortcut, if any, is disabled.

--------------------------------
## `setOpenExternalLinks(open)`

PARAMETERS:

- open – bool

Setter of property openExternalLinks.

--------------------------------
## `setPicture(arg__1)`

PARAMETERS:

- arg__1 – QPicture

Sets the label contents to picture. Any previous content is cleared.

The buddy shortcut, if any, is disabled.

--------------------------------
## `setPixmap(arg__1)`

PARAMETERS:

- arg__1 – QPixmap

Setter of property pixmap.

--------------------------------
## `setScaledContents(arg__1)`

PARAMETERS:

- arg__1 – bool

Setter of property scaledContents.

--------------------------------
## `setSelection(arg__1, arg__2)`

P1ARAMETERS:

- arg__1 – int
- arg__2 – int

Selects text from position start and for length characters.

--------------------------------
## `setText(arg__1)`

PARAMETERS:

- arg__1 – str

Setter of property text.

--------------------------------
## `setTextFormat(arg__1)`

PARAMETERS:

- arg__1 – TextFormat

Setter of property textFormat.

--------------------------------
## `setTextInteractionFlags(flags)`

PARAMETERS:

- flags – Combination of TextInteractionFlag

Setter of property textInteractionFlags.

--------------------------------
## `setWordWrap(on)`

PARAMETERS:

- on – bool

Setter of property wordWrap.

--------------------------------
## `text()`

RETURN TYPE: str

Getter of property text.

--------------------------------
## `textFormat()`

RETURN TYPE: TextFormat

Getter of property textFormat.

--------------------------------
## `textInteractionFlags()`

RETURN TYPE: Combination of TextInteractionFlag

Getter of property textInteractionFlags.

--------------------------------
## `wordWrap()`

RETURN TYPE: bool

Getter of property wordWrap.

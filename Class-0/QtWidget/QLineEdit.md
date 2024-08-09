
[Chinese doc](QLineEdit.CN.md)

# class QLineEdit

The QLineEdit widget is a one-line text editor.


# Synopsis

## Properties

- [acceptableInput](#property-acceptableinput--bool)

    Whether the input satisfies the inputMask and the validator.

- [alignment](#property-alignment--combination-of-qtalignmentflag)

    Of the line edit.

- [clearButtonEnabled](#property-clearbuttonenabled--bool)

    Whether the line edit displays a clear button when it is not empty.

- [cursorMoveStyle](#property-cursormovestyle--qtcursormovestyle)

    Movement style of the cursor in this line edit.

- [cursorPosition](#property-cursorposition--int)

    Current cursor position for this line edit.

- [displayText](#property-displaytext--str)

    Displayed text.

- [dragEnabled](#property-dragenabled--bool)

    Whether the line edit starts a drag if the user presses and moves the mouse on some selected text.

- [echoMode](#property-echomode--qlineeditechomode)

    Line edit’s echo mode.

- [frame](#property-frame--bool)

    Whether the line edit draws itself with a frame.

- [hasSelectedText](#property-hasselectedtext--bool)

    Whether there is any text selected.

- [inputMask](#property-inputmask--str)

    Validation input mask.

- [maxLength](#property-maxlength--int)

    Maximum permitted length of the text.

- [modified](#property-modified--bool)

    Whether the line edit’s contents has been modified by the user.

- [placeholderText](#property-placeholdertext--str)

    Line edit’s placeholder text.

- [readOnly](#property-readonly--bool)

    Whether the line edit is read-only.

- [redoAvailable](#property-redoavailable--bool)

    Whether redo is available.

- [selectedText](#property-selectedtext--str)

    Selected text.

- [text](#property-text--str)

    Line edit’s text.

- [undoAvailable](#property-undoavailable--bool)

    Whether undo is available.


## Methods

- [def \_\_init__()](#initparentnone)

- [def addAction()](#addactionaction-position)

- [def alignment()](#alignment)

- [def backspace()](#backspace)

- [def completer()](#completer)

- [def createStandardContextMenu()](#createstandardcontextmenu)

- [def cursorBackward()](#cursorbackwardmark-steps1)

- [def cursorForward()](#cursorforwardmark-steps1)

- [def cursorMoveStyle()](#cursormovestyle)

- [def cursorPosition()](#cursorposition)

- [def cursorPositionAt()](#cursorpositionatpos)

- [def cursorRect()](#cursorrect)

- [def cursorWordBackward()](#cursorwordbackwardmark)

- [def cursorWordForward()](#cursorwordforwardmark)

- [def del_()](#del_)

- [def deselect()](#deselect)

- [def displayText()](#displaytext)

- [def dragEnabled()](#dragenabled)

- [def echoMode()](#echomode)

- [def end()](#endmark)

- [def hasAcceptableInput()](#hasacceptableinput)

- [def hasFrame()](#hasframe)

- [def hasSelectedText()](#hasselectedtext)

- [def home()](#homemark)

- [def inputMask()](#inputmask)

- [def inputMethodQuery()](#inputmethodqueryproperty-argument)

- [def insert()](#insertarg__1)

- [def isClearButtonEnabled()](#isclearbuttonenabled)

- [def isModified()](#ismodified)

- [def isReadOnly()](#isreadonly)

- [def isRedoAvailable()](#isredoavailable)

- [def isUndoAvailable()](#isundoavailable)

- [def maxLength()](#maxlength)

- [def placeholderText()](#placeholdertext)

- [def selectedText()](#selectedtext)

- [def selectionEnd()](#selectionend)

- [def selectionLength()](#selectionlength)

- [def selectionStart()](#selectionstart)

- [def setAlignment()](#setalignmentflag)

- [def setClearButtonEnabled()](#setclearbuttonenabledenable)

- [def setCompleter()](#setcompletercompleter)

- [def setCursorMoveStyle()](#setcursormovestylestyle)

- [def setCursorPosition()](#setcursorpositionarg__1)

- [def setDragEnabled()](#setdragenabledb)

- [def setEchoMode()](#setechomodearg__1)

- [def setFrame()](#setframearg__1)

- [def setInputMask()](#setinputmaskinputmask)

- [def setMaxLength()](#setmaxlengtharg__1)

- [def setModified()](#setmodifiedarg__1)

- [def setPlaceholderText()](#setplaceholdertextarg__1)

- [def setReadOnly()](#setreadonlyarg__1)

- [def setSelection()](#setselectionarg__1-arg__2)

- [def setTextMargins()](#settextmarginsmargins)

- [def setValidator()](#setvalidatorarg__1)

- [def text()](#text)

- [def textMargins()](#textmargins)

- [def validator()](#validator)


## Virtual methods

- [def initStyleOption()](#initstyleoptionoption)


## Slots

- [def clear()](#clear)

- [def copy()](#copy)

- [def cut()](#cut)

- [def paste()](#paste)

- [def redo()](#redo)

- [def selectAll()](#selectall)

- [def setText()](#settextarg__1)

- [def undo()](#undo)


## Signals

- [def cursorPositionChanged()](#cursorpositionchangedarg__1-arg__2)

- [def editingFinished()](#editingfinished)

- [def inputRejected()](#inputrejected)

- [def returnPressed()](#returnpressed)

- [def selectionChanged()](#selectionchanged)

- [def textChanged()](#textchangedarg__1)

- [def textEdited()](#texteditedarg__1)


# Detailed Description

A line edit allows users to enter and edit a single line of plain text with useful editing functions, including undo and redo, cut and paste, and drag and drop.

By changing the echoMode() of a line edit, it can also be used as a write-only field for inputs such as passwords.

QTextEdit is a related class that allows multi-line, rich text editing.


## Constraining Text

Use maxLength to define the maximum permitted length of a text. You can use a inputMask and setValidator() to further constrain the text content.


## Editing Text

You can change the text with setText() or insert() . Use text() to retrieve the text and displayText() to retrieve the displayed text (which may be different, see EchoMode ). You can select the text with setSelection() or selectAll() , and you can cut() , copy() , and paste() the selection. To align the text, use setAlignment() .

When the text changes, the textChanged() signal is emitted. When the text changes in some other way than by calling setText() , the textEdited() signal is emitted. When the cursor is moved, the cursorPositionChanged() signal is emitted. And when the Return or Enter key is selected, the returnPressed() signal is emitted.

When text editing is finished, either because the line edit lost focus or Return/Enter was selected, the editingFinished() signal is emitted.

If the line edit focus is lost without any text changes, the editingFinished() signal won’t be emitted.

If there is a validator set on the line edit, the returnPressed() / editingFinished() signals will only be emitted if the validator returns QValidator::Acceptable.

For more information on the many ways that QLineEdit can be used, see Line Edits Example , which also provides a selection of line edit examples that show the effects of various properties and validators on the input and output supplied by the user.


## Setting a Frame

By default, QLineEdits have a frame as specified in the platform style guides. You can turn the frame off by calling setFrame (false).


## Default Key Bindings

The table below describes the default key bindings.

Any other keystroke that represents a valid character, will cause the character to be inserted into the line edit.


--------------------------------
## class ActionPosition

This enum type describes how a line edit should display the action widgets to be added.

| Constant                   | Description |
| -------------------------- | ----------- |
| QLineEdit.LeadingPosition  | The widget is displayed to the left of the text when using layout direction Qt::LeftToRight or to the right when using Qt::RightToLeft, respectively. |
| QLineEdit.TrailingPosition | The widget is displayed to the right of the text when using layout direction Qt::LeftToRight or to the left when using Qt::RightToLeft, respectively. |


--------------------------------
## class EchoMode

This enum type describes how a line edit should display its contents.

| Constant                     | Description |
| ---------------------------- | ----------- |
| QLineEdit.Normal             | Display characters as they are entered. This is the default. |
| QLineEdit.NoEcho             | Do not display anything. This may be appropriate for passwords where even the length of the password should be kept secret. |
| QLineEdit.Password           | Display platform-dependent password mask characters instead of the characters actually entered. |
| QLineEdit.PasswordEchoOnEdit | Display characters only while they are entered. Otherwise, display characters as with Password. |


--------------------------------
## property acceptableInput : bool

This property holds Whether the input satisfies the inputMask and the validator..

By default, this property is true.

Access functions:

- hasAcceptableInput()


--------------------------------
## property alignment : Combination of Qt.AlignmentFlag

This property holds The alignment of the line edit..

Both horizontal and vertical alignment is allowed here, Qt::AlignJustify will map to Qt::AlignLeft.

By default, this property contains a combination of Qt::AlignLeft and Qt::AlignVCenter.

Access functions:

- alignment()
- setAlignment()


--------------------------------
## property clearButtonEnabled : bool

This property holds Whether the line edit displays a clear button when it is not empty..

If enabled, the line edit displays a trailing clear button when it contains some text. Otherwise, the line edit does not show a clear button (the default).

Access functions:

- isClearButtonEnabled()
- setClearButtonEnabled()


--------------------------------
## property cursorMoveStyle : Qt.CursorMoveStyle

This property holds The movement style of the cursor in this line edit..

When this property is set to Qt::VisualMoveStyle, the line edit will use a visual movement style. Using the left arrow key will always cause the cursor to move left, regardless of the text’s writing direction. The same behavior applies to the right arrow key.

When the property is set to Qt::LogicalMoveStyle (the default), within a left-to-right (LTR) text block, using the left arrow key will increase the cursor position, whereas using the right arrow key will decrease the cursor position. If the text block is right-to-left (RTL), the opposite behavior applies.

Access functions:

- cursorMoveStyle()
- setCursorMoveStyle()


--------------------------------
## property cursorPosition : int

This property holds The current cursor position for this line edit..

Setting the cursor position causes a repaint when appropriate.

By default, this property contains a value of 0.

Access functions:

- cursorPosition()
- setCursorPosition()


--------------------------------
## property displayText : str

This property holds The displayed text..

If echoMode is Normal , this returns the same as text() . If EchoMode is Password or PasswordEchoOnEdit , it returns a string of platform-dependent password mask characters (e.g. “******”). If EchoMode is NoEcho , it returns an empty string.

By default, this property contains an empty string.

Access functions:

- displayText()


--------------------------------
## property dragEnabled : bool

This property holds Whether the line edit starts a drag if the user presses and moves the mouse on some selected text..

Dragging is disabled by default.

Access functions:

- dragEnabled()
- setDragEnabled()


--------------------------------
## property echoMode : QLineEdit.EchoMode

This property holds The line edit’s echo mode..

The echo mode determines how the text entered in the line edit is displayed (or echoed) to the user.

The most common setting is Normal , in which the text entered by the user is displayed verbatim. QLineEdit also supports modes that allow the entered text to be suppressed or obscured: these include NoEcho , Password and PasswordEchoOnEdit .

The widget’s display and the ability to copy or drag the text is affected by this setting.

By default, this property is set to Normal .

Access functions:

- echoMode()
- setEchoMode()


--------------------------------
## property frame : bool

This property holds Whether the line edit draws itself with a frame..

If enabled (the default), the line edit draws itself inside a frame. Otherwise, the line edit draws itself without any frame.

Access functions:

- hasFrame()
- setFrame()


--------------------------------
## property hasSelectedText : bool

This property holds Whether there is any text selected..

hasSelectedText() returns true if some or all of the text has been selected by the user. Otherwise, it returns false.

By default, this property is false.

Access functions:

- hasSelectedText()


--------------------------------
## property inputMask : str

This property holds The validation input mask..

Sets the QLineEdit ‘s validation mask. Validators can be used instead of, or in conjunction with masks; see setValidator() . The default is an empty string, which means that no input mask is used.

To unset the mask and return to normal QLineEdit operation, pass an empty string.

The input mask is an input template string. It can contain the following elements:

|                 |          |
| --------------- | -------- |
| Mask Characters | Defines the Category of input characters that are considered valid in this position. |
| Meta Characters | Various special meanings (see details below).              |
| Separators      | All other characters are regarded as immutable separators. |

The following table shows the mask and meta characters that can be used in an input mask.

| Mask Character | Meaning |
| -------------- | ------- |
| A              | Character of the Letter category required, such as A-Z, a-z. |
| a              | Character of the Letter category permitted but not required. |
| N              | Character of the Letter or Number category required, such as A-Z, a-z, 0-9. |
| n              | Character of the Letter or Number category permitted but not required. |
| X              | Any non-blank character required.                            |
| x              | Any non-blank character permitted but not required.          |
| 9              | Character of the Number category required, such as 0-9.      |
| 0              | Character of the Number category permitted but not required. |
| D              | Character of the Number category and larger than zero required, such as 1-9. |
| d              | Character of the Number category and larger than zero permitted but not required, such as 1-9. |
| #              | Character of the Number category, or plus/minus sign permitted but not required. |
| H              | Hexadecimal character required. A-F, a-f, 0-9.               |
| h              | Hexadecimal character permitted but not required.            |
| B              | Binary character required. 0-1.                              |
| b              | Binary character permitted but not required.                 |

| Meta Character | Meaning                                             |
| -------------- | --------------------------------------------------- |
| >              | All following alphabetic characters are uppercased. |
| <              | All following alphabetic characters are lowercased. |
| !              | Switch off case conversion.                         |
| ;c             | Terminates the input mask and sets the blank character to c. |
| [ ] { }        | Reserved.                                           |
| \              | Use \ to escape the special characters listed above to use them as separators. |

When created or cleared, the line edit will be filled with a copy of the input mask string where the meta characters have been removed, and the mask characters have been replaced with the blank character (by default, a space).

When an input mask is set, the text() method returns a modified copy of the line edit content where all the blank characters have been removed. The unmodified content can be read using displayText() .

The hasAcceptableInput() method returns false if the current content of the line edit does not fulfill the requirements of the input mask.

Examples:

| Mask                | Notes                      |
| ------------------- | -------------------------- |
| 000.000.000.000;_   | IP address; blanks are _.  |
| HH:HH:HH:HH:HH:HH;_ | MAC address                |
| 0000-00-00          | ISO Date; blanks are space |
| >AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;# | License number; blanks are # and all (alphabetic) characters are converted to uppercase. |

To get range control (e.g., for an IP address) use masks together with validators .

Access functions:

- inputMask()
- setInputMask()


--------------------------------
## property maxLength : int

This property holds The maximum permitted length of the text..

If the text is too long, it is truncated at the limit.

If truncation occurs, any selected text will be unselected, the cursor position is set to 0, and the first part of the string is shown.

If the line edit has an input mask, the mask defines the maximum string length.

By default, this property contains a value of 32767.

Access functions:

- maxLength()
- setMaxLength()


--------------------------------
## property modified : bool

This property holds Whether the line edit’s contents has been modified by the user..

The modified flag is never read by QLineEdit ; it has a default value of false and is changed to true whenever the user changes the line edit’s contents.

This is useful for things that need to provide a default value but do not start out knowing what the default should be (for example, it depends on other fields on the form). Start the line edit without the best default, and when the default is known, if modified() returns false (the user hasn’t entered any text), insert the default value.

Calling setText() resets the modified flag to false.

Access functions:

- isModified()
- setModified()


--------------------------------
## property placeholderText : str

This property holds The line edit’s placeholder text..

Setting this property makes the line edit display a grayed-out placeholder text as long as the line edit is empty.

Normally, an empty line edit shows the placeholder text even when it has focus. However, if the content is horizontally centered, the placeholder text is not displayed under the cursor when the line edit has focus.

By default, this property contains an empty string.

Access functions:

- placeholderText()
- setPlaceholderText()


--------------------------------
## property readOnly : bool

This property holds Whether the line edit is read-only..

In read-only mode, the user can still copy the text to the clipboard, or drag and drop the text (if echoMode() is Normal ), but cannot edit it.

QLineEdit does not show a cursor in read-only mode.

By default, this property is false.

Access functions:

- isReadOnly()
- setReadOnly()


--------------------------------
## property redoAvailable : bool

This property holds Whether redo is available..

Redo becomes available once the user has performed one or more undo operations on the text in the line edit.

By default, this property is false.

Access functions:

- isRedoAvailable()


--------------------------------
## property selectedText : str

This property holds The selected text..

If there is no selected text, this property’s value is an empty string.

By default, this property contains an empty string.

Access functions:

- selectedText()


--------------------------------
## property text : str

This property holds The line edit’s text..

Setting this property clears the selection, clears the undo/redo history, moves the cursor to the end of the line, and resets the modified property to false. The text is not validated when inserted with setText().

The text is truncated to maxLength() length.

By default, this property contains an empty string.

Access functions:

- text()
- setText()
- Signal textChanged()


--------------------------------
## property undoAvailable : bool

This property holds Whether undo is available..

Undo becomes available once the user has modified the text in the line edit.

By default, this property is false.

Access functions:

- isUndoAvailable()


--------------------------------
## __init__(arg__1[, parent=None])

Parameters:

- arg__1 – str
- parent – QWidget

Constructs a line edit containing the text contents as a child of parent.

The cursor position is set to the end of the line and the maximum text length to 32767 characters.


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs a line edit with no text.

The maximum text length is set to 32767 characters.

The parent argument is sent to the QWidget constructor.


--------------------------------
## addAction(icon, position)

Parameters:

- icon – QIcon
- position – ActionPosition

Return type: QAction

This is an overloaded function.

Creates a new action with the given icon at the position.


--------------------------------
## addAction(action, position)

Parameters:

- action – QAction
- position – ActionPosition

Adds the action to the list of actions at the position.


--------------------------------
## alignment()

Return type: Combination of AlignmentFlag

Getter of property alignment  .


--------------------------------
## backspace()

If no text is selected, deletes the character to the left of the text cursor, and moves the cursor one position to the left. If any text is selected, the cursor is moved to the beginning of the selected text, and the selected text is deleted.


--------------------------------
## clear()

Clears the contents of the line edit.


--------------------------------
## completer()

Return type: QCompleter

Returns the current QCompleter that provides completions.


--------------------------------
## copy()

Copies the selected text to the clipboard, if there is any, and if echoMode() is Normal .


--------------------------------
## createStandardContextMenu()

Return type: QMenu

Creates the standard context menu, which is shown when the user clicks on the line edit with the right mouse button. It is called from the default contextMenuEvent() handler. The popup menu’s ownership is transferred to the caller.


--------------------------------
## cursorBackward(mark[, steps=1])

Parameters:

- mark – bool
- steps – int

Moves the cursor back steps characters. If mark is true, each character moved over is added to the selection. If mark is false, the selection is cleared.


--------------------------------
## cursorForward(mark[, steps=1])

Parameters:

- mark – bool
- steps – int

Moves the cursor forward steps characters. If mark is true, each character moved over is added to the selection. If mark is false, the selection is cleared.


--------------------------------
## cursorMoveStyle()

Return type: CursorMoveStyle

Getter of property cursorMoveStyle  .


--------------------------------
## cursorPosition()

Return type: int

Getter of property cursorPosition  .


--------------------------------
## cursorPositionAt(pos)

Parameters:

- pos – QPoint

Return type: int

Returns the cursor position under the point pos.


--------------------------------
## cursorPositionChanged(arg__1, arg__2)

Parameters:

- arg__1 – int
- arg__2 – int

This signal is emitted whenever the cursor moves. The previous position is given by oldPos, and the new position by newPos.


--------------------------------
## cursorRect()

Return type: QRect

Returns a rectangle that includes the line edit cursor.


--------------------------------
## cursorWordBackward(mark)

Parameters:

- mark – bool

Moves the cursor one word backward. If mark is true, the word is also selected.


--------------------------------
## cursorWordForward(mark)

Parameters:

- mark – bool

Moves the cursor one word forward. If mark is true, the word is also selected.


--------------------------------
## cut()

Copies the selected text to the clipboard and deletes it, if there is any, and if echoMode() is Normal .

If the current validator disallows deleting the selected text, cut() will copy without deleting.


--------------------------------
## del_()
## deselect()

Deselects any selected text.


--------------------------------
## displayText()

Return type: str

Getter of property displayText  .


--------------------------------
## dragEnabled()

Return type: bool

Getter of property dragEnabled  .


--------------------------------
## echoMode()

Return type: EchoMode

Getter of property echoMode  .

--------------------------------
## editingFinished()

This signal is emitted when the Return or Enter key is used, or if the line edit loses focus and its contents have changed since the last time this signal was emitted.


--------------------------------
## end(mark)

Parameters:

- mark – bool

Moves the text cursor to the end of the line unless it is already there. If mark is true, text is selected towards the last position. Otherwise, any selected text is unselected if the cursor is moved.


--------------------------------
## hasAcceptableInput()

Return type: bool

Getter of property acceptableInput  .


--------------------------------
## hasFrame()

Return type: bool

Getter of property frame  .


--------------------------------
## hasSelectedText()

Return type: bool

Getter of property hasSelectedText  .


--------------------------------
## home(mark)

Parameters:

- mark – bool

Moves the text cursor to the beginning of the line unless it is already there. If mark is true, text is selected towards the first position. Otherwise, any selected text is unselected if the cursor is moved.


--------------------------------
## initStyleOption(option)

Parameters:

- option – QStyleOptionFrame

Initialize option with the values from this QLineEdit . This method is useful for subclasses when they need a QStyleOptionFrame , but don’t want to fill in all the information themselves.


--------------------------------
## inputMask()

Return type: str

Getter of property inputMask  .


--------------------------------
## inputMethodQuery(property, argument)

Parameters:

- property – InputMethodQuery
- argument – object

Return type: object


--------------------------------
## inputRejected()

This signal is emitted when the user uses a key that is not considered to be valid input. For example, if using a key results in a validator’s validate() call to return Invalid. Another case is when trying to enter more characters beyond the maximum length of the line edit.


--------------------------------
## insert(arg__1)

Parameters:

- arg__1 – str

Deletes any selected text, inserts newText, and validates the result. If it is valid, it sets the new text as the new contents of the line edit.


--------------------------------
## isClearButtonEnabled()

Return type: bool

Getter of property clearButtonEnabled  .


--------------------------------
## isModified()

Return type: bool

Getter of property modified  .


--------------------------------
## isReadOnly()

Return type: bool

Getter of property readOnly  .


--------------------------------
## isRedoAvailable()

Return type: bool

Getter of property redoAvailable  .


--------------------------------
## isUndoAvailable()

Return type: bool

Getter of property undoAvailable  .


--------------------------------
## maxLength()

Return type: int

Getter of property maxLength  .


--------------------------------
## paste()

Inserts the clipboard’s text at the cursor position, deleting any selected text, providing the line edit is not read-only .

If the end result would be invalid to the current validator , nothing happens.


--------------------------------
## placeholderText()

Return type: str

Getter of property placeholderText  .


--------------------------------
## redo()

Redoes the last operation if redo is available .


--------------------------------
## returnPressed()

This signal is emitted when the Return or Enter key is used.


--------------------------------
## selectAll()

Selects all the text (highlights it) and moves the cursor to the end.


--------------------------------
## selectedText()

Return type: str

Getter of property selectedText  .


--------------------------------
## selectionChanged()

This signal is emitted whenever the selection changes.


--------------------------------
## selectionEnd()

Return type: int

Returns the index of the character directly after the selection in the line edit (or -1 if no text is selected).


--------------------------------
## selectionLength()

Return type: int

Returns the length of the selection.


--------------------------------
## selectionStart()

Return type: int

Returns the index of the first selected character in the line edit (or -1 if no text is selected).


--------------------------------
## setAlignment(flag)

Parameters:

- flag – Combination of AlignmentFlag

Setter of property alignment  .


--------------------------------
## setClearButtonEnabled(enable)

Parameters:

- enable – bool

Setter of property clearButtonEnabled  .


--------------------------------
## setCompleter(completer)

Parameters:

- completer – QCompleter

Sets this line edit to provide auto completions from the completer, c. The completion mode is set using setCompletionMode() .

To use a QCompleter with a QValidator or inputMask , you need to ensure that the model provided to QCompleter contains valid entries. You can use the QSortFilterProxyModel to ensure that the QCompleter ‘s model contains only valid entries.

To remove the completer and disable auto-completion, pass a nullptr.


--------------------------------
## setCursorMoveStyle(style)

Parameters:

- style – CursorMoveStyle

Setter of property cursorMoveStyle  .


--------------------------------
## setCursorPosition(arg__1)

Parameters:

- arg__1 – int

Setter of property cursorPosition  .


--------------------------------
## setDragEnabled(b)

Parameters:

- b – bool

Setter of property dragEnabled  .


--------------------------------
## setEchoMode(arg__1)

Parameters:

- arg__1 – EchoMode

Setter of property echoMode  .


--------------------------------
## setFrame(arg__1)

Parameters:

- arg__1 – bool

Setter of property frame  .


--------------------------------
## setInputMask(inputMask)

Parameters:

- inputMask – str

Setter of property inputMask  .


--------------------------------
## setMaxLength(arg__1)

Parameters:

- arg__1 – int

Setter of property maxLength  .


--------------------------------
## setModified(arg__1)

Parameters:

- arg__1 – bool

Setter of property modified  .


--------------------------------
## setPlaceholderText(arg__1)

Parameters:

- arg__1 – str

Setter of property placeholderText  .


--------------------------------
## setReadOnly(arg__1)

Parameters:

- arg__1 – bool

Setter of property readOnly  .


--------------------------------
## setSelection(arg__1, arg__2)

Parameters:

- arg__1 – int
- arg__2 – int

Selects text from position start and for length characters. Negative lengths are allowed.


--------------------------------
## setText(arg__1)

Parameters:

- arg__1 – str

Setter of property text  .


--------------------------------
## setTextMargins(margins)

Parameters:

- margins – QMargins

Sets the margins around the text inside the frame.


--------------------------------
## setTextMargins(left, top, right, bottom)

Parameters:

- left – int
- top – int
- right – int
- bottom – int

Sets the margins around the text inside the frame to have the sizes left, top, right, and bottom.


--------------------------------
## setValidator(arg__1)

Parameters:

- arg__1 – QValidator

Sets the validator for values of line edit to v.

The line edit’s returnPressed() and editingFinished() signals will only be emitted if v validates the line edit’s content as Acceptable. The user may change the content to any Intermediate value during editing, but will be prevented from editing the text to a value that v validates as Invalid.

This allows you to constrain the text that will be stored when editing is done while leaving users with enough freedom to edit the text from one valid state to another.

To remove the current input validator, pass nullptr. The initial setting is to have no input validator (any input is accepted up to maxLength() ).


--------------------------------
## text()

Return type: str

Getter of property text  .


--------------------------------
## textChanged(arg__1)

Parameters:

- arg__1 – str

This signal is emitted whenever the text changes. The text argument is the new text.

Unlike textEdited() , this signal is also emitted when the text is changed programmatically, for example, by calling setText() .

Notification signal of property text  .


--------------------------------
## textEdited(arg__1)

Parameters:

- arg__1 – str

This signal is emitted whenever the text is edited. The text argument is the new text.

Unlike textChanged() , this signal is not emitted when the text is changed programmatically, for example, by calling setText() .


--------------------------------
## textMargins()

Return type: QMargins

Returns the widget’s text margins.


--------------------------------
## undo()

Undoes the last operation if undo is available . Deselects any current selection, and updates the selection start to the current cursor position.


--------------------------------
## validator()

Return type: QValidator

Returns a pointer to the current input validator, or None if no validator has been set.

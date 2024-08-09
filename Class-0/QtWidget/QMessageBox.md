
[Chinese doc](QMessageBox.CN.md)

# class QMessageBox

The QMessageBox class provides a modal dialog for informing the user or for asking the user a question and receiving an answer.


# Synopsis

## Properties

- [detailedText](#property-detailedtext--str)

    The text to be displayed in the details area.

- [icon](#property-icon--qmessageboxicon)

    The message box’s icon.

- [iconPixmap](#property-iconpixmap--qpixmap)

    The current icon.

- [informativeText](#property-informativetext--str)

    The informative text that provides a fuller description for the message.

- [options](#property-options--combination-of-qabstractfileiconprovideroption)

    Options that affect the look and feel of the dialog.

- [standardButtons](#property-standardbuttons--combination-of-qdialogbuttonboxstandardbutton)

    Collection of standard buttons in the message box.

- [text](#property-text--str)

    The message box text to be displayed.

- [textFormat](#property-textformat--qttextformat)

    The format of the text displayed by the message box.

- [textInteractionFlags](#property-textinteractionflags--combination-of-qttextinteractionflag)


## Methods

- [def \_\_init__()](#initparentnone)

- [def addButton()](#addbuttonbutton)

- [def button()](#buttonwhich)

- [def buttonRole()](#buttonrolebutton)

- [def buttonText()](#buttontextbutton)

- [def buttons()](#buttons)

- [def checkBox()](#checkbox)

- [def clickedButton()](#clickedbutton)

- [def defaultButton()](#defaultbutton)

- [def detailedText()](#detailedtext)

- [def escapeButton()](#escapebutton)

- [def icon()](#icon)

- [def iconPixmap()](#iconpixmap)

- [def informativeText()](#informativetext)

- [def open()](#openreceiver-member)

- [def options()](#options)

- [def removeButton()](#removebuttonbutton)

- [def setButtonText()](#setbuttontextbutton-text)

- [def setCheckBox()](#setcheckboxcb)

- [def setDefaultButton()](#setdefaultbuttonbutton)

- [def setDetailedText()](#setdetailedtexttext)

- [def setEscapeButton()](#setescapebuttonbutton)

- [def setIcon()](#seticonarg__1)

- [def setIconPixmap()](#seticonpixmappixmap)

- [def setInformativeText()](#setinformativetexttext)

- [def setOption()](#setoptionoption-ontrue)

- [def setOptions()](#setoptionsoptions)

- [def setStandardButtons()](#setstandardbuttonsbuttons)

- [def setText()](#settexttext)

- [def setTextFormat()](#settextformatformat)

- [def setTextInteractionFlags()](#settextinteractionflagsflags)

- [def setWindowModality()](#setwindowmodalitywindowmodality)

- [def setWindowTitle()](#setwindowtitletitle)

- [def standardButton()](#standardbuttonbutton)

- [def standardButtons()](#standardbuttons)

- [def testOption()](#testoptionoption)

- [def text()](#text)

- [def textFormat()](#textformat)

- [def textInteractionFlags()](#textinteractionflags)


## Signals

- [def buttonClicked()](#buttonclickedbutton)


## Static functions

- [def about()](#static-aboutparent-title-text)

- [def aboutQt()](#static-aboutqtparent-title)

- [def critical()](#static-criticalparent-title-text-button0-button1)

- [def information()](#static-informationparent-title-text-button0-button1qmessageboxstandardbuttonnobutton)

- [def question()](#static-questionparent-title-text-button0-button1)

- [def standardIcon()](#static-standardiconicon)

- [def warning()](#static-warningparent-title-text-button0-button1)


# Detailed Description

A message box displays a primary text to alert the user to a situation, an informative text to further explain the situation, and an optional detailed text to provide even more data if the user requests it.

A message box can also display an icon and standard buttons for accepting a user response.

Two APIs for using QMessageBox are provided, the property-based API, and the static functions. Calling one of the static functions is the simpler approach, but it is less flexible than using the property-based API, and the result is less informative. Using the property-based API is recommended.


## The Property-based API

To use the property-based API, construct an instance of QMessageBox , set the desired properties, and call exec() to show the message. The simplest configuration is to set only the message text property.

```python
msgBox = QMessageBox()
msgBox.setText("The document has been modified.")
msgBox.exec()
```

The user must click the OK button to dismiss the message box. The rest of the GUI is blocked until the message box is dismissed.

A better approach than just alerting the user to an event is to also ask the user what to do about it.

Set the standard buttons property to the set of buttons you want as the set of user responses. The buttons are specified by combining values from StandardButtons using the bitwise OR operator. The display order for the buttons is platform-dependent. For example, on Windows, Save is displayed to the left of Cancel, whereas on macOS, the order is reversed. Mark one of your standard buttons to be your default button .

The informative text property can be used to add additional context to help the user choose the appropriate action.

```python
msgBox = QMessageBox()
msgBox.setText("The document has been modified.")
msgBox.setInformativeText("Do you want to save your changes?")
msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
msgBox.setDefaultButton(QMessageBox.Save)
ret = msgBox.exec()
```

The exec() slot returns the StandardButtons value of the button that was clicked.

```python
if ret == QMessageBox.Save:
    # Save was clicked
    break
elif ret == QMessageBox.Discard:
    # Don't Save was clicked
    break
elif ret == QMessageBox.Cancel:
    # Cancel was clicked
    break
else:
    # should never be reached
    break
```

To give the user more information to help them choose the appropriate, action, set the detailed text property. Depending on the platform the detailed text , may require the user to click a Show Details… button to be shown.

Clicking the Show Details… button displays the detailed text.


## Rich Text and the Text Format Property

The detailed text property is always interpreted as plain text. The main text and informative text properties can be either plain text or rich text. These strings are interpreted according to the setting of the text format property. The default setting is auto-text.

Note that for some plain text strings containing XML meta-characters, the auto-text rich text detection test may fail causing your plain text string to be interpreted incorrectly as rich text. In these rare cases, use Qt::convertFromPlainText() to convert your plain text string to a visually equivalent rich text string, or set the text format property explicitly with setTextFormat() .


## Severity Levels and the Icon and Pixmap Properties

QMessageBox supports four predefined message severity levels, or message types, which really only differ in the predefined icon they each show. Specify one of the four predefined message types by setting the icon property to one of the predefined icons . The following rules are guidelines:

|             |                                                    |
| ----------- | -------------------------------------------------- |
| Question    | For asking a question during normal operations.    |
| Information | For reporting information about normal operations. |
| Warning     | For reporting non-critical errors.                 |
| Critical    | For reporting critical errors.                     |

Predefined icons are not defined by QMessageBox , but provided by the style. The default value is No Icon . The message boxes are otherwise the same for all cases. When using a standard icon, use the one recommended in the table, or use the one recommended by the style guidelines for your platform. If none of the standard icons is right for your message box, you can use a custom icon by setting the icon pixmap property instead of setting the icon property.

In summary, to set an icon, use either setIcon() for one of the standard icons, or setIconPixmap() for a custom icon.


## The Static Functions API

Building message boxes with the static functions API, although convenient, is less flexible than using the property-based API, because the static function signatures lack parameters for setting the informative text and detailed text properties. One work-around for this has been to use the title parameter as the message box main text and the text parameter as the message box informative text. Because this has the obvious drawback of making a less readable message box, platform guidelines do not recommend it. The Microsoft Windows User Interface Guidelines recommend using the application name as the window's title , which means that if you have an informative text in addition to your main text, you must concatenate it to the text parameter.

Note that the static function signatures have changed with respect to their button parameters, which are now used to set the standard buttons and the default button .

Static functions are available for creating information() , question() , warning() , and critical() message boxes.

```python
ret = QMessageBox.warning(self, tr("My Application"),()
                               tr("The document has been modified.\n"
                                  "Do you want to save your changes?"),
                               QMessageBox.Save | QMessageBox.Discard
                               | QMessageBox.Cancel,
                               QMessageBox.Save)
```

The Standard Dialogs example shows how to use QMessageBox and the other built-in Qt dialogs.


## Advanced Usage

If the standard buttons are not flexible enough for your message box, you can use the addButton() overload that takes a text and a ButtonRole to add custom buttons. The ButtonRole is used by QMessageBox to determine the ordering of the buttons on screen (which varies according to the platform). You can test the value of clickedButton() after calling exec() . For example,

```bash
msgBox = QMessageBox()
connectButton = msgBox.addButton(tr("Connect"), QMessageBox.ActionRole)
abortButton = msgBox.addButton(QMessageBox.Abort)
msgBox.exec()
if msgBox.clickedButton() == connectButton:
    # connect
 elif msgBox.clickedButton() == abortButton:
    # abort
```


## Default and Escape Keys

The default button (i.e., the button activated when Enter is pressed) can be specified using setDefaultButton() . If a default button is not specified, QMessageBox tries to find one based on the button roles of the buttons used in the message box.

The escape button (the button activated when Esc is pressed) can be specified using setEscapeButton() . If an escape button is not specified, QMessageBox tries to find one using these rules:

1. If there is only one button, it is the button activated when Esc is pressed.

2. If there is a Cancel button, it is the button activated when Esc is pressed.

3. If there is exactly one button having either the Reject role or the the No role , it is the button activated when Esc is pressed.

When an escape button can’t be determined using these rules, pressing Esc has no effect.


--------------------------------
## class Option

| Constant                               | Description                                               |
| -------------------------------------- | --------------------------------------------------------- |
| QMessageBox.Option.DontUseNativeDialog | (inherits enum.Flag) Don’t use the native message dialog. |

New in version 6.6.


--------------------------------
## class Icon

This enum has the following values:

| Constant                | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| QMessageBox.NoIcon      | the message box does not have any icon.                                  |
| QMessageBox.Question    | an icon indicating that the message is asking a question.                |
| QMessageBox.Information | an icon indicating that the message is nothing out of the ordinary.      |
| QMessageBox.Warning     | an icon indicating that the message is a warning, but can be dealt with. |
| QMessageBox.Critical    | an icon indicating that the message represents a critical problem.       |


--------------------------------
## class ButtonRole

This enum describes the roles that can be used to describe buttons in the button box. Combinations of these roles are as flags used to describe different aspects of their behavior.

| Constant                    | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| QMessageBox.InvalidRole     | The button is invalid.                                                |
| QMessageBox.AcceptRole      | Clicking the button causes the dialog to be accepted (e.g. OK).       |
| QMessageBox.RejectRole      | Clicking the button causes the dialog to be rejected (e.g. Cancel).   |
| QMessageBox.DestructiveRole | Clicking the button causes a destructive change (e.g. for Discarding Changes) and closes the dialog. |
| QMessageBox.ActionRole      | Clicking the button causes changes to the elements within the dialog. |
| QMessageBox.HelpRole        | The button can be clicked to request help.                            |
| QMessageBox.YesRole         | The button is a “Yes”-like button.                                    |
| QMessageBox.NoRole          | The button is a “No”-like button.                                     |
| QMessageBox.ApplyRole       | The button applies current changes.                                   |
| QMessageBox.ResetRole       | The button resets the dialog’s fields to default values.              |


--------------------------------
## class StandardButton

(inherits enum.IntFlag) These enums describe flags for standard buttons. Each button has a defined ButtonRole .

| Constant                    | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| QMessageBox.Ok              | An “OK” button defined with the AcceptRole .             |
| QMessageBox.Open            | An “Open” button defined with the AcceptRole .           |
| QMessageBox.Save            | A “Save” button defined with the AcceptRole .            |
| QMessageBox.Cancel          | A “Cancel” button defined with the RejectRole .          |
| QMessageBox.Close           | A “Close” button defined with the RejectRole .           |
| QMessageBox.Discard         | A “Discard” or “Don’t Save” button, depending on the platform, defined with the DestructiveRole . |
| QMessageBox.Apply           | An “Apply” button defined with the ApplyRole .           |
| QMessageBox.Reset           | A “Reset” button defined with the ResetRole .            |
| QMessageBox.RestoreDefaults | A “Restore Defaults” button defined with the ResetRole . |
| QMessageBox.Help            | A “Help” button defined with the HelpRole .              |
| QMessageBox.SaveAll         | A “Save All” button defined with the AcceptRole .        |
| QMessageBox.Yes             | A “Yes” button defined with the YesRole .                |
| QMessageBox.YesToAll        | A “Yes to All” button defined with the YesRole .         |
| QMessageBox.No              | A “No” button defined with the NoRole .                  |
| QMessageBox.NoToAll         | A “No to All” button defined with the NoRole .           |
| QMessageBox.Abort           | An “Abort” button defined with the RejectRole .          |
| QMessageBox.Retry           | A “Retry” button defined with the AcceptRole .           |
| QMessageBox.Ignore          | An “Ignore” button defined with the AcceptRole .         |
| QMessageBox.NoButton        | An invalid button.                                       |

The following values are obsolete:

| Constant               | Description                      |
| ---------------------- | -------------------------------- |
| QMessageBox.YesAll     | Use YesToAll instead.            |
| QMessageBox.NoAll      | Use NoToAll instead.             |
| QMessageBox.Default    | Use the defaultButton argument of information() , warning() , etc. instead, or call setDefaultButton() . |
| QMessageBox.Escape     | Call setEscapeButton() instead.  |
| QMessageBox.FlagMask   |                                  |
| QMessageBox.ButtonMask |                                  |


--------------------------------
## property detailedText : str

This property holds the text to be displayed in the details area..

The text will be interpreted as a plain text.

By default, this property contains an empty string.

Access functions:

- detailedText()
- setDetailedText()


--------------------------------
## property icon : QMessageBox.Icon

This property holds the message box’s icon.

The icon of the message box can be specified with one of the values:

- NoIcon
- Question
- Information
- Warning
- Critical

The default is NoIcon .

The pixmap used to display the actual icon depends on the current GUI style . You can also set a custom pixmap for the icon by setting the icon pixmap property.

Access functions:

- icon()
- setIcon()


--------------------------------
## property iconPixmap : QPixmap

This property holds the current icon.

The icon currently used by the message box. Note that it’s often hard to draw one pixmap that looks appropriate in all GUI styles; you may want to supply a different pixmap for each platform.

By default, this property is undefined.

Access functions:

- iconPixmap()
- setIconPixmap()


--------------------------------
## property informativeText : str

This property holds the informative text that provides a fuller description for the message.

Informative text can be used to expand upon the text() to give more information to the user, for example describing the consequences of the situation, or suggestion alternative solutions.

By default, this property contains an empty string.

Access functions:

- informativeText()
- setInformativeText()


--------------------------------
## property options : Combination of QAbstractFileIconProvider.Option

This property holds Options that affect the look and feel of the dialog..

By default, these options are disabled.

The option DontUseNativeDialog should be set before changing dialog properties or showing the dialog.

Setting options while the dialog is visible is not guaranteed to have an immediate effect on the dialog.

Setting options after changing other properties may cause these values to have no effect.

Access functions:

- options()
- setOptions()


--------------------------------
## property standardButtons : Combination of QDialogButtonBox.StandardButton

This property holds collection of standard buttons in the message box.

This property controls which standard buttons are used by the message box.

By default, this property contains no standard buttons.

Access functions:

- standardButtons()
- setStandardButtons()


--------------------------------
## property text : str

This property holds the message box text to be displayed..

The text should be a brief sentence or phrase that describes the situation, ideally formulated as a neutral statement, or a call-to-action question.

The text will be interpreted either as a plain text or as rich text, depending on the text format setting ( textFormat ). The default setting is Qt::AutoText, i.e., the message box will try to auto-detect the format of the text.

The default value of this property is an empty string.

Access functions:

- text()
- setText()


--------------------------------
## property textFormat : Qt.TextFormat

This property holds the format of the text displayed by the message box.

The current text format used by the message box. See the Qt::TextFormat enum for an explanation of the possible options.

The default format is Qt::AutoText.

Access functions:

- textFormat()
- setTextFormat()


--------------------------------
## property textInteractionFlags : Combination of Qt.TextInteractionFlag

Specifies how the label of the message box should interact with user input.

The default value depends on the style.

Access functions:

- textInteractionFlags()
- setTextInteractionFlags()


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs an application modal message box with no text and no buttons. parent is passed to the QDialog constructor.

The window modality can be overridden via setWindowModality() before calling show() .

On macOS, if you want your message box to appear as a Qt::Sheet of its parent, set the message box’s window modality to Qt::WindowModal or use open() . Otherwise, the message box will be a standard dialog.


--------------------------------
## __init__(icon, title, text[, buttons=QMessageBox.StandardButton.NoButton[, parent=None[, flags=Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint]]])

Parameters:

- icon – Icon
- title – str
- text – str
- buttons – Combination of StandardButton
- parent – QWidget
- flags – Combination of WindowType

Constructs an application modal message box with the given icon, title, text, and standard buttons. Standard or custom buttons can be added at any time using addButton() . The parent and f arguments are passed to the QDialog constructor.

The window modality can be overridden via setWindowModality() before calling show() .

On macOS, if parent is not None and you want your message box to appear as a Qt::Sheet of that parent, set the message box’s window modality to Qt::WindowModal (default). Otherwise, the message box will be a standard dialog.


--------------------------------
## static about(parent, title, text)

Parameters:

- parent – QWidget
- title – str
- text – str

Displays a simple about box with title title and text text. The about box’s parent is parent.

about() looks for a suitable icon in four locations:

1. It prefers parent->icon() if that exists.

2. If not, it tries the top-level widget containing parent.

3. If that fails, it tries the PySide6.QtWidgets.QApplication.activeWindow()

4. As a last resort it uses the Information icon.

The about box has a single button labelled “OK”.

On macOS, the about box is popped up as a modeless window; on other platforms, it is currently application modal.


--------------------------------
## static aboutQt(parent[, title=""])

Parameters:

- parent – QWidget
- title – str

Displays a simple message box about Qt, with the given title and centered over parent (if parent is not None). The message includes the version number of Qt being used by the application.

This is useful for inclusion in the Help menu of an application, as shown in the Menus example.

QApplication provides this functionality as a slot.

On macOS, the aboutQt box is popped up as a modeless window; on other platforms, it is currently application modal.


--------------------------------
## addButton(button, role)

Parameters:

- button – QAbstractButton
- role – ButtonRole

Adds the given button to the message box with the specified role.


--------------------------------
## addButton(button)

Parameters:

- button – StandardButton

Return type: QPushButton

This is an overloaded function.

Adds a standard button to the message box if it is valid to do so, and returns the push button.


--------------------------------
## addButton(text, role)

Parameters:

- text – str
- role – ButtonRole

Return type: QPushButton

This is an overloaded function.

Creates a button with the given text, adds it to the message box for the specified role, and returns it.


--------------------------------
## button(which)

Parameters:

- which – StandardButton

Return type: QAbstractButton

Returns a pointer corresponding to the standard button which, or None if the standard button doesn’t exist in this message box.


--------------------------------
## buttonClicked(button)

Parameters:

- button – QAbstractButton

This signal is emitted whenever a button is clicked inside the QMessageBox . The button that was clicked in returned in button.


--------------------------------
## buttonRole(button)

Parameters:

- button – QAbstractButton

Return type: ButtonRole

Returns the button role for the specified button. This function returns InvalidRole if button is None or has not been added to the message box.


--------------------------------
## buttonText(button)

Parameters:

- button – int

Return type: str

Returns the text of the message box button button, or an empty string if the message box does not contain the button.

Use button() and text() instead.


--------------------------------
## buttons()

Return type: list of QAbstractButton

Returns a list of all the buttons that have been added to the message box.


--------------------------------
## checkBox()

Return type: QCheckBox

Returns the checkbox shown on the dialog. This is None if no checkbox is set.


--------------------------------
## clickedButton()

Return type: QAbstractButton

Returns the button that was clicked by the user, or None if the user hit the Esc key and no escape button was set.

If exec() hasn’t been called yet, returns nullptr.

Example:

```python
messageBox = QMessageBox(self)
disconnectButton =
      messageBox.addButton(tr("Disconnect"), QMessageBox.ActionRole)
...
messageBox.exec()
if messageBox.clickedButton() == disconnectButton:
    ...
```


--------------------------------
## static critical(parent, title, text, button0, button1)

Parameters:

- parent – QWidget
- title – str
- text – str
- button0 – StandardButton
- button1 – StandardButton

Return type: int

Opens a critical message box with the given title and text in front of the specified parent widget.

The standard buttons are added to the message box. defaultButton specifies the button used when Enter is pressed. defaultButton must refer to a button that was given in buttons. If defaultButton is NoButton , QMessageBox chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the escape button is returned.

The message box is an application modal dialog box.


--------------------------------
## static critical(parent, title, text[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])

Parameters:

- parent – QWidget
- title – str
- text – str
- buttons – Combination of StandardButton
- defaultButton – StandardButton

Return type: StandardButton

Opens a critical message box with the given title and text in front of the specified parent widget.

The standard buttons are added to the message box. defaultButton specifies the button used when Enter is pressed. defaultButton must refer to a button that was given in buttons. If defaultButton is NoButton , QMessageBox chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the escape button is returned.

The message box is an application modal dialog box.


--------------------------------
## defaultButton()

Return type: QPushButton

Returns the button that should be the message box’s default button . Returns nullptr if no default button was set.


--------------------------------
## detailedText()

Return type: str

Getter of property detailedText  .

--------------------------------
## escapeButton()

Return type: QAbstractButton

Returns the button that is activated when escape is pressed.

By default, QMessageBox attempts to automatically detect an escape button as follows:

If there is only one button, it is made the escape button.

If there is a Cancel button, it is made the escape button.

On macOS only, if there is exactly one button with the role RejectRole , it is made the escape button.

When an escape button could not be automatically detected, pressing Esc has no effect.


--------------------------------
## icon()

Return type: Icon

Getter of property icon  .


--------------------------------
## iconPixmap()

Return type: QPixmap

Getter of property iconPixmap  .


--------------------------------
## static information(parent, title, text[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])

Parameters:

- parent – QWidget
- title – str
- text – str
- buttons – Combination of StandardButton
- defaultButton – StandardButton

Return type: StandardButton

Opens an information message box with the given title and text in front of the specified parent widget.

The standard buttons are added to the message box. defaultButton specifies the button used when Enter is pressed. defaultButton must refer to a button that was given in buttons. If defaultButton is NoButton , QMessageBox chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the escape button is returned.

The message box is an application modal dialog box.


--------------------------------
## static information(parent, title, text, button0[, button1=QMessageBox.StandardButton.NoButton])

Parameters:

- parent – QWidget
- title – str
- text – str
- button0 – StandardButton
- button1 – StandardButton

Return type: StandardButton

Opens an information message box with the given title and text in front of the specified parent widget.

The standard buttons are added to the message box. defaultButton specifies the button used when Enter is pressed. defaultButton must refer to a button that was given in buttons. If defaultButton is NoButton , QMessageBox chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the escape button is returned.

The message box is an application modal dialog box.


--------------------------------
## informativeText()

Return type: str

Getter of property informativeText  .


--------------------------------
## open(receiver, member)

Parameters:

- receiver – QObject
- member – str

Opens the dialog and connects its finished() or buttonClicked() signal to the slot specified by receiver and member. If the slot in member has a pointer for its first parameter the connection is to buttonClicked() , otherwise the connection is to finished() .

The signal will be disconnected from the slot when the dialog is closed.


--------------------------------
## options()

Return type: Combination of Option


--------------------------------
## static question(parent, title, text[, buttons=QMessageBox.StandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)[, defaultButton=QMessageBox.StandardButton.NoButton]])

Parameters:

- parent – QWidget
- title – str
- text – str
- buttons – Combination of StandardButton
- defaultButton – StandardButton

Return type: StandardButton

Opens a question message box with the given title and text in front of the specified parent widget.

The standard buttons are added to the message box. defaultButton specifies the button used when Enter is pressed. defaultButton must refer to a button that was given in buttons. If defaultButton is NoButton , QMessageBox chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the escape button is returned.

The message box is an application modal dialog box.


--------------------------------
## static question(parent, title, text, button0, button1)

Parameters:

- parent – QWidget
- title – str
- text – str
- button0 – StandardButton
- button1 – StandardButton

Return type: int

Opens a question message box with the given title and text in front of the specified parent widget.

The standard buttons are added to the message box. defaultButton specifies the button used when Enter is pressed. defaultButton must refer to a button that was given in buttons. If defaultButton is NoButton , QMessageBox chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the escape button is returned.

The message box is an application modal dialog box.


--------------------------------
## removeButton(button)

Parameters:

- button – QAbstractButton

Removes button from the button box without deleting it.


--------------------------------
## setButtonText(button, text)

Parameters:

- button – int
- text – str

Sets the text of the message box button button to text. Setting the text of a button that is not in the message box is silently ignored.

Use addButton() instead.


--------------------------------
## setCheckBox(cb)

Parameters:

- cb – QCheckBox

Sets the checkbox cb on the message dialog. The message box takes ownership of the checkbox. The argument cb can be None to remove an existing checkbox from the message box.


--------------------------------
## setDefaultButton(button)

Parameters:

- button – StandardButton

Sets the message box’s default button to button.


--------------------------------
## setDefaultButton(button)

Parameters:

- button – QPushButton

Sets the message box’s default button to button.


--------------------------------
## setDetailedText(text)

Parameters:

- text – str

Setter of property detailedText  .


--------------------------------
## setEscapeButton(button)

Parameters:

- button – QAbstractButton

Sets the button that gets activated when the Escape key is pressed to button.


--------------------------------
## setEscapeButton(button)

Parameters:

- button – StandardButton

Sets the buttons that gets activated when the Escape key is pressed to button.


--------------------------------
## setIcon(arg__1)

Parameters:

- arg__1 – Icon

Setter of property icon  .


--------------------------------
## setIconPixmap(pixmap)

Parameters:

- pixmap – QPixmap

Setter of property iconPixmap  .


--------------------------------
## setInformativeText(text)

Parameters:

- text – str

Setter of property informativeText  .


--------------------------------
## setOption(option[, on=true])

Parameters:

- option – Option
- on – bool

Sets the given option to be enabled if on is true; otherwise, clears the given option.

Options (particularly the DontUseNativeDialog option) should be set before showing the dialog.

Setting options while the dialog is visible is not guaranteed to have an immediate effect on the dialog.

Setting options after changing other properties may cause these values to have no effect.


--------------------------------
## setOptions(options)

Parameters:

- options – Combination of Option


--------------------------------
## setStandardButtons(buttons)

Parameters:

- buttons – Combination of StandardButton


--------------------------------
## setText(text)

Parameters:

- text – str

Setter of property text  .


--------------------------------
## setTextFormat(format)

Parameters:

- format – TextFormat

Setter of property textFormat  .


--------------------------------
## setTextInteractionFlags(flags)

Parameters:

- flags – Combination of TextInteractionFlag

Setter of property textInteractionFlags  .


--------------------------------
## setWindowModality(windowModality)

Parameters:

- windowModality – WindowModality

This function shadows setWindowModality() .

Sets the modality of the message box to windowModality.

On macOS, if the modality is set to Qt::WindowModal and the message box has a parent, then the message box will be a Qt::Sheet, otherwise the message box will be a standard dialog.


--------------------------------
## setWindowTitle(title)

Parameters:

- title – str

This function shadows setWindowTitle() .

Sets the title of the message box to title. On macOS, the window title is ignored (as required by the macOS Guidelines).


--------------------------------
## standardButton(button)

Parameters:

- button – QAbstractButton

Return type: StandardButton

Returns the standard button enum value corresponding to the given button, or NoButton if the given button isn’t a standard button.


--------------------------------
## standardButtons()

Return type: Combination of StandardButton


--------------------------------
## static standardIcon(icon)

Parameters:

- icon – Icon

Return type: QPixmap

Returns the pixmap used for a standard icon. This allows the pixmaps to be used in more complex message boxes. icon specifies the required icon, e.g. Question , Information , Warning or Critical .

Call standardIcon() with SP_MessageBoxInformation etc. instead.


--------------------------------
## testOption(option)

Parameters:

- option – Option

Return type: bool

Returns true if the given option is enabled; otherwise, returns false.


--------------------------------
## text()

Return type: str

Getter of property text  .


--------------------------------
## textFormat()

Return type: TextFormat

Getter of property textFormat  .


--------------------------------
## textInteractionFlags()

Return type: Combination of TextInteractionFlag

Getter of property textInteractionFlags  .


--------------------------------
## static warning(parent, title, text[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])

Parameters:

- parent – QWidget
- title – str
- text – str
- buttons – Combination of StandardButton
- defaultButton – StandardButton

Return type: StandardButton

Opens a warning message box with the given title and text in front of the specified parent widget.

The standard buttons are added to the message box. defaultButton specifies the button used when Enter is pressed. defaultButton must refer to a button that was given in buttons. If defaultButton is NoButton , QMessageBox chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the escape button is returned.

The message box is an application modal dialog box.


--------------------------------
## static warning(parent, title, text, button0, button1)

Parameters:

- parent – QWidget
- title – str
- text – str
- button0 – StandardButton
- button1 – StandardButton

Return type: int

Opens a warning message box with the given title and text in front of the specified parent widget.

The standard buttons are added to the message box. defaultButton specifies the button used when Enter is pressed. defaultButton must refer to a button that was given in buttons. If defaultButton is NoButton , QMessageBox chooses a suitable default automatically.

Returns the identity of the standard button that was clicked. If Esc was pressed instead, the escape button is returned.

The message box is an application modal dialog box.

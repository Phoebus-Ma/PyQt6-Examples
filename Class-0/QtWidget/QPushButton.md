
[Chinese Doc](QPushButton.CN.md)

# class QPushButton

The QPushButton widget provides a command button.


# Synopsis

## Properties

- [autoDefault](#property-autodefault--bool)

    Whether the push button is an auto default button.

- [default](#property-default--bool)

    Whether the push button is the default button.

- [flat](#property-flat--bool)

    Whether the button border is raised.


## Methods

- [def \_\_init__()](#initparentnone)

- [def autoDefault()](#autodefault)

- [def isDefault()](#isdefault)

- [def isFlat()](#isflat)

- [def menu()](#menu)

- [def setAutoDefault()](#setautodefaultarg__1)

- [def setDefault()](#setdefaultarg__1)

- [def setFlat()](#setflatarg__1)

- [def setMenu()](#setmenumenu)


## Virtual methods

- [def initStyleOption()](#initstyleoptionoption)


## Slots

- [def showMenu()](#showmenu)


# Detailed Description

The push button, or command button, is perhaps the most commonly used widget in any graphical user interface. Push (click) a button to command the computer to perform some action, or to answer a question. Typical buttons are OK, Apply, Cancel, Close, Yes, No and Help.

A command button is rectangular and typically displays a text label describing its action. A shortcut key can be specified by preceding the preferred character with an ampersand in the text. For example:

```python
button = QPushButton("Download", self)
```

In this example the shortcut is Alt+D. See the QShortcut documentation for details (to display an actual ampersand, use ‘&&’).

Push buttons display a textual label, and optionally a small icon. These can be set using the constructors and changed later using setText() and setIcon() . If the button is disabled, the appearance of the text and icon will be manipulated with respect to the GUI style to make the button look “disabled”.

A push button emits the signal clicked() when it is activated by the mouse, the Spacebar or by a keyboard shortcut. Connect to this signal to perform the button’s action. Push buttons also provide less commonly used signals, for example pressed() and released() .

Command buttons in dialogs are by default auto-default buttons, i.e., they become the default push button automatically when they receive the keyboard input focus. A default button is a push button that is activated when the user presses the Enter or Return key in a dialog. You can change this with setAutoDefault() . Note that auto-default buttons reserve a little extra space which is necessary to draw a default-button indicator. If you do not want this space around your buttons, call setAutoDefault (false).

Being so central, the button widget has grown to accommodate a great many variations in the past decade. The Microsoft style guide now shows about ten different states of Windows push buttons and the text implies that there are dozens more when all the combinations of features are taken into consideration.

The most important modes or states are:

- Available or not (grayed out, disabled).

- Standard push button, toggling push button or menu button.

- On or off (only for toggling push buttons).

- Default or normal. The default button in a dialog can generally be “clicked” using the Enter or Return key.

- Auto-repeat or not.

- Pressed down or not.

As a general rule, use a push button when the application or dialog window performs an action when the user clicks on it (such as Apply, Cancel, Close and Help) and when the widget is supposed to have a wide, rectangular shape with a text label. Small, typically square buttons that change the state of the window rather than performing an action (such as the buttons in the top-right corner of the QFileDialog ) are not command buttons, but tool buttons. Qt provides a special class ( QToolButton ) for these buttons.

If you need toggle behavior (see setCheckable() ) or a button that auto-repeats the activation signal when being pushed down like the arrows in a scroll bar (see setAutoRepeat() ), a command button is probably not what you want. When in doubt, use a tool button.

A variation of a command button is a menu button. These provide not just one command, but several, since when they are clicked they pop up a menu of options. Use the method setMenu() to associate a popup menu with a push button.

Other classes of buttons are option buttons (see QRadioButton ) and check boxes (see QCheckBox ).

In Qt, the QAbstractButton base class provides most of the modes and other API, and QPushButton provides GUI logic. See QAbstractButton for more information about the API.


--------------------------------
## property autoDefault : bool

This property holds whether the push button is an auto default button.

If this property is set to true then the push button is an auto default button.

In some GUI styles a default button is drawn with an extra frame around it, up to 3 pixels or more. Qt automatically keeps this space free around auto-default buttons, i.e., auto-default buttons may have a slightly larger size hint.

This property’s default is true for buttons that have a QDialog parent; otherwise it defaults to false.

See the default property for details of how default and auto-default interact.

Access functions:

- autoDefault()
- setAutoDefault()


--------------------------------
## property default : bool

This property holds whether the push button is the default button.

Default and autodefault buttons decide what happens when the user presses enter in a dialog.

A button with this property set to true (i.e., the dialog’s default button,) will automatically be pressed when the user presses enter, with one exception: if an autoDefault button currently has focus, the autoDefault button is pressed. When the dialog has autoDefault buttons but no default button, pressing enter will press either the autoDefault button that currently has focus, or if no button has focus, the next autoDefault button in the focus chain.

In a dialog, only one push button at a time can be the default button. This button is then displayed with an additional frame (depending on the GUI style).

The default button behavior is provided only in dialogs. Buttons can always be clicked from the keyboard by pressing Spacebar when the button has focus.

If the default property is set to false on the current default button while the dialog is visible, a new default will automatically be assigned the next time a push button in the dialog receives focus.

This property’s default is false.

Access functions:

- isDefault()
- setDefault()


--------------------------------
## property flat : bool

This property holds whether the button border is raised.

This property’s default is false. If this property is set, most styles will not paint the button background unless the button is being pressed. setAutoFillBackground() can be used to ensure that the background is filled using the QPalette::Button brush.

Access functions:

- isFlat()
- setFlat()


--------------------------------
## __init__([parent=None])

PARAMETERS:

- parent – QWidget

Constructs a push button with no text and a parent.


--------------------------------
## __init__(icon, text[, parent=None])

PARAMETERS:

- icon – QIcon
- text – str
- parent – QWidget

Constructs a push button with an icon and a text, and a parent.

Note that you can also pass a QPixmap object as an icon (thanks to the implicit type conversion provided by C++).


--------------------------------
## __init__(text[, parent=None])

PARAMETERS:

- text – str
- parent – QWidget

Constructs a push button with the parent parent and the text text.


--------------------------------
## autoDefault()

RETURN TYPE: bool

Getter of property autoDefault.


--------------------------------
## initStyleOption(option)

PARAMETERS:

- option – QStyleOptionButton

Initialize option with the values from this QPushButton . This method is useful for subclasses when they need a QStyleOptionButton , but don’t want to fill in all the information themselves.


--------------------------------
## isDefault()

RETURN TYPE: bool

Getter of property default.


--------------------------------
## isFlat()

RETURN TYPE: bool

Getter of property flat.


--------------------------------
## menu()

RETURN TYPE: QMenu

Returns the button’s associated popup menu or None if no popup menu has been set.


--------------------------------
## setAutoDefault(arg__1)

PARAMETERS:

- arg__1 – bool

Setter of property autoDefault.


--------------------------------
## setDefault(arg__1)

PARAMETERS:

- arg__1 – bool

Setter of property default.


--------------------------------
## setFlat(arg__1)

PARAMETERS:

- arg__1 – bool

Setter of property flat.


--------------------------------
## setMenu(menu)

PARAMETERS:

- menu – QMenu

Associates the popup menu menu with this push button. This turns the button into a menu button, which in some styles will produce a small triangle to the right of the button’s text.

Ownership of the menu is not transferred to the push button.

A push button with popup menus shown in the Fusion widget style .


--------------------------------
## showMenu()

Shows (pops up) the associated popup menu. If there is no such menu, this function does nothing. This function does not return until the popup menu has been closed by the user.

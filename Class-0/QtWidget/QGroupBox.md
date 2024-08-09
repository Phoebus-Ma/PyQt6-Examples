
[Chinese doc](QGroupBox.CN.md)

# class QGroupBox

The QGroupBox widget provides a group box frame with a title.


# Synopsis

## Properties

- [alignment](#property-alignment--combination-of-qtalignmentflag)

    The alignment of the group box title.

- [checkable](#property-checkable--bool)

    Whether the group box has a checkbox in its title.

- [checked](#property-checked--bool)

    Whether the group box is checked.

- [flat](#property-flat--bool)

    Whether the group box is painted flat or has a frame.

- [title](#property-title--str)

    The group box title text.


## Methods

- [def \_\_init__()](#initparentnone)

- [def alignment()](#alignment)

- [def isCheckable()](#ischeckable)

- [def isChecked()](#ischecked)

- [def isFlat()](#isflat)

- [def setAlignment()](#setalignmentalignment)

- [def setCheckable()](#setcheckablecheckable)

- [def setFlat()](#setflatflat)

- [def setTitle()](#settitletitle)

- [def title()](#title)


## Virtual methods

- [def initStyleOption()](#initstyleoptionoption)


## Slots

- [def setChecked()](#setcheckedchecked)


## Signals

- [def clicked()](#clickedcheckedfalse)

- [def toggled()](#toggledarg__1)


# Detailed Description

A group box provides a frame, a title on top, a keyboard shortcut, and displays various other widgets inside itself. The keyboard shortcut moves keyboard focus to one of the group box’s child widgets.

QGroupBox also lets you set the title (normally set in the constructor) and the title’s alignment . Group boxes can be checkable . Child widgets in checkable group boxes are enabled or disabled depending on whether or not the group box is checked .

You can minimize the space consumption of a group box by enabling the flat property. In most styles , enabling this property results in the removal of the left, right and bottom edges of the frame.

QGroupBox doesn’t automatically lay out the child widgets (which are often QCheckBox es or QRadioButton s but can be any widgets). The following example shows how we can set up a QGroupBox with a layout:

```bash
groupBox = QGroupBox(tr("Exclusive Radio Buttons"))
radio1 = QRadioButton(tr("Radio button 1"))
radio2 = QRadioButton(tr("Radio button 2"))
radio3 = QRadioButton(tr("Radio button 3"))
radio1.setChecked(True)
```


--------------------------------
## property alignment : Combination of Qt.AlignmentFlag

This property holds the alignment of the group box title..

Most styles place the title at the top of the frame. The horizontal alignment of the title can be specified using single values from the following list:

- Qt::AlignLeft aligns the title text with the left-hand side of the group box.
- Qt::AlignRight aligns the title text with the right-hand side of the group box.
- Qt::AlignHCenter aligns the title text with the horizontal center of the group box.

The default alignment is Qt::AlignLeft.

Access functions:

- alignment()
- setAlignment()


--------------------------------
## property checkable : bool

This property holds whether the group box has a checkbox in its title.

If this property is true, the group box displays its title using a checkbox in place of an ordinary label. If the checkbox is checked, the group box’s children are enabled; otherwise, they are disabled and inaccessible.

By default, group boxes are not checkable.

If this property is enabled for a group box, it will also be initially checked to ensure that its contents are enabled.

Access functions:

- isCheckable()
- setCheckable()


--------------------------------
## property checked : bool

This property holds whether the group box is checked.

If the group box is checkable, it is displayed with a check box. If the check box is checked, the group box’s children are enabled; otherwise, the children are disabled and are inaccessible to the user.

By default, checkable group boxes are also checked.

Access functions:

- isChecked()
- setChecked()
- Signal toggled()


--------------------------------
## property flat : bool

This property holds whether the group box is painted flat or has a frame.

A group box usually consists of a surrounding frame with a title at the top. If this property is enabled, only the top part of the frame is drawn in most styles; otherwise, the whole frame is drawn.

By default, this property is disabled, i.e., group boxes are not flat unless explicitly specified.

Access functions:

- isFlat()
- setFlat()


--------------------------------
## property title : str

This property holds the group box title text.

The group box title text will have a keyboard shortcut if the title contains an ampersand (’&’) followed by a letter.

```python
g.setTitle("User information")
```

In the example above, Alt+U moves the keyboard focus to the group box. See the QShortcut documentation for details (to display an actual ampersand, use ‘&&’).

There is no default title text.

Access functions:

- title()
- setTitle()


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs a group box widget with the given parent but with no title.


--------------------------------
## __init__(title[, parent=None])

Parameters:

- title – str
- parent – QWidget

Constructs a group box with the given title and parent.


--------------------------------
## alignment()

Return type: Combination of AlignmentFlag

Getter of property alignment  .


--------------------------------
## clicked([checked=false])

Parameters:

- checked – bool

This signal is emitted when the check box is activated (i.e., pressed down then released while the mouse cursor is inside the button), or when the shortcut key is typed. Notably, this signal is not emitted if you call setChecked() .

If the check box is checked, checked is true; it is false if the check box is unchecked.


--------------------------------
## initStyleOption(option)

Parameters:

- option – QStyleOptionGroupBox

Initialize option with the values from this QGroupBox . This method is useful for subclasses when they need a QStyleOptionGroupBox , but don’t want to fill in all the information themselves.


--------------------------------
## isCheckable()

Return type: bool

Getter of property checkable  .


--------------------------------
## isChecked()

Return type: bool

Getter of property checked  .


--------------------------------
## isFlat()

Return type: bool

Getter of property flat  .


--------------------------------
## setAlignment(alignment)

Parameters:

- alignment – int


--------------------------------
## setCheckable(checkable)

Parameters:

- checkable – bool

Setter of property checkable  .


--------------------------------
## setChecked(checked)

Parameters:

- checked – bool

Setter of property checked  .


--------------------------------
## setFlat(flat)

Parameters:

- flat – bool

Setter of property flat  .


--------------------------------
## setTitle(title)

Parameters:

- title – str

Setter of property title  .


--------------------------------
## title()

Return type: str

Getter of property title  .


--------------------------------
## toggled(arg__1)

Parameters:

- arg__1 – bool

If the group box is checkable, this signal is emitted when the check box is toggled. on is true if the check box is checked; otherwise, it is false.

Notification signal of property checked  .

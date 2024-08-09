
[Chinese doc](QRadioButton.CN.md)

# class QRadioButton

The QRadioButton widget provides a radio button with a text label.


# Synopsis

## Methods

- [def \_\_init__()](#initparentnone)


## Virtual methods

- [def initStyleOption()](#initstyleoptionbutton)


## Detailed Description

A QRadioButton is an option button that can be switched on (checked) or off (unchecked). Radio buttons typically present the user with a “one of many” choice. In a group of radio buttons, only one radio button at a time can be checked; if the user selects another button, the previously selected button is switched off.

Radio buttons are autoExclusive by default. If auto-exclusive is enabled, radio buttons that belong to the same parent widget behave as if they were part of the same exclusive button group. If you need multiple exclusive button groups for radio buttons that belong to the same parent widget, put them into a QButtonGroup .

Whenever a button is switched on or off, it emits the toggled() signal. Connect to this signal if you want to trigger an action each time the button changes state. Use isChecked() to see if a particular button is selected.

Just like QPushButton , a radio button displays text, and optionally a small icon. The icon is set with setIcon() . The text can be set in the constructor or with setText() . A shortcut key can be specified by preceding the preferred character with an ampersand in the text. For example:

```python
button = QRadioButton("Search from the cursor", self)
```

In this example the shortcut is Alt+c. See the QShortcut documentation for details. To display an actual ampersand, use ‘&&’.

Important inherited members: text() , setText() , text() , setDown() , isDown() , autoRepeat() , group() , setAutoRepeat() , toggle() , pressed() , released() , clicked() , and toggled() .


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs a radio button with the given parent, but with no text or pixmap.

The parent argument is passed on to the QAbstractButton constructor.


--------------------------------
## __init__(text[, parent=None])

Parameters:

- text – str
- parent – QWidget

Constructs a radio button with the given parent and text string.

The parent argument is passed on to the QAbstractButton constructor.


--------------------------------
## initStyleOption(button)

Parameters:

- button – QStyleOptionButton

Initialize option with the values from this QRadioButton . This method is useful for subclasses when they need a QStyleOptionButton , but don’t want to fill in all the information themselves.

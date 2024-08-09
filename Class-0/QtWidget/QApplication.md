
[Chinese doc](QApplication.CN.md)

# class QApplication

The QApplication class manages the GUI application’s control flow and main settings.


# Synopsis

## Properties

- [autoSipEnabled](#property-autosipenabled--bool)

    Toggles automatic SIP (software input panel) visibility.

- [cursorFlashTime](#property-cursorflashtime--int)

    The text cursor’s flash (blink) time in milliseconds.

- [doubleClickInterval](#property-doubleclickinterval--int)

    The time limit in milliseconds that distinguishes a double click from two consecutive mouse clicks.

- [keyboardInputInterval](#property-keyboardinputinterval--int)

    The time limit in milliseconds that distinguishes a key press from two consecutive key presses.

- [startDragDistance](#property-startdragdistance--int)

    The minimum distance required for a drag and drop operation to start.

- [startDragTime](#property-startdragtime--int)

    The time in milliseconds that a mouse button must be held down before a drag and drop operation will begin.

- [styleSheet](#property-stylesheet--str)

    The application style sheet.

- [wheelScrollLines](#property-wheelscrolllines--int)

    The number of lines to scroll a widget, when the mouse wheel is rotated.


## Methods

- [def \_\_init__()](#initarg__1)

- [def autoSipEnabled()](#autosipenabled)

- [def exec_()](#exec_)

- [def styleSheet()](#stylesheet)


## Slots

- [def setAutoSipEnabled()](#setautosipenabledenabled)

- [def setStyleSheet()](#setstylesheetsheet)


## Signals

- [def focusChanged()](#focuschangedold-now)


## Static functions

- [def aboutQt()](#static-aboutqt)

- [def activeModalWidget()](#static-activemodalwidget)

- [def activePopupWidget()](#static-activepopupwidget)

- [def activeWindow()](#static-activewindow)

- [def alert()](#static-alertwidget-duration0)

- [def allWidgets()](#static-allwidgets)

- [def beep()](#static-beep)

- [def closeAllWindows()](#static-closeallwindows)

- [def cursorFlashTime()](#static-cursorflashtime)

- [def doubleClickInterval()](#static-doubleclickinterval)

- [def focusWidget()](#static-focuswidget)

- [def font()](#static-fontarg__1)

- [def fontMetrics()](#static-fontmetrics)

- [def isEffectEnabled()](#static-iseffectenabledarg__1)

- [def keyboardInputInterval()](#static-keyboardinputinterval)

- [def palette()](#static-palettearg__1)

- [def setActiveWindow()](#static-setactivewindowact)

- [def setCursorFlashTime()](#static-setcursorflashtimearg__1)

- [def setDoubleClickInterval()](#static-doubleclickinterval)

- [def setEffectEnabled()](#static-seteffectenabledarg__1-enabletrue)

- [def setFont()](#static-setfontarg__1-classnamenone)

- [def setKeyboardInputInterval()](#static-setkeyboardinputintervalarg__1)

- [def setPalette()](#static-setpalettearg__1-classnamenone)

- [def setStartDragDistance()](#static-setstartdragdistancel)

- [def setStartDragTime()](#static-setstartdragtimems)

- [def setStyle()](#static-setstylearg__1)

- [def setWheelScrollLines()](#static-setwheelscrolllinesarg__1)

- [def startDragDistance()](#static-startdragdistance)

- [def startDragTime()](#static-startdragtime)

- [def style()](#static-style)

- [def topLevelAt()](#static-toplevelatx-y)

- [def topLevelWidgets()](#static-toplevelwidgets)

- [def wheelScrollLines()](#static-wheelscrolllines)

- [def widgetAt()](#static-widgetatp)


## Detailed Description

QApplication specializes QGuiApplication with some functionality needed for QWidget -based applications. It handles widget specific initialization, finalization.

For any GUI application using Qt, there is precisely one QApplication object, no matter whether the application has 0, 1, 2 or more windows at any given time. For non- QWidget based Qt applications, use QGuiApplication instead, as it does not depend on the QtWidgets library.

Some GUI applications provide a special batch mode ie. provide command line arguments for executing tasks without manual intervention. In such non-GUI mode, it is often sufficient to instantiate a plain QCoreApplication to avoid unnecessarily initializing resources needed for a graphical user interface. The following example shows how to dynamically create an appropriate type of application instance:

```python
QCoreApplication* createApplication(int argc, char *argv[])

    for i in range(1, argc):
        if not qstrcmp(argv[i], "-no-gui"):
            return QCoreApplication(argc, argv)

    return QApplication(argc, argv)

if __name__ == "__main__":

app = QScopedPointer(createApplication(argc, argv))
    if QApplication(app.data()):
       # start GUI version...
    else:
       # start non-GUI version...

    sys.exit(app.exec())
```

The QApplication object is accessible through the instance() function that returns a pointer equivalent to the global qApp pointer.

QApplication ‘s main areas of responsibility are:

- It initializes the application with the user’s desktop settings such as palette() , font() and doubleClickInterval() . It keeps track of these properties in case the user changes the desktop globally, for example through some kind of control panel.

- It performs event handling, meaning that it receives events from the underlying window system and dispatches them to the relevant widgets. By using sendEvent() and postEvent() you can send your own events to widgets.

- It parses common command line arguments and sets its internal state accordingly. See the constructor documentation below for more details.

- It defines the application’s look and feel, which is encapsulated in a QStyle object. This can be changed at runtime with setStyle() .

- It provides localization of strings that are visible to the user via translate().

- It provides some magical objects like the clipboard().

- It knows about the application’s windows. You can ask which widget is at a certain position using widgetAt() , get a list of topLevelWidgets() and closeAllWindows() , etc.

- It manages the application’s mouse cursor handling, see setOverrideCursor()

Since the QApplication object does so much initialization, it must be created before any other objects related to the user interface are created. QApplication also deals with common command line arguments. Hence, it is usually a good idea to create it before any interpretation or modification of argv is done in the application itself.

|                 |          |
| --------------- | -------- |
| System settings | desktopSettingsAware(), setDesktopSettingsAware(), cursorFlashTime() , setCursorFlashTime() , doubleClickInterval() , setDoubleClickInterval() , setKeyboardInputInterval() , wheelScrollLines() , setWheelScrollLines() , palette() , setPalette() , font() , setFont() , fontMetrics(). |
| Event handling  | exec() , processEvents(), exit(), quit(). sendEvent(), postEvent(), sendPostedEvents(), removePostedEvents(), notify() . |
| GUI Styles      | style() , setStyle() . |
| Text handling   | installTranslator(), removeTranslator() translate(). |
| Widgets         | allWidgets() , topLevelWidgets() , activePopupWidget() , activeModalWidget() , clipboard(), focusWidget() , activeWindow() , widgetAt() . |
| Advanced cursor handling | overrideCursor(), setOverrideCursor(), restoreOverrideCursor(). |
| Miscellaneous   | closeAllWindows() , startingUp(), closingDown(). |


--------------------------------
## property autoSipEnabled : bool

This property holds toggles automatic SIP (software input panel) visibility.

Set this property to true to automatically display the SIP when entering widgets that accept keyboard input. This property only affects widgets with the WA_InputMethodEnabled attribute set, and is typically used to launch a virtual keyboard on devices which have very few or no keys.

The property only has an effect on platforms that use software input panels.

The default is platform dependent.

Access functions:

- autoSipEnabled()
- setAutoSipEnabled()


--------------------------------
## property cursorFlashTime : int

This property holds the text cursor’s flash (blink) time in milliseconds.

The flash time is the time required to display, invert and restore the caret display. Usually the text cursor is displayed for half the cursor flash time, then hidden for the same amount of time, but this may vary.

The default value on X11 is 1000 milliseconds. On Windows, the Control Panel value is used and setting this property sets the cursor flash time for all applications.

We recommend that widgets do not cache this value as it may change at any time if the user changes the global desktop settings.

Access functions:

- cursorFlashTime()
- setCursorFlashTime()


--------------------------------
## property doubleClickInterval : int

This property holds the time limit in milliseconds that distinguishes a double click from two consecutive mouse clicks.

The default value on X11 is 400 milliseconds. On Windows and Mac OS, the operating system’s value is used.

Access functions:

- doubleClickInterval()
- setDoubleClickInterval()


--------------------------------
## property keyboardInputInterval : int

This property holds the time limit in milliseconds that distinguishes a key press from two consecutive key presses.

The default value on X11 is 400 milliseconds. On Windows and Mac OS, the operating system’s value is used.

Access functions:

- keyboardInputInterval()
- setKeyboardInputInterval()


--------------------------------
## property startDragDistance : int

This property holds the minimum distance required for a drag and drop operation to start..

If you support drag and drop in your application, and want to start a drag and drop operation after the user has moved the cursor a certain distance with a button held down, you should use this property’s value as the minimum distance required.

For example, if the mouse position of the click is stored in startPos and the current position (e.g. in the mouse move event) is currentPos, you can find out if a drag should be started with code like this:

```python
if ((startPos - currentPos).manhattanLength() >=
        QApplication.startDragDistance())
    startTheDrag()
```

Qt uses this value internally, e.g. in QFileDialog .

The default value (if the platform doesn’t provide a different default) is 10 pixels.

Access functions:

- startDragDistance()
- setStartDragDistance()


--------------------------------
## property startDragTime : int

This property holds the time in milliseconds that a mouse button must be held down before a drag and drop operation will begin.

If you support drag and drop in your application, and want to start a drag and drop operation after the user has held down a mouse button for a certain amount of time, you should use this property’s value as the delay.

Qt also uses this delay internally, e.g. in QTextEdit and QLineEdit , for starting a drag.

The default value is 500 ms.

Access functions:

- startDragTime()
- setStartDragTime()


--------------------------------
## property styleSheet : str

This property holds the application style sheet.

By default, this property returns an empty string unless the user specifies the -stylesheet option on the command line when running the application.

Access functions:

- styleSheet()
- setStyleSheet()


--------------------------------
## property wheelScrollLines : int

This property holds the number of lines to scroll a widget, when the mouse wheel is rotated..

If the value exceeds the widget’s number of visible lines, the widget should interpret the scroll operation as a single page up or page down. If the widget is an item view class , then the result of scrolling one line depends on the setting of the widget’s scroll mode . Scroll one line can mean scroll one item or scroll one pixel .

By default, this property has a value of 3.

Access functions:

- wheelScrollLines()
- setWheelScrollLines()


--------------------------------
## __init__(arg__1)

Parameters:

- arg__1 – list of strings

__init__()

--------------------------------
## static aboutQt()

Displays a simple message box about Qt. The message includes the version number of Qt being used by the application.

This is useful for inclusion in the Help menu of an application, as shown in the Menus example.

This function is a convenience slot for aboutQt() .


--------------------------------
## static activeModalWidget()

Return type: QWidget

Returns the active modal widget.

A modal widget is a special top-level widget which is a subclass of QDialog that specifies the modal parameter of the constructor as true. A modal widget must be closed before the user can continue with other parts of the program.

Modal widgets are organized in a stack. This function returns the active modal widget at the top of the stack.


--------------------------------
## static activePopupWidget()

Return type: QWidget

Returns the active popup widget.

A popup widget is a special top-level widget that sets the Qt::WType_Popup widget flag, e.g. the QMenu widget. When the application opens a popup widget, all events are sent to the popup. Normal widgets and modal widgets cannot be accessed before the popup widget is closed.

Only other popup widgets may be opened when a popup widget is shown. The popup widgets are organized in a stack. This function returns the active popup widget at the top of the stack.


--------------------------------
## static activeWindow()

Return type: QWidget

Returns the application top-level window that has the keyboard input focus, or None if no application window has the focus. There might be an activeWindow() even if there is no focusWidget() , for example if no widget in that window accepts key events.


--------------------------------
## static alert(widget[, duration=0])

Parameters:

- widget – QWidget
- duration – int

Causes an alert to be shown for widget if the window is not the active window. The alert is shown for msec milliseconds. If msec is zero (the default), then the alert is shown indefinitely until the window becomes active again.

Currently this function does nothing on Qt for Embedded Linux.

On macOS, this works more at the application level and will cause the application icon to bounce in the dock.

On Windows, this causes the window’s taskbar entry to flash for a time. If msec is zero, the flashing will stop and the taskbar entry will turn a different color (currently orange).

On X11, this will cause the window to be marked as “demands attention”, the window must not be hidden (i.e. not have hide() called on it, but be visible in some sort of way) in order for this to work.


--------------------------------
## static allWidgets()

Return type: list of QWidget

Returns a list of all the widgets in the application.

The list is empty (QList::isEmpty()) if there are no widgets.

Example:

```python
def updateAllWidgets():

    allWidgets = QApplication.allWidgets()
    for widget in allWidgets:
        widget.update()
```


--------------------------------
## autoSipEnabled()

Return type: bool

Getter of property autoSipEnabled  .

--------------------------------
## static beep()

Sounds the bell, using the default volume and sound. The function is not available in Qt for Embedded Linux.


--------------------------------
## static closeAllWindows()

Closes all top-level windows.

This function is particularly useful for applications with many top-level windows.

The windows are closed in random order, until one window does not accept the close event. The application quits when the last window was successfully closed, unless quitOnLastWindowClosed is set to false. To trigger application termination from e.g. a menu, use QCoreApplication::quit() instead of this function.


--------------------------------
## static cursorFlashTime()

Return type: int

Getter of property cursorFlashTime  .


--------------------------------
## static doubleClickInterval()

Return type: int

Getter of property doubleClickInterval  .


--------------------------------
## exec_()

Return type: int


--------------------------------
## focusChanged(old, now)

Parameters:

- old – QWidget
- now – QWidget

This signal is emitted when the widget that has keyboard focus changed from old to now, i.e., because the user pressed the tab-key, clicked into a widget or changed the active window. Both old and now can be None.

The signal is emitted after both widget have been notified about the change through QFocusEvent.


--------------------------------
## static focusWidget()

Return type: QWidget

Returns the application widget that has the keyboard input focus, or None if no widget in this application has the focus.


--------------------------------
## static font(arg__1)

Parameters:

- arg__1 – QWidget

Return type: QFont

This is an overloaded function.

Returns the default font for the widget. If a default font was not registered for the widget's class, it returns the default font of its nearest registered superclass.


--------------------------------
## static font(className)

Parameters:

- className – str

Return type: QFont

This is an overloaded function.

Returns the font for widgets of the given className.


--------------------------------
## static fontMetrics()

Return type: QFontMetrics

Use the QFontMetricsF constructor instead. Returns display (screen) font metrics for the application font.


--------------------------------
## static isEffectEnabled(arg__1)

Parameters:

- arg__1 – UIEffect

Return type: bool

Returns true if effect is enabled; otherwise returns false.

By default, Qt will try to use the desktop settings. To prevent this, call setDesktopSettingsAware(false).


--------------------------------
## static keyboardInputInterval()

Return type: int

Getter of property keyboardInputInterval  .


--------------------------------
## static palette(arg__1)

Parameters:

- arg__1 – QWidget

Return type: QPalette

If a widget is passed, the default palette for the widget’s class is returned. This may or may not be the application palette. In most cases there is no special palette for certain types of widgets, but one notable exception is the popup menu under Windows, if the user has defined a special background color for menus in the display settings.


--------------------------------
## static palette(className)

Parameters:

- className – str

Return type: QPalette

This is an overloaded function.

Returns the palette for widgets of the given className.


--------------------------------
## static setActiveWindow(act)

Parameters:

- act – QWidget

Use activateWindow() instead.

Sets the active window to the active widget in response to a system event. The function is called from the platform specific event handlers.

It sets the activeWindow() and focusWidget() attributes and sends proper WindowActivate/WindowDeactivate and FocusIn/FocusOut events to all appropriate widgets. The window will then be painted in active state (e.g. cursors in line edits will blink), and it will have tool tips enabled.


--------------------------------
## setAutoSipEnabled(enabled)

Parameters:

- enabled – bool

Setter of property autoSipEnabled  .


--------------------------------
## static setCursorFlashTime(arg__1)

Parameters:

- arg__1 – int

Setter of property cursorFlashTime  .


--------------------------------
## static setDoubleClickInterval(arg__1)

Parameters:

- arg__1 – int

Setter of property doubleClickInterval  .


--------------------------------
## static setEffectEnabled(arg__1[, enable=true])

Parameters:

- arg__1 – UIEffect
- enable – bool

Enables the UI effect effect if enable is true, otherwise the effect will not be used.


--------------------------------
## static setFont(arg__1[, className=None])

Parameters:

- arg__1 – QFont
- className – str

Changes the default application font to font. If className is passed, the change applies only to classes that inherit className (as reported by QObject::inherits()).

On application start-up, the default font depends on the window system. It can vary depending on both the window system version and the locale. This function lets you override the default font; but overriding may be a bad idea because, for example, some locales need extra large fonts to support their special characters.


--------------------------------
## static setKeyboardInputInterval(arg__1)

Parameters:

- arg__1 – int

Setter of property keyboardInputInterval  .


--------------------------------
## static setPalette(arg__1[, className=None])

Parameters:

- arg__1 – QPalette
- className – str

Changes the application palette to palette.

If className is passed, the change applies only to widgets that inherit className (as reported by QObject::inherits()). If className is left 0, the change affects all widgets, thus overriding any previously set class specific palettes.

The palette may be changed according to the current GUI style in polish() .


--------------------------------
## static setStartDragDistance(l)

Parameters:

- l – int

Setter of property startDragDistance  .


--------------------------------
## static setStartDragTime(ms)

Parameters:

- ms – int

Setter of property startDragTime  .


--------------------------------
## static setStyle(arg__1)

Parameters:

- arg__1 – QStyle

Sets the application’s GUI style to style. Ownership of the style object is transferred to QApplication , so QApplication will delete the style object on application exit or when a new style is set and the old style is still the parent of the application object.

Example usage:

```python
QApplication.setStyle(QStyleFactory.create("Fusion"))
```

When switching application styles, the color palette is set back to the initial colors or the system defaults. This is necessary since certain styles have to adapt the color palette to be fully style-guide compliant.

Setting the style before a palette has been set, i.e., before creating QApplication , will cause the application to use standardPalette() for the palette.


--------------------------------
## static setStyle(arg__1)

Parameters:

- arg__1 – str

Return type: QStyle

This is an overloaded function.

Requests a QStyle object for style from the QStyleFactory .

The string must be one of the keys() , typically one of “windows”, “windowsvista”, “fusion”, or “macos”. Style names are case insensitive.

Returns None if an unknown style is passed, otherwise the QStyle object returned is set as the application’s GUI style.


--------------------------------
## setStyleSheet(sheet)

Parameters:

- sheet – str

Setter of property styleSheet  .


--------------------------------
## static setWheelScrollLines(arg__1)

Parameters:

- arg__1 – int

Setter of property wheelScrollLines  .


--------------------------------
## static startDragDistance()

Return type: int

Getter of property startDragDistance  .


--------------------------------
## static startDragTime()

Return type: int

Getter of property startDragTime  .


--------------------------------
## static style()

Return type: QStyle

Returns the application’s style object.


--------------------------------
## styleSheet()

Return type: str

Getter of property styleSheet  .


--------------------------------
## static topLevelAt(x, y)

Parameters:

- x – int
- y – int

Return type: QWidget

This is an overloaded function.

Returns the top-level widget at the point (x, y); returns 0 if there is no such widget.


--------------------------------
## static topLevelWidgets()

Return type: list of QWidget

Returns a list of the top-level widgets (windows) in the application.

Example:

```python
def showAllHiddenTopLevelWidgets():

    topLevelWidgets = QApplication.topLevelWidgets()
    for widget in topLevelWidgets:
        if widget.isHidden():
            widget.show()
```


--------------------------------
## static wheelScrollLines()

Return type: int

Getter of property wheelScrollLines  .


--------------------------------
## static widgetAt(p)

Parameters:

- p – QPoint

Return type: QWidget

Returns the widget at global screen position point, or None if there is no Qt widget there.

This function can be slow.


--------------------------------
## static widgetAt(x, y)

Parameters:

- x – int
- y – int

Return type: QWidget

This is an overloaded function.

Returns the widget at global screen position (x, y), or None if there is no Qt widget there.

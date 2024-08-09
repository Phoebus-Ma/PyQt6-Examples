
[English doc](QApplication.md)

# class QApplication

QApplication 类管理 GUI 应用程序的控制流和主要设置。


# Synopsis

## Properties

- [autoSipEnabled](#property-autosipenabled--bool)

    切换自动 SIP（​​软件输入面板）可见性。

- [cursorFlashTime](#property-cursorflashtime--int)

    文本光标的闪烁时间（以毫秒为单位）。

- [doubleClickInterval](#property-doubleclickinterval--int)

    区分双击和两次连续鼠标单击的时间限制（以毫秒为单位）。

- [keyboardInputInterval](#property-keyboardinputinterval--int)

    区分一次按键和两次连续按键的时间限制（以毫秒为单位）。

- [startDragDistance](#property-startdragdistance--int)

    开始拖放操作所需的最小距离。

- [startDragTime](#property-startdragtime--int)

    开始拖放操作之前必须按住鼠标按钮的时间（以毫秒为单位）。

- [styleSheet](#property-stylesheet--str)

    应用程序样式表。

- [wheelScrollLines](#property-wheelscrolllines--int)

    当鼠标滚轮旋转时，小部件滚动的行数。


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

QApplication 专门化了 QGuiApplication，并增加了基于 QWidget 的应用程序所需的一些功能。它处理特定于窗口小部件的初始化和结束。

对于使用 Qt 的任何 GUI 应用程序，无论应用程序在任何给定时间拥有 0、1、2 或更多窗口，都只有一个 QApplication 对象。对于不基于 QWidget 的 Qt 应用程序，请改用 QGuiApplication，因为它不依赖于 QtWidgets 库。

一些 GUI 应用程序提供特殊的批处理模式，即提供用于执行任务而无需手动干预的命令行参数。在这种非 GUI 模式下，实例化一个简单的 QCoreApplication 往往就足以避免不必要地初始化图形用户界面所需的资源。以下示例显示了如何动态创建适当类型的应用程序实例：

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

QApplication 对象可通过 instance() 函数访问，该函数返回一个与全局 qApp 指针等效的指针。

QApplication 的主要职责包括：

- 它使用用户的桌面设置（如 palette() 、 font() 和 doubleClickInterval() ）初始化应用程序。它会跟踪这些属性，以防用户全局更改桌面（例如通过某种控制面板）。

- 它执行事件处理，这意味着它从底层窗口系统接收事件并将它们分派到相关小部件。通过使用 sendEvent() 和 postEvent()，您可以将自己的事件发送到小部件。

- 它解析常见的命令行参数并相应地设置其内部状态。有关更多详细信息，请参阅下面的构造函数文档。

- 它定义应用程序的外观，封装在 QStyle 对象中。这可以在运行时使用 setStyle() 进行更改。

- 它通过 Translation() 提供用户可见的字符串的本地化。

- 它提供了一些神奇的对象，如 clipboard()。

- 它了解应用程序的窗口。您可以使用 widgetAt() 询问哪个小部件位于某个位置，获取 topLevelWidgets() 和 closeAllWindows() 的列表等。

- 它管理应用程序的鼠标光标处理，请参阅 setOverrideCursor()

由于 QApplication 对象执行了大量初始化，因此必须在创建与用户界面相关的任何其他对象之前创建它。QApplication 还处理常见的命令行参数。因此，在应用程序本身中对 argv 进行任何解释或修改之前创建它通常是一个好主意。

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

此属性用于切换自动 SIP（​​软件输入面板）可见性。

将此属性设置为 true，以在输入接受键盘输入的小部件时自动显示 SIP。此属性仅影响设置了 WA_InputMethodEnabled 属性的小部件，通常用于在按键很少或没有按键的设备上启动虚拟键盘。

此属性仅对使用软件输入面板的平台有效。

默认值取决于平台。

访问函数：

- autoSipEnabled()
- setAutoSipEnabled()


--------------------------------
## property cursorFlashTime : int

此属性保存文本光标的闪烁时间（以毫秒为单位）。

闪烁时间是显示、反转和恢复插入符号显示所需的时间。通常，文本光标的显示时间为光标闪烁时间的一半，然后隐藏相同的时间，但这可能会有所不同。

X11 上的默认值为 1000 毫秒。在 Windows 上，使用控制面板值，设置此属性会为所有应用程序设置光标闪烁时间。

我们建议小部件不要缓存此值，因为如果用户更改全局桌面设置，该值可能会随时更改。

访问函数：

- cursorFlashTime()
- setCursorFlashTime()


--------------------------------
## property doubleClickInterval : int

此属性保存区分双击和两次连续鼠标单击的时间限制（以毫秒为单位）。

X11 上的默认值为 400 毫秒。在 Windows 和 Mac OS 上，使用操作系统的值。

访问函数：

- doubleClickInterval()
- setDoubleClickInterval()


--------------------------------
## property keyboardInputInterval : int

此属性保存区分一次按键和两次连续按键的时间限制（以毫秒为单位）。

X11 上的默认值为 400 毫秒。在 Windows 和 Mac OS 上，使用操作系统的值。

访问函数：

- keyboardInputInterval()
- setKeyboardInputInterval()


--------------------------------
## property startDragDistance : int

此属性保存拖放操作启动所需的最小距离。

如果您的应用程序支持拖放，并希望在用户按住按钮将光标移动一定距离后启动拖放操作，则应使用此属性的值作为所需的最小距离。

例如，如果单击的鼠标位置存储在startPos中，当前位置（例如在鼠标移动事件中）是currentPos，则可以使用如下代码确定是否应启动拖动：

```python
if ((startPos - currentPos).manhattanLength() >=
        QApplication.startDragDistance())
    startTheDrag()
```

Qt 在内部使用此值，例如在 QFileDialog 中。

默认值（如果平台未提供其他默认值）为 10 像素。

访问函数：

- startDragDistance()
- setStartDragDistance()


--------------------------------
## property startDragTime : int

此属性保存在开始拖放操作之前必须按住鼠标按钮的时间（以毫秒为单位）。

如果您的应用程序支持拖放，并且希望在用户按住鼠标按钮一段时间后开始拖放操作，则应使用此属性的值作为延迟。

Qt 也在内部使用此延迟（例如在 QTextEdit 和 QLineEdit 中）来开始拖动。

默认值为 500 毫秒。

访问函数：

- startDragTime()
- setStartDragTime()


--------------------------------
## property styleSheet : str

此属性保存应用程序样式表。

默认情况下，除非用户在运行应用程序时在命令行上指定 -stylesheet 选项，否则此属性将返回空字符串。

访问函数：

- styleSheet()
- setStyleSheet()


--------------------------------
## property wheelScrollLines : int

此属性保存鼠标滚轮旋转时小部件要滚动的行数。

如果该值超出小部件的可见行数，小部件应将滚动操作解释为单页向上或向下翻页。如果小部件是项目视图类，则滚动一行的结果取决于小部件的滚动模式的设置。滚动一行可以意味着滚动一个项目或滚动一个像素。

默认情况下，此属性的值为 3。

访问函数：

- wheelScrollLines()
- setWheelScrollLines()


--------------------------------
## __init__(arg__1)

参数：

- arg__1 – list of strings

__init__()

--------------------------------
## static aboutQt()

显示有关 Qt 的简单消息框。该消息包括应用程序正在使用的 Qt 的版本号。

这对于包含在应用程序的帮助菜单中很有用，如菜单示例所示。

此函数是 aboutQt() 的便利槽。


--------------------------------
## static activeModalWidget()

返回类型：QWidget

返回活动模式小部件。

模式小部件是一种特殊的顶级小部件，它是 QDialog 的子类，它将构造函数的模式参数指定为 true。用户必须先关闭模式小部件，然后才能继续执行程序的其他部分。

模式小部件组织在堆栈中。此函数返回堆栈顶部的活动模式小部件。


--------------------------------
## static activePopupWidget()

返回类型：QWidget

返回活动的弹出窗口小部件。

弹出窗口小部件是一种特殊的顶级窗口小部件，用于设置 Qt::WType_Popup 窗口小部件标志，例如 QMenu 窗口小部件。当应用程序打开弹出窗口小部件时，所有事件都会发送到弹出窗口。在弹出窗口小部件关闭之前，无法访问普通窗口小部件和模式窗口小部件。

显示弹出窗口小部件时，只能打开其他弹出窗口小部件。弹出窗口小部件组织在一个堆栈中。此函数返回堆栈顶部的活动弹出窗口小部件。


--------------------------------
## static activeWindow()

返回类型：QWidget

返回具有键盘输入焦点的应用程序顶层窗口，如果没有应用程序窗口具有焦点，则返回 None。即使没有 focusWidget() ，也可能存在 activeWindow() ，例如，如果该窗口中没有小部件接受键盘事件。


--------------------------------
## static alert(widget[, duration=0])

参数：

- widget – QWidget
- duration – int

如果窗口不是活动窗口，则会导致小部件显示警报。警报显示时间为 msec 毫秒。如果 msec 为零（默认值），则警报将无限期显示，直到窗口再次变为活动状态。

目前，此功能在 Qt for Embedded Linux 上不执行任何操作。

在 macOS 上，这更多地在应用程序级别起作用，并将导致应用程序图标在 dock 中弹跳。

在 Windows 上，这会导致窗口的任务栏条目闪烁一段时间。如果 msec 为零，闪烁将停止，任务栏条目将变为不同的颜色（当前为橙色）。

在 X11 上，这将导致窗口被标记为“需要注意”，窗口不能被隐藏（即没有在其上调用 hide()，但以某种方式可见）才能正常工作。


--------------------------------
## static allWidgets()

返回类型：list of QWidget

返回应用程序中所有小部件的列表。

如果没有小部件，则列表为空 (QList::isEmpty())。

示例：

```python
def updateAllWidgets():

    allWidgets = QApplication.allWidgets()
    for widget in allWidgets:
        widget.update()
```


--------------------------------
## autoSipEnabled()

返回类型：bool

属性 autoSipEnabled 的获取器。

--------------------------------
## static beep()

使用默认音量和声音发出铃声。此功能在 Qt for Embedded Linux 中不可用。


--------------------------------
## static closeAllWindows()

关闭所有顶层窗口。

此函数对于具有许多顶层窗口的应用程序特别有用。

窗口以随机顺序关闭，直到一个窗口不接受关闭事件。当最后一个窗口成功关闭时，应用程序退出，除非 quitOnLastWindowClosed 设置为 false。要从菜单等触发应用程序终止，请使用 QCoreApplication::quit() 代替此函数。


--------------------------------
## static cursorFlashTime()

返回类型：int

属性 cursorFlashTime 的获取器。


--------------------------------
## static doubleClickInterval()

返回类型：int

属性 doubleClickInterval 的获取器。


--------------------------------
## exec_()

返回类型：int


--------------------------------
## focusChanged(old, now)

参数：

- old – QWidget
- now – QWidget

当具有键盘焦点的小部件从旧状态变为现在状态时，即由于用户按下 Tab 键、单击小部件或更改活动窗口，将发出此信号。旧状态和现在状态都可以为 None。

在两个小部件都通过 QFocusEvent 收到有关更改的通知后，将发出此信号。


--------------------------------
## static focusWidget()

返回类型：QWidget

返回具有键盘输入焦点的应用程序小部件，如果此应用程序中没有小部件具有焦点，则返回 None。


--------------------------------
## static font(arg__1)

参数：

- arg__1 – QWidget

返回类型：QFont

这是一个重载函数。

返回小部件的默认字体。如果小部件的类未注册默认字体，则返回其最近的已注册超类的默认字体。


--------------------------------
## static font(className)

参数：

- className – str

返回类型：QFont

这是一个重载函数。

返回给定 className 的小部件的字体。


--------------------------------
## static fontMetrics()

返回类型：QFontMetrics

改用 QFontMetricsF 构造函数。返回应用程序字体的显示（屏幕）字体度量。


--------------------------------
## static isEffectEnabled(arg__1)

参数：

- arg__1 – UIEffect

返回类型：bool

如果启用了效果，则返回 true；否则返回 false。

默认情况下，Qt 将尝试使用桌面设置。为防止这种情况，请调用 setDesktopSettingsAware(false)。


--------------------------------
## static keyboardInputInterval()

返回类型：int

属性 keyboardInputInterval 的获取器。


--------------------------------
## static palette(arg__1)

参数：

- arg__1 – QWidget

返回类型：QPalette

如果传递了小部件，则返回小部件类的默认调色板。这可能是也可能不是应用程序调色板。在大多数情况下，某些类型的小部件没有特殊调色板，但一个值得注意的例外是 Windows 下的弹出菜单，如果用户在显示设置中为菜单定义了特殊背景颜色。


--------------------------------
## static palette(className)

参数：

- className – str

返回类型：QPalette

这是一个重载函数。

返回给定 className 的小部件的调色板。


--------------------------------
## static setActiveWindow(act)

参数：

- act – QWidget

改用 activateWindow()。

将活动窗口设置为活动小部件以响应系统事件。该函数从特定于平台的事件处理程序调用。

它设置 activeWindow() 和 focusWidget() 属性，并将适当的 WindowActivate/WindowDeactivate 和 FocusIn/FocusOut 事件发送到所有适当的小部件。然后窗口将以活动状态绘制（例如，行编辑中的光标将闪烁），并且将启用工具提示。


--------------------------------
## setAutoSipEnabled(enabled)

参数：

- enabled – bool

属性 autoSipEnabled 的设置者。


--------------------------------
## static setCursorFlashTime(arg__1)

参数：

- arg__1 – int

属性 cursorFlashTime 的设置方法。


--------------------------------
## static setDoubleClickInterval(arg__1)

参数：

- arg__1 – int

属性 doubleClickInterval 的设置者。


--------------------------------
## static setEffectEnabled(arg__1[, enable=true])

参数：

- arg__1 – UIEffect
- enable – bool

如果enable为true则启用UI效果，否则不会使用该效果。


--------------------------------
## static setFont(arg__1[, className=None])

参数：

- arg__1 – QFont
- className – str

将默认应用程序字体更改为 font。如果传递了 className，则更改仅适用于继承 className 的类（由 QObject::inherits() 报告）。

在应用程序启动时，默认字体取决于窗口系统。它可能因窗口系统版本和语言环境而异。此函数允许您覆盖默认字体；但覆盖可能不是一个好主意，因为例如，某些语言环境需要超大字体来支持其特殊字符。


--------------------------------
## static setKeyboardInputInterval(arg__1)

参数：

- arg__1 – int

属性 keyboardInputInterval 的设置者。


--------------------------------
## static setPalette(arg__1[, className=None])

参数：

- arg__1 – QPalette
- className – str

将应用程序调色板更改为 palette。

如果传递了 className，则更改仅适用于继承 className 的小部件（由 QObject::inherits() 报告）。 如果 className 保留为 0，则更改会影响所有小部件，从而覆盖任何先前设置的特定于类的调色板。

可以根据 polish() 中的当前 GUI 样式更改调色板。


--------------------------------
## static setStartDragDistance(l)

参数：

- l – int

属性 startDragDistance 的设置者。


--------------------------------
## static setStartDragTime(ms)

参数：

- ms – int

属性 startDragTime 的设置者。


--------------------------------
## static setStyle(arg__1)

参数：

- arg__1 – QStyle

将应用程序的 GUI 样式设置为 style。样式对象的所有权将转移给 QApplication ，因此 QApplication 将在应用程序退出时或设置新样式且旧样式仍为应用程序对象的父级时删除样式对象。

使用示例：

```python
QApplication.setStyle(QStyleFactory.create("Fusion"))
```

切换应用程序样式时，调色板将恢复为初始颜色或系统默认值。这是必要的，因为某些样式必须调整调色板才能完全符合样式指南。

在设置调色板之前（即在创建 QApplication 之前）设置样式将导致应用程序使用 standardPalette() 作为调色板。


--------------------------------
## static setStyle(arg__1)

参数：

- arg__1 – str

返回类型：QStyle

这是一个重载函数。

从 QStyleFactory 请求样式的 QStyle 对象。

字符串必须是 keys() 之一，通常是“windows”、“windowsvista”、“fusion”或“macos”之一。样式名称不区分大小写。

如果传递了未知样式，则返回 None，否则返回的 QStyle 对象将设置为应用程序的 GUI 样式。


--------------------------------
## setStyleSheet(sheet)

参数：

- sheet – str

属性 styleSheet 的设置者。


--------------------------------
## static setWheelScrollLines(arg__1)

参数：

- arg__1 – int

属性 wheelScrollLines 的设置者。


--------------------------------
## static startDragDistance()

返回类型：int

属性 startDragDistance 的获取器。


--------------------------------
## static startDragTime()

返回类型：int

属性 startDragTime 的获取器。


--------------------------------
## static style()

返回类型：QStyle

返回应用程序的样式对象。


--------------------------------
## styleSheet()

返回类型：str

属性 styleSheet 的获取器。


--------------------------------
## static topLevelAt(x, y)

参数：

- x – int
- y – int

返回类型：QWidget

这是一个重载函数。

返回点 (x, y) 处的顶级小部件；如果不存在这样的小部件，则返回 0。


--------------------------------
## static topLevelWidgets()

返回类型：list of QWidget

返回应用程序中顶级小部件（窗口）的列表。

示例：

```python
def showAllHiddenTopLevelWidgets():

    topLevelWidgets = QApplication.topLevelWidgets()
    for widget in topLevelWidgets:
        if widget.isHidden():
            widget.show()
```


--------------------------------
## static wheelScrollLines()

返回类型：int

属性 wheelScrollLines 的获取器。


--------------------------------
## static widgetAt(p)

参数：

- p – QPoint

返回类型：QWidget

返回全局屏幕位置点处的窗口小部件，如果该位置没有 Qt 窗口小部件，则返回 None。

此功能可能很慢。


--------------------------------
## static widgetAt(x, y)

参数：

- x – int
- y – int

返回类型：QWidget

这是一个重载函数。

返回全局屏幕位置 (x, y) 处的窗口小部件，如果该位置没有 Qt 窗口小部件，则返回 None。

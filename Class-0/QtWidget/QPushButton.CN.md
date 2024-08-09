
# class QPushButton

QPushButton 小部件提供了一个命令按钮。


# Synopsis

## Properties

- [autoDefault](#property-autodefault--bool)

    该按钮是否是自动默认按钮。

- [default](#property-default--bool)

    该按钮是否是默认按钮。

- [flat](#property-flat--bool)

    按钮边框是否凸起。


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

按钮或命令按钮可能是图形用户界面中最常用的小部件。按下（单击）按钮可命令计算机执行某些操作或回答问题。典型的按钮有确定、应用、取消、关闭、是、否和帮助。

命令按钮是矩形的，通常显示描述其操作的文本标签。可以通过在文本中将首选字符前面加上“与”符号来指定快捷键。例如：

```python
button = QPushButton("Download", self)
```

在此示例中，快捷键为 Alt+D。有关详细信息，请参阅 QShortcut 文档（要显示实际的 & 符号，请使用“&&”）。

按钮显示文本标签，并可选显示小图标。可以使用构造函数设置这些，然后使用 setText() 和 setIcon() 进行更改。如果按钮被禁用，则将根据 GUI 样式操纵文本和图标的外观，以使按钮看起来“已禁用”。

当按钮被鼠标、空格键或键盘快捷键激活时，它会发出信号 clicked()。连接到此信号以执行按钮的操作。按钮还提供不太常用的信号，例如 pressed() 和 release()。

对话框中的命令按钮默认为自动默认按钮，即，当它们获得键盘输入焦点时，它们会自动成为默认按钮。默认按钮是当用户在对话框中按下 Enter 或 Return 键时激活的按钮。您可以使用 setAutoDefault() 更改此设置。请注意，自动默认按钮会保留一些额外的空间，这是绘制默认按钮指示器所必需的。如果您不希望按钮周围有此空间，请调用 setAutoDefault (false)。

按钮小部件如此重要，在过去十年中已经发展到可以容纳大量变体。Microsoft 样式指南现在显示了大约十种不同的 Windows 按钮状态，并且文本暗示，如果考虑所有功能组合，则还有几十种不同的状态。

最重要的模式或状态是：

- 可用或不可用（灰色，禁用）。

- 标准按钮、切换按钮或菜单按钮。

- 开启或关闭（仅适用于切换按钮）。

- 默认或正常。对话框中的默认按钮通常可以使用 Enter 或 Return 键“单击”。

- 是否自动重复。

- 是否按下。

作为一般规则，当用户单击应用程序或对话框窗口时执行操作（例如应用、取消、关闭和帮助），并且小部件应该具有带有文本标签的宽矩形形状时，请使用按钮。小型、通常为方形的按钮会更改窗口的状态而不是执行操作（例如 QFileDialog 右上角的按钮）不是命令按钮，而是工具按钮。Qt 为这些按钮提供了一个特殊的类 (QToolButton)。

如果您需要切换行为（请参阅 setCheckable()）或按钮，当按下时会自动重复激活信号，如滚动条中的箭头（请参阅 setAutoRepeat()），则命令按钮可能不是您想要的。如有疑问，请使用工具按钮。

命令按钮的一种变体是菜单按钮。这些按钮不仅提供一个命令，而且提供多个命令，因为单击它们时会弹出一个选项菜单。使用方法 setMenu() 将弹出菜单与按钮关联。

其他按钮类包括选项按钮（参见 QRadioButton ）和复选框（参见 QCheckBox ）。

在 Qt 中，QAbstractButton 基类提供大多数模式和其他 API，而 QPushButton 提供 GUI 逻辑。有关 API 的更多信息，请参阅 QAbstractButton。


--------------------------------
## property autoDefault : bool

此属性用于保存按钮是否为自动默认按钮。

如果此属性设置为 true，则按钮为自动默认按钮。

在某些 GUI 样式中，默认按钮周围会画一个额外的边框，最多 3 个像素或更多。Qt 会自动在自动默认按钮周围保留此空间，即自动默认按钮可能具有稍大的尺寸提示。

对于具有 QDialog 父级的按钮，此属性的默认值为 true；否则默认值为 false。

有关默认和自动默认如何交互的详细信息，请参阅默认属性。

访问函数：

- autoDefault()
- setAutoDefault()


--------------------------------
## property default : bool

此属性保存按钮是否为默认按钮。

默认按钮和自动默认按钮决定用户在对话框中按下 Enter 键时会发生什么。

将此属性设置为 true 的按钮（即对话框的默认按钮）将在用户按下 Enter 键时自动按下，但有一个例外：如果当前焦点为自动默认按钮，则按下自动默认按钮。当对话框有自动默认按钮但没有默认按钮时，按下 Enter 键将按下当前焦点为自动默认按钮，或者如果没有按钮为焦点，则按下焦点链中的下一个自动默认按钮。

在对话框中，一次只能有一个按钮是默认按钮。然后，此按钮将与附加框架一起显示（取决于 GUI 样式）。

默认按钮行为仅在对话框中提供。当按钮具有焦点时，始终可以通过按空格键从键盘单击按钮。

如果在对话框可见时将当前默认按钮的默认属性设置为 false，则下次对话框中的按钮获得焦点时将自动分配新的默认值。

该属性的默认值为 false。

访问函数：

- isDefault()
- setDefault()


--------------------------------
## property flat : bool

此属性保存按钮边框是否凸起。

此属性的默认值为 false。如果设置了此属性，则大多数样式将不会绘制按钮背景，除非按下按钮。setAutoFillBackground() 可用于确保使用 QPalette::Button 画笔填充背景。

访问函数：

- isFlat()
- setFlat()


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

构造一个没有文本但有父级的按钮。


--------------------------------
## __init__(icon, text[, parent=None])

参数：

- icon – QIcon
- text – str
- parent – QWidget

构造一个带有图标、文本和父级的按钮。

请注意，您还可以将 QPixmap 对象作为图标传递（这要归功于 C++ 提供的隐式类型转换）。


--------------------------------
## __init__(text[, parent=None])

参数：

- text – str
- parent – QWidget

构造一个具有父级parent和文本text的按钮。


--------------------------------
## autoDefault()

返回值：bool

属性 autoDefault 的获取器。


--------------------------------
## initStyleOption(option)

参数：

- option – QStyleOptionButton

用此 QPushButton 中的值初始化选项。当子类需要 QStyleOptionButton 但不想自己填写所有信息时，此方法很有用。


--------------------------------
## isDefault()

返回值：bool

属性默认值的获取器。


--------------------------------
## isFlat()

返回值：bool

财产单位的获取者。


--------------------------------
## menu()

返回值：QMenu

返回按钮关联的弹出菜单；如果未设置弹出菜单，则返回 None。


--------------------------------
## setAutoDefault(arg__1)

参数：

- arg__1 – bool

属性 autoDefault 的设置者。


--------------------------------
## setDefault(arg__1)

参数：

- arg__1 – bool

属性默认值的设置者。


--------------------------------
## setFlat(arg__1)

参数：

- arg__1 – bool

房产公寓的安置者。


--------------------------------
## setMenu(menu)

参数：

- menu – QMenu

将弹出菜单与此按钮关联。这会将按钮变成菜单按钮，在某些样式中，按钮文本右侧会出现一个小三角形。

菜单的所有权不会转移到按钮。

Fusion 小部件样式中显示的带有弹出菜单的按钮。


--------------------------------
## showMenu()

显示（弹出）关联的弹出菜单。如果没有这样的菜单，则此函数不执行任何操作。直到用户关闭弹出菜单后，此函数才会返回。

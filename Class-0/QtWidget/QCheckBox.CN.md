
[English doc](QCheckBox.md)

# class QCheckBox

QCheckBox 小部件提供了一个带有文本标签的复选框。


# Synopsis

## Properties

- [tristate](#property-tristate--bool)

    该复选框是否是三态复选框。


## Methods

- [def \_\_init__()](#initparentnone)

- [def checkState()](#checkstate)

- [def isTristate()](#istristate)

- [def setCheckState()](#setcheckstatestate)

- [def setTristate()](#settristateytrue)


## Virtual methods

- [def initStyleOption()](#initstyleoptionoption)


## Signals

- [def checkStateChanged()](#checkstatechangedarg__1)

- [def stateChanged()](#statechangedarg__1)


# Detailed Description

QCheckBox 是一个可以打开（选中）或关闭（取消选中）的选项按钮。复选框通常用于表示应用程序中可以启用或禁用而不会影响其他功能的功能。可以实现不同类型的行为。例如，可以使用 QButtonGroup 对复选按钮进行逻辑分组，从而允许使用独占复选框。但是，QButtonGroup 不提供任何视觉表示。

下图进一步说明了独占复选框和非独占复选框之间的区别。

每当选中或清除复选框时，它都会发出信号 checkStateChanged() 。如果您想在复选框每次改变状态时触发操作，请连接到此信号。您可以使用 isChecked() 来查询复选框是否被选中。

除了通常的选中和未选中状态外，QCheckBox 还可以选择提供第三种状态来指示“无变化”。当您需要为用户提供既不选中也不取消选中复选框的选项时，这很有用。如果您需要第三种状态，请使用 setTristate() 启用它，并使用 checkState() 查询当前的切换状态。

就像 QPushButton 一样，复选框显示文本，也可以显示小图标。图标使用 setIcon() 设置。文本可以在构造函数中设置，也可以使用 setText() 设置。可以通过在首选字符前加上 & 符号来指定快捷键。例如：

```python
checkbox = QCheckBox("Case sensitive", self)
```

在此示例中，快捷键为 Alt+A。有关详细信息，请参阅 QShortcut 文档。要显示实际的 & 符号，请使用“&&”。

重要的继承函数：text()、setText()、text()、pixmap()、setPixmap()、accel()、setAccel()、isToggleButton()、setDown()、isDown()、isOn()、checkState()、autoRepeat()、isExclusiveToggle()、group()、setAutoRepeat()、toggle()、pressed()、released()、clicked()、toggled()、checkState() 和 checkStateChanged()。


--------------------------------
## property tristate : bool

此属性保存复选框是否为三态复选框。

默认值为 false，即复选框只有两种状态。

访问函数：

- isTristate()
- setTristate()


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

使用给定的父级构造一个复选框，但没有文本。

父级被传递给 QAbstractButton 构造函数。


--------------------------------
## __init__(text[, parent=None])

参数：

- text – str
- parent – QWidget

使用给定的父级和文本构造一个复选框。

父级被传递给 QAbstractButton 构造函数。


--------------------------------
## checkState()

返回类型：CheckState

返回复选框的选中状态。如果不需要三态支持，也可以使用 isChecked() ，它返回布尔值。


--------------------------------
## checkStateChanged(arg__1)

参数：

- arg__1 – CheckState

每当复选框的状态发生变化时（即，每当用户选中或取消选中复选框时），都会发出此信号。

state 包含复选框的新 Qt::CheckState。


--------------------------------
## initStyleOption(option)

参数：

- option – QStyleOptionButton

用此 QCheckBox 中的值初始化选项。此方法对于需要 QStyleOptionButton 但不想自己填写所有信息的子类很有用。


--------------------------------
## isTristate()

返回类型：bool

属性 tristateᅟ 的获取器。


--------------------------------
## setCheckState(state)

参数：

- state – CheckState

将复选框的选中状态设置为 state。如果不需要三态支持，也可以使用 setChecked() ，它接受一个布尔值。


--------------------------------
## setTristate([y=true])

参数：

- y – bool

属性 tristateᅟ 的 setter。


--------------------------------
## stateChanged(arg__1)

参数：

- arg__1 – int

改用 checkStateChanged (Qt::CheckState)。


[English doc](QRadioButton.md)

# class QRadioButton

QRadioButton 小部件提供了一个带有文本标签的单选按钮。


# Synopsis

## Methods

- [def \_\_init__()](#initparentnone)


## Virtual methods

- [def initStyleOption()](#initstyleoptionbutton)


## Detailed Description

QRadioButton 是一个可以打开（选中）或关闭（取消选中）的选项按钮。单选按钮通常为用户提供“众多选择之一”。在一组单选按钮中，一次只能选中一个单选按钮；如果用户选择另一个按钮，则先前选择的按钮将被关闭。

单选按钮默认为自动独占。如果启用了自动独占，则属于同一父窗口小部件的单选按钮的行为就像它们是同一独占按钮组的一部分一样。如果您需要属于同一父窗口小部件的单选按钮的多个独占按钮组，请将它们放入 QButtonGroup 中。

每当按钮打开或关闭时，它都会发出 toggled() 信号。如果您想在按钮每次改变状态时触发操作，请连接到此信号。使用 isChecked() 查看是否选择了特定按钮。

与 QPushButton 一样，单选按钮显示文本，也可以显示小图标。图标使用 setIcon() 设置。文本可以在构造函数中或使用 setText() 设置。可以通过在文本中将首选字符置于“&”符号前来指定快捷键。例如：

```python
button = QRadioButton("Search from the cursor", self)
```

在此示例中，快捷键为 Alt+c。有关详细信息，请参阅 QShortcut 文档。要显示实际的 & 符号，请使用“&&”。

重要的继承成员：text()、setText()、text()、setDown()、isDown()、autoRepeat()、group()、setAutoRepeat()、toggle()、pressed()、released()、clicked() 和 toggled()。


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

使用给定的父级构造一个单选按钮，但没有文本或像素图。

父级参数传递给 QAbstractButton 构造函数。


--------------------------------
## __init__(text[, parent=None])

参数：

- text – str
- parent – QWidget

使用给定的父级和文本字符串构造一个单选按钮。

父级参数被传递给 QAbstractButton 构造函数。


--------------------------------
## initStyleOption(button)

参数：

- button – QStyleOptionButton

用此 QRadioButton 中的值初始化选项。当子类需要 QStyleOptionButton 但不想自己填写所有信息时，此方法很有用。

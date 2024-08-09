
[English doc](QGroupBox.md)

# class QGroupBox

QGroupBox 小部件提供了一个带有标题的组合框。


# Synopsis

## Properties

- [alignment](#property-alignment--combination-of-qtalignmentflag)

    组框标题的对齐方式。

- [checkable](#property-checkable--bool)

    组框的标题中是否有复选框。

- [checked](#property-checked--bool)

    组框是否被选中。

- [flat](#property-flat--bool)

    组框是否涂成平面或带有框架。

- [title](#property-title--str)

    组框标题文本。


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

组框提供框架、顶部的标题、键盘快捷键，并在其内部显示各种其他小部件。键盘快捷键将键盘焦点移动到组框的子小部件之一。

QGroupBox 还允许您设置标题（通常在构造函数中设置）和标题的对齐方式。组框可以是可选中的。可选中组框中的子小部件的启用或禁用取决于组框是否被选中。

您可以通过启用 flat 属性来最大限度地减少组框的空间消耗。在大多数样式中，启用此属性会导致删除框架的左、右和下边缘。

QGroupBox 不会自动布局子小部件（通常是 QCheckBox 或 QRadioButton，但可以是任何小部件）。以下示例显示了如何使用布局设置 QGroupBox：

```bash
groupBox = QGroupBox(tr("Exclusive Radio Buttons"))
radio1 = QRadioButton(tr("Radio button 1"))
radio2 = QRadioButton(tr("Radio button 2"))
radio3 = QRadioButton(tr("Radio button 3"))
radio1.setChecked(True)
```


--------------------------------
## property alignment : Combination of Qt.AlignmentFlag

此属性保存组框标题的对齐方式。

大多数样式将标题放在框架顶部。可以使用以下列表中的单个值指定标题的水平对齐方式：

- Qt::AlignLeft 将标题文本与组框左侧对齐。

- Qt::AlignRight 将标题文本与组框右侧对齐。

- Qt::AlignHCenter 将标题文本与组框水平中心对齐。

默认对齐方式为 Qt::AlignLeft。

访问函数：

- alignment()
- setAlignment()


--------------------------------
## property checkable : bool

此属性保存组框的标题中是否有复选框。

如果此属性为真，则组框将使用复选框代替普通标签来显示其标题。 如果选中复选框，则组框的子项将被启用；否则，它们将被禁用且无法访问。

默认情况下，组框不可选中。

如果为组框启用了此属性，则还会首先检查它以确保其内容已启用。

访问函数：

- isCheckable()
- setCheckable()


--------------------------------
## property checked : bool

此属性保存组框是否被选中。

如果组框是可选中的，则显示复选框。 如果复选框被选中，则组框的子项被启用；否则，子项被禁用，用户无法访问。

默认情况下，可选中的组框也会被选中。

访问函数：

- isChecked()
- setChecked()
- Signal toggled()


--------------------------------
## property flat : bool

此属性用于控制组框是平铺绘制还是带有框架。

组框通常由一个周围框架组成，顶部带有标题。如果启用此属性，则在大多数样式中仅绘制框架的顶部；否则，将绘制整个框架。

默认情况下，此属性处于禁用状态，即，除非明确指定，否则组框不是平铺的。

访问函数：

- isFlat()
- setFlat()


--------------------------------
## property title : str

此属性保存组框标题文本。

如果标题包含一个与号 (’&’) 和一个字母，则组框标题文本将具有键盘快捷键。

```python
g.setTitle("User information")
```

在上面的示例中，Alt+U 将键盘焦点移至组框。有关详细信息，请参阅 QShortcut 文档（要显示实际的 & 符号，请使用“&&”）。

没有默认标题文本。

访问函数：

- title()
- setTitle()


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

构造一个具有给定父级但没有标题的组合框小部件。


--------------------------------
## __init__(title[, parent=None])

参数：

- title – str
- parent – QWidget

构造具有给定标题和父级的组合框。


--------------------------------
## alignment()

返回类型：Combination of AlignmentFlag

属性 alignment 的获取器。


--------------------------------
## clicked([checked=false])

参数：

- checked – bool

当复选框被激活（即，当鼠标光标位于按钮内时按下然后释放）或键入快捷键时，会发出此信号。值得注意的是，如果您调用 setChecked() ，则不会发出此信号。

如果复选框被选中，则 checked 为 true；如果复选框未被选中，则为 false。


--------------------------------
## initStyleOption(option)

参数：

- option – QStyleOptionGroupBox

用此 QGroupBox 中的值初始化选项。当子类需要 QStyleOptionGroupBox 但不想自己填写所有信息时，此方法很有用。


--------------------------------
## isCheckable()

返回类型：bool

属性 checkable 的获取器。


--------------------------------
## isChecked()

返回类型：bool

属性 checked 的获取器。


--------------------------------
## isFlat()

返回类型：bool

财产 单位 的 获得者 。


--------------------------------
## setAlignment(alignment)

参数：

- alignment – int


--------------------------------
## setCheckable(checkable)

参数：

- checkable – bool

属性 checkable 的设置者。


--------------------------------
## setChecked(checked)

参数：

- checked – bool

已检查属性的设置者。


--------------------------------
## setFlat(flat)

参数：

- flat – bool

物业单位设置者。


--------------------------------
## setTitle(title)

参数：

- title – str

财产所有权的设定者。


--------------------------------
## title()

返回类型：str

财产所有权的获取者。


--------------------------------
## toggled(arg__1)

参数：

- arg__1 – bool

如果组框是可勾选的，则在复选框被切换时发出此信号。如果复选框被勾选，则 on 为 true；否则为 false。

属性 checked 的通知信号。

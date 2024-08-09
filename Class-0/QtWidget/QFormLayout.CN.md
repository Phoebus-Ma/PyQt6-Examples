
[English doc](QFormLayout.md)

# class QFormLayout

QFormLayout 类管理输入小部件的形式及其相关标签。


# Synopsis

## Properties

- [fieldGrowthPolicy](#property-fieldgrowthpolicy--qformlayoutfieldgrowthpolicy)

    表单字段的增长方式。

- [formAlignment](#property-formalignment--combination-of-qtalignmentflag)

    表单布局内容在布局几何形状内的对齐方式。

- [horizontalSpacing](#property-horizontalspacing--int)

    并排布局的小部件之间的间距。

- [labelAlignment](#property-labelalignment--combination-of-qtalignmentflag)

    标签的水平对齐方式。

- [rowWrapPolicy](#property-rowwrappolicy--qformlayoutrowwrappolicy)

    表单行换行的方式。

- [verticalSpacing](#property-verticalspacing--int)

    垂直布局的小部件之间的间距。


## Methods

- [def __init__()](#initparentnone)

- [def addRow()](#addrowlabel-field)

- [def fieldGrowthPolicy()](#fieldgrowthpolicy)

- [def formAlignment()](#formalignment)

- [def getItemPosition()](#getitempositionindex)

- [def getLayoutPosition()](#getlayoutpositionlayout)

- [def getWidgetPosition()](#getwidgetpositionwidget)

- [def horizontalSpacing()](#horizontalspacing)

- [def insertRow()](#insertrowrow-label-field)

- [def isRowVisible()](#isrowvisiblelayout)

- [def itemAt()](#itematrow-role)

- [def labelAlignment()](#labelalignment)

- [def labelForField()](#labelforfieldfield)

- [def removeRow()](#removerowwidget)

- [def rowCount()](#rowcount)

- [def rowWrapPolicy()](#rowwrappolicy)

- [def setFieldGrowthPolicy()](#setfieldgrowthpolicypolicy)

- [def setFormAlignment()](#setformalignmentalignment)

- [def setHorizontalSpacing()](#sethorizontalspacingspacing)

- [def setItem()](#setitemrow-role-item)

- [def setLabelAlignment()](#setlabelalignmentalignment)

- [def setLayout()](#setlayoutrow-role-layout)

- [def setRowVisible()](#setrowvisiblelayout-on)

- [def setRowWrapPolicy()](#setrowwrappolicypolicy)

- [def setVerticalSpacing()](#setverticalspacingspacing)

- [def setWidget()](#setwidgetrow-role-widget)

- [def takeRow()](#takerowlayout)

- [def verticalSpacing()](#verticalspacing)


# Detailed Description

QFormLayout 是一个便利的布局类，它以两列的形式布局其子项。左列由标签组成，右列由“字段”小部件（行编辑器、旋转框等）组成。

传统上，这种两列表格布局是使用 QGridLayout 实现的。QFormLayout 是一种更高级的替代方案，它具有以下优势：

- 遵守不同平台的外观和感觉指南。

    例如，macOS Aqua 和 KDE 指南规定标签应右对齐，而 Windows 和 GNOME 应用程序通常使用左对齐。

- 支持长行换行。

    对于具有小显示屏的设备，可以将 QFormLayout 设置为换行长行，甚至可以换行所有行。

- 用于创建标签字段对的便捷 API。

    接受 QString 和 QWidget * 的 addRow() 重载在后台创建 QLabel 并自动设置其伙伴。然后我们可以编写如下代码：

```python
formLayout = QFormLayout(self)
formLayout.addRow(tr("Name:"), nameLineEdit)
formLayout.addRow(tr("Email:"), emailLineEdit)
formLayout.addRow(tr("Age:"), ageSpinBox)
```

将其与以下使用 QGridLayout 编写的代码进行比较：

```python
gridLayout = QGridLayout(self)
nameLabel = QLabel(tr("Name:"))
nameLabel.setBuddy(nameLineEdit)
emailLabel = QLabel(tr("Name:"))
emailLabel.setBuddy(emailLineEdit)
ageLabel = QLabel(tr("Name:"))
ageLabel.setBuddy(ageSpinBox)
gridLayout.addWidget(nameLabel, 0, 0)
gridLayout.addWidget(nameLineEdit, 0, 1)
gridLayout.addWidget(emailLabel, 1, 0)
gridLayout.addWidget(emailLineEdit, 1, 1)
gridLayout.addWidget(ageLabel, 2, 0)
gridLayout.addWidget(ageSpinBox, 2, 1)
```

下表显示了不同样式的默认外观。

还可以通过调用 setLabelAlignment() 、 setFormAlignment() 、 setFieldGrowthPolicy() 和 setRowWrapPolicy() 单独覆盖表单样式。例如，要在所有平台上模拟 QMacStyle 的表单布局外观，但使用左对齐标签，您可以编写：

```python
formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
formLayout.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
formLayout.setLabelAlignment(Qt.AlignLeft)
```


--------------------------------
## class FieldGrowthPolicy

此枚举指定了可用于控制表单字段增长方式的不同策略。

| Constant                          | Description |
| --------------------------------- | ----------- |
| QFormLayout.FieldsStayAtSizeHint  | 字段永远不会超出其有效大小提示。这是 QMacStyle 的默认设置。 |
| QFormLayout.ExpandingFieldsGrow   | 水平尺寸策略为 Expanding 或 MinimumExpanding 的字段将增长以填充可用空间。其他字段不会超出其有效尺寸提示。这是 Plastique 的默认策略。 |
| QFormLayout.AllNonFixedFieldsGrow | 所有具有允许其增长的尺寸策略的字段都将增长以填充可用空间。这是大多数样式的默认策略。 |


--------------------------------
## class RowWrapPolicy

此枚举指定了可用于控制表单行换行方式的不同策略。

| Constant                 | Description |
| ------------------------ | ----------- |
| QFormLayout.DontWrapRows | 字段始终排列在其标签旁边。这是除 Qt Extended 样式之外的所有样式的默认策略。 |
| QFormLayout.WrapLongRows | 标签有足够的水平空间来容纳最宽的标签，其余空间分配给字段。如果字段对的最小大小比可用空间宽，则字段将换行到下一行。这是 Qt Extended 样式的默认策略。 |
| QFormLayout.WrapAllRows  | 字段始终布置在其标签下方。 |


--------------------------------
## class ItemRole

此枚举指定可能出现在一行中的小部件（或其他布局项）的类型。

| Constant                 | Description              |
| ------------------------ | ------------------------ |
| QFormLayout.LabelRole    | 标签小部件。              |
| QFormLayout.FieldRole    | 字段小部件。              |
| QFormLayout.SpanningRole | 跨越标签和字段列的小部件。 |


--------------------------------
## property fieldGrowthPolicy : QFormLayout.FieldGrowthPolicy

此属性保存表单字段的增长方式。

默认值取决于小部件或应用程序样式。对于 QMacStyle，默认值为 FieldsStayAtSizeHint ；对于 QCommonStyle 派生样式（如 Plastique 和 Windows），默认值为 ExpandingFieldsGrow ；对于 Qt Extended 样式，默认值为 AllNonFixedFieldsGrow 。

如果所有字段都无法增长且表单大小已调整，则根据当前表单对齐方式分配额外空间。

访问函数：

- fieldGrowthPolicy()
- setFieldGrowthPolicy()


--------------------------------
## property formAlignment : Combination of Qt.AlignmentFlag

此属性保存表单布局内容在布局几何图形内的对齐方式。

默认值取决于小部件或应用程序样式。对于 QMacStyle，默认值为 Qt::AlignHCenter | Qt::AlignTop；对于其他样式，默认值为 Qt::AlignLeft | Qt::AlignTop。

访问函数：

- formAlignment()
- setFormAlignment()


--------------------------------
## property horizontalSpacing : int

此属性保存并排布局的小部件之间的间距。

默认情况下，如果未明确设置值，则布局的水平间距将从父布局或父小部件的样式设置继承。

访问函数：

- horizontalSpacing()
- setHorizontalSpacing()


--------------------------------
## property labelAlignment : Combination of Qt.AlignmentFlag

此属性保存标签的水平对齐方式。

默认值取决于小部件或应用程序样式。对于 QCommonStyle 派生样式，除 QPlastiqueStyle 外，默认值为 Qt::AlignLeft；对于其他样式，默认值为 Qt::AlignRight。

访问函数：

- labelAlignment()
- setLabelAlignment()


--------------------------------
## property rowWrapPolicy : QFormLayout.RowWrapPolicy

此属性保存表单行换行的方式。

默认值取决于小部件或应用程序样式。对于 Qt Extended 样式，默认值为 WrapLongRows ；对于其他样式，默认值为 DontWrapRows 。

如果要将每个标签显示在其关联字段上方（而不是旁边），请将此属性设置为 WrapAllRows 。

访问函数：

- rowWrapPolicy()
- setRowWrapPolicy()


--------------------------------
## property verticalSpacing : int

此属性保存垂直布局的小部件之间的间距。

默认情况下，如果未明确设置任何值，则布局的垂直间距将从父布局或父小部件的样式设置继承。

访问函数：

- verticalSpacing()
- setVerticalSpacing()


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

使用给定的父窗口小部件构造新的表单布局。

布局直接设置为父窗口小部件的顶级布局。窗口小部件只能有一个顶级布局。它由 layout() 返回。


--------------------------------
## addRow(layout)

参数：

- layout – QLayout

这是一个重载函数。

在此表单布局的末尾添加指定的布局。布局跨越两列。


--------------------------------
## addRow(labelText, field)

参数：

- labelText – str
- field – QWidget

这是一个重载函数。

此重载会自动在后台创建一个 QLabel，其文本为 labelText。该字段设置为新 QLabel 的伙伴。


--------------------------------
## addRow(labelText, field)

参数：

- labelText – str
- field – QLayout

这是一个重载函数。

此重载会自动在后台创建一个 QLabel，并以 labelText 作为其文本。


--------------------------------
## addRow(label, field)

参数：

- label – QWidget
- field – QWidget

在此表单布局的底部添加一个新行，其中包含给定的标签和字段。


--------------------------------
## addRow(label, field)

参数：

- label – QWidget
- field – QLayout

这是一个重载函数。


--------------------------------
## addRow(widget)

参数：

- widget – QWidget

这是一个重载函数。

在此表单布局的末尾添加指定的小部件。小部件跨越两列。


--------------------------------
## fieldGrowthPolicy()

返回类型：FieldGrowthPolicy

属性 fieldGrowthPolicy 的 getter 。


--------------------------------
## formAlignment()

返回类型：Combination of AlignmentFlag

属性 formAlignment 的获取器。


--------------------------------
## getItemPosition(index)

参数：

- index – int

返回类型：PyObject

检索指定索引处项目的行和角色（列）。如果索引超出范围，则将 *``rowPtr`` 设置为 -1；否则将行存储在 *``rowPtr`` 中，将角色存储在 *``rolePtr`` 中。


--------------------------------
## getLayoutPosition(layout)

参数：

- layout – QLayout

返回类型：PyObject

检索指定子布局的行和角色（列）。如果布局不在表单布局中，则将*``rowPtr``设置为 -1；否则将行存储在*``rowPtr``中，将角色存储在*``rolePtr``中。


--------------------------------
## getWidgetPosition(widget)

参数：

- widget – QWidget

返回类型：PyObject

检索布局中指定窗口小部件的行和角色（列）。如果窗口小部件不在布局中，则将 *``rowPtr`` 设置为 -1；否则将行存储在 *``rowPtr`` 中，将角色存储在 *``rolePtr`` 中。


--------------------------------
## horizontalSpacing()

返回类型：int

属性 Horizo​​ntalSpacing 的获取器。


--------------------------------
## insertRow(row, label, field)

参数：

- row – int
- label – QWidget
- field – QLayout

这是一个重载函数。


--------------------------------
## insertRow(row, labelText, field)

参数：

- row – int
- labelText – str
- field – QWidget

这是一个重载函数。

此重载会自动在后台创建一个 QLabel，其文本为 labelText。该字段设置为新 QLabel 的伙伴。


--------------------------------
## insertRow(row, labelText, field)

参数：

- row – int
- labelText – str
- field – QLayout

这是一个重载函数。

此重载会自动在后台创建一个 QLabel，并以 labelText 作为其文本。


--------------------------------
## insertRow(row, widget)

参数：

- row – int
- widget – QWidget

这是一个重载函数。

在此表单布局中的行位置插入指定的小部件。小部件跨越两列。如果行超出范围，则将小部件添加到末尾。


--------------------------------
## insertRow(row, label, field)

参数：

- row – int
- label – QWidget
- field – QWidget

在此表单布局中的 row 位置插入一个新行，并带有给定的标签和字段。如果 row 超出范围，则将新行添加到末尾。


--------------------------------
## insertRow(row, layout)

参数：

- row – int
- layout – QLayout

这是一个重载函数。

在此表单布局的行位置插入指定的布局。布局跨越两列。如果行超出范围，则将小部件添加到末尾。


--------------------------------
## isRowVisible(layout)

参数：

- layout – QLayout

返回类型：bool

这是一个重载函数。

如果布局对应的行中的某些项目可见，则返回 true，否则返回 false。


--------------------------------
## isRowVisible(widget)

参数：

- widget – QWidget

返回类型：bool

这是一个重载函数。

如果小部件对应的行中的某些项目可见，则返回 true，否则返回 false。


--------------------------------
## isRowVisible(row)

参数：

- row – int

返回类型：bool

如果行中的某些项目可见，则返回 true，否则返回 false。


--------------------------------
## itemAt(row, role)

参数：

- row – int
- role – ItemRole

返回类型：QLayoutItem

返回给定行中具有指定角色（列）的布局项。如果不存在这样的项，则返回 None。


--------------------------------
## labelAlignment()

返回类型：Combination of AlignmentFlag

属性 labelAlignment 的获取器。


--------------------------------
## labelForField(field)

参数：

- field – QWidget

返回类型：QWidget

返回与给定字段关联的标签。


--------------------------------
## labelForField(field)

参数：

- field – QLayout

返回类型：QWidget

这是一个重载函数。


--------------------------------
## removeRow(layout)

参数：

- layout – QLayout

这是一个重载函数。

从此表单布局中删除与布局对应的行。

调用此函数后，rowCount() 减一。 占用此行的所有小部件和嵌套布局都将被删除。 包括字段小部件和标签（如果有）。 所有后续行都上移一行，释放的垂直空间将在剩余行中重新分配。

您可以使用此函数撤消上一个 addRow() 或 insertRow() ：

```python
flay = ...
vbl = QVBoxLayout()
flay.insertRow(2, "User:", vbl)
# later:
flay.removeRow(layout) # vbl == None at this point
```

如果您想从表单布局中删除行而不删除插入的布局，请改用 takeRow()。


--------------------------------
## removeRow(widget)

参数：

- widget – QWidget

这是一个重载函数。

从此表单布局中删除与 widget 对应的行。

调用此函数后，rowCount() 减一。占用此行的所有 widget 和嵌套布局都将被删除。这包括字段 widget 和标签（如果有）。所有后续行都上移一行，释放的垂直空间将在剩余行中重新分配。

您可以使用此函数撤消上一个 addRow() 或 insertRow() ：

```python
flay = ...
le = QLineEdit()
flay.insertRow(2, "User:", le)
# later:
flay.removeRow(le) # le == None at this point
```

如果您想从布局中删除行而不删除小部件，请改用 takeRow()。


--------------------------------
## removeRow(row)

参数：

- row – int

从此表单布局中删除行 row。

row 必须为非负数且小于 rowCount() 。

调用此函数后， rowCount() 减一。占用此行的所有小部件和嵌套布局都将被删除。这包括字段小部件和标签（如果有）。所有后续行都上移一行，释放的垂直空间将在剩余行中重新分配。

您可以使用此函数撤消上一个 addRow() 或 insertRow() ：

```python
flay = ...
le = QLineEdit()
flay.insertRow(2, "User:", le)
# later:
flay.removeRow(2) # le == None at this point
```

如果您想从布局中删除行而不删除小部件，请改用 takeRow()。


--------------------------------
## rowCount()

返回类型：int

返回表单中的行数。


--------------------------------
## rowWrapPolicy()

返回类型：RowWrapPolicy

属性 rowWrapPolicy 的获取器。


--------------------------------
## setFieldGrowthPolicy(policy)

参数：

- policy – FieldGrowthPolicy

属性 fieldGrowthPolicy 的设置者。


--------------------------------
## setFormAlignment(alignment)

参数：

- alignment – Combination of AlignmentFlag

属性 formAlignment 的设置器。


--------------------------------
## setHorizontalSpacing(spacing)

参数：

- spacing – int

属性 Horizo​​ntalSpacing 的设置器。


--------------------------------
## setItem(row, role, item)

参数：

- row – int
- role – ItemRole
- item – QLayoutItem

将给定角色的给定行中的项目设置为 item，必要时使用空行扩展布局。

如果单元格已被占用，则不会插入该项目，并向控制台发送错误消息。该项目跨越两列。


--------------------------------
## setLabelAlignment(alignment)

参数：

- alignment – Combination of AlignmentFlag

属性 labelAlignment 的设置器。


--------------------------------
## setLayout(row, role, layout)

参数：

- row – int
- role – ItemRole
- layout – QLayout

将给定角色的给定行中的子布局设置为布局，必要时使用空行扩展表单布局。

如果单元格已被占用，则不会插入布局，并向控制台发送错误消息。


--------------------------------
## setRowVisible(layout, on)

参数：

- layout – QLayout
- on – bool

这是一个重载函数。

如果 on 为真，则显示与布局对应的行，否则隐藏该行。


--------------------------------
## setRowVisible(widget, on)

参数：

- widget – QWidget
- on – bool

这是一个重载函数。

如果 on 为真，则显示与小部件对应的行，否则隐藏该行。


--------------------------------
## setRowVisible(row, on)

参数：

- row – int
- on – bool

如果 on 为真则显示该行，否则隐藏该行。

row 必须为非负数且小于 rowCount() 。


--------------------------------
## setRowWrapPolicy(policy)

参数：

- policy – RowWrapPolicy

属性 rowWrapPolicy 的设置者。


--------------------------------
## setVerticalSpacing(spacing)

参数：

- spacing – int

属性 verticalSpacing 的设置器。


--------------------------------
## setWidget(row, role, widget)

参数：

- row – int
- role – ItemRole
- widget – QWidget

将给定角色的给定行中的小部件设置为小部件，如有必要，使用空行扩展布局。

如果单元格已被占用，则不会插入小部件，并向控制台发送错误消息。


--------------------------------
## takeRow(layout)

参数：

- layout – QLayout

返回类型：TakeRowResult

这是一个重载函数。

从此表单布局中删除指定的布局。

调用此函数后，rowCount() 会减一。所有后续行都会上移一行，释放的垂直空间会在剩余行之间重新分配。

```python
flay = ...
vbl = QVBoxLayout()
flay.insertRow(2, "User:", vbl)
# later:
QFormLayout.TakeRowResult result = flay.takeRow(widget)
```

如果要从表单布局中删除行并删除插入的布局，请改用 removeRow()。

返回包含小部件和相应标签布局项的结构。


--------------------------------
## takeRow(widget)

参数：

- widget – QWidget

返回类型：TakeRowResult

这是一个重载函数。

从此表单布局中删除指定的小部件。

调用此函数后，rowCount() 会减一。所有后续行都会上移一行，释放的垂直空间会在剩余行之间重新分配。

```python
flay = ...
le = QLineEdit()
flay.insertRow(2, "User:", le)
# later:
QFormLayout.TakeRowResult result = flay.takeRow(widget)
```

如果要从布局中删除行并删除小部件，请改用 removeRow()。

返回包含小部件和相应标签布局项的结构。


--------------------------------
## takeRow(row)

参数：

- row – int

返回类型：TakeRowResult

从此表单布局中删除指定的行。

row 必须为非负数且小于 rowCount() 。

调用此函数后， rowCount() 减一。所有后续行均上移一行，释放的垂直空间将在剩余行中重新分配。

您可以使用此函数撤消上一个 addRow() 或 insertRow() ：

```python
flay = ...
le = QLineEdit()
flay.insertRow(2, "User:", le)
# later:
QFormLayout.TakeRowResult result = flay.takeRow(2)
```

如果要从布局中删除行并删除小部件，请改用 removeRow()。

返回包含小部件和相应标签布局项的结构。


--------------------------------
## verticalSpacing()

返回类型：int

属性 verticalSpacing 的获取器。

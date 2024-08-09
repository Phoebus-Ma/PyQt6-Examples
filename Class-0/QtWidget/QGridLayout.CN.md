
[English doc](QGridLayout.md)

# class QGridLayout

QGridLayout 类在网格中布置小部件。


# Synopsis

## Methods

- [def \_\_init__()](#initparentnone)

- [def addItem()](#additemitem-row-column-rowspan1-columnspan1-alignmentqtalignment)

- [def addLayout()](#addlayoutarg__1-row-column-alignmentqtalignment)

- [def addWidget()](#addwidgetarg__1-row-column-alignmentqtalignment)

- [def cellRect()](#cellrectrow-column)

- [def columnCount()](#columncount)

- [def columnMinimumWidth()](#columnminimumwidthcolumn)

- [def columnStretch()](#columnstretchcolumn)

- [def getItemPosition()](#getitempositionidx)

- [def horizontalSpacing()](#horizontalspacing)

- [def itemAtPosition()](#itematpositionrow-column)

- [def originCorner()](#origincorner)

- [def rowCount()](#rowcount)

- [def rowMinimumHeight()](#rowminimumheightrow)

- [def rowStretch()](#rowstretchrow)

- [def setColumnMinimumWidth()](#setcolumnminimumwidthcolumn-minsize)

- [def setColumnStretch()](#setcolumnstretchcolumn-stretch)

- [def setDefaultPositioning()](#setdefaultpositioningn-orient)

- [def setHorizontalSpacing()](#sethorizontalspacingspacing)

- [def setOriginCorner()](#setorigincornerarg__1)

- [def setRowMinimumHeight()](#setrowminimumheightrow-minsize)

- [def setRowStretch()](#setrowstretchrow-stretch)

- [def setVerticalSpacing()](#setverticalspacingspacing)

- [def verticalSpacing()](#verticalspacing)


# Detailed Description

QGridLayout 占用提供给它的空间（由其父布局或 parentWidget() 提供），将其划分为行和列，并将其管理的每个小部件放入正确的单元格中。

列和行的行为相同；我们将讨论列，但行也有等效函数。

每列都有一个最小宽度和一个拉伸因子。最小宽度是使用 setColumnMinimumWidth() 设置的最小宽度和该列中每个小部件的最小宽度中的最大值。拉伸因子使用 setColumnStretch() 设置，并确定列将获得多少可用空间超过其必要的最小值。

通常，每个管理的小部件或布局都使用 addWidget() 放入自己的单元格中。小部件也可以使用 addItem() 和 addWidget() 的行和列跨越重载来占据多个单元格。如果这样做，QGridLayout 将猜测如何在列/行上分配大小（基于拉伸因子）。

要从布局中删除小部件，请调用 removeWidget() 。在小部件上调用 hide() 也会有效地从布局中移除小部件，直到调用 show()。

此图显示了一个对话框片段，其中包含一个五列、三行网格（网格以洋红色显示）：

此对话框片段中的第 0、2 和 4 列由 QLabel、QLineEdit 和 QListBox 组成。第 1 列和第 3 列是使用 setColumnMinimumWidth() 创建的占位符。第 0 行包含三个 QLabel 对象，第 1 行包含三个 QLineEdit 对象，第 2 行包含三个 QListBox 对象。我们使用占位符列（1 和 3）来获得列之间正确的空间量。

请注意，列和行的宽度和高度并不相同。如果您希望两列具有相同的宽度，则必须自行将其最小宽度和拉伸因子设置为相同。您可以使用 setColumnMinimumWidth() 和 setColumnStretch() 执行此操作。

如果 QGridLayout 不是顶层布局（即不管理所有小部件的区域和子项），则必须在创建它时将其添加到其父布局中，但在对其进行任何操作之前。添加布局的正常方法是在父布局上调用 addLayout()。

添加布局后，您可以使用 addWidget() 、 addItem() 和 addLayout() 将小部件和其他布局放入网格布局的单元格中。

QGridLayout 还包括两个边距宽度：内容边距和间距()。内容边距是 QGridLayout 四边的保留空间的宽度。间距() 是相邻框之间自动分配的间距的宽度。

默认内容边距值由 style 提供。Qt 样式指定的默认值为子小部件的 9 和窗口的 11。间距默认与顶层布局的边距宽度相同，或与父布局相同。


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

使用父窗口小部件 parent 构造一个新的 QGridLayout。布局最初有一行和一列，插入新项目时会扩展。

布局直接设置为父级的顶级布局。窗口小部件只能有一个顶级布局。它由 layout() 返回。

如果 parent 为 None，则必须将此网格布局插入另一个布局，或使用 setLayout() 将其设置为窗口小部件的布局。


--------------------------------
## addItem(item, row, column[, rowSpan=1[, columnSpan=1[, alignment=Qt.Alignment()]]])

参数：

- item – QLayoutItem
- row – int
- column – int
- rowSpan – int
- columnSpan – int
- alignment – Combination of AlignmentFlag

在 row、column 位置添加项目，跨越 rowSpan 行和 columnSpan 列，并根据对齐方式对其进行对齐。如果 rowSpan 和/或 columnSpan 为 -1，则项目将分别延伸到底部和/或右边缘。布局拥有该项目的所有权。


--------------------------------
## addLayout(arg__1, row, column[, alignment=Qt.Alignment()])

参数：

- arg__1 – QLayout
- row – int
- column – int
- alignment – Combination of AlignmentFlag

将布局放置在网格中的 (row, column) 位置。左上角位置为 (0, 0)。

对齐由 alignment 指定。默认对齐为 0，这意味着小部件填充整个单元格。

非零对齐表示布局不应增长以填充可用空间，而应根据 sizeHint() 调整大小。

布局成为网格布局的子项。


--------------------------------
## addLayout(arg__1, row, column, rowSpan, columnSpan[, alignment=Qt.Alignment()])

参数：

- arg__1 – QLayout
- row – int
- column – int
- rowSpan – int
- columnSpan – int
- alignment – Combination of AlignmentFlag

这是一个重载函数。

此版本将布局添加到单元格网格，跨越多行/列。单元格将从行开始，列跨越 rowSpan 行和 columnSpan 列。

如果 rowSpan 和/或 columnSpan 为 -1，则布局将分别延伸到底部和/或右边缘。

--------------------------------
## addWidget(arg__1, row, column[, alignment=Qt.Alignment()])

参数：

- arg__1 – QWidget
- row – int
- column – int
- alignment – Combination of AlignmentFlag

将给定的小部件添加到单元格网格的行、列处。默认情况下，左上角位置为 (0, 0)。

对齐方式由对齐方式指定。默认对齐方式为 0，这意味着小部件填充整个单元格。


--------------------------------
## addWidget(arg__1, row, column, rowSpan, columnSpan[, alignment=Qt.Alignment()])

参数：

- arg__1 – QWidget
- row – int
- column – int
- rowSpan – int
- columnSpan – int
- alignment – Combination of AlignmentFlag

这是一个重载函数。

此版本将给定的小部件添加到单元格网格，跨越多行/列。单元格将从 fromRow、fromColumn 开始，跨越 rowSpan 行和 columnSpan 列。小部件将具有给定的对齐方式。

如果 rowSpan 和/或 columnSpan 为 -1，则小部件将分别延伸到底部和/或右侧边缘。


--------------------------------
## cellRect(row, column)

参数：

- row – int
- column – int

返回类型：QRect

返回网格中行 row 和列 column 单元格的几何形状。如果行或列超出网格范围，则返回无效矩形。


--------------------------------
## columnCount()

返回类型：int

返回此网格中的列数。


--------------------------------
## columnMinimumWidth(column)

参数：

- column – int

返回类型：int

返回列的列间距。


--------------------------------
## columnStretch(column)

参数：

- column – int

返回类型：int

返回列的拉伸因子。


--------------------------------
## getItemPosition(idx)

参数：

- idx – int

返回类型：PyObject*

返回具有给定索引的项目的位置信息。

作为行和列传递的变量将使用布局中项目的位置进行更新，rowSpan 和 columnSpan 变量将使用项目的垂直和水平跨度进行更新。


--------------------------------
## horizontalSpacing()

返回类型：int


--------------------------------
## itemAtPosition(row, column)

参数：

- row – int
- column – int

返回类型：QLayoutItem

返回占据单元格（行、列）的布局项，如果单元格为空，则返回 None。


--------------------------------
## originCorner()

返回类型：Corner

返回用于网格原点的角，即位置 (0, 0)。


--------------------------------
## rowCount()

返回类型：int

返回此网格中的行数。


--------------------------------
## rowMinimumHeight(row)

参数：

- row – int

返回类型：int

返回为行设置的最小宽度。


--------------------------------
## rowStretch(row)

参数：

- row – int

返回类型：int

返回行 row 的拉伸因子。


--------------------------------
## setColumnMinimumWidth(column, minSize)

参数：

- column – int
- minSize – int

将列的最小宽度设置为 minSize 像素。


--------------------------------
## setColumnStretch(column, stretch)

参数：

- column – int
- stretch – int

将列的拉伸因子设置为拉伸。第一列为数字 0。

拉伸因子与此网格中的其他列相关。拉伸因子较高的列占用更多可用空间。

默认拉伸因子为 0。如果拉伸因子为 0，并且此表中的其他列都无法增长，则该列仍可能增长。

另一种方法是使用带有 QSpacerItem 的 addItem() 添加间距。


--------------------------------
## setDefaultPositioning(n, orient)

参数：

- n – int
- orient – Orientation


--------------------------------
## setHorizontalSpacing(spacing)

参数：

- spacing – int


--------------------------------
## setOriginCorner(arg__1)

参数：

- arg__1 – Corner

将网格的原点角（即位置 (0, 0)）设置为角。


--------------------------------
## setRowMinimumHeight(row, minSize)

参数：

- row – int
- minSize – int

将行的最小高度设置为 minSize 像素。


--------------------------------
## setRowStretch(row, stretch)

参数：

- row – int
- stretch – int

将行的拉伸因子设置为拉伸。第一行是数字 0。

拉伸因子是相对于此网格中的其他行。拉伸因子越高的行占用的可用空间越多。

默认拉伸因子为 0。如果拉伸因子为 0，并且此表中的其他行都无法增长，则该行仍可能增长。


--------------------------------
## setVerticalSpacing(spacing)

参数：

- spacing – int


--------------------------------
## verticalSpacing()

返回类型：int

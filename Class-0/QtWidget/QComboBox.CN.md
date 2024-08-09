
[English doc](QComboBox.md)

# class QComboBox

QComboBox 小部件将按钮与下拉列表结合在一起。


# Synopsis

## Properties

- [count](#property-count--int)

    组合框中的项目数。

- [currentData](#property-currentdata--object)

    当前项目的数据。

- [currentIndex](#property-currentindex--int)

    组合框中当前项目的索引。

- [currentText](#property-currenttext--str)

    当前文本。

- [duplicatesEnabled](#property-duplicatesenabled--bool)

    用户是否可以在组合框中输入重复的项目。

- [editable](#property-editable--bool)

    组合框是否可以由用户编辑。

- [frame](#property-frame--bool)

    组合框是否用框架绘制自身。

- [iconSize](#property-iconsize--qsize)

    组合框中显示的图标的大小。

- [insertPolicy](#property-insertpolicy--qcomboboxinsertpolicy)

    该策略用于确定用户插入的项目应出现在组合框中的何处。

- [maxCount](#property-maxcount--int)

    组合框中允许的最大项目数。

- [maxVisibleItems](#property-maxvisibleitems--int)

    组合框在屏幕上允许的最大尺寸，以项目为单位。

- [minimumContentsLength](#property-minimumcontentslength--int)

    组合框中应容纳的最小字符数。

- [modelColumn](#property-modelcolumn--int)

    模型中可见的列。

- [placeholderText](#property-placeholdertext--str)

    设置在未设置有效索引时显示的占位符文本。

- [sizeAdjustPolicy](#property-sizeadjustpolicy--qcomboboxsizeadjustpolicy)

    描述当内容改变时组合框的大小如何变化的策略。


## Methods

- [def \_\_init__()](#initparentnone)

- [def addItem()](#additemicon-text-userdatanone)

- [def addItems()](#additemstexts)

- [def completer()](#completer)

- [def count()](#count)

- [def currentData()](#currentdataroleqtuserrole)

- [def currentIndex()](#currentindex)

- [def currentText()](#currenttext)

- [def duplicatesEnabled()](#duplicatesenabled)

- [def findData()](#finddatadata-roleqtuserrole-flagsstatic_castqtmatchflagsqtmatchexactlyqtmatchcasesensitive)

- [def findText()](#findtexttext-flagsstatic_castqtmatchflagsqtmatchexactlyqtmatchcasesensitive)

- [def hasFrame()](#hasframe)

- [def iconSize()](#iconsize)

- [def inputMethodQuery()](#inputmethodqueryquery-argument)

- [def insertItem()](#insertitemindex-icon-text-userdatanone)

- [def insertItems()](#insertitemsindex-texts)

- [def insertPolicy()](#insertpolicy)

- [def insertSeparator()](#insertseparatorindex)

- [def isEditable()](#iseditable)

- [def itemData()](#itemdataindex-roleqtuserrole)

- [def itemDelegate()](#itemdelegate)

- [def itemIcon()](#itemiconindex)

- [def itemText()](#itemtextindex)

- [def lineEdit()](#lineedit)

- [def maxCount()](#maxcount)

- [def maxVisibleItems()](#maxvisibleitems)

- [def minimumContentsLength()](#minimumcontentslength)

- [def model()](#model)

- [def modelColumn()](#modelcolumn)

- [def placeholderText()](#placeholdertext)

- [def removeItem()](#removeitemindex)

- [def rootModelIndex()](#rootmodelindex)

- [def setCompleter()](#setcompleterc)

- [def setDuplicatesEnabled()](#setduplicatesenabledenable)

- [def setEditable()](#seteditableeditable)

- [def setFrame()](#setframearg__1)

- [def setIconSize()](#seticonsizesize)

- [def setInsertPolicy()](#setinsertpolicypolicy)

- [def setItemData()](#setitemdataindex-value-roleqtuserrole)

- [def setItemDelegate()](#setitemdelegatedelegate)

- [def setItemIcon()](#setitemiconindex-icon)

- [def setItemText()](#setitemtextindex-text)

- [def setLineEdit()](#setlineeditedit)

- [def setMaxCount()](#setmaxcountmax)

- [def setMaxVisibleItems()](#setmaxvisibleitemsmaxitems)

- [def setMinimumContentsLength()](#setminimumcontentslengthcharacters)

- [def setModelColumn()](#setmodelcolumnvisiblecolumn)

- [def setPlaceholderText()](#setplaceholdertextplaceholdertext)

- [def setRootModelIndex()](#setrootmodelindexindex)

- [def setSizeAdjustPolicy()](#setsizeadjustpolicypolicy)

- [def setValidator()](#setvalidatorv)

- [def setView()](#setviewitemview)

- [def sizeAdjustPolicy()](#sizeadjustpolicy)

- [def validator()](#validator)

- [def view()](#view)


## Virtual methods

- [def hidePopup()](#hidepopup)

- [def initStyleOption()](#initstyleoptionoption)

- [def setModel()](#setmodelmodel)

- [def showPopup()](#showpopup)


## Slots

- [def clear()](#clear)

- [def clearEditText()](#clearedittext)

- [def setCurrentIndex()](#setcurrentindexindex)

- [def setCurrentText()](#setcurrenttexttext)

- [def setEditText()](#setedittexttext)


## Signals

- [def activated()](#activatedindex)

- [def currentIndexChanged()](#currentindexchangedindex)

- [def currentTextChanged()](#currenttextchangedarg__1)

- [def editTextChanged()](#edittextchangedarg__1)

- [def highlighted()](#highlightedindex)

- [def textActivated()](#textactivatedarg__1)

- [def textHighlighted()](#texthighlightedarg__1)


# Detailed Description

## Display Features

QComboBox 是一种向用户呈现选项列表的紧凑方式。

组合框是一个选择小部件，它显示当前项目，并在单击时弹出可选项目的列表。如果 insertItem() 和 setItemText() 函数适当重载，组合框可以包含像素图和字符串。


## Editing Features

组合框可以是可编辑的，允许用户修改列表中的每个项目。对于可编辑组合框，提供了 clearEditText() 函数，用于清除显示的字符串而不更改组合框的内容。

当用户在可编辑组合框中输入新字符串时，小部件可能会或可能不会插入它，并且可以将其插入到多个位置。默认策略是 InsertAtBottom，但您可以使用 setInsertPolicy() 更改它。

可以使用 QValidator 将输入限制为可编辑组合框；请参阅 setValidator() 。默认情况下，接受任何输入。

可以使用插入函数（例如 insertItem() 和 insertItems()）填充组合框。可以使用 setItemText() 更改项目。可以使用 removeItem() 删除项目，可以使用 clear() 删除所有项目。当前项目的文本由 currentText() 返回，编号项目的文本由 text() 返回。可以使用 setCurrentIndex() 设置当前项目。组合框中的项目数由 count() 返回；可以使用 setMaxCount() 设置最大项目数。您可以使用 setEditable() 允许编辑。对于可编辑组合框，您可以使用 setCompleter() 设置自动完成，并使用 setDuplicatesEnabled() 设置用户是否可以添加重复项。


## Signals

如果组合框的当前项发生变化，则会发出三个信号： currentIndexChanged() 、 currentTextChanged() 和 activated() 。 currentIndexChanged() 和 currentTextChanged() 始终会发出，无论更改是通过编程完成还是通过用户交互完成，而 activated() 仅在更改由用户交互引起时才会发出。当用户突出显示组合框弹出列表中的某项时，会发出 highlighting() 信号。所有这三个信号都有两个版本，一个带有 QString 参数，另一个带有 int 参数。如果用户选择或突出显示像素图，则只会发出 int 信号。每当可编辑组合框的文本发生变化时，都会发出 editTextChanged() 信号。


## Model/View Framework

QComboBox 使用模型/视图框架来处理弹出列表并存储其项目。默认情况下，QStandardItemModel 存储项目，QListView 子类显示弹出列表。您可以直接访问模型和视图（使用 model() 和 view() ），但 QComboBox 还提供了设置和获取项目数据的函数，例如 setItemData() 和 itemText() 。您还可以设置新的模型和视图（使用 setModel() 和 setView() ）。对于组合框标签中的文本和图标，使用具有 Qt::DisplayRole 和 Qt::DecorationRole 的模型中的数据。


--------------------------------
## class InsertPolicy

这个枚举指定当用户输入新字符串时 QComboBox 应该做什么。

| Constant                       | Description                            |
| ------------------------------ | -------------------------------------- |
| QComboBox.NoInsert             | 该字符串将不会插入到组合框中。            |
| QComboBox.InsertAtTop          | 该字符串将作为组合框中的第一个项目插入。   |
| QComboBox.InsertAtCurrent      | 当前项目将被字符串替换。                 |
| QComboBox.InsertAtBottom       | 该字符串将插入到组合框中的最后一项之后。   |
| QComboBox.InsertAfterCurrent   | 该字符串插入到组合框中的当前项之后。      |
| QComboBox.InsertBeforeCurrent  | 该字符串插入到组合框中的当前项之前。      |
| QComboBox.InsertAlphabetically | 该字符串按字母顺序插入组合框中。          |


--------------------------------
## class SizeAdjustPolicy

此枚举指定当添加新内容或内容改变时，QComboBox 的大小提示应如何调整。

| Constant                              | Description                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| QComboBox.AdjustToContents            | 组合框将始终根据内容进行调整。                                                        |
| QComboBox.AdjustToContentsOnFirstShow | 组合框将在第一次显示时调整其内容。                                                     |
| QComboBox.AdjustToMinimumContentsLengthWithIcon | 组合框将调整为最小内容长度加上图标空间。出于性能原因，请在大型模型上使用此策略。 |


--------------------------------
## property count : int

此属性保存组合框中的项目数。

默认情况下，对于空组合框，此属性的值为 0。

访问函数：

- count()


--------------------------------
## property currentData : object

此属性保存当前项的数据。

默认情况下，对于空组合框或未设置当前项的组合框，此属性包含无效的 QVariant。

访问函数：

- currentData()


--------------------------------
## property currentIndex : int

此属性保存组合框中当前项目的索引。

插入或删除项目时，当前索引可能会发生变化。

默认情况下，对于空组合框或未设置当前项目的组合框，此属性的值为 -1。

访问函数：

- currentIndex()
- setCurrentIndex()
- Signal currentIndexChanged()


--------------------------------
## property currentText : str

此属性保存当前文本。

如果组合框可编辑，则当前文本是行编辑显示的值。否则，它是当前项的值，如果组合框为空或未设置当前项，则为空字符串。

如果组合框可编辑，setter setCurrentText() 只需调用 setEditText()。否则，如果列表中有匹配的文本，则将 currentIndex 设置为相应的索引。

访问函数：

- currentText()
- setCurrentText()
- Signal currentTextChanged()


--------------------------------
## property duplicatesEnabled : bool

此属性控制用户是否可以将重复项输入到组合框中。

请注意，始终可以通过编程将重复项插入到组合框中。

默认情况下，此属性为 false（不允许重复）。

访问函数：

- duplicatesEnabled()
- setDuplicatesEnabled()


--------------------------------
## property editable : bool

此属性保存组合框是否可由用户编辑。

默认情况下，此属性为 false。编辑的效果取决于插入策略。

访问函数：

- isEditable()
- setEditable()


--------------------------------
## property frame : bool

此属性保存组合框是否使用框架绘制自身。

如果启用（默认），组合框将在框架内绘制自身，否则组合框将在没有任何框架的情况下绘制自身。

访问函数：

- hasFrame()
- setFrame()


--------------------------------
## property iconSize : QSize

此属性保存组合框中显示的图标的大小。

除非明确设置，否则将返回当前样式的默认值。此大小是图标可以具有的最大尺寸；较小尺寸的图标不会放大。

访问函数：

- iconSize()
- setIconSize()


--------------------------------
## property insertPolicy : QComboBox.InsertPolicy

此属性保存用于确定用户插入的项目应出现在组合框中何处的策略。

默认值为 InsertAtBottom ，表示新项目将出现在项目列表的底部。

访问函数：

- insertPolicy()
- setInsertPolicy()


--------------------------------
## property maxCount : int

此属性保存组合框中允许的最大项目数。

默认情况下，此属性的值来自可用的最高有符号整数（通常为 2147483647）。

访问函数：

- maxCount()
- setMaxCount()


--------------------------------
## property maxVisibleItems : int

此属性保存组合框在屏幕上允许的最大尺寸（以项目为单位）。

默认情况下，此属性的值为 10。

访问函数：

- maxVisibleItems()
- setMaxVisibleItems()


--------------------------------
## property minimumContentsLength : int

此属性保存组合框中应容纳的最小字符数。

默认值为 0。

如果将此属性设置为正值，则 minimumSizeHint() 和 sizeHint() 会将其考虑在内。

访问函数：

- minimumContentsLength()
- setMinimumContentsLength()


--------------------------------
## property modelColumn : int

此属性保存模型中可见的列。

如果在填充组合框之前设置，弹出视图将不受影响并显示第一列（使用此属性的默认值）。

默认情况下，此属性的值为 0。

访问函数：

- modelColumn()
- setModelColumn()


--------------------------------
## property placeholderText : str

此属性用于设置未设置有效索引时显示的占位符文本。

设置无效索引时将显示占位符文本。下拉列表中无法访问该文本。在添加项目之前调用此函数时，将显示占位符文本，否则，如果您想显示占位符文本，则必须以编程方式调用 setCurrentIndex (-1)。设置空的占位符文本以重置设置。

当 QComboBox 可编辑时，请改用 setPlaceholderText()。

访问函数：

- placeholderText()
- setPlaceholderText()


--------------------------------
## property sizeAdjustPolicy : QComboBox.SizeAdjustPolicy

此属性保存描述当内容更改时组合框的大小如何更改的策略。

默认值为 AdjustToContentsOnFirstShow 。

访问函数：

- sizeAdjustPolicy()
- setSizeAdjustPolicy()


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

使用默认模型 QStandardItemModel 构造具有给定父级的组合框。


--------------------------------
## activated(index)

参数：

- index – int

当用户选择组合框中的项目时，会发送此信号。传递项目的索引。请注意，即使选项未更改，也会发送此信号。如果您需要知道选项何时实际更改，请使用信号 currentIndexChanged() 或 currentTextChanged() 。


--------------------------------
## addItem(text[, userData=None])

参数：

- text – str
- userData – object

使用给定的文本向组合框添加一个项目，并包含指定的用户数据（存储在 Qt::UserRole 中）。该项目将附加到现有项目列表中。


--------------------------------
## addItem(icon, text[, userData=None])

参数：

- icon – QIcon
- text – str
- userData – object

使用给定的图标和文本向组合框添加一个项目，并包含指定的用户数据（存储在 Qt::UserRole 中）。该项目将附加到现有项目列表中。


--------------------------------
## addItems(texts)

参数：

- texts – list of strings

将给定文本中的每个字符串添加到组合框。每个项目依次附加到现有项目的列表中。


--------------------------------
## clear()

清除组合框，删除所有项目。


--------------------------------
## clearEditText()

清除组合框中用于编辑的行编辑的内容。


--------------------------------
## completer()

返回类型：QCompleter

返回用于自动完成组合框文本输入的完成器。


--------------------------------
## count()

返回类型：int

属性 count 的获取器。


--------------------------------
## currentData([role=Qt.UserRole])

参数：

- role – int

返回类型：object


--------------------------------
## currentIndex()

返回类型：int

属性 currentIndex 的获取器。


--------------------------------
## currentIndexChanged(index)

参数：

- index – int

每当组合框中的 currentIndex 通过用户交互或编程发生变化时，都会发送此信号。如果组合框变为空或 currentIndex 被重置，则传递项目的索引或 -1。

属性 currentIndex 的通知信号。


--------------------------------
## currentText()

返回类型：str

属性 currentText 的获取器。


--------------------------------
## currentTextChanged(arg__1)

参数：

- arg__1 – str

每当 currentText 发生变化时，都会发出此信号。新值以文本形式传递。

属性 currentText 的通知信号。


--------------------------------
## duplicatesEnabled()

返回类型：bool

属性 duplicatesEnabled 的获取器。


--------------------------------
## editTextChanged(arg__1)

参数：

- arg__1 – str

当组合框的行编辑小部件中的文本发生更改时，会发出此信号。新文本由 text 指定。


--------------------------------
## findData(data[, role=Qt.UserRole[, flags=static_cast<Qt.MatchFlags>(Qt.MatchExactly|Qt.MatchCaseSensitive)]])

参数：

- data – object
- role – int
- flags – Combination of MatchFlag

返回类型：int

返回包含给定角色的给定数据的项目的索引；否则返回 -1。

标志指定如何搜索组合框中的项目。


--------------------------------
## findText(text[, flags=static_cast<Qt.MatchFlags>(Qt.MatchExactly|Qt.MatchCaseSensitive)])

参数：

- text – str
- flags – Combination of MatchFlag

返回类型：int

返回包含指定文本的项目的索引；否则返回 -1。

标志指定如何搜索组合框中的项目。


--------------------------------
## hasFrame()

返回类型：bool

属性框架的获取器。

--------------------------------
## hidePopup()

如果组合框中的项目列表当前可见，则隐藏它并重置内部状态，因此，如果自定义弹出窗口显示在重新实现的 showPopup() 中，那么您还需要重新实现 hidePopup() 函数来隐藏自定义弹出窗口，并在自定义弹出窗口小部件隐藏时调用基类实现来重置内部状态。


--------------------------------
## highlighted(index)

参数：

- index – int

当用户突出显示组合框弹出列表中的某项时，将发送此信号。传递该项的索引。


--------------------------------
## iconSize()

返回类型：QSize

属性 iconSize 的获取器。


--------------------------------
## initStyleOption(option)

参数：

- option – QStyleOptionComboBox

用此 QComboBox 中的值初始化选项。当子类需要 QStyleOptionComboBox 但又不想自己填写所有信息时，此方法非常有用。


--------------------------------
## inputMethodQuery(query, argument)

参数：

- query – InputMethodQuery
- argument – object

返回类型：object


--------------------------------
## insertItem(index, icon, text[, userData=None])

参数：

- index – int
- icon – QIcon
- text – str
- userData – object

将图标、文本和用户数据（存储在 Qt::UserRole 中）插入到给定索引处的组合框中。

如果索引等于或大于项目总数，则新项目将附加到现有项目列表中。 如果索引为零或负数，则新项目将附加到现有项目列表中。


--------------------------------
## insertItem(index, text[, userData=None])

参数：

- index – int
- text – str
- userData – object

将文本和用户数据（存储在 Qt::UserRole 中）插入到给定索引处的组合框中。

如果索引等于或大于项目总数，则新项目将附加到现有项目列表中。 如果索引为零或负数，则新项目将附加到现有项目列表中。


--------------------------------
## insertItems(index, texts)

参数：

- index – int
- texts – list of strings

从指定的索引开始，将列表中的字符串作为单独的项目插入到组合框中。

如果索引等于或大于项目总数，则新项目将附加到现有项目列表中。 如果索引为零或负数，则新项目将附加到现有项目列表中。


--------------------------------
## insertPolicy()

返回类型：InsertPolicy

属性 insertPolicy 的获取器。


--------------------------------
## insertSeparator(index)

参数：

- index – int

在给定索引处将分隔项插入组合框。

如果索引等于或大于项的总数，则新项将附加到现有项的列表中。 如果索引为零或负数，则新项将附加到现有项的列表中。


--------------------------------
## isEditable()

返回类型：bool

属性 editable 的获取器。


--------------------------------
## itemData(index[, role=Qt.UserRole])

参数：

- index – int
- role – int

返回类型：object

返回组合框中给定索引中给定角色的数据，如果此角色没有数据，则返回无效的 QVariant。


--------------------------------
## itemDelegate()

返回类型：QAbstractItemDelegate

返回弹出列表视图使用的项目委托。


--------------------------------
## itemIcon(index)

参数：

- index – int

返回类型：QIcon

返回组合框中给定索引的图标。


--------------------------------
## itemText(index)

参数：

- index – int

返回类型：str

返回组合框中给定索引的文本。


--------------------------------
## lineEdit()

返回类型：QLineEdit

返回用于编辑组合框中项目的行编辑，如果没有行编辑则返回 None。

只有可编辑的组合框才有行编辑。


--------------------------------
## maxCount()

返回类型：int

属性 maxCount 的获取方法。


--------------------------------
## maxVisibleItems()

返回类型：int

属性 maxVisibleItems 的获取器。


--------------------------------
## minimumContentsLength()

返回类型：int

属性 minimumContentsLength 的获取器。


--------------------------------
## model()

返回类型：QAbstractItemModel

返回组合框使用的模型。


--------------------------------
## modelColumn()

返回类型：int

属性 modelColumn 的获取方法。


--------------------------------
## placeholderText()

返回类型：str

属性 placeholderText 的获取方法。


--------------------------------
## removeItem(index)

参数：

- index – int

从组合框中删除给定索引处的项目。如果索引被删除，这将更新当前索引。

如果索引超出范围，则此函数不执行任何操作。


--------------------------------
## rootModelIndex()

返回类型：QModelIndex

返回组合框中项目的根模型项目索引。


--------------------------------
## setCompleter(c)

参数：

- c – QCompleter

设置要使用的补全器，而不是当前补全器。如果补全器为 None，则禁用自动补全。

默认情况下，对于可编辑组合框，会自动创建执行不区分大小写的内联补全的 QCompleter。


--------------------------------
## setCurrentIndex(index)

参数：

- index – int

currentIndex 属性的设置者。


--------------------------------
## setCurrentText(text)

参数：

- text – str

currentText 属性的设置器。


--------------------------------
## setDuplicatesEnabled(enable)

参数：

- enable – bool

属性 duplicatesEnabled 的设置者。


--------------------------------
## setEditText(text)

参数：

- text – str

设置组合框的文本编辑中的文本。


--------------------------------
## setEditable(editable)

参数：

- editable – bool

属性的设置者可编辑。


--------------------------------
## setFrame(arg__1)

参数：

- arg__1 – bool

属性框架的设置者。


--------------------------------
## setIconSize(size)

参数：

- size – QSize

属性 iconSize 的设置者。


--------------------------------
## setInsertPolicy(policy)

参数：

- policy – InsertPolicy

属性 insertPolicy 的设置者。


--------------------------------
## setItemData(index, value[, role=Qt.UserRole])

参数：

- index – int
- value – object
- role – int

将组合框中给定索引上的项目的数据角色设置为指定值。


--------------------------------
## setItemDelegate(delegate)

参数：

- delegate – QAbstractItemDelegate

设置弹出列表视图的项目委托。组合框拥有委托的所有权。

任何现有委托都将被移除，但不会被删除。QComboBox 不拥有委托的所有权。


--------------------------------
## setItemIcon(index, icon)

参数：

- index – int
- icon – QIcon

设置组合框中给定索引的项目的图标。


--------------------------------
## setItemText(index, text)

参数：

- index – int
- text – str

设置组合框中给定索引的项目的文本。


--------------------------------
## setLineEdit(edit)

参数：

- edit – QLineEdit

设置要使用的行编辑，而不是当前行编辑小部件。

组合框拥有行编辑的所有权。


--------------------------------
## setMaxCount(max)

参数：

- max – int

属性 maxCount 的设置者。


--------------------------------
## setMaxVisibleItems(maxItems)

参数：

- maxItems – int

属性 maxVisibleItems 的设置者。


--------------------------------
## setMinimumContentsLength(characters)

参数：

- characters – int

属性 minimumContentsLength 的设置者。


--------------------------------
## setModel(model)

参数：

- model – QAbstractItemModel

将模型设置为 model。model 不能为 None。如果要清除模型的内容，请调用 clear() 。


--------------------------------
## setModelColumn(visibleColumn)

参数：

- visibleColumn – int

属性 modelColumn 的设置器。


--------------------------------
## setPlaceholderText(placeholderText)

参数：

- placeholderText – str

属性 placeholderText 的设置者。


--------------------------------
## setRootModelIndex(index)

参数：

- index – QModelIndex

设置组合框中项目的根模型项目索引。


--------------------------------
## setSizeAdjustPolicy(policy)

参数：

- policy – SizeAdjustPolicy

属性 sizeAdjustPolicy 的设置者。


--------------------------------
## setValidator(v)

参数：

- v – QValidator

设置要使用的验证器来代替当前验证器。


--------------------------------
## setView(itemView)

参数：

- itemView – QAbstractItemView

将组合框弹出窗口中要使用的视图设置为给定的 itemView。组合框拥有该视图的所有权。

注意：如果您想要使用便利视图（如 QListWidget、QTableWidget 或 QTreeWidget），请确保在调用此函数之前使用便利小部件模型在组合框上调用 setModel()。


--------------------------------
## showPopup()

显示组合框中的项目列表。如果列表为空，则不会显示任何项目。

如果您重新实现此函数以显示自定义弹出窗口，请确保调用 hidePopup() 来重置内部状态。


--------------------------------
## sizeAdjustPolicy()

返回类型：SizeAdjustPolicy

属性 sizeAdjustPolicy 的获取器。


--------------------------------
## textActivated(arg__1)

参数：

- arg__1 – str

当用户选择组合框中的项目时，会发送此信号。传递项目的文本。请注意，即使选项未更改，也会发送此信号。如果您需要知道选项何时实际更改，请使用信号 currentIndexChanged() 或 currentTextChanged() 。


--------------------------------
## textHighlighted(arg__1)

参数：

- arg__1 – str

当用户突出显示组合框弹出列表中的某项时，会发送此信号。传递该项的文本。


--------------------------------
## validator()

返回类型：QValidator

返回用于约束组合框的文本输入的验证器。


--------------------------------
## view()

返回类型：QAbstractItemView

返回用于组合框弹出的列表视图。


[English doc](QLineEdit.md)

# class QLineEdit

QLineEdit 小部件是一个单行文本编辑器。


# Synopsis

## Properties

- [acceptableInput](#property-acceptableinput--bool)

    输入是否满足inputMask和validator。

- [alignment](#property-alignment--combination-of-qtalignmentflag)

    行的编辑。

- [clearButtonEnabled](#property-clearbuttonenabled--bool)

    当行编辑不为空时是否显示清除按钮。

- [cursorMoveStyle](#property-cursormovestyle--qtcursormovestyle)

    本行编辑中光标的移动风格。

- [cursorPosition](#property-cursorposition--int)

    此行编辑的当前光标位置。

- [displayText](#property-displaytext--str)

    显示的文本。

- [dragEnabled](#property-dragenabled--bool)

    当用户按下并移动鼠标到某些选定的文本上时，行编辑是否开始拖动。

- [echoMode](#property-echomode--qlineeditechomode)

    行编辑的回声模式。

- [frame](#property-frame--bool)

    线编辑是否用框架绘制自身。

- [hasSelectedText](#property-hasselectedtext--bool)

    是否选择了任何文本。

- [inputMask](#property-inputmask--str)

    验证输入掩码。

- [maxLength](#property-maxlength--int)

    文本的最大允许长度。

- [modified](#property-modified--bool)

    行编辑的内容是否已被用户修改。

- [placeholderText](#property-placeholdertext--str)

    行编辑的占位符文本。

- [readOnly](#property-readonly--bool)

    行编辑是否是只读的。

- [redoAvailable](#property-redoavailable--bool)

    是否可以重做。

- [selectedText](#property-selectedtext--str)

    选定的文本。

- [text](#property-text--str)

    行编辑的文本。

- [undoAvailable](#property-undoavailable--bool)

    是否可以撤消。


## Methods

- [def \_\_init__()](#initparentnone)

- [def addAction()](#addactionaction-position)

- [def alignment()](#alignment)

- [def backspace()](#backspace)

- [def completer()](#completer)

- [def createStandardContextMenu()](#createstandardcontextmenu)

- [def cursorBackward()](#cursorbackwardmark-steps1)

- [def cursorForward()](#cursorforwardmark-steps1)

- [def cursorMoveStyle()](#cursormovestyle)

- [def cursorPosition()](#cursorposition)

- [def cursorPositionAt()](#cursorpositionatpos)

- [def cursorRect()](#cursorrect)

- [def cursorWordBackward()](#cursorwordbackwardmark)

- [def cursorWordForward()](#cursorwordforwardmark)

- [def del_()](#del_)

- [def deselect()](#deselect)

- [def displayText()](#displaytext)

- [def dragEnabled()](#dragenabled)

- [def echoMode()](#echomode)

- [def end()](#endmark)

- [def hasAcceptableInput()](#hasacceptableinput)

- [def hasFrame()](#hasframe)

- [def hasSelectedText()](#hasselectedtext)

- [def home()](#homemark)

- [def inputMask()](#inputmask)

- [def inputMethodQuery()](#inputmethodqueryproperty-argument)

- [def insert()](#insertarg__1)

- [def isClearButtonEnabled()](#isclearbuttonenabled)

- [def isModified()](#ismodified)

- [def isReadOnly()](#isreadonly)

- [def isRedoAvailable()](#isredoavailable)

- [def isUndoAvailable()](#isundoavailable)

- [def maxLength()](#maxlength)

- [def placeholderText()](#placeholdertext)

- [def selectedText()](#selectedtext)

- [def selectionEnd()](#selectionend)

- [def selectionLength()](#selectionlength)

- [def selectionStart()](#selectionstart)

- [def setAlignment()](#setalignmentflag)

- [def setClearButtonEnabled()](#setclearbuttonenabledenable)

- [def setCompleter()](#setcompletercompleter)

- [def setCursorMoveStyle()](#setcursormovestylestyle)

- [def setCursorPosition()](#setcursorpositionarg__1)

- [def setDragEnabled()](#setdragenabledb)

- [def setEchoMode()](#setechomodearg__1)

- [def setFrame()](#setframearg__1)

- [def setInputMask()](#setinputmaskinputmask)

- [def setMaxLength()](#setmaxlengtharg__1)

- [def setModified()](#setmodifiedarg__1)

- [def setPlaceholderText()](#setplaceholdertextarg__1)

- [def setReadOnly()](#setreadonlyarg__1)

- [def setSelection()](#setselectionarg__1-arg__2)

- [def setTextMargins()](#settextmarginsmargins)

- [def setValidator()](#setvalidatorarg__1)

- [def text()](#text)

- [def textMargins()](#textmargins)

- [def validator()](#validator)


## Virtual methods

- [def initStyleOption()](#initstyleoptionoption)


## Slots

- [def clear()](#clear)

- [def copy()](#copy)

- [def cut()](#cut)

- [def paste()](#paste)

- [def redo()](#redo)

- [def selectAll()](#selectall)

- [def setText()](#settextarg__1)

- [def undo()](#undo)


## Signals

- [def cursorPositionChanged()](#cursorpositionchangedarg__1-arg__2)

- [def editingFinished()](#editingfinished)

- [def inputRejected()](#inputrejected)

- [def returnPressed()](#returnpressed)

- [def selectionChanged()](#selectionchanged)

- [def textChanged()](#textchangedarg__1)

- [def textEdited()](#texteditedarg__1)


# Detailed Description

行编辑允许用户输入和编辑一行纯文本，并具有有用的编辑功能，包括撤消和重做、剪切和粘贴以及拖放。

通过更改行编辑的 echoMode()，它还可以用作输入密码等的只写字段。

QTextEdit 是一个相关类，允许多行、富文本编辑。


## Constraining Text

使用 maxLength 定义文本的最大允许长度。您可以使用 inputMask 和 setValidator() 进一步限制文本内容。


## Editing Text

您可以使用 setText() 或 insert() 更改文本。使用 text() 检索文本，使用 displayText() 检索显示的文本（可能有所不同，请参阅 EchoMode）。您可以使用 setSelection() 或 selectAll() 选择文本，还可以 cut() 、 copy() 和 paste() 选定内容。要对齐文本，请使用 setAlignment() 。

当文本更改时，将发出 textChanged() 信号。当文本以除调用 setText() 以外的其他方式更改时，将发出 textEdited() 信号。当光标移动时，将发出 cursorPositionChanged() 信号。当选择 Return 或 Enter 键时，将发出 returnPressed() 信号。

当文本编辑完成时（因为行编辑失去焦点或选择了 Return/Enter 键），将发出 editingFinished() 信号。

如果行编辑焦点丢失且文本没有任何变化，则不会发出 editingFinished() 信号。

如果在行编辑中设置了验证器，则仅当验证器返回 QValidator::Acceptable 时，才会发出 returnPressed() / editingFinished() 信号。

有关 QLineEdit 的多种使用方式的更多信息，请参阅行编辑示例，其中还提供了一系列行编辑示例，展示了各种属性和验证器对用户提供的输入和输出的影响。


## Setting a Frame

默认情况下，QLineEdits 具有平台样式指南中指定的框架。您可以通过调用 setFrame (false) 关闭框架。


## Default Key Bindings

下表介绍了默认的键绑定。

任何其他代表有效字符的按键都将导致该字符插入到行编辑中。


--------------------------------
## class ActionPosition

此枚举类型描述了行编辑应如何显示要添加的操作小部件。

| Constant                   | Description |
| -------------------------- | ----------- |
| QLineEdit.LeadingPosition  | 当使用布局方向 Qt::LeftToRight 时，小部件显示在文本左侧；当使用 Qt::RightToLeft 时，小部件显示在文本右侧。 |
| QLineEdit.TrailingPosition | 当使用布局方向 Qt::LeftToRight 时，小部件显示在文本的右侧；当使用 Qt::RightToLeft 时，小部件显示在文本的左侧。 |


--------------------------------
## class EchoMode

此枚举类型描述了行编辑应如何显示其内容。

| Constant                     | Description |
| ---------------------------- | ----------- |
| QLineEdit.Normal             | 按输入的方式显示字符。这是默认设置。 |
| QLineEdit.NoEcho             | 不显示任何内容。这可能适用于密码长度也应保密的密码。 |
| QLineEdit.Password           | 显示与平台相关的密码掩码字符而不是实际输入的字符。 |
| QLineEdit.PasswordEchoOnEdit | 仅显示输入的字符。否则，显示与密码相同的字符。 |


--------------------------------
## property acceptableInput : bool

此属性保存输入是否满足 inputMask 和验证器。

默认情况下，此属性为 true。

访问函数：

- hasAcceptableInput()


--------------------------------
## property alignment : Combination of Qt.AlignmentFlag

此属性保存行编辑的对齐方式。

此处允许水平和垂直对齐，Qt::AlignJustify 将映射到 Qt::AlignLeft。

默认情况下，此属性包含 Qt::AlignLeft 和 Qt::AlignVCenter 的组合。

访问函数：

- alignment()
- setAlignment()


--------------------------------
## property clearButtonEnabled : bool

此属性保存当行编辑不为空时是否显示清除按钮。

如果启用，当行编辑包含一些文本时，它会显示尾随清除按钮。否则，行编辑不会显示清除按钮（默认）。

访问函数：

- isClearButtonEnabled()
- setClearButtonEnabled()


--------------------------------
## property cursorMoveStyle : Qt.CursorMoveStyle

此属性保存此行编辑中光标的移动样式。

当此属性设置为 Qt::VisualMoveStyle 时，行编辑将使用视觉移动样式。使用左箭头键将始终导致光标向左移动，无论文本的书写方向如何。右箭头键也适用相同的行为。

当此属性设置为 Qt::LogicalMoveStyle（默认值）时，在从左到右 (LTR) 的文本块中，使用左箭头键将增加光标位置，而使用右箭头键将减少光标位置。如果文本块是从右到左 (RTL)，则适用相反的行为。

访问函数：

- cursorMoveStyle()
- setCursorMoveStyle()


--------------------------------
## property cursorPosition : int

此属性保存此行编辑的当前光标位置。

设置光标位置会在适当的时候导致重新绘制。

默认情况下，此属性包含值为 0。

访问函数：

- cursorPosition()
- setCursorPosition()


--------------------------------
## property displayText : str

此属性保存显示的文本。

如果 echoMode 为 Normal ，则返回与 text() 相同的结果。如果 EchoMode 为 Password 或 PasswordEchoOnEdit ，则返回一串与平台相关的密码掩码字符（例如“******”）。如果 EchoMode 为 NoEcho ，则返回一个空字符串。

默认情况下，此属性包含一个空字符串。

访问函数：

- displayText()


--------------------------------
## property dragEnabled : bool

此属性保存当用户按下并移动鼠标到某些选定文本上时，行编辑是否开始拖动。

默认情况下，拖动功能处于禁用状态。

访问函数：

- dragEnabled()
- setDragEnabled()


--------------------------------
## property echoMode : QLineEdit.EchoMode

此属性保存行编辑的回显模式。

回显模式决定了行编辑中输入的文本如何显示（或回显）给用户。

最常见的设置是 Normal ，其中用户输入的文本将逐字显示。QLineEdit 还支持允许抑制或隐藏输入文本的模式：这些模式包括 NoEcho 、 Password 和 PasswordEchoOnEdit 。

小部件的显示以及复制或拖动文本的能力受此设置的影响。

默认情况下，此属性设置为 Normal 。

访问函数：

- echoMode()
- setEchoMode()


--------------------------------
## property frame : bool

此属性保存线编辑是否使用框架绘制自身。

如果启用（默认），线编辑将在框架内绘制自身。否则，线编辑将在没有任何框架的情况下绘制自身。

访问函数：

- hasFrame()
- setFrame()


--------------------------------
## property hasSelectedText : bool

此属性保存是否有任何文本被选中。

如果用户选择了部分或全部文本，hasSelectedText() 将返回 true。否则，它将返回 false。

默认情况下，此属性为 false。

访问函数：

- hasSelectedText()


--------------------------------
## property inputMask : str

此属性保存验证输入掩码。

设置 QLineEdit 的验证掩码。验证器可以代替掩码或与掩码一起使用；请参阅 setValidator() 。默认值为空字符串，表示不使用输入掩码。

要取消设置掩码并返回正常的 QLineEdit 操作，请传递一个空字符串。

输入掩码是输入模板字符串。它可以包含以下元素：

|                 |                                      |
| --------------- | ------------------------------------ |
| Mask Characters | 定义在此位置被视为有效的输入字符的类别。 |
| Meta Characters | 各种特殊含义（详见下文）。              |
| Separators      | 所有其他字符都被视为不可变的分隔符。     |

下表显示了输入掩码中可以使用的掩码和元字符。

| Mask Character | Meaning                                       |
| -------------- | --------------------------------------------- |
| A              | 必填字母类别的字符，例如 A-Z、a-z。              |
| a              | 允许但不是必须的字母类别的字符。                 |
| N              | 必需的字母或数字类别的字符，例如 A-Z、a-z、0-9。  |
| n              | 允许但不是必须的字母或数字类别的字符。            |
| X              | 需要任何非空白字符。                            |
| x              | 允许但不是必须的任何非空白字符。                 |
| 9              | 必填数字类别的字符，例如0-9。                    |
| 0              | 允许但不是必须的数字类别的字符。                 |
| D              | 必须为数字类别且大于零的字符，例如1-9。           |
| d              | 数字类别的字符，允许但不要求大于零，例如 1-9。    |
| #              | 数字类别的字符，或者加号/减号，允许但不要求。     |
| H              | 需要十六进制字符。A-F、a-f、0-9。               |
| h              | 允许但不是必须的十六进制字符。                   |
| B              | 需要二进制字符。0-1。                           |
| b              | 允许但不是必需的二进制字符。                     |

| Meta Character | Meaning                                          |
| -------------- | ------------------------------------------------ |
| >              | 所有后续字母均大写。                               |
| <              | 以下所有字母均为小写。                             |
| !              | 关闭大小写转换。                                   |
| ;c             | 终止输入掩码并将空白字符设置为 c。                  |
| [ ] { }        | 保留的。                                          |
| \              | 使用 \ 来转义上面列出的特殊字符，以将它们用作分隔符。 |

创建或清除后，行编辑将用输入掩码字符串的副本填充，其中元字符已被删除，掩码字符已被替换为空白字符（默认情况下为空格）。

设置输入掩码后，text() 方法将返回行编辑内容的修改副本，其中所有空白字符均已被删除。可以使用 displayText() 读取未修改的内容。

如果行编辑的当前内容不满足输入掩码的要求，hasAcceptableInput() 方法将返回 false。

示例：

| Mask                | Notes                      |
| ------------------- | -------------------------- |
| 000.000.000.000;_   | IP address; blanks are _.  |
| HH:HH:HH:HH:HH:HH;_ | MAC address                |
| 0000-00-00          | ISO Date; blanks are space |
| >AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;# | 许可证号码；空格为#且所有（字母）字符均转换为大写。 |

为了获得范围控制（例如，对于 IP 地址），请将掩码与验证器一起使用。

访问函数：

- inputMask()
- setInputMask()


--------------------------------
## property maxLength : int

此属性保存文本的最大允许长度。

如果文本太长，则会在限制处截断。

如果发生截断，则将取消选择任何选定的文本，将光标位置设置为 0，并显示字符串的第一部分。

如果行编辑具有输入掩码，则掩码定义最大字符串长度。

默认情况下，此属性包含值 32767。

访问函数：

- maxLength()
- setMaxLength()


--------------------------------
## property modified : bool

此属性保存的是行编辑的内容是否已被用户修改。

QLineEdit 永远不会读取 modified 标志；它的默认值为 false，并且每当用户更改行编辑的内容时，它都会更改为 true。

这对于需要提供默认值但一开始不知道默认值应该是什么的情况很有用（例如，它取决于表单上的其他字段）。在没有最佳默认值的情况下开始行编辑，当默认值已知时，如果 modified() 返回 false（用户未输入任何文本），则插入默认值。

调用 setText() 会将 modified 标志重置为 false。

访问函数：

- isModified()
- setModified()


--------------------------------
## property placeholderText : str

此属性保存行编辑的占位符文本。

设置此属性会使行编辑显示灰色的占位符文本（只要行编辑为空）。

通常，空行编辑即使具有焦点也会显示占位符文本。但是，如果内容水平居中，则当行编辑具有焦点时，占位符文本不会显示在光标下方。

默认情况下，此属性包含一个空字符串。

访问函数：

- placeholderText()
- setPlaceholderText()


--------------------------------
## property readOnly : bool

此属性保存行编辑是否为只读。

在只读模式下，用户仍然可以将文本复制到剪贴板，或拖放文本（如果 echoMode() 为 Normal ），但无法编辑它。

QLineEdit 在只读模式下不显示光标。

默认情况下，此属性为 false。

访问函数：

- isReadOnly()
- setReadOnly()


--------------------------------
## property redoAvailable : bool

此属性保存是否可重做。

一旦用户对行编辑中的文本执行了一个或多个撤消操作，即可重做。

默认情况下，此属性为 false。

访问函数：

- isRedoAvailable()


--------------------------------
## property selectedText : str

此属性保存所选文本。

如果没有选定文本，则此属性的值为空字符串。

默认情况下，此属性包含一个空字符串。

访问函数：

- selectedText()


--------------------------------
## property text : str

此属性保存行编辑的文本。

设置此属性将清除选择，清除撤消/重做历史记录，将光标移动到行尾，并将修改后的属性重置为 false。使用 setText() 插入时不会验证文本。

文本被截断为 maxLength() 长度。

默认情况下，此属性包含一个空字符串。

访问函数：

- text()
- setText()
- Signal textChanged()


--------------------------------
## property undoAvailable : bool

此属性保存是否可撤消。

一旦用户修改了行编辑中的文本，撤消即可变为可用。

默认情况下，此属性为 false。

访问函数：

- isUndoAvailable()


--------------------------------
## __init__(arg__1[, parent=None])

参数：

- arg__1 – str
- parent – QWidget

构造一个包含文本内容的行编辑作为父级的子级。

光标位置设置为行尾，最大文本长度为 32767 个字符。


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

构造一个没有文本的行编辑。

最大文本长度设置为 32767 个字符。

父参数被发送到 QWidget 构造函数。


--------------------------------
## addAction(icon, position)

参数：

- icon – QIcon
- position – ActionPosition

返回类型：QAction

这是一个重载函数。

在指定位置使用给定图标创建新操作。


--------------------------------
## addAction(action, position)

参数：

- action – QAction
- position – ActionPosition

将该动作添加到该位置的动作列表中。


--------------------------------
## alignment()

返回类型：Combination of AlignmentFlag

属性 alignment 的获取器。


--------------------------------
## backspace()

如果未选择任何文本，则删除文本光标左侧的字符，并将光标向左移动一个位置。如果选择了任何文本，则将光标移动到所选文本的开头，并删除所选文本。


--------------------------------
## clear()

清除行编辑的内容。


--------------------------------
## completer()

返回类型：QCompleter

返回当前提供完成的 QCompleter。


--------------------------------
## copy()

将选定的文本复制到剪贴板（如果有），并且 echoMode() 为 Normal 。


--------------------------------
## createStandardContextMenu()

返回类型：QMenu

创建标准上下文菜单，当用户用鼠标右键单击行编辑时显示。它从默认 contextMenuEvent() 处理程序调用。弹出菜单的所有权将转移给调用者。


--------------------------------
## cursorBackward(mark[, steps=1])

参数：

- mark – bool
- steps – int

将光标向后移动几个字符。如果 mark 为真，则移动的每个字符都会添加到选择中。如果 mark 为假，则清除选择。


--------------------------------
## cursorForward(mark[, steps=1])

参数：

- mark – bool
- steps – int

将光标向前移动几个字符。如果 mark 为真，则移动的每个字符都会添加到选择中。如果 mark 为假，则清除选择。


--------------------------------
## cursorMoveStyle()

返回类型：CursorMoveStyle

属性 cursorMoveStyle 的获取器。


--------------------------------
## cursorPosition()

返回类型：int

属性 cursorPosition 的获取器。


--------------------------------
## cursorPositionAt(pos)

参数：

- pos – QPoint

返回类型：int

返回点 pos 下的光标位置。


--------------------------------
## cursorPositionChanged(arg__1, arg__2)

参数：

- arg__1 – int
- arg__2 – int

光标移动时会发出此信号。之前的位置由 oldPos 指定，新位置由 newPos 指定。


--------------------------------
## cursorRect()

返回类型：QRect

返回包含行编辑光标的矩形。


--------------------------------
## cursorWordBackward(mark)

参数：

- mark – bool

将光标向后移动一个单词。如果 mark 为真，则还会选择该单词。


--------------------------------
## cursorWordForward(mark)

参数：

- mark – bool

将光标向前移动一个单词。如果 mark 为真，则还会选择该单词。


--------------------------------
## cut()

将选定的文本复制到剪贴板并删除它（如果有），并且 echoMode() 为 Normal 。

如果当前验证器不允许删除选定的文本，则 cut() 将复制但不删除。


--------------------------------
## del_()
## deselect()

取消选择任何选定的文本。


--------------------------------
## displayText()

返回类型：str

属性 displayText 的获取器。


--------------------------------
## dragEnabled()

返回类型：bool

属性 dragEnabled 的获取器。


--------------------------------
## echoMode()

返回类型：EchoMode

属性 echoMode 的获取器。

--------------------------------
## editingFinished()

当使用 Return 或 Enter 键时，或者行编辑失去焦点并且其内容自上次发射此信号以来发生了变化时，就会发射此信号。


--------------------------------
## end(mark)

参数：

- mark – bool

将文本光标移动到行尾，除非光标已经位于该处。如果 mark 为真，则文本将朝最后一个位置选择。否则，如果移动光标，则任何选定的文本都将取消选择。


--------------------------------
## hasAcceptableInput()

返回类型：bool

属性 acceptingInput 的获取器。


--------------------------------
## hasFrame()

返回类型：bool

属性框架的获取器。


--------------------------------
## hasSelectedText()

返回类型：bool

属性 hasSelectedText 的获取器。


--------------------------------
## home(mark)

参数：

- mark – bool

将文本光标移动到行首，除非光标已经位于该处。如果 mark 为真，则文本将朝第一个位置选定。否则，如果移动光标，则任何选定的文本都将取消选定。


--------------------------------
## initStyleOption(option)

参数：

- option – QStyleOptionFrame

使用此 QLineEdit 中的值初始化选项。当子类需要 QStyleOptionFrame ，但又不想自己填写所有信息时，此方法很有用。


--------------------------------
## inputMask()

返回类型：str

属性 inputMask 的获取方法。


--------------------------------
## inputMethodQuery(property, argument)

参数：

- property – InputMethodQuery
- argument – object

返回类型：object


--------------------------------
## inputRejected()

当用户使用不被视为有效输入的键时，会发出此信号。例如，如果使用键导致验证器的validate（）调用返回无效。另一种情况是尝试输入超出行编辑最大长度的字符。


--------------------------------
## insert(arg__1)

参数：

- arg__1 – str

删除任何选定的文本，插入新文本，并验证结果。如果有效，则将新文本设置为行编辑的新内容。


--------------------------------
## isClearButtonEnabled()

返回类型：bool

属性 clearButtonEnabled 的获取器。


--------------------------------
## isModified()

返回类型：bool

修改属性的 getter。


--------------------------------
## isReadOnly()

返回类型：bool

属性 readOnly 的获取器。


--------------------------------
## isRedoAvailable()

返回类型：bool

属性 redoAvailable 的获取器。


--------------------------------
## isUndoAvailable()

返回类型：bool

属性 undoAvailable 的获取器。


--------------------------------
## maxLength()

返回类型：int

属性 maxLength 的获取器。


--------------------------------
## paste()

将剪贴板的文本插入到光标位置，删除任何选定的文本，前提是行编辑不是只读的。

如果最终结果对当前验证器无效，则不会发生任何事情。


--------------------------------
## placeholderText()

返回类型：str

属性 placeholderText 的获取方法。


--------------------------------
## redo()

如果可重做，则重做上一次操作。


--------------------------------
## returnPressed()

当使用 Return 或 Enter 键时发出此信号。


--------------------------------
## selectAll()

选择所有文本（突出显示）并将光标移动到末尾。


--------------------------------
## selectedText()

返回类型：str

属性 selectedText 的获取方法。


--------------------------------
## selectionChanged()

每当选择改变时就会发射此信号。


--------------------------------
## selectionEnd()

返回类型：int

返回行编辑中选择内容之后直接显示的字符的索引（如果未选择文本，则返回 -1）。


--------------------------------
## selectionLength()

返回类型：int

返回选择的长度。


--------------------------------
## selectionStart()

返回类型：int

返回行编辑中第一个选定字符的索引（如果未选择文本，则返回 -1）。


--------------------------------
## setAlignment(flag)

参数：

- flag – Combination of AlignmentFlag

属性对齐的设置者。


--------------------------------
## setClearButtonEnabled(enable)

参数：

- enable – bool

属性 clearButtonEnabled 的设置者。


--------------------------------
## setCompleter(completer)

参数：

- completer – QCompleter

设置此行编辑以提供来自完成器 c 的自动完成。使用 setCompletionMode() 设置完成模式。

要将 QCompleter 与 QValidator 或 inputMask 一起使用，您需要确保提供给 QCompleter 的模型包含有效条目。您可以使用 QSortFilterProxyModel 来确保 QCompleter 的模型仅包含有效条目。

要删除完成器并禁用自动完成，请传递一个 nullptr。


--------------------------------
## setCursorMoveStyle(style)

参数：

- style – CursorMoveStyle

属性 cursorMoveStyle 的设置器。


--------------------------------
## setCursorPosition(arg__1)

参数：

- arg__1 – int

属性 cursorPosition 的设置器。


--------------------------------
## setDragEnabled(b)

参数：

- b – bool

属性 dragEnabled 的设置者。


--------------------------------
## setEchoMode(arg__1)

参数：

- arg__1 – EchoMode

属性 echoMode 的设置者。


--------------------------------
## setFrame(arg__1)

参数：

- arg__1 – bool

属性框架的设置者。


--------------------------------
## setInputMask(inputMask)

参数：

- inputMask – str

属性 inputMask 的设置者。


--------------------------------
## setMaxLength(arg__1)

参数：

- arg__1 – int

属性 maxLength 的设置者。


--------------------------------
## setModified(arg__1)

参数：

- arg__1 – bool

属性的设置者已修改。


--------------------------------
## setPlaceholderText(arg__1)

参数：

- arg__1 – str

属性 placeholderText 的设置者。


--------------------------------
## setReadOnly(arg__1)

参数：

- arg__1 – bool

属性 readOnly 的设置者。


--------------------------------
## setSelection(arg__1, arg__2)

参数：

- arg__1 – int
- arg__2 – int

从位置 start 选择文本，长度为字符数。允许使用负长度。


--------------------------------
## setText(arg__1)

参数：

- arg__1 – str

属性文本的设置者。


--------------------------------
## setTextMargins(margins)

参数：

- margins – QMargins

设置框架内文本周围的边距。


--------------------------------
## setTextMargins(left, top, right, bottom)

参数：

- left – int
- top – int
- right – int
- bottom – int

设置框架内文本周围的边距，包括左边距、上边距、右边距和下边距。


--------------------------------
## setValidator(arg__1)

参数：

- arg__1 – QValidator

将行编辑值的验证器设置为 v。

仅当 v 验证行编辑的内容为可接受时，才会发出行编辑的 returnPressed() 和 editingFinished() 信号。用户可以在编辑期间将内容更改为任何中间值，但无法将文本编辑为 v 验证为无效的值。

这允许您限制编辑完成后将存储的文本，同时让用户有足够的自由将文本从一个有效状态编辑到另一个有效状态。

要删除当前输入验证器，请传递 nullptr。初始设置是没有输入验证器（接受任何输入，最大长度为 maxLength() ）。


--------------------------------
## text()

返回类型：str

属性 text 的获取器。


--------------------------------
## textChanged(arg__1)

参数：

- arg__1 – str

每当文本发生变化时，都会发出此信号。text 参数是新文本。

与 textEdited() 不同，当以编程方式更改文本（例如通过调用 setText() ）时也会发出此信号。

属性 text 的通知信号。


--------------------------------
## textEdited(arg__1)

参数：

- arg__1 – str

每当编辑文本时都会发出此信号。文本参数是新文本。

与 textChanged() 不同，当以编程方式更改文本（例如通过调用 setText() ）时不会发出此信号。


--------------------------------
## textMargins()

返回类型：QMargins

返回小部件的文本边距。


--------------------------------
## undo()

如果可撤消，则撤消上一个操作。取消选择任何当前选择，并将选择开始更新为当前光标位置。


--------------------------------
## validator()

返回类型：QValidator

返回指向当前输入验证器的指针，如果未设置验证器，则返回 None。

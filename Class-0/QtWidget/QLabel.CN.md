
# class QLabel

QLabel 小部件提供文本或图像显示。


# Synopsis

## Properties

- [alignment](#property-alignment--combination-of-qtalignmentflag)

    标签内容的对齐方式。

- [hasSelectedText](#property-hasselectedtext--bool)

    是否选择了任何文本。

- [indent](#property-indent--int)

    标签的文本缩进（以像素为单位）。

- [margin](#property-margin--int)

    边距的宽度。

- [openExternalLinks](#property-openexternallinks--bool)

- [pixmap](#property-pixmap--qpixmap)

    标签的像素图。

- [scaledContents](#property-scaledcontents--bool)

    标签是否会缩放其内容以填充所有可用空间。

- [selectedText](#property-selectedtext--str)

    选定的文本。

- [text](#property-text--str)

    标签的文本。

- [textFormat](#property-textformat--qttextformat)

    标签的文本格式。

- [textInteractionFlags](#property-textinteractionflags--combination-of-qttextinteractionflag)

- [wordWrap](#property-wordwrap--bool)

    标签的自动换行策略。


## Methods

- [def \_\_init__()](#__init__text-parentnone-fqtwindowflags)

- [def alignment()](#alignment)

- [def buddy()](#buddy)

- [def hasScaledContents()](#hasScaledContents)

- [def hasSelectedText()](#hasselectedtext)

- [def indent()](#indent)

- [def margin()](#margin)

- [def movie()](#movie)

- [def openExternalLinks()](#openexternallinks)

- [def picture()](#picture)

- [def pixmap()](#pixmap)

- [def selectedText()](#selectedtext)

- [def selectionStart()](#selectionstart)

- [def setAlignment()](#setalignmentarg__1)

- [def setBuddy()](#setbuddyarg__1)

- [def setIndent()](#setindentarg__1)

- [def setMargin()](#setmarginarg__1)

- [def setOpenExternalLinks()](#setopenexternallinksopen)

- [def setScaledContents()](#setscaledcontentsarg__1)

- [def setSelection()](#setselectionarg__1-arg__2)

- [def setTextFormat()](#settextformatarg__1)

- [def setTextInteractionFlags()](#settextinteractionflagsflags)

- [def setWordWrap()](#setwordwrapon)

- [def text()](#text)

- [def textFormat()](#textformat)

- [def textInteractionFlags()](#textinteractionflags)

- [def wordWrap()](#wordwrap)


## Slots

- [def clear()](#clear)

- [def setMovie()](#setmoviemovie)

- [def setNum()](#setnumarg__1)

- [def setPicture()](#setpicturearg__1)

- [def setPixmap()](#setpixmaparg__1)

- [def setText()](#settextarg__1)


## Signals

- [def linkActivated()](#linkactivatedlink)

- [def linkHovered()](#linkhoveredlink)


# Detailed Description

QLabel 用于显示文本或图像。不提供用户交互功能。标签的外观可以以多种方式配置，并且可用于为另一个小部件指定焦点助记键。

QLabel 可以包含以下任意内容类型：

| Content    | Setting                                                                       |
| ---------- | ----------------------------------------------------------------------------- |
| Plain text | 将 QString 传递给 setText()                                                   |
| Rich text  | 将包含富文本的 QString 传递给 setText()                           |
| A pixmap   | 将 QPixmap 传递给 setPixmap()                                                 |
| A movie    | 将 QMovie 传递给 setMovie()                                                   |
| A number   | 将 int 或 double 传递给 setNum() ，它将数字转换为纯文本 |
| Nothing    | 与空纯文本相同。这是默认值。通过 clear() 设置          |

当使用其中任何一项功能更改内容时，所有先前的内容都会被清除。

默认情况下，标签显示左对齐、垂直居中的文本和图像，其中要显示的文本中的任何选项卡都会自动展开。但是，QLabel 的外观可以通过多种方式进行调整和微调。

可以使用 setAlignment() 和 setIndent() 调整 QLabel 小部件区域内内容的定位。文本内容还可以使用 setWordWrap() 沿单词边界换行。例如，此代码设置了一个凹陷面板，右下角有两行文本（两行都与标签的右侧齐平）：

```python
label = QLabel(self)
label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
label.setText("first line\nsecond line")
label.setAlignment(Qt.AlignBottom | Qt.AlignRight)
```

QLabel 从 QFrame 继承的属性和函数也可用于指定用于任何给定标签的小部件框架。

QLabel 通常用作交互式小部件的标签。对于此用途，QLabel 提供了一种有用的机制来添加助记符（参见 QKeySequence），该助记符将键盘焦点设置到另一个小部件（称为 QLabel 的“伙伴”）。例如：

```python
phoneEdit = QLineEdit(self)
phoneLabel = QLabel("Phone:", self)
phoneLabel.setBuddy(phoneEdit)
```

在此示例中，当用户按下 Alt+P 时，键盘焦点将转移到标签的伙伴（QLineEdit）。如果伙伴是一个按钮（继承自 QAbstractButton），则触发助记符将模拟按钮单击。

--------------------------------
## `property alignment` : Combination of Qt.AlignmentFlag

此属性保存标签内容的对齐方式。

默认情况下，标签的内容是左对齐且垂直居中。

访问函数：

- alignment()
- setAlignment()

--------------------------------
## `property hasSelectedText` : bool

此属性保存的是是否有任何文本被选中。

如果用户选择了部分或全部文本，则 hasSelectedText() 返回 true；否则返回 false。

默认情况下，此属性为 false。

访问函数：

- hasSelectedText()

--------------------------------
## `property indent` : int

此属性保存标签的文本缩进（以像素为单位）。

如果标签显示文本，则如果 alignment() 为 Qt::AlignLeft，则缩进应用于左边缘；如果 alignment() 为 Qt::AlignRight，则缩进应用于右边缘；如果 alignment() 为 Qt::AlignTop，则缩进应用于上边缘；如果 alignment() 为 Qt::AlignBottom，则缩进应用于下边缘。

如果缩进为负数，或者未设置缩进，则标签将按如下方式计算有效缩进：如果 frameWidth() 为 0，则有效缩进为 0。如果 frameWidth() 大于 0，则有效缩进为小部件当前 font() 的“x”字符宽度的一半。

默认情况下，缩进为 -1，这意味着有效缩进按上面描述的方式计算。

访问函数：

- indent()
- setIndent()

--------------------------------
## `property margin` : int

此属性保存边距的宽度。

边距是框架最内像素与内容最外像素之间的距离。

默认边距为 0。

访问函数：

- margin()
- setMargin()

--------------------------------
## `property openExternalLinks` : bool

指定 QLabel 是否应使用 QDesktopServices::openUrl() 自动打开链接，而不是发出 linkActivated() 信号。

默认值为 false。

访问函数：

- openExternalLinks()
- setOpenExternalLinks()

--------------------------------
## `property pixmap` : QPixmap

此属性保存标签的像素图。

设置像素图会清除所有先前的内容。好友快捷方式（如果有）将被禁用。

访问函数：

- pixmap()
- setPixmap()

--------------------------------
## `property scaledContents` : bool

此属性保存标签是否缩放其内容以填充所有可用空间。

启用后，标签​​会显示像素图，它将缩放像素图以填充可用空间。

此属性的默认值为 false。

访问函数：

- hasScaledContents()
- setScaledContents()

--------------------------------
## `property selectedText` : str

此属性保存选定的文本。

如果没有选定的文本，则此属性的值为空字符串。

默认情况下，此属性包含一个空字符串。

访问函数：

- selectedText()

--------------------------------
## `property text` : str

此属性保存标签的文本。

如果未设置文本，则将返回一个空字符串。设置文本将清除所有先前的内容。

根据文本格式设置，文本将被解释为纯文本或富文本；请参阅 setTextFormat() 。默认设置为 Qt::AutoText；即 QLabel 将尝试自动检测文本集的格式。有关富文本的定义，请参阅支持的 HTML 子集。

如果已设置好友，则好友助记键将从新文本更新。

请注意，QLabel 非常适合显示小型富文本文档，例如从标签的调色板和字体属性获取其文档特定设置（字体、文本颜色、链接颜色）的小型文档。对于大型文档，请改用只读模式的 QTextEdit。QTextEdit 还可以在必要时提供滚动条。

访问函数：

- text()
- setText()

--------------------------------
## `property textFormat` : Qt.TextFormat

此属性保存标签的文本格式。

有关可能选项的说明，请参阅 Qt::TextFormat 枚举。

默认格式为 Qt::AutoText。

访问函数：

- textFormat()
- setTextFormat()

--------------------------------
## `property textInteractionFlags` : Combination of Qt.TextInteractionFlag

指定标签在显示文本时应如何与用户输入交互。

如果标志包含 Qt::LinksAccessibleByKeyboard，则焦点策略也会自动设置为 Qt::StrongFocus。 如果设置了 Qt::TextSelectableByKeyboard，则焦点策略将设置为 Qt::ClickFocus。

默认值为 Qt::LinksAccessibleByMouse。

访问函数：

- textInteractionFlags()
- setTextInteractionFlags()

--------------------------------
## `property wordWrap` : bool

此属性保存标签的自动换行策略。

如果此属性为真，则标签文本在必要时在单词中断处换行；否则根本不换行。

默认情况下，自动换行处于禁用状态。

访问函数：

- wordWrap()
- setWordWrap()

--------------------------------
## `__init__(text[, parent=None[, f=Qt.WindowFlags()]])`

参数: 

- text – str
- parent – QWidget
- f – Combination of WindowType

构造一个显示文本 text 的标签。

父级和小部件标志 f 参数被传递给 QFrame 构造函数。

--------------------------------
## `__init__([parent=None[, f=Qt.WindowFlags()]])`

参数: 

- parent – QWidget
- f – Combination of WindowType

构造一个空标签。

父级和小部件标志 f 参数被传递给 QFrame 构造函数。

--------------------------------
## `alignment()`

返回值: Combination of AlignmentFlag

属性对齐的获取器。

--------------------------------
## `buddy()`

返回值: QWidget

返回此标签的伙伴，如果当前未设置伙伴，则返回 nullptr。

--------------------------------
## `clear()`

清除所有标签内容。

--------------------------------
## `hasScaledContents()`

返回值: bool

属性 scaledContents 的获取器。

--------------------------------
## `hasSelectedText()`

返回值: bool

属性 hasSelectedText 的获取器。

--------------------------------
## `indent()`

返回值: int

属性缩进的获取器。

--------------------------------
## `linkActivated(link)`

参数: 

- link – str

当用户点击链接时，会发出此信号。锚点所指向的 URL 在链接中传递。

--------------------------------
## `linkHovered(link)`

参数: 

- link – str

当用户将鼠标悬停在链接上时，会发出此信号。锚点所指的 URL 在链接中传递。

--------------------------------
## `margin()`

返回值: int

属性 margin 的获取器。

--------------------------------
## `movie()`

返回值: QMovie

返回指向标签电影的指针，如果未设置电影，则返回 nullptr。

--------------------------------
## `openExternalLinks()`

返回值: bool

属性 openExternalLinks 的获取器。

--------------------------------
## `picture()`

返回值: QPicture

返回标签的图片。

--------------------------------
## `pixmap()`

返回值: QPixmap

属性 pixmap 的获取器。

--------------------------------
## `selectedText()`

返回值: str

属性 selectedText 的获取器。

--------------------------------
## `selectionStart()`

返回值: int

SelectionStart() 返回标签中第一个选定字符的索引，如果没有选定文本，则返回 -1。

--------------------------------
## `setAlignment(arg__1)`

参数: 

- arg__1 – Combination of AlignmentFlag

属性对齐的设置器。

--------------------------------
## `setBuddy(arg__1)`

参数: 

- arg__1 – QWidget

将此标签的伙伴设置为 buddy。

当用户按下此标签指示的快捷键时，键盘焦点将转移到标签的伙伴小部件。

伙伴机制仅适用于包含一个字符以“&”为前缀的文本的 QLabels。此字符设置为快捷键。有关详细信息，请参阅 QKeySequence::mnemonic() 文档（要显示实际的“&”符号，请使用“&&”）。

在对话框中，您可以创建两个数据输入小部件并为每个小部件创建一个标签，并设置几何布局，以便每个标签都位于其数据输入小部件（其“伙伴”）的左侧，例如：

```python
nameEdit = QLineEdit(self)
QLabel nameLabel = QLabel("Name:", self)
nameLabel.setBuddy(nameEdit)
phoneEdit = QLineEdit(self)
QLabel phoneLabel = QLabel("Phone:", self)
phoneLabel.setBuddy(phoneEdit)
# (layout setup not shown)
```

使用上述代码，当用户按下 Alt+N 时，焦点会跳转到“姓名”字段，当用户按下 Alt+P 时，焦点会跳转到“电话”字段。

要取消之前设置的好友，请调用此函数并将好友设置为 nullptr。

--------------------------------
## `setIndent(arg__1)`

参数: 

- arg__1 – int

属性缩进的设置者。

--------------------------------
## `setMargin(arg__1)`

参数: 

- arg__1 – int

属性 margin 的设置者。

--------------------------------
## `setMovie(movie)`

参数: 

- movie – QMovie

将标签内容设置为电影。所有先前的内容都将被清除。标签不会拥有该电影的所有权。

好友快捷方式（如果有）将被禁用。

--------------------------------
## `setNum(arg__1)`

参数: 

- arg__1 – float

这是一个重载函数。

将标签内容设置为包含双精度数文本表示的纯文本。任何先前的内容都将被清除。如果双精度数的字符串表示与标签的当前内容相同，则不执行任何操作。

好友快捷方式（如果有）被禁用。

--------------------------------
## `setNum(arg__1)`

参数: 

- arg__1 – int

将标签内容设置为包含整数 num 的文本表示的纯文本。任何先前的内容都将被清除。如果整数的字符串表示与标签的当前内容相同，则不执行任何操作。

好友快捷方式（如果有）被禁用。

--------------------------------
## `setOpenExternalLinks(open)`

参数: 

- open – bool

属性 openExternalLinks 的设置者。

--------------------------------
## `setPicture(arg__1)`

参数: 

- arg__1 – QPicture

将标签内容设置为图片。所有先前的内容都将被清除。

好友快捷方式（如果有）将被禁用。

--------------------------------
## `setPixmap(arg__1)`

参数: 

- arg__1 – QPixmap

属性 pixmap 的设置者。

--------------------------------
## `setScaledContents(arg__1)`

参数: 

- arg__1 – bool

scaledContents 属性的设置者。

--------------------------------
## `setSelection(arg__1, arg__2)`

P1ARAMETERS:

- arg__1 – int
- arg__2 – int

从开始位置选择长度为字符的文本。

--------------------------------
## `setText(arg__1)`

参数: 

- arg__1 – str

属性文本的设置者。

--------------------------------
## `setTextFormat(arg__1)`

参数: 

- arg__1 – TextFormat

属性 textFormat 的设置者。

--------------------------------
## `setTextInteractionFlags(flags)`

参数: 

- flags – Combination of TextInteractionFlag

属性 textInteractionFlags 的设置者。

--------------------------------
## `setWordWrap(on)`

参数: 

- on – bool

属性 wordWrap 的设置器。

--------------------------------
## `text()`

返回值: str

属性文本的获取器。

--------------------------------
## `textFormat()`

返回值: TextFormat

属性 textFormat 的获取方法。

--------------------------------
## `textInteractionFlags()`

返回值: Combination of TextInteractionFlag

属性 textInteractionFlags 的获取器。

--------------------------------
## `wordWrap()`

返回值: bool

属性 wordWrap 的获取方法。

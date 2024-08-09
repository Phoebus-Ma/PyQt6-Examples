
[English doc](QMessageBox.md)

# class QMessageBox

QMessageBox 类提供了一个模态对话框，用于通知用户或者向用户提问并得到答案。


# Synopsis

## Properties

- [detailedText](#property-detailedtext--str)

    要在详细信息区域中显示的文本。

- [icon](#property-icon--qmessageboxicon)

    消息框的图标。

- [iconPixmap](#property-iconpixmap--qpixmap)

    当前图标。

- [informativeText](#property-informativetext--str)

    为消息提供更详细描述的信息文本。

- [options](#property-options--combination-of-qabstractfileiconprovideroption)

    影响对话框外观的选项。

- [standardButtons](#property-standardbuttons--combination-of-qdialogbuttonboxstandardbutton)

    消息框中的标准按钮集合。

- [text](#property-text--str)

    要显示的消息框文本。

- [textFormat](#property-textformat--qttextformat)

    消息框显示的文本的格式。

- [textInteractionFlags](#property-textinteractionflags--combination-of-qttextinteractionflag)


## Methods

- [def \_\_init__()](#initparentnone)

- [def addButton()](#addbuttonbutton)

- [def button()](#buttonwhich)

- [def buttonRole()](#buttonrolebutton)

- [def buttonText()](#buttontextbutton)

- [def buttons()](#buttons)

- [def checkBox()](#checkbox)

- [def clickedButton()](#clickedbutton)

- [def defaultButton()](#defaultbutton)

- [def detailedText()](#detailedtext)

- [def escapeButton()](#escapebutton)

- [def icon()](#icon)

- [def iconPixmap()](#iconpixmap)

- [def informativeText()](#informativetext)

- [def open()](#openreceiver-member)

- [def options()](#options)

- [def removeButton()](#removebuttonbutton)

- [def setButtonText()](#setbuttontextbutton-text)

- [def setCheckBox()](#setcheckboxcb)

- [def setDefaultButton()](#setdefaultbuttonbutton)

- [def setDetailedText()](#setdetailedtexttext)

- [def setEscapeButton()](#setescapebuttonbutton)

- [def setIcon()](#seticonarg__1)

- [def setIconPixmap()](#seticonpixmappixmap)

- [def setInformativeText()](#setinformativetexttext)

- [def setOption()](#setoptionoption-ontrue)

- [def setOptions()](#setoptionsoptions)

- [def setStandardButtons()](#setstandardbuttonsbuttons)

- [def setText()](#settexttext)

- [def setTextFormat()](#settextformatformat)

- [def setTextInteractionFlags()](#settextinteractionflagsflags)

- [def setWindowModality()](#setwindowmodalitywindowmodality)

- [def setWindowTitle()](#setwindowtitletitle)

- [def standardButton()](#standardbuttonbutton)

- [def standardButtons()](#standardbuttons)

- [def testOption()](#testoptionoption)

- [def text()](#text)

- [def textFormat()](#textformat)

- [def textInteractionFlags()](#textinteractionflags)


## Signals

- [def buttonClicked()](#buttonclickedbutton)


## Static functions

- [def about()](#static-aboutparent-title-text)

- [def aboutQt()](#static-aboutqtparent-title)

- [def critical()](#static-criticalparent-title-text-button0-button1)

- [def information()](#static-informationparent-title-text-button0-button1qmessageboxstandardbuttonnobutton)

- [def question()](#static-questionparent-title-text-button0-button1)

- [def standardIcon()](#static-standardiconicon)

- [def warning()](#static-warningparent-title-text-button0-button1)


# Detailed Description

消息框显示主要文本以提醒用户注意某种情况，显示信息性文本以进一步解释该情况，以及显示可选的详细文本以在用户请求时提供更多数据。

消息框还可以显示图标和标准按钮以接受用户响应。

提供了两个使用 QMessageBox 的 API，即基于属性的 API 和静态函数。调用其中一个静态函数是更简单的方法，但它不如使用基于属性的 API 灵活，结果信息量较少。建议使用基于属性的 API。


## The Property-based API

要使用基于属性的 API，请构造 QMessageBox 的一个实例，设置所需的属性，然后调用 exec() 来显示消息。最简单的配置是仅设置消息文本属性。

```python
msgBox = QMessageBox()
msgBox.setText("The document has been modified.")
msgBox.exec()
```

用户必须单击“确定”按钮才能关闭消息框。在消息框关闭之前，其余 GUI 将被阻止。

比仅提醒用户事件更好的方法是询问用户如何处理。

将标准按钮属性设置为您想要作为用户响应的按钮集。通过使用按位或运算符组合 StandardButtons 中的值来指定按钮。按钮的显示顺序取决于平台。例如，在 Windows 上，“保存”显示在“取消”的左侧，而在 macOS 上，顺序相反。将其中一个标准按钮标记为默认按钮。

信息文本属性可用于添加其他上下文，以帮助用户选择适当的操作。

```python
msgBox = QMessageBox()
msgBox.setText("The document has been modified.")
msgBox.setInformativeText("Do you want to save your changes?")
msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
msgBox.setDefaultButton(QMessageBox.Save)
ret = msgBox.exec()
```

exec() 槽返回被点击的按钮的 StandardButtons 值。

```python
if ret == QMessageBox.Save:
    # Save was clicked
    break
elif ret == QMessageBox.Discard:
    # Don't Save was clicked
    break
elif ret == QMessageBox.Cancel:
    # Cancel was clicked
    break
else:
    # should never be reached
    break
```

为了向用户提供更多信息以帮助他们选择适当的操作，请设置详细文本属性。根据平台的不同，详细文本可能需要用户单击“显示详细信息…”按钮才能显示。

单击“显示详细信息…”按钮将显示详细文本。


## Rich Text and the Text Format Property

详细文本属性始终被解释为纯文本。主文本和信息文本属性可以是纯文本或富文本。这些字符串根据文本格式属性的设置进行解释。默认设置为自动文本。

请注意，对于某些包含 XML 元字符的纯文本字符串，自动文本富文本检测测试可能会失败，导致您的纯文本字符串被错误地解释为富文本。在这些罕见情况下，使用 Qt::convertFromPlainText() 将纯文本字符串转换为视觉上等效的富文本字符串，或使用 setTextFormat() 明确设置文本格式属性。


## Severity Levels and the Icon and Pixmap Properties

QMessageBox 支持四种预定义消息严重性级别或消息类型，它们实际上仅在各自显示的预定义图标上有所不同。通过将 icon 属性设置为预定义图标之一，可以指定四种预定义消息类型之一。以下规则是指导原则：

|             |                              |
| ----------- | --------------- ------------ |
| Question    | 用于在正常操作期间提出问题。    |
| Information | 用于报告有关正常操作的信息。    |
| Warning     | 用于报告非严重错误。           |
| Critical    | 用于报告严重错误。             |

预定义图标不是由 QMessageBox 定义的，而是由样式提供的。默认值为 No Icon 。消息框在所有情况下都是相同的。使用标准图标时，请使用表中推荐的图标，或使用平台样式指南推荐的图标。如果没有标准图标适合您的消息框，您可以通过设置图标像素映射属性而不是设置图标属性来使用自定义图标。

总之，要设置图标，请对标准图标之一使用 setIcon()，或对自定义图标使用 setIconPixmap()。


## The Static Functions API

使用静态函数 API 构建消息框虽然方便，但不如使用基于属性的 API 灵活，因为静态函数签名缺少用于设置信息文本和详细文本属性的参数。一种解决方法是使用 title 参数作为消息框主文本，使用 text 参数作为消息框信息文本。由于这显然会导致消息框的可读性降低，因此平台指南不建议这样做。Microsoft Windows 用户界面指南建议使用应用程序名称作为窗口的 title ，这意味着如果除了主文本之外还有信息文本，则必须将其连接到 text 参数。

请注意，静态函数签名的按钮参数已更改，现在用于设置标准按钮和默认按钮。

静态函数可用于创建 information() 、 question() 、 warning() 和 critical() 消息框。

```python
ret = QMessageBox.warning(self, tr("My Application"),()
                               tr("The document has been modified.\n"
                                  "Do you want to save your changes?"),
                               QMessageBox.Save | QMessageBox.Discard
                               | QMessageBox.Cancel,
                               QMessageBox.Save)
```

标准对话框示例展示了如何使用 QMessageBox 和其他内置 Qt 对话框。


## Advanced Usage

如果标准按钮对于您的消息框来说不够灵活，您可以使用 addButton() 重载，该重载接受文本和 ButtonRole 来添加自定义按钮。QMessageBox 使用 ButtonRole 来确定屏幕上按钮的顺序（根据平台的不同而不同）。您可以在调用 exec() 后测试 clickedButton() 的值。例如，

```bash
msgBox = QMessageBox()
connectButton = msgBox.addButton(tr("Connect"), QMessageBox.ActionRole)
abortButton = msgBox.addButton(QMessageBox.Abort)
msgBox.exec()
if msgBox.clickedButton() == connectButton:
    # connect
 elif msgBox.clickedButton() == abortButton:
    # abort
```


## Default and Escape Keys

可以使用 setDefaultButton() 指定默认按钮（即按下 Enter 时激活的按钮）。如果未指定默认按钮，QMessageBox 将尝试根据消息框中使用的按钮的按钮角色找到一个。

可以使用 setEscapeButton() 指定退出按钮（按下 Esc 时激活的按钮）。如果未指定退出按钮，QMessageBox 将尝试使用以下规则找到一个：

1. 如果只有一个按钮，则它是按下 Esc 时激活的按钮。

2. 如果有取消按钮，则它是按下 Esc 时激活的按钮。

3. 如果只有一个按钮具有拒绝角色或否角色，则它是按下 Esc 时激活的按钮。

当使用这些规则无法确定退出按钮时，按 Esc 无效。


--------------------------------
## class Option

| Constant                               | Description                          |
| -------------------------------------- | ------------------------------------ |
| QMessageBox.Option.DontUseNativeDialog | （继承枚举标志）不要使用本机消息对话框。 |

6.6 版本中的新功能。


--------------------------------
## class Icon

该枚举具有以下值：

| Constant                | Description                           |
| ----------------------- | ------------------------------------- |
| QMessageBox.NoIcon      | 消息框没有任何图标。                    |
| QMessageBox.Question    | 一个图标，表示该消息正在提出问题。        |
| QMessageBox.Information | 一个图标，表示该消息并无异常。           |
| QMessageBox.Warning     | 一个图标，表示该消息是警告，但可以处理。  |
| QMessageBox.Critical    | 一个图标，表示该消息代表严重问题。       |


--------------------------------
## class ButtonRole

此枚举描述了可用于描述按钮框中的按钮的角色。这些角色的组合作为用于描述其行为不同方面的标志。

| Constant                    | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| QMessageBox.InvalidRole     | 该按钮无效。                                           |
| QMessageBox.AcceptRole      | 单击该按钮将导致对话框被接受（例如，确定）。              |
| QMessageBox.RejectRole      | 单击该按钮会导致对话框被拒绝（例如取消）。               |
| QMessageBox.DestructiveRole | 单击该按钮会导致破坏性更改（例如，放弃更改）并关闭对话框。 |
| QMessageBox.ActionRole      | 单击该按钮会导致对话框中的元素发生变化。                 |
| QMessageBox.HelpRole        | 可以点击该按钮来请求帮助。                              |
| QMessageBox.YesRole         | 该按钮是一个类似“是”的按钮。                            |
| QMessageBox.NoRole          | 该按钮是一个类似“否”的按钮。                            |
| QMessageBox.ApplyRole       | 该按钮应用当前更改。                                   |
| QMessageBox.ResetRole       | 该按钮将对话框的字段重置为默认值。                      |


--------------------------------
## class StandardButton

（继承 enum.IntFlag）这些枚举描述标准按钮的标志。每个按钮都有一个定义的 ButtonRole 。

| Constant                    | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| QMessageBox.Ok              | 使用 AcceptRole 定义的“OK”按钮。                          |
| QMessageBox.Open            | 使用 AcceptRole 定义的“打开”按钮。                         |
| QMessageBox.Save            | 使用 AcceptRole 定义的“保存”按钮。                         |
| QMessageBox.Cancel          | 使用 RejectRole 定义的“取消”按钮。                         |
| QMessageBox.Close           | 使用 RejectRole 定义的“关闭”按钮。                         |
| QMessageBox.Discard         | 根据平台，使用 DestructiveRole 定义的“丢弃”或“不保存”按钮。 |
| QMessageBox.Apply           | 使用 ApplyRole 定义的“应用”按钮。                         |
| QMessageBox.Reset           | 使用 ResetRole 定义的“重置”按钮。                         |
| QMessageBox.RestoreDefaults | 使用 ResetRole 定义的“恢复默认值”按钮。                    |
| QMessageBox.Help            | 使用 HelpRole 定义的“帮助”按钮。                          |
| QMessageBox.SaveAll         | 使用 AcceptRole 定义的“全部保存”按钮。                    |
| QMessageBox.Yes             | 使用 YesRole 定义的“是”按钮。                             |
| QMessageBox.YesToAll        | 使用 YesRole 定义的“全部是”按钮。                         |
| QMessageBox.No              | 使用 NoRole 定义的“否”按钮。                              |
| QMessageBox.NoToAll         | 使用 NoRole 定义的“全部否”按钮。                          |
| QMessageBox.Abort           | 使用 RejectRole 定义的“中止”按钮。                        |
| QMessageBox.Retry           | 使用 AcceptRole 定义的“重试”按钮。                        |
| QMessageBox.Ignore          | 使用 AcceptRole 定义的“忽略”按钮。                        |
| QMessageBox.NoButton        | 无效按钮。                                               |

以下值已过时：

| Constant               | Description                      |
| ---------------------- | -------------------------------- |
| QMessageBox.YesAll     | 改用 YesToAll。                  |
| QMessageBox.NoAll      | 改用NoToAll。                    |
| QMessageBox.Default    | 请改用 information() 、 warning() 等的 defaultButton 参数，或者调用 setDefaultButton() 。 |
| QMessageBox.Escape     | 改为调用 setEscapeButton()。      |
| QMessageBox.FlagMask   |                                  |
| QMessageBox.ButtonMask |                                  |


--------------------------------
## property detailedText : str

此属性保存要在详细信息区域中显示的文本。

文本将被解释为纯文本。

默认情况下，此属性包含一个空字符串。

访问函数：

- detailedText()
- setDetailedText()


--------------------------------
## property icon : QMessageBox.Icon

此属性保存消息框的图标。

可以使用以下值之一指定消息框的图标：

- NoIcon
- Question
- Information
- Warning
- Critical

默认值为 NoIcon 。

用于显示实际图标的像素图取决于当前的 GUI 样式。您还可以通过设置图标像素图属性为图标设置自定义像素图。

访问函数：

- icon()
- setIcon()


--------------------------------
## property iconPixmap : QPixmap

此属性保存当前图标。

消息框当前使用的图标。请注意，绘制一个在所有 GUI 样式中都合适的像素图通常很困难；您可能希望为每个平台提供不同的像素图。

默认情况下，此属性未定义。

访问函数：

- iconPixmap()
- setIconPixmap()


--------------------------------
## property informativeText : str

此属性包含提供消息更完整描述的信息性文本。

信息性文本可用于扩展 text()，以便向用户提供更多信息，例如描述情况的后果或建议替代解决方案。

默认情况下，此属性包含一个空字符串。

访问函数：

- informativeText()
- setInformativeText()


--------------------------------
## property options : Combination of QAbstractFileIconProvider.Option

此属性包含影响对话框外观的选项。

默认情况下，这些选项是禁用的。

应在更改对话框属性或显示对话框之前设置选项 DontUseNativeDialog。

在对话框可见时设置选项不能保证立即对对话框产生影响。

在更改其他属性后设置选项可能会导致这些值不起作用。

访问函数：

- options()
- setOptions()


--------------------------------
## property standardButtons : Combination of QDialogButtonBox.StandardButton

此属性保存消息框中的标准按钮集合。

此属性控制消息框使用哪些标准按钮。

默认情况下，此属性不包含任何标准按钮。

访问函数：

- standardButtons()
- setStandardButtons()


--------------------------------
## property text : str

此属性保存要显示的消息框文本。

文本应为描述情况的简短句子或短语，最好表述为中性陈述或号召性用语问题。

文本将被解释为纯文本或富文本，具体取决于文本格式设置 (textFormat)。默认设置为 Qt::AutoText，即消息框将尝试自动检测文本的格式。

此属性的默认值为空字符串。

访问函数：

- text()
- setText()


--------------------------------
## property textFormat : Qt.TextFormat

此属性保存消息框显示的文本格式。

消息框当前使用的文本格式。有关可能选项的说明，请参阅 Qt::TextFormat 枚举。

默认格式为 Qt::AutoText。

访问函数：

- textFormat()
- setTextFormat()


--------------------------------
## property textInteractionFlags : Combination of Qt.TextInteractionFlag

指定消息框的标签应如何与用户输入交互。

默认值取决于样式。

访问函数：

- textInteractionFlags()
- setTextInteractionFlags()


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

构造一个没有文本和按钮的应用程序模式消息框。parent 传递给 QDialog 构造函数。

在调用 show() 之前，可以通过 setWindowModality() 覆盖窗口模式。

在 macOS 上，如果您希望消息框显示为其父级的 Qt::Sheet，请将消息框的窗口模式设置为 Qt::WindowModal 或使用 open() 。否则，消息框将是一个标准对话框。


--------------------------------
## __init__(icon, title, text[, buttons=QMessageBox.StandardButton.NoButton[, parent=None[, flags=Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint]]])

参数：

- icon – Icon
- title – str
- text – str
- buttons – Combination of StandardButton
- parent – QWidget
- flags – Combination of WindowType

使用给定的图标、标题、文本和标准按钮构造一个应用程序模式消息框。可以随时使用 addButton() 添加标准或自定义按钮。parent 和 f 参数传递给 QDialog 构造函数。

在调用 show() 之前，可以通过 setWindowModality() 覆盖窗口模式。

在 macOS 上，如果 parent 不是 None 并且您希望消息框显示为该父级的 Qt::Sheet，请将消息框的窗口模式设置为 Qt::WindowModal（默认）。否则，消息框将是一个标准对话框。


--------------------------------
## static about(parent, title, text)

参数：

- parent – QWidget
- title – str
- text – str

显示一个简单的 about 框，标题为 title，文本为 text。about 框的父级为 parent。

about() 在四个位置查找合适的图标：

1. 如果存在，则优先使用 parent->icon()。

2. 如果不存在，则尝试包含 parent 的顶级小部件。

3. 如果失败，则尝试 PySide6.QtWidgets.QApplication.activeWindow()

4. 作为最后的手段，它使用信息图标。

about 框有一个标记为“OK”的按钮。

在 macOS 上，about 框会弹出为非模式窗口；在其他平台上，它当前是应用程序模式。


--------------------------------
## static aboutQt(parent[, title=""])

参数：

- parent – QWidget
- title – str

显示一个关于 Qt 的简单消息框，带有给定的标题，位于父级上方（如果父级不为 None）。消息包括应用程序正在使用的 Qt 的版本号。

这对于包含在应用程序的帮助菜单中很有用，如菜单示例所示。

QApplication 以插槽的形式提供此功能。

在 macOS 上，aboutQt 框会弹出为非模式窗口；在其他平台上，它当前是应用程序模式。


--------------------------------
## addButton(button, role)

参数：

- button – QAbstractButton
- role – ButtonRole

将给定的按钮添加到具有指定角色的消息框。


--------------------------------
## addButton(button)

参数：

- button – StandardButton

返回类型：QPushButton

这是一个重载函数。

如果有效，则向消息框添加一个标准按钮，并返回该按钮。


--------------------------------
## addButton(text, role)

参数：

- text – str
- role – ButtonRole

返回类型：QPushButton

这是一个重载函数。

使用给定的文本创建一个按钮，将其添加到指定角色的消息框中，然后返回它。


--------------------------------
## button(which)

参数：

- which – StandardButton

返回类型：QAbstractButton

返回与标准按钮相对应的指针，如果此消息框中不存在标准按钮，则返回 None。


--------------------------------
## buttonClicked(button)

参数：

- button – QAbstractButton

每当 QMessageBox 中的按钮被点击时，都会发出此信号。被点击的按钮在按钮中返回。


--------------------------------
## buttonRole(button)

参数：

- button – QAbstractButton

返回类型：ButtonRole

返回指定按钮的按钮角色。如果按钮为 None 或尚未添加到消息框，则此函数返回 InvalidRole。


--------------------------------
## buttonText(button)

参数：

- button – int

返回类型：str

返回消息框按钮按钮的文本，如果消息框不包含按钮，则​​返回空字符串。

请改用 button() 和 text()。


--------------------------------
## buttons()

返回类型：list of QAbstractButton

返回已添加到消息框的所有按钮的列表。


--------------------------------
## checkBox()

返回类型：QCheckBox

返回对话框中显示的复选框。如果没有设置复选框，则返回 None。


--------------------------------
## clickedButton()

返回类型：QAbstractButton

返回用户点击的按钮，如果用户按下 Esc 键且未设置退出按钮，则返回 None。

如果尚未调用 exec()，则返回 nullptr。

示例：

```python
messageBox = QMessageBox(self)
disconnectButton =
      messageBox.addButton(tr("Disconnect"), QMessageBox.ActionRole)
...
messageBox.exec()
if messageBox.clickedButton() == disconnectButton:
    ...
```


--------------------------------
## static critical(parent, title, text, button0, button1)

参数：

- parent – QWidget
- title – str
- text – str
- button0 – StandardButton
- button1 – StandardButton

返回类型：int

在指定的父窗口小部件前面打开一个具有给定标题和文本的关键消息框。

标准按钮被添加到消息框中。 defaultButton 指定按下 Enter 时使用的按钮。 defaultButton 必须引用按钮中给出的按钮。 如果 defaultButton 为 NoButton ，QMessageBox 会自动选择合适的默认值。

返回单击的标准按钮的标识。 如果按下了 Esc ，则返回退出按钮。

消息框是应用程序模式对话框。


--------------------------------
## static critical(parent, title, text[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])

参数：

- parent – QWidget
- title – str
- text – str
- buttons – Combination of StandardButton
- defaultButton – StandardButton

返回类型：StandardButton

在指定的父窗口小部件前面打开一个具有给定标题和文本的关键消息框。

标准按钮被添加到消息框中。 defaultButton 指定按下 Enter 时使用的按钮。 defaultButton 必须引用按钮中给出的按钮。 如果 defaultButton 为 NoButton ，QMessageBox 会自动选择合适的默认值。

返回单击的标准按钮的标识。 如果按下了 Esc ，则返回退出按钮。

消息框是应用程序模式对话框。


--------------------------------
## defaultButton()

返回类型：QPushButton

返回应为消息框默认按钮的按钮。如果未设置默认按钮，则返回 nullptr。


--------------------------------
## detailedText()

返回类型：str

属性 DetailedText 的获取器。

--------------------------------
## escapeButton()

返回类型：QAbstractButton

返回按下退出键时激活的按钮。

默认情况下，QMessageBox 会尝试自动检测退出键，如下所示：

如果只有一个按钮，则将其设为退出键。

如果有取消按钮，则将其设为退出键。

仅在 macOS 上，如果只有一个按钮具有 RejectRole 角色，则将其设为退出键。

当无法自动检测到退出键时，按 Esc 键无效。


--------------------------------
## icon()

返回类型：Icon

属性图标的获取器。


--------------------------------
## iconPixmap()

返回类型：QPixmap

属性 iconPixmap 的获取器。


--------------------------------
## static information(parent, title, text[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])

参数：

- parent – QWidget
- title – str
- text – str
- buttons – Combination of StandardButton
- defaultButton – StandardButton

返回类型：StandardButton

在指定的父窗口小部件前面打开一个具有给定标题和文本的信息消息框。

标准按钮被添加到消息框中。 defaultButton 指定按下 Enter 时使用的按钮。 defaultButton 必须引用 buttons 中给出的按钮。 如果 defaultButton 为 NoButton ，QMessageBox 会自动选择合适的默认值。

返回单击的标准按钮的标识。 如果按下了 Esc ，则返回退出按钮。

消息框是应用程序模式对话框。


--------------------------------
## static information(parent, title, text, button0[, button1=QMessageBox.StandardButton.NoButton])

参数：

- parent – QWidget
- title – str
- text – str
- button0 – StandardButton
- button1 – StandardButton

返回类型：StandardButton

在指定的父窗口小部件前面打开一个具有给定标题和文本的信息消息框。

标准按钮被添加到消息框中。 defaultButton 指定按下 Enter 时使用的按钮。 defaultButton 必须引用 buttons 中给出的按钮。 如果 defaultButton 为 NoButton ，QMessageBox 会自动选择合适的默认值。

返回单击的标准按钮的标识。 如果按下了 Esc ，则返回退出按钮。

消息框是应用程序模式对话框。


--------------------------------
## informativeText()

返回类型：str

属性 informativeText 的获取器。


--------------------------------
## open(receiver, member)

参数：

- receiver – QObject
- member – str

打开对话框并将其 finish() 或 buttonClicked() 信号连接到接收器和成员指定的插槽。如果成员中的插槽的第一个参数有指针，则连接到 buttonClicked() ，否则连接到 finish() 。

当对话框关闭时，信号将与插槽断开连接。


--------------------------------
## options()

返回类型：Combination of Option


--------------------------------
## static question(parent, title, text[, buttons=QMessageBox.StandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)[, defaultButton=QMessageBox.StandardButton.NoButton]])

参数：

- parent – QWidget
- title – str
- text – str
- buttons – Combination of StandardButton
- defaultButton – StandardButton

返回类型：StandardButton

在指定的父窗口小部件前面打开一个带有给定标题和文本的问题消息框。

标准按钮被添加到消息框中。 defaultButton 指定按下 Enter 时使用的按钮。 defaultButton 必须引用按钮中给出的按钮。 如果 defaultButton 为 NoButton ，QMessageBox 会自动选择合适的默认值。

返回单击的标准按钮的标识。 如果按下了 Esc ，则返回退出按钮。

消息框是应用程序模式对话框。


--------------------------------
## static question(parent, title, text, button0, button1)

参数：

- parent – QWidget
- title – str
- text – str
- button0 – StandardButton
- button1 – StandardButton

返回类型：int

在指定的父窗口小部件前面打开一个带有给定标题和文本的问题消息框。

标准按钮被添加到消息框中。 defaultButton 指定按下 Enter 时使用的按钮。 defaultButton 必须引用按钮中给出的按钮。 如果 defaultButton 为 NoButton ，QMessageBox 会自动选择合适的默认值。

返回单击的标准按钮的标识。 如果按下了 Esc ，则返回退出按钮。

消息框是应用程序模式对话框。


--------------------------------
## removeButton(button)

参数：

- button – QAbstractButton

从按钮框中移除按钮但不删除它。


--------------------------------
## setButtonText(button, text)

参数：

- button – int
- text – str

将消息框按钮的文本设置为文本。设置不在消息框中的按钮的文本将被忽略。

请改用 addButton()。


--------------------------------
## setCheckBox(cb)

参数：

- cb – QCheckBox

在消息对话框中设置复选框 cb。消息框拥有复选框的所有权。参数 cb 可以为 None，以从消息框中删除现有复选框。


--------------------------------
## setDefaultButton(button)

参数：

- button – StandardButton

将消息框的默认按钮设置为按钮。


--------------------------------
## setDefaultButton(button)

参数：

- button – QPushButton

将消息框的默认按钮设置为按钮。


--------------------------------
## setDetailedText(text)

参数：

- text – str

属性 DetailedText 的设置器。


--------------------------------
## setEscapeButton(button)

参数：

- button – QAbstractButton

将按下 Esc 键时激活的按钮设置为按钮。


--------------------------------
## setEscapeButton(button)

参数：

- button – StandardButton

设置当按下 Esc 键时激活的按钮。


--------------------------------
## setIcon(arg__1)

参数：

- arg__1 – Icon

属性图标的设置者。


--------------------------------
## setIconPixmap(pixmap)

参数：

- pixmap – QPixmap

属性 iconPixmap 的设置者。


--------------------------------
## setInformativeText(text)

参数：

- text – str

属性 informativeText 的设置者。


--------------------------------
## setOption(option[, on=true])

参数：

- option – Option
- on – bool

如果 on 为真，则将给定选项设置为启用；否则，清除给定选项。

应在显示对话框之前设置选项（尤其是 DontUseNativeDialog 选项）。

在对话框可见时设置选项不能保证立即对对话框产生影响。

在更改其他属性后设置选项可能会导致这些值不起作用。


--------------------------------
## setOptions(options)

参数：

- options – Combination of Option


--------------------------------
## setStandardButtons(buttons)

参数：

- buttons – Combination of StandardButton


--------------------------------
## setText(text)

参数：

- text – str

Setter of property text  .


--------------------------------
## setTextFormat(format)

参数：

- format – TextFormat

Setter of property textFormat  .


--------------------------------
## setTextInteractionFlags(flags)

参数：

- flags – Combination of TextInteractionFlag

属性 textInteractionFlags 的设置者。


--------------------------------
## setWindowModality(windowModality)

参数：

- windowModality – WindowModality

此函数隐藏 setWindowModality() 。

将消息框的模式设置为 windowModality。

在 macOS 上，如果模式设置为 Qt::WindowModal 并且消息框有父级，则消息框将为 Qt::Sheet，否则消息框将为标准对话框。


--------------------------------
## setWindowTitle(title)

参数：

- title – str

此函数会隐藏 setWindowTitle() 。

将消息框的标题设置为 title。在 macOS 上，窗口标题会被忽略（根据 macOS 指南的要求）。


--------------------------------
## standardButton(button)

参数：

- button – QAbstractButton

返回类型：StandardButton

返回与给定按钮对应的标准按钮枚举值，如果给定按钮不是标准按钮，则返回 NoButton。


--------------------------------
## standardButtons()

返回类型：Combination of StandardButton


--------------------------------
## static standardIcon(icon)

参数：

- icon – Icon

返回类型：QPixmap

返回用于标准图标的像素图。这允许在更复杂的消息框中使用像素图。icon 指定所需的图标，例如问题、信息、警告或严重。

改为使用 SP_MessageBoxInformation 等调用 standardIcon()。


--------------------------------
## testOption(option)

参数：

- option – Option

返回类型：bool

如果给定选项启用，则返回 true；否则返回 false。


--------------------------------
## text()

返回类型：str

属性 text 的获取器。


--------------------------------
## textFormat()

返回类型：TextFormat

属性 textFormat 的获取器。


--------------------------------
## textInteractionFlags()

返回类型：Combination of TextInteractionFlag

属性 textInteractionFlags 的获取器。


--------------------------------
## static warning(parent, title, text[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])

参数：

- parent – QWidget
- title – str
- text – str
- buttons – Combination of StandardButton
- defaultButton – StandardButton

返回类型：StandardButton

在指定的父窗口小部件前面打开一个带有给定标题和文本的警告消息框。

标准按钮将添加到消息框中。 defaultButton 指定按下 Enter 时使用的按钮。 defaultButton 必须引用按钮中给出的按钮。 如果 defaultButton 为 NoButton ，QMessageBox 会自动选择合适的默认值。

返回单击的标准按钮的标识。 如果按下了 Esc ，则返回退出按钮。

消息框是应用程序模式对话框。


--------------------------------
## static warning(parent, title, text, button0, button1)

参数：

- parent – QWidget
- title – str
- text – str
- button0 – StandardButton
- button1 – StandardButton

返回类型：int

在指定的父窗口小部件前面打开一个带有给定标题和文本的警告消息框。

标准按钮将添加到消息框中。 defaultButton 指定按下 Enter 时使用的按钮。 defaultButton 必须引用按钮中给出的按钮。 如果 defaultButton 为 NoButton ，QMessageBox 会自动选择合适的默认值。

返回单击的标准按钮的标识。 如果按下了 Esc ，则返回退出按钮。

消息框是应用程序模式对话框。

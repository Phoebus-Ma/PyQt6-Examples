
[English doc](QProgressBar.md)

# class QProgressBar

QProgressBar 小部件提供水平或垂直进度条。


# Synopsis

## Properties

- [alignment](#property-alignment--combination-of-qtalignmentflag)

    进度条的对齐方式。

- [format](#property-format--str)

    用于生成当前文本的字符串。

- [invertedAppearance](#property-invertedappearance--bool)

    进度条是否反转显示进度。

- [maximum](#property-maximum--int)

    进度条的最大值。

- [minimum](#property-minimum--int)

    进度条的最小值。

- [orientation](#property-orientation--qtorientation)

    进度条的方向。

- [text](#property-text--str)

    随进度条显示的描述性文字。

- [textDirection](#property-textdirection--qprogressbardirection)

    垂直进度条的文本阅读方向。

- [textVisible](#property-textvisible--bool)

    是否显示当前完成的百分比。

- [value](#property-value--int)

    进度条的当前值。


## Methods

- [def \_\_init__()](#initparentnone)

- [def alignment()](#alignment)

- [def format()](#format)

- [def invertedAppearance()](#invertedappearance)

- [def isTextVisible()](#istextvisible)

- [def maximum()](#maximum)

- [def minimum()](#minimum)

- [def orientation()](#orientation)

- [def resetFormat()](#resetformat)

- [def setAlignment()](#setalignmentalignment)

- [def setFormat()](#setformatformat)

- [def setInvertedAppearance()](#setinvertedappearanceinvert)

- [def setTextDirection()](#settextdirectiontextdirection)

- [def setTextVisible()](#settextvisiblevisible)

- [def textDirection()](#textdirection)

- [def value()](#value)


## Virtual methods

- [def initStyleOption()](#initstyleoptionoption)

- [def text()](#text)


## Slots

- [def reset()](#reset)

- [def setMaximum()](#setmaximummaximum)

- [def setMinimum()](#setminimumminimum)

- [def setOrientation()](#setorientationarg__1)

- [def setRange()](#setrangeminimum-maximum)

- [def setValue()](#setvaluevalue)


## Signals

- [def valueChanged()](#valuechangedvalue)


# Detailed Description

进度条用于向用户指示操作的进度，并向他们保证应用程序仍在运行。

进度条使用步骤的概念。您可以通过指定最小和最大可能的步长值来设置它，当您稍后为其提供当前步长值时，它将显示已完成的步骤百分比。百分比是通过将进度 ( value() - minimum() ) 除以 maximum() - minimum() 来计算的。

您可以使用 setMinimum() 和 setMaximum 指定最小和最大步长数。当前步长数使用 setValue() 设置。可以使用 reset() 将进度条倒回到开头。

如果最小值和最大值都设置为 0，则进度条会显示繁忙指示符而不是步长百分比。这很有用，例如，当使用 QNetworkAccessManager 下载项目时，如果无法确定正在下载的项目的大小。


--------------------------------
## class Direction

指定垂直进度条文本的阅读方向。

| Constant                 | Description          |
| ------------------------ | -------------------- |
| QProgressBar.TopToBottom | 文本顺时针旋转 90 度。 |
| QProgressBar.BottomToTop | 文本逆时针旋转 90 度。 |

请注意，是否绘制文本取决于样式。目前 CleanLooks 和 Plastique 绘制文本。Mac、Windows 和 WindowsVista 样式不绘制文本。


--------------------------------
## property alignment : Combination of Qt.AlignmentFlag

此属性保存的是进度条的对齐方式。

访问函数：

- alignment()
- setAlignment()


--------------------------------
## property format : str

此属性保存用于生成当前文本的字符串。

%p - 替换为完成的百分比。 %v - 替换为当前值。 %m - 替换为总步骤数。

默认值为“%p%”。

访问函数：

- format()
- setFormat()
- resetFormat()


--------------------------------
## property invertedAppearance : bool

此属性用于控制进度条是否反转显示进度。

如果此属性为真，进度条将朝另一个方向增长（例如从右到左）。默认情况下，进度条不会反转。

访问函数：

- invertedAppearance()
- setInvertedAppearance()


--------------------------------
## property maximum : int

此属性保存进度条的最大值。

设置此属性时，会根据需要调整最小值以确保范围保持有效。如果当前值超出新范围，则使用 reset() 重置进度条。

访问函数：

- maximum()
- setMaximum()


--------------------------------
## property minimum : int

此属性保存进度条的最小值。

设置此属性时，会根据需要调整最大值以确保范围保持有效。如果当前值超出新范围，则使用 reset() 重置进度条。

访问函数：

- minimum()
- setMinimum()


--------------------------------
## property orientation : Qt.Orientation

此属性保存进度条的方向。

方向必须是 Qt::Horizo​​ntal（默认）或 Qt::Vertical。

访问函数：

- orientation()
- setOrientation()


--------------------------------
## property text : str

此属性保存与进度条一起显示的描述性文本。

返回的文本与进度条中心（或在某些样式中，左侧）显示的文本相同。

文本中显示的进度可能小于最小值，表示在设置任何进度之前，进度条处于“重置”状态。

在默认实现中，文本要么包含指示迄今为止进度的百分比值，要么为空白，因为进度条处于重置状态。

访问函数：

- text()


--------------------------------
## property textDirection : QProgressBar.Direction

此属性保存垂直进度条的文本阅读方向。

此属性对水平进度条没有影响。默认情况下，阅读方向为 TopToBottom 。

访问函数：

- textDirection()
- setTextDirection()


--------------------------------
## property textVisible : bool

此属性保存是否应显示当前完成的百分比。

样式可能会忽略此属性（例如，QMacStyle 从不绘制文本）。

访问函数：

- isTextVisible()
- setTextVisible()


--------------------------------
## property value : int

此属性保存进度条的当前值。

尝试将当前值更改为最小-最大范围之外的值不会对当前值产生任何影响。

访问函数：

- value()
- setValue()
- Signal valueChanged()


--------------------------------
## __init__([parent=None])

参数：

- parent – QWidget

使用给定的父级构造一个进度条。

默认情况下，最小步长值设置为 0，最大步长值设置为 100。


--------------------------------
## alignment()

返回类型：Combination of AlignmentFlag

属性 alignment 的获取器。


--------------------------------
## format()

返回类型：str

属性格式的获取器。


--------------------------------
## initStyleOption(option)

参数：

- option – QStyleOptionProgressBar

用此 QProgressBar 中的值初始化选项。当子类需要 QStyleOptionProgressBar 但又不想自己填写所有信息时，此方法非常有用。


--------------------------------
## invertedAppearance()

返回类型：bool

属性反转外观的获取器。


--------------------------------
## isTextVisible()

返回类型：bool

属性 textVisible 的获取器。


--------------------------------
## maximum()

返回类型：int

属性最大值的获取者。


--------------------------------
## minimum()

返回类型：int

属性最小值的获取者。


--------------------------------
## orientation()

返回类型：Orientation

属性方向的获取器。


--------------------------------
## reset()

重置进度条。进度条“倒退”并且不显示任何进度。


--------------------------------
## resetFormat()

属性格式的重置功能。


--------------------------------
## setAlignment(alignment)

参数：

- alignment – Combination of AlignmentFlag

属性对齐的设置者。


--------------------------------
## setFormat(format)

参数：

- format – str

属性格式的设置者。


--------------------------------
## setInvertedAppearance(invert)

参数：

- invert – bool

属性的设置器反转外观。


--------------------------------
## setMaximum(maximum)

参数：

- maximum – int

属性最大值的设置者。


--------------------------------
## setMinimum(minimum)

参数：

- minimum – int

财产最低限额的设定者 。


--------------------------------
## setOrientation(arg__1)

参数：

- arg__1 – Orientation

属性方向的设置者。


--------------------------------
## setRange(minimum, maximum)

参数：

- minimum – int
- maximum – int

将进度条的最小值和最大值分别设置为最小值和最大值。

如果最大值小于最小值，则最小值将成为唯一合法值。

如果当前值超出新范围，则使用 reset() 重置进度条。

可以使用 setRange(0, 0) 将 QProgressBar 设置为未确定状态。


--------------------------------
## setTextDirection(textDirection)

参数：

- textDirection – Direction

属性 textDirection 的设置器。


--------------------------------
## setTextVisible(visible)

参数：

- visible – bool

属性 textVisible 的设置者。


--------------------------------
## setValue(value)

参数：

- value – int

属性值的设置者。


--------------------------------
## text()

返回类型：str

属性 text 的获取器。


--------------------------------
## textDirection()

返回类型：Direction

属性 textDirection 的获取器。


--------------------------------
## value()

返回类型：int

属性值的获取器。


--------------------------------
## valueChanged(value)

参数：

- value – int

当进度条显示的值发生变化时发出此信号。value 是进度条显示的新值。

属性 value 的通知信号。

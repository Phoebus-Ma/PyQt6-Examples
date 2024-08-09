
[English doc](QWidget.md)

# class QWidget

QWidget 类是所有用户界面对象的基类。


# Synopsis

## Properties

- [acceptDrops](#property-acceptdrops--bool)

    是否为此小部件启用放置事件。

- [accessibleDescription](#property-accessibledescription--str)

    辅助技术所见的小部件描述。

- [accessibleName](#property-accessiblename--str)

    辅助技术所见的小部件名称。

- [autoFillBackground](#property-autofillbackground--bool)

    小部件背景是否自动填充。

- [baseSize](#property-basesize--qsize)

    小部件的基本尺寸。

- [childrenRect](#property-childrenrect--qrect)

    小部件子项的边界矩形。

- [childrenRegion](#property-childrenregion--qregion)

    小部件的子部件所占据的组合区域。

- [contextMenuPolicy](#property-contextmenupolicy--qtcontextmenupolicy)

    小部件如何显示上下文菜单。

- [cursor](#property-cursor--qcursor)

    此小部件的光标形状。

- [enabled](#property-enabled--bool)

    小部件是否已启用。

- [focus](#property-focus--bool)

    此小部件（或其焦点代理）是否具有键盘输入焦点。

- [focusPolicy](#property-focuspolicy--qtfocuspolicy)

    小部件接受键盘焦点的方式。

- [font](#property-font--qfont)

    当前为小部件设置的字体。

- [frameGeometry](#property-framegeometry--qrect)

    小部件相对于其父级（包括任何窗口框架）的几何形状。

- [frameSize](#property-framesize--qsize)

    小部件的大小（包括任何窗口框架）

- [fullScreen](#property-fullscreen--bool)

    小部件是否以全屏模式显示。

- [geometry](#property-geometry--qrect)

    小部件相对于其父级的几何形状，不包括窗口框架。

- [height](#property-height--int)

    不包括任何窗口框架的小部件的高度。

- [inputMethodHints](#property-inputmethodhints--combination-of-qtinputmethodhint)

    小部件具有哪些输入法特定提示。

- [isActiveWindow](#property-isactivewindow--bool)

    此小部件的窗口是否为活动窗口。

- [layoutDirection](#property-layoutdirection--qtlayoutdirection)

    此小部件的布局方向。

- [locale](#property-locale--qlocale)

    小部件的语言环境。

- [maximized](#property-maximized--bool)

    此小部件是否最大化。

- [maximumHeight](#property-maximumheight--int)

    小部件的最大高度（以像素为单位）。

- [maximumSize](#property-maximumsize--qsize)

    小部件的最大尺寸（以像素为单位）。

- [maximumWidth](#property-maximumwidth--int)

    小部件的最大宽度（以像素为单位）。

- [minimized](#property-minimized--bool)

    此小部件是否最小化（图标化）。

- [minimumHeight](#property-minimumheight--int)

    小部件的最小高度（以像素为单位）。

- [minimumSize](#property-minimumsize--qsize)

    小部件的最小尺寸。

- [minimumSizeHint](#property-minimumsizehint--qsize)

    建议的小部件的最小尺寸。

- [minimumWidth](#property-minimumwidth--int)

    小部件的最小宽度（以像素为单位）。

- [modal](#property-modal--bool)

    该小部件是否是模态小部件。

- [mouseTracking](#property-mousetracking--bool)

    是否为小部件启用鼠标跟踪。

- [normalGeometry](#property-normalgeometry--qrect)

    当窗口小部件显示为正常（非最大化或全屏）顶层窗口小部件时，其几何形状将会出现。

- [palette](#property-palette--qpalette)

    小部件的调色板。

- [pos](#property-pos--qpoint)

    小部件在其父小部件中的位置。

- [rect](#property-rect--qrect)

    窗口小部件的内部几何形状（不包括任何窗口框架）。

- [size](#property-size--qsize)

    不包括任何窗口框架的小部件的大小。

- [sizeHint](#property-sizehint--qsize)

    小部件的推荐尺寸。

- [sizeIncrement](#property-sizeincrement--qsize)

    小部件的尺寸增量。

- [sizePolicy](#property-sizepolicy--qsizepolicy)

    小部件的默认布局行为。

- [statusTip](#property-statustip--str)

    小部件的状态提示。

- [styleSheet](#property-stylesheet--str)

    小部件的样式表。

- [tabletTracking](#property-tablettracking--bool)

    是否为小部件启用平板电脑跟踪。

- [toolTip](#property-tooltip--str)

    小部件的工具提示。

- [toolTipDuration](#property-tooltipduration--int)

    小部件的工具提示持续时间。

- [updatesEnabled](#property-updatesenabled--bool)

    是否启用更新。

- [visible](#property-visible--bool)

    小部件是否可见。

- [whatsThis](#property-whatsthis--str)

    小部件的“这是什么”帮助文本。

- [width](#property-width--int)

    不包括任何窗口框架的小部件的宽度。

- [windowFilePath](#property-windowfilepath--str)

    与小部件关联的文件路径。

- [windowIcon](#property-windowicon--qicon)

    小部件的图标。

- [windowIconText](#property-windowicontext--str)

    最小化窗口图标上显示的文本。

- [windowModality](#property-windowmodality--qtwindowmodality)

    哪些窗口被模态窗口小部件阻挡。

- [windowModified](#property-windowmodified--bool)

    窗口中显示的文档是否有未保存的更改。

- [windowOpacity](#property-windowopacity--float)

    窗口的不透明度。

- [windowTitle](#property-windowtitle--str)

    窗口标题（cap）。

- [x](#property-x--int)

    小部件相对于其父级（包括任何窗口框架）的 x 坐标。

- [y](#property-y--int)

    小部件相对于其父级的 y 坐标，包括任何窗口框架。


## Methods

- [def \_\_init__()](#initparentnone-fqtwindowflags)

- [def acceptDrops()](#acceptdrops)

- [def accessibleDescription()](#accessibledescription)

- [def accessibleName()](#accessiblename)

- [def actions()](#actions)

- [def activateWindow()](#activatewindow)

- [def addAction()](#addactionaction)

- [def addActions()](#addactionsactions)

- [def adjustSize()](#adjustsize)

- [def autoFillBackground()](#autofillbackground)

- [def backgroundRole()](#backgroundrole)

- [def backingStore()](#backingstore)

- [def baseSize()](#basesize)

- [def childAt()](#childatp)

- [def childrenRect()](#childrenrect)

- [def childrenRegion()](#childrenregion)

- [def clearFocus()](#clearfocus)

- [def clearMask()](#clearmask)

- [def contentsMargins()](#contentsmargins)

- [def contentsRect()](#contentsrect)

- [def contextMenuPolicy()](#contextmenupolicy)

- [def create()](#createarg__10-initializewindowtrue-destroyoldwindowtrue)

- [def createWinId()](#createwinid)

- [def cursor()](#cursor)

- [def destroy()](#destroydestroywindowtrue-destroysubwindowstrue)

- [def effectiveWinId()](#effectivewinid)

- [def ensurePolished()](#ensurepolished)

- [def focusNextChild()](#focusnextchild)

- [def focusPolicy()](#focuspolicy)

- [def focusPreviousChild()](#focuspreviouschild)

- [def focusProxy()](#focusproxy)

- [def focusWidget()](#focuswidget)

- [def font()](#font)

- [def fontInfo()](#fontinfo)

- [def fontMetrics()](#fontmetrics)

- [def foregroundRole()](#foregroundrole)

- [def frameGeometry()](#framegeometry)

- [def frameSize()](#framesize)

- [def geometry()](#geometry)

- [def grab()](#grabrectangleqrectqpoint0-0-qsize-1--1)

- [def grabGesture()](#grabgesturetype-flagsqtgestureflags)

- [def grabKeyboard()](#grabkeyboard)

- [def grabMouse()](#grabmouse)

- [def grabShortcut()](#grabshortcutkey-contextqtwindowshortcut)

- [def graphicsEffect()](#graphicseffect)

- [def graphicsProxyWidget()](#graphicsproxywidget)

- [def hasFocus()](#hasfocus)

- [def hasMouseTracking()](#hasmousetracking)

- [def hasTabletTracking()](#hastablettracking)

- [def inputMethodHints()](#inputmethodhints)

- [def insertAction()](#insertactionbefore-action)

- [def insertActions()](#insertactionsbefore-actions)

- [def internalWinId()](#internalwinid)

- [def isActiveWindow()](#isactivewindow)

- [def isAncestorOf()](#isancestorofchild)

- [def isEnabled()](#isenabled)

- [def isEnabledTo()](#isenabledtoarg__1)

- [def isFullScreen()](#isfullscreen)

- [def isHidden()](#ishidden)

- [def isLeftToRight()](#islefttoright)

- [def isMaximized()](#ismaximized)

- [def isMinimized()](#isminimized)

- [def isModal()](#ismodal)

- [def isRightToLeft()](#isrighttoleft)

- [def isTopLevel()](#istoplevel)

- [def isVisible()](#isvisible)

- [def isVisibleTo()](#isvisibletoarg__1)

- [def isWindow()](#iswindow)

- [def isWindowModified()](#iswindowmodified)

- [def layout()](#layout)

- [def layoutDirection()](#layoutdirection)

- [def locale()](#locale)

- [def mapFrom()](#mapfromarg__1-arg__2)

- [def mapFromGlobal()](#mapfromglobalarg__1)

- [def mapFromParent()](#mapfromparentarg__1)

- [def mapTo()](#maptoarg__1-arg__2)

- [def mapToGlobal()](#maptoglobalarg__1)

- [def mapToParent()](#maptoparentarg__1)

- [def mask()](#mask)

- [def maximumHeight()](#maximumheight)

- [def maximumSize()](#maximumsize)

- [def maximumWidth()](#maximumwidth)

- [def minimumHeight()](#minimumheight)

- [def minimumSize()](#minimumsize)

- [def minimumWidth()](#minimumwidth)

- [def move()](#movearg__1)

- [def nativeParentWidget()](#nativeparentwidget)

- [def nextInFocusChain()](#nextinfocuschain)

- [def normalGeometry()](#normalgeometry)

- [def overrideWindowFlags()](#overridewindowflagstype)

- [def overrideWindowState()](#overridewindowstatestate)

- [def palette()](#palette)

- [def parentWidget()](#parentwidget)

- [def pos()](#pos)

- [def previousInFocusChain()](#previousinfocuschain)

- [def rect()](#rect)

- [def releaseKeyboard()](#releasekeyboard)

- [def releaseMouse()](#releasemouse)

- [def releaseShortcut()](#releaseshortcutid)

- [def removeAction()](#removeactionaction)

- [def render()](#renderpainter-targetoffset-sourceregionqregion-renderflagsqwidgetrenderflagsqwidgetrenderflagdrawwindowbackground--qwidgetrenderflagdrawchildren)

- [def repaint()](#repaint)

- [def resize()](#resizearg__1)

- [def restoreGeometry()](#restoregeometrygeometry)

- [def saveGeometry()](#savegeometry)

- [def screen()](#screen)

- [def scroll()](#scrolldx-dy)

- [def setAcceptDrops()](#setacceptdropson)

- [def setAccessibleDescription()](#setaccessibledescriptiondescription)

- [def setAccessibleName()](#setaccessiblenamename)

- [def setAttribute()](#setattributearg__1-ontrue)

- [def setAutoFillBackground()](#setautofillbackgroundenabled)

- [def setBackgroundRole()](#setbackgroundrolearg__1)

- [def setBaseSize()](#setbasesizearg__1)

- [def setContentsMargins()](#setcontentsmarginsmargins)

- [def setContextMenuPolicy()](#setcontextmenupolicypolicy)

- [def setCursor()](#setcursorarg__1)

- [def setFixedHeight()](#setfixedheighth)

- [def setFixedSize()](#setfixedsizearg__1)

- [def setFixedWidth()](#setfixedwidthw)

- [def setFocus()](#setfocus)

- [def setFocusPolicy()](#setfocuspolicypolicy)

- [def setFocusProxy()](#setfocusproxyarg__1)

- [def setFont()](#setfontarg__1)

- [def setForegroundRole()](#setforegroundrolearg__1)

- [def setGeometry()](#setgeometryarg__1)

- [def setGraphicsEffect()](#setgraphicseffecteffect)

- [def setInputMethodHints()](#setinputmethodhintshints)

- [def setLayout()](#setlayoutarg__1)

- [def setLayoutDirection()](#setlayoutdirectiondirection)

- [def setLocale()](#setlocalelocale)

- [def setMask()](#setmaskarg__1)

- [def setMaximumHeight()](#setmaximumheightmaxh)

- [def setMaximumSize()](#setmaximumsizearg__1)

- [def setMaximumWidth()](#setmaximumwidthmaxw)

- [def setMinimumHeight()](#setminimumheightminh)

- [def setMinimumSize()](#setminimumsizearg__1)

- [def setMinimumWidth()](#setminimumwidthminw)

- [def setMouseTracking()](#setmousetrackingenable)

- [def setPalette()](#setpalettearg__1)

- [def setParent()](#setparentparent)

- [def setScreen()](#setscreenarg__1)

- [def setShortcutAutoRepeat()](#setshortcutautorepeatid-enabletrue)

- [def setShortcutEnabled()](#setshortcutenabledid-enabletrue)

- [def setSizeIncrement()](#setsizeincrementarg__1)

- [def setSizePolicy()](#setsizepolicyarg__1)

- [def setStatusTip()](#setstatustiparg__1)

- [def setStyle()](#setstylearg__1)

- [def setTabletTracking()](#settablettrackingenable)

- [def setToolTip()](#settooltiparg__1)

- [def setToolTipDuration()](#settooltipdurationmsec)

- [def setUpdatesEnabled()](#setupdatesenabledenable)

- [def setWhatsThis()](#setwhatsthisarg__1)

- [def setWindowFilePath()](#setwindowfilepathfilepath)

- [def setWindowFlag()](#setwindowflagarg__1-ontrue)

- [def setWindowFlags()](#setwindowflagstype)

- [def setWindowIcon()](#setwindowiconicon)

- [def setWindowIconText()](#setwindowicontextarg__1)

- [def setWindowModality()](#setwindowmodalitywindowmodality)

- [def setWindowOpacity()](#setwindowopacitylevel)

- [def setWindowRole()](#setwindowrolearg__1)

- [def setWindowState()](#setwindowstatestate)

- [def size()](#size)

- [def sizeIncrement()](#sizeincrement)

- [def sizePolicy()](#sizepolicy)

- [def stackUnder()](#stackunderarg__1)

- [def statusTip()](#statustip)

- [def style()](#style)

- [def styleSheet()](#stylesheet)

- [def testAttribute()](#testattributearg__1)

- [def toolTip()](#tooltip)

- [def toolTipDuration()](#tooltipduration)

- [def topLevelWidget()](#toplevelwidget)

- [def underMouse()](#undermouse)

- [def ungrabGesture()](#ungrabgesturetype)

- [def unsetCursor()](#unsetcursor)

- [def unsetLayoutDirection()](#unsetlayoutdirection)

- [def unsetLocale()](#unsetlocale)

- [def update()](#update)

- [def updateGeometry()](#updategeometry)

- [def updatesEnabled()](#updatesenabled)

- [def visibleRegion()](#visibleregion)

- [def whatsThis()](#whatsthis)

- [def winId()](#winid)

- [def window()](#window)

- [def windowFilePath()](#windowfilepath)

- [def windowFlags()](#windowflags)

- [def windowHandle()](#windowhandle)

- [def windowIcon()](#windowicon)

- [def windowIconText()](#windowicontext)

- [def windowModality()](#windowmodality)

- [def windowOpacity()](#windowopacity)

- [def windowRole()](#windowrole)

- [def windowState()](#windowstate)

- [def windowTitle()](#windowtitle)

- [def windowType()](#windowtype)

- [def x()](#x)

- [def y()](#y)


## Virtual methods

- [def actionEvent()](#actioneventevent)

- [def changeEvent()](#changeeventevent)

- [def closeEvent()](#closeeventevent)

- [def contextMenuEvent()](#contextmenueventevent)

- [def dragEnterEvent()](#dragentereventevent)

- [def dragLeaveEvent()](#dragleaveeventevent)

- [def dragMoveEvent()](#dragmoveeventevent)

- [def dropEvent()](#dropeventevent)

- [def enterEvent()](#entereventevent)

- [def focusInEvent()](#focusineventevent)

- [def focusNextPrevChild()](#focusnextprevchildnext)

- [def focusOutEvent()](#focusouteventevent)

- [def hasHeightForWidth()](#hasheightforwidth)

- [def heightForWidth()](#heightforwidtharg__1)

- [def hideEvent()](#hideeventevent)

- [def inputMethodEvent()](#inputmethodeventevent)

- [def inputMethodQuery()](#inputmethodqueryarg__1)

- [def keyPressEvent()](#keypresseventevent)

- [def keyReleaseEvent()](#keyreleaseeventevent)

- [def leaveEvent()](#leaveeventevent)

- [def minimumSizeHint()](#minimumsizehint)

- [def mouseDoubleClickEvent()](#mousedoubleclickeventevent)

- [def mouseMoveEvent()](#mousemoveeventevent)

- [def mousePressEvent()](#mousepresseventevent)

- [def mouseReleaseEvent()](#mousereleaseeventevent)

- [def moveEvent()](#moveeventevent)

- [def nativeEvent()](#nativeeventeventtype-message)

- [def paintEvent()](#painteventevent)

- [def resizeEvent()](#resizeeventevent)

- [def setVisible()](#setvisiblevisible)

- [def showEvent()](#showeventevent)

- [def sizeHint()](#sizehint)

- [def tabletEvent()](#tableteventevent)

- [def wheelEvent()](#wheeleventevent)


## Slots

- [def close()](#close)

- [def hide()](#hide)

- [def lower()](#lower)

- [def raise_()](#raise_)

- [def repaint()](#repaint)

- [def setDisabled()](#setdisabledarg__1)

- [def setEnabled()](#setenabledarg__1)

- [def setFocus()](#setfocus)

- [def setHidden()](#sethiddenhidden)

- [def setStyleSheet()](#setstylesheetstylesheet)

- [def setWindowModified()](#setwindowmodifiedarg__1)

- [def setWindowTitle()](#setwindowtitlearg__1)

- [def show()](#show)

- [def showFullScreen()](#showfullscreen)

- [def showMaximized()](#showmaximized)

- [def showMinimized()](#showminimized)

- [def showNormal()](#shownormal)

- [def update()](#update)

- [def updateMicroFocus()](#updatemicrofocusqueryqtimqueryall)


## Signals

- [def customContextMenuRequested()](#customcontextmenurequestedpos)

- [def windowIconChanged()](#windowiconchangedicon)

- [def windowIconTextChanged()](#windowicontextchangedicontext)

- [def windowTitleChanged()](#windowtitlechangedtitle)


## Static functions

- [def createWindowContainer()](#static-createwindowcontainerwindow-parentnone-flagsqtwindowflags)

- [def find()](#static-findarg__1)

- [def keyboardGrabber()](#static-keyboardgrabber)

- [def mouseGrabber()](#static-mousegrabber)

- [def setTabOrder()](#static-settaborderarg__1-arg__2)


# Detailed Description

小部件是用户界面的原子：它从窗口系统接收鼠标、键盘和其他事件，并在屏幕上绘制自己的表示。每个小部件都是矩形的，它们按 Z 顺序排序。小部件由其父部件和其前面的小部件裁剪。

未嵌入父部件的小部件称为窗口。通常，窗口有一个框架和一个标题栏，但也可以使用合适的窗口标志创建没有这种装饰的窗口。在 Qt 中，QMainWindow 和 QDialog 的各种子类是最常见的窗口类型。

每个小部件的构造函数都接受一个或两个标准参数：

1. QWidget *parent = nullptr 是新小部件的父部件。如果它是 None（默认值），则新小部件将是一个窗口。如果不是，它将是父部件的子部件，并受父部件的几何形状约束（除非您将 Qt::Window 指定为窗口标志）。

2. Qt::WindowFlags f = { }（如果可用）设置窗口标志；默认值适用于大多数窗口小部件，但要获取（例如）没有窗口系统框架的窗口，则必须使用特殊标志。

QWidget 有许多成员函数，但其​​中一些几乎没有直接功能；例如，QWidget 有一个字体属性，但它本身从不使用它。有许多子类提供真正的功能，例如 QLabel 、 QPushButton 、 QListWidget 和 QTabWidget 。


## Top-Level and Child Widgets

没有父窗口小部件的窗口小部件始终是独立窗口（顶级窗口小部件）。对于这些窗口小部件，setWindowTitle() 和 setWindowIcon() 分别设置标题栏和图标。

非窗口窗口小部件是子窗口小部件，显示在其父窗口小部件内。Qt 中的大多数窗口小部件主要用作子窗口小部件。例如，可以将按钮显示为顶级窗口，但大多数人更喜欢将按钮放在其他窗口小部件中，例如 QDialog 。

上图显示了 QGroupBox 小部件，用于在 QGridLayout 提供的布局中容纳各种子窗口小部件。QLabel 子窗口小部件已被勾勒出来以指示其完整尺寸。

如果您想使用 QWidget 来容纳子窗口小部件，通常需要向父 QWidget 添加布局。有关更多信息，请参阅布局管理。


## Composite Widgets

当小部件用作容器来对多个子小部件进行分组时，它被称为复合小部件。可以通过构造具有所需视觉属性的小部件（例如 QFrame ）并向其添加子小部件（通常由布局管理）来创建这些小部件。

还可以通过对标准小部件（例如 QWidget 或 QFrame ）进行子类化并在子类的构造函数中添加必要的布局和子小部件来创建复合小部件。Qt 提供的许多示例都使用这种方法，Qt Widgets 教程中也介绍了这种方法。


## Custom Widgets and Painting

由于 QWidget 是 QPaintDevice 的子类，因此可以使用子类来显示自定义内容，这些内容由 QPainter 类的实例通过一系列绘制操作组成。这种方法与图形视图框架使用的画布样式方法形成对比，在画布样式方法中，项目由应用程序添加到场景中，并由框架本身进行渲染。

每个小部件都在其 paintEvent() 函数中执行所有绘制操作。每当小部件需要重新绘制时，都会调用此函数，无论是由于某些外部更改还是应用程序请求。

模拟时钟示例展示了一个简单的小部件如何处理绘制事件。


## Size Hints and Size Policies

在实现新的小部件时，重新实现 sizeHint() 以提供小部件的合理默认大小并使用 setSizePolicy() 设置正确的大小策略几乎总是有用的。

默认情况下，不提供大小提示的复合小部件将根据其子小部件的空间要求进行大小调整。

大小策略允许您为布局管理系统提供良好的默认行为，以便其他小部件可以轻松包含和管理您的小部件。默认大小策略表示大小提示代表小部件的首选大小，这通常对许多小部件来说已经足够好了。


## Events

小部件响应通常由用户操作引起的事件。Qt 通过调用特定的事件处理程序函数（其中包含有关每个事件的信息的 QEvent 子类实例）将事件传递给小部件。

如果您的小部件仅包含子小部件，则可能不需要实现任何事件处理程序。如果您想检测子小部件中的鼠标单击，请在小部件的 mousePressEvent() 中调用子部件的 underMouse() 函数。

Scribble 示例实现了一组更广泛的事件来处理鼠标移动、按钮按下和窗口大小调整。

您需要为自己的窗口小部件提供行为和内容，但这里简要概述了与 QWidget 相关的事件，从最常见的事件开始：

- 每当需要重新绘制小部件时，都会调用 paintEvent()。每个显示自定义内容的小部件都必须实现它。使用 QPainter 进行绘制只能在 paintEvent() 或由 paintEvent() 调用的函数中进行。

- 调整小部件大小后会调用 resizeEvent()。

- 当鼠标光标位于窗口小部件内时按下鼠标按钮，或当窗口小部件使用 grabMouse() 抓取鼠标时，将调用 mousePressEvent() 。按下鼠标而不释放它实际上与调用 grabMouse() 相同。

- 当释放鼠标按钮时，将调用 mouseReleaseEvent() 。窗口小部件在收到相应的鼠标按下事件时会接收鼠标释放事件。这意味着，如果用户在窗口小部件内按下鼠标，然后在释放鼠标按钮之前将鼠标拖到其他地方，则窗口小部件会收到释放事件。有一个例外：如果在按住鼠标按钮时出现弹出菜单，则此弹出菜单会立即窃取鼠标事件。

- 当用户在窗口小部件中双击时，将调用 mouseDoubleClickEvent() 。如果用户双击，则窗口小部件会收到鼠标按下事件、鼠标释放事件、（鼠标单击事件）、第二次鼠标按下、此事件以及最后的第二次鼠标释放事件。 （如果在此操作期间鼠标没有保持稳定，也可能会收到一些鼠标移动事件。）在第二次单击到来之前，无法区分单击和双击。（这就是为什么大多数 GUI 书籍建议将双击作为单击的扩展，而不是触发不同的操作的原因之一。）

接受键盘输入的小部件需要重新实现几个事件处理程序：

- 每次按下某个键时都会调用 keyPressEvent()，并且当某个键被按住足够长的时间以使其自动重复时，也会再次调用。只有当焦点更改机制未使用 Tab 和 Shift+Tab 键时，才会将它们传递给小部件。要强制小部件处理这些键，您必须重新实现 event() 。

- 当小部件获得键盘焦点时（假设您已调用 setFocusPolicy() ），会调用 focusInEvent() 。行为良好的小部件会以清晰但谨慎的方式表明它们拥有键盘焦点。

- 当小部件失去键盘焦点时，将调用 focusOutEvent()。

您可能还需要重新实现一些不太常见的事件处理程序：

- 鼠标在按住鼠标按钮的情况下移动时，将调用 mouseMoveEvent()。这在拖放操作期间很有用。如果您调用 setMouseTracking (true)，即使没有按下任何按钮，您也会收到鼠标移动事件。（另请参阅拖放指南。）

- 每当释放按键并按住按键时（如果按键是自动重复的），将调用 keyReleaseEvent()。在这种情况下，小部件将在每次重复时收到一对按键释放和按键按下事件。只有当焦点更改机制未使用 Tab 和 Shift+Tab 键时，它们才会传递给小部件。要强制小部件处理这些键，您必须重新实现 event()。

- 每当用户在小部件具有焦点的情况下转动鼠标滚轮时，将调用 wheelEvent()。

- 当鼠标进入小部件的屏幕空间时，将调用 enterEvent()。 （这不包括小部件的任何子部件所拥有的屏幕空间。）

- 当鼠标离开小部件的屏幕空间时，将调用 leaveEvent()。如果鼠标进入子小部件，则不会引起 leaveEvent()。

- 当小部件相对于其父部件移动时，将调用 moveEvent()。

- 当用户关闭小部件时（或调用 close() 时），将调用 closeEvent()。

QEvent::Type 的文档中还描述了一些相当晦涩的事件。要处理这些事件，您需要直接重新实现 event()。

event() 的默认实现处理 Tab 和 Shift+Tab（用于移动键盘焦点），并将大多数其他事件传递给上述更专业的处理程序之一。

事件和用于传递它们的机制在事件系统中介绍。


## Groups of Functions and Properties

| Context           | Functions and Properties |
| ----------------- | ------------------------ |
| Window functions  | show() , hide() , raise() , lower() , close() . |
| Top-level windows | windowModified , windowTitle , windowIcon , isActiveWindow , activateWindow() , minimized , showMinimized() , maximized , showMaximized() , fullScreen , showFullScreen() , showNormal() . |
| Window contents   | update() , repaint() , scroll() . |
| Geometry          | pos , x() , y() , rect , size , width() , height() , move() , resize() , sizePolicy , sizeHint() , minimumSizeHint() , updateGeometry() , layout() , frameGeometry , geometry , childrenRect , childrenRegion , adjustSize() , mapFromGlobal() , mapToGlobal() , mapFromParent() , mapToParent() , maximumSize , minimumSize , sizeIncrement , baseSize , setFixedSize() |
| Mode              | visible , isVisibleTo() , enabled , isEnabledTo() , modal , isWindow() , mouseTracking , updatesEnabled , visibleRegion() . |
| Look and feel     | style() , setStyle() , styleSheet , cursor , font , palette , backgroundRole() , setBackgroundRole() , fontInfo() , fontMetrics() . |
| Keyboard focus functions | focus , focusPolicy , setFocus() , clearFocus() , setTabOrder() , setFocusProxy() , focusNextChild() , focusPreviousChild() . |
| Mouse and keyboard grabbing | grabMouse() , releaseMouse() , grabKeyboard() , releaseKeyboard() , mouseGrabber() , keyboardGrabber() . |
| Event handlers    | event() , mousePressEvent() , mouseReleaseEvent() , mouseDoubleClickEvent() , mouseMoveEvent() , keyPressEvent() , keyReleaseEvent() , focusInEvent() , focusOutEvent() , wheelEvent() , enterEvent() , leaveEvent() , paintEvent() , moveEvent() , resizeEvent() , closeEvent() , dragEnterEvent() , dragMoveEvent() , dragLeaveEvent() , dropEvent() , childEvent(), showEvent() , hideEvent() , customEvent(). changeEvent() , |
| System functions  | parentWidget() , window() , setParent() , winId() , find() , metric() . |
| Context menu      | contextMenuPolicy , contextMenuEvent() , customContextMenuRequested() , actions() |
| Interactive help  | setToolTip() , setWhatsThis() |


## Widget Style Sheets

除了每个平台的标准小部件样式外，还可以根据样式表中指定的规则对小部件进行样式设置。此功能使您能够自定义特定小部件的外观，以向用户提供有关其用途的视觉提示。例如，可以以特定方式对按钮进行样式设置，以指示它执行破坏性操作。

Qt 样式表文档中更详细地描述了小部件样式表的使用。


## Transparency and Double Buffering

QWidget 自动对其绘制进行双缓冲，因此无需在 paintEvent() 中编写双缓冲代码来避免闪烁。

只要未设置 Qt::WA_PaintOnScreen，父窗口小部件的内容就会默认传播到其每个子窗口小部件。可以编写自定义窗口小部件来利用此功能，方法是更新不规则区域（以创建非矩形子窗口小部件），或使用具有小于完整 alpha 分量的颜色进行绘制。下图显示了如何微调自定义窗口小部件的属性和特性以实现不同的效果。

在上图中，构建了一个移除了某个区域的半透明矩形子窗口小部件并将其添加到父窗口小部件（显示像素图的 QLabel）。然后，设置不同的属性和窗口小部件属性以实现不同的效果：

- 左侧窗口小部件没有设置其他属性或窗口小部件属性。此默认状态适合大多数具有透明度、形状不规则或不使用不透明画笔绘制整个区域的自定义窗口小部件。

- 中心小部件设置了 autoFillBackground 属性。此属性用于依赖小部件提供默认背景且不使用不透明画笔绘制其整个区域的自定义小部件。

- 右侧小部件设置了 Qt::WA_OpaquePaintEvent 小部件属性。这表示小部件将使用不透明颜色绘制其整个区域。小部件的区域最初将未初始化，在图中以红色对角网格图案表示，该图案透过覆盖的区域发光。

要快速更新具有简单背景颜色的自定义小部件（例如实时绘图或图形小部件），最好定义合适的背景颜色（使用带有 QPalette::Window 角色的 setBackgroundRole()），设置 autoFillBackground 属性，并仅在小部件的 paintEvent() 中实现必要的绘图功能。

要快速更新不断用不透明内容覆盖整个区域的自定义小部件（例如视频流小部件），最好设置小部件的 Qt::WA_OpaquePaintEvent，避免与重新绘制小部件背景相关的任何不必要的开销。

如果小部件同时设置了 Qt::WA_OpaquePaintEvent 小部件属性和 autoFillBackground 属性，则 Qt::WA_OpaquePaintEvent 属性优先。根据您的要求，您应该选择其中之一。

父小部件的内容也会传播到标准 Qt 小部件。如果父小部件以非标准方式装饰，这可能会导致一些意外结果，如下图所示。

无需诉诸子类化即可自定义标准 Qt 小部件的绘制行为的范围略小于自定义小部件的范围。通常，可以通过设置标准小部件的 autoFillBackground 属性来实现其所需的外观。


## Creating Translucent Windows

您可以在支持合成的窗口系统上创建具有半透明区域的窗口。

要在顶级小部件中启用此功能，请使用 setAttribute() 设置其 Qt::WA_TranslucentBackground 属性，并确保其背景在您希望部分透明的区域中用非不透明颜色绘制。

平台说明：

- X11：此功能依赖于使用支持 ARGB 视觉效果和合成窗口管理器的 X 服务器。

- Windows：小部件需要设置 Qt::FramelessWindowHint 窗口标志才能使半透明效果发挥作用。

- macOS：小部件需要设置 Qt::FramelessWindowHint 窗口标志才能使半透明效果发挥作用。


## Native Widgets vs Alien Widgets

外来窗口小部件是窗口系统未知的小部件。它们没有与之关联的本机窗口句柄。此功能可显著加快窗口小部件绘制、调整大小的速度，并消除闪烁。

如果您需要本机窗口的旧行为，请选择以下选项之一：

1. 在您的环境中使用 QT_USE_NATIVE_WINDOWS=1。

2. 在您的应用程序上设置 Qt::AA_NativeWindows 属性。所有窗口小部件都将是本机窗口小部件。

3. 在窗口小部件上设置 Qt::WA_NativeWindow 属性：窗口小部件本身及其所有祖先都将成为本机窗口小部件（除非设置了 Qt::WA_DontCreateNativeAncestors）。

4. 调用 winId 以强制使用本机窗口（这意味着 3）。

5. 设置 Qt::WA_PaintOnScreen 属性以强制使用本机窗口（这意味着 3）。


--------------------------------
## class RenderFlag

（继承 enum.Flag）此枚举描述了在调用 render() 时如何渲染小部件。

| Constant                     | Description |
| ---------------------------- | ----------- |
| QWidget.DrawWindowBackground | 如果启用此选项，即使未设置 autoFillBackground，小部件的背景也会呈现到目标中。默认情况下，此选项处于启用状态。 |
| QWidget.DrawChildren         | 如果启用此选项，则小部件的子项将递归渲染到目标中。默认情况下，此选项处于启用状态。 |
| QWidget.IgnoreMask           | 如果启用此选项，则在渲染到目标时会忽略小部件的 mask()。默认情况下，此选项处于禁用状态。 |


--------------------------------
## property acceptDrops : bool

此属性保存是否为该小部件启用了放置事件。

将此属性设置为 true 会向系统宣布该小部件可能能够接受放置事件。

如果小部件是桌面 (windowType() == Qt::Desktop)，则当其他应用程序正在使用桌面时，此操作可能会失败；您可以调用 acceptDrops() 来测试是否发生这种情况。

默认情况下，此属性为 false。

访问函数：

- acceptDrops()
- setAcceptDrops()


--------------------------------
## property accessibleDescription : str

此属性保存辅助技术所看到的窗口小部件的描述。

窗口小部件的可访问描述应传达窗口小部件的功能。虽然 accessibleName 应该是简短而简洁的字符串（例如 Save），但描述应提供更多上下文，例如 Saves the current document。

此属性必须本地化。

默认情况下，此属性包含一个空字符串，Qt 将使用工具提示来提供此信息。

访问函数：

- accessibleDescription()
- setAccessibleDescription()


--------------------------------
## property accessibleName : str

此属性保存辅助技术所见的小部件名称。

这是辅助技术（如屏幕阅读器）宣布此小部件的主要名称。 对于大多数小部件，无需设置此属性。 例如，对于 QPushButton，将使用按钮的文本。

当小部件不提供任何文本时，设置此属性很重要。 例如，仅包含图标的按钮需要设置此属性才能与屏幕阅读器配合使用。 名称应简短且等同于小部件传达的视觉信息。

此属性必须本地化。

默认情况下，此属性包含一个空字符串。

访问函数：

- accessibleName()
- setAccessibleName()


--------------------------------
## property autoFillBackground : bool

此属性保存小部件背景是否自动填充。

如果启用，此属性将导致 Qt 在调用绘制事件之前填充小部件的背景。使用的颜色由小部件调色板中的 QPalette::Window 颜色角色定义。

此外，除非设置了 WA_OpaquePaintEvent 或 WA_NoSystemBackground 属性，否则窗口始终由 QPalette::Window 填充。

如果小部件的父级背景为静态渐变，则无法关闭此属性（即设置为 false）。

默认情况下，此属性为 false。

访问函数：

- autoFillBackground()
- setAutoFillBackground()


--------------------------------
## property baseSize : QSize

此属性保存小部件的基本大小。

如果小部件定义了 sizeIncrement() ，则使用基本大小来计算适当的小部件大小。

默认情况下，对于新创建的小部件，此属性包含宽度和高度为零的尺寸。

访问函数：

- baseSize()
- setBaseSize()


--------------------------------
## property childrenRect : QRect

此属性保存小部件子项的边界矩形。

隐藏的子项被排除在外。

默认情况下，对于没有子项的小部件，此属性包含位于原点的宽度和高度为零的矩形。

访问函数：

- childrenRect()


--------------------------------
## property childrenRegion : QRegion

此属性保存小部件子项所占据的组合区域。

隐藏的子项被排除在外。

默认情况下，对于没有子项的小部件，此属性包含一个空区域。

访问函数：

- childrenRegion()


--------------------------------
## property contextMenuPolicy : Qt.ContextMenuPolicy

此属性保存小部件如何显示上下文菜单。

此属性的默认值为 Qt::DefaultContextMenu，这意味着将调用 contextMenuEvent() 处理程序。其他值包括 Qt::NoContextMenu、Qt::PreventContextMenu、Qt::ActionsContextMenu 和 Qt::CustomContextMenu。使用 Qt::CustomContextMenu 时，将发出信号 customContextMenuRequested()。

访问函数：

- contextMenuPolicy()
- setContextMenuPolicy()


--------------------------------
## property cursor : QCursor

此属性保存此小部件的光标形状。

当鼠标光标位于此小部件上方时，它将呈现此形状。请参阅预定义光标对象列表，了解一系列有用的形状。

编辑器小部件可能使用 I 型光标：

```python
setCursor(Qt.IBeamCursor)
```

如果未设置光标，或者在调用 unsetCursor() 后，则使用父级光标。

默认情况下，此属性包含具有 Qt::ArrowCursor 形状的光标。

某些底层窗口实现会在光标离开窗口小部件时重置光标，即使鼠标被抓取也是如此。如果您想为所有窗口小部件设置光标，即使在窗口外，也可以考虑使用 QGuiApplication::setOverrideCursor()。

访问函数：

- cursor()
- setCursor()
- unsetCursor()


--------------------------------
## property enabled : bool

此属性保存窗口小部件是否已启用。

通常，已启用的窗口小部件会处理键盘和鼠标事件；已禁用的窗口小部件则不会。QAbstractButton 是个例外。

某些窗口小部件在被禁用时会以不同的方式显示自身。例如，按钮可能会将其标签绘制为灰色。如果您的窗口小部件需要知道它何时被启用或禁用，您可以使用类型为 QEvent::EnabledChange 的 changeEvent()。

禁用窗口小部件会隐式禁用其所有子窗口小部件。分别启用会启用所有子窗口小部件，除非它们已被明确禁用。当其父窗口小部件保持禁用状态时，不可能明确启用非窗口的子窗口小部件。

默认情况下，此属性为 true。

访问函数：

- isEnabled()
- setEnabled()


--------------------------------
## property focus : bool

此属性保存此小部件（或其焦点代理）是否具有键盘输入焦点。

默认情况下，此属性为 false。

访问函数：

- hasFocus()


--------------------------------
## property focusPolicy : Qt.FocusPolicy

此属性保存小部件接受键盘焦点的方式。

如果小部件通过 Tab 键接受键盘焦点，则策略为 Qt::TabFocus；如果小部件通过单击接受焦点，则策略为 Qt::ClickFocus；如果小部件同时接受这两种方式，则策略为 Qt::StrongFocus；如果小部件根本不接受焦点，则策略为 Qt::NoFocus（默认值）。

如果小部件处理键盘事件，则必须为其启用键盘焦点。这通常是从小部件的构造函数中完成的。例如，QLineEdit 构造函数调用 setFocusPolicy(Qt::StrongFocus)。

如果小部件具有焦点代理，则焦点策略将传播给它。

访问函数：

- focusPolicy()
- setFocusPolicy()


--------------------------------
## property font : QFont

此属性保存当前为窗口小部件设置的字体。

此属性描述窗口小部件请求的字体。在呈现标准组件时，窗口小部件的样式会使用该字体，并且该字体可用作确保自定义窗口小部件能够与本机平台的外观保持一致性的一种手段。不同的平台或不同的样式通常会为应用程序定义不同的字体。

当您为窗口小部件分配新字体时，此字体的属性将与窗口小部件的默认字体组合以形成窗口小部件的最终字体。您可以调用 fontInfo() 来获取窗口小部件最终字体的副本。最终字体还用于初始化 QPainter 的字体。

默认值取决于系统环境。QApplication 维护一个系统/主题字体，该字体用作所有窗口小部件的默认字体。某些类型的窗口小部件可能还有特殊的字体默认值。您还可以通过将自定义字体和窗口小部件的名称传递给 setFont() 来自己定义窗口小部件的默认字体。最后，将字体与 Qt 的字体数据库进行匹配，以找到最佳匹配。

QWidget 将显式字体属性从父级传播到子级。如果您更改字体上的特定属性并将该字体分配给小部件，则该属性将传播到小部件的所有子级，覆盖该属性的任何系统默认值。请注意，除非启用了 Qt::WA_WindowPropagation 属性，否则默认情况下字体不会传播到窗口（请参阅 isWindow()）。

QWidget 的字体传播类似于其调色板传播。

当前样式用于呈现所有标准 Qt 小部件的内容，可以自由选择使用小部件字体，或者在某些情况下忽略它（部分或完全）。特别是，某些样式（如 GTK 样式、Mac 样式和 Windows Vista 样式）会对小部件字体应用特殊修改以匹配平台的本机外观。因此，将属性分配给小部件的字体并不能保证会改变小部件的外观。相反，您可以选择应用 styleSheet 。

访问函数：

- font()
- setFont()


--------------------------------
## property frameGeometry : QRect

此属性保存小部件相对于其父级（包括任何窗口框架）的几何形状。

有关窗口几何问题的概述，请参阅窗口几何文档。

默认情况下，此属性包含一个取决于用户平台和屏幕几何形状的值。

访问函数：

- frameGeometry()


--------------------------------
## property frameSize : QSize

此属性保存小部件（包括任何窗口框架）的大小。

默认情况下，此属性包含一个取决于用户平台和屏幕几何形状的值。

访问函数：

- frameSize()


--------------------------------
## property fullScreen : bool

此属性保存小部件是否以全屏模式显示。

全屏模式下的小部件占据整个屏幕区域，不显示窗口装饰，例如标题栏。

默认情况下，此属性为 false。

访问函数：

- isFullScreen()


--------------------------------
## property geometry : QRect

此属性保存小部件相对于其父级（不包括窗口框架）的几何形状。

更改几何形状时，小部件（如果可见）会立即接收移动事件 ( moveEvent() ) 和/或调整大小事件 ( resizeEvent() )。 如果小部件当前不可见，则保证在显示之前接收适当的事件。

如果尺寸组件超出由 minimumSize() 和 maximumSize() 定义的范围，则会调整尺寸组件。

有关窗口几何问题的概述，请参阅窗口几何文档。

默认情况下，此属性包含一个取决于用户平台和屏幕几何形状的值。

访问函数：

- geometry()
- setGeometry()


--------------------------------
## property height : int

此属性保存小部件的高度（不包括任何窗口框架）。

有关窗口几何问题的概述，请参阅窗口几何文档。

默认情况下，此属性包含一个取决于用户平台和屏幕几何的值。

访问函数：


--------------------------------
## property inputMethodHints : Combination of Qt.InputMethodHint

此属性保存小部件具有哪些输入法特定提示。

这仅与输入小部件相关。输入法使用它来检索有关输入法应如何操作的提示。例如，如果设置了 Qt::ImhFormattedNumbersOnly 标志，输入法可能会更改其视觉组件以反映只能输入数字。


--------------------------------
## The default value is Qt::ImhNone.

访问函数：

- inputMethodHints()
- setInputMethodHints()


--------------------------------
## property isActiveWindow : bool

此属性保存此小部件的窗口是否为活动窗口。

活动窗口是包含具有键盘焦点的小部件的窗口（如果窗口没有小部件或其小部件均不接受键盘焦点，则窗口可能仍具有焦点）。

当弹出窗口可见时，此属性对于活动窗口和弹出窗口均为 true。

默认情况下，此属性为 false。

访问函数：

- isActiveWindow()


--------------------------------
## property layoutDirection : Qt.LayoutDirection

此属性保存此小部件的布局方向。

默认情况下，此属性设置为 Qt::LeftToRight。

当在小部件上设置布局方向时，它将传播到小部件的子项，但不会传播到窗口子项，也不会传播到已明确调用 setLayoutDirection() 的子项。此外，在为父项调用 setLayoutDirection() 之后添加的子小部件不会继承父项的布局方向。

访问函数：

- layoutDirection()
- setLayoutDirection()
- unsetLayoutDirection()


--------------------------------
## property locale : QLocale

此属性保存小部件的语言环境。

只要未设置特殊语言环境，则此属性要么是父级语言环境，要么是默认语言环境（如果此小部件是顶级小部件）。

如果小部件显示日期或数字，则应使用小部件的语言环境进行格式化。

访问函数：

- locale()
- setLocale()
- unsetLocale()


--------------------------------
## property maximized : bool

此属性保存此小部件是否最大化。

此属性仅与窗口相关。

默认情况下，此属性为 false。

访问函数：

- isMaximized()


--------------------------------
## property maximumHeight : int

此属性保存小部件的最大高度（以像素为单位）。

此属性对应于 maximumSize 属性所保存的高度。

默认情况下，此属性包含值 16777215。

访问函数：

- maximumHeight()
- setMaximumHeight()


--------------------------------
## property maximumSize : QSize

此属性保存小部件的最大尺寸（以像素为单位）。

小部件不能调整为大于最大小部件尺寸。

默认情况下，此属性包含一个宽度和高度均为 16777215 的尺寸。

访问函数：

- maximumSize()
- setMaximumSize()


--------------------------------
## property maximumWidth : int

此属性保存小部件的最大宽度（以像素为单位）。

此属性对应于 maximumSize 属性所保存的宽度。

默认情况下，此属性包含值 16777215。

访问函数：

- maximumWidth()
- setMaximumWidth()


--------------------------------
## property minimized : bool

此属性保存此小部件是否最小化（图标化）。

此属性仅适用于窗口。

默认情况下，此属性为 false。

访问函数：

- isMinimized()


--------------------------------
## property minimumHeight : int

此属性保存小部件的最小高度（以像素为单位）。

此属性对应于 minimumSize 属性所保存的高度。

默认情况下，此属性的值为 0。

访问函数：

- minimumHeight()
- setMinimumHeight()


--------------------------------
## property minimumSize : QSize

此属性保存小部件的最小尺寸。

小部件不能调整为小于最小小部件尺寸。 如果当前尺寸小于最小小部件尺寸，则小部件的尺寸将强制为最小尺寸。

此函数设置的最小尺寸将覆盖 QLayout 定义的最小尺寸。 要取消设置最小尺寸，请使用 QSize(0, 0) 值。

默认情况下，此属性包含宽度和高度为零的尺寸。

访问函数：

- minimumSize()
- setMinimumSize()


--------------------------------
## property minimumSizeHint : QSize

此属性保存小部件的建议最小尺寸。

如果此属性的值为无效尺寸，则不建议使用最小尺寸。

如果此小部件没有布局，则 minimumSizeHint() 的默认实现将返回无效尺寸，否则将返回布局的最小尺寸。 大多数内置小部件都会重新实现 minimumSizeHint()。

除非设置了 minimumSize() 或将尺寸策略设置为 QSizePolicy::Ignore，否则 QLayout 永远不会将小部件调整为小于最小尺寸提示的尺寸。 如果设置了 minimumSize()，则将忽略最小尺寸提示。

访问函数：

- minimumSizeHint()


--------------------------------
## property minimumWidth : int

此属性保存小部件的最小宽度（以像素为单位）。

此属性对应于 minimumSize 属性所保存的宽度。

默认情况下，此属性的值为 0。

访问函数：

- minimumWidth()
- setMinimumWidth()


--------------------------------
## property modal : bool

此属性保存小部件是否为模态小部件。

此属性仅适用于窗口。模态小部件会阻止所有其他窗口中的小部件获取任何输入。

默认情况下，此属性为 false。

访问函数：

- isModal()


--------------------------------
## property mouseTracking : bool

此属性保存是否为小部件启用鼠标跟踪。

如果禁用鼠标跟踪（默认），则小部件仅在鼠标移动期间按下至少一个鼠标按钮时接收鼠标移动事件。

如果启用鼠标跟踪，则即使未按下任何按钮，小部件也会接收鼠标移动事件。

访问函数：

- hasMouseTracking()
- setMouseTracking()


--------------------------------
## property normalGeometry : QRect

此属性保存小部件的几何形状，当其显示为正常（非最大化或全屏）顶层小部件时，它将出现。

如果小部件已处于此状态，则正常几何形状将反映小部件的当前 geometry() 。

对于子小部件，此属性始终保存一个空矩形。

默认情况下，此属性包含一个空矩形。

访问函数：

- normalGeometry()


--------------------------------
## property palette : QPalette

此属性保存小部件的调色板。

此属性描述小部件的调色板。调色板由小部件的样式在呈现标准组件时使用，并可用作确保自定义小部件能够与本机平台的外观保持一致性的一种手段。不同的平台或不同的样式通常具有不同的调色板。

当您为小部件分配新调色板时，此调色板中的颜色角色将与小部件的默认调色板组合以形成小部件的最终调色板。小部件背景角色的调色板条目用于填充小部件的背景（请参阅 autoFillBackground ），而前台角色初始化 QPainter 的画笔。

默认值取决于系统环境。QApplication 维护一个系统/主题调色板，作为所有小部件的默认值。某些类型的小部件可能还有特殊的调色板默认值（例如，在 Windows Vista 上，从 QMenuBar 派生的所有类都有一个特殊的默认调色板）。您还可以通过将自定义调色板和小部件的名称传递给 setPalette() 来自己定义小部件的默认调色板。最后，样式始终可以选择在分配调色板时对其进行润色（请参阅 polish()）。

QWidget 将显式调色板角色从父级传播到子级。如果您将画笔或颜色分配给调色板上的特定角色，并将该调色板分配给小部件，则该角色将传播到小部件的所有子级，覆盖该角色的任何系统默认值。请注意，除非启用了 Qt::WA_WindowPropagation 属性，否则调色板默认情况下不会传播到窗口（请参阅 isWindow()）。

QWidget 的调色板传播与其字体传播类似。

当前样式用于呈现所有标准 Qt 小部件的内容，可以自由选择小部件调色板中的颜色和画笔，或者在某些情况下忽略调色板（部分或完全）。具体来说，某些样式（如 GTK 样式、Mac 样式和 Windows Vista 样式）依赖于第三方 API 来呈现小部件的内容，而这些样式通常不遵循调色板。因此，将角色分配给小部件的调色板并不能保证改变小部件的外观。相反，您可以选择应用 styleSheet 。

访问函数：

- palette()
- setPalette()


--------------------------------
## property pos : QPoint

此属性保存小部件在其父小部件中的位置。

如果小部件是窗口，则位置是小部件在桌面上的位置，包括其框架。

更改位置时，如果小部件可见，则立即接收移动事件 ( moveEvent() )。 如果小部件当前不可见，则保证在显示之前收到事件。

默认情况下，此属性包含引用原点的位置。

有关窗口几何问题的概述，请参阅窗口几何文档。

访问函数：

- pos()
- move()


--------------------------------
## property rect : QRect

此属性保存小部件的内部几何形状（不包括任何窗口框架）。

rect 属性等于 QRect(0, 0, width() , height() )。

有关窗口几何问题的概述，请参阅窗口几何文档。

默认情况下，此属性包含一个取决于用户平台和屏幕几何形状的值。

访问函数：

- rect()


--------------------------------
## property size : QSize

此属性保存小部件的尺寸（不包括任何窗口框架）。

如果小部件在调整大小时可见，它会立即收到调整大小事件 ( resizeEvent() )。 如果小部件当前不可见，则保证在显示之前收到事件。

如果尺寸超出由 minimumSize() 和 maximumSize() 定义的范围，则会调整尺寸。

默认情况下，此属性包含一个取决于用户平台和屏幕几何形状的值。

访问函数：

- size()
- resize()


--------------------------------
## property sizeHint : QSize

此属性保存小部件的推荐尺寸。

如果此属性的值为无效尺寸，则不推荐任何尺寸。

如果此小部件没有布局，sizeHint() 的默认实现将返回无效尺寸，否则将返回布局的首选尺寸。

访问函数：

- sizeHint()


--------------------------------
## property sizeIncrement : QSize

此属性保存小部件的尺寸增量。

当用户调整窗口大小时，尺寸将以 sizeIncrement(). width() 像素为水平方向移动，sizeIncrement. height() 像素为垂直方向移动，以 baseSize() 为基础。首选的小部件尺寸为非负整数 i 和 j：

width = baseSize().width() + i * sizeIncrement().width()
height = baseSize().height() + j * sizeIncrement().height()
请注意，虽然您可以为所有小部件设置尺寸增量，但它仅影响窗口。

默认情况下，此属性包含宽度和高度为零的尺寸。

访问函数：

- sizeIncrement()
- setSizeIncrement()


--------------------------------
## property sizePolicy : QSizePolicy

此属性保存窗口小部件的默认布局行为。

如果存在管理此窗口小部件的子项的 QLayout ，则使用该布局指定的大小策略。如果没有这样的 QLayout ，则使用此函数的结果。

默认策略是 Preferred/Preferred，这意味着窗口小部件可以自由调整大小，但最好是 sizeHint() 返回的大小。按钮类窗口小部件设置大小策略以指定它们可以水平拉伸，但垂直固定。这同样适用于行编辑控件（例如 QLineEdit 、 QSpinBox 或可编辑的 QComboBox ）和其他水平方向的窗口小部件（例如 QProgressBar ）。 QToolButton 通常是正方形的，因此它们允许在两个方向上增长。支持不同方向的窗口小部件（例如 QSlider 、 QScrollBar 或 QHeader）仅指定在相应方向上拉伸。可以提供滚动条的小部件（通常是 QScrollArea 的子类）倾向于指定它们可以使用额外的空间，并且它们可以使用小于 sizeHint() 的空间。

访问函数：

- sizePolicy()
- setSizePolicy()


--------------------------------
## property statusTip : str

此属性保存小部件的状态提示。

默认情况下，此属性包含一个空字符串。

访问函数：

- statusTip()
- setStatusTip()


--------------------------------
## property styleSheet : str

此属性保存小部件的样式表。

样式表包含对小部件样式的自定义的文本描述，如 Qt 样式表文档中所述。

自 Qt 4.5 起，Qt 样式表完全支持 macOS。

访问函数：

- styleSheet()
- setStyleSheet()


--------------------------------
## property tabletTracking : bool

此属性用于保存小部件是否启用平板电脑跟踪。

如果禁用平板电脑跟踪（默认），则小部件仅在触控笔与平板电脑接触时接收平板电脑移动事件，或者在触控笔移动时按下至少一个触控笔按钮。

如果启用平板电脑跟踪，则小部件即使在附近悬停时也会接收平板电脑移动事件。这对于监控位置以及辅助属性（例如旋转和倾斜）以及在 UI 中提供反馈非常有用。

访问函数：

- hasTabletTracking()
- setTabletTracking()


--------------------------------
## property toolTip : str

此属性保存小部件的工具提示。

请注意，默认情况下，工具提示仅显示活动窗口的子窗口小部件。您可以通过在窗口上设置属性 Qt::WA_AlwaysShowToolTips 来更改此行为，而不是在带有工具提示的小部件上设置。

如果您想控制工具提示的行为，您可以拦截 event() 函数并捕获 QEvent::ToolTip 事件（例如，如果您想自定义应显示工具提示的区域）。

默认情况下，此属性包含一个空字符串。

访问函数：

- toolTip()
- setToolTip()


--------------------------------
## property toolTipDuration : int

此属性保存小部件的工具提示持续时间。

指定工具提示的显示时间（以毫秒为单位）。如果值为 -1（默认值），则持续时间将根据工具提示的长度计算。

访问函数：

- toolTipDuration()
- setToolTipDuration()


--------------------------------
## property updatesEnabled : bool

此属性保存是否启用更新。

启用更新的小部件接收绘制事件并具有系统背景；禁用的小部件则没有。这也意味着如果禁用更新，则调用 update() 和 repaint() 无效。

默认情况下，此属性为 true。

setUpdatesEnabled() 通常用于短时间禁用更新，例如避免在发生较大变化时屏幕闪烁。在 Qt 中，小部件通常不会产生屏幕闪烁，但在 X11 上，当小部件被隐藏时，服务器可能会擦除屏幕上的区域，然后才能用其他小部件替换它们。禁用更新可以解决这个问题。

示例：

```bash
setUpdatesEnabled(False)
bigVisualChanges()
setUpdatesEnabled(True)
```

禁用小部件会隐式禁用其所有子部件。启用小部件会启用除顶级小部件或已明确禁用的小部件之外的所有子部件。重新启用更新会隐式调用小部件上的 update()。

访问函数：

- updatesEnabled()
- setUpdatesEnabled()


--------------------------------
## property visible : bool

此属性保存小部件是否可见。

如果小部件的所有父小部件（直至窗口）都可见，则调用 setVisible(true) 或 show() 会将小部件设置为可见状态。如果祖先不可见，则小部件将在其所有祖先都显示之前变为可见。如果其大小或位置已更改，Qt 会保证小部件在显示之前获得移动和调整大小事件。如果小部件尚未调整大小，Qt 将使用 adjustSize() 将小部件的大小调整为有用的默认值。

调用 setVisible(false) 或 hide() 会明确隐藏小部件。明确隐藏的小部件永远不会变为可见，即使其所有祖先都变为可见，除非您显示它。

当小部件的可见性状态发生变化时，它会接收显示和隐藏事件。在隐藏和显示事件之间，无需浪费 CPU 周期来准备或向用户显示信息。例如，视频应用程序可能只是停止生成新帧。

恰巧被屏幕上的其他窗口遮挡的小部件被视为可见。这同样适用于图标化窗口和存在于另一个虚拟桌面上的窗口（在支持此概念的平台上）。当窗口系统更改窗口小部件的映射状态时，窗口小部件会收到自发显示和隐藏事件，例如，当用户最小化窗口时会收到自发隐藏事件，而当窗口再次恢复时会收到自发显示事件。

您很少需要重新实现 setVisible() 函数。如果您需要在显示窗口小部件之前更改某些设置，请改用 showEvent()。如果您需要进行一些延迟初始化，请使用传递给 event() 函数的 Polish 事件。

访问函数：

- isVisible()
- setVisible()


--------------------------------
## property whatsThis : str

此属性保存小部件的“这是什么”帮助文本。

默认情况下，此属性包含一个空字符串。

访问函数：

- whatsThis()
- setWhatsThis()


--------------------------------
## property width : int

此属性保存小部件的宽度（不包括任何窗口框架）。

有关窗口几何问题的概述，请参阅窗口几何文档。

默认情况下，此属性包含一个取决于用户平台和屏幕几何的值。

访问函数：


--------------------------------
## property windowFilePath : str

此属性保存与小部件关联的文件路径。

此属性仅对窗口有意义。它将文件路径与窗口关联。如果您设置了文件路径，但未设置窗口标题，Qt 会将窗口标题设置为使用 QFileInfo::fileName() 获得的指定路径的文件名。

如果在任何时候设置了窗口标题，则窗口标题优先，并将显示而不是文件路径字符串。

此外，在 macOS 上，这还有一个额外的好处，即它为窗口设置代理图标，假设文件路径存在。

如果未设置文件路径，则此属性包含一个空字符串。

默认情况下，此属性包含一个空字符串。

访问函数：

- windowFilePath()
- setWindowFilePath()


--------------------------------
## property windowIcon : QIcon

此属性保存小部件的图标。

此属性仅对窗口有意义。如果未设置图标，window Icon() 将返回应用程序图标 (QApplication::window Icon())。

访问函数：

- windowIcon()
- setWindowIcon()
- Signal windowIconChanged()


--------------------------------
## property windowIconText : str

此属性保存要显示在最小化窗口图标上的文本。

此属性仅对窗口有意义。如果未设置图标文本，此访问器将返回一个空字符串。它仅在 X11 平台上实现，并且只有某些窗口管理器使用此窗口属性。

此属性已弃用。

访问函数：

- windowIconText()
- setWindowIconText()
- Signal windowIconTextChanged()


--------------------------------
## property windowModality : Qt.WindowModality

此属性保存哪些窗口被模式窗口小部件阻挡。

此属性仅对窗口有意义。模式窗口小部件阻止其他窗口中的窗口小部件获取输入。此属性的值控制当窗口小部件可见时哪些窗口被阻挡。在窗口可见时更改此属性无效；您必须先隐藏（）窗口小部件，然后再次显示（）。

默认情况下，此属性为 Qt::NonModal。

访问函数：

- windowModality()
- setWindowModality()


--------------------------------
## property windowModified : bool

此属性保存窗口中显示的文档是否有未保存的更改。

已修改窗口是指内容已更改但尚未保存到磁盘的窗口。此标志将根据平台的不同产生不同的效果。在 macOS 上，关闭按钮将具有已修改的外观；在其他平台上，窗口标题将带有“*”（星号）。

窗口标题必须包含“[*]”占位符，表示“*”应出现的位置。通常，它应出现在文件名之后（例如，“document1.txt[*] - 文本编辑器”）。如果窗口未修改，则仅删除占位符。

请注意，如果将小部件设置为已修改，则其所有祖先也将被设置为已修改。但是，如果您在小部件上调用 setWindowModified(false)，则这不会传播到其父级，因为父级的其他子级可能已被修改。

访问函数：

- isWindowModified()
- setWindowModified()


--------------------------------
## property windowOpacity : float

此属性保存窗口的不透明度级别。

不透明度的有效范围是从 1.0（完全不透明）到 0.0（完全透明）。

默认情况下，此属性的值为 1.0。

此功能在支持 Composite 扩展的嵌入式 Linux、macOS、Windows 和 X11 平台上可用。

访问函数：

- windowOpacity()
- setWindowOpacity()


--------------------------------
## property windowTitle : str

此属性保存窗口标题 (caption)。

此属性仅对顶级小部件（如窗口和对话框）有意义。如果未设置标题，则标题基于 windowFilePath 。如果两者都未设置，则标题为空字符串。

如果您使用 windowModified 机制，则窗口标题必须包含“[*]”占位符，指示“*”应出现的位置。通常，它应出现在文件名之后（例如，“document1.txt[*] - 文本编辑器”）。如果 windowModified 属性为 false（默认值），则将删除占位符。

在某些桌面平台（包括 Windows 和 Unix）上，如果设置了应用程序名称（来自 QGuiApplication::applicationDisplayName），则会将其添加到窗口标题的末尾。这是由 QPA 插件完成的，因此它会显示给用户，但不是 windowTitle 字符串的一部分。

访问函数：

- windowTitle()
- setWindowTitle()
- Signal windowTitleChanged()


--------------------------------
## property x : int

此属性保存小部件相对于其父级（包括任何窗口框架）的 x 坐标。

有关窗口几何问题的概述，请参阅窗口几何文档。

默认情况下，此属性的值为 0。

访问函数：

- x()


--------------------------------
## property y : int

此属性保存小部件相对于其父级（包括任何窗口框架）的 y 坐标。

有关窗口几何问题的概述，请参阅窗口几何文档。

默认情况下，此属性的值为 0。

访问函数：

- y()


--------------------------------
## __init__([parent=None[, f=Qt.WindowFlags()]])

参数：

- parent – QWidget
- f – Combination of WindowType

构造一个窗口小部件，它是父窗口小部件的子窗口小部件，窗口小部件标志设置为 f。

如果父窗口小部件为 None，则新窗口小部件将变成一个窗口。 如果父窗口小部件是另一个窗口小部件，则此窗口小部件将变成父窗口小部件内的子窗口。 当父窗口小部件被删除时，新窗口小部件也会被删除。

窗口小部件标志参数 f 通常为 0，但可以将其设置为自定义窗口的框架（即父窗口小部件必须为 None）。 要自定义框架，请使用由任何窗口标志的按位或组成的值。

如果将子窗口小部件添加到已经可见的窗口小部件，则必须明确显示子窗口小部件以使其可见。

请注意，Qt 的 X11 版本可能无法在所有系统上提供所有样式标志组合。 这是因为在 X11 上，Qt 只能询问窗口管理器，而窗口管理器可以覆盖应用程序的设置。 在 Windows 上，Qt 可以设置您想要的任何标志。


--------------------------------
## acceptDrops()

返回类型：bool

属性 acceptDrops 的获取器。


--------------------------------
## accessibleDescription()

返回类型：str

属性 accessibleDescription 的获取器。


--------------------------------
## accessibleName()

返回类型：str

属性 accessibleName 的获取器。


--------------------------------
## actionEvent(event)

参数：

- event – QActionEvent

每当小部件的操作发生变化时，就会使用给定的事件调用此事件处理程序。


--------------------------------
## actions()

返回类型：list of QAction

返回此小部件的操作列表（可能为空）。


--------------------------------
## activateWindow()

将包含此小部件的顶级小部件设置为活动窗口。

活动窗口是具有键盘输入焦点的可见顶级窗口。

此函数执行的操作与在顶级窗口的标题栏上单击鼠标相同。在 X11 上，结果取决于窗口管理器。如果您想确保窗口也堆叠在顶部，您还应该调用 raise() 。请注意，窗口必须可见，否则 activateWindow() 无效。

在 Windows 上，如果您在应用程序当前不是活动应用程序时调用此函数，则不会使其成为活动窗口。它将更改任务栏条目的颜色以指示窗口已发生某种变化。这是因为 Microsoft 不允许应用程序中断用户当前在另一个应用程序中执行的操作。


--------------------------------
## addAction(icon, text, receiver, member[, type=Qt.AutoConnection])

参数：

- icon – QIcon
- text – str
- receiver – QObject
- member – str
- type – ConnectionType

返回类型：QAction


--------------------------------
## addAction(text, receiver, member[, type=Qt.AutoConnection])

参数：

- text – str
- receiver – QObject
- member – str
- type – ConnectionType

返回类型：QAction


--------------------------------
## addAction(text, shortcut, receiver, member[, type=Qt.AutoConnection])

参数：

- text – str
- shortcut – QKeySequence
- receiver – QObject
- member – str
- type – ConnectionType

返回类型：QAction


--------------------------------
## addAction(text, shortcut)

参数：

- text – str
- shortcut – QKeySequence

返回类型：QAction


--------------------------------
## addAction(text)

参数：

- text – str

返回类型：QAction


--------------------------------
## addAction(icon, text, shortcut, receiver, member[, type=Qt.AutoConnection])

参数：

- icon – QIcon
- text – str
- shortcut – QKeySequence
- receiver – QObject
- member – str
- type – ConnectionType

返回类型：QAction


--------------------------------
## addAction(icon, text, shortcut)

参数：

- icon – QIcon
- text – str
- shortcut – QKeySequence

返回类型：QAction


--------------------------------
## addAction(icon, text)

参数：

- icon – QIcon
- text – str

返回类型：QAction


--------------------------------
## addAction(text, shortcut, callable)

参数：

- text – str
- shortcut – QKeySequence
- callable – object

返回类型：QAction


--------------------------------
## addAction(text, callable)

参数：

- text – str
- callable – object

返回类型：QAction


--------------------------------
## addAction(icon, text, shortcut, callable)

参数：

- icon – QIcon
- text – str
- shortcut – QKeySequence
- callable – object

返回类型：QAction


--------------------------------
## addAction(icon, text, callable)

参数：

- icon – QIcon
- text – str
- callable – object

返回类型：QAction


--------------------------------
## addAction(action)

参数：

- action – QAction

将操作 action 附加到此小部件的操作列表中。

所有 QWidget 都有一个 QActions 列表。但是，它们可以以多种不同的方式以图形方式表示。QAction 列表（由actions()返回）的默认用途是创建上下文 QMenu。

QWidget 应该只具有每个操作中的一个，并且添加它已经具有的操作不会导致相同的操作在小部件中出现两次。

操作的所有权不会转移到此 QWidget。


--------------------------------
## addActions(actions)

参数：

- actions – list of QAction

将操作附加到此小部件的操作列表中。


--------------------------------
## adjustSize()

调整小部件的大小以适合其内容。

如果有效，即大小提示的宽度和高度 >= 0，则此函数使用 sizeHint()。否则，它将大小设置为覆盖所有子小部件的子矩形（所有子小部件矩形的并集）。

对于窗口，还会考虑屏幕尺寸。如果 sizeHint() 小于 (200, 100) 且尺寸策略为扩展，则窗口将至少为 (200, 100)。窗口的最大尺寸是屏幕宽度和高度的 2/3。


--------------------------------
## autoFillBackground()

返回类型：bool

属性 autoFillBackground 的获取器。


--------------------------------
## backgroundRole()

返回类型：ColorRole

返回小部件的背景角色。

背景角色定义小部件调色板中用于渲染背景的画笔。

如果未设置明确的背景角色，则小部件将继承其父小部件的背景角色。


--------------------------------
## backingStore()

返回类型：QBackingStore

返回此小部件将被绘制到的 QBackingStore。


--------------------------------
## baseSize()

返回类型：QSize

属性 baseSize 的获取器。


--------------------------------
## changeEvent(event)

参数：

- event – QEvent

可以重新实现此事件处理程序来处理状态更改。

可以通过提供的事件检索此事件中更改的状态。

变更事件包括：QEvent::ToolBarChange, QEvent::ActivationChange, QEvent::EnabledChange, QEvent::FontChange, QEvent::StyleChange, QEvent::PaletteChange, QEvent::WindowTitleChange, QEvent::IconTextChange, QEvent::ModifiedChange, QEvent::MouseTrackingChange, QEvent::ParentChange, QEvent::WindowStateChange, QEvent::LanguageChange, QEvent::LocaleChange, QEvent::LayoutDirectionChange, QEvent::ReadOnlyChange.


--------------------------------
## childAt(p)

参数：

- p – QPoint

返回类型：QWidget

这是一个重载函数。

返回小部件自身坐标系中点 p 处的可见子小部件。


--------------------------------
## childAt(x, y)

参数：

- x – int
- y – int

返回类型：QWidget

返回窗口小部件坐标系中位置 (x, y) 处的可见子窗口小部件。如果指定位置处没有可见子窗口小部件，则该函数返回 None。


--------------------------------
## childrenRect()

返回类型：QRect

属性 childrenRect 的获取器。


--------------------------------
## childrenRegion()

返回类型：QRegion

属性 childrenRegion 的获取方法。


--------------------------------
## clearFocus()

从小部件获取键盘输入焦点。

如果小部件具有活动焦点，则会向此小部件发送焦点消失事件，以告知它已失去焦点。

此小部件必须启用焦点设置才能获取键盘输入焦点；也就是说，它必须调用 setFocusPolicy() 。


--------------------------------
## clearMask()

删除由 setMask() 设置的所有掩码。


--------------------------------
## close()

返回类型：bool

关闭此小部件。如果小部件已关闭，则返回 true；否则返回 false。

首先，它向小部件发送 QCloseEvent。如果小部件接受关闭事件，则隐藏小部件。如果忽略该事件，则不会发生任何事情。closeEvent() 的默认实现接受关闭事件。

如果小部件具有 Qt::WA_DeleteOnClose 标志，则小部件也会被删除。无论小部件是否可见，都会向小部件传递关闭事件。

当设置了 Qt::WA_QuitOnClose 属性的最后一个可见主窗口（即没有父窗口的窗口）关闭时，会发出 QGuiApplication::lastWindowClosed() 信号。默认情况下，此属性适用于除启动画面、工具窗口和弹出菜单等临时窗口之外的所有小部件。


--------------------------------
## closeEvent(event)

参数：

- event – QCloseEvent

当 Qt 从窗口系统收到针对顶级窗口小部件的窗口关闭请求时，将使用给定事件调用此事件处理程序。

默认情况下，事件被接受并且窗口小部件被关闭。您可以重新实现此函数以更改窗口小部件响应窗口关闭请求的方式。例如，您可以通过在所有事件上调用 ignore() 来阻止窗口关闭。

主窗口应用程序通常使用此函数的重新实现来检查用户的工作是否已保存并在关闭前请求权限。


--------------------------------
## contentsMargins()

返回类型：QMargins

contentMargins 函数返回小部件的内容边距。


--------------------------------
## contentsRect()

返回类型：QRect

返回小部件边缘内的区域。


--------------------------------
## contextMenuEvent(event)

参数：

- event – QContextMenuEvent

此事件处理程序（用于事件）可在子类中重新实现，以接收小部件上下文菜单事件。

当小部件的 contextMenuPolicy 为 Qt::DefaultContextMenu 时，将调用此处理程序。

默认实现会忽略上下文事件。有关更多详细信息，请参阅 QContextMenuEvent 文档。


--------------------------------
## contextMenuPolicy()

返回类型：ContextMenuPolicy

属性 contextMenuPolicy 的获取器。


--------------------------------
## create([arg__1=0[, initializeWindow=true[, destroyOldWindow=true]]])

参数：

- arg__1 – WId
- initializeWindow – bool
- destroyOldWindow – bool

创建一个新的小部件窗口。

Qt 5 中忽略了参数 window、initializeWindow 和 destroyOldWindow。请使用 QWindow::fromWinId() 创建包装外部窗口的 QWindow，并将其传递给 createWindowContainer()。


--------------------------------
## createWinId()
## static createWindowContainer(window[, parent=None[, flags=Qt.WindowFlags()]])

参数：

- window – QWindow
- parent – QWidget
- flags – Combination of WindowType

返回类型：QWidget

创建一个 QWidget，使窗口能够嵌入到基于 QWidget 的应用程序中。

窗口容器是作为父级的子级创建的，并带有窗口标志 flags。

一旦窗口嵌入到容器中，容器将控制窗口的几何形状和可见性。不建议在嵌入窗口上显式调用 QWindow::setGeometry()、QWindow::show() 或 QWindow::hide()。

容器接管窗口的所有权。可以通过调用 QWindow::setParent() 从窗口容器中移除窗口。

窗口容器作为本机子窗口附加到其所属的顶层窗口。当窗口容器用作 QAbstractScrollArea 或 QMdiArea 的子级时，它将为其父链中的每个小部件创建一个本机窗口，以便在这种用例中正确堆叠和裁剪。为窗口容器创建本机窗口还可以正确堆叠和裁剪。这必须在显示窗口容器之前完成。具有许多本机子窗口的应用程序可能会出现性能问题。

窗口容器有许多已知的限制：

堆叠顺序；嵌入窗口将作为不透明框堆叠在小部件层次结构的顶部。多个重叠窗口容器实例的堆叠顺序未定义。

渲染集成；窗口容器不与 QGraphicsProxyWidget、render() 或类似功能互操作。

焦点处理；可以让窗口容器实例具有任何焦点策略，它将通过调用 QWindow::requestActivate() 将焦点委托给窗口。但是，从 QWindow 实例返回正常焦点链将取决于 QWindow 实例实现本身。例如，当进入具有选项卡焦点的基于 Qt Quick 的窗口时，很可能进一步的选项卡按下只会在 QML 应用程序内循环。此外，QWindow::requestActivate() 是否真正给予窗口焦点取决于平台。

在基于 QWidget 的应用程序中，使用许多窗口容器实例会极大地损害应用程序的整体性能。

自 6.7 起，如果窗口属于某个小部件（即，窗口是从调用 windowHandle() 接收的），则不会创建容器。相反，此函数将在重新设置为父级后返回小部件本身。由于不会创建容器，因此将忽略标志。换句话说，如果窗口属于某个小部件，请考虑直接将该小部件重新设置为父级，而不是使用此函数。


--------------------------------
## cursor()

返回类型：QCursor

Getter of property cursor  .


--------------------------------
## customContextMenuRequested(pos)

参数：

- pos – QPoint

当窗口小部件的 contextMenuPolicy 为 Qt::CustomContextMenu 且用户已请求窗口小部件上的上下文菜单时，会发出此信号。位置 pos 是窗口小部件接收的上下文菜单事件的位置。通常，这是在窗口小部件坐标中。此规则的例外是 QAbstractScrollArea 及其子类，它们将上下文菜单事件映射到 viewport() 的坐标。


--------------------------------
## destroy([destroyWindow=true[, destroySubWindows=true]])

参数：

- destroyWindow – bool
- destroySubWindows – bool

释放窗口系统资源。如果 destroyWindow 为真，则销毁窗口小部件窗口。

destroy() 对所有子窗口小部件递归调用自身，并将 destroySubWindows 传递给 destroyWindow 参数。为了更好地控制子窗口小部件的销毁，请先有选择地销毁子窗口小部件。

此函数通常从 QWidget 析构函数调用。


--------------------------------
## dragEnterEvent(event)

参数：

- event – QDragEnterEvent

当拖动正在进行且鼠标进入此小部件时，将调用此事件处理程序。事件在事件参数中传递。

如果忽略该事件，小部件将不会收到任何拖动移动事件。

请参阅拖放文档，了解如何在应用程序中提供拖放功能的概述。


--------------------------------
## dragLeaveEvent(event)

参数：

- event – QDragLeaveEvent

当拖动正在进行且鼠标离开此小部件时，将调用此事件处理程序。事件在事件参数中传递。

请参阅拖放文档，了解如何在应用程序中提供拖放功能的概述。


--------------------------------
## dragMoveEvent(event)

参数：

- event – QDragMoveEvent

如果正在进行拖放，并且发生以下任一情况，则将调用此事件处理程序：光标进入此小部件、光标在此小部件内移动，或者当此小部件具有焦点时按下键盘上的修饰键。事件在事件参数中传递。

请参阅拖放文档，了解如何在应用程序中提供拖放功能的概述。


--------------------------------
## dropEvent(event)

参数：

- event – QDropEvent

当拖动到此小部件上时，将调用此事件处理程序。事件在事件参数中传递。

请参阅拖放文档，了解如何在应用程序中提供拖放功能的概述。


--------------------------------
## effectiveWinId()

返回类型：WId

返回小部件的有效窗口系统标识符，即原生父窗口系统标识符。

如果小部件是原生的，则此函数返回原生小部件 ID。否则，将返回第一个原生父小部件（即包含此小部件的顶级小部件）的窗口 ID。


--------------------------------
## ensurePolished()

确保小部件及其子项已由 QStyle 润色（即具有适当的字体和调色板）。

QWidget 在小部件完全构建之后但在第一次显示之前调用此函数。如果您想确保在执行操作之前小部件已润色，则可以调用此函数，例如，在小部件的 sizeHint() 重新实现中可能需要正确的字体大小。请注意，此函数是从 sizeHint() 的默认实现中调用的。

润色对于最终初始化很有用，必须在调用所有构造函数（来自基类以及子类）之后进行。

如果您需要在小部件润色时更改某些设置，请重新实现 event() 并处理 QEvent::Polish 事件类型。


--------------------------------
## enterEvent(event)

参数：

- event – QEnterEvent

可以在子类中重新实现此事件处理程序，以接收在事件参数中传递的小部件进入事件。

当鼠标光标进入小部件时，会向小部件发送事件。


--------------------------------
## static find(arg__1)

参数：

- arg__1 – WId

返回类型：QWidget

返回指向具有窗口标识符/句柄 ID 的小部件的指针。

窗口标识符类型取决于底层窗口系统，请参阅 qwindowdefs.h 了解实际定义。如果没有具有此标识符的小部件，则返回 None。


--------------------------------
## focusInEvent(event)

参数：

- event – QFocusEvent

此事件处理程序可以在子类中重新实现，以接收小部件的键盘焦点事件（焦点已接收）。事件在事件参数中传递

小部件通常必须将FocusPolicy() 设置为 Qt::NoFocus 以外的其他内容才能接收焦点事件。（请注意，应用程序程序员可以在任何小部件上调用 setFocus()，即使是那些通常不接受焦点的小部件。）

默认实现会更新小部件（未指定 focusPolicy() 的窗口除外）。


--------------------------------
## focusNextChild()

返回类型：bool

查找一个新的窗口小部件，将键盘焦点赋予该窗口小部件（适合 Tab），如果可以找到新的窗口小部件，则返回 true，如果找不到，则返回 false。


--------------------------------
## focusNextPrevChild(next)

参数：

- next – bool

返回类型：bool

查找一个新的控件，将键盘焦点赋予该控件，以适应 Tab 和 Shift+Tab，如果可以找到新的控件，则返回 true，如果找不到，则返回 false。

如果 next 为 true，则此函数向前搜索，如果 next 为 false，则向后搜索。

有时，您需要重新实现此函数。例如，Web 浏览器可能会重新实现它以将其“当前活动链接”向前或向后移动，并且仅当到达“页面”上的最后一个或第一个链接时才调用 focusNextPrevChild()。

子控件在其父控件上调用 focusNextPrevChild()，但只有包含子控件的窗口才能决定将焦点重定向到何处。通过为对象重新实现此函数，您可以控制所有子控件的焦点遍历。


--------------------------------
## focusOutEvent(event)

参数：

- event – QFocusEvent

此事件处理程序可以在子类中重新实现，以接收小部件的键盘焦点事件（焦点丢失）。事件在事件参数中传递。

小部件通常必须将FocusPolicy() 设置为 Qt::NoFocus 以外的其他内容才能接收焦点事件。（请注意，应用程序程序员可以对任何小部件调用 setFocus()，即使是那些通常不接受焦点的小部件。）

默认实现会更新小部件（未指定 focusPolicy() 的窗口除外）。


--------------------------------
## focusPolicy()

返回类型：FocusPolicy

属性 focusPolicy 的获取器。


--------------------------------
## focusPreviousChild()

返回类型：bool

找到一个新的窗口小部件来赋予键盘焦点，适合 Shift+Tab，如果可以找到新的窗口小部件则返回 true，如果找不到则返回 false。


--------------------------------
## focusProxy()

返回类型：QWidget

返回焦点代理，如果没有焦点代理，则返回 None。


--------------------------------
## focusWidget()

返回类型：QWidget

返回已调用 setFocus 的此小部件的最后一个子项。对于顶级小部件，这是在此窗口被激活时将获得焦点的小部件

这与 focusWidget() 不同，后者返回当前活动窗口中的焦点小部件。


--------------------------------
## font()

返回类型：QFont

属性 font 的获取方法。


--------------------------------
## fontInfo()

返回类型：QFontInfo

返回小部件当前字体的字体信息。相当于 QFontInfo(widget->font())。


--------------------------------
## fontMetrics()

返回类型：QFontMetrics

返回小部件当前字体的字体度量。相当于 QFontMetrics(widget->font())。


--------------------------------
## foregroundRole()

返回类型：ColorRole

返回前景角色。

前景角色定义小部件调色板中用于绘制前景的颜色。

如果未设置明确的前景角色，则该函数返回与背景角色形成对比的角色。


--------------------------------
## frameGeometry()

返回类型：QRect

属性 frameGeometry 的获取器。


--------------------------------
## frameSize()

返回类型：QSize

属性 frameSize 的获取器。


--------------------------------
## geometry()

返回类型：QRect

属性 geometry 的获取器。


--------------------------------
## grab([rectangle=QRect(QPoint(0, 0), QSize(-1, -1))])

参数：

- rectangle – QRect

返回类型：QPixmap

将小部件渲染到受给定矩形限制的像素图中。如果小部件有任何子项，则它们也会被绘制在适当的位置。

如果指定了无效大小的矩形（默认），则会绘制整个小部件。


--------------------------------
## grabGesture(type[, flags=Qt.GestureFlags()])

参数：

- type – GestureType
- flags – Combination of GestureFlag

使用特定标志将小部件订阅到给定的手势。


--------------------------------
## grabKeyboard()

抓取键盘输入。

此小部件接收所有键盘事件，直到调用 releaseKeyboard()；其他小部件根本不会收到键盘事件。鼠标事件不受影响。如果要抓取鼠标事件，请使用 grabMouse()。

焦点小部件不受影响，但它不会接收任何键盘事件。setFocus() 会像往常一样移动焦点，但新的焦点小部件仅在调用 releaseKeyboard() 后才会接收键盘事件。

如果其他小部件当前正在抓取键盘输入，则首先释放该小部件的抓取。


--------------------------------
## grabMouse()

抓取鼠标输入。

此小部件接收所有鼠标事件，直到调用 releaseMouse()；其他小部件根本不会收到鼠标事件。键盘事件不受影响。如果要抓取，请使用 grabKeyboard()。

使用 Qt 时很少需要抓取鼠标，因为 Qt 会合理地抓取和释放鼠标。具体来说，Qt 会在按下鼠标按钮时抓取鼠标，并保持鼠标状态，直到释放最后一个按钮。


--------------------------------
## grabMouse(arg__1)

参数：

- arg__1 – QCursor

此函数重载 grabMouse() 。

抓取鼠标输入并更改光标形状。

光标将呈现光标形状（只要鼠标焦点被抓取），并且此小部件将是唯一接收鼠标事件的小部件，直到调用 releaseMouse() 为止。


--------------------------------
## grabShortcut(key[, context=Qt.WindowShortcut])

参数：

- key – QKeySequence
- context – ShortcutContext

返回类型：int

向 Qt 的快捷键系统添加快捷键，该系统在给定上下文中监视给定的按键序列。如果上下文是 Qt::ApplicationShortcut，则快捷键将应用于整个应用程序。否则，它要么是此小部件的本地按键，即 Qt::WidgetShortcut，要么是窗口本身的本地按键，即 Qt::WindowShortcut。

如果多个小部件都抓取了相同的按键序列，则当按键序列发生时，QEvent::Shortcut 事件将以非确定性顺序发送到它应用的所有小部件，但“ambiguous”标志设置为 true。


--------------------------------
## graphicsEffect()

返回类型：QGraphicsEffect

graphicsEffect 函数返回指向小部件图形效果的指针。

如果小部件没有图形效果，则返回 None。


--------------------------------
## graphicsProxyWidget()

返回类型：QGraphicsProxyWidget

返回图形视图中相应嵌入窗口小部件的代理窗口小部件；否则返回 None。


--------------------------------
## hasFocus()

返回类型：bool

属性焦点的获取器。


--------------------------------
## hasHeightForWidth()

返回类型：bool

如果小部件的首选高度取决于其宽度，则返回 true；否则返回 false。


--------------------------------
## hasMouseTracking()

返回类型：bool

属性 mouseTracking 的获取器。


--------------------------------
## hasTabletTracking()

返回类型：bool

属性 tabletTracking 的获取器。


--------------------------------
## heightForWidth(arg__1)

参数：

- arg__1 – int

返回类型：int

给定宽度 w，返回此小部件的首选高度。

如果此小部件具有布局，则默认实现将返回布局的首选高度。如果没有布局，则默认实现将返回 -1，表示首选高度不依赖于宽度。


--------------------------------
## hide()

隐藏小部件。该函数相当于 setVisible (false)。


--------------------------------
## hideEvent(event)

参数：

- event – QHideEvent

可以在子类中重新实现此事件处理程序以接收小部件隐藏事件。事件在事件参数中传递。

小部件隐藏后，会立即向其发送隐藏事件。


--------------------------------
## inputMethodEvent(event)

参数：

- event – QInputMethodEvent

此事件处理程序（用于事件）可在子类中重新实现，以接收输入法组合事件。当输入法状态发生变化时，将调用此处理程序。

请注意，在创建自定义文本编辑小部件时，必须明确设置 Qt::WA_InputMethodEnabled 窗口属性（使用 setAttribute() 函数）才能接收输入法事件。

默认实现调用 event->ignore()，它会拒绝输入法事件。有关更多详细信息，请参阅 QInputMethodEvent 文档。


--------------------------------
## inputMethodHints()

返回类型：Combination of InputMethodHint

属性 inputMethodHints 的获取器。


--------------------------------
## inputMethodQuery(arg__1)

参数：

- arg__1 – InputMethodQuery

返回类型：object

此方法仅与输入小部件相关。输入法使用它来查询小部件的一组属性，以便能够支持复杂的输入法操作，如支持周围文本和重新转换。

查询指定查询哪个属性。


--------------------------------
## insertAction(before, action)

参数：

- before – QAction
- action – QAction

将操作 action 插入到此小部件的操作列表中，位于操作 before 之前。如果 before 为 None 或 before 不是此小部件的有效操作，则附加操作。

QWidget 应该只具有每个操作中的一个。


--------------------------------
## insertActions(before, actions)

参数：

- before – QAction
- actions – .list of QAction

将操作操作插入到此小部件的操作列表中，在操作之前。如果操作之前为 None 或之前不是此小部件的有效操作，则附加操作。

QWidget 最多可以拥有每个操作中的一个。


--------------------------------
## internalWinId()

返回类型：WId


--------------------------------
## isActiveWindow()

返回类型：bool

属性 isActiveWindow 的获取器。


--------------------------------
## isAncestorOf(child)

参数：

- child – QWidget

返回类型：bool

如果此窗口小部件是给定子窗口小部件的父窗口小部件（或祖父母窗口小部件等，直到任何级别），并且两个窗口小部件都在同一个窗口内，则返回 true；否则返回 false。


--------------------------------
## isEnabled()

返回类型：bool

已启用属性的获取器。


--------------------------------
## isEnabledTo(arg__1)

参数：

- arg__1 – QWidget

返回类型：bool

如果此小部件在祖先已启用的情况下变为启用状态，则返回 true；否则返回 false。

如果小部件本身以及除祖先之外的每个父级均未明确禁用，则会出现这种情况。

如果此小部件或其任何祖先已明确禁用，则 isEnabledTo(0) 返回 false。

此处的祖先一词表示同一窗口内的父小部件。

因此，isEnabledTo(0) 停止在此小部件的窗口，而 isEnabled() 则将父窗口也考虑在内。


--------------------------------
## isFullScreen()

返回类型：bool

属性 fullScreen 的获取器。


--------------------------------
## isHidden()

返回类型：bool

如果小部件被隐藏，则返回 true，否则返回 false。

隐藏的小部件只有在调用 show() 时才会变为可见。当父级显示时，它不会自动显示。

要检查可见性，请改用 ! isVisible()（注意感叹号）。

isHidden() 意味着 ! isVisible() ，但小部件可以同时不可见和不隐藏。对于不可见小部件的子小部件，情况就是如此。

如果出现以下情况，小部件将被隐藏：

- 它们被创建为独立窗口，
- 它们被创建为可见小部件的子小部件，
- 调用了 hide() 或 setVisible (false)。


--------------------------------
## isLeftToRight()

返回类型：bool


--------------------------------
##  isMaximized()

返回类型：bool

属性最大化的获取器。


--------------------------------
## isMinimized()

返回类型：bool

属性的吸气剂最小化。


--------------------------------
## isModal()

返回类型：bool

属性 modal 的获取方法。


--------------------------------
## isRightToLeft()

返回类型：bool


--------------------------------
## isTopLevel()

返回类型：bool

改用 isWindow()。


--------------------------------
## isVisible()

返回类型：bool

可见属性的获取器。


--------------------------------
## isVisibleTo(arg__1)

参数：

- arg__1 – QWidget

返回类型：bool

如果此小部件在显示祖先时变为可见，则返回 true；否则返回 false。

如果小部件本身以及除祖先之外的任何父级都没有被明确隐藏，则会出现 true 的情况。

如果小部件被屏幕上的其他窗口遮挡，但如果它或它们被移动，则可能在物理上可见，则此函数仍将返回 true。

isVisibleTo(0) 与 isVisible() 相同。


--------------------------------
## isWindow()

返回类型：bool

如果窗口小部件是独立窗口，则返回 true，否则返回 false。

窗口是一种在视觉上不是任何其他窗口小部件的子窗口小部件，通常具有框架和窗口标题。

窗口可以有一个父窗口小部件。然后它将与其父窗口小部件组合在一起，并在父窗口小部件被删除时被删除，在父窗口小部件最小化时被最小化等。如果窗口管理器支持，它还将与其父窗口小部件具有一个公共任务栏条目。

QDialog 和 QMainWindow 窗口小部件默认为窗口，即使在构造函数中指定了父窗口小部件。此行为由 Qt::Window 标志指定。


--------------------------------
## isWindowModified()

返回类型：bool

属性 windowModified 的获取器。


--------------------------------
## keyPressEvent(event)

参数：

- event – QKeyEvent

此事件处理程序（用于事件）可在子类中重新实现，以接收小部件的按键事件。

小部件必须调用 setFocusPolicy() 来初始接受焦点，并具有焦点才能接收按键事件。

如果您重新实现此处理程序，则在您未对按键执行操作时调用基类实现非常重要。

如果用户按下 QKeySequence::Cancel 的按键序列（通常是 Escape 键），则默认实现会关闭弹出小部件。否则，事件将被忽略，以便小部件的父级可以对其进行解释。

请注意，QKeyEvent 以 isAccepted() == true 开头，因此您无需调用 QKeyEvent::accept() - 如果您对按键执行操作，则不要调用基类实现。


--------------------------------
## keyReleaseEvent(event)

参数：

- event – QKeyEvent

此事件处理程序（用于事件）可在子类中重新实现，以接收小部件的按键释放事件。

小部件必须首先接受焦点并具有焦点才能接收按键释放事件。

如果您重新实现此处理程序，则在不对按键采取行动的情况下调用基类实现非常重要。

默认实现会忽略该事件，以便小部件的父级可以对其进行解释。

请注意，QKeyEvent 以 isAccepted() == true 开头，因此您无需调用 QKeyEvent::accept() - 如果您对按键采取行动，则不要调用基类实现。


--------------------------------
## static keyboardGrabber()

返回类型：QWidget

返回当前正在抓取键盘输入的小部件。

如果此应用程序中当前没有小部件正在抓取键盘，则返回 None。


--------------------------------
## layout()

返回类型：QLayout

返回此小部件上安装的布局管理器，如果未安装布局管理器，则返回 None。

布局管理器设置已添加到布局的小部件子项的几何形状。


--------------------------------
## layoutDirection()

返回类型：LayoutDirection

属性 layoutDirection 的获取方法。


--------------------------------
## leaveEvent(event)

参数：

- event – QEvent

可以在子类中重新实现此事件处理程序，以接收在事件参数中传递的小部件离开事件。

当鼠标光标离开小部件时，将向小部件发送离开事件。


--------------------------------
## locale()

返回类型：QLocale

属性 locale 的获取器。


--------------------------------
## lower()

将小部件降低到父小部件堆栈的底部。

调用此函数后，小部件将在视觉上位于任何重叠的兄弟小部件后面（因此被其遮挡）。


--------------------------------
## mapFrom(arg__1, arg__2)

参数：

- arg__1 – QWidget
- arg__2 – QPoint

返回类型：QPoint

这是一个重载函数。


--------------------------------
## mapFrom(arg__1, arg__2)

参数：

- arg__1 – QWidget
- arg__2 – QPointF

返回类型：QPointF

将小部件坐标 pos 从父级坐标系转换为此小部件的坐标系。父级不能为 None，并且必须是调用小部件的父级。


--------------------------------
## mapFromGlobal(arg__1)

参数：

- arg__1 – QPoint

返回类型：QPoint

这是一个重载函数。


--------------------------------
## mapFromGlobal(arg__1)

参数：

- arg__1 – QPointF

返回类型：QPointF

将全局屏幕坐标 pos 转换为小部件坐标。


--------------------------------
## mapFromParent(arg__1)

参数：

- arg__1 – QPoint

返回类型：QPoint

这是一个重载函数。


--------------------------------
## mapFromParent(arg__1)

参数：

- arg__1 – QPointF

返回类型：QPointF

将父窗口小部件坐标 pos 转换为窗口小部件坐标。

如果窗口小部件没有父级，则与 mapFromGlobal() 相同。


--------------------------------
## mapTo(arg__1, arg__2)

参数：

- arg__1 – QWidget
- arg__2 – QPoint

返回类型：QPoint

这是一个重载函数。


--------------------------------
## mapTo(arg__1, arg__2)

参数：

- arg__1 – QWidget
- arg__2 – QPointF

返回类型：QPointF

将小部件坐标 pos 转换为父级坐标系。父级不能为 None，并且必须是调用小部件的父级。


--------------------------------
## mapToGlobal(arg__1)

参数：

- arg__1 – QPoint

返回类型：QPoint

这是一个重载函数。


--------------------------------
## mapToGlobal(arg__1)

参数：

- arg__1 – QPointF

返回类型：QPointF

将小部件坐标 pos 转换为全局屏幕坐标。例如，mapToGlobal(QPointF(0,0)) 将提供小部件左上角像素的全局坐标。


--------------------------------
## mapToParent(arg__1)

参数：

- arg__1 – QPointF

返回类型：QPointF

将小部件坐标 pos 转换为父小部件中的坐标。

如果小部件没有父级，则与 mapToGlobal() 相同。


--------------------------------
## mapToParent(arg__1)

参数：

- arg__1 – QPoint

返回类型：QPoint

这是一个重载函数。


--------------------------------
## mask()

返回类型：QRegion

返回当前在小部件上设置的掩码。如果没有设置掩码，则返回值将是一个空区域。


--------------------------------
## maximumHeight()

返回类型：int

属性 maximumHeight 的获取器。


--------------------------------
## maximumSize()

返回类型：QSize

属性 maximumSize 的获取器。


--------------------------------
## maximumWidth()

返回类型：int

属性 maximumWidth 的获取器。


--------------------------------
## minimumHeight()

返回类型：int

属性 minimumHeight 的获取器。


--------------------------------
## minimumSize()

返回类型：QSize

属性 minimumSize 的获取器。


--------------------------------
## minimumSizeHint()

返回类型：QSize

属性 minimumSizeHint 的获取器。


--------------------------------
## minimumWidth()

返回类型：int

属性 minimumWidth 的获取器。


--------------------------------
## mouseDoubleClickEvent(event)

参数：

- event – QMouseEvent

此事件处理程序（用于事件）可以在子类中重新实现，以接收小部件的鼠标双击事件。

默认实现调用 mousePressEvent() 。


--------------------------------
## static mouseGrabber()

返回类型：QWidget

返回当前正在抓取鼠标输入的小部件。

如果此应用程序中当前没有小部件正在抓取鼠标，则返回 None。


--------------------------------
## mouseMoveEvent(event)

参数：

- event – QMouseEvent

此事件处理程序（用于事件）可以在子类中重新实现，以接收小部件的鼠标移动事件。

如果关闭鼠标跟踪，则只有在移动鼠标时按下鼠标按钮时才会发生鼠标移动事件。 如果打开鼠标跟踪，即使没有按下鼠标按钮也会发生鼠标移动事件。

QMouseEvent::pos() 报告鼠标光标相对于此小部件的位置。 对于按下和释放事件，位置通常与上次鼠标移动事件的位置相同，但如果用户的手抖动，位置可能会有所不同。 这是底层窗口系统的功能，而不是 Qt。

如果您想在鼠标移动时立即显示工具提示（例如，使用 QMouseEvent::pos() 获取鼠标坐标并将其显示为工具提示），您必须首先启用鼠标跟踪，如上所述。 然后，为了确保工具提示立即更新，您必须在 mouseMoveEvent() 的实现中调用 showText() 而不是 setToolTip()。


--------------------------------
## mousePressEvent(event)

参数：

- event – QMouseEvent

此事件处理程序（用于事件）可在子类中重新实现，以接收小部件的鼠标按下事件。

如果您在 mousePressEvent() 中创建新的小部件，mouseReleaseEvent() 可能不会到达您期望的位置，这取决于底层窗口系统（或 X11 窗口管理器）、小部件的位置等。

默认实现会在您单击窗口外部时关闭弹出小部件。对于其他小部件类型，它不执行任何操作。


--------------------------------
## mouseReleaseEvent(event)

参数：

- event – QMouseEvent

对于事件，此事件处理程序可以在子类中重新实现，以接收小部件的鼠标释放事件。


--------------------------------
## move(arg__1)

参数：

- arg__1 – QPoint

属性 pos 的设置者。


--------------------------------
## move(x, y)

参数：

- x – int
- y – int

这是一个重载函数。

这对应于 move(QPoint(x, y))。


--------------------------------
## moveEvent(event)

参数：

- event – QMoveEvent

此事件处理程序可以在子类中重新实现，以接收在事件参数中传递的小部件移动事件。当小部件接收到此事件时，它已经处于新位置。

可以通过 QMoveEvent::oldPos() 访问旧位置。


--------------------------------
## nativeEvent(eventType, message)

参数：

- eventType – QByteArray
- message – void

返回类型：PyObject

此特殊事件处理程序可以在子类中重新实现，以接收由消息参数中传递的 eventType 标识的本机平台事件。

在重新实现此函数时，如果您想停止 Qt 处理的事件，请返回 true 并设置结果。result 参数仅在 Windows 上有意义。如果返回 false，则此本机事件将传递回 Qt，Qt 会将该事件转换为 Qt 事件并将其发送到小部件。

| Platform | Event Type Identifier | Message Type | Result Type |
| -------- | --------------------- | ------------ | ----------- |
| Windows  | “windows_generic_MSG” | MSG *        | LRESULT     |
| macOS    | “NSEvent”             | NSEvent *    |             |
| XCB      | “xcb_generic_event_t” | xcb_generic_event_t * |    |


--------------------------------
## nativeParentWidget()

返回类型：QWidget

返回此小部件的本机父级，即下一个具有系统标识符的祖先小部件，如果它没有任何本机父级，则返回 None。


--------------------------------
## nextInFocusChain()

返回类型：QWidget

返回此小部件焦点链中的下一个小部件。


--------------------------------
## normalGeometry()

返回类型：QRect

属性 normalGeometry 的获取方法。


--------------------------------
## overrideWindowFlags(type)

参数：

- type – Combination of WindowType

将小部件的窗口标志设置为标志，而不告知窗口系统。


--------------------------------
## overrideWindowState(state)

参数：

- state – Combination of WindowState


--------------------------------
## paintEvent(event)

参数：

- event – QPaintEvent

此事件处理程序可以在子类中重新实现，以接收事件中传递的绘制事件。

绘制事件是重新绘制全部或部分小部件的请求。它可能由于以下原因之一而发生：

调用了 repaint() 或 update()，

小部件被遮挡并且现在已被发现，或者

许多其他原因。

许多小部件可以在被要求时简单地重新绘制其整个表面，但一些速度较慢的小部件需要通过仅绘制请求的区域进行优化：QPaintEvent::region()。这种速度优化不会改变结果，因为在事件处理期间绘制被剪辑到该区域。例如，QListView 和 QTableView 就是这样做的。

Qt 还尝试通过将多个绘制事件合并为一个来加快绘制速度。当多次调用 update() 或窗口系统发送多个绘制事件时，Qt 会将这些事件合并为一个具有较大区域的事件（请参阅 QRegion::united()）。repaint() 函数不允许这种优化，因此我们建议尽可能使用 update()。

当发生绘制事件时，更新区域通常已被擦除，因此您正在小部件的背景上进行绘制。

可以使用 setBackgroundRole() 和 setPalette() 设置背景。

自 Qt 4.0 起，QWidget 会自动对其绘制进行双缓冲，因此无需在 paintEvent() 中编写双缓冲代码来避免闪烁。


--------------------------------
## palette()

返回类型：QPalette

属性调色板的获取器。


--------------------------------
## parentWidget()

返回类型：QWidget

返回此小部件的父级，如果它没有任何父小部件，则返回 None。


--------------------------------
## pos()

返回类型：QPoint

属性 pos 的获取器。


--------------------------------
## previousInFocusChain()

返回类型：QWidget

previousInFocusChain 函数返回此小部件焦点链中的前一个小部件。


--------------------------------
## raise_()
## rect()

返回类型：QRect

属性 rect 的获取器。


--------------------------------
## releaseKeyboard()

释放键盘抓取。


--------------------------------
## releaseMouse()

释放鼠标抓取。


--------------------------------
## releaseShortcut(id)

参数：

- id – int

从 Qt 的快捷方式系统中删除具有指定 ID 的快捷方式。小部件将不再接收快捷方式的键序列的 QEvent::Shortcut 事件（除非它有其他具有相同键序列的快捷方式）。


--------------------------------
## removeAction(action)

参数：

- action – QAction

从此小部件的操作列表中删除操作。


--------------------------------
## render(target[, targetOffset=QPoint()[, sourceRegion=QRegion()[, renderFlags=QWidget.RenderFlags(QWidget.RenderFlag.DrawWindowBackground | QWidget.RenderFlag.DrawChildren)]]])

参数：

- target – QPaintDevice
- targetOffset – QPoint
- sourceRegion – QRegion
- renderFlags – Combination of RenderFlag


使用 renderFlags 将此小部件的 sourceRegion 渲染到目标中，以确定如何渲染。渲染从目标中的 targetOffset 开始。例如：

```python
pixmap = QPixmap(widget.size())
widget.render(pixmap)
```

如果 sourceRegion 为空区域，则此函数将使用 rect() 作为区域，即整个小部件。

确保在渲染之前为目标设备的活动绘图器（如果有）调用 QPainter::end()。例如：

```python
painter = QPainter(self)
...
painter.end()
myWidget.render(self)
```


--------------------------------
## render(painter, targetOffset[, sourceRegion=QRegion()[, renderFlags=QWidget.RenderFlags(QWidget.RenderFlag.DrawWindowBackground | QWidget.RenderFlag.DrawChildren)]])

参数：

- painter – QPainter
- targetOffset – QPoint
- sourceRegion – QRegion
- renderFlags – Combination of RenderFlag

这是一个重载函数。

将小部件渲染到绘图器的 QPainter::device() 中。

渲染时将使用应用于绘图器的变换和设置。


--------------------------------
## repaint()

通过立即调用 paintEvent() 直接重新绘制小部件，除非更新被禁用或小部件被隐藏。

我们建议仅在需要立即重新绘制时（例如在动画期间）才使用 repaint()。在大多数情况下，update() 更好，因为它允许 Qt 优化速度并最大限度地减少闪烁。


--------------------------------
## repaint(arg__1)

参数：

- arg__1 – QRect

这是一个重载函数。

此版本重新绘制了小部件内部的矩形。


--------------------------------
## repaint(arg__1)

参数：

- arg__1 – QRegion

这是一个重载函数。

此版本重新绘制了小部件内部的区域 rgn。


--------------------------------
## repaint(x, y, w, h)

参数：

- x – int
- y – int
- w – int
- h – int

这是一个重载函数。

此版本在小部件内重新绘制一个矩形 (x, y, w, h)。

如果 w 为负数，则用 width() - x 替换；如果 h 为负数，则用 width height() - y 替换。


--------------------------------
## resize(arg__1)

参数：

- arg__1 – QSize

属性大小的设置者。


--------------------------------
## resize(w, h)

参数：

- w – int
- h – int

这是一个重载函数。

这对应于resize(QSize(w, h)).


--------------------------------
## resizeEvent(event)

参数：

- event – QResizeEvent

此事件处理程序可以在子类中重新实现，以接收在事件参数中传递的小部件调整大小事件。调用 resizeEvent() 时，小部件已经具有其新的几何形状。旧大小可通过 QResizeEvent::oldSize() 访问。

处理调整大小事件后，小部件将被擦除并立即接收绘制事件。此处理程序内不需要（或不应该）进行任何绘制。


--------------------------------
## restoreGeometry(geometry)

参数：

- geometry – QByteArray

返回类型：bool

恢复存储在字节数组 geometry 中的顶级小部件的几何形状和状态。成功时返回 true；否则返回 false。

如果恢复的几何形状不在屏幕上，它将被修改为位于可用的屏幕几何形状内。

要恢复使用 QSettings 保存的几何形状，您可以使用如下代码：

```python
settings = QSettings("MyCompany", "MyApp")
myWidget.restoreGeometry(settings.value("myWidget/geometry").toByteArray())
```

有关窗口几何问题的概述，请参阅窗口几何文档。

使用 restoreState() 恢复工具栏和停靠小部件的几何形状和状态。


--------------------------------
## saveGeometry()

返回类型：QByteArray

保存顶层小部件的当前几何图形和状态。

要在窗口关闭时保存几何图形，您可以实现如下关闭事件：

```python
def closeEvent(self, event):

    settings = QSettings("MyCompany", "MyApp")
    settings.setValue("geometry", saveGeometry())
    QWidget.closeEvent(event)
```

有关窗口几何问题的概述，请参阅窗口几何文档。

使用 saveState() 保存工具栏和停靠小部件的几何形状和状态。


--------------------------------
## screen()

返回类型：QScreen

返回小部件所在的屏幕。


--------------------------------
## scroll(dx, dy, arg__3)

参数：

- dx – int
- dy – int
- arg__3 – QRect

这是一个重载函数。

此版本仅滚动 r，不会移动小部件的子项。

如果 r 为空或无效，则结果未定义。


--------------------------------
## scroll(dx, dy)

参数：

- dx – int
- dy – int

将包括其子项的窗口小部件向右滚动 dx 像素，向下滚动 dy。dx 和 dy 都可能为负数。

滚动后，窗口小部件将收到需要重新绘制的区域的绘制事件。对于 Qt 知道不透明的窗口小部件，这仅是新暴露的部分。例如，如果不透明窗口小部件向左滚动 8 像素，则只有右边缘的 8 像素宽条纹需要更新。

由于窗口小部件默认传播其父项的内容，因此您需要设置 autoFillBackground 属性，或使用 setAttribute() 设置 Qt::WA_OpaquePaintEvent 属性，以使窗口小部件不透明。

对于使用内容传播的窗口小部件，滚动将导致整个滚动区域的更新。


--------------------------------
## setAcceptDrops(on)

参数：

- on – bool

属性 acceptDrops 的设置者。


--------------------------------
## setAccessibleDescription(description)

参数：

- description – str

属性 accessibleDescription 的设置者。


--------------------------------
## setAccessibleName(name)

参数：

- name – str

属性 accessibleName 的设置者。


--------------------------------
## setAttribute(arg__1[, on=true])

参数：

- arg__1 – WidgetAttribute
- on – bool

如果为真，则设置此小部件上的属性attribute；否则清除该属性。


--------------------------------
## setAutoFillBackground(enabled)

参数：

- enabled – bool

属性 autoFillBackground 的设置者。


--------------------------------
## setBackgroundRole(arg__1)

参数：

- arg__1 – ColorRole

将小部件的背景角色设置为 role。

背景角色定义小部件调色板中用于渲染背景的画笔。

如果 role 是 QPalette::NoRole，则小部件将继承其父级的背景角色。

请注意，样式可以自由选择调色板中的任何颜色。如果使用 setBackgroundRole() 未获得所需结果，您可以修改调色板或设置样式表。


--------------------------------
## setBaseSize(basew, baseh)

参数：

- basew – int
- baseh – int

这是一个重载函数。

这对应于 setBaseSize (QSize(basew, baseh))。将小部件基本大小设置为宽度 basew 和高度 baseh。


--------------------------------
## setBaseSize(arg__1)

参数：

- arg__1 – QSize

属性 baseSize 的设置者。


--------------------------------
## setContentsMargins(margins)

参数：

- margins – QMargins

这是一个重载函数。

setContentsMargins 函数设置小部件内容周围的边距。

设置小部件内容周围的边距，使其大小由边距决定。边距由布局系统使用，并可由子类使用来指定要绘制的区域（例如，不包括框架）。

更改边距将触发 resizeEvent() 。


--------------------------------
## setContentsMargins(left, top, right, bottom)

参数：

- left – int
- top – int
- right – int
- bottom – int

设置小部件内容周围的边距，使其具有左、上、右和下的大小。边距由布局系统使用，并可由子类使用来指定要绘制的区域（例如，不包括框架）。

更改边距将触发 resizeEvent() 。


--------------------------------
## setContextMenuPolicy(policy)

参数：

- policy – ContextMenuPolicy

属性 contextMenuPolicy 的设置者。


--------------------------------
## setCursor(arg__1)

参数：

- arg__1 – QCursor

属性 cursor 的设置者。


--------------------------------
## setDisabled(arg__1)

参数：

- arg__1 – bool

如果 disable 为真，则禁用小部件输入事件；否则启用输入事件。

请参阅启用文档以了解更多信息。


--------------------------------
## setEnabled(arg__1)

参数：

- arg__1 – bool

属性的设置器已启用。


--------------------------------
## setFixedHeight(h)

参数：

- h – int

将小部件的最小和最大高度都设置为 h，而不改变宽度。提供方便。


--------------------------------
## setFixedSize(w, h)

参数：

- w – int
- h – int

这是一个重载函数。

将小部件的宽度设置为 w，高度设置为 h。


--------------------------------
## setFixedSize(arg__1)

参数：

- arg__1 – QSize

将小部件的最小和最大尺寸都设置为 s，从而防止其增大或缩小。

这将覆盖 QLayout 设置的默认尺寸限制。

要删除限制，请将尺寸设置为 QWIDGETSIZE_MAX 。

或者，如果您希望小部件根据其内容具有固定尺寸，则可以调用 setSizeConstraint ( SetFixedSize )；


--------------------------------
## setFixedWidth(w)

参数：

- w – int

将小部件的最小和最大宽度都设置为 w，而不改变高度。提供方便。


--------------------------------
## setFocus(reason)

参数：

- reason – FocusReason

如果此小部件或其父项之一是活动窗口，则将键盘输入焦点赋予此小部件（或其焦点代理）。原因参数将传递到从此函数发送的任何焦点事件中，它用于解释导致小部件获得焦点的原因。如果窗口不活动，则窗口变为活动状态时将为小部件提供焦点。

首先，将焦点即将改变事件发送到焦点小部件（如果有），以告知它即将失去焦点。然后改变焦点，将焦点移出事件发送到上一个焦点项目，并将焦点进入事件发送到新项目，以告知它刚刚收到焦点。（如果焦点进入和焦点移出小部件相同，则不会发生任何事情。）

setFocus() 将焦点赋予小部件，无论其焦点策略如何，但不会清除任何键盘抓取（请参阅 grabKeyboard()）。

请注意，如果小部件被隐藏，它将不会接受焦点，直到显示出来。


--------------------------------
## setFocus()

这是一个重载函数。

如果此窗口小部件或其父代之一是活动窗口，则将键盘输入焦点赋予此窗口小部件（或其焦点代理）。


--------------------------------
## setFocusPolicy(policy)

参数：

- policy – FocusPolicy

focusPolicy 属性的设置者。


--------------------------------
## setFocusProxy(arg__1)

参数：

- arg__1 – QWidget

将小部件的焦点代理设置为小部件 w。如果 w 为 None，则该函数会将此小部件重置为没有焦点代理。

某些小部件可以“具有焦点”，但会创建一个子小部件（例如 QLineEdit）来实际处理焦点。在这种情况下，小部件可以将行编辑设置为其焦点代理。

setFocusProxy() 设置当“此小部件”获得焦点时实际获得焦点的小部件。如果有焦点代理，则 setFocus() 和 hasFocus() 将对焦点代理进行操作。如果“此小部件”是焦点小部件，则 setFocusProxy() 会将焦点移动到新的焦点代理。


--------------------------------
## setFont(arg__1)

参数：

- arg__1 – QFont

字体属性的设置者。


--------------------------------
## setForegroundRole(arg__1)

参数：

- arg__1 – ColorRole

将小部件的前景角色设置为 role。

前景角色定义小部件调色板中用于绘制前景的颜色。

如果 role 是 QPalette::NoRole，则小部件使用与背景角色形成对比的前景角色。

请注意，样式可以自由选择调色板中的任何颜色。 如果使用 setForegroundRole() 未获得所需结果，您可以修改调色板或设置样式表。


--------------------------------
## setGeometry(arg__1)

参数：

- arg__1 – QRect

几何属性的设置者。


--------------------------------
## setGeometry(x, y, w, h)

参数：

- x – int
- y – int
- w – int
- h – int

这是一个重载函数。

这对应于 setGeometry (QRect(x, y, w, h))。


--------------------------------
## setGraphicsEffect(effect)

参数：

- effect – QGraphicsEffect

setGraphicsEffect 函数用于设置小部件的图形效果。

将效果设置为小部件的效果。如果此小部件上已安装效果，QWidget 将在安装新效果之前删除现有效果。

如果效果是其他小部件上安装的效果，setGraphicsEffect() 将从小部件中删除该效果并将其安装在此小部件上。

QWidget 拥有效果。


--------------------------------
## setHidden(hidden)

参数：

- hidden – bool

便利功能，相当于setVisible(!``hidden``)。


--------------------------------
## setInputMethodHints(hints)

参数：

- hints – Combination of InputMethodHint

属性 inputMethodHints 的设置器。


--------------------------------
## setLayout(arg__1)

参数：

- arg__1 – QLayout

将此小部件的布局管理器设置为布局。

如果此小部件上已安装布局管理器，QWidget 将不允许您安装另一个。您必须先删除现有布局管理器（由 layout() 返回），然后才能使用新布局调用 setLayout()。

如果 layout 是不同小部件上的布局管理器，setLayout() 将重新设置布局的父级并使其成为此小部件的布局管理器。

示例：

```python
layout = QVBoxLayout()
layout.addWidget(formWidget)
setLayout(layout)
```

调用此函数的另一种方法是将此小部件传递给布局的构造函数。

QWidget 将拥有布局的所有权。


--------------------------------
## setLayoutDirection(direction)

参数：

- direction – LayoutDirection

属性 layoutDirection 的设置器。


--------------------------------
## setLocale(locale)

参数：

- locale – QLocale

属性 locale 的设置者。


--------------------------------
## setMask(arg__1)

参数：

- arg__1 – QBitmap

仅使位图具有相应 1 位的小部件像素可见。如果区域包含小部件 rect() 之外的像素，则该区域中的窗口系统控件可能可见也可能不可见，具体取决于平台。

请注意，如果区域特别复杂，此效果可能会很慢。

以下代码显示了如何使用具有 alpha 通道的图像为小部件生成蒙版：

```python
topLevelLabel = QLabel()
pixmap = QPixmap(":/images/tux.png")
topLevelLabel.setPixmap(pixmap)
topLevelLabel.setMask(pixmap.mask())
```

此代码显示的标签使用其包含的图像进行屏蔽，使其看起来像是将不规则形状的图像直接绘制在屏幕上。

屏蔽的小部件仅在其可见部分接收鼠标事件。


--------------------------------
## setMask(arg__1)

参数：

- arg__1 – QRegion

这是一个重载函数。

仅使窗口小部件与区域重叠的部分可见。如果该区域包含窗口小部件 rect() 之外的像素，则该区域中的窗口系统控件可能可见也可能不可见，具体取决于平台。

由于 QRegion 允许创建任意复杂的区域，因此可以制作窗口小部件蒙版以适应最不寻常形状的窗口，甚至允许显示带有孔的窗口小部件。请注意，如果区域特别复杂，此效果可能会很慢。

窗口小部件蒙版用于向窗口系统提示应用程序不希望蒙版外的区域发生鼠标事件。在大多数系统上，它们还会导致粗糙的视觉剪辑。要获得平滑的窗口边缘，请改用半透明背景和抗锯齿绘画，如半透明背景示例中所示。


--------------------------------
## setMaximumHeight(maxh)

参数：

- maxh – int

属性 maximumHeight 的设置者。


--------------------------------
## setMaximumSize(maxw, maxh)

参数：

- maxw – int
- maxh – int

这是一个重载函数。

此函数对应于setMaximumSize (QSize(maxw, maxh))。将最大宽度设置为maxw，将最大高度设置为maxh。


--------------------------------
## setMaximumSize(arg__1)

参数：

- arg__1 – QSize

属性 maximumSize 的设置者。


--------------------------------
## setMaximumWidth(maxw)

参数：

- maxw – int

属性 maximumWidth 的设置者。


--------------------------------
## setMinimumHeight(minh)

参数：

- minh – int

属性 minimumHeight 的设置者。


--------------------------------
## setMinimumSize(arg__1)

参数：

- arg__1 – QSize

属性 minimumSize 的设置者。


--------------------------------
## setMinimumSize(minw, minh)

参数：

- minw – int
- minh – int

这是一个重载函数。

此函数对应于setMinimumSize (QSize(minw, minh))。将最小宽度设置为minw，将最小高度设置为minh。


--------------------------------
## setMinimumWidth(minw)

参数：

- minw – int

属性 minimumWidth 的设置者。


--------------------------------
## setMouseTracking(enable)

参数：

- enable – bool

属性 mouseTracking 的设置器。


--------------------------------
## setPalette(arg__1)

参数：

- arg__1 – QPalette

属性调色板的设置器。


--------------------------------
## setParent(parent)

参数：

- parent – QWidget

将窗口小部件的父窗口设置为父窗口，并重置窗口标志。窗口小部件将移动到其新父窗口的位置 (0, 0)。

如果新的父窗口小部件位于不同的窗口中，则重新设置父窗口小部件及其子窗口将附加到新父窗口小部件的选项卡链的末尾，内部顺序与之前相同。如果其中一个移动的窗口小部件具有键盘焦点，setParent() 将为该窗口小部件调用 clearFocus()。

如果新的父窗口小部件与旧的父窗口小部件位于同一个窗口中，则设置父窗口小部件不会更改选项卡顺序或键盘焦点。

如果“新”父窗口小部件是旧的父窗口小部件，则此函数不执行任何操作。


--------------------------------
## setParent(parent, f)

参数：

- parent – QWidget
- f – Combination of WindowType

这是一个重载函数。

此函数还将小部件标志 f 作为参数。


--------------------------------
## setScreen(arg__1)

参数：

- arg__1 – QScreen

设置小部件应在哪个屏幕上显示。

设置屏幕只对窗口有意义。如有必要，小部件的窗口将在屏幕上重新创建。


--------------------------------
## setShortcutAutoRepeat(id[, enable=true])

参数：

- id – int
- enable – bool

如果 enable 为真，则启用具有给定 id 的快捷方式的自动重复；否则，禁用该功能。


--------------------------------
## setShortcutEnabled(id[, enable=true])

参数：

- id – int
- enable – bool

如果 enable 为真，则启用具有给定 id 的快捷方式；否则禁用该快捷方式。


--------------------------------
## setSizeIncrement(arg__1)

参数：

- arg__1 – QSize

属性 sizeIncrement 的设置者。


--------------------------------
## setSizeIncrement(w, h)

参数：

- w – int
- h – int

这是一个重载函数。

将 x（宽度）尺寸增量设置为 w，将 y（高度）尺寸增量设置为 h。


--------------------------------
## setSizePolicy(horizontal, vertical)

参数：

- horizontal – Policy
- vertical – Policy

这是一个重载函数。

将小部件的尺寸策略设置为水平和垂直，具有标准拉伸并且没有高度与宽度。


--------------------------------
## setSizePolicy(arg__1)

参数：

- arg__1 – QSizePolicy

属性 sizePolicy 的设置者。


--------------------------------
## setStatusTip(arg__1)

参数：

- arg__1 – str

属性 statusTip 的设置者。


--------------------------------
## setStyle(arg__1)

参数：

- arg__1 – QStyle

将小部件的 GUI 样式设置为 style。样式对象的所有权不会转移。

如果未设置样式，小部件将改用应用程序的样式 style()。

设置小部件的样式对现有或未来的子小部件没有影响。


--------------------------------
## setStyleSheet(styleSheet)

参数：

- styleSheet – str

属性 styleSheet 的设置者。


--------------------------------
## static setTabOrder(arg__1, arg__2)

参数：

- arg__1 – QWidget
- arg__2 – QWidget

将第二个小部件放在焦点顺序中第一个小部件之后。

它有效地将第二个小部件从其焦点链中移除，并将其插入到第一个小部件之后。

请注意，由于第二个小部件的选项卡顺序已更改，因此您应该按如下方式对链进行排序：

```python
setTabOrder(a, b) # a to b
setTabOrder(b, c) # a to b to c
setTabOrder(c, d) # a to b to c to d
```

不是这样的：

```python
# WRONG
setTabOrder(c, d) # c to d
setTabOrder(a, b) # a to b AND c to d
setTabOrder(b, c) # a to b to c, but not c to d
```

如果第一个或第二个具有焦点代理，则 setTabOrder() 会正确替换代理。


--------------------------------
## setTabletTracking(enable)

参数：

- enable – bool

属性 tabletTracking 的设置者。


--------------------------------
## setToolTip(arg__1)

参数：

- arg__1 – str

属性 toolTip 的设置者。


--------------------------------
## setToolTipDuration(msec)

参数：

- msec – int

属性 toolTipDuration 的设置者。


--------------------------------
## setUpdatesEnabled(enable)

参数：

- enable – bool

属性 updatesEnabled 的设置者。


--------------------------------
## setVisible(visible)

参数：

- visible – bool

属性的设置者可见。


--------------------------------
## setWhatsThis(arg__1)

参数：

- arg__1 – str

属性 whatsThis 的设置者。


--------------------------------
## setWindowFilePath(filePath)

参数：

- filePath – str

属性 windowFilePath 的设置器。


--------------------------------
## setWindowFlag(arg__1[, on=true])

参数：

- arg__1 – WindowType
- on – bool

如果为真则设置此小部件上的窗口标志flag；否则清除该标志。


--------------------------------
## setWindowFlags(type)

参数：

- type – Combination of WindowType


--------------------------------
## setWindowIcon(icon)

参数：

- icon – QIcon

属性 windowIcon 的设置者。


--------------------------------
## setWindowIconText(arg__1)

参数：

- arg__1 – str

属性 windowIconText 的设置者。


--------------------------------
## setWindowModality(windowModality)

参数：

- windowModality – WindowModality

属性 windowModality 的设置者。


--------------------------------
## setWindowModified(arg__1)

参数：

- arg__1 – bool

属性 windowModified 的设置者。


--------------------------------
## setWindowOpacity(level)

参数：

- level – float


--------------------------------
## setWindowRole(arg__1)

参数：

- arg__1 – str

将窗口的角色设置为 role。这只对 X11 上的窗口有意义。


--------------------------------
## setWindowState(state)

参数：

- state – Combination of WindowState

将窗口状态设置为 windowState。窗口状态是 Qt::WindowState 的 OR 组合：Qt::WindowMinimized、Qt::WindowMaximized、Qt::WindowFullScreen 和 Qt::WindowActive。

如果窗口不可见（即 isVisible() 返回 false），则调用 show() 时窗口状态将生效。对于可见窗口，更改是即时的。例如，要在全屏和正常模式之间切换，请使用以下代码：

```python
w.setWindowState(w.windowState() ^ Qt.WindowFullScreen)
```

要恢复并激活最小化的窗口（同时保留其最大化和/或全屏状态），请使用以下命令：

```python
w.setWindowState((w.windowState()  ~Qt.WindowMinimized) | Qt.WindowActive)
```

调用此函数将隐藏小部件。您必须调用 show() 才能使小部件再次可见。

当窗口状态发生变化时，小部件会收到 QEvent::WindowStateChange 类型的 changeEvent()。


--------------------------------
## setWindowTitle(arg__1)

参数：

- arg__1 – str

属性 windowTitle 的设置者。


--------------------------------
## show()

显示小部件及其子小部件。

对于子窗口，这相当于调用 setVisible (true)。否则，这相当于调用 showFullScreen() 、 showMaximized() 或 setVisible (true)，具体取决于平台对窗口标志的默认行为。


--------------------------------
## showEvent(event)

参数：

- event – QShowEvent

此事件处理程序可以在子类中重新实现，以接收在事件参数中传递的小部件显示事件。

非自发显示事件在小部件显示之前立即发送给小部件。窗口的自发显示事件随后传递。


--------------------------------
## showFullScreen()

以全屏模式显示小部件。

调用此函数仅影响窗口。

要从全屏模式返回，请调用 showNormal() 或 close()。

另一种方法是完全绕过窗口管理器，并使用 Qt::X11BypassWindowManagerHint 标志创建一个窗口。但这还有其他严重问题，例如键盘焦点损坏以及桌面更改或用户调出其他窗口时产生非常奇怪的效果。

遵循现代后 ICCCM 规范的 X11 窗口管理器正确支持全屏模式。

在 macOS 上，全屏显示窗口会使整个应用程序处于全屏模式，为其提供专用桌面。在应用程序以全屏模式运行时显示另一个窗口可能会自动使该窗口也全屏。为防止这种情况，请在显示另一个窗口之前通过调用 showNormal() 或全屏窗口上的 close() 退出全屏模式。


--------------------------------
## showMaximized()

显示最大化的小部件。

调用此函数仅影响窗口。

在 X11 上，此功能可能无法与某些窗口管理器正常工作。请参阅窗口几何文档以了解说明。


--------------------------------
## showMinimized()

将小部件最小化显示为图标。

调用此函数只会影响窗口。


--------------------------------
## showNormal()

在窗口小部件最大化或最小化后恢复它​​。

调用此函数只会影响窗口。


--------------------------------
## size()

返回类型：QSize

属性 size 的获取器。


--------------------------------
## sizeHint()

返回类型：QSize

属性 sizeHint 的获取方法。


--------------------------------
## sizeIncrement()

返回类型：QSize

属性 sizeIncrement 的获取器。


--------------------------------
## sizePolicy()

返回类型：QSizePolicy

属性 sizePolicy 的获取器。


--------------------------------
## stackUnder(arg__1)

参数：

- arg__1 – QWidget

将小部件放置在父小部件堆栈中的 w 下。

要实现此功能，小部件本身和 w 必须是同级。


--------------------------------
## statusTip()

返回类型：str

属性 statusTip 的获取器。


--------------------------------
## style()

返回类型：QStyle


--------------------------------
## styleSheet()

返回类型：str

属性 styleSheet 的获取器。


--------------------------------
## tabletEvent(event)

参数：

- event – QTabletEvent

此事件处理程序（用于事件）可在子类中重新实现，以接收小部件的平板电脑事件。

如果您重新实现此处理程序，则非常重要的是，如果您不处理该事件，则请忽略（）该事件，以便小部件的父级可以解释它。

默认实现将忽略该事件。

如果关闭平板电脑跟踪，则仅当触控笔与平板电脑接触，或者在移动触控笔时按下至少一个触控笔按钮时，才会发生平板电脑移动事件。 如果打开平板电脑跟踪，即使触控笔悬停在平板电脑附近，没有按下任何按钮，也会发生平板电脑移动事件。


--------------------------------
## testAttribute(arg__1)

参数：

- arg__1 – WidgetAttribute

返回类型：bool

如果此小部件上设置了属性，则返回 true；否则返回 false。


--------------------------------
## toolTip()

返回类型：str

属性 toolTip 的获取器。


--------------------------------
## toolTipDuration()

返回类型：int

属性 toolTipDuration 的获取器。


--------------------------------
## topLevelWidget()

返回类型：QWidget

改用 window()。


--------------------------------
## underMouse()

返回类型：bool

如果小部件位于鼠标光标下方，则返回 true；否则返回 false。

在拖放操作期间，此值无法正确更新。


--------------------------------
## ungrabGesture(type)

参数：

- type – GestureType

取消对小部件的给定手势类型的订阅。


--------------------------------
## unsetCursor()

属性光标的重置功能。


--------------------------------
## unsetLayoutDirection()

重置属性layoutDirection的功能。


--------------------------------
## unsetLocale()

属性 locale 的重置功能。


--------------------------------
## update(arg__1)

参数：

- arg__1 – QRegion

这是一个重载函数。

此版本重新绘制小部件内的区域 rgn。


--------------------------------
## update(x, y, w, h)

参数：

- x – int
- y – int
- w – int
- h – int

这是一个重载函数。

此版本更新小部件内的矩形 (x, y, w, h)。


--------------------------------
## update(arg__1)

参数：

- arg__1 – QRect

这是一个重载函数。

此版本更新小部件内的矩形。


--------------------------------
## update()

更新小部件，除非更新被禁用或小部件被隐藏。

此函数不会导致立即重新绘制；相反，它会在 Qt 返回主事件循环时安排绘制事件进行处理。这允许 Qt 优化速度，并减少对 repaint() 的调用所产生的闪烁。

多次调用 update() 通常只会导致一次 paintEvent() 调用。

Qt 通常会在 paintEvent() 调用之前擦除小部件的区域。如果设置了 Qt::WA_OpaquePaintEvent 小部件属性，则小部件负责用不透明颜色绘制其所有像素。


--------------------------------
## updateGeometry()

通知布局系统此小部件已更改，可能需要更改几何形状。

如果 sizeHint() 或 sizePolicy() 已更改，则调用此函数。

对于明确隐藏的小部件，updateGeometry() 为无操作。小部件显示后，布局系统将立即收到通知。


--------------------------------
## updateMicroFocus([query=Qt.ImQueryAll])

参数：

- query – InputMethodQuery

更新小部件的微焦点并通知输入方法查询指定的状态已改变。


--------------------------------
## updatesEnabled()

返回类型：bool

属性 updatesEnabled 的获取器。


--------------------------------
## visibleRegion()

返回类型：QRegion

返回可发生绘制事件的未被遮挡的区域。

对于可见的小部件，这是未被其他小部件覆盖的区域的近似值；否则，这是一个空区域。

repaint() 函数会在必要时调用此函数，因此一般来说您不需要调用它。


--------------------------------
## whatsThis()

返回类型：str

属性 whatsThis 的获取器。


--------------------------------
## wheelEvent(event)

参数：

- event – QWheelEvent

此事件处理程序（用于事件）可在子类中重新实现，以接收小部件的滚轮事件。

如果您重新实现此处理程序，则非常重要的是，如果您不处理该事件，则请忽略（）该事件，以便小部件的父级可以解释它。

默认实现会忽略该事件。


--------------------------------
## winId()

返回类型：WId

返回窗口小部件的窗口系统标识符。

原则上是可移植的，但如果您使用它，您可能要做一些不可移植的事情。请小心。

如果窗口小部件是非本机的（外来）并且在其上调用 winId()，则将为该窗口小部件提供本机句柄。

此值可能会在运行时更改。窗口系统标识符更改后，将向窗口小部件发送类型为 QEvent::WinIdChange 的事件。


--------------------------------
## window()

返回类型：QWidget

返回此小部件的窗口，即具有（或可能具有）窗口系统框架的下一个祖先小部件。

如果小部件是窗口，则返回小部件本身。

典型用法是更改窗口标题：

```python
aWidget.window().setWindowTitle("New Window Title")
```


--------------------------------
## windowFilePath()

返回类型：str

属性 windowFilePath 的获取器。


--------------------------------
## windowFlags()

返回类型：Combination of WindowType


--------------------------------
## windowHandle()

返回类型：QWindow

如果这是本机小部件，则返回关联的 QWindow。否则返回 null。

本机小部件包括顶层小部件、QGLWidget 和调用 winId() 的子小部件。


--------------------------------
## windowIcon()

返回类型：QIcon

属性 windowIcon 的获取器。


--------------------------------
## windowIconChanged(icon)

参数：

- icon – QIcon

当窗口图标发生变化时，将发出此信号，并以新图标作为参数。

属性 windowIcon 的通知信号。


--------------------------------
## windowIconText()

返回类型：str

属性 windowIconText 的获取器。


--------------------------------
## windowIconTextChanged(iconText)

参数：

- iconText – str

当窗口的图标文本发生更改时，将发出此信号，并以新的 iconText 作为参数。

此信号已弃用。

属性 windowIconText 的通知信号。


--------------------------------
## windowModality()

返回类型：WindowModality

属性 windowModality 的获取器。


--------------------------------
## windowOpacity()

返回类型：float


--------------------------------
## windowRole()

返回类型：str

返回窗口的角色，或者一个空字符串。


--------------------------------
## windowState()

返回类型：Combination of WindowState

返回当前窗口状态。窗口状态是 Qt::WindowState：Qt::WindowMinimized、Qt::WindowMaximized、Qt::WindowFullScreen 和 Qt::WindowActive 的或组合。


--------------------------------
## windowTitle()

返回类型：str

属性 windowTitle 的获取器。


--------------------------------
## windowTitleChanged(title)

参数：

- title – str

当窗口标题发生改变时，将发出此信号，并以新标题作为参数。

属性 windowTitle 的通知信号。


--------------------------------
## windowType()

返回类型：WindowType

返回此小部件的窗口类型。这与 windowFlags() 和 Qt::WindowType_Mask 相同。


--------------------------------
## x()

返回类型：int

属性 x 的获取器。


--------------------------------
## y()

返回类型：int

属性 y 的获取者。

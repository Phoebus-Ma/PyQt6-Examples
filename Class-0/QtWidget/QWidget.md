
[Chinese doc](QWidget.CN.md)

# class QWidget

The QWidget class is the base class of all user interface objects.


# Synopsis

## Properties

- [acceptDrops](#property-acceptdrops--bool)

    Whether drop events are enabled for this widget.

- [accessibleDescription](#property-accessibledescription--str)

    The widget’s description as seen by assistive technologies.

- [accessibleName](#property-accessiblename--str)

    The widget’s name as seen by assistive technologies.

- [autoFillBackground](#property-autofillbackground--bool)

    Whether the widget background is filled automatically.

- [baseSize](#property-basesize--qsize)

    The base size of the widget.

- [childrenRect](#property-childrenrect--qrect)

    The bounding rectangle of the widget’s children.

- [childrenRegion](#property-childrenregion--qregion)

    The combined region occupied by the widget’s children.

- [contextMenuPolicy](#property-contextmenupolicy--qtcontextmenupolicy)

    How the widget shows a context menu.

- [cursor](#property-cursor--qcursor)

    The cursor shape for this widget.

- [enabled](#property-enabled--bool)

    Whether the widget is enabled.

- [focus](#property-focus--bool)

    Whether this widget (or its focus proxy) has the keyboard input focus.

- [focusPolicy](#property-focuspolicy--qtfocuspolicy)

    The way the widget accepts keyboard focus.

- [font](#property-font--qfont)

    The font currently set for the widget.

- [frameGeometry](#property-framegeometry--qrect)

    Geometry of the widget relative to its parent including any window frame.

- [frameSize](#property-framesize--qsize)

    The size of the widget including any window frame.

- [fullScreen](#property-fullscreen--bool)

    Whether the widget is shown in full screen mode.

- [geometry](#property-geometry--qrect)

    The geometry of the widget relative to its parent and excluding the window frame.

- [height](#property-height--int)

    The height of the widget excluding any window frame.

- [inputMethodHints](#property-inputmethodhints--combination-of-qtinputmethodhint)

    What input method specific hints the widget has.

- [isActiveWindow](#property-isactivewindow--bool)

    Whether this widget’s window is the active window.

- [layoutDirection](#property-layoutdirection--qtlayoutdirection)

    The layout direction for this widget.

- [locale](#property-locale--qlocale)

    The widget’s locale.

- [maximized](#property-maximized--bool)

    Whether this widget is maximized.

- [maximumHeight](#property-maximumheight--int)

    The widget’s maximum height in pixels.

- [maximumSize](#property-maximumsize--qsize)

    The widget’s maximum size in pixels.

- [maximumWidth](#property-maximumwidth--int)

    The widget’s maximum width in pixels.

- [minimized](#property-minimized--bool)

    Whether this widget is minimized (iconified).

- [minimumHeight](#property-minimumheight--int)

    The widget’s minimum height in pixels.

- [minimumSize](#property-minimumsize--qsize)

    The widget’s minimum size.

- [minimumSizeHint](#property-minimumsizehint--qsize)

    The recommended minimum size for the widget.

- [minimumWidth](#property-minimumwidth--int)

    The widget’s minimum width in pixels.

- [modal](#property-modal--bool)

    Whether the widget is a modal widget.

- [mouseTracking](#property-mousetracking--bool)

    Whether mouse tracking is enabled for the widget.

- [normalGeometry](#property-normalgeometry--qrect)

    The geometry of the widget as it will appear when shown as a normal (not maximized or full screen) top-level widget.

- [palette](#property-palette--qpalette)

    The widget’s palette.

- [pos](#property-pos--qpoint)

    The position of the widget within its parent widget.

- [rect](#property-rect--qrect)

    The internal geometry of the widget excluding any window frame.

- [size](#property-size--qsize)

    The size of the widget excluding any window frame.

- [sizeHint](#property-sizehint--qsize)

    The recommended size for the widget.

- [sizeIncrement](#property-sizeincrement--qsize)

    The size increment of the widget.

- [sizePolicy](#property-sizepolicy--qsizepolicy)

    The default layout behavior of the widget.

- [statusTip](#property-statustip--str)

    The widget’s status tip.

- [styleSheet](#property-stylesheet--str)

    The widget’s style sheet.

- [tabletTracking](#property-tablettracking--bool)

    Whether tablet tracking is enabled for the widget.

- [toolTip](#property-tooltip--str)

    The widget’s tooltip.

- [toolTipDuration](#property-tooltipduration--int)

    The widget’s tooltip duration.

- [updatesEnabled](#property-updatesenabled--bool)

    Whether updates are enabled.

- [visible](#property-visible--bool)

    Whether the widget is visible.

- [whatsThis](#property-whatsthis--str)

    The widget’s What’s This help text.

- [width](#property-width--int)

    The width of the widget excluding any window frame.

- [windowFilePath](#property-windowfilepath--str)

    The file path associated with a widget.

- [windowIcon](#property-windowicon--qicon)

    The widget’s icon.

- [windowIconText](#property-windowicontext--str)

    The text to be displayed on the icon of a minimized window.

- [windowModality](#property-windowmodality--qtwindowmodality)

    Which windows are blocked by the modal widget.

- [windowModified](#property-windowmodified--bool)

    Whether the document shown in the window has unsaved changes.

- [windowOpacity](#property-windowopacity--float)

    Level of opacity for the window.

- [windowTitle](#property-windowtitle--str)

    The window title (caption).

- [x](#property-x--int)

    The x coordinate of the widget relative to its parent including any window frame.

- [y](#property-y--int)

    The y coordinate of the widget relative to its parent and including any window frame.


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

The widget is the atom of the user interface: it receives mouse, keyboard and other events from the window system, and paints a representation of itself on the screen. Every widget is rectangular, and they are sorted in a Z-order. A widget is clipped by its parent and by the widgets in front of it.

A widget that is not embedded in a parent widget is called a window. Usually, windows have a frame and a title bar, although it is also possible to create windows without such decoration using suitable window flags. In Qt, QMainWindow and the various subclasses of QDialog are the most common window types.

Every widget’s constructor accepts one or two standard arguments:

1. QWidget *parent = nullptr is the parent of the new widget. If it is None (the default), the new widget will be a window. If not, it will be a child of parent, and be constrained by parent's geometry (unless you specify Qt::Window as window flag).

2. Qt::WindowFlags f = { } (where available) sets the window flags; the default is suitable for most widgets, but to get, for example, a window without a window system frame, you must use special flags.

QWidget has many member functions, but some of them have little direct functionality; for example, QWidget has a font property, but never uses this itself. There are many subclasses that provide real functionality, such as QLabel , QPushButton , QListWidget , and QTabWidget .


## Top-Level and Child Widgets

A widget without a parent widget is always an independent window (top-level widget). For these widgets, setWindowTitle() and setWindowIcon() set the title bar and icon, respectively.

Non-window widgets are child widgets, displayed within their parent widgets. Most widgets in Qt are mainly useful as child widgets. For example, it is possible to display a button as a top-level window, but most people prefer to put their buttons inside other widgets, such as QDialog .

The diagram above shows a QGroupBox widget being used to hold various child widgets in a layout provided by QGridLayout . The QLabel child widgets have been outlined to indicate their full sizes.

If you want to use a QWidget to hold child widgets, you will usually want to add a layout to the parent QWidget . See Layout Management for more information.


## Composite Widgets

When a widget is used as a container to group a number of child widgets, it is known as a composite widget. These can be created by constructing a widget with the required visual properties - a QFrame , for example - and adding child widgets to it, usually managed by a layout.

Composite widgets can also be created by subclassing a standard widget, such as QWidget or QFrame , and adding the necessary layout and child widgets in the constructor of the subclass. Many of the examples provided with Qt use this approach, and it is also covered in the Qt Widgets Tutorial .


## Custom Widgets and Painting

Since QWidget is a subclass of QPaintDevice, subclasses can be used to display custom content that is composed using a series of painting operations with an instance of the QPainter class. This approach contrasts with the canvas-style approach used by the Graphics View Framework where items are added to a scene by the application and are rendered by the framework itself.

Each widget performs all painting operations from within its paintEvent() function. This is called whenever the widget needs to be redrawn, either because of some external change or when requested by the application.

The Analog Clock example shows how a simple widget can handle paint events.


## Size Hints and Size Policies

When implementing a new widget, it is almost always useful to reimplement sizeHint() to provide a reasonable default size for the widget and to set the correct size policy with setSizePolicy() .

By default, composite widgets that do not provide a size hint will be sized according to the space requirements of their child widgets.

The size policy lets you supply good default behavior for the layout management system, so that other widgets can contain and manage yours easily. The default size policy indicates that the size hint represents the preferred size of the widget, and this is often good enough for many widgets.


## Events

Widgets respond to events that are typically caused by user actions. Qt delivers events to widgets by calling specific event handler functions with instances of QEvent subclasses containing information about each event.

If your widget only contains child widgets, you probably don’t need to implement any event handlers. If you want to detect a mouse click in a child widget, call the child’s underMouse() function inside the widget’s mousePressEvent() .

The Scribble example implements a wider set of events to handle mouse movement, button presses, and window resizing.

You will need to supply the behavior and content for your own widgets, but here is a brief overview of the events that are relevant to QWidget , starting with the most common ones:

- paintEvent() is called whenever the widget needs to be repainted. Every widget displaying custom content must implement it. Painting using a QPainter can only take place in a paintEvent() or a function called by a paintEvent() .

- resizeEvent() is called when the widget has been resized.

- mousePressEvent() is called when a mouse button is pressed while the mouse cursor is inside the widget, or when the widget has grabbed the mouse using grabMouse() . Pressing the mouse without releasing it is effectively the same as calling grabMouse() .

- mouseReleaseEvent() is called when a mouse button is released. A widget receives mouse release events when it has received the corresponding mouse press event. This means that if the user presses the mouse inside your widget, then drags the mouse somewhere else before releasing the mouse button, your widget receives the release event. There is one exception: if a popup menu appears while the mouse button is held down, this popup immediately steals the mouse events.

- mouseDoubleClickEvent() is called when the user double-clicks in the widget. If the user double-clicks, the widget receives a mouse press event, a mouse release event, (a mouse click event,) a second mouse press, this event and finally a second mouse release event. (Some mouse move events may also be received if the mouse is not held steady during this operation.) It is not possible to distinguish a click from a double-click until the second click arrives. (This is one reason why most GUI books recommend that double-clicks be an extension of single-clicks, rather than trigger a different action.)

Widgets that accept keyboard input need to reimplement a few more event handlers:

- keyPressEvent() is called whenever a key is pressed, and again when a key has been held down long enough for it to auto-repeat. The Tab and Shift+Tab keys are only passed to the widget if they are not used by the focus-change mechanisms. To force those keys to be processed by your widget, you must reimplement event() .

- focusInEvent() is called when the widget gains keyboard focus (assuming you have called setFocusPolicy() ). Well-behaved widgets indicate that they own the keyboard focus in a clear but discreet way.

- focusOutEvent() is called when the widget loses keyboard focus.

You may be required to also reimplement some of the less common event handlers:

- mouseMoveEvent() is called whenever the mouse moves while a mouse button is held down. This can be useful during drag and drop operations. If you call setMouseTracking (true), you get mouse move events even when no buttons are held down. (See also the Drag and Drop guide.)

- keyReleaseEvent() is called whenever a key is released and while it is held down (if the key is auto-repeating). In that case, the widget will receive a pair of key release and key press event for every repeat. The Tab and Shift+Tab keys are only passed to the widget if they are not used by the focus-change mechanisms. To force those keys to be processed by your widget, you must reimplement event() .

- wheelEvent() is called whenever the user turns the mouse wheel while the widget has the focus.

- enterEvent() is called when the mouse enters the widget’s screen space. (This excludes screen space owned by any of the widget’s children.)

- leaveEvent() is called when the mouse leaves the widget’s screen space. If the mouse enters a child widget, it will not cause a leaveEvent() .

- moveEvent() is called when the widget has been moved relative to its parent.

- closeEvent() is called when the user closes the widget (or when close() is called).

There are also some rather obscure events described in the documentation for QEvent::Type. To handle these events, you need to reimplement event() directly.

The default implementation of event() handles Tab and Shift+Tab (to move the keyboard focus), and passes on most of the other events to one of the more specialized handlers above.

Events and the mechanism used to deliver them are covered in The Event System.


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

In addition to the standard widget styles for each platform, widgets can also be styled according to rules specified in a style sheet . This feature enables you to customize the appearance of specific widgets to provide visual cues to users about their purpose. For example, a button could be styled in a particular way to indicate that it performs a destructive action.

The use of widget style sheets is described in more detail in the Qt Style Sheets document.


## Transparency and Double Buffering

QWidget automatically double-buffers its painting, so there is no need to write double-buffering code in paintEvent() to avoid flicker.

The contents of parent widgets are propagated by default to each of their children as long as Qt::WA_PaintOnScreen is not set. Custom widgets can be written to take advantage of this feature by updating irregular regions (to create non-rectangular child widgets), or painting with colors that have less than full alpha component. The following diagram shows how attributes and properties of a custom widget can be fine-tuned to achieve different effects.

In the above diagram, a semi-transparent rectangular child widget with an area removed is constructed and added to a parent widget (a QLabel showing a pixmap). Then, different properties and widget attributes are set to achieve different effects:

- The left widget has no additional properties or widget attributes set. This default state suits most custom widgets that have transparency, are irregularly-shaped, or do not paint over their entire area with an opaque brush.

- The center widget has the autoFillBackground property set. This property is used with custom widgets that rely on the widget to supply a default background, and do not paint over their entire area with an opaque brush.

- The right widget has the Qt::WA_OpaquePaintEvent widget attribute set. This indicates that the widget will paint over its entire area with opaque colors. The widget’s area will initially be uninitialized, represented in the diagram with a red diagonal grid pattern that shines through the overpainted area.

To rapidly update custom widgets with simple background colors, such as real-time plotting or graphing widgets, it is better to define a suitable background color (using setBackgroundRole() with the QPalette::Window role), set the autoFillBackground property, and only implement the necessary drawing functionality in the widget’s paintEvent() .

To rapidly update custom widgets that constantly paint over their entire areas with opaque content, for example, video streaming widgets, it is better to set the widget’s Qt::WA_OpaquePaintEvent, avoiding any unnecessary overhead associated with repainting the widget’s background.

If a widget has both the Qt::WA_OpaquePaintEvent widget attribute and the autoFillBackground property set, the Qt::WA_OpaquePaintEvent attribute takes precedence. Depending on your requirements, you should choose either one of them.

The contents of parent widgets are also propagated to standard Qt widgets. This can lead to some unexpected results if the parent widget is decorated in a non-standard way, as shown in the diagram below.

The scope for customizing the painting behavior of standard Qt widgets, without resorting to subclassing, is slightly less than that possible for custom widgets. Usually, the desired appearance of a standard widget can be achieved by setting its autoFillBackground property.


## Creating Translucent Windows

You can create windows with translucent regions on window systems that support compositing.

To enable this feature in a top-level widget, set its Qt::WA_TranslucentBackground attribute with setAttribute() and ensure that its background is painted with non-opaque colors in the regions you want to be partially transparent.

Platform notes:

- X11: This feature relies on the use of an X server that supports ARGB visuals and a compositing window manager.

- Windows: The widget needs to have the Qt::FramelessWindowHint window flag set for the translucency to work.

- macOS: The widget needs to have the Qt::FramelessWindowHint window flag set for the translucency to work.


## Native Widgets vs Alien Widgets

Alien widgets are widgets unknown to the windowing system. They do not have a native window handle associated with them. This feature significantly speeds up widget painting, resizing, and removes flicker.

Should you require the old behavior with native windows, choose one of the following options:

1. Use the QT_USE_NATIVE_WINDOWS=1 in your environment.

2. Set the Qt::AA_NativeWindows attribute on your application. All widgets will be native widgets.

3. Set the Qt::WA_NativeWindow attribute on widgets: The widget itself and all its ancestors will become native (unless Qt::WA_DontCreateNativeAncestors is set).

4. Call winId to enforce a native window (this implies 3).

5. Set the Qt::WA_PaintOnScreen attribute to enforce a native window (this implies 3).


--------------------------------
## class RenderFlag

(inherits enum.Flag) This enum describes how to render the widget when calling render() .

| Constant                     | Description |
| ---------------------------- | ----------- |
| QWidget.DrawWindowBackground | If you enable this option, the widget’s background is rendered into the target even if autoFillBackground is not set. By default, this option is enabled. |
| QWidget.DrawChildren         | If you enable this option, the widget’s children are rendered recursively into the target. By default, this option is enabled. |
| QWidget.IgnoreMask           | If you enable this option, the widget’s mask() is ignored when rendering into the target. By default, this option is disabled. |


--------------------------------
## property acceptDrops : bool

This property holds whether drop events are enabled for this widget.

Setting this property to true announces to the system that this widget may be able to accept drop events.

If the widget is the desktop ( windowType() == Qt::Desktop), this may fail if another application is using the desktop; you can call acceptDrops() to test if this occurs.

By default, this property is false.

Access functions:

- acceptDrops()
- setAcceptDrops()


--------------------------------
## property accessibleDescription : str

This property holds the widget’s description as seen by assistive technologies.

The accessible description of a widget should convey what a widget does. While the accessibleName should be a short and concise string (e.g. Save), the description should give more context, such as Saves the current document.

This property has to be localized.

By default, this property contains an empty string and Qt falls back to using the tool tip to provide this information.

Access functions:

- accessibleDescription()
- setAccessibleDescription()


--------------------------------
## property accessibleName : str

This property holds the widget’s name as seen by assistive technologies.

This is the primary name by which assistive technology such as screen readers announce this widget. For most widgets setting this property is not required. For example for QPushButton the button’s text will be used.

It is important to set this property when the widget does not provide any text. For example a button that only contains an icon needs to set this property to work with screen readers. The name should be short and equivalent to the visual information conveyed by the widget.

This property has to be localized.

By default, this property contains an empty string.

Access functions:

- accessibleName()
- setAccessibleName()


--------------------------------
## property autoFillBackground : bool

This property holds whether the widget background is filled automatically.

If enabled, this property will cause Qt to fill the background of the widget before invoking the paint event. The color used is defined by the QPalette::Window color role from the widget’s palette.

In addition, Windows are always filled with QPalette::Window, unless the WA_OpaquePaintEvent or WA_NoSystemBackground attributes are set.

This property cannot be turned off (i.e., set to false) if a widget’s parent has a static gradient for its background.

By default, this property is false.

Access functions:

- autoFillBackground()
- setAutoFillBackground()


--------------------------------
## property baseSize : QSize

This property holds the base size of the widget.

The base size is used to calculate a proper widget size if the widget defines sizeIncrement() .

By default, for a newly-created widget, this property contains a size with zero width and height.

Access functions:

- baseSize()
- setBaseSize()


--------------------------------
## property childrenRect : QRect

This property holds the bounding rectangle of the widget’s children.

Hidden children are excluded.

By default, for a widget with no children, this property contains a rectangle with zero width and height located at the origin.

Access functions:

- childrenRect()


--------------------------------
## property childrenRegion : QRegion

This property holds the combined region occupied by the widget’s children.

Hidden children are excluded.

By default, for a widget with no children, this property contains an empty region.

Access functions:

- childrenRegion()


--------------------------------
## property contextMenuPolicy : Qt.ContextMenuPolicy

This property holds how the widget shows a context menu.

The default value of this property is Qt::DefaultContextMenu, which means the contextMenuEvent() handler is called. Other values are Qt::NoContextMenu, Qt::PreventContextMenu, Qt::ActionsContextMenu, and Qt::CustomContextMenu. With Qt::CustomContextMenu, the signal customContextMenuRequested() is emitted.

Access functions:

- contextMenuPolicy()
- setContextMenuPolicy()


--------------------------------
## property cursor : QCursor

This property holds the cursor shape for this widget.

The mouse cursor will assume this shape when it’s over this widget. See the list of predefined cursor objects for a range of useful shapes.

An editor widget might use an I-beam cursor:

```python
setCursor(Qt.IBeamCursor)
```

If no cursor has been set, or after a call to unsetCursor(), the parent’s cursor is used.

By default, this property contains a cursor with the Qt::ArrowCursor shape.

Some underlying window implementations will reset the cursor if it leaves a widget even if the mouse is grabbed. If you want to have a cursor set for all widgets, even when outside the window, consider QGuiApplication::setOverrideCursor().

Access functions:

- cursor()
- setCursor()
- unsetCursor()


--------------------------------
## property enabled : bool

This property holds whether the widget is enabled.

In general an enabled widget handles keyboard and mouse events; a disabled widget does not. An exception is made with QAbstractButton .

Some widgets display themselves differently when they are disabled. For example a button might draw its label grayed out. If your widget needs to know when it becomes enabled or disabled, you can use the changeEvent() with type QEvent::EnabledChange.

Disabling a widget implicitly disables all its children. Enabling respectively enables all child widgets unless they have been explicitly disabled. It it not possible to explicitly enable a child widget which is not a window while its parent widget remains disabled.

By default, this property is true.

Access functions:

- isEnabled()
- setEnabled()


--------------------------------
## property focus : bool

This property holds whether this widget (or its focus proxy) has the keyboard input focus.

By default, this property is false.

Access functions:

- hasFocus()


--------------------------------
## property focusPolicy : Qt.FocusPolicy

This property holds the way the widget accepts keyboard focus.

The policy is Qt::TabFocus if the widget accepts keyboard focus by tabbing, Qt::ClickFocus if the widget accepts focus by clicking, Qt::StrongFocus if it accepts both, and Qt::NoFocus (the default) if it does not accept focus at all.

You must enable keyboard focus for a widget if it processes keyboard events. This is normally done from the widget’s constructor. For instance, the QLineEdit constructor calls setFocusPolicy(Qt::StrongFocus).

If the widget has a focus proxy, then the focus policy will be propagated to it.

Access functions:

- focusPolicy()
- setFocusPolicy()


--------------------------------
## property font : QFont

This property holds the font currently set for the widget.

This property describes the widget’s requested font. The font is used by the widget’s style when rendering standard components, and is available as a means to ensure that custom widgets can maintain consistency with the native platform’s look and feel. It’s common that different platforms, or different styles, define different fonts for an application.

When you assign a new font to a widget, the properties from this font are combined with the widget’s default font to form the widget’s final font. You can call fontInfo() to get a copy of the widget’s final font. The final font is also used to initialize QPainter’s font.

The default depends on the system environment. QApplication maintains a system/theme font which serves as a default for all widgets. There may also be special font defaults for certain types of widgets. You can also define default fonts for widgets yourself by passing a custom font and the name of a widget to setFont() . Finally, the font is matched against Qt’s font database to find the best match.

QWidget propagates explicit font properties from parent to child. If you change a specific property on a font and assign that font to a widget, that property will propagate to all the widget’s children, overriding any system defaults for that property. Note that fonts by default don’t propagate to windows (see isWindow() ) unless the Qt::WA_WindowPropagation attribute is enabled.

QWidget ‘s font propagation is similar to its palette propagation.

The current style, which is used to render the content of all standard Qt widgets, is free to choose to use the widget font, or in some cases, to ignore it (partially, or completely). In particular, certain styles like GTK style, Mac style, and Windows Vista style, apply special modifications to the widget font to match the platform’s native look and feel. Because of this, assigning properties to a widget’s font is not guaranteed to change the appearance of the widget. Instead, you may choose to apply a styleSheet .

Access functions:

- font()
- setFont()


--------------------------------
## property frameGeometry : QRect

This property holds geometry of the widget relative to its parent including any window frame.

See the Window Geometry documentation for an overview of geometry issues with windows.

By default, this property contains a value that depends on the user’s platform and screen geometry.

Access functions:

- frameGeometry()


--------------------------------
## property frameSize : QSize

This property holds the size of the widget including any window frame.

By default, this property contains a value that depends on the user’s platform and screen geometry.

Access functions:

- frameSize()


--------------------------------
## property fullScreen : bool

This property holds whether the widget is shown in full screen mode.

A widget in full screen mode occupies the whole screen area and does not display window decorations, such as a title bar.

By default, this property is false.

Access functions:

- isFullScreen()


--------------------------------
## property geometry : QRect

This property holds the geometry of the widget relative to its parent and excluding the window frame.

When changing the geometry, the widget, if visible, receives a move event ( moveEvent() ) and/or a resize event ( resizeEvent() ) immediately. If the widget is not currently visible, it is guaranteed to receive appropriate events before it is shown.

The size component is adjusted if it lies outside the range defined by minimumSize() and maximumSize() .

See the Window Geometry documentation for an overview of geometry issues with windows.

By default, this property contains a value that depends on the user’s platform and screen geometry.

Access functions:

- geometry()
- setGeometry()


--------------------------------
## property height : int

This property holds the height of the widget excluding any window frame.

See the Window Geometry documentation for an overview of geometry issues with windows.

By default, this property contains a value that depends on the user’s platform and screen geometry.

Access functions:


--------------------------------
## property inputMethodHints : Combination of Qt.InputMethodHint

This property holds What input method specific hints the widget has..

This is only relevant for input widgets. It is used by the input method to retrieve hints as to how the input method should operate. For example, if the Qt::ImhFormattedNumbersOnly flag is set, the input method may change its visual components to reflect that only numbers can be entered.


--------------------------------
## The default value is Qt::ImhNone.

Access functions:

- inputMethodHints()
- setInputMethodHints()


--------------------------------
## property isActiveWindow : bool

This property holds whether this widget’s window is the active window.

The active window is the window that contains the widget that has keyboard focus (The window may still have focus if it has no widgets or none of its widgets accepts keyboard focus).

When popup windows are visible, this property is true for both the active window and for the popup.

By default, this property is false.

Access functions:

- isActiveWindow()


--------------------------------
## property layoutDirection : Qt.LayoutDirection

This property holds the layout direction for this widget..

By default, this property is set to Qt::LeftToRight.

When the layout direction is set on a widget, it will propagate to the widget’s children, but not to a child that is a window and not to a child for which setLayoutDirection() has been explicitly called. Also, child widgets added after setLayoutDirection() has been called for the parent do not inherit the parent’s layout direction.

Access functions:

- layoutDirection()
- setLayoutDirection()
- unsetLayoutDirection()


--------------------------------
## property locale : QLocale

This property holds the widget’s locale.

As long as no special locale has been set, this is either the parent’s locale or (if this widget is a top level widget), the default locale.

If the widget displays dates or numbers, these should be formatted using the widget’s locale.

Access functions:

- locale()
- setLocale()
- unsetLocale()


--------------------------------
## property maximized : bool

This property holds whether this widget is maximized.

This property is only relevant for windows.

By default, this property is false.

Access functions:

- isMaximized()


--------------------------------
## property maximumHeight : int

This property holds the widget’s maximum height in pixels.

This property corresponds to the height held by the maximumSize property.

By default, this property contains a value of 16777215.

Access functions:

- maximumHeight()
- setMaximumHeight()


--------------------------------
## property maximumSize : QSize

This property holds the widget’s maximum size in pixels.

The widget cannot be resized to a larger size than the maximum widget size.

By default, this property contains a size in which both width and height have values of 16777215.

Access functions:

- maximumSize()
- setMaximumSize()


--------------------------------
## property maximumWidth : int

This property holds the widget’s maximum width in pixels.

This property corresponds to the width held by the maximumSize property.

By default, this property contains a value of 16777215.

Access functions:

- maximumWidth()
- setMaximumWidth()


--------------------------------
## property minimized : bool

This property holds whether this widget is minimized (iconified).

This property is only relevant for windows.

By default, this property is false.

Access functions:

- isMinimized()


--------------------------------
## property minimumHeight : int

This property holds the widget’s minimum height in pixels.

This property corresponds to the height held by the minimumSize property.

By default, this property has a value of 0.

Access functions:

- minimumHeight()
- setMinimumHeight()


--------------------------------
## property minimumSize : QSize

This property holds the widget’s minimum size.

The widget cannot be resized to a smaller size than the minimum widget size. The widget’s size is forced to the minimum size if the current size is smaller.

The minimum size set by this function will override the minimum size defined by QLayout . To unset the minimum size, use a value of QSize(0, 0).

By default, this property contains a size with zero width and height.

Access functions:

- minimumSize()
- setMinimumSize()


--------------------------------
## property minimumSizeHint : QSize

This property holds the recommended minimum size for the widget.

If the value of this property is an invalid size, no minimum size is recommended.

The default implementation of minimumSizeHint() returns an invalid size if there is no layout for this widget, and returns the layout’s minimum size otherwise. Most built-in widgets reimplement minimumSizeHint().

QLayout will never resize a widget to a size smaller than the minimum size hint unless minimumSize() is set or the size policy is set to QSizePolicy::Ignore. If minimumSize() is set, the minimum size hint will be ignored.

Access functions:

- minimumSizeHint()


--------------------------------
## property minimumWidth : int

This property holds the widget’s minimum width in pixels.

This property corresponds to the width held by the minimumSize property.

By default, this property has a value of 0.

Access functions:

- minimumWidth()
- setMinimumWidth()


--------------------------------
## property modal : bool

This property holds whether the widget is a modal widget.

This property only makes sense for windows. A modal widget prevents widgets in all other windows from getting any input.

By default, this property is false.

Access functions:

- isModal()


--------------------------------
## property mouseTracking : bool

This property holds whether mouse tracking is enabled for the widget.

If mouse tracking is disabled (the default), the widget only receives mouse move events when at least one mouse button is pressed while the mouse is being moved.

If mouse tracking is enabled, the widget receives mouse move events even if no buttons are pressed.

Access functions:

- hasMouseTracking()
- setMouseTracking()


--------------------------------
## property normalGeometry : QRect

This property holds the geometry of the widget as it will appear when shown as a normal (not maximized or full screen) top-level widget.

If the widget is already in this state the normal geometry will reflect the widget’s current geometry() .

For child widgets this property always holds an empty rectangle.

By default, this property contains an empty rectangle.

Access functions:

- normalGeometry()


--------------------------------
## property palette : QPalette

This property holds the widget’s palette.

This property describes the widget’s palette. The palette is used by the widget’s style when rendering standard components, and is available as a means to ensure that custom widgets can maintain consistency with the native platform’s look and feel. It’s common that different platforms, or different styles, have different palettes.

When you assign a new palette to a widget, the color roles from this palette are combined with the widget’s default palette to form the widget’s final palette. The palette entry for the widget’s background role is used to fill the widget’s background (see autoFillBackground ), and the foreground role initializes QPainter’s pen.

The default depends on the system environment. QApplication maintains a system/theme palette which serves as a default for all widgets. There may also be special palette defaults for certain types of widgets (e.g., on Windows Vista, all classes that derive from QMenuBar have a special default palette). You can also define default palettes for widgets yourself by passing a custom palette and the name of a widget to setPalette() . Finally, the style always has the option of polishing the palette as it’s assigned (see polish() ).

QWidget propagates explicit palette roles from parent to child. If you assign a brush or color to a specific role on a palette and assign that palette to a widget, that role will propagate to all the widget’s children, overriding any system defaults for that role. Note that palettes by default don’t propagate to windows (see isWindow() ) unless the Qt::WA_WindowPropagation attribute is enabled.

QWidget ‘s palette propagation is similar to its font propagation.

The current style, which is used to render the content of all standard Qt widgets, is free to choose colors and brushes from the widget palette, or, in some cases, to ignore the palette (partially, or completely). In particular, certain styles like GTK style, Mac style, and Windows Vista style, depend on third party APIs to render the content of widgets, and these styles typically do not follow the palette. Because of this, assigning roles to a widget’s palette is not guaranteed to change the appearance of the widget. Instead, you may choose to apply a styleSheet .

Access functions:

- palette()
- setPalette()


--------------------------------
## property pos : QPoint

This property holds the position of the widget within its parent widget.

If the widget is a window, the position is that of the widget on the desktop, including its frame.

When changing the position, the widget, if visible, receives a move event ( moveEvent() ) immediately. If the widget is not currently visible, it is guaranteed to receive an event before it is shown.

By default, this property contains a position that refers to the origin.

See the Window Geometry documentation for an overview of geometry issues with windows.

Access functions:

- pos()
- move()


--------------------------------
## property rect : QRect

This property holds the internal geometry of the widget excluding any window frame.

The rect property equals QRect(0, 0, width() , height() ).

See the Window Geometry documentation for an overview of geometry issues with windows.

By default, this property contains a value that depends on the user’s platform and screen geometry.

Access functions:

- rect()


--------------------------------
## property size : QSize

This property holds the size of the widget excluding any window frame.

If the widget is visible when it is being resized, it receives a resize event ( resizeEvent() ) immediately. If the widget is not currently visible, it is guaranteed to receive an event before it is shown.

The size is adjusted if it lies outside the range defined by minimumSize() and maximumSize() .

By default, this property contains a value that depends on the user’s platform and screen geometry.

Access functions:

- size()
- resize()


--------------------------------
## property sizeHint : QSize

This property holds the recommended size for the widget.

If the value of this property is an invalid size, no size is recommended.

The default implementation of sizeHint() returns an invalid size if there is no layout for this widget, and returns the layout’s preferred size otherwise.

Access functions:

- sizeHint()


--------------------------------
## property sizeIncrement : QSize

This property holds the size increment of the widget.

When the user resizes the window, the size will move in steps of sizeIncrement(). width() pixels horizontally and sizeIncrement. height() pixels vertically, with baseSize() as the basis. Preferred widget sizes are for non-negative integers i and j:

width = baseSize().width() + i * sizeIncrement().width()
height = baseSize().height() + j * sizeIncrement().height()
Note that while you can set the size increment for all widgets, it only affects windows.

By default, this property contains a size with zero width and height.

Access functions:

- sizeIncrement()
- setSizeIncrement()


--------------------------------
## property sizePolicy : QSizePolicy

This property holds the default layout behavior of the widget.

If there is a QLayout that manages this widget’s children, the size policy specified by that layout is used. If there is no such QLayout , the result of this function is used.

The default policy is Preferred/Preferred, which means that the widget can be freely resized, but prefers to be the size sizeHint() returns. Button-like widgets set the size policy to specify that they may stretch horizontally, but are fixed vertically. The same applies to lineedit controls (such as QLineEdit , QSpinBox or an editable QComboBox ) and other horizontally orientated widgets (such as QProgressBar ). QToolButton ‘s are normally square, so they allow growth in both directions. Widgets that support different directions (such as QSlider , QScrollBar or QHeader) specify stretching in the respective direction only. Widgets that can provide scroll bars (usually subclasses of QScrollArea ) tend to specify that they can use additional space, and that they can make do with less than sizeHint() .

Access functions:

- sizePolicy()
- setSizePolicy()


--------------------------------
## property statusTip : str

This property holds the widget’s status tip.

By default, this property contains an empty string.

Access functions:

- statusTip()
- setStatusTip()


--------------------------------
## property styleSheet : str

This property holds the widget’s style sheet.

The style sheet contains a textual description of customizations to the widget’s style, as described in the Qt Style Sheets document.

Since Qt 4.5, Qt style sheets fully supports macOS.

Access functions:

- styleSheet()
- setStyleSheet()


--------------------------------
## property tabletTracking : bool

This property holds whether tablet tracking is enabled for the widget.

If tablet tracking is disabled (the default), the widget only receives tablet move events when the stylus is in contact with the tablet, or at least one stylus button is pressed, while the stylus is being moved.

If tablet tracking is enabled, the widget receives tablet move events even while hovering in proximity. This is useful for monitoring position as well as the auxiliary properties such as rotation and tilt, and providing feedback in the UI.

Access functions:

- hasTabletTracking()
- setTabletTracking()


--------------------------------
## property toolTip : str

This property holds the widget’s tooltip.

Note that by default tooltips are only shown for widgets that are children of the active window. You can change this behavior by setting the attribute Qt::WA_AlwaysShowToolTips on the window, not on the widget with the tooltip.

If you want to control a tooltip’s behavior, you can intercept the event() function and catch the QEvent::ToolTip event (e.g., if you want to customize the area for which the tooltip should be shown).

By default, this property contains an empty string.

Access functions:

- toolTip()
- setToolTip()


--------------------------------
## property toolTipDuration : int

This property holds the widget’s tooltip duration.

Specifies how long time the tooltip will be displayed, in milliseconds. If the value is -1 (default) the duration is calculated depending on the length of the tooltip.

Access functions:

- toolTipDuration()
- setToolTipDuration()


--------------------------------
## property updatesEnabled : bool

This property holds whether updates are enabled.

An updates enabled widget receives paint events and has a system background; a disabled widget does not. This also implies that calling update() and repaint() has no effect if updates are disabled.

By default, this property is true.

setUpdatesEnabled() is normally used to disable updates for a short period of time, for instance to avoid screen flicker during large changes. In Qt, widgets normally do not generate screen flicker, but on X11 the server might erase regions on the screen when widgets get hidden before they can be replaced by other widgets. Disabling updates solves this.

Example:

```bash
setUpdatesEnabled(False)
bigVisualChanges()
setUpdatesEnabled(True)
```

Disabling a widget implicitly disables all its children. Enabling a widget enables all child widgets except top-level widgets or those that have been explicitly disabled. Re-enabling updates implicitly calls update() on the widget.

Access functions:

- updatesEnabled()
- setUpdatesEnabled()


--------------------------------
## property visible : bool

This property holds whether the widget is visible.

Calling setVisible(true) or show() sets the widget to visible status if all its parent widgets up to the window are visible. If an ancestor is not visible, the widget won’t become visible until all its ancestors are shown. If its size or position has changed, Qt guarantees that a widget gets move and resize events just before it is shown. If the widget has not been resized yet, Qt will adjust the widget’s size to a useful default using adjustSize() .

Calling setVisible(false) or hide() hides a widget explicitly. An explicitly hidden widget will never become visible, even if all its ancestors become visible, unless you show it.

A widget receives show and hide events when its visibility status changes. Between a hide and a show event, there is no need to waste CPU cycles preparing or displaying information to the user. A video application, for example, might simply stop generating new frames.

A widget that happens to be obscured by other windows on the screen is considered to be visible. The same applies to iconified windows and windows that exist on another virtual desktop (on platforms that support this concept). A widget receives spontaneous show and hide events when its mapping status is changed by the window system, e.g. a spontaneous hide event when the user minimizes the window, and a spontaneous show event when the window is restored again.

You seldom have to reimplement the setVisible() function. If you need to change some settings before a widget is shown, use showEvent() instead. If you need to do some delayed initialization use the Polish event delivered to the event() function.

Access functions:

- isVisible()
- setVisible()


--------------------------------
## property whatsThis : str

This property holds the widget’s What’s This help text..

By default, this property contains an empty string.

Access functions:

- whatsThis()
- setWhatsThis()


--------------------------------
## property width : int

This property holds the width of the widget excluding any window frame.

See the Window Geometry documentation for an overview of geometry issues with windows.

By default, this property contains a value that depends on the user’s platform and screen geometry.

Access functions:


--------------------------------
## property windowFilePath : str

This property holds the file path associated with a widget.

This property only makes sense for windows. It associates a file path with a window. If you set the file path, but have not set the window title, Qt sets the window title to the file name of the specified path, obtained using QFileInfo::fileName().

If the window title is set at any point, then the window title takes precedence and will be shown instead of the file path string.

Additionally, on macOS, this has an added benefit that it sets the proxy icon for the window, assuming that the file path exists.

If no file path is set, this property contains an empty string.

By default, this property contains an empty string.

Access functions:

- windowFilePath()
- setWindowFilePath()


--------------------------------
## property windowIcon : QIcon

This property holds the widget’s icon.

This property only makes sense for windows. If no icon has been set, windowIcon() returns the application icon (QApplication::windowIcon()).

Access functions:

- windowIcon()
- setWindowIcon()
- Signal windowIconChanged()


--------------------------------
## property windowIconText : str

This property holds the text to be displayed on the icon of a minimized window.

This property only makes sense for windows. If no icon text has been set, this accessor returns an empty string. It is only implemented on the X11 platform, and only certain window managers use this window property.

This property is deprecated.

Access functions:

- windowIconText()
- setWindowIconText()
- Signal windowIconTextChanged()


--------------------------------
## property windowModality : Qt.WindowModality

This property holds which windows are blocked by the modal widget.

This property only makes sense for windows. A modal widget prevents widgets in other windows from getting input. The value of this property controls which windows are blocked when the widget is visible. Changing this property while the window is visible has no effect; you must hide() the widget first, then show() it again.

By default, this property is Qt::NonModal.

Access functions:

- windowModality()
- setWindowModality()


--------------------------------
## property windowModified : bool

This property holds whether the document shown in the window has unsaved changes.

A modified window is a window whose content has changed but has not been saved to disk. This flag will have different effects varied by the platform. On macOS the close button will have a modified look; on other platforms, the window title will have an ‘*’ (asterisk).

The window title must contain a “[*]” placeholder, which indicates where the ‘*’ should appear. Normally, it should appear right after the file name (e.g., “document1.txt[*] - Text Editor”). If the window isn’t modified, the placeholder is simply removed.

Note that if a widget is set as modified, all its ancestors will also be set as modified. However, if you call setWindowModified(false) on a widget, this will not propagate to its parent because other children of the parent might have been modified.

Access functions:

- isWindowModified()
- setWindowModified()


--------------------------------
## property windowOpacity : float

This property holds The level of opacity for the window..

The valid range of opacity is from 1.0 (completely opaque) to 0.0 (completely transparent).

By default the value of this property is 1.0.

This feature is available on Embedded Linux, macOS, Windows, and X11 platforms that support the Composite extension.

Access functions:

- windowOpacity()
- setWindowOpacity()


--------------------------------
## property windowTitle : str

This property holds the window title (caption).

This property only makes sense for top-level widgets, such as windows and dialogs. If no caption has been set, the title is based of the windowFilePath . If neither of these is set, then the title is an empty string.

If you use the windowModified mechanism, the window title must contain a “[*]” placeholder, which indicates where the ‘*’ should appear. Normally, it should appear right after the file name (e.g., “document1.txt[*] - Text Editor”). If the windowModified property is false (the default), the placeholder is simply removed.

On some desktop platforms (including Windows and Unix), the application name (from QGuiApplication::applicationDisplayName) is added at the end of the window title, if set. This is done by the QPA plugin, so it is shown to the user, but isn’t part of the windowTitle string.

Access functions:

- windowTitle()
- setWindowTitle()
- Signal windowTitleChanged()


--------------------------------
## property x : int

This property holds the x coordinate of the widget relative to its parent including any window frame.

See the Window Geometry documentation for an overview of geometry issues with windows.

By default, this property has a value of 0.

Access functions:

- x()


--------------------------------
## property y : int

This property holds the y coordinate of the widget relative to its parent and including any window frame.

See the Window Geometry documentation for an overview of geometry issues with windows.

By default, this property has a value of 0.

Access functions:

- y()


--------------------------------
## __init__([parent=None[, f=Qt.WindowFlags()]])

Parameters:

- parent – QWidget
- f – Combination of WindowType

Constructs a widget which is a child of parent, with widget flags set to f.

If parent is None, the new widget becomes a window. If parent is another widget, this widget becomes a child window inside parent. The new widget is deleted when its parent is deleted.

The widget flags argument, f, is normally 0, but it can be set to customize the frame of a window (i.e. parent must be None). To customize the frame, use a value composed from the bitwise OR of any of the window flags.

If you add a child widget to an already visible widget you must explicitly show the child to make it visible.

Note that the X11 version of Qt may not be able to deliver all combinations of style flags on all systems. This is because on X11, Qt can only ask the window manager, and the window manager can override the application’s settings. On Windows, Qt can set whatever flags you want.


--------------------------------
## acceptDrops()

Return type: bool

Getter of property acceptDrops  .


--------------------------------
## accessibleDescription()

Return type: str

Getter of property accessibleDescription  .


--------------------------------
## accessibleName()

Return type: str

Getter of property accessibleName  .


--------------------------------
## actionEvent(event)

Parameters:

- event – QActionEvent

This event handler is called with the given event whenever the widget’s actions are changed.


--------------------------------
## actions()

Return type: list of QAction

Returns the (possibly empty) list of this widget’s actions.


--------------------------------
## activateWindow()

Sets the top-level widget containing this widget to be the active window.

An active window is a visible top-level window that has the keyboard input focus.

This function performs the same operation as clicking the mouse on the title bar of a top-level window. On X11, the result depends on the Window Manager. If you want to ensure that the window is stacked on top as well you should also call raise() . Note that the window must be visible, otherwise activateWindow() has no effect.

On Windows, if you are calling this when the application is not currently the active one then it will not make it the active window. It will change the color of the taskbar entry to indicate that the window has changed in some way. This is because Microsoft does not allow an application to interrupt what the user is currently doing in another application.


--------------------------------
## addAction(icon, text, receiver, member[, type=Qt.AutoConnection])

Parameters:

- icon – QIcon
- text – str
- receiver – QObject
- member – str
- type – ConnectionType

Return type: QAction


--------------------------------
addAction(text, receiver, member[, type=Qt.AutoConnection])

Parameters:

- text – str
- receiver – QObject
- member – str
- type – ConnectionType

Return type: QAction


--------------------------------
## addAction(text, shortcut, receiver, member[, type=Qt.AutoConnection])

Parameters:

- text – str
- shortcut – QKeySequence
- receiver – QObject
- member – str
- type – ConnectionType

Return type: QAction


--------------------------------
## addAction(text, shortcut)

Parameters:

- text – str
- shortcut – QKeySequence

Return type: QAction


--------------------------------
## addAction(text)

Parameters:

- text – str

Return type: QAction


--------------------------------
## addAction(icon, text, shortcut, receiver, member[, type=Qt.AutoConnection])

Parameters:

- icon – QIcon
- text – str
- shortcut – QKeySequence
- receiver – QObject
- member – str
- type – ConnectionType

Return type: QAction


--------------------------------
## addAction(icon, text, shortcut)

Parameters:

- icon – QIcon
- text – str
- shortcut – QKeySequence

Return type: QAction


--------------------------------
## addAction(icon, text)

Parameters:

- icon – QIcon
- text – str

Return type: QAction


--------------------------------
## addAction(text, shortcut, callable)

Parameters:

- text – str
- shortcut – QKeySequence
- callable – object

Return type: QAction


--------------------------------
## addAction(text, callable)

Parameters:

- text – str
- callable – object

Return type: QAction


--------------------------------
## addAction(icon, text, shortcut, callable)

Parameters:

- icon – QIcon
- text – str
- shortcut – QKeySequence
- callable – object

Return type: QAction


--------------------------------
## addAction(icon, text, callable)

Parameters:

- icon – QIcon
- text – str
- callable – object

Return type: QAction


--------------------------------
## addAction(action)

Parameters:

- action – QAction

Appends the action action to this widget’s list of actions.

All QWidgets have a list of QActions. However, they can be represented graphically in many different ways. The default use of the QAction list (as returned by actions() ) is to create a context QMenu .

A QWidget should only have one of each action and adding an action it already has will not cause the same action to be in the widget twice.

The ownership of action is not transferred to this QWidget .


--------------------------------
## addActions(actions)

Parameters:

- actions – list of QAction

Appends the actions actions to this widget’s list of actions.


--------------------------------
## adjustSize()

Adjusts the size of the widget to fit its contents.

This function uses sizeHint() if it is valid, i.e., the size hint’s width and height are >= 0. Otherwise, it sets the size to the children rectangle that covers all child widgets (the union of all child widget rectangles).

For windows, the screen size is also taken into account. If the sizeHint() is less than (200, 100) and the size policy is expanding , the window will be at least (200, 100). The maximum size of a window is 2/3 of the screen’s width and height.


--------------------------------
## autoFillBackground()

Return type: bool

Getter of property autoFillBackground  .


--------------------------------
## backgroundRole()

Return type: ColorRole

Returns the background role of the widget.

The background role defines the brush from the widget’s palette that is used to render the background.

If no explicit background role is set, the widget inherits its parent widget’s background role.


--------------------------------
## backingStore()

Return type: QBackingStore

Returns the QBackingStore this widget will be drawn into.


--------------------------------
## baseSize()

Return type: QSize

Getter of property baseSize  .


--------------------------------
## changeEvent(event)

Parameters:

- event – QEvent

This event handler can be reimplemented to handle state changes.

The state being changed in this event can be retrieved through the event supplied.

Change events include: QEvent::ToolBarChange, QEvent::ActivationChange, QEvent::EnabledChange, QEvent::FontChange, QEvent::StyleChange, QEvent::PaletteChange, QEvent::WindowTitleChange, QEvent::IconTextChange, QEvent::ModifiedChange, QEvent::MouseTrackingChange, QEvent::ParentChange, QEvent::WindowStateChange, QEvent::LanguageChange, QEvent::LocaleChange, QEvent::LayoutDirectionChange, QEvent::ReadOnlyChange.


--------------------------------
## childAt(p)

Parameters:

- p – QPoint

Return type: QWidget

This is an overloaded function.

Returns the visible child widget at point p in the widget’s own coordinate system.


--------------------------------
## childAt(x, y)

Parameters:

- x – int
- y – int

Return type: QWidget

Returns the visible child widget at the position (x, y) in the widget’s coordinate system. If there is no visible child widget at the specified position, the function returns None.


--------------------------------
## childrenRect()

Return type: QRect

Getter of property childrenRect  .


--------------------------------
## childrenRegion()

Return type: QRegion

Getter of property childrenRegion  .


--------------------------------
## clearFocus()

Takes keyboard input focus from the widget.

If the widget has active focus, a focus out event is sent to this widget to tell it that it has lost the focus.

This widget must enable focus setting to get the keyboard input focus; that is, it must call setFocusPolicy() .


--------------------------------
## clearMask()

Removes any mask set by setMask() .


--------------------------------
## close()

Return type: bool

Closes this widget. Returns true if the widget was closed; otherwise returns false.

First it sends the widget a QCloseEvent. The widget is hidden if it accepts the close event. If it ignores the event, nothing happens. The default implementation of closeEvent() accepts the close event.

If the widget has the Qt::WA_DeleteOnClose flag, the widget is also deleted. A close events is delivered to the widget no matter if the widget is visible or not.

The QGuiApplication::lastWindowClosed() signal is emitted when the last visible primary window (i.e. window with no parent) with the Qt::WA_QuitOnClose attribute set is closed. By default this attribute is set for all widgets except transient windows such as splash screens, tool windows, and popup menus.


--------------------------------
## closeEvent(event)

Parameters:

- event – QCloseEvent

This event handler is called with the given event when Qt receives a window close request for a top-level widget from the window system.

By default, the event is accepted and the widget is closed. You can reimplement this function to change the way the widget responds to window close requests. For example, you can prevent the window from closing by calling ignore() on all events.

Main window applications typically use reimplementations of this function to check whether the user’s work has been saved and ask for permission before closing.


--------------------------------
## contentsMargins()

Return type:

- QMargins

The contentsMargins function returns the widget’s contents margins.


--------------------------------
## contentsRect()

Return type: QRect

Returns the area inside the widget’s margins.


--------------------------------
## contextMenuEvent(event)

Parameters:

- event – QContextMenuEvent

This event handler, for event event, can be reimplemented in a subclass to receive widget context menu events.

The handler is called when the widget’s contextMenuPolicy is Qt::DefaultContextMenu.

The default implementation ignores the context event. See the QContextMenuEvent documentation for more details.


--------------------------------
## contextMenuPolicy()

Return type: ContextMenuPolicy

Getter of property contextMenuPolicy  .


--------------------------------
## create([arg__1=0[, initializeWindow=true[, destroyOldWindow=true]]])

Parameters:

- arg__1 – WId
- initializeWindow – bool
- destroyOldWindow – bool

Creates a new widget window.

The parameters window, initializeWindow, and destroyOldWindow are ignored in Qt 5. Please use QWindow::fromWinId() to create a QWindow wrapping a foreign window and pass it to createWindowContainer() instead.


--------------------------------
## createWinId()
## static createWindowContainer(window[, parent=None[, flags=Qt.WindowFlags()]])

Parameters:

- window – QWindow
- parent – QWidget
- flags – Combination of WindowType

Return type: QWidget

Creates a QWidget that makes it possible to embed window into a QWidget -based application.

The window container is created as a child of parent and with window flags flags.

Once the window has been embedded into the container, the container will control the window’s geometry and visibility. Explicit calls to QWindow::setGeometry(), QWindow::show() or QWindow::hide() on an embedded window is not recommended.

The container takes over ownership of window. The window can be removed from the window container with a call to QWindow::setParent().

The window container is attached as a native child window to the toplevel window it is a child of. When a window container is used as a child of a QAbstractScrollArea or QMdiArea , it will create a native window for every widget in its parent chain to allow for proper stacking and clipping in this use case. Creating a native window for the window container also allows for proper stacking and clipping. This must be done before showing the window container. Applications with many native child windows may suffer from performance issues.

The window container has a number of known limitations:

Stacking order; The embedded window will stack on top of the widget hierarchy as an opaque box. The stacking order of multiple overlapping window container instances is undefined.

Rendering Integration; The window container does not interoperate with QGraphicsProxyWidget , render() or similar functionality.

Focus Handling; It is possible to let the window container instance have any focus policy and it will delegate focus to the window via a call to QWindow::requestActivate(). However, returning to the normal focus chain from the QWindow instance will be up to the QWindow instance implementation itself. For instance, when entering a Qt Quick based window with tab focus, it is quite likely that further tab presses will only cycle inside the QML application. Also, whether QWindow::requestActivate() actually gives the window focus, is platform dependent.

Using many window container instances in a QWidget -based application can greatly hurt the overall performance of the application.

Since 6.7, if window belongs to a widget (that is, window was received from calling windowHandle() ), no container will be created. Instead, this function will return the widget itself, after being reparented to parent. Since no container will be created, flags will be ignored. In other words, if window belongs to a widget, consider just reparenting that widget to parent instead of using this function.


--------------------------------
## cursor()

Return type: QCursor

Getter of property cursor  .


--------------------------------
## customContextMenuRequested(pos)

Parameters:

- pos – QPoint

This signal is emitted when the widget’s contextMenuPolicy is Qt::CustomContextMenu, and the user has requested a context menu on the widget. The position pos is the position of the context menu event that the widget receives. Normally this is in widget coordinates. The exception to this rule is QAbstractScrollArea and its subclasses that map the context menu event to coordinates of the viewport() .


--------------------------------
## destroy([destroyWindow=true[, destroySubWindows=true]])

Parameters:

- destroyWindow – bool
- destroySubWindows – bool

Frees up window system resources. Destroys the widget window if destroyWindow is true.

destroy() calls itself recursively for all the child widgets, passing destroySubWindows for the destroyWindow parameter. To have more control over destruction of subwidgets, destroy subwidgets selectively first.

This function is usually called from the QWidget destructor.


--------------------------------
## dragEnterEvent(event)

Parameters:

- event – QDragEnterEvent

This event handler is called when a drag is in progress and the mouse enters this widget. The event is passed in the event parameter.

If the event is ignored, the widget won’t receive any drag move events .

See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.


--------------------------------
## dragLeaveEvent(event)

Parameters:

- event – QDragLeaveEvent

This event handler is called when a drag is in progress and the mouse leaves this widget. The event is passed in the event parameter.

See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.


--------------------------------
## dragMoveEvent(event)

Parameters:

- event – QDragMoveEvent

This event handler is called if a drag is in progress, and when any of the following conditions occur: the cursor enters this widget, the cursor moves within this widget, or a modifier key is pressed on the keyboard while this widget has the focus. The event is passed in the event parameter.

See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.


--------------------------------
## dropEvent(event)

Parameters:

- event – QDropEvent

This event handler is called when the drag is dropped on this widget. The event is passed in the event parameter.

See the Drag-and-drop documentation for an overview of how to provide drag-and-drop in your application.


--------------------------------
## effectiveWinId()

Return type: WId

Returns the effective window system identifier of the widget, i.e. the native parent’s window system identifier.

If the widget is native, this function returns the native widget ID. Otherwise, the window ID of the first native parent widget, i.e., the top-level widget that contains this widget, is returned.


--------------------------------
## ensurePolished()

Ensures that the widget and its children have been polished by QStyle (i.e., have a proper font and palette).

QWidget calls this function after it has been fully constructed but before it is shown the very first time. You can call this function if you want to ensure that the widget is polished before doing an operation, e.g., the correct font size might be needed in the widget’s sizeHint() reimplementation. Note that this function is called from the default implementation of sizeHint() .

Polishing is useful for final initialization that must happen after all constructors (from base classes as well as from subclasses) have been called.

If you need to change some settings when a widget is polished, reimplement event() and handle the QEvent::Polish event type.


--------------------------------
## enterEvent(event)

Parameters:

- event – QEnterEvent

This event handler can be reimplemented in a subclass to receive widget enter events which are passed in the event parameter.

An event is sent to the widget when the mouse cursor enters the widget.


--------------------------------
## static find(arg__1)

Parameters:

- arg__1 – WId

Return type: QWidget

Returns a pointer to the widget with window identifier/handle id.

The window identifier type depends on the underlying window system, see qwindowdefs.h for the actual definition. If there is no widget with this identifier, None is returned.


--------------------------------
## focusInEvent(event)

Parameters:

- event – QFocusEvent

This event handler can be reimplemented in a subclass to receive keyboard focus events (focus received) for the widget. The event is passed in the event parameter

A widget normally must setFocusPolicy() to something other than Qt::NoFocus to receive focus events. (Note that the application programmer can call setFocus() on any widget, even those that do not normally accept focus.)

The default implementation updates the widget (except for windows that do not specify a focusPolicy() ).


--------------------------------
## focusNextChild()

Return type: bool

Finds a new widget to give the keyboard focus to, as appropriate for Tab, and returns true if it can find a new widget, or false if it can’t.


--------------------------------
## focusNextPrevChild(next)

Parameters:

- next – bool

Return type: bool

Finds a new widget to give the keyboard focus to, as appropriate for Tab and Shift+Tab, and returns true if it can find a new widget, or false if it can’t.

If next is true, this function searches forward, if next is false, it searches backward.

Sometimes, you will want to reimplement this function. For example, a web browser might reimplement it to move its “current active link” forward or backward, and call focusNextPrevChild() only when it reaches the last or first link on the “page”.

Child widgets call focusNextPrevChild() on their parent widgets, but only the window that contains the child widgets decides where to redirect focus. By reimplementing this function for an object, you thus gain control of focus traversal for all child widgets.


--------------------------------
## focusOutEvent(event)

Parameters:

- event – QFocusEvent

This event handler can be reimplemented in a subclass to receive keyboard focus events (focus lost) for the widget. The events is passed in the event parameter.

A widget normally must setFocusPolicy() to something other than Qt::NoFocus to receive focus events. (Note that the application programmer can call setFocus() on any widget, even those that do not normally accept focus.)

The default implementation updates the widget (except for windows that do not specify a focusPolicy() ).


--------------------------------
## focusPolicy()

Return type: FocusPolicy

Getter of property focusPolicy  .


--------------------------------
## focusPreviousChild()

Return type: bool

Finds a new widget to give the keyboard focus to, as appropriate for Shift+Tab, and returns true if it can find a new widget, or false if it can’t.


--------------------------------
## focusProxy()

Return type: QWidget

Returns the focus proxy, or None if there is no focus proxy.


--------------------------------
## focusWidget()

Return type: QWidget

Returns the last child of this widget that setFocus had been called on. For top level widgets this is the widget that will get focus in case this window gets activated

This is not the same as focusWidget() , which returns the focus widget in the currently active window.


--------------------------------
## font()

Return type: QFont

Getter of property font  .


--------------------------------
## fontInfo()

Return type: QFontInfo

Returns the font info for the widget’s current font. Equivalent to QFontInfo(widget->font()).


--------------------------------
## fontMetrics()

Return type: QFontMetrics

Returns the font metrics for the widget’s current font. Equivalent to QFontMetrics(widget->font()).


--------------------------------
## foregroundRole()

Return type: ColorRole

Returns the foreground role.

The foreground role defines the color from the widget’s palette that is used to draw the foreground.

If no explicit foreground role is set, the function returns a role that contrasts with the background role.


--------------------------------
## frameGeometry()

Return type: QRect

Getter of property frameGeometry  .


--------------------------------
## frameSize()

Return type: QSize

Getter of property frameSize  .


--------------------------------
## geometry()

Return type: QRect

Getter of property geometry  .


--------------------------------
## grab([rectangle=QRect(QPoint(0, 0), QSize(-1, -1))])

Parameters:

- rectangle – QRect

Return type: QPixmap

Renders the widget into a pixmap restricted by the given rectangle. If the widget has any children, then they are also painted in the appropriate positions.

If a rectangle with an invalid size is specified (the default), the entire widget is painted.


--------------------------------
## grabGesture(type[, flags=Qt.GestureFlags()])

Parameters:

- type – GestureType
- flags – Combination of GestureFlag

Subscribes the widget to a given gesture with specific flags.


--------------------------------
## grabKeyboard()

Grabs the keyboard input.

This widget receives all keyboard events until releaseKeyboard() is called; other widgets get no keyboard events at all. Mouse events are not affected. Use grabMouse() if you want to grab that.

The focus widget is not affected, except that it doesn’t receive any keyboard events. setFocus() moves the focus as usual, but the new focus widget receives keyboard events only after releaseKeyboard() is called.

If a different widget is currently grabbing keyboard input, that widget’s grab is released first.


--------------------------------
## grabMouse()

Grabs the mouse input.

This widget receives all mouse events until releaseMouse() is called; other widgets get no mouse events at all. Keyboard events are not affected. Use grabKeyboard() if you want to grab that.

It is seldom necessary to grab the mouse when using Qt, as Qt grabs and releases it sensibly. In particular, Qt grabs the mouse when a mouse button is pressed and keeps it until the last button is released.


--------------------------------
## grabMouse(arg__1)

Parameters:

- arg__1 – QCursor

This function overloads grabMouse() .

Grabs the mouse input and changes the cursor shape.

The cursor will assume shape cursor (for as long as the mouse focus is grabbed) and this widget will be the only one to receive mouse events until releaseMouse() is called().


--------------------------------
## grabShortcut(key[, context=Qt.WindowShortcut])

Parameters:

- key – QKeySequence
- context – ShortcutContext

Return type: int

Adds a shortcut to Qt’s shortcut system that watches for the given key sequence in the given context. If the context is Qt::ApplicationShortcut, the shortcut applies to the application as a whole. Otherwise, it is either local to this widget, Qt::WidgetShortcut, or to the window itself, Qt::WindowShortcut.

If the same key sequence has been grabbed by several widgets, when the key sequence occurs a QEvent::Shortcut event is sent to all the widgets to which it applies in a non-deterministic order, but with the ``ambiguous’’ flag set to true.


--------------------------------
## graphicsEffect()

Return type: QGraphicsEffect

The graphicsEffect function returns a pointer to the widget’s graphics effect.

If the widget has no graphics effect, None is returned.


--------------------------------
## graphicsProxyWidget()

Return type: QGraphicsProxyWidget

Returns the proxy widget for the corresponding embedded widget in a graphics view; otherwise returns None.


--------------------------------
## hasFocus()

Return type: bool

Getter of property focus  .


--------------------------------
## hasHeightForWidth()

Return type: bool

Returns true if the widget’s preferred height depends on its width; otherwise returns false.


--------------------------------
## hasMouseTracking()

Return type: bool

Getter of property mouseTracking  .


--------------------------------
## hasTabletTracking()

Return type: bool

Getter of property tabletTracking  .


--------------------------------
## heightForWidth(arg__1)

Parameters:

- arg__1 – int

Return type: int

Returns the preferred height for this widget, given the width w.

If this widget has a layout, the default implementation returns the layout’s preferred height. if there is no layout, the default implementation returns -1 indicating that the preferred height does not depend on the width.


--------------------------------
## hide()

Hides the widget. This function is equivalent to setVisible (false).


--------------------------------
## hideEvent(event)

Parameters:

- event – QHideEvent

This event handler can be reimplemented in a subclass to receive widget hide events. The event is passed in the event parameter.

Hide events are sent to widgets immediately after they have been hidden.


--------------------------------
## inputMethodEvent(event)

Parameters:

- event – QInputMethodEvent

This event handler, for event event, can be reimplemented in a subclass to receive Input Method composition events. This handler is called when the state of the input method changes.

Note that when creating custom text editing widgets, the Qt::WA_InputMethodEnabled window attribute must be set explicitly (using the setAttribute() function) in order to receive input method events.

The default implementation calls event->ignore(), which rejects the Input Method event. See the QInputMethodEvent documentation for more details.


--------------------------------
## inputMethodHints()

Return type: Combination of InputMethodHint

Getter of property inputMethodHints  .


--------------------------------
## inputMethodQuery(arg__1)

Parameters:

- arg__1 – InputMethodQuery

Return type: object

This method is only relevant for input widgets. It is used by the input method to query a set of properties of the widget to be able to support complex input method operations as support for surrounding text and reconversions.

query specifies which property is queried.


--------------------------------
## insertAction(before, action)

Parameters:

- before – QAction
- action – QAction

Inserts the action action to this widget’s list of actions, before the action before. It appends the action if before is None or before is not a valid action for this widget.

A QWidget should only have one of each action.


--------------------------------
## insertActions(before, actions)

Parameters:

- before – QAction
- actions – .list of QAction

Inserts the actions actions to this widget’s list of actions, before the action before. It appends the action if before is None or before is not a valid action for this widget.

A QWidget can have at most one of each action.


--------------------------------
## internalWinId()

Return type: WId


--------------------------------
## isActiveWindow()

Return type: bool

Getter of property isActiveWindow  .


--------------------------------
## isAncestorOf(child)

Parameters:

- child – QWidget

Return type: bool

Returns true if this widget is a parent, (or grandparent and so on to any level), of the given child, and both widgets are within the same window; otherwise returns false.


--------------------------------
## isEnabled()

Return type: bool

Getter of property enabled  .


--------------------------------
## isEnabledTo(arg__1)

Parameters:

- arg__1 – QWidget

Return type: bool

Returns true if this widget would become enabled if ancestor is enabled; otherwise returns false.

This is the case if neither the widget itself nor every parent up to but excluding ancestor has been explicitly disabled.

isEnabledTo(0) returns false if this widget or any if its ancestors was explicitly disabled.

The word ancestor here means a parent widget within the same window.

Therefore isEnabledTo(0) stops at this widget’s window, unlike isEnabled() which also takes parent windows into considerations.


--------------------------------
## isFullScreen()

Return type: bool

Getter of property fullScreen  .


--------------------------------
## isHidden()

Return type: bool

Returns true if the widget is hidden, otherwise returns false.

A hidden widget will only become visible when show() is called on it. It will not be automatically shown when the parent is shown.

To check visibility, use ! isVisible() instead (notice the exclamation mark).

isHidden() implies ! isVisible() , but a widget can be not visible and not hidden at the same time. This is the case for widgets that are children of widgets that are not visible.

Widgets are hidden if:

- they were created as independent windows,
- they were created as children of visible widgets,
- hide() or setVisible (false) was called.


--------------------------------
## isLeftToRight()

Return type: bool


--------------------------------
##  isMaximized()

Return type: bool

Getter of property maximized  .


--------------------------------
## isMinimized()

Return type: bool

Getter of property minimized  .


--------------------------------
## isModal()

Return type: bool

Getter of property modal  .


--------------------------------
## isRightToLeft()

Return type: bool


--------------------------------
## isTopLevel()

Return type: bool

Use isWindow() instead.


--------------------------------
## isVisible()

Return type: bool

Getter of property visible  .


--------------------------------
## isVisibleTo(arg__1)

Parameters:

- arg__1 – QWidget

Return type: bool

Returns true if this widget would become visible if ancestor is shown; otherwise returns false.

The true case occurs if neither the widget itself nor any parent up to but excluding ancestor has been explicitly hidden.

This function will still return true if the widget is obscured by other windows on the screen, but could be physically visible if it or they were to be moved.

isVisibleTo(0) is identical to isVisible() .


--------------------------------
## isWindow()

Return type: bool

Returns true if the widget is an independent window, otherwise returns false.

A window is a widget that isn’t visually the child of any other widget and that usually has a frame and a window title .

A window can have a parent widget . It will then be grouped with its parent and deleted when the parent is deleted, minimized when the parent is minimized etc. If supported by the window manager, it will also have a common taskbar entry with its parent.

QDialog and QMainWindow widgets are by default windows, even if a parent widget is specified in the constructor. This behavior is specified by the Qt::Window flag.


--------------------------------
## isWindowModified()

Return type: bool

Getter of property windowModified  .


--------------------------------
## keyPressEvent(event)

Parameters:

- event – QKeyEvent

This event handler, for event event, can be reimplemented in a subclass to receive key press events for the widget.

A widget must call setFocusPolicy() to accept focus initially and have focus in order to receive a key press event.

If you reimplement this handler, it is very important that you call the base class implementation if you do not act upon the key.

The default implementation closes popup widgets if the user presses the key sequence for QKeySequence::Cancel (typically the Escape key). Otherwise the event is ignored, so that the widget’s parent can interpret it.

Note that QKeyEvent starts with isAccepted() == true, so you do not need to call QKeyEvent::accept() - just do not call the base class implementation if you act upon the key.


--------------------------------
## keyReleaseEvent(event)

Parameters:

- event – QKeyEvent

This event handler, for event event, can be reimplemented in a subclass to receive key release events for the widget.

A widget must accept focus initially and have focus in order to receive a key release event.

If you reimplement this handler, it is very important that you call the base class implementation if you do not act upon the key.

The default implementation ignores the event, so that the widget’s parent can interpret it.

Note that QKeyEvent starts with isAccepted() == true, so you do not need to call QKeyEvent::accept() - just do not call the base class implementation if you act upon the key.


--------------------------------
## static keyboardGrabber()

Return type: QWidget

Returns the widget that is currently grabbing the keyboard input.

If no widget in this application is currently grabbing the keyboard, None is returned.


--------------------------------
## layout()

Return type: QLayout

Returns the layout manager that is installed on this widget, or None if no layout manager is installed.

The layout manager sets the geometry of the widget’s children that have been added to the layout.


--------------------------------
## layoutDirection()

Return type: LayoutDirection

Getter of property layoutDirection  .


--------------------------------
## leaveEvent(event)

Parameters:

- event – QEvent

This event handler can be reimplemented in a subclass to receive widget leave events which are passed in the event parameter.

A leave event is sent to the widget when the mouse cursor leaves the widget.


--------------------------------
## locale()

Return type: QLocale

Getter of property locale  .


--------------------------------
## lower()

Lowers the widget to the bottom of the parent widget’s stack.

After this call the widget will be visually behind (and therefore obscured by) any overlapping sibling widgets.


--------------------------------
## mapFrom(arg__1, arg__2)

Parameters:

- arg__1 – QWidget
- arg__2 – QPoint

Return type: QPoint

This is an overloaded function.


--------------------------------
## mapFrom(arg__1, arg__2)

Parameters:

- arg__1 – QWidget
- arg__2 – QPointF

Return type: QPointF

Translates the widget coordinate pos from the coordinate system of parent to this widget’s coordinate system. The parent must not be None and must be a parent of the calling widget.


--------------------------------
## mapFromGlobal(arg__1)

Parameters:

- arg__1 – QPoint

Return type: QPoint

This is an overloaded function.


--------------------------------
## mapFromGlobal(arg__1)

Parameters:

- arg__1 – QPointF

Return type: QPointF

Translates the global screen coordinate pos to widget coordinates.


--------------------------------
## mapFromParent(arg__1)

Parameters:

- arg__1 – QPoint

Return type: QPoint

This is an overloaded function.


--------------------------------
## mapFromParent(arg__1)

Parameters:

- arg__1 – QPointF

Return type: QPointF

Translates the parent widget coordinate pos to widget coordinates.

Same as mapFromGlobal() if the widget has no parent.


--------------------------------
## mapTo(arg__1, arg__2)

Parameters:

- arg__1 – QWidget
- arg__2 – QPoint

Return type: QPoint

This is an overloaded function.


--------------------------------
## mapTo(arg__1, arg__2)

Parameters:

- arg__1 – QWidget
- arg__2 – QPointF

Return type: QPointF

Translates the widget coordinate pos to the coordinate system of parent. The parent must not be None and must be a parent of the calling widget.


--------------------------------
## mapToGlobal(arg__1)

Parameters:

- arg__1 – QPoint

Return type: QPoint

This is an overloaded function.


--------------------------------
## mapToGlobal(arg__1)

Parameters:

- arg__1 – QPointF

Return type: QPointF

Translates the widget coordinate pos to global screen coordinates. For example, mapToGlobal(QPointF(0,0)) would give the global coordinates of the top-left pixel of the widget.


--------------------------------
## mapToParent(arg__1)

Parameters:

- arg__1 – QPointF

Return type: QPointF

Translates the widget coordinate pos to a coordinate in the parent widget.

Same as mapToGlobal() if the widget has no parent.


--------------------------------
## mapToParent(arg__1)

Parameters:

- arg__1 – QPoint

Return type: QPoint

This is an overloaded function.


--------------------------------
## mask()

Return type: QRegion

Returns the mask currently set on a widget. If no mask is set the return value will be an empty region.


--------------------------------
## maximumHeight()

Return type: int

Getter of property maximumHeight  .


--------------------------------
## maximumSize()

Return type: QSize

Getter of property maximumSize  .


--------------------------------
## maximumWidth()

Return type: int

Getter of property maximumWidth  .


--------------------------------
## minimumHeight()

Return type: int

Getter of property minimumHeight  .


--------------------------------
## minimumSize()

Return type: QSize

Getter of property minimumSize  .


--------------------------------
## minimumSizeHint()

Return type: QSize

Getter of property minimumSizeHint  .


--------------------------------
## minimumWidth()

Return type: int

Getter of property minimumWidth  .


--------------------------------
## mouseDoubleClickEvent(event)

Parameters:

- event – QMouseEvent

This event handler, for event event, can be reimplemented in a subclass to receive mouse double click events for the widget.

The default implementation calls mousePressEvent() .


--------------------------------
## static mouseGrabber()

Return type: QWidget

Returns the widget that is currently grabbing the mouse input.

If no widget in this application is currently grabbing the mouse, None is returned.


--------------------------------
## mouseMoveEvent(event)

Parameters:

- event – QMouseEvent

This event handler, for event event, can be reimplemented in a subclass to receive mouse move events for the widget.

If mouse tracking is switched off, mouse move events only occur if a mouse button is pressed while the mouse is being moved. If mouse tracking is switched on, mouse move events occur even if no mouse button is pressed.

QMouseEvent::pos() reports the position of the mouse cursor, relative to this widget. For press and release events, the position is usually the same as the position of the last mouse move event, but it might be different if the user’s hand shakes. This is a feature of the underlying window system, not Qt.

If you want to show a tooltip immediately, while the mouse is moving (e.g., to get the mouse coordinates with QMouseEvent::pos() and show them as a tooltip), you must first enable mouse tracking as described above. Then, to ensure that the tooltip is updated immediately, you must call showText() instead of setToolTip() in your implementation of mouseMoveEvent().


--------------------------------
## mousePressEvent(event)

Parameters:

- event – QMouseEvent

This event handler, for event event, can be reimplemented in a subclass to receive mouse press events for the widget.

If you create new widgets in the mousePressEvent() the mouseReleaseEvent() may not end up where you expect, depending on the underlying window system (or X11 window manager), the widgets’ location and maybe more.

The default implementation implements the closing of popup widgets when you click outside the window. For other widget types it does nothing.


--------------------------------
## mouseReleaseEvent(event)

Parameters:

- event – QMouseEvent

This event handler, for event event, can be reimplemented in a subclass to receive mouse release events for the widget.


--------------------------------
## move(arg__1)

Parameters:

- arg__1 – QPoint

Setter of property pos  .


--------------------------------
## move(x, y)

Parameters:

- x – int
- y – int

This is an overloaded function.

This corresponds to move(QPoint(x, y)).


--------------------------------
## moveEvent(event)

Parameters:

- event – QMoveEvent

This event handler can be reimplemented in a subclass to receive widget move events which are passed in the event parameter. When the widget receives this event, it is already at the new position.

The old position is accessible through QMoveEvent::oldPos().


--------------------------------
## nativeEvent(eventType, message)

Parameters:

- eventType – QByteArray
- message – void

Return type: PyObject

This special event handler can be reimplemented in a subclass to receive native platform events identified by eventType which are passed in the message parameter.

In your reimplementation of this function, if you want to stop the event being handled by Qt, return true and set result. The result parameter has meaning only on Windows. If you return false, this native event is passed back to Qt, which translates the event into a Qt event and sends it to the widget.

| Platform | Event Type Identifier | Message Type | Result Type |
| -------- | --------------------- | ------------ | ----------- |
| Windows  | “windows_generic_MSG” | MSG *        | LRESULT     |
| macOS    | “NSEvent”             | NSEvent *    |             |
| XCB      | “xcb_generic_event_t” | xcb_generic_event_t * |    |


--------------------------------
## nativeParentWidget()

Return type: QWidget

Returns the native parent for this widget, i.e. the next ancestor widget that has a system identifier, or None if it does not have any native parent.


--------------------------------
## nextInFocusChain()

Return type: QWidget

Returns the next widget in this widget’s focus chain.


--------------------------------
## normalGeometry()

Return type: QRect

Getter of property normalGeometry  .


--------------------------------
## overrideWindowFlags(type)

Parameters:

- type – Combination of WindowType

Sets the window flags for the widget to flags, without telling the window system.


--------------------------------
## overrideWindowState(state)

Parameters:

- state – Combination of WindowState


--------------------------------
## paintEvent(event)

Parameters:

- event – QPaintEvent

This event handler can be reimplemented in a subclass to receive paint events passed in event.

A paint event is a request to repaint all or part of a widget. It can happen for one of the following reasons:

repaint() or update() was invoked,

the widget was obscured and has now been uncovered, or

many other reasons.

Many widgets can simply repaint their entire surface when asked to, but some slow widgets need to optimize by painting only the requested region: QPaintEvent::region(). This speed optimization does not change the result, as painting is clipped to that region during event processing. QListView and QTableView do this, for example.

Qt also tries to speed up painting by merging multiple paint events into one. When update() is called several times or the window system sends several paint events, Qt merges these events into one event with a larger region (see QRegion::united()). The repaint() function does not permit this optimization, so we suggest using update() whenever possible.

When the paint event occurs, the update region has normally been erased, so you are painting on the widget’s background.

The background can be set using setBackgroundRole() and setPalette() .

Since Qt 4.0, QWidget automatically double-buffers its painting, so there is no need to write double-buffering code in paintEvent() to avoid flicker.


--------------------------------
## palette()

Return type: QPalette

Getter of property palette  .


--------------------------------
## parentWidget()

Return type: QWidget

Returns the parent of this widget, or None if it does not have any parent widget.


--------------------------------
## pos()

Return type: QPoint

Getter of property pos  .


--------------------------------
## previousInFocusChain()

Return type: QWidget

The previousInFocusChain function returns the previous widget in this widget’s focus chain.


--------------------------------
## raise_()
## rect()

Return type: QRect

Getter of property rect  .


--------------------------------
## releaseKeyboard()

Releases the keyboard grab.


--------------------------------
## releaseMouse()

Releases the mouse grab.


--------------------------------
## releaseShortcut(id)

Parameters:

- id – int

Removes the shortcut with the given id from Qt’s shortcut system. The widget will no longer receive QEvent::Shortcut events for the shortcut’s key sequence (unless it has other shortcuts with the same key sequence).


--------------------------------
## removeAction(action)

Parameters:

- action – QAction

Removes the action action from this widget’s list of actions.


--------------------------------
## render(target[, targetOffset=QPoint()[, sourceRegion=QRegion()[, renderFlags=QWidget.RenderFlags(QWidget.RenderFlag.DrawWindowBackground | QWidget.RenderFlag.DrawChildren)]]])

Parameters:

- target – QPaintDevice
- targetOffset – QPoint
- sourceRegion – QRegion
- renderFlags – Combination of RenderFlag


Renders the sourceRegion of this widget into the target using renderFlags to determine how to render. Rendering starts at targetOffset in the target. For example:

```python
pixmap = QPixmap(widget.size())
widget.render(pixmap)
```

If sourceRegion is a null region, this function will use rect() as the region, i.e. the entire widget.

Ensure that you call QPainter::end() for the target device’s active painter (if any) before rendering. For example:

```python
painter = QPainter(self)
...
painter.end()
myWidget.render(self)
```


--------------------------------
## render(painter, targetOffset[, sourceRegion=QRegion()[, renderFlags=QWidget.RenderFlags(QWidget.RenderFlag.DrawWindowBackground | QWidget.RenderFlag.DrawChildren)]])

Parameters:

- painter – QPainter
- targetOffset – QPoint
- sourceRegion – QRegion
- renderFlags – Combination of RenderFlag

This is an overloaded function.

Renders the widget into the painter's QPainter::device().

Transformations and settings applied to the painter will be used when rendering.


--------------------------------
## repaint()

Repaints the widget directly by calling paintEvent() immediately, unless updates are disabled or the widget is hidden.

We suggest only using repaint() if you need an immediate repaint, for example during animation. In most circumstances update() is better, as it permits Qt to optimize for speed and minimize flicker.


--------------------------------
## repaint(arg__1)

Parameters:

- arg__1 – QRect

This is an overloaded function.

This version repaints a rectangle rect inside the widget.


--------------------------------
## repaint(arg__1)

Parameters:

- arg__1 – QRegion

This is an overloaded function.

This version repaints a region rgn inside the widget.


--------------------------------
## repaint(x, y, w, h)

Parameters:

- x – int
- y – int
- w – int
- h – int

This is an overloaded function.

This version repaints a rectangle (x, y, w, h) inside the widget.

If w is negative, it is replaced with width() - x, and if h is negative, it is replaced width height() - y.


--------------------------------
## resize(arg__1)

Parameters:

- arg__1 – QSize

Setter of property size  .


--------------------------------
## resize(w, h)

Parameters:

- w – int
- h – int

This is an overloaded function.

This corresponds to resize(QSize(w, h)).


--------------------------------
## resizeEvent(event)

Parameters:

- event – QResizeEvent

This event handler can be reimplemented in a subclass to receive widget resize events which are passed in the event parameter. When resizeEvent() is called, the widget already has its new geometry. The old size is accessible through QResizeEvent::oldSize().

The widget will be erased and receive a paint event immediately after processing the resize event. No drawing need be (or should be) done inside this handler.


--------------------------------
## restoreGeometry(geometry)

Parameters:

- geometry – QByteArray

Return type: bool

Restores the geometry and state of top-level widgets stored in the byte array geometry. Returns true on success; otherwise returns false.

If the restored geometry is off-screen, it will be modified to be inside the available screen geometry.

To restore geometry saved using QSettings, you can use code like this:

```python
settings = QSettings("MyCompany", "MyApp")
myWidget.restoreGeometry(settings.value("myWidget/geometry").toByteArray())
```

See the Window Geometry documentation for an overview of geometry issues with windows.

Use restoreState() to restore the geometry and the state of toolbars and dock widgets.


--------------------------------
## saveGeometry()

Return type: QByteArray

Saves the current geometry and state for top-level widgets.

To save the geometry when the window closes, you can implement a close event like this:

```python
def closeEvent(self, event):

    settings = QSettings("MyCompany", "MyApp")
    settings.setValue("geometry", saveGeometry())
    QWidget.closeEvent(event)
```

See the Window Geometry documentation for an overview of geometry issues with windows.

Use saveState() to save the geometry and the state of toolbars and dock widgets.


--------------------------------
## screen()

Return type: QScreen

Returns the screen the widget is on.


--------------------------------
## scroll(dx, dy, arg__3)

Parameters:

- dx – int
- dy – int
- arg__3 – QRect

This is an overloaded function.

This version only scrolls r and does not move the children of the widget.

If r is empty or invalid, the result is undefined.


--------------------------------
## scroll(dx, dy)

Parameters:

- dx – int
- dy – int

Scrolls the widget including its children dx pixels to the right and dy downward. Both dx and dy may be negative.

After scrolling, the widgets will receive paint events for the areas that need to be repainted. For widgets that Qt knows to be opaque, this is only the newly exposed parts. For example, if an opaque widget is scrolled 8 pixels to the left, only an 8-pixel wide stripe at the right edge needs updating.

Since widgets propagate the contents of their parents by default, you need to set the autoFillBackground property, or use setAttribute() to set the Qt::WA_OpaquePaintEvent attribute, to make a widget opaque.

For widgets that use contents propagation, a scroll will cause an update of the entire scroll area.


--------------------------------
## setAcceptDrops(on)

Parameters:

- on – bool

Setter of property acceptDrops  .


--------------------------------
## setAccessibleDescription(description)

Parameters:

- description – str

Setter of property accessibleDescription  .


--------------------------------
## setAccessibleName(name)

Parameters:

- name – str

Setter of property accessibleName  .


--------------------------------
## setAttribute(arg__1[, on=true])

Parameters:

- arg__1 – WidgetAttribute
- on – bool

Sets the attribute attribute on this widget if on is true; otherwise clears the attribute.


--------------------------------
## setAutoFillBackground(enabled)

Parameters:

- enabled – bool

Setter of property autoFillBackground  .


--------------------------------
## setBackgroundRole(arg__1)

Parameters:

- arg__1 – ColorRole

Sets the background role of the widget to role.

The background role defines the brush from the widget’s palette that is used to render the background.

If role is QPalette::NoRole, then the widget inherits its parent’s background role.

Note that styles are free to choose any color from the palette. You can modify the palette or set a style sheet if you don’t achieve the result you want with setBackgroundRole().


--------------------------------
## setBaseSize(basew, baseh)

Parameters:

- basew – int
- baseh – int

This is an overloaded function.

This corresponds to setBaseSize (QSize(basew, baseh)). Sets the widgets base size to width basew and height baseh.


--------------------------------
## setBaseSize(arg__1)

Parameters:

- arg__1 – QSize

Setter of property baseSize  .


--------------------------------
## setContentsMargins(margins)

Parameters:

- margins – QMargins

This is an overloaded function.

The setContentsMargins function sets the margins around the widget’s contents.

Sets the margins around the contents of the widget to have the sizes determined by margins. The margins are used by the layout system, and may be used by subclasses to specify the area to draw in (e.g. excluding the frame).

Changing the margins will trigger a resizeEvent() .


--------------------------------
## setContentsMargins(left, top, right, bottom)

Parameters:

- left – int
- top – int
- right – int
- bottom – int

Sets the margins around the contents of the widget to have the sizes left, top, right, and bottom. The margins are used by the layout system, and may be used by subclasses to specify the area to draw in (e.g. excluding the frame).

Changing the margins will trigger a resizeEvent() .


--------------------------------
## setContextMenuPolicy(policy)

Parameters:

- policy – ContextMenuPolicy

Setter of property contextMenuPolicy  .


--------------------------------
## setCursor(arg__1)

Parameters:

- arg__1 – QCursor

Setter of property cursor  .


--------------------------------
## setDisabled(arg__1)

Parameters:

- arg__1 – bool

Disables widget input events if disable is true; otherwise enables input events.

See the enabled documentation for more information.


--------------------------------
## setEnabled(arg__1)

Parameters:

- arg__1 – bool

Setter of property enabled  .


--------------------------------
## setFixedHeight(h)

Parameters:

- h – int

Sets both the minimum and maximum heights of the widget to h without changing the widths. Provided for convenience.


--------------------------------
## setFixedSize(w, h)

Parameters:

- w – int
- h – int

This is an overloaded function.

Sets the width of the widget to w and the height to h.


--------------------------------
## setFixedSize(arg__1)

Parameters:

- arg__1 – QSize

Sets both the minimum and maximum sizes of the widget to s, thereby preventing it from ever growing or shrinking.

This will override the default size constraints set by QLayout .

To remove constraints, set the size to QWIDGETSIZE_MAX .

Alternatively, if you want the widget to have a fixed size based on its contents, you can call setSizeConstraint ( SetFixedSize );


--------------------------------
## setFixedWidth(w)

Parameters:

- w – int

Sets both the minimum and maximum width of the widget to w without changing the heights. Provided for convenience.


--------------------------------
## setFocus(reason)

Parameters:

- reason – FocusReason

Gives the keyboard input focus to this widget (or its focus proxy) if this widget or one of its parents is the active window . The reason argument will be passed into any focus event sent from this function, it is used to give an explanation of what caused the widget to get focus. If the window is not active, the widget will be given the focus when the window becomes active.

First, a focus about to change event is sent to the focus widget (if any) to tell it that it is about to lose the focus. Then focus is changed, a focus out event is sent to the previous focus item and a focus in event is sent to the new item to tell it that it just received the focus. (Nothing happens if the focus in and focus out widgets are the same.)


setFocus() gives focus to a widget regardless of its focus policy, but does not clear any keyboard grab (see grabKeyboard() ).

Be aware that if the widget is hidden, it will not accept focus until it is shown.


--------------------------------
## setFocus()

This is an overloaded function.

Gives the keyboard input focus to this widget (or its focus proxy) if this widget or one of its parents is the active window .


--------------------------------
## setFocusPolicy(policy)

Parameters:

- policy – FocusPolicy

Setter of property focusPolicy  .


--------------------------------
## setFocusProxy(arg__1)

Parameters:

- arg__1 – QWidget

Sets the widget’s focus proxy to widget w. If w is None, the function resets this widget to have no focus proxy.

Some widgets can “have focus”, but create a child widget, such as QLineEdit , to actually handle the focus. In this case, the widget can set the line edit to be its focus proxy.

setFocusProxy() sets the widget which will actually get focus when “this widget” gets it. If there is a focus proxy, setFocus() and hasFocus() operate on the focus proxy. If “this widget” is the focus widget, then setFocusProxy() moves focus to the new focus proxy.


--------------------------------
## setFont(arg__1)

Parameters:

- arg__1 – QFont

Setter of property font  .


--------------------------------
## setForegroundRole(arg__1)

Parameters:

- arg__1 – ColorRole

Sets the foreground role of the widget to role.

The foreground role defines the color from the widget’s palette that is used to draw the foreground.

If role is QPalette::NoRole, the widget uses a foreground role that contrasts with the background role.

Note that styles are free to choose any color from the palette. You can modify the palette or set a style sheet if you don’t achieve the result you want with setForegroundRole().


--------------------------------
## setGeometry(arg__1)

Parameters:

- arg__1 – QRect

Setter of property geometry  .


--------------------------------
## setGeometry(x, y, w, h)

Parameters:

- x – int
- y – int
- w – int
- h – int

This is an overloaded function.

This corresponds to setGeometry (QRect(x, y, w, h)).


--------------------------------
## setGraphicsEffect(effect)

Parameters:

- effect – QGraphicsEffect

The setGraphicsEffect function is for setting the widget’s graphics effect.

Sets effect as the widget’s effect. If there already is an effect installed on this widget, QWidget will delete the existing effect before installing the new effect.

If effect is the installed effect on a different widget, setGraphicsEffect() will remove the effect from the widget and install it on this widget.

QWidget takes ownership of effect.


--------------------------------
## setHidden(hidden)

Parameters:

- hidden – bool

Convenience function, equivalent to setVisible (!``hidden``).


--------------------------------
## setInputMethodHints(hints)

Parameters:

- hints – Combination of InputMethodHint

Setter of property inputMethodHints  .


--------------------------------
## setLayout(arg__1)

Parameters:

- arg__1 – QLayout


Sets the layout manager for this widget to layout.

If there already is a layout manager installed on this widget, QWidget won’t let you install another. You must first delete the existing layout manager (returned by layout() ) before you can call setLayout() with the new layout.

If layout is the layout manager on a different widget, setLayout() will reparent the layout and make it the layout manager for this widget.

Example:

```python
layout = QVBoxLayout()
layout.addWidget(formWidget)
setLayout(layout)
```

An alternative to calling this function is to pass this widget to the layout’s constructor.

The QWidget will take ownership of layout.


--------------------------------
## setLayoutDirection(direction)

Parameters:

- direction – LayoutDirection

Setter of property layoutDirection  .


--------------------------------
## setLocale(locale)

Parameters:

- locale – QLocale

Setter of property locale  .


--------------------------------
## setMask(arg__1)

Parameters:

- arg__1 – QBitmap

Causes only the pixels of the widget for which bitmap has a corresponding 1 bit to be visible. If the region includes pixels outside the rect() of the widget, window system controls in that area may or may not be visible, depending on the platform.

Note that this effect can be slow if the region is particularly complex.

The following code shows how an image with an alpha channel can be used to generate a mask for a widget:

```python
topLevelLabel = QLabel()
pixmap = QPixmap(":/images/tux.png")
topLevelLabel.setPixmap(pixmap)
topLevelLabel.setMask(pixmap.mask())
```

The label shown by this code is masked using the image it contains, giving the appearance that an irregularly-shaped image is being drawn directly onto the screen.

Masked widgets receive mouse events only on their visible portions.


--------------------------------
## setMask(arg__1)

Parameters:

- arg__1 – QRegion

This is an overloaded function.

Causes only the parts of the widget which overlap region to be visible. If the region includes pixels outside the rect() of the widget, window system controls in that area may or may not be visible, depending on the platform.

Since QRegion allows arbitrarily complex regions to be created, widget masks can be made to suit the most unconventionally-shaped windows, and even allow widgets to be displayed with holes in them. Note that this effect can be slow if the region is particularly complex.

Widget masks are used to hint to the window system that the application does not want mouse events for areas outside the mask. On most systems, they also result in coarse visual clipping. To get smooth window edges, use translucent background and anti-aliased painting instead, as shown in the Translucent Background example.


--------------------------------
## setMaximumHeight(maxh)

Parameters:

- maxh – int

Setter of property maximumHeight  .


--------------------------------
## setMaximumSize(maxw, maxh)

Parameters:

- maxw – int
- maxh – int

This is an overloaded function.

This function corresponds to setMaximumSize (QSize(maxw, maxh)). Sets the maximum width to maxw and the maximum height to maxh.


--------------------------------
## setMaximumSize(arg__1)

Parameters:

- arg__1 – QSize

Setter of property maximumSize  .


--------------------------------
## setMaximumWidth(maxw)

Parameters:

- maxw – int

Setter of property maximumWidth  .


--------------------------------
## setMinimumHeight(minh)

Parameters:

- minh – int

Setter of property minimumHeight  .


--------------------------------
## setMinimumSize(arg__1)

Parameters:

- arg__1 – QSize

Setter of property minimumSize  .


--------------------------------
## setMinimumSize(minw, minh)

Parameters:

- minw – int
- minh – int

This is an overloaded function.

This function corresponds to setMinimumSize (QSize(minw, minh)). Sets the minimum width to minw and the minimum height to minh.


--------------------------------
## setMinimumWidth(minw)

Parameters:

- minw – int

Setter of property minimumWidth  .


--------------------------------
## setMouseTracking(enable)

Parameters:

- enable – bool

Setter of property mouseTracking  .


--------------------------------
## setPalette(arg__1)

Parameters:

- arg__1 – QPalette

Setter of property palette  .


--------------------------------
## setParent(parent)

Parameters:

- parent – QWidget

Sets the parent of the widget to parent, and resets the window flags. The widget is moved to position (0, 0) in its new parent.

If the new parent widget is in a different window, the reparented widget and its children are appended to the end of the tab chain of the new parent widget, in the same internal order as before. If one of the moved widgets had keyboard focus, setParent() calls clearFocus() for that widget.

If the new parent widget is in the same window as the old parent, setting the parent doesn’t change the tab order or keyboard focus.

If the “new” parent widget is the old parent widget, this function does nothing.


--------------------------------
## setParent(parent, f)

Parameters:

- parent – QWidget
- f – Combination of WindowType

This is an overloaded function.

This function also takes widget flags, f as an argument.


--------------------------------
## setScreen(arg__1)

Parameters:

- arg__1 – QScreen

Sets the screen on which the widget should be shown to screen.

Setting the screen only makes sense for windows. If necessary, the widget’s window will get recreated on screen.


--------------------------------
## setShortcutAutoRepeat(id[, enable=true])

Parameters:

- id – int
- enable – bool

If enable is true, auto repeat of the shortcut with the given id is enabled; otherwise it is disabled.


--------------------------------
## setShortcutEnabled(id[, enable=true])

Parameters:

- id – int
- enable – bool

If enable is true, the shortcut with the given id is enabled; otherwise the shortcut is disabled.


--------------------------------
## setSizeIncrement(arg__1)

Parameters:

- arg__1 – QSize

Setter of property sizeIncrement  .


--------------------------------
## setSizeIncrement(w, h)

Parameters:

- w – int
- h – int

This is an overloaded function.

Sets the x (width) size increment to w and the y (height) size increment to h.


--------------------------------
## setSizePolicy(horizontal, vertical)

Parameters:

- horizontal – Policy
- vertical – Policy

This is an overloaded function.

Sets the size policy of the widget to horizontal and vertical, with standard stretch and no height-for-width.


--------------------------------
## setSizePolicy(arg__1)

Parameters:

- arg__1 – QSizePolicy

Setter of property sizePolicy  .


--------------------------------
## setStatusTip(arg__1)

Parameters:

- arg__1 – str

Setter of property statusTip  .


--------------------------------
## setStyle(arg__1)

Parameters:

- arg__1 – QStyle

Sets the widget’s GUI style to style. The ownership of the style object is not transferred.

If no style is set, the widget uses the application’s style, style() instead.

Setting a widget’s style has no effect on existing or future child widgets.


--------------------------------
## setStyleSheet(styleSheet)

Parameters:

- styleSheet – str

Setter of property styleSheet  .


--------------------------------
## static setTabOrder(arg__1, arg__2)

Parameters:

- arg__1 – QWidget
- arg__2 – QWidget


Puts the second widget after the first widget in the focus order.

It effectively removes the second widget from its focus chain and inserts it after the first widget.

Note that since the tab order of the second widget is changed, you should order a chain like this:

```python
setTabOrder(a, b) # a to b
setTabOrder(b, c) # a to b to c
setTabOrder(c, d) # a to b to c to d
```

not like this:

```python
# WRONG
setTabOrder(c, d) # c to d
setTabOrder(a, b) # a to b AND c to d
setTabOrder(b, c) # a to b to c, but not c to d
```

If first or second has a focus proxy, setTabOrder() correctly substitutes the proxy.


--------------------------------
## setTabletTracking(enable)

Parameters:

- enable – bool

Setter of property tabletTracking  .


--------------------------------
## setToolTip(arg__1)

Parameters:

- arg__1 – str

Setter of property toolTip  .


--------------------------------
## setToolTipDuration(msec)

Parameters:

- msec – int

Setter of property toolTipDuration  .


--------------------------------
## setUpdatesEnabled(enable)

Parameters:

- enable – bool

Setter of property updatesEnabled  .


--------------------------------
## setVisible(visible)

Parameters:

- visible – bool

Setter of property visible  .


--------------------------------
## setWhatsThis(arg__1)

Parameters:

- arg__1 – str

Setter of property whatsThis  .


--------------------------------
## setWindowFilePath(filePath)

Parameters:

- filePath – str

Setter of property windowFilePath  .


--------------------------------
## setWindowFlag(arg__1[, on=true])

Parameters:

- arg__1 – WindowType
- on – bool

Sets the window flag flag on this widget if on is true; otherwise clears the flag.


--------------------------------
## setWindowFlags(type)

Parameters:

- type – Combination of WindowType


--------------------------------
## setWindowIcon(icon)

Parameters:

- icon – QIcon

Setter of property windowIcon  .


--------------------------------
## setWindowIconText(arg__1)

Parameters:

- arg__1 – str

Setter of property windowIconText  .


--------------------------------
## setWindowModality(windowModality)

Parameters:

- windowModality – WindowModality

Setter of property windowModality  .


--------------------------------
## setWindowModified(arg__1)

Parameters:

- arg__1 – bool

Setter of property windowModified  .


--------------------------------
## setWindowOpacity(level)

Parameters:

- level – float


--------------------------------
## setWindowRole(arg__1)

Parameters:

- arg__1 – str

Sets the window’s role to role. This only makes sense for windows on X11.


--------------------------------
## setWindowState(state)

Parameters:

- state – Combination of WindowState


Sets the window state to windowState. The window state is a OR’ed combination of Qt::WindowState: Qt::WindowMinimized, Qt::WindowMaximized, Qt::WindowFullScreen, and Qt::WindowActive.

If the window is not visible (i.e. isVisible() returns false), the window state will take effect when show() is called. For visible windows, the change is immediate. For example, to toggle between full-screen and normal mode, use the following code:

```python
w.setWindowState(w.windowState() ^ Qt.WindowFullScreen)
```

To restore and activate a minimized window (while preserving its maximized and/or full-screen state), use the following:

```python
w.setWindowState((w.windowState()  ~Qt.WindowMinimized) | Qt.WindowActive)
```

Calling this function will hide the widget. You must call show() to make the widget visible again.

When the window state changes, the widget receives a changeEvent() of type QEvent::WindowStateChange.


--------------------------------
## setWindowTitle(arg__1)

Parameters:

- arg__1 – str

Setter of property windowTitle  .


--------------------------------
## show()

Shows the widget and its child widgets.

For child windows, this is equivalent to calling setVisible (true). Otherwise, it is equivalent to calling showFullScreen() , showMaximized() , or setVisible (true), depending on the platform’s default behavior for the window flags.


--------------------------------
## showEvent(event)

Parameters:

- event – QShowEvent

This event handler can be reimplemented in a subclass to receive widget show events which are passed in the event parameter.

Non-spontaneous show events are sent to widgets immediately before they are shown. The spontaneous show events of windows are delivered afterwards.


--------------------------------
## showFullScreen()

Shows the widget in full-screen mode.

Calling this function only affects windows .

To return from full-screen mode, call showNormal() or close() .

An alternative would be to bypass the window manager entirely and create a window with the Qt::X11BypassWindowManagerHint flag. This has other severe problems though, like broken keyboard focus and very strange effects on desktop changes or when the user raises other windows.

X11 window managers that follow modern post-ICCCM specifications support full-screen mode properly.

On macOS, showing a window full screen puts the entire application in full-screen mode, providing it with a dedicated desktop. Showing another window while the application runs in full-screen mode might automatically make that window full screen as well. To prevent that, exit full-screen mode by calling showNormal() or by close() on the full screen window before showing another window.


--------------------------------
## showMaximized()

Shows the widget maximized.

Calling this function only affects windows .

On X11, this function may not work properly with certain window managers. See the Window Geometry documentation for an explanation.


--------------------------------
## showMinimized()

Shows the widget minimized, as an icon.

Calling this function only affects windows .


--------------------------------
## showNormal()

Restores the widget after it has been maximized or minimized.

Calling this function only affects windows .


--------------------------------
## size()

Return type: QSize

Getter of property size  .


--------------------------------
## sizeHint()

Return type: QSize

Getter of property sizeHint  .


--------------------------------
## sizeIncrement()

Return type: QSize

Getter of property sizeIncrement  .


--------------------------------
## sizePolicy()

Return type: QSizePolicy

Getter of property sizePolicy  .


--------------------------------
## stackUnder(arg__1)

Parameters:

- arg__1 – QWidget

Places the widget under w in the parent widget’s stack.

To make this work, the widget itself and w must be siblings.


--------------------------------
## statusTip()

Return type: str

Getter of property statusTip  .


--------------------------------
## style()

Return type: QStyle


--------------------------------
## styleSheet()

Return type: str

Getter of property styleSheet  .


--------------------------------
## tabletEvent(event)

Parameters:

- event – QTabletEvent

This event handler, for event event, can be reimplemented in a subclass to receive tablet events for the widget.

If you reimplement this handler, it is very important that you ignore() the event if you do not handle it, so that the widget’s parent can interpret it.

The default implementation ignores the event.

If tablet tracking is switched off, tablet move events only occur if the stylus is in contact with the tablet, or at least one stylus button is pressed, while the stylus is being moved. If tablet tracking is switched on, tablet move events occur even while the stylus is hovering in proximity of the tablet, with no buttons pressed.


--------------------------------
## testAttribute(arg__1)

Parameters:

- arg__1 – WidgetAttribute

Return type: bool

Returns true if attribute attribute is set on this widget; otherwise returns false.


--------------------------------
## toolTip()

Return type: str

Getter of property toolTip  .


--------------------------------
## toolTipDuration()

Return type: int

Getter of property toolTipDuration  .


--------------------------------
## topLevelWidget()

Return type: QWidget

Use window() instead.


--------------------------------
## underMouse()

Return type: bool

Returns true if the widget is under the mouse cursor; otherwise returns false.

This value is not updated properly during drag and drop operations.


--------------------------------
## ungrabGesture(type)

Parameters:

- type – GestureType

Unsubscribes the widget from a given gesture type


--------------------------------
## unsetCursor()

Reset function of property cursor  .


--------------------------------
## unsetLayoutDirection()

Reset function of property layoutDirection  .


--------------------------------
## unsetLocale()

Reset function of property locale  .


--------------------------------
## update(arg__1)

Parameters:

- arg__1 – QRegion

This is an overloaded function.

This version repaints a region rgn inside the widget.


--------------------------------
## update(x, y, w, h)

Parameters:

- x – int
- y – int
- w – int
- h – int

This is an overloaded function.

This version updates a rectangle (x, y, w, h) inside the widget.


--------------------------------
## update(arg__1)

Parameters:

- arg__1 – QRect

This is an overloaded function.

This version updates a rectangle rect inside the widget.


--------------------------------
## update()

Updates the widget unless updates are disabled or the widget is hidden.

This function does not cause an immediate repaint; instead it schedules a paint event for processing when Qt returns to the main event loop. This permits Qt to optimize for more speed and less flicker than a call to repaint() does.

Calling update() several times normally results in just one paintEvent() call.

Qt normally erases the widget’s area before the paintEvent() call. If the Qt::WA_OpaquePaintEvent widget attribute is set, the widget is responsible for painting all its pixels with an opaque color.


--------------------------------
## updateGeometry()

Notifies the layout system that this widget has changed and may need to change geometry.

Call this function if the sizeHint() or sizePolicy() have changed.

For explicitly hidden widgets, updateGeometry() is a no-op. The layout system will be notified as soon as the widget is shown.


--------------------------------
## updateMicroFocus([query=Qt.ImQueryAll])

Parameters:

- query – InputMethodQuery

Updates the widget’s micro focus and informs input methods that the state specified by query has changed.


--------------------------------
## updatesEnabled()

Return type: bool

Getter of property updatesEnabled  .


--------------------------------
## visibleRegion()

Return type: QRegion

Returns the unobscured region where paint events can occur.

For visible widgets, this is an approximation of the area not covered by other widgets; otherwise, this is an empty region.

The repaint() function calls this function if necessary, so in general you do not need to call it.


--------------------------------
## whatsThis()

Return type: str

Getter of property whatsThis  .


--------------------------------
## wheelEvent(event)

Parameters:

- event – QWheelEvent

This event handler, for event event, can be reimplemented in a subclass to receive wheel events for the widget.

If you reimplement this handler, it is very important that you ignore() the event if you do not handle it, so that the widget’s parent can interpret it.

The default implementation ignores the event.


--------------------------------
## winId()

Return type: WId

Returns the window system identifier of the widget.

Portable in principle, but if you use it you are probably about to do something non-portable. Be careful.

If a widget is non-native (alien) and winId() is invoked on it, that widget will be provided a native handle.

This value may change at run-time. An event with type QEvent::WinIdChange will be sent to the widget following a change in window system identifier.


--------------------------------
## window()

Return type: QWidget

Returns the window for this widget, i.e. the next ancestor widget that has (or could have) a window-system frame.

If the widget is a window, the widget itself is returned.

Typical usage is changing the window title:

```python
aWidget.window().setWindowTitle("New Window Title")
```


--------------------------------
## windowFilePath()

Return type: str

Getter of property windowFilePath  .


--------------------------------
## windowFlags()

Return type: Combination of WindowType


--------------------------------
## windowHandle()

Return type: QWindow

If this is a native widget, return the associated QWindow. Otherwise return null.

Native widgets include toplevel widgets, QGLWidget, and child widgets on which winId() was called.


--------------------------------
## windowIcon()

Return type: QIcon

Getter of property windowIcon  .


--------------------------------
## windowIconChanged(icon)

Parameters:

- icon – QIcon

This signal is emitted when the window’s icon has changed, with the new icon as an argument.

Notification signal of property windowIcon  .


--------------------------------
## windowIconText()

Return type: str

Getter of property windowIconText  .


--------------------------------
## windowIconTextChanged(iconText)

Parameters:

- iconText – str

This signal is emitted when the window’s icon text has changed, with the new iconText as an argument.

This signal is deprecated.

Notification signal of property windowIconText  .


--------------------------------
## windowModality()

Return type: WindowModality

Getter of property windowModality  .


--------------------------------
## windowOpacity()

Return type: float


--------------------------------
## windowRole()

Return type: str

Returns the window’s role, or an empty string.


--------------------------------
## windowState()

Return type: Combination of WindowState

Returns the current window state. The window state is a OR’ed combination of Qt::WindowState: Qt::WindowMinimized, Qt::WindowMaximized, Qt::WindowFullScreen, and Qt::WindowActive.


--------------------------------
## windowTitle()

Return type: str

Getter of property windowTitle  .


--------------------------------
## windowTitleChanged(title)

Parameters:

- title – str

This signal is emitted when the window’s title has changed, with the new title as an argument.

Notification signal of property windowTitle  .


--------------------------------
## windowType()

Return type: WindowType

Returns the window type of this widget. This is identical to windowFlags() & Qt::WindowType_Mask.


--------------------------------
## x()

Return type: int

Getter of property x  .


--------------------------------
## y()

Return type: int

Getter of property y  .

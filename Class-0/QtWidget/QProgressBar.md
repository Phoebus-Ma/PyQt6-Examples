
[Chinese doc](QProgressBar.CN.md)

# class QProgressBar

The QProgressBar widget provides a horizontal or vertical progress bar.


# Synopsis

## Properties

- [alignment](#property-alignment--combination-of-qtalignmentflag)

    The alignment of the progress bar.

- [format](#property-format--str)

    The string used to generate the current text.

- [invertedAppearance](#property-invertedappearance--bool)

    Whether or not a progress bar shows its progress inverted.

- [maximum](#property-maximum--int)

    The progress bar’s maximum value.

- [minimum](#property-minimum--int)

    The progress bar’s minimum value.

- [orientation](#property-orientation--qtorientation)

    The orientation of the progress bar.

- [text](#property-text--str)

    The descriptive text shown with the progress bar.

- [textDirection](#property-textdirection--qprogressbardirection)

    The reading direction of the text for vertical progress bars.

- [textVisible](#property-textvisible--bool)

    Whether the current completed percentage should be displayed.

- [value](#property-value--int)

    The progress bar’s current value.


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

A progress bar is used to give the user an indication of the progress of an operation and to reassure them that the application is still running.

The progress bar uses the concept of steps. You set it up by specifying the minimum and maximum possible step values, and it will display the percentage of steps that have been completed when you later give it the current step value. The percentage is calculated by dividing the progress ( value() - minimum() ) divided by maximum() - minimum() .

You can specify the minimum and maximum number of steps with setMinimum() and setMaximum . The current number of steps is set with setValue() . The progress bar can be rewound to the beginning with reset() .

If minimum and maximum both are set to 0, the bar shows a busy indicator instead of a percentage of steps. This is useful, for example, when using QNetworkAccessManager to download items when they are unable to determine the size of the item being downloaded.


--------------------------------
## class Direction

Specifies the reading direction of the text for vertical progress bars.

| Constant                 | Description                               |
| ------------------------ | ----------------------------------------- |
| QProgressBar.TopToBottom | The text is rotated 90 degrees clockwise. |
| QProgressBar.BottomToTop | The text is rotated 90 degrees counter-clockwise. |

Note that whether or not the text is drawn is dependent on the style. Currently CleanLooks and Plastique draw the text. Mac, Windows and WindowsVista style do not.


--------------------------------
## property alignment : Combination of Qt.AlignmentFlag

This property holds the alignment of the progress bar.

Access functions:

- alignment()
- setAlignment()


--------------------------------
## property format : str

This property holds the string used to generate the current text.

%p - is replaced by the percentage completed. %v - is replaced by the current value. %m - is replaced by the total number of steps.

The default value is “%p%”.

Access functions:

- format()
- setFormat()
- resetFormat()


--------------------------------
## property invertedAppearance : bool

This property holds whether or not a progress bar shows its progress inverted.

If this property is true, the progress bar grows in the other direction (e.g. from right to left). By default, the progress bar is not inverted.

Access functions:

- invertedAppearance()
- setInvertedAppearance()


--------------------------------
## property maximum : int

This property holds the progress bar’s maximum value.

When setting this property, the minimum is adjusted if necessary to ensure that the range remains valid. If the current value falls outside the new range, the progress bar is reset with reset() .

Access functions:

- maximum()
- setMaximum()


--------------------------------
## property minimum : int

This property holds the progress bar’s minimum value.

When setting this property, the maximum is adjusted if necessary to ensure that the range remains valid. If the current value falls outside the new range, the progress bar is reset with reset() .

Access functions:

- minimum()
- setMinimum()


--------------------------------
## property orientation : Qt.Orientation

This property holds the orientation of the progress bar.

The orientation must be Qt::Horizontal (the default) or Qt::Vertical.

Access functions:

- orientation()
- setOrientation()


--------------------------------
## property text : str

This property holds the descriptive text shown with the progress bar.

The text returned is the same as the text displayed in the center (or in some styles, to the left) of the progress bar.

The progress shown in the text may be smaller than the minimum value, indicating that the progress bar is in the “reset” state before any progress is set.

In the default implementation, the text either contains a percentage value that indicates the progress so far, or it is blank because the progress bar is in the reset state.

Access functions:

- text()


--------------------------------
## property textDirection : QProgressBar.Direction

This property holds the reading direction of the text for vertical progress bars.

This property has no impact on horizontal progress bars. By default, the reading direction is TopToBottom .

Access functions:

- textDirection()
- setTextDirection()


--------------------------------
## property textVisible : bool

This property holds whether the current completed percentage should be displayed.

This property may be ignored by the style (e.g., QMacStyle never draws the text).

Access functions:

- isTextVisible()
- setTextVisible()


--------------------------------
## property value : int

This property holds the progress bar’s current value.

Attempting to change the current value to one outside the minimum-maximum range has no effect on the current value.

Access functions:

- value()
- setValue()
- Signal valueChanged()


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs a progress bar with the given parent.

By default, the minimum step value is set to 0, and the maximum to 100.


--------------------------------
## alignment()

Return type: Combination of AlignmentFlag

Getter of property alignment  .


--------------------------------
## format()

Return type: str

Getter of property format  .


--------------------------------
## initStyleOption(option)

Parameters:

- option – QStyleOptionProgressBar

Initialize option with the values from this QProgressBar . This method is useful for subclasses when they need a QStyleOptionProgressBar , but don’t want to fill in all the information themselves.


--------------------------------
## invertedAppearance()

Return type: bool

Getter of property invertedAppearance  .


--------------------------------
## isTextVisible()

Return type: bool

Getter of property textVisible  .


--------------------------------
## maximum()

Return type: int

Getter of property maximum  .


--------------------------------
## minimum()

Return type: int

Getter of property minimum  .


--------------------------------
## orientation()

Return type: Orientation

Getter of property orientation  .


--------------------------------
## reset()

Reset the progress bar. The progress bar “rewinds” and shows no progress.


--------------------------------
## resetFormat()

Reset function of property format  .


--------------------------------
## setAlignment(alignment)

Parameters:

- alignment – Combination of AlignmentFlag

Setter of property alignment  .


--------------------------------
## setFormat(format)

Parameters:

- format – str

Setter of property format  .


--------------------------------
## setInvertedAppearance(invert)

Parameters:

- invert – bool

Setter of property invertedAppearance  .


--------------------------------
## setMaximum(maximum)

Parameters:

- maximum – int

Setter of property maximum  .


--------------------------------
## setMinimum(minimum)

Parameters:

- minimum – int

Setter of property minimum  .


--------------------------------
## setOrientation(arg__1)

Parameters:

- arg__1 – Orientation

Setter of property orientation  .


--------------------------------
## setRange(minimum, maximum)

Parameters:

- minimum – int
- maximum – int

Sets the progress bar’s minimum and maximum values to minimum and maximum respectively.

If maximum is smaller than minimum, minimum becomes the only legal value.

If the current value falls outside the new range, the progress bar is reset with reset() .

The QProgressBar can be set to undetermined state by using setRange(0, 0).


--------------------------------
## setTextDirection(textDirection)

Parameters:

- textDirection – Direction

Setter of property textDirection  .


--------------------------------
## setTextVisible(visible)

Parameters:

- visible – bool

Setter of property textVisible  .


--------------------------------
## setValue(value)

Parameters:

- value – int

Setter of property value  .


--------------------------------
## text()

Return type: str

Getter of property text  .


--------------------------------
## textDirection()

Return type: Direction

Getter of property textDirection  .


--------------------------------
## value()

Return type: int

Getter of property value  .


--------------------------------
## valueChanged(value)

Parameters:

- value – int

This signal is emitted when the value shown in the progress bar changes. value is the new value shown by the progress bar.

Notification signal of property value  .

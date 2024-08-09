
[Chinese doc](QFormLayout.CN.md)

# class QFormLayout

The QFormLayout class manages forms of input widgets and their associated labels.


# Synopsis

## Properties

- [fieldGrowthPolicy](#property-fieldgrowthpolicy--qformlayoutfieldgrowthpolicy)

    The way in which the form’s fields grow.

- [formAlignment](#property-formalignment--combination-of-qtalignmentflag)

    The alignment of the form layout’s contents within the layout’s geometry.

- [horizontalSpacing](#property-horizontalspacing--int)

    The spacing between widgets that are laid out side by side.

- [labelAlignment](#property-labelalignment--combination-of-qtalignmentflag)

    The horizontal alignment of the labels.

- [rowWrapPolicy](#property-rowwrappolicy--qformlayoutrowwrappolicy)

    The way in which the form’s rows wrap.

- [verticalSpacing](#property-verticalspacing--int)

    The spacing between widgets that are laid out vertically.


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

QFormLayout is a convenience layout class that lays out its children in a two-column form. The left column consists of labels and the right column consists of “field” widgets (line editors, spin boxes, etc.).

Traditionally, such two-column form layouts were achieved using QGridLayout . QFormLayout is a higher-level alternative that provides the following advantages:

- Adherence to the different platform’s look and feel guidelines.

    For example, the macOS Aqua and KDE guidelines specify that the labels should be right-aligned, whereas Windows and GNOME applications normally use left-alignment.

- Support for wrapping long rows.

    For devices with small displays, QFormLayout can be set to wrap long rows , or even to wrap all rows .

- Convenient API for creating label–field pairs.

    The addRow() overload that takes a QString and a QWidget * creates a QLabel behind the scenes and automatically set up its buddy. We can then write code like this:

```python
formLayout = QFormLayout(self)
formLayout.addRow(tr("Name:"), nameLineEdit)
formLayout.addRow(tr("Email:"), emailLineEdit)
formLayout.addRow(tr("Age:"), ageSpinBox)
```

Compare this with the following code, written using QGridLayout :

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

The table below shows the default appearance in different styles.

The form styles can be also be overridden individually by calling setLabelAlignment() , setFormAlignment() , setFieldGrowthPolicy() , and setRowWrapPolicy() . For example, to simulate the form layout appearance of QMacStyle on all platforms, but with left-aligned labels, you could write:

```python
formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
formLayout.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
formLayout.setLabelAlignment(Qt.AlignLeft)
```


--------------------------------
## class FieldGrowthPolicy

This enum specifies the different policies that can be used to control the way in which the form’s fields grow.

| Constant                          | Description |
| --------------------------------- | ----------- |
| QFormLayout.FieldsStayAtSizeHint  | The fields never grow beyond their effective size hint . This is the default for QMacStyle. |
| QFormLayout.ExpandingFieldsGrow   | Fields with an horizontal size policy of Expanding or MinimumExpanding will grow to fill the available space. The other fields will not grow beyond their effective size hint. This is the default policy for Plastique. |
| QFormLayout.AllNonFixedFieldsGrow | All fields with a size policy that allows them to grow will grow to fill the available space. This is the default policy for most styles. |


--------------------------------
## class RowWrapPolicy

This enum specifies the different policies that can be used to control the way in which the form’s rows wrap.

| Constant                 | Description |
| ------------------------ | ----------- |
| QFormLayout.DontWrapRows | Fields are always laid out next to their label. This is the default policy for all styles except Qt Extended styles. |
| QFormLayout.WrapLongRows | Labels are given enough horizontal space to fit the widest label, and the rest of the space is given to the fields. If the minimum size of a field pair is wider than the available space, the field is wrapped to the next line. This is the default policy for Qt Extended styles. |
| QFormLayout.WrapAllRows  | Fields are always laid out below their label. |


--------------------------------
## class ItemRole

This enum specifies the types of widgets (or other layout items) that may appear in a row.

| Constant                 | Description     |
| ------------------------ | --------------- |
| QFormLayout.LabelRole    | A label widget. |
| QFormLayout.FieldRole    | A field widget. |
| QFormLayout.SpanningRole | A widget that spans label and field columns. |


--------------------------------
## property fieldGrowthPolicy : QFormLayout.FieldGrowthPolicy

This property holds the way in which the form’s fields grow.

The default value depends on the widget or application style. For QMacStyle, the default is FieldsStayAtSizeHint ; for QCommonStyle derived styles (like Plastique and Windows), the default is ExpandingFieldsGrow ; for Qt Extended styles, the default is AllNonFixedFieldsGrow .

If none of the fields can grow and the form is resized, extra space is distributed according to the current form alignment .

Access functions:

- fieldGrowthPolicy()
- setFieldGrowthPolicy()


--------------------------------
## property formAlignment : Combination of Qt.AlignmentFlag

This property holds the alignment of the form layout’s contents within the layout’s geometry.

The default value depends on the widget or application style. For QMacStyle, the default is Qt::AlignHCenter | Qt::AlignTop; for the other styles, the default is Qt::AlignLeft | Qt::AlignTop.

Access functions:

- formAlignment()
- setFormAlignment()


--------------------------------
## property horizontalSpacing : int

This property holds the spacing between widgets that are laid out side by side.

By default, if no value is explicitly set, the layout’s horizontal spacing is inherited from the parent layout, or from the style settings for the parent widget.

Access functions:

- horizontalSpacing()
- setHorizontalSpacing()


--------------------------------
## property labelAlignment : Combination of Qt.AlignmentFlag

This property holds the horizontal alignment of the labels.

The default value depends on the widget or application style. For QCommonStyle derived styles, except for QPlastiqueStyle, the default is Qt::AlignLeft; for the other styles, the default is Qt::AlignRight.

Access functions:

- labelAlignment()
- setLabelAlignment()


--------------------------------
## property rowWrapPolicy : QFormLayout.RowWrapPolicy

This property holds the way in which the form’s rows wrap.

The default value depends on the widget or application style. For Qt Extended styles, the default is WrapLongRows ; for the other styles, the default is DontWrapRows .

If you want to display each label above its associated field (instead of next to it), set this property to WrapAllRows .

Access functions:

- rowWrapPolicy()
- setRowWrapPolicy()


--------------------------------
## property verticalSpacing : int

This property holds the spacing between widgets that are laid out vertically.

By default, if no value is explicitly set, the layout’s vertical spacing is inherited from the parent layout, or from the style settings for the parent widget.

Access functions:

- verticalSpacing()
- setVerticalSpacing()


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs a new form layout with the given parent widget.

The layout is set directly as the top-level layout for parent. There can be only one top-level layout for a widget. It is returned by layout() .


--------------------------------
## addRow(layout)

Parameters:

- layout – QLayout

This is an overloaded function.

Adds the specified layout at the end of this form layout. The layout spans both columns.


--------------------------------
## addRow(labelText, field)

Parameters:

- labelText – str
- field – QWidget

This is an overloaded function.

This overload automatically creates a QLabel behind the scenes with labelText as its text. The field is set as the new QLabel ‘s buddy .


--------------------------------
## addRow(labelText, field)

Parameters:

- labelText – str
- field – QLayout

This is an overloaded function.

This overload automatically creates a QLabel behind the scenes with labelText as its text.


--------------------------------
## addRow(label, field)

Parameters:

- label – QWidget
- field – QWidget

Adds a new row to the bottom of this form layout, with the given label and field.


--------------------------------
## addRow(label, field)

Parameters:

- label – QWidget
- field – QLayout

This is an overloaded function.


--------------------------------
## addRow(widget)

Parameters:

- widget – QWidget

This is an overloaded function.

Adds the specified widget at the end of this form layout. The widget spans both columns.


--------------------------------
## fieldGrowthPolicy()

Return type: FieldGrowthPolicy

Getter of property fieldGrowthPolicy  .


--------------------------------
## formAlignment()

Return type: Combination of AlignmentFlag

Getter of property formAlignment  .


--------------------------------
## getItemPosition(index)

Parameters:

- index – int

Return type: PyObject

Retrieves the row and role (column) of the item at the specified index. If index is out of bounds, *``rowPtr`` is set to -1; otherwise the row is stored in *``rowPtr`` and the role is stored in *``rolePtr``.


--------------------------------
## getLayoutPosition(layout)

Parameters:

- layout – QLayout

Return type: PyObject

Retrieves the row and role (column) of the specified child layout. If layout is not in the form layout, *``rowPtr`` is set to -1; otherwise the row is stored in *``rowPtr`` and the role is stored in *``rolePtr``.


--------------------------------
## getWidgetPosition(widget)

Parameters:

- widget – QWidget

Return type: PyObject

Retrieves the row and role (column) of the specified widget in the layout. If widget is not in the layout, *``rowPtr`` is set to -1; otherwise the row is stored in *``rowPtr`` and the role is stored in *``rolePtr``.


--------------------------------
## horizontalSpacing()

Return type: int

Getter of property horizontalSpacing  .


--------------------------------
## insertRow(row, label, field)

Parameters:

- row – int
- label – QWidget
- field – QLayout

This is an overloaded function.


--------------------------------
## insertRow(row, labelText, field)

Parameters:

- row – int
- labelText – str
- field – QWidget

This is an overloaded function.

This overload automatically creates a QLabel behind the scenes with labelText as its text. The field is set as the new QLabel ‘s buddy .


--------------------------------
## insertRow(row, labelText, field)

Parameters:

- row – int
- labelText – str
- field – QLayout

This is an overloaded function.

This overload automatically creates a QLabel behind the scenes with labelText as its text.


--------------------------------
## insertRow(row, widget)

Parameters:

- row – int
- widget – QWidget

This is an overloaded function.

Inserts the specified widget at position row in this form layout. The widget spans both columns. If row is out of bounds, the widget is added at the end.


--------------------------------
## insertRow(row, label, field)

Parameters:

- row – int
- label – QWidget
- field – QWidget

Inserts a new row at position row in this form layout, with the given label and field. If row is out of bounds, the new row is added at the end.


--------------------------------
## insertRow(row, layout)

Parameters:

- row – int
- layout – QLayout

This is an overloaded function.

Inserts the specified layout at position row in this form layout. The layout spans both columns. If row is out of bounds, the widget is added at the end.


--------------------------------
## isRowVisible(layout)

Parameters:

- layout – QLayout

Return type: bool

This is an overloaded function.

Returns true if some items in the row corresponding to layout are visible, otherwise returns false.


--------------------------------
## isRowVisible(widget)

Parameters:

- widget – QWidget

Return type: bool

This is an overloaded function.

Returns true if some items in the row corresponding to widget are visible, otherwise returns false.


--------------------------------
## isRowVisible(row)

Parameters:

- row – int

Return type: bool

Returns true if some items in the row row are visible, otherwise returns false.


--------------------------------
## itemAt(row, role)

Parameters:

- row – int
- role – ItemRole

Return type: QLayoutItem

Returns the layout item in the given row with the specified role (column). Returns None if there is no such item.


--------------------------------
## labelAlignment()

Return type: Combination of AlignmentFlag

Getter of property labelAlignment  .


--------------------------------
## labelForField(field)

Parameters:

- field – QWidget

Return type: QWidget

Returns the label associated with the given field.


--------------------------------
## labelForField(field)

Parameters:

- field – QLayout

Return type: QWidget

This is an overloaded function.


--------------------------------
## removeRow(layout)

Parameters:

- layout – QLayout

This is an overloaded function.

Deletes the row corresponding to layout from this form layout.

After this call, rowCount() is decremented by one. All widgets and nested layouts that occupied this row are deleted. That includes both the field widget(s) and the label, if any. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

You can use this function to undo a previous addRow() or insertRow() :

```python
flay = ...
vbl = QVBoxLayout()
flay.insertRow(2, "User:", vbl)
# later:
flay.removeRow(layout) # vbl == None at this point
```

If you want to remove the row from the form layout without deleting the inserted layout, use takeRow() instead.


--------------------------------
## removeRow(widget)

Parameters:

- widget – QWidget

This is an overloaded function.

Deletes the row corresponding to widget from this form layout.

After this call, rowCount() is decremented by one. All widgets and nested layouts that occupied this row are deleted. That includes both the field widget(s) and the label, if any. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

You can use this function to undo a previous addRow() or insertRow() :

```python
flay = ...
le = QLineEdit()
flay.insertRow(2, "User:", le)
# later:
flay.removeRow(le) # le == None at this point
```

If you want to remove the row from the layout without deleting the widgets, use takeRow() instead.


--------------------------------
## removeRow(row)

Parameters:

- row – int

Deletes row row from this form layout.

row must be non-negative and less than rowCount() .

After this call, rowCount() is decremented by one. All widgets and nested layouts that occupied this row are deleted. That includes both the field widget(s) and the label, if any. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

You can use this function to undo a previous addRow() or insertRow() :

```python
flay = ...
le = QLineEdit()
flay.insertRow(2, "User:", le)
# later:
flay.removeRow(2) # le == None at this point
```

If you want to remove the row from the layout without deleting the widgets, use takeRow() instead.


--------------------------------
## rowCount()

Return type: int

Returns the number of rows in the form.


--------------------------------
## rowWrapPolicy()

Return type: RowWrapPolicy

Getter of property rowWrapPolicy  .


--------------------------------
## setFieldGrowthPolicy(policy)

Parameters:

- policy – FieldGrowthPolicy

Setter of property fieldGrowthPolicy  .


--------------------------------
## setFormAlignment(alignment)

Parameters:

- alignment – Combination of AlignmentFlag

Setter of property formAlignment  .


--------------------------------
## setHorizontalSpacing(spacing)

Parameters:

- spacing – int

Setter of property horizontalSpacing  .


--------------------------------
## setItem(row, role, item)

Parameters:

- row – int
- role – ItemRole
- item – QLayoutItem

Sets the item in the given row for the given role to item, extending the layout with empty rows if necessary.

If the cell is already occupied, the item is not inserted and an error message is sent to the console. The item spans both columns.


--------------------------------
## setLabelAlignment(alignment)

Parameters:

- alignment – Combination of AlignmentFlag

Setter of property labelAlignment  .


--------------------------------
## setLayout(row, role, layout)

Parameters:

- row – int
- role – ItemRole
- layout – QLayout

Sets the sub-layout in the given row for the given role to layout, extending the form layout with empty rows if necessary.

If the cell is already occupied, the layout is not inserted and an error message is sent to the console.


--------------------------------
## setRowVisible(layout, on)

Parameters:

- layout – QLayout
- on – bool

This is an overloaded function.

Shows the row corresponding to layout if on is true, otherwise hides the row.


--------------------------------
## setRowVisible(widget, on)

Parameters:

- widget – QWidget
- on – bool

This is an overloaded function.

Shows the row corresponding to widget if on is true, otherwise hides the row.


--------------------------------
## setRowVisible(row, on)

Parameters:

- row – int
- on – bool

Shows the row row if on is true, otherwise hides the row.

row must be non-negative and less than rowCount() .


--------------------------------
## setRowWrapPolicy(policy)

Parameters:

- policy – RowWrapPolicy

Setter of property rowWrapPolicy  .


--------------------------------
## setVerticalSpacing(spacing)

Parameters:

- spacing – int

Setter of property verticalSpacing  .


--------------------------------
## setWidget(row, role, widget)

Parameters:

- row – int
- role – ItemRole
- widget – QWidget

Sets the widget in the given row for the given role to widget, extending the layout with empty rows if necessary.

If the cell is already occupied, the widget is not inserted and an error message is sent to the console.


--------------------------------
## takeRow(layout)

Parameters:

- layout – QLayout

Return type: TakeRowResult

This is an overloaded function.

Removes the specified layout from this form layout.

After this call, rowCount() is decremented by one. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

```python
flay = ...
vbl = QVBoxLayout()
flay.insertRow(2, "User:", vbl)
# later:
QFormLayout.TakeRowResult result = flay.takeRow(widget)
```

If you want to remove the row from the form layout and delete the inserted layout, use removeRow() instead.

Returns A structure containing both the widget and corresponding label layout items


--------------------------------
## takeRow(widget)

Parameters:

- widget – QWidget

Return type: TakeRowResult

This is an overloaded function.

Removes the specified widget from this form layout.

After this call, rowCount() is decremented by one. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

```python
flay = ...
le = QLineEdit()
flay.insertRow(2, "User:", le)
# later:
QFormLayout.TakeRowResult result = flay.takeRow(widget)
```

If you want to remove the row from the layout and delete the widgets, use removeRow() instead.

Returns A structure containing both the widget and corresponding label layout items


--------------------------------
## takeRow(row)

Parameters:

- row – int

Return type: TakeRowResult

Removes the specified row from this form layout.

row must be non-negative and less than rowCount() .

After this call, rowCount() is decremented by one. All following rows are shifted up one row and the freed vertical space is redistributed amongst the remaining rows.

You can use this function to undo a previous addRow() or insertRow() :

```python
flay = ...
le = QLineEdit()
flay.insertRow(2, "User:", le)
# later:
QFormLayout.TakeRowResult result = flay.takeRow(2)
```

If you want to remove the row from the layout and delete the widgets, use removeRow() instead.

Returns A structure containing both the widget and corresponding label layout items


--------------------------------
## verticalSpacing()

Return type: int

Getter of property verticalSpacing  .


[Chinese doc](QGridLayout.CN.md)

# class QGridLayout

The QGridLayout class lays out widgets in a grid.


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

QGridLayout takes the space made available to it (by its parent layout or by the parentWidget() ), divides it up into rows and columns, and puts each widget it manages into the correct cell.

Columns and rows behave identically; we will discuss columns, but there are equivalent functions for rows.

Each column has a minimum width and a stretch factor. The minimum width is the greatest of that set using setColumnMinimumWidth() and the minimum width of each widget in that column. The stretch factor is set using setColumnStretch() and determines how much of the available space the column will get over and above its necessary minimum.

Normally, each managed widget or layout is put into a cell of its own using addWidget() . It is also possible for a widget to occupy multiple cells using the row and column spanning overloads of addItem() and addWidget() . If you do this, QGridLayout will guess how to distribute the size over the columns/rows (based on the stretch factors).

To remove a widget from a layout, call removeWidget() . Calling hide() on a widget also effectively removes the widget from the layout until show() is called.

This illustration shows a fragment of a dialog with a five-column, three-row grid (the grid is shown overlaid in magenta):

Columns 0, 2 and 4 in this dialog fragment are made up of a QLabel , a QLineEdit , and a QListBox. Columns 1 and 3 are placeholders made with setColumnMinimumWidth() . Row 0 consists of three QLabel objects, row 1 of three QLineEdit objects and row 2 of three QListBox objects. We used placeholder columns (1 and 3) to get the right amount of space between the columns.

Note that the columns and rows are not equally wide or tall. If you want two columns to have the same width, you must set their minimum widths and stretch factors to be the same yourself. You do this using setColumnMinimumWidth() and setColumnStretch() .

If the QGridLayout is not the top-level layout (i.e. does not manage all of the widget’s area and children), you must add it to its parent layout when you create it, but before you do anything with it. The normal way to add a layout is by calling addLayout() on the parent layout.

Once you have added your layout you can start putting widgets and other layouts into the cells of your grid layout using addWidget() , addItem() , and addLayout() .

QGridLayout also includes two margin widths: the contents margin and the spacing() . The contents margin is the width of the reserved space along each of the QGridLayout ‘s four sides. The spacing() is the width of the automatically allocated spacing between neighboring boxes.

The default contents margin values are provided by the style . The default value Qt styles specify is 9 for child widgets and 11 for windows. The spacing defaults to the same as the margin width for a top-level layout, or to the same as the parent layout.


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs a new QGridLayout with parent widget, parent. The layout has one row and one column initially, and will expand when new items are inserted.

The layout is set directly as the top-level layout for parent. There can be only one top-level layout for a widget. It is returned by layout() .

If parent is None, then you must insert this grid layout into another layout, or set it as a widget’s layout using setLayout() .


--------------------------------
## addItem(item, row, column[, rowSpan=1[, columnSpan=1[, alignment=Qt.Alignment()]]])

Parameters:

- item – QLayoutItem
- row – int
- column – int
- rowSpan – int
- columnSpan – int
- alignment – Combination of AlignmentFlag

Adds item at position row, column, spanning rowSpan rows and columnSpan columns, and aligns it according to alignment. If rowSpan and/or columnSpan is -1, then the item will extend to the bottom and/or right edge, respectively. The layout takes ownership of the item.


--------------------------------
## addLayout(arg__1, row, column[, alignment=Qt.Alignment()])

Parameters:

- arg__1 – QLayout
- row – int
- column – int
- alignment – Combination of AlignmentFlag

Places the layout at position (row, column) in the grid. The top-left position is (0, 0).

The alignment is specified by alignment. The default alignment is 0, which means that the widget fills the entire cell.

A non-zero alignment indicates that the layout should not grow to fill the available space but should be sized according to sizeHint() .

layout becomes a child of the grid layout.


--------------------------------
## addLayout(arg__1, row, column, rowSpan, columnSpan[, alignment=Qt.Alignment()])

Parameters:

- arg__1 – QLayout
- row – int
- column – int
- rowSpan – int
- columnSpan – int
- alignment – Combination of AlignmentFlag

This is an overloaded function.

This version adds the layout layout to the cell grid, spanning multiple rows/columns. The cell will start at row, column spanning rowSpan rows and columnSpan columns.

If rowSpan and/or columnSpan is -1, then the layout will extend to the bottom and/or right edge, respectively.

--------------------------------
## addWidget(arg__1, row, column[, alignment=Qt.Alignment()])

Parameters:

- arg__1 – QWidget
- row – int
- column – int
- alignment – Combination of AlignmentFlag

Adds the given widget to the cell grid at row, column. The top-left position is (0, 0) by default.

The alignment is specified by alignment. The default alignment is 0, which means that the widget fills the entire cell.


--------------------------------
## addWidget(arg__1, row, column, rowSpan, columnSpan[, alignment=Qt.Alignment()])

Parameters:

- arg__1 – QWidget
- row – int
- column – int
- rowSpan – int
- columnSpan – int
- alignment – Combination of AlignmentFlag

This is an overloaded function.

This version adds the given widget to the cell grid, spanning multiple rows/columns. The cell will start at fromRow, fromColumn spanning rowSpan rows and columnSpan columns. The widget will have the given alignment.

If rowSpan and/or columnSpan is -1, then the widget will extend to the bottom and/or right edge, respectively.


--------------------------------
## cellRect(row, column)

Parameters:

- row – int
- column – int

Return type: QRect

Returns the geometry of the cell with row row and column column in the grid. Returns an invalid rectangle if row or column is outside the grid.


--------------------------------
## columnCount()

Return type: int

Returns the number of columns in this grid.


--------------------------------
## columnMinimumWidth(column)

Parameters:

- column – int

Return type: int

Returns the column spacing for column column.


--------------------------------
## columnStretch(column)

Parameters:

- column – int

Return type: int

Returns the stretch factor for column column.


--------------------------------
## getItemPosition(idx)

Parameters:

- idx – int

Return type: PyObject*

Returns the position information of the item with the given index.

The variables passed as row and column are updated with the position of the item in the layout, and the rowSpan and columnSpan variables are updated with the vertical and horizontal spans of the item.


--------------------------------
## horizontalSpacing()

Return type: int


--------------------------------
## itemAtPosition(row, column)

Parameters:

- row – int
- column – int

Return type: QLayoutItem

Returns the layout item that occupies cell (row, column), or None if the cell is empty.


--------------------------------
## originCorner()

Return type: Corner

Returns the corner that’s used for the grid’s origin, i.e. for position (0, 0).


--------------------------------
## rowCount()

Return type: int

Returns the number of rows in this grid.


--------------------------------
## rowMinimumHeight(row)

Parameters:

- row – int

Return type: int

Returns the minimum width set for row row.


--------------------------------
## rowStretch(row)

Parameters:

- row – int

Return type: int

Returns the stretch factor for row row.


--------------------------------
## setColumnMinimumWidth(column, minSize)

Parameters:

- column – int
- minSize – int

Sets the minimum width of column column to minSize pixels.


--------------------------------
## setColumnStretch(column, stretch)

Parameters:

- column – int
- stretch – int

Sets the stretch factor of column column to stretch. The first column is number 0.

The stretch factor is relative to the other columns in this grid. Columns with a higher stretch factor take more of the available space.

The default stretch factor is 0. If the stretch factor is 0 and no other column in this table can grow at all, the column may still grow.

An alternative approach is to add spacing using addItem() with a QSpacerItem .


--------------------------------
## setDefaultPositioning(n, orient)

Parameters:

- n – int
- orient – Orientation


--------------------------------
## setHorizontalSpacing(spacing)

Parameters:

- spacing – int


--------------------------------
## setOriginCorner(arg__1)

Parameters:

- arg__1 – Corner

Sets the grid’s origin corner, i.e. position (0, 0), to corner.


--------------------------------
## setRowMinimumHeight(row, minSize)

Parameters:

- row – int
- minSize – int

Sets the minimum height of row row to minSize pixels.


--------------------------------
## setRowStretch(row, stretch)

Parameters:

- row – int
- stretch – int

Sets the stretch factor of row row to stretch. The first row is number 0.

The stretch factor is relative to the other rows in this grid. Rows with a higher stretch factor take more of the available space.

The default stretch factor is 0. If the stretch factor is 0 and no other row in this table can grow at all, the row may still grow.


--------------------------------
## setVerticalSpacing(spacing)

Parameters:

- spacing – int


--------------------------------
## verticalSpacing()

Return type: int


[Chinese doc](QComboBox.CN.md)

# class QComboBox

The QComboBox widget combines a button with a dropdown list.


# Synopsis

## Properties

- [count](#property-count--int)

    The number of items in the combobox.

- [currentData](#property-currentdata--object)

    The data for the current item.

- [currentIndex](#property-currentindex--int)

    The index of the current item in the combobox.

- [currentText](#property-currenttext--str)

    The current text.

- [duplicatesEnabled](#property-duplicatesenabled--bool)

    Whether the user can enter duplicate items into the combobox.

- [editable](#property-editable--bool)

    Whether the combo box can be edited by the user.

- [frame](#property-frame--bool)

    Whether the combo box draws itself with a frame.

- [iconSize](#property-iconsize--qsize)

    The size of the icons shown in the combobox.

- [insertPolicy](#property-insertpolicy--qcomboboxinsertpolicy)

    The policy used to determine where user-inserted items should appear in the combobox.

- [maxCount](#property-maxcount--int)

    The maximum number of items allowed in the combobox.

- [maxVisibleItems](#property-maxvisibleitems--int)

    The maximum allowed size on screen of the combo box, measured in items.

- [minimumContentsLength](#property-minimumcontentslength--int)

    The minimum number of characters that should fit into the combobox.

- [modelColumn](#property-modelcolumn--int)

    The column in the model that is visible.

- [placeholderText](#property-placeholdertext--str)

    Sets a placeholderText text shown when no valid index is set.

- [sizeAdjustPolicy](#property-sizeadjustpolicy--qcomboboxsizeadjustpolicy)

    The policy describing how the size of the combobox changes when the content changes.


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

A QComboBox is a compact way to present a list of options to the user.

A combobox is a selection widget that shows the current item, and pops up a list of selectable items when clicked. Comboboxes can contain pixmaps as well as strings if the insertItem() and setItemText() functions are suitably overloaded.


## Editing Features

A combobox may be editable, allowing the user to modify each item in the list. For editable comboboxes, the function clearEditText() is provided, to clear the displayed string without changing the combobox’s contents.

When the user enters a new string in an editable combobox, the widget may or may not insert it, and it can insert it in several locations. The default policy is InsertAtBottom but you can change this using setInsertPolicy() .

It is possible to constrain the input to an editable combobox using QValidator; see setValidator() . By default, any input is accepted.

A combobox can be populated using the insert functions, insertItem() and insertItems() for example. Items can be changed with setItemText() . An item can be removed with removeItem() and all items can be removed with clear() . The text of the current item is returned by currentText() , and the text of a numbered item is returned with text(). The current item can be set with setCurrentIndex() . The number of items in the combobox is returned by count() ; the maximum number of items can be set with setMaxCount() . You can allow editing using setEditable() . For editable comboboxes you can set auto-completion using setCompleter() and whether or not the user can add duplicates is set with setDuplicatesEnabled() .


## Signals

There are three signals emitted if the current item of a combobox changes: currentIndexChanged() , currentTextChanged() , and activated() . currentIndexChanged() and currentTextChanged() are always emitted regardless if the change was done programmatically or by user interaction, while activated() is only emitted when the change is caused by user interaction. The highlighted() signal is emitted when the user highlights an item in the combobox popup list. All three signals exist in two versions, one with a QString argument and one with an int argument. If the user selects or highlights a pixmap, only the int signals are emitted. Whenever the text of an editable combobox is changed, the editTextChanged() signal is emitted.


## Model/View Framework

QComboBox uses the model/view framework for its popup list and to store its items. By default a QStandardItemModel stores the items and a QListView subclass displays the popuplist. You can access the model and view directly (with model() and view() ), but QComboBox also provides functions to set and get item data, for example, setItemData() and itemText() . You can also set a new model and view (with setModel() and setView() ). For the text and icon in the combobox label, the data in the model that has the Qt::DisplayRole and Qt::DecorationRole is used.


--------------------------------
## class InsertPolicy

This enum specifies what the QComboBox should do when a new string is entered by the user.

| Constant                       | Description                                                      |
| ------------------------------ | ---------------------------------------------------------------- |
| QComboBox.NoInsert             | The string will not be inserted into the combobox.               |
| QComboBox.InsertAtTop          | The string will be inserted as the first item in the combobox.   |
| QComboBox.InsertAtCurrent      | The current item will be replaced by the string.                 |
| QComboBox.InsertAtBottom       | The string will be inserted after the last item in the combobox. |
| QComboBox.InsertAfterCurrent   | The string is inserted after the current item in the combobox.   |
| QComboBox.InsertBeforeCurrent  | The string is inserted before the current item in the combobox.  |
| QComboBox.InsertAlphabetically | The string is inserted in the alphabetic order in the combobox.  |


--------------------------------
## class SizeAdjustPolicy

This enum specifies how the size hint of the QComboBox should adjust when new content is added or content changes.

| Constant                              | Description                                                          |
| ------------------------------------- | -------------------------------------------------------------------- |
| QComboBox.AdjustToContents            | The combobox will always adjust to the contents                      |
| QComboBox.AdjustToContentsOnFirstShow | The combobox will adjust to its contents the first time it is shown. |
| QComboBox.AdjustToMinimumContentsLengthWithIcon | The combobox will adjust to minimumContentsLength plus space for an icon. For performance reasons use this policy on large models. |


--------------------------------
## property count : int

This property holds the number of items in the combobox..

By default, for an empty combo box, this property has a value of 0.

Access functions:

- count()


--------------------------------
## property currentData : object

This property holds the data for the current item.

By default, for an empty combo box or a combo box in which no current item is set, this property contains an invalid QVariant.

Access functions:

- currentData()


--------------------------------
## property currentIndex : int

This property holds the index of the current item in the combobox..

The current index can change when inserting or removing items.

By default, for an empty combo box or a combo box in which no current item is set, this property has a value of -1.

Access functions:

- currentIndex()
- setCurrentIndex()
- Signal currentIndexChanged()


--------------------------------
## property currentText : str

This property holds the current text.

If the combo box is editable, the current text is the value displayed by the line edit. Otherwise, it is the value of the current item or an empty string if the combo box is empty or no current item is set.

The setter setCurrentText() simply calls setEditText() if the combo box is editable. Otherwise, if there is a matching text in the list, currentIndex is set to the corresponding index.

Access functions:

- currentText()
- setCurrentText()
- Signal currentTextChanged()


--------------------------------
## property duplicatesEnabled : bool

This property holds whether the user can enter duplicate items into the combobox..

Note that it is always possible to programmatically insert duplicate items into the combobox.

By default, this property is false (duplicates are not allowed).

Access functions:

- duplicatesEnabled()
- setDuplicatesEnabled()


--------------------------------
## property editable : bool

This property holds whether the combo box can be edited by the user..

By default, this property is false. The effect of editing depends on the insert policy.

Access functions:

- isEditable()
- setEditable()


--------------------------------
## property frame : bool

This property holds whether the combo box draws itself with a frame..

If enabled (the default) the combo box draws itself inside a frame, otherwise the combo box draws itself without any frame.

Access functions:

- hasFrame()
- setFrame()


--------------------------------
## property iconSize : QSize

This property holds the size of the icons shown in the combobox..

Unless explicitly set this returns the default value of the current style. This size is the maximum size that icons can have; icons of smaller size are not scaled up.

Access functions:

- iconSize()
- setIconSize()


--------------------------------
## property insertPolicy : QComboBox.InsertPolicy

This property holds the policy used to determine where user-inserted items should appear in the combobox..

The default value is InsertAtBottom , indicating that new items will appear at the bottom of the list of items.

Access functions:

- insertPolicy()
- setInsertPolicy()


--------------------------------
## property maxCount : int

This property holds the maximum number of items allowed in the combobox..

By default, this property’s value is derived from the highest signed integer available (typically 2147483647).

Access functions:

- maxCount()
- setMaxCount()


--------------------------------
## property maxVisibleItems : int

This property holds the maximum allowed size on screen of the combo box, measured in items.

By default, this property has a value of 10.

Access functions:

- maxVisibleItems()
- setMaxVisibleItems()


--------------------------------
## property minimumContentsLength : int

This property holds the minimum number of characters that should fit into the combobox..

The default value is 0.

If this property is set to a positive value, the minimumSizeHint() and sizeHint() take it into account.

Access functions:

- minimumContentsLength()
- setMinimumContentsLength()


--------------------------------
## property modelColumn : int

This property holds the column in the model that is visible..

If set prior to populating the combo box, the pop-up view will not be affected and will show the first column (using this property’s default value).

By default, this property has a value of 0.

Access functions:

- modelColumn()
- setModelColumn()


--------------------------------
## property placeholderText : str

This property holds Sets a placeholderText text shown when no valid index is set..

The placeholderText will be shown when an invalid index is set. The text is not accessible in the dropdown list. When this function is called before items are added the placeholder text will be shown, otherwise you have to call setCurrentIndex (-1) programmatically if you want to show the placeholder text. Set an empty placeholder text to reset the setting.

When the QComboBox is editable, use setPlaceholderText() instead.

Access functions:

- placeholderText()
- setPlaceholderText()


--------------------------------
## property sizeAdjustPolicy : QComboBox.SizeAdjustPolicy

This property holds the policy describing how the size of the combobox changes when the content changes..

The default value is AdjustToContentsOnFirstShow .

Access functions:

- sizeAdjustPolicy()
- setSizeAdjustPolicy()


--------------------------------
## __init__([parent=None])

Parameters:

- parent – QWidget

Constructs a combobox with the given parent, using the default model QStandardItemModel.


--------------------------------
## activated(index)

Parameters:

- index – int

This signal is sent when the user chooses an item in the combobox. The item’s index is passed. Note that this signal is sent even when the choice is not changed. If you need to know when the choice actually changes, use signal currentIndexChanged() or currentTextChanged() .


--------------------------------
## addItem(text[, userData=None])

Parameters:

- text – str
- userData – object

Adds an item to the combobox with the given text, and containing the specified userData (stored in the Qt::UserRole). The item is appended to the list of existing items.


--------------------------------
## addItem(icon, text[, userData=None])

Parameters:

- icon – QIcon
- text – str
- userData – object

Adds an item to the combobox with the given icon and text, and containing the specified userData (stored in the Qt::UserRole). The item is appended to the list of existing items.


--------------------------------
## addItems(texts)

Parameters:

- texts – list of strings

Adds each of the strings in the given texts to the combobox. Each item is appended to the list of existing items in turn.


--------------------------------
## clear()

Clears the combobox, removing all items.


--------------------------------
## clearEditText()

Clears the contents of the line edit used for editing in the combobox.


--------------------------------
## completer()

Return type: QCompleter

Returns the completer that is used to auto complete text input for the combobox.


--------------------------------
## count()

Return type: int

Getter of property count  .


--------------------------------
## currentData([role=Qt.UserRole])

Parameters:

- role – int

Return type: object


--------------------------------
## currentIndex()

Return type: int

Getter of property currentIndex  .


--------------------------------
## currentIndexChanged(index)

Parameters:

- index – int

This signal is sent whenever the currentIndex in the combobox changes either through user interaction or programmatically. The item’s index is passed or -1 if the combobox becomes empty or the currentIndex was reset.

Notification signal of property currentIndex  .


--------------------------------
## currentText()

Return type: str

Getter of property currentText  .


--------------------------------
## currentTextChanged(arg__1)

Parameters:

- arg__1 – str

This signal is emitted whenever currentText changes. The new value is passed as text.

Notification signal of property currentText  .


--------------------------------
## duplicatesEnabled()

Return type: bool

Getter of property duplicatesEnabled  .


--------------------------------
## editTextChanged(arg__1)

Parameters:

- arg__1 – str

This signal is emitted when the text in the combobox’s line edit widget is changed. The new text is specified by text.


--------------------------------
## findData(data[, role=Qt.UserRole[, flags=static_cast<Qt.MatchFlags>(Qt.MatchExactly|Qt.MatchCaseSensitive)]])

Parameters:

- data – object
- role – int
- flags – Combination of MatchFlag

Return type: int

Returns the index of the item containing the given data for the given role; otherwise returns -1.

The flags specify how the items in the combobox are searched.


--------------------------------
## findText(text[, flags=static_cast<Qt.MatchFlags>(Qt.MatchExactly|Qt.MatchCaseSensitive)])

Parameters:

- text – str
- flags – Combination of MatchFlag

Return type: int

Returns the index of the item containing the given text; otherwise returns -1.

The flags specify how the items in the combobox are searched.


--------------------------------
## hasFrame()

Return type: bool

Getter of property frame  .

--------------------------------
## hidePopup()

Hides the list of items in the combobox if it is currently visible and resets the internal state, so that if the custom pop-up was shown inside the reimplemented showPopup() , then you also need to reimplement the hidePopup() function to hide your custom pop-up and call the base class implementation to reset the internal state whenever your custom pop-up widget is hidden.


--------------------------------
## highlighted(index)

Parameters:

- index – int

This signal is sent when an item in the combobox popup list is highlighted by the user. The item’s index is passed.


--------------------------------
## iconSize()

Return type: QSize

Getter of property iconSize  .


--------------------------------
## initStyleOption(option)

Parameters:

- option – QStyleOptionComboBox

Initialize option with the values from this QComboBox . This method is useful for subclasses when they need a QStyleOptionComboBox , but don’t want to fill in all the information themselves.


--------------------------------
## inputMethodQuery(query, argument)

Parameters:

- query – InputMethodQuery
- argument – object

Return type: object


--------------------------------
## insertItem(index, icon, text[, userData=None])

Parameters:

- index – int
- icon – QIcon
- text – str
- userData – object

Inserts the icon, text and userData (stored in the Qt::UserRole) into the combobox at the given index.

If the index is equal to or higher than the total number of items, the new item is appended to the list of existing items. If the index is zero or negative, the new item is prepended to the list of existing items.


--------------------------------
## insertItem(index, text[, userData=None])

Parameters:

- index – int
- text – str
- userData – object

Inserts the text and userData (stored in the Qt::UserRole) into the combobox at the given index.

If the index is equal to or higher than the total number of items, the new item is appended to the list of existing items. If the index is zero or negative, the new item is prepended to the list of existing items.


--------------------------------
## insertItems(index, texts)

Parameters:

- index – int
- texts – list of strings

Inserts the strings from the list into the combobox as separate items, starting at the index specified.

If the index is equal to or higher than the total number of items, the new items are appended to the list of existing items. If the index is zero or negative, the new items are prepended to the list of existing items.


--------------------------------
## insertPolicy()

Return type: InsertPolicy

Getter of property insertPolicy  .


--------------------------------
## insertSeparator(index)

Parameters:

- index – int

Inserts a separator item into the combobox at the given index.

If the index is equal to or higher than the total number of items, the new item is appended to the list of existing items. If the index is zero or negative, the new item is prepended to the list of existing items.


--------------------------------
## isEditable()

Return type: bool

Getter of property editable  .


--------------------------------
## itemData(index[, role=Qt.UserRole])

Parameters:

- index – int
- role – int

Return type: object

Returns the data for the given role in the given index in the combobox, or an invalid QVariant if there is no data for this role.


--------------------------------
## itemDelegate()

Return type: QAbstractItemDelegate

Returns the item delegate used by the popup list view.


--------------------------------
## itemIcon(index)

Parameters:

- index – int

Return type: QIcon

Returns the icon for the given index in the combobox.


--------------------------------
## itemText(index)

Parameters:

- index – int

Return type: str

Returns the text for the given index in the combobox.


--------------------------------
## lineEdit()

Return type: QLineEdit

Returns the line edit used to edit items in the combobox, or None if there is no line edit.

Only editable combo boxes have a line edit.


--------------------------------
## maxCount()

Return type: int

Getter of property maxCount  .


--------------------------------
## maxVisibleItems()

Return type: int

Getter of property maxVisibleItems  .


--------------------------------
## minimumContentsLength()

Return type: int

Getter of property minimumContentsLength  .


--------------------------------
## model()

Return type: QAbstractItemModel

Returns the model used by the combobox.


--------------------------------
## modelColumn()

Return type: int

Getter of property modelColumn  .


--------------------------------
## placeholderText()

Return type: str

Getter of property placeholderText  .


--------------------------------
## removeItem(index)

Parameters:

- index – int

Removes the item at the given index from the combobox. This will update the current index if the index is removed.

This function does nothing if index is out of range.


--------------------------------
## rootModelIndex()

Return type: QModelIndex

Returns the root model item index for the items in the combobox.


--------------------------------
## setCompleter(c)

Parameters:

- c – QCompleter

Sets the completer to use instead of the current completer. If completer is None, auto completion is disabled.

By default, for an editable combo box, a QCompleter that performs case insensitive inline completion is automatically created.


--------------------------------
## setCurrentIndex(index)

Parameters:

- index – int

Setter of property currentIndex  .


--------------------------------
## setCurrentText(text)

Parameters:

- text – str

Setter of property currentText  .


--------------------------------
## setDuplicatesEnabled(enable)

Parameters:

- enable – bool

Setter of property duplicatesEnabled  .


--------------------------------
## setEditText(text)

Parameters:

- text – str

Sets the text in the combobox’s text edit.


--------------------------------
## setEditable(editable)

Parameters:

- editable – bool

Setter of property editable  .


--------------------------------
## setFrame(arg__1)

Parameters:

- arg__1 – bool

Setter of property frame  .


--------------------------------
## setIconSize(size)

Parameters:

- size – QSize

Setter of property iconSize  .


--------------------------------
## setInsertPolicy(policy)

Parameters:

- policy – InsertPolicy

Setter of property insertPolicy  .


--------------------------------
## setItemData(index, value[, role=Qt.UserRole])

Parameters:

- index – int
- value – object
- role – int

Sets the data role for the item on the given index in the combobox to the specified value.


--------------------------------
## setItemDelegate(delegate)

Parameters:

- delegate – QAbstractItemDelegate

Sets the item delegate for the popup list view. The combobox takes ownership of the delegate.

Any existing delegate will be removed, but not deleted. QComboBox does not take ownership of delegate.


--------------------------------
## setItemIcon(index, icon)

Parameters:

- index – int
- icon – QIcon

Sets the icon for the item on the given index in the combobox.


--------------------------------
## setItemText(index, text)

Parameters:

- index – int
- text – str

Sets the text for the item on the given index in the combobox.


--------------------------------
## setLineEdit(edit)

Parameters:

- edit – QLineEdit

Sets the line edit to use instead of the current line edit widget.

The combo box takes ownership of the line edit.


--------------------------------
## setMaxCount(max)

Parameters:

- max – int

Setter of property maxCount  .


--------------------------------
## setMaxVisibleItems(maxItems)

Parameters:

- maxItems – int

Setter of property maxVisibleItems  .


--------------------------------
## setMinimumContentsLength(characters)

Parameters:

- characters – int

Setter of property minimumContentsLength  .


--------------------------------
## setModel(model)

Parameters:

- model – QAbstractItemModel

Sets the model to be model. model must not be None. If you want to clear the contents of a model, call clear() .


--------------------------------
## setModelColumn(visibleColumn)

Parameters:

- visibleColumn – int

Setter of property modelColumn  .


--------------------------------
## setPlaceholderText(placeholderText)

Parameters:

- placeholderText – str

Setter of property placeholderText  .


--------------------------------
## setRootModelIndex(index)

Parameters:

- index – QModelIndex

Sets the root model item index for the items in the combobox.


--------------------------------
## setSizeAdjustPolicy(policy)

Parameters:

- policy – SizeAdjustPolicy

Setter of property sizeAdjustPolicy  .


--------------------------------
## setValidator(v)

Parameters:

- v – QValidator

Sets the validator to use instead of the current validator.


--------------------------------
## setView(itemView)

Parameters:

- itemView – QAbstractItemView

Sets the view to be used in the combobox popup to the given itemView. The combobox takes ownership of the view.

Note: If you want to use the convenience views (like QListWidget , QTableWidget or QTreeWidget ), make sure to call setModel() on the combobox with the convenience widgets model before calling this function.


--------------------------------
## showPopup()

Displays the list of items in the combobox. If the list is empty then no items will be shown.

If you reimplement this function to show a custom pop-up, make sure you call hidePopup() to reset the internal state.


--------------------------------
## sizeAdjustPolicy()

Return type: SizeAdjustPolicy

Getter of property sizeAdjustPolicy  .


--------------------------------
## textActivated(arg__1)

Parameters:

- arg__1 – str

This signal is sent when the user chooses an item in the combobox. The item’s text is passed. Note that this signal is sent even when the choice is not changed. If you need to know when the choice actually changes, use signal currentIndexChanged() or currentTextChanged() .


--------------------------------
## textHighlighted(arg__1)

Parameters:

- arg__1 – str

This signal is sent when an item in the combobox popup list is highlighted by the user. The item’s text is passed.


--------------------------------
## validator()

Return type: QValidator

Returns the validator that is used to constrain text input for the combobox.


--------------------------------
## view()

Return type: QAbstractItemView

Returns the list view used for the combobox popup.

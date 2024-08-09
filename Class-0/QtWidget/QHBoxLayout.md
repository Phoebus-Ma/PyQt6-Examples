
[Chinese doc](QHBoxLayout.CN.md)

# class QHBoxLayout

The QHBoxLayout class lines up widgets horizontally.


# Synopsis

## Methods

- [def \_\_init__()](#init)

## Detailed Description

This class is used to construct horizontal box layout objects. See QBoxLayout for details.

The simplest use of the class is like this:

```python
window = QWidget()
button1 = QPushButton("One")
button2 = QPushButton("Two")
button3 = QPushButton("Three")
button4 = QPushButton("Four")
button5 = QPushButton("Five")

layout = QHBoxLayout(window)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)
window.show()
```

First, we create the widgets we want to add to the layout. Then, we create the QHBoxLayout object, setting window as parent by passing it in the constructor; next we add the widgets to the layout. window will be the parent of the widgets that are added to the layout.

If you don’t pass a parent window to the constructor, you can at a later point use setLayout() to install the QHBoxLayout object onto window. At that point, the widgets in the layout are reparented to have window as their parent.


--------------------------------
## __init__()

Constructs a new horizontal box. You must add it to another layout.


--------------------------------
## __init__(parent)

Parameters:

- parent – QWidget

Constructs a new top-level horizontal box with parent parent.

The layout is set directly as the top-level layout for parent. There can be only one top-level layout for a widget. It is returned by layout() .

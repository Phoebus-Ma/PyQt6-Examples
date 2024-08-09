
[English doc](QVBoxLayout.md)

# class QVBoxLayout

QVBoxLayout 类垂直排列小部件。


# Synopsis

## Methods

- [def \_\_init__()](#init)


## Detailed Description

此类用于构造垂直框布局对象。详情请参阅 QBoxLayout。

该类的最简单用法如下：

```python
window = QWidget()
button1 = QPushButton("One")
button2 = QPushButton("Two")
button3 = QPushButton("Three")
button4 = QPushButton("Four")
button5 = QPushButton("Five")

layout = QVBoxLayout(window)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)
window.show()
```

首先，我们创建要添加到布局中的小部件。然后，我们创建 QVBoxLayout 对象，并通过在构造函数中传递它来将窗口设置为父级；接下来，我们将小部件添加到布局中。窗口将是添加到布局中的小部件的父级。

如果您没有将父窗口传递给构造函数，您可以在稍后使用 setLayout() 将 QVBoxLayout 对象安装到窗口上。此时，布局中的小部件将重新设置为以窗口为父级。


--------------------------------
## __init__()

构造一个新的垂直框。您必须将其添加到另一个布局中。


--------------------------------
## __init__(parent)

参数:

- parent – QWidget

构造一个新的顶层垂直框，其父级为 parent。

布局直接设置为 parent 的顶层布局。每个小部件只能有一个顶层布局。它由 layout() 返回。

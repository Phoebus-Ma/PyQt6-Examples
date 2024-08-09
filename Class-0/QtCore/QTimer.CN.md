
[English doc](QTimer.md)

# class QTimer

QTimer 类提供重复和单次计时器。


# Synopsis

## Properties

- [active](#property-active--bool)

- [interval](#property-interval--int)

    超时间隔（以毫秒为单位）。

- [remainingTime](#property-remainingtime--int)

    剩余时间（以毫秒为单位）。

- [singleShot](#property-singleshot--bool)

    计时器是否为单次计时器。

- [timerType](#property-timertype--qttimertype)

    控制计时器的准确性。


## Methods

- [def \_\_init__()](#initparentnone)

- [def interval()](#interval)

- [def isActive()](#isactive)

- [def isSingleShot()](#issingleshot)

- [def remainingTime()](#remainingtime)

- [def setInterval()](#setintervalmsec)

- [def setSingleShot()](#setsingleshotsingleshot)

- [def setTimerType()](#settimertypeatype)

- [def timerId()](#timerid)

- [def timerType()](#timertype)


## Slots

- [def start()](#start)

- [def stop()](#stop)


## Signals

- [def timeout()](#timeout)


## Static functions

- [def singleShot()](#static-singleshotmsec-context-functor)


## Detailed Description

QTimer 类为计时器提供了高级编程接口。要使用它，请创建一个 QTimer ，将其 timeout() 信号连接到适当的插槽，然后调用 start() 。从那时起，它将以恒定的间隔发出 timeout() 信号。

一秒（1000 毫秒）计时器的示例（来自模拟时钟示例）：

```python
timer = QTimer(self)
timer.timeout.connect(this, QOverload<>::of(&AnalogClock::update))
timer.start(1000)
```

从那时起，update() 槽每秒都会被调用一次。

您可以通过调用 setSingleShot (true) 将计时器设置为仅超时一次。您还可以使用静态 singleShot() 函数在指定间隔后调用槽：

```python
QTimer::singleShot(200, self.updateCaption)
```

在多线程应用程序中，您可以在任何具有事件循环的线程中使用 QTimer。要从非 GUI 线程启动事件循环，请使用 exec() 。Qt 使用计时器的线程亲和性来确定哪个线程将发出 timeout() 信号。因此，您必须在其线程中启动和停止计时器；无法从另一个线程启动计时器。

作为一种特殊情况，超时为 0 的 QTimer 将尽快超时，尽管零计时器和其他事件源之间的顺序未指定。零计时器可用于执行某些工作，同时仍提供敏捷的用户界面：

```python
timer = QTimer(self)
timer.timeout.connect(self.processOneThing)
timer.start()
```

从此以后，processOneThing() 将被重复调用。应以始终快速返回（通常在处理一个数据项后）的方式编写它，以便 Qt 可以将事件传递到用户界面并在完成所有工作后立即停止计时器。这是在 GUI 应用程序中实现繁重工作的传统方式，但随着多线程如今在越来越多的平台上可用，我们预计零毫秒 QTimer 对象将逐渐被 QThread 取代。


## Accuracy and Timer Resolution

计时器的精度取决于底层操作系统和硬件。大多数平台支持 1 毫秒的精度，但在很多实际情况下，计时器的精度不会等于此精度。

精度还取决于计时器类型。对于 PreciseTimer ，QTimer 将尝试将精度保持在 1 毫秒。精确计时器也绝不会比预期更早超时。

对于 CoarseTimer 和 VeryCoarseTimer 类型，QTimer 可能会比预期更早唤醒，在这些类型的范围内：CoarseTimer 为间隔的 5%，VeryCoarseTimer 为 500 毫秒。

如果系统繁忙或无法提供所要求的精度，所有计时器类型的超时都可能比预期更晚。在这种超时超限的情况下，Qt 只会发出一次 timeout()，即使多个超时已过期，然后将恢复原始间隔。


## Alternatives to QTimer

使用 QTimer 的另一种方法是调用对象的 startTimer() 并在类中重新实现 timerEvent() 事件处理程序（必须继承 QObject ）。缺点是 timerEvent() 不支持单次定时器或信号等高级功能。

另一种替代方案是 QBasicTimer 。它通常比直接使用 startTimer() 更省事。请参阅计时器以了解所有三种方法的概述。

某些操作系统限制可使用的计时器数量；Qt 会尝试解决这些限制。


--------------------------------
## property active : bool

如果计时器正在运行，则此布尔属性为真；否则为假。

访问功能：

- isActive()


--------------------------------
## property interval : int

此属性保存超时间隔（以毫秒为单位）。

此属性的默认值为 0。超时间隔为 0 的 QTimer 将在窗口系统事件队列中的所有事件处理完毕后立即超时。

设置活动计时器的间隔会更改其 timerId() 。

访问功能：

- interval()
- setInterval()


--------------------------------
## property remainingTime : int

此属性保存剩余时间（以毫秒为单位）。

返回计时器在超时前剩余的毫秒值。如果计时器处于非活动状态，则返回值为 -1。如果计时器已过期，则返回值为 0。

访问功能：

- remainingTime()


--------------------------------
## property singleShot : bool

此属性保存计时器是否为单次计时器。

单次计时器仅触发一次，非单次计时器每隔几毫秒触发一次。

此属性的默认值为 false。

访问功能：

- isSingleShot()
- setSingleShot()


--------------------------------
## property timerType : Qt.TimerType

此属性控制计时器的准确性。

此属性的默认值为 Qt::CoarseTimer。

访问功能：

- timerType()
- setTimerType()


--------------------------------
## __init__([parent=None])

参数：

- parent – QObject

使用给定的父级构造一个计时器。


--------------------------------
## interval()

返回类型：int

属性 interval 的获取器。


--------------------------------
## isActive()

返回类型：bool

如果计时器正在运行（待处理），则返回 true；否则返回 false。

属性 active 的获取器。


--------------------------------
## isSingleShot()

返回类型：bool

属性 singleShot 的获取器。


--------------------------------
## remainingTime()

返回类型：int

属性 remainingTime 的获取器。


--------------------------------
## setInterval(msec)

参数：

- msec – int

属性 interval 的设置者。


--------------------------------
## setSingleShot(singleShot)

参数：

- singleShot – bool

属性 singleShot 的设置者。


--------------------------------
## setTimerType(atype)

参数：

- atype – TimerType

属性timerType的设置者。


--------------------------------
## static singleShot(msec, timerType, receiver, member)

参数：

- msec – int
- timerType – TimerType
- receiver – QObject
- member – str

这是一个重载函数。

这个静态函数在给定的时间间隔后调用一个槽。

使用这个函数非常方便，因为您不需要为 timerEvent 烦恼，也不需要创建本地 QTimer 对象。

接收器是接收对象，成员是槽。时间间隔是 msec 毫秒。 timerType 影响计时器的准确性。


--------------------------------
## static singleShot(msec, receiver, member)

参数：

- msec – int
- receiver – QObject
- member – str

此静态函数在给定的时间间隔后调用一个槽。

使用此函数非常方便，因为您不需要担心 timerEvent 或创建本地 QTimer 对象。

示例：

```python
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
if __name__ == "__main__":

    app = QApplication([])
    QTimer.singleShot(600000, app, QCoreApplication.quit)
    ...
    sys.exit(app.exec())
```

此示例程序在 10 分钟（600,000 毫秒）后自动终止。

接收器为接收对象，成员为槽。时间间隔为 msec 毫秒。


--------------------------------
## static singleShot(msec, context, functor)

参数：

- msec – int
- context – QObject
- functor – PyCallable


--------------------------------
## static singleShot(msec, functor)

参数：

- msec – int
- functor – PyCallable


--------------------------------
## start()

此函数重载 start()。

使用 interval 中指定的超时时间启动或重新启动计时器。

如果计时器已在运行，则将停止并重新启动。

如果 singleShot 为 true，则计时器将仅激活一次。


--------------------------------
## start(msec)

参数：

- msec – int

以 msec 毫秒的超时间隔启动或重新启动计时器。

如果计时器已在运行，则将停止并重新启动。

如果 singleShot 为真，则计时器将仅激活一次。这相当于：

```bash
timer.setInterval(msec);
timer.start();
```


--------------------------------
## stop()

停止计时器。


--------------------------------
## timeout()

当计时器超时时发出此信号。


--------------------------------
## timerId()

返回类型：int

如果计时器正在运行，则返回计时器的 ID；否则返回 -1。


--------------------------------
## timerType()

返回类型：TimerType

属性 timerType 的获取器。

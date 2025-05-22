###
# PyQt6 GraphicsView main window.
#
# License - MIT.
###

from PyQt6.QtCore import QRectF, QPointF
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsEllipseItem,
    QGraphicsPolygonItem
)
from PyQt6.QtGui import (
    QBrush,
    QColor,
    QPolygonF
)


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        self.title     = 'GraphicsView'
        self.winWidth  = 320
        self.winHeight = 240

        self.initUI()
    # }

    def initUI(self):
    # {
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.winWidth, self.winHeight)

        layout = QVBoxLayout()

        # Create a QGraphicsView.
        self.graphicsView = QGraphicsView()

        # Creat a QGraphicsScene.
        self.scene = QGraphicsScene()

        # Set scene rectangle.
        self.scene.setSceneRect(0, 0, 400, 300)

        # Add graphics to scene.
        self.addItemsToScene()

        # GraphicsView setup scene.
        self.graphicsView.setScene(self.scene)

        layout.addWidget(self.graphicsView)
        self.setLayout(layout)
    # }

    def addItemsToScene(self):
    # {
        # Add a rectangle.
        rectItem = QGraphicsRectItem(QRectF(50, 50, 100, 100))
        rectItem.setBrush(QBrush(QColor(255, 0, 0)))    # Red.
        self.scene.addItem(rectItem)

        # Add a circle.
        ellipseItem = QGraphicsEllipseItem(QRectF(200, 50, 100, 100))
        ellipseItem.setBrush(QBrush(QColor(0, 255, 0))) # Green.
        self.scene.addItem(ellipseItem)

        # Add a triangle.
        triangle = QPolygonF()
        triangle.append(QPointF(200, 200))
        triangle.append(QPointF(250, 250))
        triangle.append(QPointF(150, 250))
        triItem = QGraphicsPolygonItem(triangle)
        triItem.setBrush(QBrush(QColor(0, 0, 255)))     # Blue.
        self.scene.addItem(triItem)
    # }
# }

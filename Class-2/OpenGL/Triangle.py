###
# PyQt6 OpenGL triangle.
#
# License - MIT.
###

from PyQt6.QtCore import QTimer
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
# pip install PyOpenGL
from OpenGL.GL import *


class Triangle(QOpenGLWidget):
# {
    def __init__(self, parent=None):
    # {
        super().__init__(parent)

        # Rotation angle.
        self.rotation = 0.0

        # Set the animation timer.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_rotation)
        self.timer.start(30)  # Refresh every 30ms.
    # }

    """Initialize OpenGL"""
    def initializeGL(self):
    # {
        # Set the background color (dark gray).
        glClearColor(0.1, 0.1, 0.1, 1.0)

        # Enable depth test.
        glEnable(GL_DEPTH_TEST)
    # }

    """Handle window size changes"""
    def resizeGL(self, w, h):
    # {
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspect = (w / h) if (h != 0) else 1.0
        glOrtho(-aspect, aspect, -1, 1, -1, 1)  # Orthogonal projection.

        glMatrixMode(GL_MODELVIEW)
    # }

    """Performing a draw operation"""
    def paintGL(self):
    # {
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Apply rotation.
        glRotatef(self.rotation, 0, 0, 1)

        # Draw colored triangles.
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)   # Red vertex.
        glVertex2f(-0.6, -0.6)

        glColor3f(0.0, 1.0, 0.0)   # Green vertex.
        glVertex2f(0.6, -0.6)

        glColor3f(0.0, 0.0, 1.0)   # Blue vertex.
        glVertex2f(0.0, 0.6)
        glEnd()
    # }

    """Update rotation angle"""
    def update_rotation(self):
    # {
        self.rotation = (self.rotation + 2) % 360
        self.update()
    # }
# }

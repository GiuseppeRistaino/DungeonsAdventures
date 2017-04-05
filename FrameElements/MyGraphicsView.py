import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyGraphicsView(QGraphicsView):
    def __init__(self):
        super(QGraphicsView,self).__init__()
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        #self.setAcceptDrops(True)
        #self.setDragMode(QGraphicsView.ScrollHandDrag)

        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()
        self.isRubber = False


    def wheelEvent(self, event):
        adj = (event.delta()/120) * 0.1
        self.scale(1+adj, 1+adj)


    def mouseMoveEvent(self, event):
        if self.scene().state == "SELECT":
            if self.isRubber:
                self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
        else:
            self.rubberBand.hide()
        QGraphicsView.mouseMoveEvent(self, event)

    def mousePressEvent(self, event):
        if self.scene().state == "SELECT":
            if event.button() == Qt.LeftButton:
                self.isRubber = True
                self.origin = QPoint(event.pos())
                self.rubberBand.setGeometry(QRect(self.origin, QSize()))
                self.rubberBand.show()
        else:
            self.rubberBand.hide()
        QGraphicsView.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self.scene().state == "SELECT":
            self.isRubber = False
        QGraphicsView.mouseReleaseEvent(self, event)




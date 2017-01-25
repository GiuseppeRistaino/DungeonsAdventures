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

    def wheelEvent(self, event):
        adj = (event.delta()/120) * 0.1
        self.scale(1+adj, 1+adj)
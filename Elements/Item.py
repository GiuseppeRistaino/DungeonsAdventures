from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Item(QGraphicsPixmapItem):
    def __init__(self, pixmap, x=None, y=None, parent=None, scene=None, pathRes=None, rotate=0):
        super(Item, self).__init__(pixmap, parent, scene)
        self.pixmap = pixmap
        self.x = x
        self.y = y
        self.parent = parent
        self.scene = scene
        self.pathRes = pathRes
        self.rotate=rotate
        centerX = self.boundingRect().width() / 2
        centerY = self.boundingRect().height() / 2
        self.setTransformOriginPoint(QPointF(centerX, centerY))
        self.setRotation(self.rotate)
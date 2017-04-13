from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Place(QGraphicsPixmapItem):
    def __init__(self, pixmap, x=None, y=None, parent=None, scene=None, pathRes=None):
        super(Place, self).__init__(pixmap, parent, scene)
        self.pixmap = pixmap
        self.x = x
        self.y = y
        self.parent = parent
        self.scene = scene
        self.pathRes = pathRes
        self.dungeons = []
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def addDungeon(self, scene):
        isNew = True
        for d in self.dungeons:
            if d.name == scene.name:
                isNew = False
        if isNew:
            self.dungeons.append(scene)


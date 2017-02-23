from PyQt4.QtGui import *


class Terrain(QGraphicsPixmapItem):

    def __init__(self, pixmap, x=None, y=None, parent=None, scene=None, pathRes=None):
        super(Terrain, self).__init__(pixmap, parent, scene)
        self.pixmap = pixmap
        self.x = x
        self.y = y
        self.parent = parent
        self.scene = scene
        self.pathRes = pathRes
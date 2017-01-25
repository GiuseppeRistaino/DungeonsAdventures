from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Text(QGraphicsTextItem):

    def __init__(self, string, x= None, y=None, parent=None, scene=None):
        super(Text, self).__init__(string, parent, scene)
        self.string = string
        self.x=x
        self.y=y
        self.parent = parent
        self.scene = scene
        self.font = QFont("Times", 12, QFont.Normal, True)
        self.setFont(self.font)
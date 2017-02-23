from PyQt4.QtGui import *


class MyGraphicsView(QGraphicsView):
    def __init__(self):
        super(QGraphicsView,self).__init__()
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):
        adj = (event.delta()/120) * 0.1
        self.scale(1+adj, 1+adj)
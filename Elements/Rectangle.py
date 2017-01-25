from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Elements.Terrain import *
from Elements.Item import *
from Elements.Place import *
from Elements.Text import *

class Rectangle(QGraphicsRectItem):

    def __init__(self, x, y, width, height, parent=None, scene=None, terrain=None, item=None, place=None, text=None):
        super(Rectangle, self).__init__(x, y, width, height, parent, scene)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.parent = parent
        self.scene = scene
        self.terrain = terrain
        self.item = item
        self.place = place
        self.text = text
        self.dungeonIcon = None

    def removeChildsFromScene(self):
        listChilds = self.childItems()
        for child in listChilds:
            self.scene.removeItem(child)

    def removePlace(self):
        listChilds = self.childItems()
        for child in listChilds:
            if isinstance(child, Place):
                self.scene.removeItem(child)

    def removeTerrain(self):
        listChilds = self.childItems()
        for child in listChilds:
            if isinstance(child, Terrain):
                self.scene.removeItem(child)

    def removeItems(self):
        self.terrain = None
        self.item = None
        self.place = None
        self.text = None
        self.dungeonIcon = None
        self.scene.deleteItems(self)

    def addText(self, text):
        self.removeChildsFromScene()
        self.text = Text(text.string, self.boundingRect().x(), self.boundingRect().y())
        self.text.setPos(self.boundingRect().x(), self.boundingRect().y())
        self.draw()

    def addPlace(self, place):
        self.removeChildsFromScene()
        self.place = Place(QPixmap(place.pathRes), self.boundingRect().x(), self.boundingRect().y(), pathRes=place.pathRes)
        for dung in place.dungeons:
            self.addNewDungeon(dung)
        self.place.setPos(self.boundingRect().x(), self.boundingRect().y())
        self.draw()


    def addTerrain(self, terrain):
        self.removeChildsFromScene()
        self.terrain = Terrain(QPixmap(terrain.pathRes), pathRes=terrain.pathRes)
        self.terrain.setPos(self.boundingRect().x(), self.boundingRect().y())
        self.draw()

    def addItem(self, item):
        self.removeChildsFromScene()
        self.item = Item(QPixmap(item.pathRes), rotate=item.rotate, pathRes=item.pathRes)
        self.item.setPos(self.boundingRect().x(), self.boundingRect().y())
        self.draw()

    def addDungeonIcon(self):
        self.removeChildsFromScene()
        self.dungeonIcon = QGraphicsPixmapItem(QPixmap("img/dungeon_icon.png"))
        self.dungeonIcon.setPos(self.boundingRect().x(), self.boundingRect().y())
        self.draw()

    def rotateItem(self):
        if self.item is not None:
            centerX = self.item.boundingRect().width() / 2
            centerY = self.item.boundingRect().height() / 2
            self.item.setTransformOriginPoint(QPointF(centerX, centerY))
            print(self.item.rotation)
            self.item.setRotation(self.item.rotation() + 90)
            self.item.rotate = self.item.rotation()

    def draw(self):
        # Disegna
        if self.terrain is not None:
            self.terrain.setParentItem(self)
        if self.item is not None:
            self.item.setParentItem(self)
        if self.place is not None:
            self.place.setParentItem(self)
        if self.text is not None:
            self.text.setParentItem(self)
        if self.dungeonIcon is not None:
            self.dungeonIcon.setParentItem(self)



    def getListDungeons(self):
        if self.place is not None:
            return self.place.dungeons
        return None

    def addNewDungeon(self, scene):
        if self.place is not None:
            self.place.addDungeon(scene)
            self.addDungeonIcon()



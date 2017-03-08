import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Dialogs.DialogAddNpg import DialogAddNpg
from Elements.Rectangle import *
from Dialogs.DialogTextOnMap import *
from Dialogs.DialogNewDungeon import *
from Dialogs.DialogViewDungeons import *
from Dialogs.DialogAddNpg import *

class Scene(QGraphicsScene):

    HEIGTH_RECT = 50
    WIDTH_RECT = 50
    STATES = ["CANC", "TEXT", "MAP", "DROP", "ROTATE", "VIEW", "DRAG", "INFO"]

    def __init__(self, numRow, numColumn, name=None, places=None):
        super(Scene, self).__init__()
        self.name = name
        self.numRow = numRow
        self.numColumn = numColumn
        self.chess = []
        self.places = places
        self.itemToDraw = None
        self.state = None
        self.itemToDrop = None
        self.npgs = []

        self.drawChess(self.numRow, self.numColumn)


    def drawChess(self, numRow, numColumn):
        self.setSceneRect(0, 0, self.HEIGTH_RECT * numColumn, self.WIDTH_RECT * numRow)
        for i in range(0, numRow):
            for j in range(0, numColumn):
                rect = Rectangle(j*self.WIDTH_RECT, i*self.HEIGTH_RECT, self.WIDTH_RECT,self.HEIGTH_RECT, scene=self)
                self.chess.append(rect)

    def mouseMoveEvent(self, event):
        coord = event.scenePos()
        rect = self.isPointOnItemRect(coord.x(), coord.y())
        self.manageStateEvent(event, rect)
        if isinstance(self.itemToDrop, Npg):
            for npg in self.npgs:
                if self.itemToDrop == npg:
                    self.itemToDrop.setPos(coord.x()-self.itemToDrop.boundingRect().width() / 2, coord.y()-self.itemToDrop.boundingRect().height() / 2)
                    self.itemToDrop.x = coord.x()-self.itemToDrop.boundingRect().width() / 2
                    self.itemToDrop.y = coord.y()-self.itemToDrop.boundingRect().height() / 2

    def mousePressEvent(self, event):
        coord = event.scenePos()
        rect = self.isPointOnItemRect(coord.x(), coord.y())
        self.manageStateEvent(event, rect)
        if event.buttons() == Qt.RightButton:
            if isinstance(self.itemToDraw, Npg):
                if self.isPointOnNpg(coord.x(), coord.y()) is None:
                    self.dialog = DialogAddNpg(self, rect)
                    self.dialog.show()
        if self.state == self.STATES[1]:
            if event.buttons() == Qt.LeftButton:
                if rect is not None:
                    # Metti del testo sulla mappa
                    self.dialog = DialogTextOnMap(rect)
                    self.dialog.show()
        if self.state == self.STATES[2]:
            if event.buttons() == Qt.LeftButton:
               if rect is not None and rect.place is not None:
                    # Aggiungi un dungeon
                    self.dialog = DialogNewDungeon(rect)
                    self.dialog.show()
        if self.state == self.STATES[5]:
            if event.buttons() == Qt.LeftButton:
               if rect is not None and rect.place is not None:
                    # Visualizza un dungeon
                    self.dialog = DialogViewDungeons(rect)
                    self.dialog.show()
        if self.state == self.STATES[6]:
            if event.buttons() == Qt.LeftButton:
                item = self.itemAt(coord.x(), coord.y())
                if item == self.itemToDrop:
                    self.itemToDrop.x = rect.boundingRect().x()
                    self.itemToDrop.y = rect.boundingRect().y()
                    self.itemToDrop.setPos(rect.boundingRect().x(), rect.boundingRect().y())
                    self.itemToDrop = None
                else:
                    if isinstance(item, Npg):
                        self.itemToDrop = item
        if self.state == self.STATES[7]:
            if event.buttons() == Qt.LeftButton:
                npg = self.isPointOnNpg(coord.x(), coord.y())
                if npg is not None:
                    self.msg = QMessageBox()
                    self.msg.setText(npg.name)
                    self.msg.setWindowTitle("Info Npg")
                    self.msg.show()

    def manageStateEvent(self, event, rect=None):
        coord = event.scenePos()
        if event.buttons() == Qt.RightButton:
            if rect is not None:
                #Disegna
                if isinstance(self.itemToDraw, Place):
                    rect.addPlace(self.itemToDraw)
        if self.state == self.STATES[0]:
            if event.buttons() == Qt.LeftButton:
                if rect is not None:
                    # Cancella
                    rect.removeItems()
                item = self.itemAt(coord.x(), coord.y())
                if isinstance(item, Npg):
                    for npg in self.npgs:
                        if npg == item:
                            self.npgs.remove(npg)
                            self.removeItem(npg)




    def isPointOnItemRect(self, x, y):
        for rect in self.chess:
            if rect.boundingRect().contains(x, y):
                return rect
        return None

    def isPointOnNpg(self, x, y):
        for npg in self.npgs:
            if npg.x < x < npg.x+npg.boundingRect().width() and npg.y < y < npg.y + npg.boundingRect().height():
                return npg
        return None

    def deleteItems(self, rect):
        for child in rect.childItems():
            self.removeItem(child)

    def getListPlaces(self):
        places = []
        for rect in self.chess:
            if rect.place is not None:
                places.append(rect.place)
        return places

    def getLisTextes(self):
        textes = []
        for rect in self.chess:
            if rect.text is not None:
                textes.append(rect.text)
        return textes

    def getListRect(self):
        places = []
        for rect in self.chess:
            places.append(rect)
        return places

    def addPlaces(self, places):
        for place in places:
            for rect in self.chess:
                if rect.boundingRect().x() == place.x and rect.boundingRect().y() == place.y:
                    rect.addPlace(place)

    def addTextes(self, textes):
        for text in textes:
            for rect in self.chess:
                if rect.boundingRect().x() == text.x and rect.boundingRect().y() == text.y:
                    rect.addText(text)


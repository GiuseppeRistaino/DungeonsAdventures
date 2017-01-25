import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Elements.Rectangle import *
from Dialogs.DialogTextOnMap import *
from Dialogs.DialogNewDungeon import *
from Dialogs.DialogViewDungeons import *

class Scene(QGraphicsScene):

    HEIGTH_RECT = 50
    WIDTH_RECT = 50
    STATES = ["CANC", "TEXT", "MAP", "DROP", "ROTATE", "VIEW"]

    def __init__(self, numRow, numColumn, name=None, places=None):
        super(Scene, self).__init__()
        self.name = name
        self.numRow = numRow
        self.numColumn = numColumn
        self.chess = []
        self.places = places
        self.itemToDraw = None
        self.state = None

        self.drawChess(self.numRow, self.numColumn)


    def drawChess(self, numRow, numColumn):
        self.setSceneRect(0, 0, self.HEIGTH_RECT * numColumn, self.WIDTH_RECT * numRow)
        for i in range(0, numRow):
            for j in range(0, numColumn):
                rect = Rectangle(j*self.WIDTH_RECT, i*self.HEIGTH_RECT, self.WIDTH_RECT,self.HEIGTH_RECT, scene=self)
                self.chess.append(rect)

    def mouseMoveEvent(self, event):
        self.manageStateEvent(event)

    def mousePressEvent(self, event):
        self.manageStateEvent(event)

    def manageStateEvent(self, event):
        coord = event.scenePos()
        rect = self.isPointOnItemRect(coord.x(), coord.y())
        if event.buttons() == Qt.RightButton:
            if rect is not None:
                #Disegna
                rect.addPlace(self.itemToDraw)
        if self.state == self.STATES[0]:
            if event.buttons() == Qt.LeftButton:
                if rect is not None:
                    # Cancella
                    rect.removeItems()
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



    def isPointOnItemRect(self, x, y):
        for rect in self.chess:
            if rect.boundingRect().contains(x, y):
                return rect
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


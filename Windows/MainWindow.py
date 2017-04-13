import sys
import os

import time
from PyQt4 import QtGui,QtCore
from Windows.Progressbar import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Frames.FrameAdventure import *
from Windows.GuideWindow import *
from Dialogs.DialogNewAdventure import *
from Dialogs.DialogNewGame import *
from Database.Adventure import Adventure_Manager


WINDOW_TITLE = "D&D"

MENU_PLAY = "Gioca"
MENU_PLAY_NEW_GAME = "Nuova Partita"
MENU_PLAY_LOAD_GAME = "Carica Partita"
MENU_EDITOR = "Editor"
MENU_EDITOR_ADVENTURE = "Nuova Avventura"
#MENU_EDITOR_SAVE_ADVENTURE = "Salva Avventura"
MENU_EDITOR_LOAD_ADVENTURE = "Carica Avventura"
MENU_GUIDE = "Manuale"
MENU_GUIDE_OPEN = "Apri Manuale"

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        #self.frame = FrameAdventure(self)

        #self.setCentralWidget(self.frame)

        #Elementi da aggiungere alla finestra principale
        # 1 - Menu
        menu = self.menuBar()

        # Menu Gioca
        menuPlay = menu.addMenu(MENU_PLAY)
        menuPlay.addAction(MENU_PLAY_NEW_GAME)
        menuPlay.addAction(MENU_PLAY_LOAD_GAME)

        # Menu Crea
        menuEditor = menu.addMenu(MENU_EDITOR)
        menuEditor.addAction(MENU_EDITOR_ADVENTURE)
        #menuEditor.addAction(MENU_EDITOR_SAVE_ADVENTURE)
        menuEditor.addAction(MENU_EDITOR_LOAD_ADVENTURE)

        # Menu Manuale
        menuDatabase = menu.addMenu(MENU_GUIDE)
        menuDatabase.addAction(MENU_GUIDE_OPEN)

        # Event Listener MenuBar
        menu.triggered[QAction].connect(self.eventMenuBar)

        self.setWindowTitle(WINDOW_TITLE)

    #Event listener sul Menu Bar per determinare quale Frame deve essere visualizzato
    def eventMenuBar(self, q):

        textMenuBar = q.text()
        if (textMenuBar == MENU_PLAY_NEW_GAME):
            #Visualizzare un dialog...prima del seguente frame
            #self.centralWidget.addWidget(self.framePlay)
            #self.centralWidget.setCurrentWidget(self.framePlay)
            self.dialog = DialogNewGame(self)
            self.dialog.show()
        elif (textMenuBar == MENU_PLAY_LOAD_GAME):
            #visualizzare un dialog
            print("CIAO")
        elif (textMenuBar == MENU_EDITOR_ADVENTURE):
            self.dialog = DialogNewAdventure(self)
            self.dialog.show()
        elif (textMenuBar == MENU_EDITOR_LOAD_ADVENTURE):
            self.load()
        elif (textMenuBar == MENU_GUIDE_OPEN):
            #visualizzare la guida in un'altra finestra a parte
            self.dialog = GuideWindow()
            self.dialog.show()

        print(q.text() + " is triggered")


    def load(self):
        fileDialog = QFileDialog()
        fname = fileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'Map files (*.map)')
        manager = Adventure_Manager()
        adv = manager.load(fname)
        listPlaces = adv.places
        places = []

        value = len(listPlaces)
        for place in listPlaces:
            listDungeons = place.dungeons
            value += len(listDungeons)

        self.Dialog = QtGui.QDialog()
        self.dialog = Ui_Dialog(self.Dialog, value)
        self.Dialog.show()

        count = 0
        for place in listPlaces:
            p = Place(QPixmap(place.pathRes), x=place.x, y=place.y, pathRes=place.pathRes)

            listDungeons = place.dungeons
            self.dialog.update_progressbar(count)
            time.sleep(0.001)

            for dungeon in listDungeons:
                d = Dungeon(dungeon.numRow, dungeon.numColumn, dungeon.name)
                listTerrains = dungeon.terrains
                listItems = dungeon.items
                listNpgs = dungeon.npgs
                d.addTerrains(listTerrains)
                d.addItems(listItems)
                d.addNpgs(listNpgs)
                p.dungeons.append(d)

                self.dialog.update_progressbar(count)
                count += 1
                time.sleep(0.001)

            count += 1
            places.append(p)

        listTextes = adv.textes
        textes = []
        for text in listTextes:
            t = Text(text.string, text.x, text.y)
            textes.append(t)

        self.frame = FrameAdventure(adventureName=adv.name)
        self.setCentralWidget(self.frame)
        self.setWindowTitle(adv.name)

        self.frame.tabAdventure.scene.addPlaces(places)
        self.frame.tabAdventure.scene.addTextes(textes)
        self.frame.tabAdventure.scene.name = adv.name
        self.frame.tabAdventure.scene.numColumn = adv.numColumn
        self.frame.tabAdventure.scene.numRow = adv.numRow
        self.frame.tabAdventure.editTextEnvironment.setText(adv.textEnvironment)
        self.frame.tabAdventure.editTextAdventure.setText(adv.textAdventure)
        self.Dialog.close()

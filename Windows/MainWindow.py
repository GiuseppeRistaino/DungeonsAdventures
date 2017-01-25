import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Frames.FrameAdventure import *
from Windows.GuideWindow import *
from Dialogs.DialogNewAdventure import *
from Dialogs.DialogNewGame import *


WINDOW_TITLE = "D&D"

MENU_PLAY = "Gioca"
MENU_PLAY_NEW_GAME = "Nuova Partita"
MENU_PLAY_LOAD_GAME = "Carica Partita"
MENU_EDITOR = "Editor"
MENU_EDITOR_ADVENTURE = "Nuova Avventura"
#MENU_EDITOR_SAVE_ADVENTURE = "Salva Avventura"
#MENU_EDITOR_LOAD_ADVENTURE = "Carica Avventura"
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
        #menuEditor.addAction(MENU_EDITOR_LOAD_ADVENTURE)

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
        elif (textMenuBar == MENU_GUIDE_OPEN):
            #visualizzare la guida in un'altra finestra a parte
            self.dialog = GuideWindow()
            self.dialog.show()

        print(q.text() + " is triggered")
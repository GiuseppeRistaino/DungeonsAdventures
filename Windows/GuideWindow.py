from PyQt4.QtGui import *
from Frames.GuideFrame import GuideFrame
from Frames.GuideFrameItem import GuideFrameItem
from Database.DB_Manager import DB_Manager

class GuideWindow(QMainWindow):

    WINDOW_TITLE = "Manuale D&D"

    DB_NAME = "Database/Dungeons&Dragons.db"

    STATE = ("Ability", "Weapon", "Magic", "Ingredient", "Monster", "Item", "Potion", "Talent")

    def __init__(self):
        super(GuideWindow, self).__init__()

        self.databaseManuale = DB_Manager(self.DB_NAME)

        self.showFrameGuide(None)

        self.setWindowTitle(self.WINDOW_TITLE)

        self.setMinimumSize(500, 500)


    def listWidgetClicked(self, item):
        dic = dict()
        if self.mainFrame.state == self.STATE[0]:
            dic = self.mainFrame.dbManager.getAbility(item.text())
        elif self.mainFrame.state == self.STATE[1]:
            dic = self.mainFrame.dbManager.getWeapon(item.text())
        elif self.mainFrame.state == self.STATE[2]:
            dic = self.mainFrame.dbManager.getMagic(item.text())
        elif self.mainFrame.state == self.STATE[3]:
            dic = self.mainFrame.dbManager.getIngredient(item.text())
        elif self.mainFrame.state == self.STATE[4]:
            dic = self.mainFrame.dbManager.getMonster(item.text())
        elif self.mainFrame.state == self.STATE[5]:
            dic = self.mainFrame.dbManager.getItem(item.text())
        elif self.mainFrame.state == self.STATE[6]:
            dic = self.mainFrame.dbManager.getPotion(item.text())
        elif self.mainFrame.state == self.STATE[7]:
            dic = self.mainFrame.dbManager.getTalent(item.text())

        self.showFrameGuideItem(dic)

    #metodo per cambiare frame (mostra il frame dell'oggetto selezionato nella lista
    def showFrameGuideItem(self, dictionary):
        frame = GuideFrameItem(self, dictionary, self.mainFrame.state)
        frame.buttonReturn.clicked.connect(self.buttonReturnClicked)
        self.setCentralWidget(frame)

    # metodo per cambiare frame (mostra il frame iniziale
    def showFrameGuide(self, state):
        self.mainFrame = GuideFrame(self, self.databaseManuale, state)
        self.mainFrame.listWidget.itemClicked.connect(self.listWidgetClicked)
        self.setCentralWidget(self.mainFrame)

    #Event Listener per il pulsante di ritorno nel frame GuideFrameItem
    def buttonReturnClicked(self):
        self.showFrameGuide(self.mainFrame.state)

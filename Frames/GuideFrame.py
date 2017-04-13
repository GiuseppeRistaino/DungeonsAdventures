import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GuideFrame(QFrame):

    def __init__(self, window, databaseManuale, state):
        super(GuideFrame, self).__init__()

        self.dbManager = databaseManuale

        self.state = state
        self.window = window

        #il layout principale è quello verticale in cui vi sono una listWidget e un layout orizzontale che contiene i pulsanti
        self.vbox = QVBoxLayout()

        #Lista degli item visibili
        self.listWidget = QListWidget()
        #copia della lista degli oggetti per poter effettuare il filter della ricerca (serviva una lista che conteneva gli oggetti originali)
        self.listWidgetCopy = QListWidget()

        self.hbox = QHBoxLayout()

        #Text Edit per il filter di ricerca
        self.lineEdit = QLineEdit()
        self.lineEdit.setAlignment(Qt.AlignLeft)
        self.lineEdit.setFont(QFont("Arial",20))
        self.lineEdit.textChanged.connect(self.lineEditTextChanged)

        #Pulsanti del manuale
        self.buttonAbility = QPushButton("Abilità")
        self.buttonWeapon = QPushButton("Armi")
        self.buttonMagic = QPushButton("Incantesimi")
        self.buttonIngredient = QPushButton("Ingredienti")
        self.buttonMonster = QPushButton("Mostri")
        self.buttonItem = QPushButton("Oggetti")
        self.buttonPotion = QPushButton("Pozioni")
        self.buttonTalent = QPushButton("Talenti")

        if self.state == self.window.STATE[0]:
            self.showListAbility()
        elif self.state == self.window.STATE[1]:
            self.showListWeapon()
        elif self.state == self.window.STATE[2]:
            self.showListMagic()
        elif self.state == self.window.STATE[3]:
            self.showListIngredient()
        elif self.state == self.window.STATE[4]:
            self.showListMonster()
        elif self.state == self.window.STATE[5]:
            self.showListItem()
        elif self.state == self.window.STATE[6]:
            self.showListPotion()
        elif self.state == self.window.STATE[7]:
            self.showListTalent()

        #Eventi sui pulsanti
        self.buttonAbility.clicked.connect(self.showListAbility)
        self.buttonWeapon.clicked.connect(self.showListWeapon)
        self.buttonMagic.clicked.connect(self.showListMagic)
        self.buttonIngredient.clicked.connect(self.showListIngredient)
        self.buttonMonster.clicked.connect(self.showListMonster)
        self.buttonItem.clicked.connect(self.showListItem)
        self.buttonPotion.clicked.connect(self.showListPotion)
        self.buttonTalent.clicked.connect(self.showListTalent)

        self.hbox.addWidget(self.buttonAbility)
        self.hbox.addWidget(self.buttonWeapon)
        self.hbox.addWidget(self.buttonMagic)
        self.hbox.addWidget(self.buttonIngredient)
        self.hbox.addWidget(self.buttonMonster)
        self.hbox.addWidget(self.buttonItem)
        self.hbox.addWidget(self.buttonPotion)
        self.hbox.addWidget(self.buttonTalent)

        self.vbox.addWidget(self.lineEdit)
        self.vbox.addWidget(self.listWidget)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)


    #Event listener per effettuare il filter della ricerca nella edit text
    def lineEditTextChanged(self, text):
        out = self.listWidgetCopy.findItems(text, Qt.MatchContains)
        listStr = []
        for elem in out:
            listStr.append(elem.text())
        self.listWidget.clear()
        self.listWidget.addItems(listStr)


    #Event listener pulsante lista abilità
    def showListAbility(self):
        self.state = self.window.STATE[0]
        listAbility = self.dbManager.getListAbility()
        self.listWidget.clear()
        for ability in listAbility:
            self.listWidget.addItem(ability)
            self.listWidgetCopy.addItem(ability)

    #Event listener pulsante lista armi
    def showListWeapon(self):
        self.state = self.window.STATE[1]
        listWeapon = self.dbManager.getListWeapon()
        self.listWidget.clear()
        for weapon in listWeapon:
            self.listWidget.addItem(weapon)
            self.listWidgetCopy.addItem(weapon)

    #Event listener pulsante lista incantesimi
    def showListMagic(self):
        self.state = self.window.STATE[2]
        listMagic = self.dbManager.getListMagic()
        self.listWidget.clear()
        for magic in listMagic:
            self.listWidget.addItem(magic)
            self.listWidgetCopy.addItem(magic)

    # Event listener pulsante lista ingredienti
    def showListIngredient(self):
        self.state = self.window.STATE[3]
        result = self.dbManager.getListIngredient()
        self.listWidget.clear()
        for elem in result:
            self.listWidget.addItem(elem)
            self.listWidgetCopy.addItem(elem)

    # Event listener pulsante lista mostri
    def showListMonster(self):
        self.state = self.window.STATE[4]
        result = self.dbManager.getListMonster()
        self.listWidget.clear()
        for elem in result:
            self.listWidget.addItem(elem)
            self.listWidgetCopy.addItem(elem)

    # Event listener pulsante lista mostri
    def showListItem(self):
        self.state = self.window.STATE[5]
        result = self.dbManager.getListItem()
        self.listWidget.clear()
        for elem in result:
            self.listWidget.addItem(elem)
            self.listWidgetCopy.addItem(elem)

    # Event listener pulsante lista mostri
    def showListPotion(self):
        self.state = self.window.STATE[6]
        result = self.dbManager.getListPotion()
        self.listWidget.clear()
        for elem in result:
            self.listWidget.addItem(elem)
            self.listWidgetCopy.addItem(elem)

    # Event listener pulsante lista mostri
    def showListTalent(self):
        self.state = self.window.STATE[7]
        result = self.dbManager.getListTalent()
        self.listWidget.clear()
        for elem in result:
            self.listWidget.addItem(elem)
            self.listWidgetCopy.addItem(elem)

import time
from FrameElements.Scene import *
from FrameElements.MyGraphicsView import *
from Elements.Place import *
from FrameElements.Dungeon import *
from Database.Adventure import Adventure_Manager
#from Database.MapStorage import *


class TabGame(QTabWidget):

    PATH_ICONS = "img/npg/"

    def __init__(self, adventure, parent=None):
        super(TabGame, self).__init__(parent)
        self.parent = parent
        self.adventure = adventure

        self.scene = None

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabPlayer1 = QWidget()
        self.tabPlayer2 = QWidget()
        self.tabPlayer3 = QWidget()

        self.addTab(self.tab1, "Mappa")
        self.addTab(self.tab2, "Ambientazione")
        self.addTab(self.tab3, "Avventura")

        self.editTextAdventure = QTextEdit()
        self.editTextEnvironment = QTextEdit()

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tabPlayerUI()
        #self.setWindowTitle("tab demo")

    def loadScene(self, adv):
        listPlaces = adv.places
        places = []
        for place in listPlaces:
            p = Place(QPixmap(place.pathRes), x=place.x, y=place.y, pathRes=place.pathRes)
            listDungeons = place.dungeons
            for dungeon in listDungeons:
                d = Dungeon(dungeon.numRow, dungeon.numColumn, dungeon.name)
                listTerrains = dungeon.terrains
                listItems = dungeon.items
                listNpgs = dungeon.npgs
                d.addTerrains(listTerrains)
                d.addItems(listItems)
                d.addNpgs(listNpgs)
                p.dungeons.append(d)
            places.append(p)

        listTextes = adv.textes
        textes = []
        for text in listTextes:
            t = Text(text.string, text.x, text.y)
            textes.append(t)

        self.scene = Scene(adv.numRow, adv.numColumn, adv.name)
        self.scene.addPlaces(places)
        self.scene.addTextes(textes)
        self.scene.name = adv.name
        self.scene.numColumn = adv.numColumn
        self.scene.numRow = adv.numRow
        self.editTextEnvironment.setText(adv.textEnvironment)
        self.editTextAdventure.setText(adv.textAdventure)

    def tab1UI(self):
        vbox = QVBoxLayout()
        hboxTop = QHBoxLayout()
        vboxRight = QVBoxLayout()
        hBoxTopRight = QHBoxLayout()
        hBoxBottomRight = QHBoxLayout()

        self.loadScene(self.adventure)

        self.buttonSave = QPushButton("Salva")
        #self.buttonLoad = QPushButton("Load")

        self.listWidget = QListWidget()
        self.listWidget.selectionModel().selectionChanged.connect(self.eventListItemWidgetSelect)
        self.populateListWidget()

        #Widget del layout hBoxBottomRight
        self.buttonCancel = QPushButton()
        self.buttonText = QPushButton()
        self.buttonMap = QPushButton()
        self.buttonDrop = QPushButton()
        self.buttonDrag = QPushButton()
        self.buttonInfo = QPushButton()
        self.buttonView = QPushButton()
        self.buttonCancel.setIcon(QIcon(QPixmap("img/icon_cancel.png")))
        self.buttonText.setIcon(QIcon(QPixmap("img/icon_text.png")))
        self.buttonMap.setIcon(QIcon(QPixmap("img/icon_map.png")))
        self.buttonDrop.setIcon(QIcon(QPixmap("img/icon_drop.png")))
        self.buttonDrag.setText("Drag")
        self.buttonInfo.setText("Info")
        self.buttonView.setText("View Map")

        self.buttonMap.setCheckable(True)
        self.buttonDrop.setCheckable(True)
        self.buttonCancel.setCheckable(True)
        self.buttonText.setCheckable(True)
        self.buttonDrag.setCheckable(True)
        self.buttonInfo.setCheckable(True)
        self.buttonView.setCheckable(True)

        self.buttonSave.clicked.connect(self.eventButtonSave)
        #self.buttonLoad.clicked.connect(self.eventButtonLoad)
        self.buttonMap.clicked.connect(self.eventButtonMap)
        self.buttonDrop.clicked.connect(self.eventButtonDrop)
        self.buttonCancel.clicked.connect(self.eventButtonCanc)
        self.buttonText.clicked.connect(self.eventButtonText)
        self.buttonDrag.clicked.connect(self.eventButtonDrag)
        self.buttonInfo.clicked.connect(self.eventButtonInfo)
        self.buttonView.clicked.connect(self.eventButtonView)

        hBoxTopRight.addWidget(self.buttonSave)
        #hBoxTopRight.addWidget(self.buttonLoad)

        hBoxBottomRight.addWidget(self.buttonCancel)
        hBoxBottomRight.addWidget(self.buttonText)
        hBoxBottomRight.addWidget(self.buttonMap)
        hBoxBottomRight.addWidget(self.buttonDrop)
        hBoxBottomRight.addWidget(self.buttonDrag)
        hBoxBottomRight.addWidget(self.buttonInfo)
        hBoxBottomRight.addWidget(self.buttonView)

        vboxRight.addLayout(hBoxTopRight)
        vboxRight.addWidget(self.listWidget)
        vboxRight.addLayout(hBoxBottomRight)

        self.view = MyGraphicsView()
        self.view.setScene(self.scene)

        hboxTop.addWidget(self.view)
        hboxTop.addLayout(vboxRight)

        vbox.addLayout(hboxTop)

        self.tab1.setLayout(vbox)

    def populateListWidget(self):
        listIcons = os.listdir(self.PATH_ICONS)
        for icon in listIcons:
            item = QListWidgetItem()
            item.setIcon(QIcon(QPixmap(self.PATH_ICONS + icon)))
            item.setText(self.PATH_ICONS + icon)
            item.setTextAlignment(Qt.AlignRight)
            item.setSizeHint(QSize(52, 52))
            self.listWidget.addItem(item)

        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setIconSize(QSize(50, 50))

    def eventListItemWidgetSelect(self):
        for elem in self.listWidget.selectedItems():
            path = self.listWidget.currentItem().text()
            pixmap = elem.icon().pixmap(QSize(50, 50))
            self.scene.itemToDraw = Npg(pixmap, pathRes=path)

    def eventButtonMap(self):
        self.checkButton(self.buttonMap)
        self.view.setDragMode(False)
        self.scene.state = self.scene.STATES[2]
        self.setCursor(QCursor(Qt.CrossCursor))

    def eventButtonDrop(self):
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.checkButton(self.buttonDrop)
        self.scene.state = self.scene.STATES[3]
        self.setCursor(QCursor(Qt.OpenHandCursor))

    def eventButtonCanc(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonCancel)
        self.scene.state = self.scene.STATES[0]
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def eventButtonText(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonText)
        self.scene.state = self.scene.STATES[1]
        self.setCursor(QCursor(Qt.IBeamCursor))

    def eventButtonDrag(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonDrag)
        self.scene.state = self.scene.STATES[6]
        self.setCursor(QCursor(Qt.ArrowCursor))

    def eventButtonInfo(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonInfo)
        self.scene.state = self.scene.STATES[7]
        self.setCursor(QCursor(Qt.ArrowCursor))

    def eventButtonView(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonView)
        self.scene.state = self.scene.STATES[5]
        self.setCursor(QCursor(Qt.ArrowCursor))

    def unCheckAllButton(self):
        self.buttonDrop.setChecked(False)
        self.buttonMap.setChecked(False)
        self.buttonText.setChecked(False)
        self.buttonCancel.setChecked(False)
        self.buttonDrag.setChecked(False)
        self.buttonInfo.setChecked(False)
        self.buttonView.setChecked(False)
        self.scene.state = None

    def checkButton(self, button):
        self.unCheckAllButton()
        button.setChecked(True)


    def tab2UI(self):
        vBox = QVBoxLayout()

        self.editTextEnvironment.setLineWrapMode(QTextEdit.WidgetWidth)

        font = QFont("Times", 12, QFont.Normal, True)
        self.editTextEnvironment.setFont(font)
        cursor = self.editTextEnvironment.textCursor()
        cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.editTextEnvironment.setTextCursor(cursor)

        vBox.addWidget(self.editTextEnvironment)
        self.tab2.setLayout(vBox)

    def tab3UI(self):
        vBox = QVBoxLayout()

        self.editTextAdventure.setLineWrapMode(QTextEdit.WidgetWidth)

        font = QFont("Times", 12, QFont.Normal, True)
        self.editTextAdventure.setFont(font)
        cursor = self.editTextAdventure.textCursor()
        cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.editTextAdventure.setTextCursor(cursor)

        vBox.addWidget(self.editTextAdventure)
        self.tab3.setLayout(vBox)

    def tabPlayerUI(self):
        vbox = QVBoxLayout()



        self.tabPlayer1.setLayout(vbox)
        self.tabPlayer2.setLayout(vbox)
        self.tabPlayer3.setLayout(vbox)



    def eventButtonSave(self):
        fileDialog = QFileDialog()
        fname = fileDialog.getSaveFileName(self, 'Save file', 'c:\\', 'Map files (*.map)')
        manager = Adventure_Manager()
        manager.save(self.scene, self.editTextEnvironment, self.editTextAdventure,fname)


    '''
    Metodo per caricare una avventura da un file .map
    per ora è stato messo in questa classe ma deve essere portato nella classe MainWindow nella quale bisognerà creare
    un opzione in più per il menu che permetta il caricamento della mappa
    '''
    def eventButtonLoad(self):
        fileDialog = QFileDialog()
        fname = fileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'Map files (*.map)')
        manager = Adventure_Manager()
        adv = manager.load(fname)
        listPlaces = adv.places
        places = []
        for place in listPlaces:
            p = Place(QPixmap(place.pathRes), x=place.x, y=place.y, pathRes=place.pathRes)
            listDungeons = place.dungeons
            for dungeon in listDungeons:
                d = Dungeon(dungeon.numRow, dungeon.numColumn, dungeon.name)
                listTerrains = dungeon.terrains
                listItems = dungeon.items
                listNpgs = dungeon.npgs
                d.addTerrains(listTerrains)
                d.addItems(listItems)
                d.addNpgs(listNpgs)
                p.dungeons.append(d)
            places.append(p)

        listTextes = adv.textes
        textes = []
        for text in listTextes:
            t = Text(text.string, text.x, text.y)
            textes.append(t)

        self.scene.addPlaces(places)
        self.scene.addTextes(textes)
        self.scene.name = adv.name
        self.scene.numColumn = adv.numColumn
        self.scene.numRow = adv.numRow

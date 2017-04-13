import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FrameElements.Scene import *
from FrameElements.MyGraphicsView import *
from Elements.Place import *
from FrameElements.Dungeon import *
from Database.DB_Manager import DB_Manager_Adventure
from Database.Adventure import Adventure_Manager
from Server.TCP_server import *
#from Database.MapStorage import *



class TabAdventure(QTabWidget):

    PATH_ICONS = "img/environment_items/"

    def __init__(self, parent=None, adventureName=None):
        super(TabAdventure, self).__init__(parent)
        self.parent = parent
        self.adventureName = adventureName
        self.numRow = 100
        self.numColumn = 100
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, "Mappa")
        self.addTab(self.tab2, "Ambientazione")
        self.addTab(self.tab3, "Avventura")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        #self.setWindowTitle("tab demo")

        start_server = Server_Deamon()
        start_server.start()


    def tab1UI(self):
        vbox = QVBoxLayout()
        hboxTop = QHBoxLayout()
        vboxRight = QVBoxLayout()
        hBoxTopRight = QHBoxLayout()
        hBoxBottomRight = QHBoxLayout()

        self.scene = Scene(self.numRow, self.numColumn, self.adventureName)

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
        self.buttonRotate = QPushButton()
        self.buttonView = QPushButton()
        self.buttonCapture = QPushButton()
        self.buttonSelect = QPushButton()
        self.buttonSend = QPushButton()
        self.buttonCancel.setIcon(QIcon(QPixmap("img/icon_cancel.png")))
        self.buttonText.setIcon(QIcon(QPixmap("img/icon_text.png")))
        self.buttonMap.setIcon(QIcon(QPixmap("img/icon_map.png")))
        self.buttonDrop.setIcon(QIcon(QPixmap("img/icon_drop.png")))
        self.buttonRotate.setIcon(QIcon(QPixmap("img/icon_rotate.png")))
        self.buttonSelect.setText("SELECT")
        self.buttonSend.setText("Send File")
        self.buttonView.setText("View Map")
        self.buttonCapture.setText("Foto")

        self.buttonMap.setCheckable(True)
        self.buttonDrop.setCheckable(True)
        self.buttonCancel.setCheckable(True)
        self.buttonText.setCheckable(True)
        self.buttonRotate.setCheckable(True)
        self.buttonSelect.setCheckable(True)
        self.buttonSend.setCheckable(True)
        self.buttonView.setCheckable(True)

        self.buttonSave.clicked.connect(self.eventButtonSave)
        #self.buttonLoad.clicked.connect(self.eventButtonLoad)
        self.buttonMap.clicked.connect(self.eventButtonMap)
        self.buttonDrop.clicked.connect(self.eventButtonDrop)
        self.buttonCancel.clicked.connect(self.eventButtonCanc)
        self.buttonText.clicked.connect(self.eventButtonText)
        self.buttonRotate.clicked.connect(self.eventButtonRotate)
        self.buttonView.clicked.connect(self.eventButtonView)
        self.buttonCapture.clicked.connect(self.eventButtonCapture)
        self.buttonSelect.clicked.connect(self.eventButtonSelect)
        self.buttonSend.clicked.connect(self.eventButtonSocket)

        hBoxTopRight.addWidget(self.buttonSave)
        #hBoxTopRight.addWidget(self.buttonLoad)

        hBoxBottomRight.addWidget(self.buttonCancel)
        hBoxBottomRight.addWidget(self.buttonText)
        hBoxBottomRight.addWidget(self.buttonMap)
        hBoxBottomRight.addWidget(self.buttonDrop)
        hBoxBottomRight.addWidget(self.buttonRotate)
        hBoxBottomRight.addWidget(self.buttonView)
        hBoxBottomRight.addWidget(self.buttonSelect)
        hBoxBottomRight.addWidget(self.buttonCapture)
        hBoxBottomRight.addWidget(self.buttonSend)

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
            self.scene.itemToDraw = Place(pixmap, pathRes=path)

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

    def eventButtonRotate(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonRotate)
        self.scene.state = self.scene.STATES[4]
        self.setCursor(QCursor(Qt.ArrowCursor))

    def eventButtonCapture(self):
        filename = "capture.jpg"
        w = self.view.rubberBand.rect().width()
        h = self.view.rubberBand.rect().height()
        image = QImage(w,h, QImage.Format_RGB32)
        image.fill(QColor(Qt.white))
        painter = QPainter(image)
        self.view.render(painter, source=QRect(self.view.rubberBand.x(), self.view.rubberBand.y(), w, h))
        painter.end()
        image.save(filename, "jpg")


    def eventButtonSocket(self):
        print("Hello")


    def eventButtonSelect(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonSelect)
        self.scene.state = self.scene.STATES[8]
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
        self.buttonRotate.setChecked(False)
        self.buttonView.setChecked(False)
        self.buttonSelect.setChecked(False)
        self.buttonSend.setChecked(False)
        self.scene.state = None

    def checkButton(self, button):
        self.unCheckAllButton()
        button.setChecked(True)


    def tab2UI(self):
        vBox = QVBoxLayout()

        self.editTextEnvironment = QTextEdit()
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

        self.editTextAdventure = QTextEdit()
        self.editTextAdventure.setLineWrapMode(QTextEdit.WidgetWidth)

        font = QFont("Times", 12, QFont.Normal, True)
        self.editTextAdventure.setFont(font)
        cursor = self.editTextAdventure.textCursor()
        cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.editTextAdventure.setTextCursor(cursor)

        vBox.addWidget(self.editTextAdventure)
        self.tab3.setLayout(vBox)


    def eventButtonSave(self):
        fileDialog = QFileDialog()
        fname = fileDialog.getSaveFileName(self, 'Save file', 'c:\\', 'Map files (*.map)')
        manager = Adventure_Manager()
        manager.save(self.scene, self.editTextEnvironment, self.editTextAdventure, fname)

import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from FrameElements.Dungeon import Dungeon
from FrameElements.MyGraphicsView import MyGraphicsView
from FrameElements.TabListWidgetDungeon import *

class FrameDungeon(QFrame):

    def __init__(self, mapName=None, rect=None, numRow=None, numColumn=None, parent=None, dungeon=None):
        super(FrameDungeon, self).__init__(parent)
        layout = QHBoxLayout()

        #Scene
        self.dungeon = dungeon
        if self.dungeon is None:
            self.dungeon = Dungeon(numRow, numColumn, mapName)
        self.view = MyGraphicsView()
        self.view.setScene(self.dungeon)
        self.view.update()

        layout.addWidget(self.view)

        vBox = QVBoxLayout()

        #Righe colonne
        hBoxRowColumn = QHBoxLayout()
        self.labelRow = QLabel("Righe")
        self.editRow = QLineEdit()
        self.labelColumn = QLabel("Column")
        self.editColumn = QLineEdit()
        self.buttonUpdateRowColumn = QPushButton("Ridisegna")
        self.buttonUpdateRowColumn.clicked.connect(self.eventButtonUpdateRowColumn)
        hBoxRowColumn.addWidget(self.labelRow)
        hBoxRowColumn.addWidget(self.editRow)
        hBoxRowColumn.addWidget(self.labelColumn)
        hBoxRowColumn.addWidget(self.editColumn)
        hBoxRowColumn.addWidget(self.buttonUpdateRowColumn)

        vBox.addLayout(hBoxRowColumn)

        #TabListWidgetDungeon
        self.tabDungeon = TabListWidgetDungeon(self)
        vBox.addWidget(self.tabDungeon)

        self.buttonCancel = QPushButton()
        self.buttonText = QPushButton()
        self.buttonDrop = QPushButton()
        self.buttonRotate = QPushButton()
        self.buttonDrag = QPushButton()
        self.buttonInfo = QPushButton()
        self.buttonSelect = QPushButton()
        self.buttonCapture = QPushButton()
        self.buttonCancel.setIcon(QIcon(QPixmap("img/icon_cancel.png")))
        self.buttonText.setIcon(QIcon(QPixmap("img/icon_text.png")))
        self.buttonDrop.setIcon(QIcon(QPixmap("img/icon_drop.png")))
        self.buttonRotate.setIcon(QIcon(QPixmap("img/icon_rotate.png")))
        self.buttonDrag.setText("Drag")
        self.buttonInfo.setText("Info")
        self.buttonSelect.setText("SELECT")
        self.buttonCapture.setText("FOTO")

        self.buttonDrop.setCheckable(True)
        self.buttonCancel.setCheckable(True)
        self.buttonText.setCheckable(True)
        self.buttonRotate.setCheckable(True)
        self.buttonDrag.setCheckable(True)
        self.buttonInfo.setCheckable(True)
        self.buttonSelect.setCheckable(True)

        # self.buttonSave.clicked.connect(self.eventButtonSave)
        # self.buttonLoad.clicked.connect(self.eventButtonLoad)
        self.buttonDrop.clicked.connect(self.eventButtonDrop)
        self.buttonCancel.clicked.connect(self.eventButtonCanc)
        self.buttonText.clicked.connect(self.eventButtonText)
        self.buttonRotate.clicked.connect(self.eventButtonRotate)
        self.buttonDrag.clicked.connect(self.eventButtonDrag)
        self.buttonInfo.clicked.connect(self.eventButtonInfo)
        self.buttonSelect.clicked.connect(self.eventButtonSelect)
        self.buttonCapture.clicked.connect(self.eventButtonCapture)

        hBoxButtons = QHBoxLayout()
        hBoxButtons.addWidget(self.buttonCancel)
        hBoxButtons.addWidget(self.buttonText)
        hBoxButtons.addWidget(self.buttonDrop)
        hBoxButtons.addWidget(self.buttonRotate)
        hBoxButtons.addWidget(self.buttonDrag)
        hBoxButtons.addWidget(self.buttonInfo)
        hBoxButtons.addWidget(self.buttonSelect)
        hBoxButtons.addWidget(self.buttonCapture)

        vBox.addLayout(hBoxButtons)
        layout.addLayout(vBox)

        self.setLayout(layout)

    def eventButtonUpdateRowColumn(self):
        numRow = self.editRow.text()
        numColumn = self.editColumn.text()
        if numRow != "" and numColumn != "":
            self.dungeon.setDimension(int(numRow), int(numColumn))

    def eventButtonDrop(self):
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.checkButton(self.buttonDrop)
        self.dungeon.state = self.dungeon.STATES[3]
        self.setCursor(QCursor(Qt.OpenHandCursor))

    def eventButtonCanc(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonCancel)
        self.dungeon.state = self.dungeon.STATES[0]
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def eventButtonText(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonText)
        self.dungeon.state = self.dungeon.STATES[1]
        self.setCursor(QCursor(Qt.IBeamCursor))

    def eventButtonRotate(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonRotate)
        self.dungeon.state = self.dungeon.STATES[4]
        self.setCursor(QCursor(Qt.ArrowCursor))

    def eventButtonDrag(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonDrag)
        self.dungeon.state = self.dungeon.STATES[5]
        self.setCursor(QCursor(Qt.ArrowCursor))

    def eventButtonInfo(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonInfo)
        self.dungeon.state = self.dungeon.STATES[6]
        self.setCursor(QCursor(Qt.ArrowCursor))

    def eventButtonSelect(self):
        self.view.setDragMode(False)
        self.checkButton(self.buttonSelect)
        self.dungeon.state = self.dungeon.STATES[7]
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

    def unCheckAllButton(self):
        self.buttonDrop.setChecked(False)
        self.buttonText.setChecked(False)
        self.buttonCancel.setChecked(False)
        self.buttonRotate.setChecked(False)
        self.buttonDrag.setChecked(False)
        self.buttonInfo.setChecked(False)
        self.buttonSelect.setChecked(False)
        self.dungeon.state = None

    def checkButton(self, button):
        self.unCheckAllButton()
        button.setChecked(True)

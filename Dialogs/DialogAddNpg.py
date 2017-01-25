import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Frames.FrameAdventure import *
from Elements.Npg import *

class DialogAddNpg(QDialog):

    def __init__(self, dungeon, rect, parent=None):
        super(DialogAddNpg, self).__init__(parent)

        self.dungeon = dungeon
        self.rect = rect
        self.parent = parent

        self.labelName = QLabel("Inserisci il nome dell'npg")
        self.editName = QLineEdit()
        self.buttonOk = QPushButton("OK")
        self.buttonOk.clicked.connect(self.eventClickButtonOk)

        vbox = QVBoxLayout()
        vbox.addWidget(self.labelName)
        vbox.addWidget(self.editName)
        vbox.addWidget(self.buttonOk)

        self.setLayout(vbox)


    def eventClickButtonOk(self):
        npgName = self.editName.text()
        #controllare se il nome non è già presente nel database
        if npgName != "":
            npg = Npg(self.dungeon.itemToDraw.pixmap, x=self.rect.boundingRect().x(), y=self.rect.boundingRect().y(),
                      pathRes=self.dungeon.itemToDraw.pathRes, name=npgName)
            npg.setPos(npg.x, npg.y)
            npg.setFlag(QGraphicsPixmapItem.ItemIsMovable)
            self.dungeon.addItem(npg)
            self.dungeon.npgs.append(npg)
            self.close()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Nome non valido")
            self.msg.setWindowTitle("Attenzione")
            self.msg.show()

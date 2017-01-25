import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Frames.FrameAdventure import *

class DialogNewAdventure(QDialog):

    def __init__(self, parent=None):
        super(DialogNewAdventure, self).__init__(parent)

        self.parent = parent

        self.labelName = QLabel("Inserisci il nome dell'avventura")
        self.editName = QLineEdit()
        self.buttonOk = QPushButton("OK")
        self.buttonOk.clicked.connect(self.eventClickButtonOk)

        vbox = QVBoxLayout()
        vbox.addWidget(self.labelName)
        vbox.addWidget(self.editName)
        vbox.addWidget(self.buttonOk)

        self.setLayout(vbox)


    def eventClickButtonOk(self):
        adventureName = self.editName.text()
        isNew = True
        #controllare se il nome non è già presente nel database
        if adventureName != "" and isNew:
            self.frame = FrameAdventure(adventureName=adventureName)
            self.parent.setCentralWidget(self.frame)
            self.parent.setWindowTitle(adventureName)
            self.close()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Esiste già un'avventura con questo nome, oppure il campo è vuoto")
            self.msg.setWindowTitle("Attenzione")
            self.msg.show()

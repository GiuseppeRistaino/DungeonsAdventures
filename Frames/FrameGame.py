import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from FrameElements.Scene import *
from FrameElements.TabGame import *

class FrameGame(QFrame):

    def __init__(self, parent, adventure, numPlayer):
        super(FrameGame, self).__init__(parent)
        self.parent = parent
        self.adventure = adventure
        self.numPlayer = numPlayer
        layout = QHBoxLayout()

        #Scene
        #scene = Scene(50, 50, "asjda")
        #self.view = MyGraphicsView()
        #self.view.setScene(self.scene)

        #layout.addWidget(self.view)

        #List Widget Place
        self.tabGame = TabGame(self.adventure, self.numPlayer, self)

        layout.addWidget(self.tabGame)

        self.setLayout(layout)

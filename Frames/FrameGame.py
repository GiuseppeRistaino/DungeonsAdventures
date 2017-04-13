import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from FrameElements.Scene import *
from FrameElements.TabGame import *

class FrameGame(QFrame):

    def __init__(self, parent, adventure):
        super(FrameGame, self).__init__(parent)
        self.parent = parent
        self.adventure = adventure
        layout = QHBoxLayout()

        #List Widget Place
        self.tabGame = TabGame(self.adventure, self)

        layout.addWidget(self.tabGame)

        self.setLayout(layout)

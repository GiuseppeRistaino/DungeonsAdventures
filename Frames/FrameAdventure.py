import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from FrameElements.Scene import *
from FrameElements.TabAdventure import *

class FrameAdventure(QFrame):

    def __init__(self, parent=None, adventureName=None):
        super(FrameAdventure, self).__init__(parent)
        self.parent = parent
        self.adventureName = adventureName
        layout = QHBoxLayout()

        #Scene
        #scene = Scene(50, 50, "asjda")
        #self.view = MyGraphicsView()
        #self.view.setScene(self.scene)

        #layout.addWidget(self.view)

        #List Widget Place
        self.tabAdventure = TabAdventure(self, self.adventureName)

        layout.addWidget(self.tabAdventure)

        self.setLayout(layout)


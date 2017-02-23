from FrameElements.Scene import *
from FrameElements.TabAdventure import *

class FrameAdventure(QFrame):

    def __init__(self, parent=None, adventureName=None):
        super(FrameAdventure, self).__init__(parent)
        self.parent = parent
        self.adventureName = adventureName
        layout = QHBoxLayout()

        #List Widget Place
        self.tabAdventure = TabAdventure(self, self.adventureName)

        layout.addWidget(self.tabAdventure)

        self.setLayout(layout)


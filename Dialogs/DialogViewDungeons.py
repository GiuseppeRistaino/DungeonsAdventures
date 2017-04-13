import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Windows.EditorDungeonWindow import EditorDungeonWindow

class DialogViewDungeons(QDialog):

    def __init__(self, rect, parent=None):
        super(DialogViewDungeons, self).__init__(parent)

        self.rect = rect
        self.parent = parent

        self.listWidget = QListWidget()

        self.listDungeons = self.rect.place.dungeons
        if self.listDungeons is not None:
            for elem in self.listDungeons:
                self.item = QListWidgetItem()
                self.item.setText(elem.name)
                self.listWidget.addItem(self.item)

        vbox = QVBoxLayout()
        vbox.addWidget(self.listWidget)

        self.listWidget.itemClicked.connect(self.eventClickListWidget)

        self.setLayout(vbox)


    def eventClickListWidget(self, item):
        self.scene = None
        self.name = None
        for elem in self.listDungeons:
            if elem.name == item.text():
               self.scene = elem
        self.editorMapWindow = EditorDungeonWindow(self.scene.name, self.rect, self.scene.numRow, self.scene.numColumn, self.scene)
        self.editorMapWindow.show()
        self.close()
        #self.scene.drawChess(self.scene.numRaw, self.scene.numColumn)
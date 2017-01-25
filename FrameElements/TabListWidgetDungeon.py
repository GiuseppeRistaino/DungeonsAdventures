import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Elements.Terrain import *
from Elements.Item import *
from Elements.Npg import *


class TabListWidgetDungeon(QTabWidget):

    PATH_TERRAINS = "img/terreni/"
    PATH_ITEMS = "img/item/"
    PATH_NPG = "img/npg/"

    def __init__(self, parent=None):
        super(TabListWidgetDungeon, self).__init__(parent)
        self.parent = parent
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, "Terreno")
        self.addTab(self.tab2, "Oggetti")
        self.addTab(self.tab3, "Npg")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        #self.setWindowTitle("tab demo")

    def tab1UI(self):
        vBox = QVBoxLayout()
        self.listTerrainWidget = QListWidget()
        self.listTerrainWidget.selectionModel().selectionChanged.connect(self.eventListTerrainWidgetSelect)
        self.populateListTerrainWidget()
        vBox.addWidget(self.listTerrainWidget)
        self.tab1.setLayout(vBox)

    def populateListTerrainWidget(self):
        listIcons = os.listdir(self.PATH_TERRAINS)
        for icon in listIcons:
            item = QListWidgetItem()
            item.setIcon(QIcon(QPixmap(self.PATH_TERRAINS + icon)))
            item.setText(self.PATH_TERRAINS + icon)
            item.setTextAlignment(Qt.AlignRight)
            item.setSizeHint(QSize(52, 52))
            self.listTerrainWidget.addItem(item)
        self.listTerrainWidget.setViewMode(QListView.IconMode)

        self.listTerrainWidget.setDragEnabled(False)
        self.listTerrainWidget.setIconSize(QSize(50, 50))

    def eventListTerrainWidgetSelect(self):
        for elem in self.listTerrainWidget.selectedItems():
            pathRes = self.listTerrainWidget.currentItem().text()
            pixmap = elem.icon().pixmap(QSize(50, 50))
            self.parent.dungeon.itemToDraw = Terrain(pixmap, pathRes=pathRes)

    def tab2UI(self):
        vBox = QVBoxLayout()
        self.listItemWidget = QListWidget()
        self.listItemWidget.selectionModel().selectionChanged.connect(self.eventListItemWidgetSelect)
        self.populateListItemWidget()
        vBox.addWidget(self.listItemWidget)
        self.tab2.setLayout(vBox)

    def populateListItemWidget(self):
        listIcons = os.listdir(self.PATH_ITEMS)
        for icon in listIcons:
            item = QListWidgetItem()
            item.setIcon(QIcon(QPixmap(self.PATH_ITEMS + icon)))
            item.setText(self.PATH_ITEMS + icon)
            item.setTextAlignment(Qt.AlignRight)
            item.setSizeHint(QSize(52, 52))
            self.listItemWidget.addItem(item)
        self.listItemWidget.setViewMode(QListView.IconMode)

        self.listItemWidget.setDragEnabled(False)
        self.listItemWidget.setIconSize(QSize(50, 50))

    def eventListItemWidgetSelect(self):
        for elem in self.listItemWidget.selectedItems():
            pathRes = self.listItemWidget.currentItem().text()
            pixmap = elem.icon().pixmap(QSize(50, 50))
            self.parent.dungeon.itemToDraw = Item(pixmap, pathRes=pathRes)

    def tab3UI(self):
        vBox = QVBoxLayout()
        self.listNpgWidget = QListWidget()
        self.listNpgWidget.selectionModel().selectionChanged.connect(self.eventListNpgWidgetSelect)
        self.populateListNpgWidget()
        vBox.addWidget(self.listNpgWidget)
        self.tab3.setLayout(vBox)

    def populateListNpgWidget(self):
        listIcons = os.listdir(self.PATH_NPG)
        for icon in listIcons:
            item = QListWidgetItem()
            item.setIcon(QIcon(QPixmap(self.PATH_NPG + icon)))
            item.setText(self.PATH_NPG + icon)
            item.setTextAlignment(Qt.AlignRight)
            item.setSizeHint(QSize(52, 52))
            self.listNpgWidget.addItem(item)
        self.listNpgWidget.setViewMode(QListView.IconMode)

        self.listNpgWidget.setDragEnabled(False)
        self.listNpgWidget.setIconSize(QSize(50, 50))

    def eventListNpgWidgetSelect(self):
        for elem in self.listNpgWidget.selectedItems():
            pathRes = self.listNpgWidget.currentItem().text()
            pixmap = elem.icon().pixmap(QSize(50, 50))
            self.parent.dungeon.itemToDraw = Npg(pixmap, pathRes=pathRes)
            print(self.parent.dungeon.itemToDraw)






from Frames.FrameDungeon import *


class EditorDungeonWindow(QMainWindow):

    def __init__(self, mapName=None, rect=None, numRow=None, numColumn=None, dungeon=None):
        super(EditorDungeonWindow, self).__init__()

        self.mapName = mapName
        self.rect = rect
        self.dungeon = dungeon
        self.frame = FrameDungeon(self.mapName, self.rect, numRow, numColumn, self, self.dungeon)

        self.setWindowTitle(mapName)

        self.setMinimumSize(500, 500)

        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)

        self.centralWidget.addWidget(self.frame)
        self.centralWidget.setCurrentWidget(self.frame)

    def closeEvent(self, event):
        self.rect.addNewDungeon(self.frame.dungeon)

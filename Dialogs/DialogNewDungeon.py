from Windows.EditorDungeonWindow import *

class DialogNewDungeon(QDialog):

    def __init__(self, rect, parent=None, scene=None):
        super(DialogNewDungeon, self).__init__(parent)

        self.rect = rect
        self.parent = parent
        self.scene = scene

        self.labelName = QLabel("Inserisci il nome del Dungeon")
        self.editName = QLineEdit()
        self.numRow = QLineEdit()
        self.numRow.setValidator(QIntValidator())
        self.numRow.setMaxLength(3)
        self.numRow.setText("10")
        self.numColumn = QLineEdit()
        self.numColumn.setValidator(QIntValidator())
        self.numColumn.setMaxLength(3)
        self.numColumn.setText("10")
        form = QFormLayout()
        form.addRow(QLabel("Righe"), self.numRow)
        form.addRow(QLabel("Colonne"), self.numColumn)
        self.buttonOk = QPushButton("OK")
        self.buttonOk.clicked.connect(self.eventClickButtonOk)

        vbox = QVBoxLayout()
        vbox.addWidget(self.labelName)
        vbox.addWidget(self.editName)
        vbox.addLayout(form)
        vbox.addWidget(self.buttonOk)

        self.setLayout(vbox)


    def eventClickButtonOk(self):
        mapName = self.editName.text()
        numRow = int(self.numRow.text())
        numColumn = int(self.numColumn.text())
        isNewMap = True
        listDungeons = self.rect.getListDungeons()
        if listDungeons is not None:
            for elem in listDungeons:
                if elem.name == mapName:
                    isNewMap = False
        if mapName != "" and isNewMap:
            self.editorMapWindow = EditorDungeonWindow(mapName, self.rect, numRow, numColumn)
            self.editorMapWindow.show()
            self.close()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Esiste già un Dungeon con questo nome in questo luogo oppure il campo è vuoto")
            self.msg.setWindowTitle("Attenzione")
            self.msg.show()

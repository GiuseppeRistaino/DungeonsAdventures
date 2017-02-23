from Frames.FrameGame import *

class DialogNewGame(QDialog):

    def __init__(self, parent):
        super(DialogNewGame, self).__init__(parent)

        self.parent = parent

        self.labelNumPlayer = QLabel("Inserisci il numero di giocatori")
        self.editNumPlayer = QLineEdit()
        self.editNumPlayer.setValidator(QIntValidator())
        self.buttonLoadAdv = QPushButton("Carica Avventura")
        self.buttonLoadAdv.clicked.connect(self.eventClickButtonLoadAdv)
        self.labelAdv = QLabel()
        self.buttonOk = QPushButton("OK")
        self.buttonOk.clicked.connect(self.eventClickButtonOk)
        self.adventure = None

        vbox = QVBoxLayout()
        vbox.addWidget(self.labelNumPlayer)
        vbox.addWidget(self.editNumPlayer)
        vbox.addWidget(self.buttonLoadAdv)
        vbox.addWidget(self.labelAdv)
        vbox.addWidget(self.buttonOk)

        self.setLayout(vbox)

    def eventClickButtonLoadAdv(self):
        fileDialog = QFileDialog()
        fname = fileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'Map files (*.map)')
        manager = Adventure_Manager()
        self.adventure = manager.load(fname)
        self.labelAdv.setText(self.adventure.name)


    def eventClickButtonOk(self):
        numPlayer = int(self.editNumPlayer.text())

        #controllare se il numero è accettabile
        if numPlayer != "" or self.adventure is None:
            self.frame = FrameGame(parent=self.parent, adventure=self.adventure)
            self.parent.setCentralWidget(self.frame)
            self.parent.setWindowTitle(self.adventure.name)
            self.close()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Bisogna caricare un'avventura e immettere il numero giusto di giocatori per andare avanti")
            self.msg.setWindowTitle("Attenzione")
            self.msg.show()

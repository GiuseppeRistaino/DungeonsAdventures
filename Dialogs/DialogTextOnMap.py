from Elements.Text import *

class DialogTextOnMap(QDialog):

    def __init__(self, rect=None, parent=None):
        super(DialogTextOnMap, self).__init__()
        self.parent = parent
        self.rect = rect
        layout = QVBoxLayout()
        label = QLabel("Inserisci il testo da trascrivere")
        layout.addWidget(label)
        self.edit = QLineEdit()
        layout.addWidget(self.edit)
        self.buttonOk = QPushButton("OK")
        self.buttonOk.clicked.connect(self.eventClickButtonOk)
        layout.addWidget(self.buttonOk)
        self.setLayout(layout)

    def eventClickButtonOk(self):
        t = self.edit.text()
        text = Text(t)
        self.rect.addText(text)
        self.close()
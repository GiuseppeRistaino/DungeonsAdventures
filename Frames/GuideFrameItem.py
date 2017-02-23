from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Database.DB_Manager import DB_Manager

PATH_ICON_RETURN = "img/icon_return"
MAX_WIDTH_BUTTON_RETURN = 50

class GuideFrameItem(QFrame):

    def __init__(self, window, dictionary, state):
        super(GuideFrameItem, self).__init__()

        self.window = window

        self.vbox = QVBoxLayout()

        self.buttonReturn = QPushButton()
        self.buttonReturn.setIcon(QIcon(QPixmap(PATH_ICON_RETURN)))
        self.buttonReturn.setMaximumWidth(MAX_WIDTH_BUTTON_RETURN)

        self.editText = QTextEdit()
        self.editText.setReadOnly(True)
        self.editText.setLineWrapMode(QTextEdit.WidgetWidth)

        self.populateEditText(dictionary, state)

        font = QFont("Times", 14, QFont.Normal, True)
        self.editText.setFont(font)
        cursor = self.editText.textCursor()
        cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.editText.setTextCursor(cursor)

        self.vbox.addWidget(self.buttonReturn)
        self.vbox.addWidget(self.editText)

        self.setLayout(self.vbox)

    #Scrive nel textedit gli elementi degli attributi che fanno parte di un determinato titolo (preso dal DB_Manager)
    def populateEditText(self, listItem, state):
        if state == self.window.STATE[0]:
            self.populate(listItem, DB_Manager.ATTRIBUTE_ABILITY)
        elif state == self.window.STATE[1]:
            self.populate(listItem, DB_Manager.ATTRIBUTE_WEAPON)
        elif state == self.window.STATE[2]:
            self.populate(listItem, DB_Manager.ATTRIBUTE_MAGIC)
        elif state == self.window.STATE[3]:
            self.populate(listItem, DB_Manager.ATTRIBUTE_INGREDIENT)
        elif state == self.window.STATE[4]:
            self.populate(listItem, DB_Manager.ATTRIBUTE_MONSTER)
        elif state == self.window.STATE[5]:
            self.populate(listItem, DB_Manager.ATTRIBUTE_ITEM)
        elif state == self.window.STATE[6]:
            self.populate(listItem, DB_Manager.ATTRIBUTE_POTION)
        elif state == self.window.STATE[7]:
            self.populate(listItem, DB_Manager.ATTRIBUTE_TALENT)

    #scrive nel text edit i listItem una sotto ogni list title
    def populate(self, listItem, listTitle):
        i = 0
        for elem in listItem:
            title = listTitle[i]
            i +=1
            if isinstance(elem, str):
                self.editText.append("<b>" + title + "<\b>")
                self.editText.append(elem)
            else:
                img = QImage()
                if isinstance(elem, QByteArray):
                    img.loadFromData(elem)
                    cursor = self.editText.textCursor()
                    cursor.movePosition(QTextCursor.End, QTextCursor.MoveAnchor)
                    format = QTextCharFormat()
                    format.setFontWeight(QFont.Bold)
                    cursor.insertText(title +"\n", format)
                    cursor.insertImage(img)
            self.editText.append("\n")

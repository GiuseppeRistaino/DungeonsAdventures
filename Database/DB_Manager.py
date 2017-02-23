import sys
from PyQt4 import QtCore, QtGui, QtSql



class DB_Manager():

    TABLE_ABILITY = "Ability"
    ATTRIBUTE_ABILITY = ("Nome", "Descrizione", "Prova", "Azione", "Ritentare", "Speciale",
                         "Sinergia", "Restrizioni", "Senza_addestramento")
    TABLE_WEAPON = "Arma"
    ATTRIBUTE_WEAPON = ("Nome", "Tipo", "Integrità", "Costo", "Danni_piccola", "Danni_media",
                        "Critico", "Gittata", "Peso")
    TABLE_MAGIC = "Incantesimo"
    ATTRIBUTE_MAGIC = ("Nome", "Scuola", "Livello", "Temo di lancio", "Componenti", "Raggio di azione",
                        "Area", "Bersaglio", "Durata", "Tiro salvezza", "Resistenza agli incantesimi",
                        "Descrizione", "Immagine")
    TABLE_INGREDEINT = "Ingrediente"
    ATTRIBUTE_INGREDIENT = ("Nome", "Luogo", "Percentuale", "Descrizione", "Costo")
    TABLE_MONSTER = "Mostro"
    ATTRIBUTE_MONSTER = ("Nome", "Tipo", "Taglia", "Vita", "Iniziativa", "Velocità", "CA", "Attacco_base", "Lotta",
                  "Attacco", "Attacco_completo", "Spazio", "Portata", "Attacco_speciale", "Qualità_speciale",
                  "Tiri_salvezza", "Forza", "Destrezza", "Costituzione", "Intelligenza", "Saggezza", "Carisma",
                  "Abilità", "Talento", "Organizzazione", "Grado_di_sfida", "Tesoro", "Allineamento", "Modificatore_di_livello",
                  "Descrizione", "Combattimento")
    TABLE_ITEM = "Oggetti"
    ATTRIBUTE_ITEM = ("Nome", "Resistenza", "Valore", "Peso", "Descrizione", "Immagine")
    TABLE_POTION = "Pozione"
    ATTRIBUTE_POTION = ("Nome", "Ricetta", "Tempo", "Effetto", "CD", "Valore")
    TABLE_TALENT = "Talenti"
    ATTRIBUTE_TALENT = ("Nome", "Descrizione", "Prerequisito", "Beneficio", "Normale", "Speciale")


    def __init__(self, DB_Name):
        self.createDB(DB_Name)


    def createDB(self, DB_Name):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(DB_Name)
        if not db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                       QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                     "This example needs SQLite support. Please read "
                                                     "the Qt SQL driver documentation for information "
                                                     "how to build it.\n\n"
                                                     "Click Cancel to exit."),
                                       QtGui.QMessageBox.Cancel)
            return False
        return True


    #Restituisce la lista dei nomi delle abilità
    def getListAbility(self):
        queryString = "SELECT * FROM " +self.TABLE_ABILITY
        return self.getListOfOneElementForRow(queryString)

    #Restituisce il dizionario contenente i valori della abilità data
    def getAbility(self, nameAbility):
        queryString = "SELECT * FROM " +self.TABLE_ABILITY +" WHERE " +self.ATTRIBUTE_ABILITY[0] +" = " +"\"" +nameAbility +"\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_ABILITY)

    # Restituisce la lista dei nomi delle armi
    def getListWeapon(self):
        queryString = "SELECT * FROM " + self.TABLE_WEAPON +" ORDER BY " +self.ATTRIBUTE_WEAPON[0]
        return self.getListOfOneElementForRow(queryString)

    #Restituisce il dizionario contenente i valori dell'arma data
    def getWeapon(self, nameWeapon):
        queryString = "SELECT * FROM " +self.TABLE_WEAPON +" WHERE " +self.ATTRIBUTE_WEAPON[0] +" = " +"\"" +nameWeapon +"\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_WEAPON)


    # Restituisce la lista dei nomi delle armi
    def getListMagic(self):
        queryString = "SELECT * FROM " + self.TABLE_MAGIC + " ORDER BY " + self.ATTRIBUTE_MAGIC[0]
        return self.getListOfOneElementForRow(queryString)


    # Restituisce il dizionario contenente i valori dalla magia data
    def getMagic(self, nameMagic):
        queryString = "SELECT * FROM " + self.TABLE_MAGIC + " WHERE " + self.ATTRIBUTE_MAGIC[0] + " = " + "\"" + nameMagic + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_MAGIC)

    # Restituisce la lista degli ingredienti
    def getListIngredient(self):
        queryString = "SELECT * FROM " + self.TABLE_INGREDEINT + " ORDER BY " + self.ATTRIBUTE_INGREDIENT[0]
        return self.getListOfOneElementForRow(queryString)


    # Restituisce il dizionario contenente i valori dall'ingrediente dato
    def getIngredient(self, name):
        queryString = "SELECT * FROM " + self.TABLE_INGREDEINT + " WHERE " + self.ATTRIBUTE_INGREDIENT[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_INGREDIENT)

    # Restituisce la lista dei mostri
    def getListMonster(self):
        queryString = "SELECT * FROM " + self.TABLE_MONSTER + " ORDER BY " + self.ATTRIBUTE_MONSTER[0]
        return self.getListOfOneElementForRow(queryString)

    # Restituisce il dizionario contenente i valori dal mostro dato
    def getMonster(self, name):
        queryString = "SELECT * FROM " + self.TABLE_MONSTER + " WHERE " + self.ATTRIBUTE_MONSTER[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_MONSTER)

    # Restituisce la lista degli oggetti
    def getListItem(self):
        queryString = "SELECT * FROM " + self.TABLE_ITEM + " ORDER BY " + self.ATTRIBUTE_ITEM[0]
        return self.getListOfOneElementForRow(queryString)

    # Restituisce il dizionario contenente i valori dall'oggetto dato
    def getItem(self, name):
        queryString = "SELECT * FROM " + self.TABLE_ITEM + " WHERE " + self.ATTRIBUTE_ITEM[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_ITEM)

    # Restituisce la lista delle pozioni
    def getListPotion(self):
        queryString = "SELECT * FROM " + self.TABLE_POTION + " ORDER BY " + self.ATTRIBUTE_POTION[0]
        return self.getListOfOneElementForRow(queryString)


    # Restituisce il dizionario contenente i valori dalla pozione data
    def getPotion(self, name):
        queryString = "SELECT * FROM " + self.TABLE_POTION + " WHERE " + self.ATTRIBUTE_POTION[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_POTION)

    # Restituisce la lista degli oggetti
    def getListTalent(self):
        queryString = "SELECT * FROM " + self.TABLE_TALENT + " ORDER BY " + self.ATTRIBUTE_TALENT[0]
        return self.getListOfOneElementForRow(queryString)

    # Restituisce il dizionario contenente i valori dal talento dato
    def getTalent(self, name):
        queryString = "SELECT * FROM " + self.TABLE_TALENT + " WHERE " + self.ATTRIBUTE_TALENT[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_TALENT)

    #restituisce gli elementi per ogni attributo di una data riga
    def getElementsInRowFromKey(self, queryString, attributeList):
        query = QtSql.QSqlQuery()
        query.exec(queryString)
        listItem = []
        while (query.next()):
            for elem in range(0, len(attributeList)):
                listItem.append(query.value(elem))
        return listItem

    def getListOfOneElementForRow(self, queryString):
        query = QtSql.QSqlQuery()
        query.exec(queryString)
        result = []
        while (query.next()):
            result.append(query.value(0))
        return result


class DB_Manager_Adventure():

    TABLE_ADVENTURE = "Adventure"
    ATTRIBUTE_ADVENTURE = ["ID", "Name", "Row", "Column"]
    TABLE_PLACE = "Place"
    ATTRIBUTE_PLACE = ["ID", "Adventure", "PosX", "PosY", "Pixmap"]
    TABLE_DUNGEON = "Dungeon"
    ATTRIBUTE_DUNGEON = ["ID", "Place", "Name", "Row", "Column"]
    TABLE_TERRAIN = "Terrain"
    ATTRIBUTE_TERRAIN = ["ID", "Dungeon", "PosX", "PosY", "Pixmap"]
    TABLE_ITEM = "Item"
    ATTRIBUTE_ITEM = ["ID", "Dungeon", "PosX", "PosY", "Pixmap", "Rotate"]

    def createDB(self, scene):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('adventures.db')
        if not db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                       QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                     "This example needs SQLite support. Please read "
                                                     "the Qt SQL driver documentation for information "
                                                     "how to build it.\n\n"
                                                     "Click Cancel to exit."),
                                       QtGui.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()


        query.exec_("create table '" + self.TABLE_ADVENTURE + "' ('"
                    + self.ATTRIBUTE_ADVENTURE[0] + "' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '"
                    + self.ATTRIBUTE_ADVENTURE[1] + "' TEXT UNIQUE,'"
                    + self.ATTRIBUTE_ADVENTURE[2] + "' TEXT,'"
                    + self.ATTRIBUTE_ADVENTURE[3] + "' TEXT);")
        query.exec_("create table '" + self.TABLE_PLACE + "' ('"
                    + self.ATTRIBUTE_PLACE[0] + "' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '"
                    + self.ATTRIBUTE_PLACE[1] + "' TEXT,'"
                    + self.ATTRIBUTE_PLACE[2] + "' TEXT,'"
                    + self.ATTRIBUTE_PLACE[3] + "' TEXT,'"
                    + self.ATTRIBUTE_PLACE[4] + "' TEXT);")
        query.exec_("create table '" + self.TABLE_DUNGEON + "' ('"
                    + self.ATTRIBUTE_DUNGEON[0] + "' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '"
                    + self.ATTRIBUTE_DUNGEON[1] + "' TEXT,'"
                    + self.ATTRIBUTE_DUNGEON[2] + "' TEXT,'"
                    + self.ATTRIBUTE_DUNGEON[3] + "' TEXT,'"
                    + self.ATTRIBUTE_DUNGEON[4] + "' TEXT);")
        query.exec_("create table '" + self.TABLE_TERRAIN + "' ('"
                    + self.ATTRIBUTE_TERRAIN[0] + "' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '"
                    + self.ATTRIBUTE_TERRAIN[1] + "' TEXT,'"
                    + self.ATTRIBUTE_TERRAIN[2] + "' TEXT,'"
                    + self.ATTRIBUTE_TERRAIN[3] + "' TEXT,'"
                    + self.ATTRIBUTE_TERRAIN[4] + "' TEXT);")
        query.exec_("create table '" + self.TABLE_ITEM + "' ('"
                    + self.ATTRIBUTE_ITEM[0] + "' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '"
                    + self.ATTRIBUTE_ITEM[1] + "' TEXT,'"
                    + self.ATTRIBUTE_ITEM[2] + "' TEXT,'"
                    + self.ATTRIBUTE_ITEM[3] + "' TEXT,'"
                    + self.ATTRIBUTE_ITEM[4] + "' TEXT,'"
                    + self.ATTRIBUTE_ITEM[5] + "' TEXT);")

        nameAdventure = scene.name
        rowAdventure = str(scene.numRow)
        columnAdventure = str(scene.numColumn)
        query.exec_(
            "insert into " + self.TABLE_ADVENTURE + " values(NULL, '" + nameAdventure + "', '" + rowAdventure + "', '" + columnAdventure + "')")

        query.exec("SELECT ID FROM Adventure WHERE Name = '" +nameAdventure +"'")
        query.next()
        adventureID = query.value(0)
        listPlaces = scene.getListPlaces()
        for place in listPlaces:
            x = str(place.pos().x())
            y = str(place.pos().y())
            pathRes = str(place.pathRes)
            query.exec_(
                "INSERT INTO " + self.TABLE_PLACE + " values(NULL, '" + str(adventureID) + "', '" + str(x) + "', '" + str(y) + "', '" +str(pathRes) + "')")


        #query.exec_("insert into " +self.TABLE_ADVENTURE + " values(100, '" +nameAdventure + "',"+ "'" +rowAdventure + "',"+ "'ada')")
        #query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
        #query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
        #query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
        #query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
        return True





if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    DB_Manager()
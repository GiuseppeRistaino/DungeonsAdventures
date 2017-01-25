import pickle

class Adventure():

    def __init__(self, name, numRow, numColumn, places=None, textes=None):
        self.name = name
        self.numRow = numRow
        self.numColumn = numColumn
        #places è una lista di Place
        self.places = places
        self.textes = textes

class Place():
    def __init__(self, x, y, pathRes, dungeons=None):
        self.x = x
        self.y = y
        #pixmap è la stringa del filename
        self.pathRes = pathRes
        #dungeons è una lista di dungeon
        self.dungeons = dungeons

class Terrain():
    def __init__(self, x, y, pathRes):
        self.x = x
        self.y = y
        self.pathRes = pathRes

class Item():
    def __init__(self, x, y, rotate, pathRes):
        self.x = x
        self.y = y
        self.rotate = rotate
        self.pathRes = pathRes

class Npg():
    def __init__(self, x, y, pathRes, name):
        self.x = x
        self.y = y
        self.pathRes = pathRes
        self.name = name

class Dungeon():
    def __init__(self, name, numRow, numColumn, terrains=None, items=None, npgs=None):
        self.name = name
        self.numRow = numRow
        self.numColumn = numColumn
        self.terrains = terrains
        self.items = items
        self.npgs = npgs

class Text():
    def __init__(self, string, x, y):
        self.string = string
        self.x = x
        self.y = y


class Adventure_Manager():


    def save(self, scene, fname):

        listPlaces = []
        for place in scene.getListPlaces():
            listDungeon = []
            for dungeon in  place.dungeons:
                listTerrain = []
                listItem = []
                listNpg = []
                for terrain in dungeon.getListTerrains():
                    t = Terrain(terrain.pos().x(), terrain.pos().y(), terrain.pathRes)
                    listTerrain.append(t)
                for item in dungeon.getListItems():
                    i = Item(item.pos().x(), item.pos().y(), item.rotate,item.pathRes)
                    listItem.append(i)
                for npg in dungeon.getListNpgs():
                    n = Npg(npg.x, npg.y, npg.pathRes, npg.name)
                    listNpg.append(n)
                d = Dungeon(dungeon.name, dungeon.numRow, dungeon.numColumn, listTerrain, listItem, listNpg)
                listDungeon.append(d)
            p = Place(place.pos().x(), place.pos().y(), place.pathRes, listDungeon)
            listPlaces.append(p)

        textes = []
        for text in scene.getLisTextes():
            t = Text(text.string, text.x, text.y)
            textes.append(t)


        adv = Adventure(scene.name, scene.numRow, scene.numColumn, listPlaces, textes)

        with open(fname, 'wb') as output:
            pickle.dump(adv, output, pickle.HIGHEST_PROTOCOL)


    def load(self, fname):
        with open(fname, 'rb') as input:
            adv = pickle.load(input)
        return adv

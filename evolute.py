import random as r

worldSize = 128
startingPopulation = 5
genAmount = 5

occupiedX = []
occupiedY = []

class Pos:
    def __init__(self, locationX, locationY):
        self.locationX = locationX
        self.locationY = locationY

    def currentLocation(self):
        return self.locationX, self.locationY

    def storedLocations(self):
        occupiedX.append(self.locationX)
        occupiedY.append(self.locationY)


class Lute:
    def __init__(self, ID, lifeStatus, location):
        self.ID = ID
        self.lifeStatus = lifeStatus
        self.location = location

    def store_ID(self):
        return self.ID

    def getLifeStatus(self):
        if self.lifeStatus == 1:
            return True
        else: return False

class NewWorld:

    def __init__(self, worldSize, startingPopulation, genAmount):
        self.worldSize = worldSize
        self.startingPopulation = startingPopulation
        self.genAmount = genAmount

    def spawn():
        p = 1
        for l in range(0,startingPopulation):
            lo = Pos(r.randint(1,worldSize),r.randint(1,worldSize))
            l = Lute(p,r.randint(0,1),lo)
            print(f"Lute: {str(p)}, Alive: {l.getLifeStatus()}, Location: {lo.currentLocation()}")
            Pos.storedLocations(lo)
            p = p + 1

world = NewWorld(worldSize, startingPopulation, genAmount)
NewWorld.spawn()

print(f"Occupied in X: {occupiedX}")
print(f"Occupied in Y: {occupiedY}")






class World:
    pass

worldSize = 3
worldSizeX = worldSize
worldSizeY = worldSize
startingPopulation = 3
genAmount = 5

worldMapX = []
worldMapY = []

def evolute():

    for p in range(startingPopulation):
        generateStartLocation(worldSize)

    # print("WorldMapX: " + str(worldMapX))
    # print("WorldMapY: " + str(worldMapY))


# def sensoryInput():
#     position = (cellX, cellY)
#     checkSurroundings(position)

def generateStartLocation(worldSize):

    cellX = r.randint(1,worldSize)
    cellY = r.randint(1,worldSize)

    if cellX == worldMapX:
        generateStartLocation(worldSize)
    else:
        worldMapX.append(cellX)

    if cellY == worldMapY:
        generateStartLocation(worldSize)
    else:
        worldMapY.append(cellY)
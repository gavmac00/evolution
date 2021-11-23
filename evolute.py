import random as r

worldSize = 128
startingPopulation = 5
genAmount = 5

class Pos:
    def __init__(self, locationX, locationY):
        self.locationX = locationX
        self.locationY = locationY

    def currentLocation(self):
        return self.locationX, self.locationY

class Lute:
    def __init__(self, lifeStatus):
        self.lifeStatus = lifeStatus

    def getStatus(self):
        if self.lifeStatus == 1:
            return True
        else: return False

class NewWorld:

    def __init__(self, worldSize, startingPopulation, genAmount):
        self.worldSize = worldSize
        self.startingPopulation = startingPopulation
        self.genAmount = genAmount
        self.lutes = []

    def spawnThem(self, lute):
        if len(self.lutes) < self.startingPopulation:
            self.lutes.append(lute)
            return True
        return False

l1 = Lute(1)
l2 = Lute(1)
l3 = Lute(0)

lo1 = Pos(r.randint(1,worldSize),r.randint(1,worldSize))
lo2 = Pos(r.randint(1,worldSize),r.randint(1,worldSize))
lo3 = Pos(r.randint(1,worldSize),r.randint(1,worldSize))

world = NewWorld(worldSize, startingPopulation, genAmount)

print(f"Alive: {l1.getStatus()}, Location: {lo1.currentLocation()}")
print(f"Alive: {l2.getStatus()}, Location: {lo2.currentLocation()}")
print(f"Alive: {l3.getStatus()}, Location: {lo3.currentLocation()}")






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

# def outputE():
#     print("")
# def outputR():
#     print("")
# def brain():
#     print("")

# def spawn():




# def checkSurroundings(position):
#     nearbyBlocks = {"nw","n","ne","e","se","s","sw","w"}
#     # for x in nearbyBlocks:

evolute()
import random as r
from typing import Sized

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

    print("WorldMapX: " + str(worldMapX))
    print("WorldMapY: " + str(worldMapY))


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
#generateStartLocation(worldSize)
import random as r

worldSize = 100
worldSizeX = worldSize
worldSizeY = worldSize
startingPopulation = 5
genAmount = 5

def evolute():
    entry = input("Use preset world conditions (y/n): ")
    if entry == 'n':
        worldSize = input("New World Size: ")
        worldSizeX = worldSize
        worldSizeY = worldSize
        startingPopulation = input("New Starting Polulaton Size: ")
        genAmount = input("Number of Generations: ")
    gen = 0
    print("\nGeneration: " + str(gen))

# def sensoryInput():
#     position = (cellX, cellY)
#     checkSurroundings(position)

def generateStartLocation(worldSize):
    cellX = r.randint(1,worldSize)
    cellY = r.randint(1,worldSize)

    location = (cellX, cellY)  #tuple

    # for playerNo in range(worldSize):
        # location[0] = worldMapX
    return location

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
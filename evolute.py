import random as r

class Pos:
    def __init__(P, locationX, locationY):
        P.locationX = locationX
        P.locationY = locationY

    def currentLocation(P):
        return P.locationX, P.locationY

    def storeLocation(P):
        occupiedX.append(P.locationX)
        occupiedY.append(P.locationY)

    def move():
        for i in range(0, World.living()):
            #take in location (done)
            #check neighbours (done)
            #choose where to go
            #go
            X = occupiedX[i] #taking in location
            Y = occupiedY[i]
            neighbours = Pos.checkNeighbours(X,Y) # getting each lute's neighbours
            print(f"{i+1}: Neighbours: {neighbours}")

    def checkNeighbours(X,Y):
        ### check boundary condition
        neighbourList = []
        for x in range(X-1,X+1):
            for y in range(Y-1,Y+1):
                if y in occupiedY & y != Y:
                    if x in occupiedX & x != X:
                        coordinate = "(" + str(occupiedX[x]) + "," + str(occupiedY[y]) + ")" #not tested yets
                        neighbourList.append(coordinate)

        return neighbourList

class Lute:
    def __init__(L, lifeStatus, location):
        L.lifeStatus = lifeStatus
        L.location = location

    def storeLifeStatus(L):
        worldLifeStatus.append(L.lifeStatus)

class NewWorld:
    def spawn():
        count = 1
        for l in range(0, startingPopulation):
            lo = Pos(r.randint(1,worldSize), r.randint(1,worldSize))
            l = Lute(1,lo)
            print(f"Lute: {count}, Alive: True, Location: {lo.currentLocation()}")
            Pos.storeLocation(lo)
            Lute.storeLifeStatus(l)
            count = count + 1

class World:
    def living():
        alive = len(worldLifeStatus)
        return alive

    def kill(ID):
        IDX = ID-1
        del(occupiedX[IDX])
        del(occupiedY[IDX])
        del(worldLifeStatus[IDX])
        print(f"Lute {ID} killed.")

    def nextGen(gen):        
        print(f"\nGeneration: {gen}\n")
        if gen <= genAmount:
            Pos.move()
            userOuput.QDataRequest()
            userOuput.QLocationRequest()
            userOuput.QKillRequest()

class userOuput:
    def QDataRequest():
        outputDataRequest = input(f"Output Data? (Y/N): ")
        if outputDataRequest == "Y":
            userOuput.Data()

    def Data():
        alive = World.living()
        if alive > 0:
            print(f"\nCurrently Living: {alive}/{startingPopulation} lutes.")
            # print(f"In the population, the status of life is {worldLifeStatus}.")
            print(f"All cells occupied in X: {occupiedX}")
            print(f"All cells occupied in Y: {occupiedY}")
        else:
            print(f"\nCurrently Living: {alive}/{startingPopulation} lutes.")

    def QLocationRequest():
        locationRequest = input(f"Query Lute locations? (Y/N): ")
        if locationRequest == "Y":
            facilitateLocationRequest()

    def QKillRequest():
        killRequest = input(f"Want to kill any? (Y/N): ")
        if killRequest == "Y":
            facilitateKillRequest(alive)

def facilitateLocationRequest():
    count = 0
    while count < startingPopulation:
        ID = input(f"Query a Lute number's coordiantes: (Enter a number between 1 and {World.living()}): ")
        ID = int(ID)
        print(f"Coordinates of Lute {ID}: ({occupiedX[ID-1]},{occupiedY[ID-1]})\n")
        count += 1
        if count < World.living():
            exitRequest = input(f"Query another? (Y/N): ")
            if exitRequest == "N": break

def facilitateKillRequest(alive):
    while alive > 0:
        ID = input(f"Enter the Lutes ID (Between 1 and {World.living()}): ")
        ID = int(ID)
        World.kill(ID)
        alive =- 1
        userOuput.QDataRequest()
        if alive > 0:
            exitRequest = input(f"\nKill another? (Y/N): ")
            if exitRequest == "N": break

#######################
occupiedX = []
occupiedY = []
worldLifeStatus = []

worldSize = input("Set world size: ")
startingPopulation = input("Set starting population: ")
genAmount = input("Set the number of generations: ")

worldSize = int(worldSize)
startingPopulation = int(startingPopulation)
genAmount = int(genAmount)
alive = startingPopulation

print(f"\nWorldsize: {worldSize} x {worldSize}.")
print(f"The population is {startingPopulation}.")
print(f"There will be {genAmount} generations.\n")

NewWorld.spawn()

for gen in range(1, genAmount+1):
    World.nextGen(gen)

print("Simulation Complete")
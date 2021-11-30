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
            neighbours = Pos.checkNeighbours(i,X,Y) # getting each lute's neighbours
            print(f"{i+1}: Neighbours: {neighbours}")

    def checkNeighbours(i,X,Y):
        neighbourList = []
        #boundary conditions & supplementary computation
        if X == 1: # left wall, no neighbours on the left, only cells 2-6
            if Y + 1 in occupiedY:
                print(f"There is a lute in row: Y = {Y+1}, which is one row above the lute in ({X},{Y})")
                print(f"Will now check if it is a neighbour...")
                z = occupiedY.index(Y+1)
                if occupiedX[z] == X:
                    print(f"There is a neighbour, above the lute ({X},{Y}) in the cell: ({occupiedX[z]},{Y+1})")
                    neighbourList.append(f"({occupiedX[z]},{Y+1})")
                elif occupiedX[z] == X+1:
                    print(f"There is a neighbour, above and right one cell from the lute ({X},{Y}) in the cell: ({occupiedX[z]},{Y+1})")
                    neighbourList.append(f"({occupiedX[z]},{Y+1})")
                else:
                    print(f"There was lute in the row above, but it was not a neighbour.")
                    print(f"The lute mentioned was in cell ({occupiedX[z]},{occupiedY[z]})")
            else:
                for s in range(0,i-1):
                    if occupiedY[s] == Y:
                        print(f"There is another lute along the row of the given lute, row {Y}")
                        print(f"Checking if it is a neighbour...")
                        q = occupiedY.index(Y)
                        if occupiedX[q] == X+1:
                            print(f"There is a neighbour to the right of lute ({X},{Y}) in the cell: ({occupiedX[q]},{Y})")
                            neighbourList.append(f"({occupiedX[q]},{Y})")
                        else:
                            print(f"There was lute in the same row, but it was not a neighbour.")
                            print(f"The lute mentioned was in cell ({occupiedX[q]},{occupiedY[q]})")
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
        while count != startingPopulation + 1:
            for l in range(0, startingPopulation):
                X = r.randint(1,worldSize)
                Y = r.randint(1,worldSize)
                if NewWorld.checkReplica(X,Y) == True:
                    #print("Found a replica")
                    pass
                elif len(occupiedY) == startingPopulation:
                    break
                else:
                    lo = Pos(X,Y)
                    l = Lute(1,lo)
                    print(f"Lute: {count}, Alive: True, Location: {lo.currentLocation()}")
                    Pos.storeLocation(lo)
                    Lute.storeLifeStatus(l)
                    count = count + 1
            #print(f"count: {count}")

    def checkReplica(X,Y):
        for s in range(0,len(occupiedX)):
            if occupiedX[s] == X and occupiedY[s] == Y:
                return True
        return False

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
            # userOuput.QDataRequest()
            # userOuput.QLocationRequest()
            # userOuput.QKillRequest()

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
import random as r

worldSize = 128
startingPopulation = 5
alive = startingPopulation
population = alive
genAmount = 5
occupiedX = []
occupiedY = []
worldLifeStatus = []

class Pos:
    def __init__(P, locationX, locationY):
        P.locationX = locationX
        P.locationY = locationY

    def currentLocation(P):
        return P.locationX, P.locationY

    def storeLocation(P):
        occupiedX.append(P.locationX)
        occupiedY.append(P.locationY)

    # def move(location): ######


class Lute:
    def __init__(L, lifeStatus, location):
        L.lifeStatus = lifeStatus
        L.location = location

    def storeLifeStatus(L):
        worldLifeStatus.append(L.lifeStatus)

class NewWorld:
    def spawn():
        count = 1
        for l in range(0,startingPopulation):
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
            userOuput.QDataRequest()
            userOuput.QLocationRequest()
            userOuput.QKillRequest()

class userOuput:

    def __init__(U):
        pass

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

print(f"\nWorldsize: {worldSize} x {worldSize}.")
print(f"The population is {startingPopulation}.")
print(f"There will be {genAmount} generations.\n")

NewWorld.spawn()

for gen in range(1, genAmount+1):
    World.nextGen(gen)

print("Simulation Complete")
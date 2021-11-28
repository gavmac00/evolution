import random as r

worldSize = 128
startingPopulation = 5
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

class Lute:
    def __init__(L, lifeStatus, location):
        L.lifeStatus = lifeStatus
        L.location = location

    def storeLifeStatus(L):
        worldLifeStatus.append(L.lifeStatus)

class NewWorld:
    def spawn():
        count = 1
        print("\n")
        for l in range(0,startingPopulation):
            lo = Pos(r.randint(1,worldSize), r.randint(1,worldSize))
            l = Lute(1,lo)
            print(f"Lute: {count}, Alive: True, Location: {lo.currentLocation()}")
            Pos.storeLocation(lo)
            Lute.storeLifeStatus(l)
            count = count + 1

class World:
    def __init__(W, ID):
        W.ID = ID
    
    def living():
        alive = 0
        for l in worldLifeStatus:
            if worldLifeStatus[l] == 1:
                alive +=1
        print(f"\nCurrently Living: {alive}/{startingPopulation} lutes.")

    def kill(ID):
        del(occupiedX[ID-1])
        del(occupiedY[ID-1])
        worldLifeStatus[ID-1] = 0

NewWorld.spawn()
World.living()

print(f"\nAll cells occupied in X: {occupiedX}")
print(f"All cells occupied in Y: {occupiedY}")
print(f"\nWorldsize: {worldSize} x {worldSize}.")
print(f"The starting population is {startingPopulation}.")
print(f"In the population, the status of life is {worldLifeStatus}.\n")

print(f"There will be {genAmount} generations.\n")

locationRequest = input(f"Want to query a lutes location? (Y/N): ")
if locationRequest == "Y":
    count = 0
    while count < startingPopulation:
        ID = input(f"Query a Lute number's coordiantes: (Enter a number between 1 and {startingPopulation}): ")
        ID = int(ID)
        print(f"({occupiedX[ID-1]},{occupiedY[ID-1]})")
        count += 1

killRequest = input(f"Want to kill any? (Y/N): ")
if killRequest == "Y":
    ID = input(f"Enter the Lutes ID (Between 1 and {startingPopulation}): ")
    ID = int(ID)
    World.kill(ID)
    print(f"\nAll cells occupied in X: {occupiedX}")
    print(f"All cells occupied in Y: {occupiedY}")
    print(f"In the population, the status of life is {worldLifeStatus}.\n")
    World.living()
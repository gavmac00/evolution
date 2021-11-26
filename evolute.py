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

NewWorld.spawn()

# print(f"\nAll cells occupied in X: {occupiedX}")
# print(f"All cells occupied in Y: {occupiedY}")
print(f"\nWorldsize: {worldSize} x {worldSize}.")
print(f"The starting population is {startingPopulation}.")
print(f"In the population, the status of life is {worldLifeStatus}.\n")

# print(f"There will be {genAmount} generations.\n")

# count = 1
# while count < 6:
#     ID = input(f"Query a Lute number's coordiantes: (Enter a number): ")
#     ID = int(ID)
#     print(f"({occupiedX[ID-1]},{occupiedY[ID-1]})")
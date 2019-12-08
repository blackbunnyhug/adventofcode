from pathlib import Path
#Calculating fuel needed for the Santa-saving spaceship!

def main():
    totalFuel(readModules())

def readModules():
    #opens file and places it into a list
    shipModules = []
    base = Path(__file__).parent
    moduleFile = (base / "./day1.txt").resolve()

    with open(moduleFile) as file:

        for module in file:
            shipModules.append(int(module))

        return shipModules
            

def fuelMath(shipModules):
    #takes each module and calculates fuel needed using x/3-2 formula, adds to total
    fuelreq = 0

    for moduleWeight in shipModules:
        modulefuelreq = 0
        modulefuelreq = moduleWeight//3-2
        fuelreq = fuelreq + modulefuelreq 

    return fuelreq


def totalFuel(shipModules):
    #prints total fuel
    fuelreq = fuelMath(shipModules)
    print ("The total amount of fuel needed to transport all ship modules is: "+ str(fuelreq))

main()
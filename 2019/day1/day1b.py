import sys
from pathlib import Path
#Calculates the fuel needed to transport the Santa-saving spaceship, including the added mass from the fuel itself


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
    #takes the mass of each module and calculates the fuel needed, then calculates the fuel needed for the additional mass added to carry the fuel
    # using x/3-2 formula, tallies into a total
    fuelReq = 0   
    addedFuel = 0 

    for moduleMass in shipModules:
        modFuelMass = 0
        modFuelMass = moduleMass//3-2
        fuelReq = fuelReq + modFuelMass
           
        while (modFuelMass//3-2) > 0:  
            addedFuel = modFuelMass//3-2
            fuelReq = fuelReq + addedFuel

            if modFuelMass > 0:
                modFuelMass = addedFuel
                print(addedFuel)
            else:
                modFuelMass = 0
        
        return fuelReq


def totalFuel(shipModules):
    #prints total fuel
    fuelreq = fuelMath(shipModules)
    print ("The total amount of fuel needed to transport all ship modules is: "+ str(fuelreq))

        
main()
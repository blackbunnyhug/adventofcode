from pathlib import Path
import sys
#Reads and resets the intcode computer to the state it was in before the 1202 error

def main():

    intCode = readIntCode() 
    Computer(intCode, 12, 2)

def readIntCode():
    #opens, reads, and converts the intcode file to a list of numbers
    base = Path(__file__).parent
    intCodeFile = (base / "./day2.txt").resolve()

    with open(intCodeFile) as file:
        intCode = file.read()

    intCode = intCode.strip("\n").split(",")
    intCode = list(map(int, intCode))

    return intCode
    

def Computer(intCode, noun, verb):
    #loops through intcode list, reading and executing opcodes
    intCode[1] = noun
    intCode[2] = verb
    currentOpCode = 0
    intCodeSlice = intCode[currentOpCode:currentOpCode + 4]

    while True:
        intCodeSlice = intCode[currentOpCode:currentOpCode + 4]

        if(intCodeSlice[0] == 1):
            value = intCode[intCodeSlice[1]] + intCode[intCodeSlice[2]]
        elif(intCodeSlice[0] == 2):
            value = intCode[intCodeSlice[1]] * intCode[intCodeSlice[2]]
        elif(intCodeSlice[0] == 99):
            stopCode(intCode)
        
        intCode.insert(intCodeSlice[3], value)
        del intCode[intCodeSlice[3] + 1]
        currentOpCode += 4

        
def stopCode(intCode):
    #prints the final opcode located at position 0 once opcode 99 has been executed
    print("Program output: " + str(intCode[0]))
    sys.exit()

main()
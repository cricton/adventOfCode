

def checkForSymbols(content, currentNum, charPos, lineNumber):
    numberLength = len(str(currentNum))

    linesToCheck = []
    if lineNumber == 0:
        for i in range(0,2):
            linesToCheck.append(content[lineNumber + i])
    elif lineNumber == len(content)-1:
        for i in range(-1,1):
            linesToCheck.append(content[lineNumber + i])
    else:
        for i in range(-1,2):
            linesToCheck.append(content[lineNumber + i])

    for line in linesToCheck:
        startIndex = max(0, charPos - numberLength - 1)
        stopIndex = min(len(line)-1, charPos + 1)
        print('\n')
        for i in range(startIndex, stopIndex):
            char = line[i]
            if char != '.' and char.isdigit() is False:
                return True
    return False
def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    sum = 0
    for lineNumber, line in enumerate(content):
        currentNum = 0
        for charPos, char in enumerate(line):
            if char.isdigit():
                currentNum=currentNum*10+int(char)
                if charPos == len(line)-1:
                    checkForSymbols(content, currentNum, charPos, lineNumber)
                    sum += currentNum
            elif currentNum>0:
                if checkForSymbols(content, currentNum, charPos, lineNumber):
                    sum += currentNum
                currentNum = 0
                
                
    print("The solution is:",sum)

def checkForNumbers(content, charPos, lineNumber):

    foundNumbers = []
    linesToCheck = []
    if lineNumber == 0:
        for i in range(0,2):
            linesToCheck.append(content[lineNumber + i])
    elif lineNumber == len(content)-1:
        for i in range(-1,1):
            linesToCheck.append(content[lineNumber + i])
    else:
        for i in range(-1,2):
            linesToCheck.append(content[lineNumber + i])

    currentNumber = 0
    for line in linesToCheck:
        startIndex = max(0, charPos - 1)
        stopIndex = min(len(line)-1, charPos + 1)
        i = startIndex
        #print("\n")
        while i < stopIndex + 1:
            char = line[i]
            #print(char, end='')
            if char.isdigit():
                currentNumber = int(char)
                #Check for digits to the left
                for leftIndex in range(1, i+1):
                    charToCheck = line[i - leftIndex]
                    if charToCheck.isdigit():
                        currentNumber = currentNumber + int(charToCheck) * pow(10,leftIndex)
                    else:
                        break
                # Check for digits to the right
                for rightIndex in range(1, len(line) - i):
                    charToCheck = line[i + rightIndex]
                    if charToCheck.isdigit():
                        currentNumber = currentNumber * 10 + int(charToCheck)
                    else:
                        #Adjust pointer after finding all digits
                        i = rightIndex + i
                        break

            else:
                i+=1
            if True:
                if currentNumber > 0:
                    foundNumbers.append(currentNumber)
                currentNumber = 0
    return foundNumbers
def problem2():
    print("Problem 2: ")
    input = open("input.txt")

    content = input.readlines()

    sum = 0
    for lineNumber, line in enumerate(content):
        for charPos, char in enumerate(line):
            if char == '*':
                adjacentNumbers = checkForNumbers(content, charPos, lineNumber)
                if len(adjacentNumbers) == 2:
                    print(adjacentNumbers)
                    sum += adjacentNumbers[0]*adjacentNumbers[1]
    print("The solution is:", sum)


if __name__ == "__main__":
    #problem1()
    problem2()

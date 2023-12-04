
def problem1():
    input = open("input.txt")

    sum = 0
    for line in input:
        firstNum = -1
        lastNum = -1
        for char in line:
            if char.isdigit():
                if firstNum == -1:
                    firstNum = char
                lastNum = char
        sum += int(firstNum)*10+int(lastNum)
        
    print(sum)

def problem2():
    input = open("input.txt")
    
    sum = 0
    for line in input:
        firstNum = -1
        lastNum = -1
        for index,char in enumerate(line):
            if char.isdigit():
                if firstNum == -1:
                    firstNum = char
                lastNum = char
            elif char in ['o','t','f','s','e','n']:
                toAdd = -1
                if char == 'o':
                    if line.find("one", index, index+3)>-1:
                        toAdd = 1
                elif char == 't':
                    if line.find("two", index, index+3)>-1:
                        toAdd = 2
                    elif line.find("three", index, index+5)>-1:
                        toAdd = 3
                elif char == 'f':
                    if line.find("four", index, index+4)>-1:
                        toAdd = 4
                    elif line.find("five", index, index+4)>-1:
                        toAdd = 5
                elif char == 's':
                    if line.find("six", index, index+3)>-1:
                        toAdd = 6
                    elif line.find("seven", index, index+5)>-1:
                        toAdd = 7
                elif char == 'e':
                    if line.find("eight", index, index+5)>-1:
                        toAdd = 8
                elif char == 'n':
                    if line.find("nine", index, index+4)>-1:
                        toAdd = 9
                
                if toAdd != -1:
                    if firstNum == -1:
                        firstNum = toAdd
                    lastNum = toAdd
                    
        #print("Adding:",int(firstNum)*10+int(lastNum))
        sum += int(firstNum)*10+int(lastNum)
            
    print(sum)
    

    

if __name__=="__main__":
    problem1()
    problem2()


def problem1():
    print("Problem 1: ")
    input = open("input.txt")

    sum = 0
    for lineNumber, line in enumerate(input):
        isPullPossible = True
        line = line.split(":")[1]
        pulls = line.split(";")
        
        for pull in pulls:

            if isPullPossible == False:
                break
            colors = pull.split(",")

            for color in colors:
                count= int(''.join(filter(str.isdigit, color)))
                if 'd' in color:
                    if count > 12:
                        isPullPossible = False
                        break
                elif 'g' in color:
                    if count > 13:
                        isPullPossible = False
                        break
                elif 'b' in color:
                    if count > 14:
                        isPullPossible = False
                        break
        if isPullPossible == True:
            sum += lineNumber+1

    print("The solution is:",sum)

def problem2():
    print("Problem 2: ")
    input = open("input.txt")

    sum = 0
    for lineNumber, line in enumerate(input):
        isPullPossible = True
        line = line.split(":")[1]
        pulls = line.split(";")
        minRed = 0
        minGreen = 0
        minBlue = 0
        for pull in pulls:
            colors = pull.split(",")

            for color in colors:
                count= int(''.join(filter(str.isdigit, color)))
                if 'd' in color:
                    if count > minRed:
                        minRed = count
                elif 'g' in color:
                    if count > minGreen:
                        minGreen = count
                elif 'b' in color:
                    if count > minBlue:
                        minBlue = count
        
        sum += minRed*minBlue*minGreen

    print("The solution is:",sum)
    


    

if __name__=="__main__":
    problem1()
    problem2()

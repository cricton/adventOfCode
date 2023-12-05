


def problem1():
    print("Problem 1: ")
    input = open("input.txt")


    sum = 0
    for line in input:
        line = line.split(":")[1]
        winNumbers = list(filter(None,line.split("|")[0].split(" ")))
        ownedNumbers = list(filter(None,line.split("|")[1].split("\n")[0].split(" ")))

        hits = 0
        for number in winNumbers:
            if number in ownedNumbers:
                hits += 1
        if hits > 0:
            sum += pow(2, hits-1)

    print("The solution is:",sum)


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()
    sum = 0

    with open('input.txt') as f:
        line_count = 0
        for line in f:
            line_count += 1
    tickets = [1]*line_count
    for lineNumber, line in enumerate(content):
        line = line.split(":")[1]
        winNumbers = list(filter(None,line.split("|")[0].split(" ")))
        ownedNumbers = list(filter(None,line.split("|")[1].split("\n")[0].split(" ")))

        hits = 0
        for number in winNumbers:
            if number in ownedNumbers:
                hits += 1
        for i in range(hits):
            tickets[lineNumber+i+1] += tickets[lineNumber]
    for i in tickets:
        sum+=i
    print("The solution is:",sum)


if __name__ == "__main__":
    problem1()
    print("\n")
    problem2()

import sys
import numpy


def mapValues(content, values):
    lines = []
    for line in content:
        toAppend = line.split("\n")[0].split(" ")
        if len(toAppend) == 1:
            break
        lines.append(toAppend)

    for valueIndex,value in enumerate(values):
        for line in lines:
            value = int(value)
            sourceStart = int(line[1])
            destinationStart = int(line[0])
            rangeLength = int(line[2])
            if sourceStart <= value < (sourceStart + rangeLength):
                offset = value - sourceStart
                values[valueIndex] = (destinationStart + offset)

    return values


def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    seedsToPlant = content[0].split("\n")[0].split(" ")[1:]

    mapped = []
    for lineNumber, line in enumerate(content):
        if line == "seed-to-soil map:\n":
            mapped = mapValues(content[lineNumber + 1:], seedsToPlant)
        if line == "soil-to-fertilizer map:\n":
            mapped = mapValues(content[lineNumber + 1:], mapped)
        if line == "fertilizer-to-water map:\n":
            mapped = mapValues(content[lineNumber + 1:], mapped)
        if line == "water-to-light map:\n":
            mapped = mapValues(content[lineNumber + 1:], mapped)
        if line == "light-to-temperature map:\n":
            mapped = mapValues(content[lineNumber + 1:], mapped)
        if line == "temperature-to-humidity map:\n":
            mapped = mapValues(content[lineNumber + 1:], mapped)
        if line == "humidity-to-location map:\n":
            mapped = mapValues(content[lineNumber + 1:], mapped)

    print("Locations: ", min(mapped))

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def getNextLineEnd(content):
    for lineNumber,line in enumerate(content):
        if line == "\n":
            return lineNumber

def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    seedsToPlant = content[0].split("\n")[0].split(" ")[1:]
    startingPoints = seedsToPlant[0::2]
    ranges = seedsToPlant[1::2]

    print(startingPoints)
    print(ranges)
    completeRange = 0
    for num in ranges:
        completeRange += int(num)
    print(completeRange)

    minLocation = sys.maxsize
    for index, startingPoint in enumerate(startingPoints):
        mapped = numpy.arange(int(startingPoint), int(ranges[index]) + int(startingPoint), 1)

        print("Checking",index+1, "starting point")

        for lineNumber, line in enumerate(content):
            if has_numbers(line) or line == "\n":
                continue
            if line == "humidity-to-location map:\n":
                print("Mapping to location")
                mapped = mapValues(content[lineNumber + 1:], mapped)
                if min(mapped) < minLocation:
                    minLocation = min(mapped)
                break

            lineEndIndex = getNextLineEnd(content[lineNumber + 1:])
            mapped = mapValues(content[lineNumber + 1:lineNumber + lineEndIndex + 1], mapped)
            continue


    print("Locations: ", minLocation)


if __name__ == "__main__":
    problem1()
    print("\n")
    #problem2()

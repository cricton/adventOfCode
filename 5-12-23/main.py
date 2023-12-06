import sys
import numpy as np
import time


def mapValues(content, values):
    lines = []
    for line in content:
        toAppend = line.split("\n")[0].split(" ")
        if len(toAppend) == 1:
            break
        lines.append(toAppend)

    for valueIndex, value in enumerate(values):
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

    startTime = time.perf_counter()
    seedsToPlant = content[0].split("\n")[0].split(" ")[1:]

    mapped = []
    for seed in seedsToPlant:
        mapped.append(np.array([seed]))

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

    print("Took:", time.perf_counter() - startTime, "ms")


def splitSet(valueStart, valueRange, index):
    if len(index) == 1:
        return [(valueStart, index[0]),(valueStart + index[0],valueRange - index[0])]

    returnSet = [(valueStart, index[0]),
                 (valueStart + index[0],index[1]-index[0]),
                 (valueStart + index[1],valueRange - index[1])]
    return returnSet

def mapValues_new(content, valueSet):
    lines = []
    for line in content:
        toAppend = line.split("\n")[0].split(" ")
        if len(toAppend) == 1:
            break
        lines.append(toAppend)

    returnSet = []
    #print("Values to check: ", valueSet)
    for values in valueSet:
        valueStart = int(values[0])
        valueRange = int(values[1])
        maxValue = valueStart + valueRange - 1

        edited = False
        split = ()
        for line in lines:
            #print("Checking new line")


            sourceStart = int(line[1])
            destinationStart = int(line[0])
            mapLength = int(line[2])-1

            offset = destinationStart - sourceStart

            # 5 cases
            # case 1: the two sets do not overlap at all
            if maxValue < sourceStart or valueStart > sourceStart + mapLength:
                continue

            # case 2: source with mapLength covers entire value Range
            if sourceStart <= valueStart and sourceStart + mapLength >= maxValue:
                returnSet.append((valueStart + offset, valueRange))
                edited = True
                break

            # case 3 the two sets overlap, the values are lower than the source but enter from the left
            if valueStart < sourceStart <= maxValue and maxValue <= sourceStart + mapLength:

                index = sourceStart - valueStart
                split = splitSet(valueStart, valueRange, [index])
                break

            # case 4 the two sets overlap, the values are inside the source but exit from the right
            if valueStart >= sourceStart and valueStart < sourceStart + mapLength and maxValue > sourceStart + mapLength:

                index = sourceStart + mapLength - valueStart + 1
                split = splitSet(valueStart, valueRange, [index])
                break

            # case 5 the value set covers the entire source range
            if valueStart < sourceStart and maxValue > sourceStart + mapLength:

                lowerIndex = sourceStart - valueStart
                upperIndex = sourceStart + mapLength - valueStart + 1
                split = splitSet(valueStart, valueRange, (lowerIndex,upperIndex))
                break

        if len(split) > 0:
            editedSet = mapValues_new(content, split)
            for set in editedSet:
                returnSet.append(set)

        elif not edited:
            returnSet.append((valueStart, valueRange))

    return returnSet


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def getNextLineEnd(content):
    for lineNumber, line in enumerate(content):
        if line == "\n":
            return lineNumber


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = time.perf_counter()

    seedsToPlant = content[0].split("\n")[0].split(" ")[1:]
    startingPoints = seedsToPlant[0::2]
    ranges = seedsToPlant[1::2]

    startRangePairs = []
    for i in range(len(startingPoints)):
        startRangePairs.append((startingPoints[i], ranges[i]))

    minLocation = sys.maxsize


    for lineNumber, line in enumerate(content):
        if has_numbers(line) or line == "\n":
            continue
        elif line == "humidity-to-location map:\n":
            # print("Mapping to location")
            startRangePairs = mapValues_new(content[lineNumber + 1:], startRangePairs)
            for location in startRangePairs:
                if location[0] < minLocation:
                    minLocation = location[0]
            break

        else:
            lineEndIndex = getNextLineEnd(content[lineNumber + 1:])
            startRangePairs = mapValues_new(content[lineNumber + 1:lineNumber + lineEndIndex + 1], startRangePairs)

            continue

    print("Locations: ", minLocation)
    print("Took:", time.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    #problem1()
    print("\n")
    problem2()

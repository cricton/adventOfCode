import sys
import numpy
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


def mapValues_new(content, values):
    lines = []
    for line in content:
        toAppend = line.split("\n")[0].split(" ")
        if len(toAppend) == 1:
            break
        lines.append(toAppend)


    valueSet = [values]
    for line in lines:

        for set in valueSet:
            valueStartIndex = 0
            valueStart = int(set[0])
            valueRange = len(set)

            sourceStart = int(line[1])
            destinationStart = int(line[0])
            mapLength = int(line[2])

            offset = destinationStart - sourceStart
            # 4 cases
            # case 1: the two sets do not overlap at all
            if valueStart + valueRange < sourceStart or valueStart > sourceStart + mapLength:
                continue

            # case 2: source with mapLength covers entire value Range
            if sourceStart <= valueStart and sourceStart + mapLength >= valueStart + valueRange:
                values[valueStartIndex:valueRange] += offset
                break

            # case 3 the two sets overlap, the values are lower than the source but enter from the left
            if valueStart < sourceStart <= valueStart + valueRange and valueStart + valueRange <= sourceStart + mapLength:
                for index, value in enumerate(values):
                    if value == sourceStart:
                        values[index:valueRange] += offset
                        valueRange = index
                        break

            # case 4 the two sets overlap, the values are inside the source but exit from the right
            if valueStart >= sourceStart and valueStart <= sourceStart + mapLength and valueStart + valueRange > sourceStart + mapLength:
                for index, value in enumerate(values):
                    if value == sourceStart + mapLength:
                        values[valueStartIndex:index] += offset
                        valueStartIndex = index
                        break

            # case 5 the value set covers the entire source range
            if valueStart < sourceStart and valueStart + valueRange > sourceStart + mapLength:
                lowerIndex = 0
                for index, value in enumerate(values):
                    if value == sourceStart:
                        lowerIndex = index
                    if value == sourceStart + mapLength:
                        values[lowerIndex:upperIndex] += offset

    return values


def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = time.perf_counter()
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

    print("Took:", time.perf_counter() - startTime, "ms")


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

    # print(startingPoints)
    # print(ranges)
    # completeRange = 0
    # for num in ranges:
    #    completeRange += int(num)
    # print(completeRange)

    minLocation = sys.maxsize
    for index, startingPoint in enumerate(startingPoints):
        mapped = numpy.arange(int(startingPoint), int(ranges[index]) + int(startingPoint), 1, dtype=numpy.int64)

        print("Checking", index + 1, "starting point")

        for lineNumber, line in enumerate(content):
            if has_numbers(line) or line == "\n":
                continue
            elif line == "humidity-to-location map:\n":
                # print("Mapping to location")
                mapped = mapValues_new(content[lineNumber + 1:], mapped)
                if min(mapped) < minLocation:
                    minLocation = min(mapped)
                break

            else:
                lineEndIndex = getNextLineEnd(content[lineNumber + 1:])
                mapped = mapValues_new(content[lineNumber + 1:lineNumber + lineEndIndex + 1], mapped)
                continue

    print("Locations: ", minLocation)
    print("Took:", time.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    #problem1()
    print("\n")
    #problem2()

import math
import sys
from copy import copy, deepcopy
import numpy
import numpy as np
import time as t


def expandSpace(spaceMap):
    for index, line in enumerate(spaceMap):
        spaceMap[index] = list(line.rstrip('\n'))

    returnMap = deepcopy(spaceMap)

    height = len(spaceMap)
    width = len(spaceMap[0])
    inserted = 0
    for y in range(width):
        containsGalaxy = False
        for x in range(height):
            if spaceMap[x][y] == '#':
                containsGalaxy = True
                break
        if not containsGalaxy:
            for x in range(height):
                returnMap[x].insert(y + inserted, '.')
            inserted += 1

    inserted = 0
    for index, line in enumerate(returnMap.copy()):
        if line.count('.') == len(returnMap[0]):
            returnMap.insert(index + inserted, ['.'] * len(returnMap[0]))
            inserted += 1

    return returnMap


def countGalaxies(inputMap):
    galaxiesFound = 0
    for x in range(len(inputMap)):
        for y in range(len(inputMap[0])):
            if inputMap[x][y] == '#':
                # inputMap[x][y] = str(galaxiesFound)
                galaxiesFound += 1
    return inputMap, galaxiesFound


def getGalaxyCoordinates(inputMap):
    galaxyCoordinates = []

    for x, line in enumerate(inputMap):
        if ''.join(line).count('.') < len(inputMap[0]):
            for y, char in enumerate(line):
                if char != '.' and char != 'O':
                    galaxyCoordinates.append((x, y))

    return galaxyCoordinates


def getDistance(pointA, pointB):
    distance = abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

    return distance


def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    image = expandSpace(content)

    image, amountOfGalaxies = countGalaxies(image)

    galaxyCoordinates = getGalaxyCoordinates(image)

    cumulativeDistance = 0
    for galaxyA in range(amountOfGalaxies):
        for galaxyB in range(galaxyA + 1, amountOfGalaxies):
            # print(galaxyA, galaxyB)
            cumulativeDistance += getDistance(galaxyCoordinates[galaxyA], galaxyCoordinates[galaxyB])

    print(cumulativeDistance)
    for line in image:
        print(''.join(line))

    print("Took:", t.perf_counter() - startTime, "ms")

def sign(num):
    return -1 if num < 0 else 1


def getBigDistance(pointA, pointB, spaceMap):
    distanceCoordinates = (pointB[0] - pointA[0],pointB[1] - pointA[1])

    distance = 0
    for x in range(0, distanceCoordinates[0]):
        symbol = spaceMap[pointA[0] + x][pointA[1]]
        if symbol == 'O':
            distance += 999999
        else:
            distance += 1
    for y in range(0, distanceCoordinates[1], sign(distanceCoordinates[1])):
        symbol = spaceMap[pointB[0]][pointB[1] - y]
        if symbol == 'O':
            distance += 999999
        else:
            distance += 1
    return distance


def expandBigSpace(spaceMap):
    for index, line in enumerate(spaceMap):
        spaceMap[index] = list(line.rstrip('\n'))

    returnMap = deepcopy(spaceMap)

    height = len(spaceMap)
    width = len(spaceMap[0])
    inserted = 0
    for y in range(width):
        containsGalaxy = False
        for x in range(height):
            if spaceMap[x][y] == '#':
                containsGalaxy = True
                break
        if not containsGalaxy:
            for x in range(height):
                returnMap[x].insert(y + inserted, 'O')
            inserted += 1

    inserted = 0
    for index, line in enumerate(spaceMap):
        if line.count('.') == len(spaceMap[0]):
            returnMap.insert(index + inserted, ['O'] * len(returnMap[0]))
            inserted += 1

    return returnMap


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    image = expandBigSpace(content)

    image, amountOfGalaxies = countGalaxies(image)

    galaxyCoordinates = getGalaxyCoordinates(image)

    cumulativeDistance = 0
    for galaxyA in range(amountOfGalaxies):
        for galaxyB in range(galaxyA + 1, amountOfGalaxies):
            cumulativeDistance += getBigDistance(galaxyCoordinates[galaxyA], galaxyCoordinates[galaxyB], image)

    print(cumulativeDistance)
    for line in image:
        print(''.join(line))

    print("Took:", t.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    problem1()
    print("\n")
    problem2()

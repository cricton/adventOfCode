import math
import sys
import numpy as np
import time as t


def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    instructionString = content[0]

    instructions = ''
    for index, rl in enumerate(instructionString):
        if rl == 'L':
            instructions += '0'
        elif rl == 'R':
            instructions += '1'

    mapDict = {}
    for i in range(2, len(content)):
        key = content[i].split(' ')[0]
        valueL = content[i].split('(')[1].split(',')[0]
        valueR = content[i].split(' ')[3].split(')')[0]
        mapDict[key] = (valueL, valueR)

    currentLocation = 'AAA'
    steps = 0
    while currentLocation != 'ZZZ':
        instructionStep = steps % len(instructions)
        currentLocation = mapDict[currentLocation][int(instructions[instructionStep])]
        steps += 1

    print("Needed", steps, "steps.")
    print("Took:", t.perf_counter() - startTime, "ms")


def findSmallestMultiple(steps):
    return np.lcm.reduce(steps, dtype=np.int64)


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    instructionString = content[0]

    instructions = ''
    for index, rl in enumerate(instructionString):
        if rl == 'L':
            instructions += '0'
        elif rl == 'R':
            instructions += '1'

    mapDict = {}
    for i in range(2, len(content)):
        key = content[i].split(' ')[0]
        valueL = content[i].split('(')[1].split(',')[0]
        valueR = content[i].split(' ')[3].split(')')[0]
        mapDict[key] = (valueL, valueR)

    startLocations = []
    for index, key in enumerate(mapDict):
        if key[2] == 'A':
            startLocations.append(key)

    steps = [0] * len(startLocations)

    for index, startLocation in enumerate(startLocations):
        currentLocation = startLocation
        while currentLocation[2] != 'Z':
            instructionStep = steps[index] % len(instructions)
            currentLocation = mapDict[currentLocation][int(instructions[instructionStep])]
            steps[index] += 1

    print(steps)
    totalSteps = findSmallestMultiple(steps)
    print("Needed", totalSteps, "steps.")

    print("Took:", t.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    problem1()
    print("\n")
    problem2()

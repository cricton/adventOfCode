import math
import sys
import numpy as np
import time as t


def getRecord(timeToCharge, time):
    return timeToCharge*(time-timeToCharge)

# We can do this as num/2 * num/2 will always satisfy the condition to win the race
def lowerBoundBS(stepSize, lastChecked, time, record):
    if(getRecord(lastChecked, time) <= record):
        step = lastChecked + stepSize
    else:
        step = lastChecked - stepSize

    if getRecord(step, time) > record and (getRecord(step - 1, time) <= record or step == 1):
        return step

    if getRecord(step, time) <= record and getRecord(step + 1, time) > record:
        return step + 1

    if getRecord(step, time) > record:
        stepSize = math.ceil(stepSize/2)
        lastChecked = step
        return lowerBoundBS(stepSize, lastChecked, time, record)

    if getRecord(step, time) <= record:
        stepSize = math.ceil(stepSize / 2)
        lastChecked = step
        return lowerBoundBS(stepSize, lastChecked, time, record)

    return step


def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    races = []

    times = list(filter(None,content[0].split(":")[1].split("\n")[0].split(" ")))
    records = list(filter(None,content[1].split(":")[1].split("\n")[0].split(" ")))

    if len(times) != len(records):
        return

    for i in range(len(times)):
        races.append((times[i],records[i]))

    mult = 1
    waysToWin = []
    for race in races:
        time = int(race[0])
        record = int(race[1])
        # Get lower bound first
        stepSize = math.ceil(time/2)

        lowerBound = lowerBoundBS(stepSize, time - stepSize, time, record)

        # lower and upper bound mirror each other
        upperbound = time - lowerBound
        waysToWin.append(upperbound-lowerBound+1)

    for i in waysToWin:
        mult *= i

    print("Margin of error: ", mult)

    print("Took:", t.perf_counter() - startTime, "ms")


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    races = []

    times = content[0].split(":")[1].split("\n")[0].replace(" ", "")
    records = content[1].split(":")[1].split("\n")[0].replace(" ", "")


    races.append((times,records))

    mult = 1
    waysToWin = []
    for race in races:
        time = int(race[0])
        record = int(race[1])
        # Get lower bound first
        stepSize = math.ceil(time/2)

        lowerBound = lowerBoundBS(stepSize, time - stepSize, time, record)

        # lower and upper bound mirror each other
        upperbound = time - lowerBound
        waysToWin.append(upperbound-lowerBound+1)

    for i in waysToWin:
        mult *= i

    print("Margin of error: ", mult)

    print("Took:", t.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    problem1()
    print("\n")
    problem2()

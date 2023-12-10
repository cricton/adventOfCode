import math
import sys
import numpy as np
import time as t


def isUniform(list):
    if len(list) == 0:
        return False
    if max(list) == min(list):
        return True
    return False


def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    histories = []
    for line in content:
        histories.append(list(map(int, line.split('\n')[0].split(' '))))

    totalValues = 0
    for history in histories:
        history = [history]
        nextValue = history[0][-1]
        while not isUniform(history[-1]):
            difference = []
            for i in range(1, len(history[-1])):
                difference.append(history[-1][i] - history[-1][i - 1])

            nextValue += difference[-1]
            history.append(difference)
        totalValues += nextValue

    print(totalValues)
    print("Took:", t.perf_counter() - startTime, "ms")


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    histories = []
    for line in content:
        histories.append(list(map(int, line.split('\n')[0].split(' '))))

    totalValues = 0
    for history in histories:
        history = [history]
        nextValue = history[0][0]
        while not isUniform(history[-1]):
            difference = []
            for i in range(1, len(history[-1])):
                difference.append(history[-1][i] - history[-1][i - 1])
            if len(history) % 2 == 1:
                nextValue -= difference[0]
            else:
                nextValue += difference[0]
            history.append(difference)
        totalValues += nextValue

    print(totalValues)

    startTime = t.perf_counter()

    print("Took:", t.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    problem1()
    print("\n")
    problem2()

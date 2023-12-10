import math
import sys
import numpy as np
import time as t

topEntered = {'|': (1, 0), 'L': (0, 1), 'J': (0, -1)}
leftEntered = {'-': (0, 1), '7': (1, 0), 'J': (-1, 0)}
rightEntered = {'-': (0, -1), 'L': (-1, 0), 'F': (1, 0)}
bottomEntered = {'|': (-1, 0), '7': (0, -1), 'F': (0, 1)}


def makeStep(lastPos, currentPos, piece):
    newPos = (0, 0)

    if lastPos[0] > currentPos[0]:
        newPos = (currentPos[0] + bottomEntered[piece][0], currentPos[1] + bottomEntered[piece][1])
    elif lastPos[0] < currentPos[0]:
        newPos = (currentPos[0] + topEntered[piece][0], currentPos[1] + topEntered[piece][1])
    elif lastPos[1] > currentPos[1]:
        newPos = (currentPos[0] + rightEntered[piece][0], currentPos[1] + rightEntered[piece][1])
    elif lastPos[1] < currentPos[1]:
        newPos = (currentPos[0] + leftEntered[piece][0], currentPos[1] + leftEntered[piece][1])
    return newPos


def canConnect(lastPos, currentPos, piece):
    connPossible = False

    if lastPos[0] > currentPos[0]:
        if piece in bottomEntered:
            connPossible = True
    elif lastPos[0] < currentPos[0]:
        if piece in topEntered:
            connPossible = True
    elif lastPos[1] > currentPos[1]:
        if piece in rightEntered:
            connPossible = True
    elif lastPos[1] < currentPos[1]:
        if piece in leftEntered:
            connPossible = True

    return connPossible


def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    maze = content

    startPos = (0, 0)
    for lineNumber, line in enumerate(maze):
        if 'S' in line:
            startPos = lineNumber, line.find('S')
            break
    # print(startPos)

    # Get pipes connected to S
    pipes = []
    for i in range(-1, 2, 2):
        if maze[startPos[0] + i][startPos[1]] != '.' and startPos[0] + i >= 0:
            currentPos = (startPos[0] + i, startPos[1])
            if canConnect(startPos, currentPos, maze[startPos[0] + i][startPos[1]]):
                pipes.append((startPos[0] + i, startPos[1]))

        if maze[startPos[0]][startPos[1] + i] != '.' and startPos[1] + i >= 0:
            currentPos = (startPos[0], startPos[1] + i)
            if canConnect(startPos, currentPos, maze[startPos[0]][startPos[1] + i]):
                pipes.append((startPos[0], startPos[1] + i))

    distance = [1, 1]
    lastPos = [startPos, startPos]
    while not pipes[0] == pipes[1]:
        for index, pipe in enumerate(pipes):
            piece = maze[pipe[0]][pipe[1]]
            newPos = makeStep(lastPos[index], pipe, piece)

            lastPos[index] = pipe
            pipes[index] = newPos
            distance[index] += 1

    print(max(distance))
    print("Took:", t.perf_counter() - startTime, "ms")


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    print("Took:", t.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    problem1()
    print("\n")
    # problem2()

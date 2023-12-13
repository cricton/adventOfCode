import math
import sys
import numpy as np
import time as t

topEntered = {'|': (1, 0), 'L': (0, 1), 'J': (0, -1)}
leftEntered = {'-': (0, 1), '7': (1, 0), 'J': (-1, 0)}
rightEntered = {'-': (0, -1), 'L': (-1, 0), 'F': (1, 0)}
bottomEntered = {'|': (-1, 0), '7': (0, -1), 'F': (0, 1)}


def makeStep(lastPos, currentPos, piece):
    """Performs a step along the pipe

        Parameters
        ----------
        lastPos : index tuple
            A tuple containing the index of the last position in the pipe.

        currentPos : index tuple
            A tuple containing the index of the current position in the pipe.

        piece : char
            The piece at the current position.

        Returns
        ----------
        newPos : index tuple
            A tuple containing the index of the next position along the pipe.
    """
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
    """Checks if the positions described in lastPos and currentPos can connect
        if the piece is the piece at the current position.

        Parameters
        ----------
        lastPos : index tuple
            A tuple containing the index of the last position in the pipe.

        currentPos : index tuple
            A tuple containing the index of the current position in the pipe.

        piece : char
            The piece at the current position.

        Returns
        ----------
        connPossible : bool
            Returns true if the connection is possible, false if not.
    """
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


UP = '0'
LEFT = '1'
RIGHT = '2'
DOWN = '3'


def replaceStartSymbol(startPos, toSanitize):
    """Figures out what symbol can replace the start symbol S

        Parameters
        ----------
        startPos : index tuple
            A tuple containing the index of the start position in the pipe.

        toSanitize : 2D Array
            Contains a 2-dimensional array containing the un-sanitized pipe network

        Returns
        ----------
        replacementSymbol : char
            Returns a symbol that can replace the starting symbol
    """
    connections = ""
    upperSymbol = toSanitize[max(startPos[0] - 1, 0)][startPos[1]]
    if upperSymbol == '|' or upperSymbol == '7' or upperSymbol == 'F':
        connections += UP
    leftSymbol = toSanitize[startPos[0]][max(startPos[1] - 1, 0)]
    if leftSymbol == '-' or leftSymbol == 'F' or leftSymbol == 'L':
        connections += LEFT
    rightSymbol = toSanitize[startPos[0]][min(startPos[1] + 1, len(toSanitize[0]))]
    if rightSymbol == '-' or rightSymbol == '7' or rightSymbol == 'J':
        connections += RIGHT
    downSymbol = toSanitize[min(startPos[0] + 1, len(toSanitize))][startPos[1]]
    if downSymbol == '|' or downSymbol == 'L' or downSymbol == 'J':
        connections += DOWN

    replacementSymbol = 'S'
    if UP in connections and RIGHT in connections:
        replacementSymbol = 'L'
    if UP in connections and LEFT in connections:
        replacementSymbol = 'J'
    if DOWN in connections and RIGHT in connections:
        replacementSymbol = 'F'
    if DOWN in connections and LEFT in connections:
        replacementSymbol = '7'
    return replacementSymbol


def sanitizeMap(toSanitize):
    """Removes all parts of the map that are not part of the main pipe loop and replaces them with '.'

        Parameters
        ----------
        toSanitize : 2D Array
            Contains a 2-dimensional array containing the un-sanitized pipe network

        Returns
        ----------
        sanitizedMap : 2D Array
            Returns a sanitized map. The starting symbol has been replaced by a regular pipe part,
            all pipe parts that are not part of the main pipe loop have been replaced by '.'
    """
    for index, line in enumerate(toSanitize):
        toSanitize[index] = line.rstrip('\n')

    sanitizedMap = []
    for i in range(len(toSanitize)):
        sanitizedMap.append(list(['.'] * len(toSanitize[0])))

    startPos = (0, 0)
    for lineNumber, line in enumerate(toSanitize):
        if 'S' in line:
            startPos = lineNumber, line.find('S')

            symbol = replaceStartSymbol(startPos, toSanitize)

            sanitizedMap[startPos[0]][startPos[1]] = symbol
            break

    # Get pipes connected to S
    pipes = []
    for i in range(-1, 2, 2):
        if toSanitize[startPos[0] + i][startPos[1]] != '.' and startPos[0] + i >= 0:
            currentPos = (startPos[0] + i, startPos[1])
            if canConnect(startPos, currentPos, toSanitize[startPos[0] + i][startPos[1]]):
                pipes.append((startPos[0] + i, startPos[1]))
                sanitizedMap[startPos[0] + i][startPos[1]] = toSanitize[startPos[0] + i][startPos[1]]

        if toSanitize[startPos[0]][startPos[1] + i] != '.' and startPos[1] + i >= 0:
            currentPos = (startPos[0], startPos[1] + i)
            if canConnect(startPos, currentPos, toSanitize[startPos[0]][startPos[1] + i]):
                pipes.append((startPos[0], startPos[1] + i))
                sanitizedMap[startPos[0]][startPos[1] + i] = toSanitize[startPos[0]][startPos[1] + i]

    lastPos = [startPos, startPos]
    while not pipes[0] == pipes[1]:
        for index, pipe in enumerate(pipes):
            piece = toSanitize[pipe[0]][pipe[1]]
            newPos = makeStep(lastPos[index], pipe, piece)

            sanitizedMap[newPos[0]][newPos[1]] = toSanitize[newPos[0]][newPos[1]]

            lastPos[index] = pipe
            pipes[index] = newPos

    return sanitizedMap


def expandable(symbol):
    """Checks if a symbol can be expanded.

        Parameters
        ----------
        symbol : char
            The symbol to check.

        Returns
        ----------
        bool
            Returns true if the symbol can be expanded and false if not.
    """
    if symbol == '.' or symbol == 't':
        return True
    return False


expandDirection = {'7': (0, 1), 'F': (0, -1), 'L': (0, -1), 'J': (0, 1)}

CW = 0
CCW = 1

rotate = {'7': (CCW, CW),
          'F': (CW, CCW),
          'L': (CCW, CW),
          'J': (CW, CCW)}

rotateCW = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
rotateCCW = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}


def rotateOffset(offset, direction):
    """Rotates the input offset clockwise or counterclockwise depending on the given direction..

        Parameters
        ----------
        offset : tuple
            Offset tuple, can either be (-1,0), (0,1), (1, 0) or (0, -1)

        direction : CW|CCW
            Direction is either CW for clockwise or CCW for counterclockwise
        Returns
        ----------
        offset : tuple
            Returns the rotated offset.
    """
    if direction == CW:
        offset = rotateCW[offset]
    elif direction == CCW:
        offset = rotateCCW[offset]
    return offset



def expandPipe(coordinates, pipeMap):

    symbol = pipeMap[coordinates[0]][coordinates[1]]

    expandTowards = expandDirection[symbol]

    coordsToCheck = (coordinates[0] + expandTowards[0], coordinates[1] + expandTowards[1])
    if pipeMap[coordsToCheck[0]][coordsToCheck[1]] == '.':
        pipeMap[coordsToCheck[0]][coordsToCheck[1]] = 't'

    if pipeMap[coordinates[0]][coordinates[1]] == '7' or pipeMap[coordinates[0]][coordinates[1]]:
        lastCoords = (coordinates[0] - 1, coordinates[1])
    else:
        lastCoords = (coordinates[0] + 1, coordinates[1])

    currentCoords = coordinates

    temp = makeStep(lastCoords, currentCoords, '|')
    lastCoords = currentCoords
    currentCoords = temp

    while currentCoords != coordinates:

        symbol = pipeMap[currentCoords[0]][currentCoords[1]]
        if symbol in expandDirection:

            coordsToCheck = (currentCoords[0] + expandTowards[0], currentCoords[1] + expandTowards[1])
            coordsToCheck = (max(coordsToCheck[0], 0), max(coordsToCheck[1], 0))
            coordsToCheck = (min(coordsToCheck[0], len(pipeMap) - 1), min(coordsToCheck[1], len(pipeMap[0]) - 1))
            if pipeMap[coordsToCheck[0]][coordsToCheck[1]] == '.':
                pipeMap[coordsToCheck[0]][coordsToCheck[1]] = 't'

            if lastCoords[0] != currentCoords[0]:
                expandTowards = rotateOffset(expandTowards, rotate[symbol][0])
            elif lastCoords[1] != currentCoords[1]:
                expandTowards = rotateOffset(expandTowards, rotate[symbol][1])

        coordsToCheck = (currentCoords[0] + expandTowards[0], currentCoords[1] + expandTowards[1])
        coordsToCheck = (max(coordsToCheck[0], 0), max(coordsToCheck[1], 0))
        coordsToCheck = (min(coordsToCheck[0], len(pipeMap) - 1), min(coordsToCheck[1], len(pipeMap[0]) - 1))
        if pipeMap[coordsToCheck[0]][coordsToCheck[1]] == '.':
            pipeMap[coordsToCheck[0]][coordsToCheck[1]] = 't'

        temp = makeStep(lastCoords, currentCoords, symbol)
        lastCoords = currentCoords
        currentCoords = temp

    return pipeMap


def expandPoint(coordinates, pipeMap):
    upCoord = (max(coordinates[0] - 1, 0), coordinates[1])
    if pipeMap[upCoord[0]][upCoord[1]] == '.':
        pipeMap[upCoord[0]][upCoord[1]] = 't'

    downCoord = (min(coordinates[0] + 1, len(pipeMap) - 1), coordinates[1])
    if pipeMap[downCoord[0]][downCoord[1]] == '.':
        pipeMap[downCoord[0]][downCoord[1]] = 't'

    righCoord = (coordinates[0], min(coordinates[1] + 1, len(pipeMap[0]) - 1))
    if pipeMap[righCoord[0]][righCoord[1]] == '.':
        pipeMap[righCoord[0]][righCoord[1]] = 't'

    leftCoord = (coordinates[0], max(coordinates[1] - 1, 0))
    if pipeMap[leftCoord[0]][leftCoord[1]] == '.':
        pipeMap[leftCoord[0]][leftCoord[1]] = 't'

    return pipeMap


def containsExpandable(maze):
    for line in maze:
        for char in line:
            if char == 't':
                return True
    return False


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    maze = sanitizeMap(content)

    checkedInnerArea = False
    for x in range(len(maze)):
        if checkedInnerArea:
            break
        for y in range(len(maze[x])):
            if maze[x][y] == 'F':
                maze = expandPipe((x, y), maze)
                checkedInnerArea = True
                break

    for index, expansionPoint in enumerate(maze[0]):
        if expandable(expansionPoint):
            maze[0][index] = 'O'
            coordinates = (0, index)
            expandPoint(coordinates, maze)

    for index, expansionPoint in enumerate(maze[-1]):
        if expandable(expansionPoint):
            maze[-1][index] = 'O'
            coordinates = (len(maze) - 1, index)
            expandPoint(coordinates, maze)

    while containsExpandable(maze):
        for x, line in enumerate(maze):
            for y, expansionPoint in enumerate(line):
                if expansionPoint == 't':
                    maze[x][y] = 'O'
                    coordinates = (x, y)
                    expandPoint(coordinates, maze)

    count = 0
    for line in maze:
        line = ''.join(line)
        print(''.join(line))

        count += line.count('.')

    print(count)
    print("Took:", t.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    # problem1()
    print("\n")
    problem2()

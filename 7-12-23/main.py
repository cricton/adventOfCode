import math
import sys
import numpy as np
import time as t


def getGameRank(cards):
    rank = 0
    for card in cards:
        if cards.count(card) == 5:
            rank = 6
            return rank
        if cards.count(card) == 4:
            rank = 5
            return rank
        if cards.count(card) == 3:
            rank += 3
            cards = cards.replace(card, '')
        if cards.count(card) == 2:
            rank += 1
            cards = cards.replace(card, '')
    return rank


valueDict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def compareGames(game1, game2):
    if game1[0] == game2[0]:
        return 0
    for i in range(len(game1[0])):
        # If cards are equal, check next set
        if compareCards(game1[0][i], game2[0][i]) == -1:
            continue
        return compareCards(game1[0][i], game2[0][i])


def compareCards(card1, card2):
    if not card1.isdigit():
        card1 = valueDict.get(card1)
    if not card2.isdigit():
        card2 = valueDict.get(card2)

    if int(card1) > int(card2):
        return 1
    if int(card1) < int(card2):
        return 0
    return -1


def problem1():
    print("Problem 1: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    games = []

    for line in content:
        hand = line.split("\n")[0].split(" ")[0]
        bid = int(line.split("\n")[0].split(" ")[1])
        games.append((hand, bid))

    sortedGames = [[], [], [], [], [], [], []]
    for game in games:
        sortedGames[getGameRank(game[0])].append(game)

    result = 0
    rank = 1
    for games in sortedGames:
        if len(games) == 0:
            continue

        while len(games) > 0:
            lowestGame = games[0]
            for game in games:
                if compareGames(lowestGame, game):
                    lowestGame = game
            games.remove(lowestGame)
            result += rank * lowestGame[1]
            rank += 1

    print(result, rank)
    print("Took:", t.perf_counter() - startTime, "ms")


pairValueDict = {5: 6, 4: 5, 3: 3, 2: 1, 1: 0}


def getGameRankWithJokers(cards):
    jokers = cards.count('J')
    if jokers == 5:
        return 6

    rank = 0
    cards = cards.replace('J', '')
    cardAmounts = []
    for card in cards:
        if cards.count(card) > 0:
            cardAmounts.append(cards.count(card))
            cards = cards.replace(card, '')

    maxCard = 0
    maxIndex = 0
    for cardIndex, card in enumerate(cardAmounts):
        if card > maxCard:
            maxCard = card
            maxIndex = cardIndex

    cardAmounts[maxIndex] += jokers

    for amount in cardAmounts:
        rank += pairValueDict[amount]

    return rank



valueDictWithJokers = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}


def compareGamesWithJokers(game1, game2):
    if game1[0] == game2[0]:
        return 0
    for i in range(len(game1[0])):
        # If cards are equal, check next set
        if compareCardsWithJokers(game1[0][i], game2[0][i]) == -1:
            continue
        return compareCardsWithJokers(game1[0][i], game2[0][i])


def compareCardsWithJokers(card1, card2):
    if not card1.isdigit():
        card1 = valueDictWithJokers.get(card1)
    if not card2.isdigit():
        card2 = valueDictWithJokers.get(card2)

    if int(card1) > int(card2):
        return 1
    if int(card1) < int(card2):
        return 0
    return -1


def problem2():
    print("Problem 2: ")
    input = open("input.txt")
    content = input.readlines()

    startTime = t.perf_counter()

    games = []

    for line in content:
        hand = line.split("\n")[0].split(" ")[0]
        bid = int(line.split("\n")[0].split(" ")[1])
        games.append((hand, bid))

    sortedGames = [[], [], [], [], [], [], []]
    for game in games:
        sortedGames[getGameRankWithJokers(game[0])].append(game)

    result = 0
    rank = 1
    for games in sortedGames:
        if len(games) == 0:
            continue

        while len(games) > 0:
            lowestGame = games[0]

            for game in games:
                if game[0] == 'Q7289':
                    pass
                if compareGamesWithJokers(lowestGame, game):


                    lowestGame = game
            games.remove(lowestGame)
            result += rank * lowestGame[1]
            rank += 1

    print(result)
    print("Took:", t.perf_counter() - startTime, "ms")


if __name__ == "__main__":
    problem1()
    print("\n")
    problem2()

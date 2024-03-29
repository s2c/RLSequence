from DeckOfCards import Deck
from Board import Board
from Player import Player
import random


class SequenceGame(object):
    """docstring for SequenceGame"""

    def __init__(self, numPlayers=2, handSize=6):
        super(SequenceGame, self).__init__()
        self.handsize = handSize
        if numPlayers > 2:  # Currently only supports 2 players
            numPlayers = 2  # Currently only supports 2 players
        self.numPlayers = numPlayers  # Currently only supports 2 players
        self.curState = 'PLAYING'
        self.curTurn = 0
        self.TotalTurns = 0
        self.board = Board()
        # 2 Decks in a standard game
        self.decks = [Deck().shuffle(), Deck().shuffle()]
        self.players = [Player() for x in range(0, self.numPlayers)]
        self.setupPlayers()  # setup player hands
        self.startGame()

    def givePlayerCard(self, player):
        curDeck = random.choice(self.decks)
        while (len(curDeck.cards) == 0):
            curDeck = random.choice(self.decks)
        self.players[player].draw(curDeck)

    def setupPlayers(self):
        for p in range(0, len(self.players)):
            for i in range(0, self.handsize):
                self.givePlayerCard(p)

    def showStatus(self, cardToggle=False):
        print('Player ' + str(self.curTurn + 1) + ' Turn')
        if cardToggle == True:
            print("Board State Below")
            print("_____________________________________________________")
            curBoard = self.board.show()
            for row in curBoard:
                print(row)
        print("Token State Below")
        print("_____________________________________________________")
        curTokens = self.board.tokens
        for row in curTokens:
            print(row)

    def startGame(self):
        print("2 Player Game Started")
        self.showStatus(True)

    def checkWin(self, pIndex, locX, locY):
        player = pIndex + 1
        for i in range(locY - 4, locY + 1):  # check Vertical
            curSum = 0
            for j in range(i, i + 5):
                if (i < 0 or i + 4 > self.board.columns - 1) and not(self.board.isCorner(j, locX)):
                    return -1  # out of bounds doesn't matter
                if (self.board.isCorner(j, locX)):
                    curSum += player
                else:
                    curSum += self.board.tokens[j][locX]
            if curSum / player == 5.0:  # player has won with vertical
                print('Player ' + str(player) + ' wins!')
                return 1

        for i in range(locX - 4, locX + 1):  # check Horizontal
            curSum = 0
            for j in range(i, i + 5.0):
                if (i < 0 or i + 4 > self.board.rows - 1) and not(self.board.isCorner(locX, j)):
                    return -1  # out of bounds doesn't matter
                if (self.board.isCorner(locY, j)):
                    curSum += player
                else:
                    curSum += self.board.tokens[locY][j]
            if curSum / player == 5:  # player has won with vertical
                print('Player ' + str(player) + ' wins!')
                return 1
        for t, i in enumerate(range(locX - 4, locX + 1)):
            curSum = 0
            for k, j in enumerate(range(i, i + 5)):  # Check Left Diagnol
                m = locY - (4 - k) + t
                if (j < 0 or j > self.board.rows - 1 or m < 0 or m > self.board.columns - 1) and not (self.board.isCorner(j, m)):
                    return -1
                if (self.board.isCorner(j, m)):
                    curSum += player
                else:
                    curSum += self.board.tokens[m][j]

            if curSum / player == 5.0:  # player has won with Left Diagnol
                print('Player ' + str(player) + ' wins!')
                return 1

    def nextState(self, pIndex, pCard, locX, locY):
        if self.curState == 'OVER':
            print('GAME IS OVER')
            print('RESET GAME TO PLAY AGAIN')
            return -1

        if pIndex != self.curTurn:
            print('It is currently not ' + str(pIndex + 1) + "'s Turn! ")
            print('It is player ' + str(self.curTurn) + "'s Turn")
            print('Game State not Advanced')
            return -1
        playerCard = self.players[pIndex].play(pCard)
        print("Player " + str(pIndex + 1) + " tries to play card " +
              str(playerCard.show()) + ' at (' + str(locX) + ',' + str(locY) + ')')
        if playerCard.show() not in self.board.removeCards:
            if self.board.placeToken(playerCard, pIndex, locX, locY) != 1:
                print('Game state not advanced')
                self.players[pIndex].returnCard(pCard, playerCard)
                return -1
        else:
            if self.board.removeToken(playerCard, locX, locY) != 1:
                print('Game state not advanced')
                self.players[pIndex].returnCard(pCard, playerCard)
                return -1

        print("Player played card succesfully")
        if (self.checkWin(pIndex, locX, locY) == 1):
            self.curState = 'OVER'
            return 1

        self.givePlayerCard(pIndex)
        self.TotalTurns += 1
        self.curTurn = (pIndex + 1) % self.numPlayers
        print('Token State')
        self.showStatus()

    def reset(self):
        del self.board
        del self.decks[:]
        del self.players[:]
        self.__init__(self.numPlayers, self.handsize)

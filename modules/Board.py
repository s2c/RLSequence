from Boards import defaultBoard


class Board(object):
    """docstring for Board"""

    def __init__(self, boardSize=10):
        super(Board, self).__init__()
        self.removeCards = [('Spades', 11), ('Hearts', 11)]
        self.jokerCards = [('Clubs', 11), ('Diamonds', 11)]
        self.rows = boardSize
        self.columns = boardSize
        self.board = []
        self.tokens = [[-1 for x in range(0, self.rows)]
                       for y in range(0, self.columns)]
        self.setBoard()

    def setBoard(self, listOfCards=None):
        if listOfCards != None:
            self.board = listOfCards  # listOfCards is 10x10 array containing Card objects
        else:  # BuildDefault Board
            self.board = defaultBoard

    def show(self):
        return [[x.show() for x in row] for row in self.board]

    def placeToken(self, card, player, x, y):
        if self.tokens[y][x] != -1 or self.isCorner(x, y):
            print('Spot already Taken or Corner Location. Token Not Placed')
            return -1
        elif self.board[y][x].show() == card.show() or card.show() in self.jokerCards:
            self.tokens[y][x] = player + 1
            print('Token Placed Succesfully')
            return 1
        else:
            print('Token Not Placed. Invalid Card')
            return -2

    def removeToken(self, card, x, y):
        if self.tokens[y][x] == -1 or (card.show() not in self.removeCards):
            print('Already empty or Invalid Card. Token Not Removed')
            return -1
        else:
            self.tokens[y][x] = -1
            print('Token Succesfully Removed')
            return 1

    def showTokens(self):
        return self.tokens

    def isCorner(self, locX, locY):
        if (locY == 0) and (locX == 0):
            return True
        elif (locY == self.columns - 1) and (locX == 0):
            return True
        elif (locY == self.columns - 1) and (locX == self.rows - 1):
            return True
        elif (locY == 0) and (locX == self.rows - 1):
            return True
        else:
            return False

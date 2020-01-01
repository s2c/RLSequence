from Boards import defaultBoard

class Board(object):
	"""docstring for Board"""
	def __init__(self, boardSize=10):
		super(Board, self).__init__()
		self.rows = boardSize
		self.columns = boardSize
		self.board = []
		self.tokens = [[-1]*self.rows]*self.columns
		self.setBoard()
		self.showBoard = self.showBoard()
	def setBoard(self,listOfCards = None):
		if listOfCards != None:
			self.board = listOfCards #listOfCards is 10x10 array containing Card objects
		else: # BuildDefault Board
			self.board = defaultBoard
	def showBoard(self):
		return [[x.show() for x in row] for row in self.board]
	def placeToken(self,card,player,x,y):
		if self.tokens[y][x] !=-1:
			print('Spot already Taken. Token Not Placed')
			return            
		if self.board[y][x].show() == card.show() or card.show()==('Diamonds',11) or card.show()==('Hearts',11):
			self.tokens[y][x] = player
			print('Token Placed Succesfully')
		else:
			print('Token Not Placed')
	def removeToken(self,card,x,y):
		if self.tokens[y][x] ==-1 or (card.show() != ('Spades',11) and card.show() !=('Clubs',11)):
			print('Already empty or Invalid Card. Token Not Removed')
			return            
		else:
			self.tokens[y][x]=-1            
			print('Token Succesfully Removed')
	def showTokens(self,):
		return self.tokens





            
            
        
from DeckOfCards import Deck
from Board import Board
from Player import Player
import random

class SequenceGame(object):
	"""docstring for SequenceGame"""
	def __init__(self, numPlayers=2):
		super(SequenceGame, self).__init__()
		self.handsize = 6
		self.numPlayers = 2
		self.curTurn = 1
		self.TotalTurns = 0
		self.board = Board()
		self.decks = [Deck().shuffle(),Deck().shuffle()] # 2 Decks in a standard game
		self.players = [Player() for x in range(0,2)]
		self.setupPlayers() # setup player hands
		self.startGame()
	def givePlayerCard(self,player):
		curDeck = random.choice(self.decks)
		while (len(curDeck.cards)==0):
			curDeck = random.choice(self.decks)
		player.draw(curDeck)
	def setupPlayers(self):        
		for p in self.players:         
			for i in range(0,self.handsize):             
				self.givePlayerCard(p)
	def showStatus(self):
		print('Player ' + str(self.curTurn) + ' Turn')
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
		self.showStatus()	
	def isCorner(self,locX,locY):
		if (locY==0) and (locX==0):
			return True
		elif (locY==9) and (locX==0):
			return True
		elif (locY==9) and (locX==9):
			return True
		elif (locY==0) and (locX==9):
			return True
		else:
			return False
	def checkWin(self,pIndex,locX,locY):
		player = pIndex + 1
		for i in range(locY-4,locY+1): # check Vertical
		    curSum = 0
		    for j in range(i,i+5):
		        if (i < 0 or i+5 >= 10) and not(g.isCorner(i,locX)):
		            break # out of bounds doesn't matter
		        curSum += g.board.tokens[locY][4]
		    if curSum/player == 5: # player has won with vertical
		    	print('Player ' + str(player) + 'wins')

		for i in range(locX-4,locX+1): # check Horizontal
		    curSum = 0
		    for j in range(i,i+5):
		        if (i < 0 or i+5 >= 10) and not(g.isCorner(locX,i)):
		            break # out of bounds doesn't matter
		        curSum += g.board.tokens[locY][locX]
		    if curSum/player == 5: # player has won with vertical
		    	print('Player ' + str(player) + 'wins')



	def nextState(self,pIndex,pCard,locX,locY):
		playerCard = self.players[pIndex].play(pCard)
		print("Player " + str(pIndex+1) + " tries to play card " + str(playerCard.show()) + ' at (' + str(locX) + ',' + str(locY) +')' )		
		if self.board.placeToken(playerCard) != 1:
			print('Game state not advanced')
			return -1
		print("Player played card succesfully" )
		self.checkWin(pIndex,locX,locY)
		self.givePlayerCard(pIndex)
		self.TotalTurns += 1
		self.curTurn = (pIndex + 1 ) % self.numPlayers


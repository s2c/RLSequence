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
	def nextState(self,pIndex,pCard,locX,locY):
		playerCard = self.players[pIndex].play(pCard)
		print("Player " + str(pIndex+1) + " tries to play card " + str(playerCard.show()) + ' at (' + str(locX) + ',' + str(locY) +')' )		
		if self.board.placeToken(playerCard) != 1:
			print('Game state not advanced')
		print("Player " + str(pIndex+1) + " Played card " + str(playerCard.show()) + ' at (' + str(locX) + ',' + str(locY) +')' )



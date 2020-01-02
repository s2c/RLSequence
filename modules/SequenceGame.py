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
	def setupPlayers(self):        
		for p in self.players:         
			for i in range(0,self.handsize):             
				curDeck = random.choice(self.decks)
				p.draw(curDeck)
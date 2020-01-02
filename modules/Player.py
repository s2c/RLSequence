from DeckOfCards import Card,Deck


class Player(object):
	"""docstring for Player"""
	def __init__(self,deck=None, handSize=6,setHand=False):
		super(Player, self).__init__()
		self.hand = []
		self.handSize = handSize
		if setHand is True:
			self.setHand(deck)        
	def setHand(self,deck):
		for i in range(0,self.handSize):
			self.draw(deck)
        
	def draw(self,deck):
		self.hand.append(deck.drawCard())
	def addCard(self,card):
		self.hand.append(card)

	def showHand(self):
		showDeck = [x.show() for x in self.hand]
		return showDeck

	def play(self,cardNumber):
		return (self.hand.pop(cardNumber))
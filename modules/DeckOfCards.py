import random


class Card(object):
    """Holds each individual Card"""

    def __init__(self, suit=None, rank=None):
        super(Card, self).__init__()
        self.suit = suit
        self.rank = rank

    def show(self):
        return(self.suit, self.rank)


class Deck(object):
    """Holds card objects"""

    def __init__(self, deckSize=52):
        super(Deck, self).__init__()
        self.cards = [Card] * deckSize
        self.build()

    def build(self):
        # Diamonds and Hearts = 2 Eyed
        suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        ranks = [x for x in range(1, 14)]
        for i, s in enumerate(suits):
            for j, r in enumerate(ranks):
                self.cards[i * 13 + j] = Card(s, r)

    def show(self):
        showDeck = [x.show() for x in self.cards]
        return showDeck

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def drawCard(self):
        return self.cards.pop()

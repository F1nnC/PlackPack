from .card import card
import random

class deck:
    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
            for value in range(1, 14):
                self.cards.append(card(suit, value, value))

    def riffle_shuffle(self):
        # Cut the deck about in half, but not perfectly
        cut = random.randint(20, 32)  # somewhere around half
        left = self.cards[:cut]
        right = self.cards[cut:]
        
        shuffled = []
        # Interleave left and right stacks
        while left or right:
            if left and (not right or random.random() > 0.5):
                shuffled.append(left.pop(0))
            if right and (not left or random.random() > 0.5):
                shuffled.append(right.pop(0))
        
        self.cards = shuffled

    def shuffle(self, n):
        for _ in range(n):
            self.riffle_shuffle()

    def printDeck(self):
        for c in self.cards:
            c.printCard()
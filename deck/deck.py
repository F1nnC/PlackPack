from .card import card
import random
from collections import deque

class deck:
    def __init__(self, decks):
        self.decks = decks
        self.cards = [
            card(suit, value, value)
            for _ in range(self.decks)
            for suit in range(1, 5)
            for value in range(1, 14)
        ]

    def riffle_shuffle(self):
        cut = random.randint(len(self.cards)//2 - 12, len(self.cards)//2 + 12)
        left = deque(self.cards[:cut])
        right = deque(self.cards[cut:])
        shuffled = []
        while left or right:
            if left and (not right or random.random() > 0.5):
                shuffled.append(left.popleft())
            if right and (not left or random.random() > 0.5):
                shuffled.append(right.popleft())
        self.cards = shuffled

    def shuffle(self, n=7):
        for _ in range(n):
            self.riffle_shuffle()

    def printDeck(self):
        for c in self.cards:
            c.printCard()

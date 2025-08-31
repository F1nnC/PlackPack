from deck.card import card
from deck.deck import deck

class blackjack:

    def __init__(self):
        self.deck = deck()
        self.player_hand = []
        self.dealer_hand = []
        self.deck.shuffle(20)
        
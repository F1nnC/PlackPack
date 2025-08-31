import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from deck.card import card
from deck.deck import deck

class blackjack:
    def __init__(self):
        input_decks = int(input("Enter number of decks to use (default 1): "))
        self.deck = deck(input_decks)
        self.player_hand = []
        self.dealer_hand = []
        self.player_chips_bet = 0
        self.player_chips = 100
        self.deck.shuffle(20)
        self.start_game()

    def start_game(self):
        self.player_bet()
        self.deal_initial()
        self.print_hands()
        self.player_turn()

    @staticmethod
    def print_cards_side_by_side(cards, reveal):
        # Get ASCII art for each card
        lines_per_card = [c.ascii() if reveal else c.back_ascii() for c in cards]

        # Print row by row
        for i in range(len(lines_per_card[0])):
            print("   ".join(card[i] for card in lines_per_card))

    def player_bet(self):
        while True:
            try:
                print(f"You have {self.player_chips} chips.")
                bet = int(input("Enter your bet amount: "))
                if 0 < bet <= self.player_chips:
                    self.player_chips_bet = bet
                    self.player_chips -= bet
                    break
                else:
                    print(f"Invalid bet. You have {self.player_chips} chips.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def print_hands(self, reveal_dealer=False):
        print("Dealer's hand:")
        if reveal_dealer:
            self.print_cards_side_by_side(self.dealer_hand, True)
            print(f"Value: {self.calculate_hand_value(self.dealer_hand)}")
        else:
            # Render first card face-up, second card face-down
            lines_per_card = [self.dealer_hand[0].ascii(), self.dealer_hand[1].back_ascii()]
            for i in range(len(lines_per_card[0])):
                print("   ".join(card[i] for card in lines_per_card))

        print("\nPlayer's hand:")
        self.print_cards_side_by_side(self.player_hand, True)
        print(f"Value: {self.calculate_hand_value(self.player_hand)}\n")
        print(f"Your bet: {self.player_chips_bet}")
        print(f"Your chips: {self.player_chips}\n")

    def calculate_hand_value(self, hand):
        value = sum(c.getCardValue() for c in hand)
        aces = sum(1 for c in hand if c.card == "A")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def deal_initial(self):
        for i in range(2):
            self.player_hand.append(self.deck.cards.pop())
            self.dealer_hand.append(self.deck.cards.pop())
    
    def player_turn(self):
        while True:
            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action == "h":
                os.system('clear' if os.name == 'posix' else 'cls')
                self.player_hand.append(self.deck.cards.pop())
                self.print_hands()
                if self.calculate_hand_value(self.player_hand) > 21:
                    print("Bust! You lose.")
                    return
            elif action == "s":
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

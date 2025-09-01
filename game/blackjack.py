import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from deck.card import card
from deck.deck import deck

class blackjack:

    logo = """
        $$$$$$$\  $$\                     $$\       $$$$$$$\                     $$\       
        $$  __$$\ $$ |                    $$ |      $$  __$$\                    $$ |      
        $$ |  $$ |$$ | $$$$$$\   $$$$$$$\ $$ |  $$\ $$ |  $$ |$$$$$$\   $$$$$$$\ $$ |  $$\ 
        $$$$$$$  |$$ | \____$$\ $$  _____|$$ | $$  |$$$$$$$  |\____$$\ $$  _____|$$ | $$  |
        $$  ____/ $$ | $$$$$$$ |$$ /      $$$$$$  / $$  ____/ $$$$$$$ |$$ /      $$$$$$  / 
        $$ |      $$ |$$  __$$ |$$ |      $$  _$$<  $$ |     $$  __$$ |$$ |      $$  _$$<  
        $$ |      $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ $$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
        \__|      \__| \_______| \_______|\__|  \__|\__|      \_______| \_______|\__|  \__|                                                                                                                                      
    """

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
        while True:
            if self.intro():
                self.player_bet()
                self.deal_initial()
                self.print_hands()
                self.player_turn()
                self.dealer_turn()
                self.reset_game()
            else:
                print("Thanks for playing!")
                print("Your final chip count is:", self.player_chips)
                break

    @staticmethod
    def print_cards_side_by_side(cards, reveal):
        # Get ASCII art for each card
        lines_per_card = [c.ascii() if reveal else c.back_ascii() for c in cards]

        # Print row by row
        for i in range(len(lines_per_card[0])):
            print("   ".join(card[i] for card in lines_per_card))

    def reset_game(self):
        # Take the cards from the hands and put them back into the deck
        self.deck.cards.extend(self.player_hand)
        self.deck.cards.extend(self.dealer_hand)
        self.player_hand = []
        self.dealer_hand = []
        self.player_chips_bet = 0
        self.deck.shuffle()

    def intro(self):
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            if self.player_chips == 0:
                print("You are out of chips! Game over. Take some from the kids College Fund.")
                return False
            print(blackjack.logo)
            choice = input("Do you want to play a game of Blackjack? (1: Yes, 2: No): ")
            if choice == "1":
                return True
            elif choice == "2":
                return False
            else:
                print("Invalid input. Please enter 1 or 2.")

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
        os.system('clear' if os.name == 'posix' else 'cls')
        print(blackjack.logo)
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
        # Change for adding insurance and doubling down
        while True:
            if self.calculate_hand_value(self.player_hand) == 21:
                print("Blackjack! You win.")
                self.player_chips += self.player_chips_bet * 2.5
                input("Press Enter to continue...")
                return
            action = input("Do you want to (h)it, (s)tand, (d)ouble down, or (i)nsure? ").lower()
            if action == "h":
                os.system('clear' if os.name == 'posix' else 'cls')
                self.player_hand.append(self.deck.cards.pop())
                self.print_hands()
                if self.calculate_hand_value(self.player_hand) > 21:
                    print("Bust! You lose.")
                    return
            elif action == "s":
                break
            elif action == "d":
                if self.player_chips >= self.player_chips_bet * 2:
                    self.player_chips -= self.player_chips_bet
                    self.player_chips_bet *= 2
                    self.player_hand.append(self.deck.cards.pop())
                    self.print_hands()
                    if self.calculate_hand_value(self.player_hand) > 21:
                        print("Bust! You lose.")
                        return
                else:
                    print("Insufficient chips to double down.")
            elif action == "i":
                if self.player_chips >= self.player_chips_bet / 2:
                    self.player_chips -= self.player_chips_bet / 2
                    self.player_chips_bet += self.player_chips_bet / 2
                    self.player_hand.append(self.deck.cards.pop())
                    self.print_hands()
                    if self.calculate_hand_value(self.player_hand) > 21:
                        print("Bust! You lose.")
                        return
                else:
                    print("Insufficient chips to place insurance.")
            else:
                print("Invalid input. Please enter 'h', 's', 'd', or 'i'.")
    
    def dealer_turn(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.cards.pop())
        self.print_hands(reveal_dealer=True)
        self.determine_winner()

    def determine_winner(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if player_value > 21:
            print("You bust! Dealer wins.")
        elif dealer_value > 21 or player_value > dealer_value:
            print("You win!")
            self.player_chips += self.player_chips_bet * 2
        elif player_value < dealer_value:
            print("Dealer wins.")
        else:
            print("It's a tie!")
            self.player_chips += self.player_chips_bet
        print(f"Your chips: {self.player_chips}")
        input("Press Enter to continue...")


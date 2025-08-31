


class card:
    def __init__(self, suit, value, card):

        match suit:
            case 1:
                self.suit = "♥"
            case 2:
                self.suit = "♦"
            case 3:
                self.suit = "♣"
            case 4:
                self.suit = "♠"

        match card:
            case 1:
                self.card = "A"
            case 11:
                self.card = "J"
            case 12:
                self.card = "Q"
            case 13:
                self.card = "K"
            case _:
                self.card = str(card)
        
        match value:
            case 1:
                self.value = 11
            case 11 | 12 | 13:
                self.value = 10
            case _:
                self.value = value

        
    def printCard(self):
        print(f"""
        -----------
        | {self.card}       |
        |         |
        |    {self.suit}    |
        |         |
        |       {self.card} |
        -----------
        """)

    def getCardValue(self):
        return self.value
    



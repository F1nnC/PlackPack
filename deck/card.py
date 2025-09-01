class card:
    def __init__(self, suit, value, card):
        match suit:
            case 1: self.suit = "♥"
            case 2: self.suit = "♦"
            case 3: self.suit = "♣"
            case 4: self.suit = "♠"

        match card:
            case 1: self.card = "A"
            case 11: self.card = "J"
            case 12: self.card = "Q"
            case 13: self.card = "K"
            case _: self.card = str(card)

        match value:
            case 1: self.value = 11
            case 11 | 12 | 13: self.value = 10
            case _: self.value = value

    def ascii(self):
        """Return card as list of strings (one line per row)."""
        if self.card == "10":
            return [
                "-----------",
                f"| {self.card}      |",
                "|         |",
                f"|    {self.suit}    |",
                "|         |",
                f"|      {self.card} |",
                "-----------"
            ]
        else:
            return [
                "-----------",
                f"| {self.card}       |",
                "|         |",
                f"|    {self.suit}    |",
                "|         |",
                f"|       {self.card} |",
                "-----------"
            ]

    def back_ascii(self):
        return [
            "-----------",
            "|         |",
            "|         |",
            "|    ?    |",
            "|         |",
            "|         |",
            "-----------"
        ]

    def getCardValue(self):
        return self.value

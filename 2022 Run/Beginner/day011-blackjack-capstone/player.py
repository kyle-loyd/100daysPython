class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = 0

    def add_to_hand(self, card):
        self.hand.append(card)
        self.hand_value += card.value
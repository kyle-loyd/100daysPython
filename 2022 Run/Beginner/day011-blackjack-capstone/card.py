class Card:
    def __init__(self, suit_param, name_param, hand_value, face_down):
        self.suit = suit_param
        self.name = name_param 
        self.value = self.get_card_value(hand_value)
        self.face_down = face_down

    def get_card_value(self, hand_value):
        royals = ["J", "Q", "K"]
        if self.name in royals:
            return 10
        elif self.name == "A":
            return 11 if hand_value > 10 else 1
        else:
            return int(self.name)
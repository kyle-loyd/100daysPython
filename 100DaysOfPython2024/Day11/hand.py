import card


class Hand:
    def __init__(self):
        self.cards = [card.Card(), card.Card()]
        self.value = sum(_card.value for _card in self.cards)
        self.bust = self.check_bust()

    def check_bust(self):
        while self.value > 21 and any(_card.value == 11 for _card in self.cards):
            for _card in self.cards:
                if _card.value == 11:
                    _card.value = 1
                    self.value -= 10
                    break
        return self.value > 21

    def add_card(self):
        new_card = card.Card()
        self.cards.append(new_card)
        if new_card.name == "A":
            value_add = 1 if self.value + 11 > 21 else 11
            self.value += value_add
        else:
            value_add = 10 if new_card.name in card.royals else new_card.value
            self.value += value_add

        self.bust = self.check_bust()


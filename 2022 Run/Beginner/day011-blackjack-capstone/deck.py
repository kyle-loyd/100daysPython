import random
import card

possible_card_names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
possible_card_suits = ["spades", "hearts", "diamonds", "clubs"]

class Deck:
    def __init__(self):
        self.available_cards = {}
        self.initialize_available_cards()

    def initialize_available_cards(self):
        for suit in possible_card_suits:
            self.available_cards.update( { suit: [name for name in possible_card_names] } )

    def adjust_available_cards(self, selected_card):
        card_index = self.available_cards[selected_card.suit].index(selected_card.name)
        self.available_cards[selected_card.suit].pop(card_index)
        if len(self.available_cards[selected_card.suit]) == 0:
            suit_index = self.available_cards.index(selected_card.suit)
            self.available_cards.pop(suit_index)
        return

    def draw_card(self, hand_value, face_down):
        selected_suit = possible_card_suits[random.randint(0, len(possible_card_suits) - 1)]
        selected_name = self.available_cards[selected_suit][random.randint(0, len(self.available_cards[selected_suit]) - 1)]
        selected_card = card.Card(selected_suit, selected_name, hand_value, face_down)
        self.adjust_available_cards(selected_card)
        return selected_card
    
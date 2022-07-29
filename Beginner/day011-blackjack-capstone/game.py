import player
import deck

class Game:
    def __init__(self):
        self.human = player.Player("human")
        self.cpu = player.Player("cpu")
        self.game_state = {}
        self.current_turn = self.human
        self.is_over = False
        self.winner = None
        self.deck = deck.Deck()
        self.deal_new_game()

    def deal_new_game(self):
        self.draw(self.human, False)
        self.draw(self.human, False)
        self.draw(self.cpu, True)
        self.draw(self.cpu, False)
        self.update_player(self.human)
        self.update_player(self.cpu)

    def draw(self, target_player, face_down):
        card = self.deck.draw_card(target_player.hand_value, face_down = face_down)
        target_player.add_to_hand(card)

    def evaluate(self):
        if self.human.hand_value > 21:
            self.is_over = True
            self.winner = self.cpu.name
            return

        if not self.current_turn.name == self.human.name:
            if self.cpu.hand_value > 21:
                self.is_over = True
                self.winner = self.human.name
                return

            elif self.cpu.hand_value > self.human.hand_value:
                self.is_over = True
                self.winner = self.cpu.name

            

    def next_turn(self):
        self.current_turn = self.cpu if self.current_turn.name == self.human.name else None
        if self.current_turn.name == self.cpu.name:
            self.cpu.hand[0].face_down = False
        else:
            self.evaluate()

    def update_player(self, target_player):
        self.game_state[target_player] = {
            "hand": [card for card in target_player.hand],
            "value": target_player.hand_value
        }

    def perform_cpu_turn():
        return
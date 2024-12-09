import random

royals = ["K", "Q", "J"]
draw_key = {
    1: "A",
    11: "J",
    12: "Q",
    13: "K"
}


class Card:
    def __init__(self):
        random_value = random.randint(1, 13)
        self.name = draw_key.get(random_value, str(random_value))
        self.value = 10 if self.name in royals else 11 if self.name == "A" else int(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

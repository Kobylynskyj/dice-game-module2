# Содержит описание классов, используемых в игре:
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"Hello I'm am {self.name}"

    def roll_dice(self):
        return random.randint(1,6)


    def update_score(self, points):
        self.score += points

            


class Computer(Player):
    def __init__(self):
        super().__init__("Computer")





from heroes import Hero
import random
from utils import show


class Monsters:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.full_health = 100
        self.power = 8
        self.armor = None
        self.stamina = None
        self.xp = 20

    def usual_attack(self, target: Hero):
        if target.armor == "light":
            real = self.power - 2
        elif target.armor == "medium":
            real = self.power - 5
        elif target.armor == "heavy":
            real = self.power - 10
        else:
            real = self.power

        if real < 1:
            real = 1
        target.health -= real

    def ultimate(self, target: Hero):
        target.health -= 50
        show("ULTIMATE")

    def attack(self, target: Hero):
        if random.randint(1, 4) == 4:
            self.ultimate(target)
        else:
            self.usual_attack(target)

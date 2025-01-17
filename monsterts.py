from heroes import Hero
import random
from utils import show


class Monsters:
    def __init__(
        self,
        name: str,
        power: int,
        health: int,
        xp: int = 0,
        ultimate: str | None = None,
        ultimate_attack: int | None = None,
    ):
        self.name = name
        self.health = health
        self.full_health = health
        self.power = power
        self.armor = None
        self.stamina = None
        self.xp = xp
        self.ultimate = ultimate
        self.ultimate_attack = ultimate_attack

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

    def attack(self, target: Hero):
        if self.ultimate:
            if random.randint(1, 4) == 4:
                show(self.ultimate)
                target.health -= self.ultimate_attack
                return
        self.usual_attack(target)

from abc import ABC


class Character(ABC):
    def __init__(self, name: str, health: int, power: int):
        self.name = name.title()
        self.health = health
        self.full_health = health
        self.power = power

    def attack(self, target: "Character"):
        target.health -= self.power

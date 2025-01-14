from utils import show


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.full_health = 100
        self.power = 8
        self.space_basket = 20
        self.armor = None
        self.mana = None
        self.stamina = None
        self.xp = 0
        self.level = 1

    def info(self):
        show(f"Имя героя: {self.name}")
        show(f"Здоровье: {self.health}")
        show(f"Урон: {self.power}")
        if self.mana:
            show(f"Мана: {self.mana}")
        if self.stamina:
            show(f"Выносливость: {self.stamina}")

    def attack(self, target):
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


class Samurai(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.stamina = 150
        self.armor = "light"

    def ultimate(self, target):

        if self.stamina > 30:
            show('\nuuuaaaa\n')
            target.health -= 20
            self.stamina -= 60
        else:
            self.attack(target)

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 120


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.stamina = 135
        self.armor = "medium"


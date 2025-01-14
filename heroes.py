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
        print(f"Имя героя: {self.name}")
        print(f"Здоровье: {self.health}")
        print(f"Урон: {self.power}")
        if self.mana:
            print(f"Мана: {self.mana}")
        if self.stamina:
            print(f"Выносливость: {self.stamina}")

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
        print('\nuuuaaaa\n')
        target.health -= 50
        self.stamina -= 50


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 120


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.stamina = 135
        self.armor = "medium"


from utils import show


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.full_health = 100
        self.power = 8
        self.space_basket = 20
        self.armor = None
        self.full_stamina = None
        self.stamina = None
        self.xp = 0
        self.level = 1

    def info(self):
        show(f"\nИмя героя: {self.name}")
        show(f"Здоровье: {self.health}")
        show(f"Урон: {self.power}")
        show(f"level: {self.level}")
        show(f"xp: {self.xp}")

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

    def lvl_up(self, lvl: int):
        self.level += lvl
        self.full_health += 10
        self.health = self.full_health
        show(f"\n{'<'*30} LEVEL UP {'>'*30}\n")

    def get_xp(self, xp: int):
        self.xp += xp
        if self.xp // 100 > self.level - 1:
            lvl = (self.xp // 100) - (self.level - 1)
            self.lvl_up(lvl)

    def get_full(self):
        self.stamina = self.full_stamina

    def __repr__(self):
        return self.name


class Samurai(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.stamina = 150
        self.full_stamina = 150
        self.armor = "light"

    def ultimate(self, target):
        how_many = 60
        if self.stamina > how_many:
            show("\nこんにちは\n")
            target.health -= 20
            self.stamina -= how_many
        else:
            self.attack(target)

    def info(self):
        super().info()
        show(f"Выносливость: {self.stamina}\n")


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 120
        self.full_mana = 120

    def ultimate(self, target):
        how_many = 30
        if self.mana > how_many:
            show("\nFIREBALL!!!\n")
            target.health -= 30
            self.mana -= how_many
        else:
            self.attack(target)

    def info(self):
        super().info()
        show(f"Мана: {self.mana}\n")

    def get_full(self):
        self.mana = self.full_mana

    def lvl_up(self, lvl: int):
        super().lvl_up(lvl)
        self.full_mana += 10
        self.mana = self.full_mana


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.stamina = 135
        self.armor = "medium"

    def ultimate(self, target):
        how_many = 30
        if self.stamina > how_many:
            show("\nFOR HONOR AND COURAGE\n")
            target.health -= 20
            self.stamina -= how_many
        else:
            self.attack(target)

    def info(self):
        super().info()
        show(f"Выносливость: {self.stamina}\n")

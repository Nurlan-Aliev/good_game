from src.utils import show
from src.game.entities.base import Character
from abc import ABC, abstractmethod


class Hero(Character, ABC):
    def __init__(self, name: str):
        super().__init__(name, 100, 10)
        self._xp = 0
        self.level = 1
        self._change_lvl_exp = 100

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        if value < 0:
            self._xp += 0
        self._xp += value
        self.check_level_up()

    def check_level_up(self):
        while self._xp >= self._change_lvl_exp:
            self.lvl_up()
            self._change_lvl_exp += self._change_lvl_exp // 100 * 15

    def lvl_up(self):
        self.level += 1
        self.full_health += self.full_health // 10
        self.health = self.full_health
        show(f"\n{'<'*30} LEVEL UP {'>'*30}\n", style="rgb(215,170,100)")

    @abstractmethod
    def ultimate(self, target):
        pass

    @abstractmethod
    def __str__(self):
        return (
            f"\nHero's name: {self.name}\n"
            f"Health: {self.health}\n"
            f"Damage: {self.power}\n"
            f"level: {self.level}\n"
            f"xp: {self.xp}\n"
        )


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._stamina = 135
        self._full_stamina = 135

    def ultimate(self, target):
        how_many = 30
        if self._stamina > how_many:
            target.health -= 20
            self._stamina -= how_many
            return "\nFOR HONOR AND COURAGE\n"
        else:
            return "Not enough stamina"

    def lvl_up(self):
        super().lvl_up()
        self._full_stamina += self._full_stamina // 10
        self._stamina = self._full_stamina

    def __str__(self):
        return super().__str__() + f"Stamina: {self._stamina}\n"


class Samurai(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._stamina = 150
        self._full_stamina = 150

    def ultimate(self, target):
        how_many = 60
        if self._stamina > how_many:
            target.health -= 20
            self._stamina -= how_many
            return "\nこんにちは\n"
        else:
            return "Not enough stamina"

    def __str__(self):
        return super().__str__() + f"Stamina: {self._stamina}\n"


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._mana = 120
        self._full_mana = 120

    def ultimate(self, target):
        how_many = 30
        if self._mana > how_many:
            target.health -= 30
            self._mana -= how_many
            return "\nFIREBALL!!!\n"
        else:
            return "Not enough mana"

    def lvl_up(self):
        super().lvl_up()
        self._full_mana += self._full_mana // 8
        self._mana = self._full_mana

    def __str__(self):
        return super().__str__() + f"Mana: {self._mana}\n"

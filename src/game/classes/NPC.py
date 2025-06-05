from src.game.classes.base import Character


class NPC(Character):
    def __init__(
        self,
        name: str,
        quest: str,
        monster: Character,
        xp: int,
        health: int,
        power: int,
    ):
        super().__init__(name, health, power)
        self._quest = quest
        self._status = False
        self.monster = monster
        self.xp = xp

    @property
    def quest(self):
        return self._quest

    @property
    def status(self):
        if not self.monster.alife:
            self._status = True
        return self._status

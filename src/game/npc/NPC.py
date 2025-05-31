class NPC:
    def __init__(self, name: str, quest, monster_list: dict, monster, xp=20):
        self.name = name
        self.quest = quest
        self.done = False
        self.monster_list = monster_list
        self.monster = monster
        self.xp = xp

    def get_quest(self):
        return self.quest

    def set_guest(self):
        enemy_monster = self.monster_list.get(self.monster).alife
        self.done = True
        return not enemy_monster

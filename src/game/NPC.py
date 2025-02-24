from src.game.heroes import Hero
import random
from src.utils import hear
import hashlib


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
                target.health -= self.ultimate_attack
                return self.ultimate.upper()
        self.usual_attack(target)

    def __repr__(self):
        return self.name


class NPC:
    def __init__(self, name: str, story: str, quest: dict):
        self.name = name
        self.story = story
        self.quest = quest
        self.correct = "you are right my boy"
        self.wrong = "no no no you must be know it"

    def get_story(self):
        return self.story

    def get_quest(self):
        answer = hashlib.sha256(hear(self.quest["question"]).encode()).hexdigest()
        if answer == self.quest["answer"]:
            return self.correct
        else:
            return self.wrong

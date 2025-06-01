from src.game.entities import heroes
from src.utils import input_data, option


def beginning():
    name = input_data("What is your name? ")
    hero = option("what is your hero?", ["Mage", "Samurai", "Warrior"])
    if hero == "Mage":
        return heroes.Mage(name)
    elif hero == "Samurai":
        return heroes.Samurai(name)
    elif hero == "Warrior":
        return heroes.Warrior(name)

from src.game.classes import heroes
from src.utils import input_data, option


def beginning():
    hero_list = {
        "Mage": heroes.Mage,
        "Samurai": heroes.Samurai,
        "Warrior": heroes.Warrior,
    }
    name = input_data("What is your name? ")
    hero = option("Pick a hero", ["Mage", "Samurai", "Warrior"])
    return hero_list.get(hero)(name)

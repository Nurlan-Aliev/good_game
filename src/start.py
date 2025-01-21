from src.game import heroes
from utils import show, hear
from src.script import scenario


def beginning():
    show(scenario.preface)
    name = hear("What should we call you hero? ")
    hero = hear("what is your hero?\n1.mage\n2.samurai\n3.warrior ").lower().strip()
    while hero not in ("mage", "1", "samurai", "2", "warrior", "3"):
        show("you have to chose from the list")
        hero = hear("what is your hero?\n1.mage\n2.samurai\n3.warrior ").lower().strip()
    if hero in ("mage", "1"):
        my_hero = heroes.Mage(name)
    elif hero in ("samurai", "2"):
        my_hero = heroes.Samurai(name)
    elif hero in ("warrior", "3"):
        my_hero = heroes.Warrior(name)

    my_hero.info()
    show(f"Go {my_hero.name}, mighty hero!")
    return my_hero

from src.game.NPC import Monsters
from src.utils import show, hear


def fight(hero, enemy: Monsters):
    while hero.health > 0:
        show(health_bar(hero), style='green', second=0.01)
        show(health_bar(enemy),style='red', second=0.01)
        kick: str = hear("how do you want to attack\n1. usual attack\n2. ultimate")
        if kick in ["2", "ultimate"]:
            show(hero.ultimate(enemy), style='green')
        else:
            hero.attack(enemy)
        if enemy.health <= 0:
            hero.get_xp(enemy.xp)
            hero.get_full()
            show("u win")
            break
        enemy.attack(hero)
    else:
        show("u lose")
        quit()


def health_bar(person):
    filled_percentage = int((person.health / person.full_health) * 100)
    empty_percentage = 100 - filled_percentage
    return f"{person.name.center(14, ' ')}: [{(filled_percentage * '=') + (empty_percentage * ' ')}]"

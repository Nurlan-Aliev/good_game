from src.game.heroes import Hero
from src.game.npc.monster_class import Monsters
from src.utils import show, option


def fight(hero: Hero, enemy: Monsters):
    while hero.health > 0:
        show(health_bar(hero), style="green", second=0.01)
        show(health_bar(enemy), style="red", second=0.01)
        choices = (
            ["usual attack", "ultimate"]
            if hero.stamina > 50 or hero.mana > 50
            else ["usual attack"]
        )
        kick: str = option("how do you want to attack", choices)
        if kick == "ultimate":
            show(hero.ultimate(enemy), style="green")
        else:
            show(hero.attack(enemy), style="green")

        if enemy.health <= 0:
            hero.get_xp(enemy.xp)
            enemy.set_alife()
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

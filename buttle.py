from monsterts import Monsters


def fight(hero, enemy: Monsters):
    while hero.health > 0:
        print(health_bar(hero))
        print(health_bar(enemy))
        kick: str = (
            input("how do you want to attack\n1. usual attack\n2. ultimate")
            .lower()
            .strip()
        )
        if kick in ["2", "ultimate"]:
            hero.ultimate(enemy)
        else:
            hero.attack(enemy)
        if enemy.health <= 0:
            print("u win")
            break
        enemy.attack(hero)
    else:
        print('u lose')


def health_bar(person):
    filled_percentage = int((person.health / person.full_health) * 100)
    empty_percentage = 100 - filled_percentage
    return f"{person.name}: [{(filled_percentage * '=') + (empty_percentage * ' ')}]"

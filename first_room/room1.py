from buttle import fight
from monsterts import Monsters
from utils import hear, show

rooms = {
    "info": "ok",
    "room1": Monsters("Mouse", 8, 25, 55),
    "room2": Monsters("Big mouse", 15, 45, 45),
    "room3": Monsters(
        "Mouse father", 20, 100, xp=55, ultimate="you will die!!!", ultimate_attack=40
    ),
}


def looking(hero, rooms):

    while rooms:

        while (
            check := hear(
                f'which room do you want to come? {''.join(['\n'+i for i in rooms])}'
            )
        ) not in ("room1", "room2", "room3", "info"):
            show("You have to chose from the list")
        if isinstance(rooms[check], Monsters):
            fight(hero, rooms[check])
            rooms[check] = "U still be here"
        elif rooms[check] == "ok":
            hero.info()
        else:
            show(rooms[check])

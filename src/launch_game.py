from src.game.classes.monster import Monsters
from src.utils import show, option
from src.game.classes.NPC import NPC
from src.game.classes.room import Room
from src.game.classes.heroes import Hero


def show_room_options(room: Room) -> str:
    message = "what do you want?"
    choices = ["info", *room.next_rooms.keys()]
    choice = option(message, choices)
    return choice


def npc_in_room():
    message = "what do you want?"
    choices = ["talk", "go out"]
    choice = option(message, choices)
    return choice


def handle_choice(hero: Hero, rooms: Room, choice: str) -> Room:
    if choice == "info":
        show(hero)
        return rooms

    room = rooms.change_room(choice)

    if isinstance(room.creature, Monsters):
        hero.fight(room.creature)
        room.creature = None
    elif isinstance(room.creature, NPC):
        choice = npc_in_room()
        if choice == "talk":
            room.creature.talk_npc(hero)
    else:
        show("The rooms is empty.")

    return room


def navigate_rooms(hero, rooms):

    while True:
        choice = show_room_options(rooms)
        rooms = handle_choice(hero, rooms, choice)

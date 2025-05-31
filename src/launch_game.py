from src.game.npc.monster_class import Monsters
from src.utils import show, option
from src.game.buttle import fight
from src.game.npc.NPC import NPC
from src.game.room.room_class import Room
from src.game.heroes import Hero


def show_room_options(room: Room) -> str:
    message = "what do you want?"
    choices = ["info", *room.next_rooms.keys(), "back"]
    choice = option(message, choices)
    return choice


def npc_in_room():
    message = "what do you want?"
    choices = ["talk", "go out"]
    choice = option(message, choices)
    return choice


def talk_npc(hero, creature: NPC):
    show(creature.get_quest())

    message = "Will you did it?"
    choices = ["yes", "i still did it"]
    choice = option(message, choices)
    if choice == "yes":
        show("I'll wait for you here")
    else:
        if creature.set_guest():
            hero.get_xp(creature.xp)
            show("thank you")
        else:
            show("Liar")


def handle_choice(hero: Hero, rooms: Room, choice: str) -> Room:
    if choice == "info":
        show(hero.info())
        return rooms
    elif choice == "back":
        room = rooms.previous_room
        if room:
            return room
        show("u are in the first room")
        return rooms
    elif choice in rooms.next_rooms.keys():
        room = rooms.next_rooms[choice]
        if isinstance(room.creature, Monsters):
            fight(hero, room.creature)
            room.creature = "just a room"
        elif isinstance(room.creature, NPC):
            choice = npc_in_room()
            if choice == "talk":
                talk_npc(hero, room.creature)
        else:
            show("The room is empty.")
        return room


def navigate_rooms(hero, rooms):

    while True:
        choice = show_room_options(rooms)
        rooms = handle_choice(hero, rooms, choice)

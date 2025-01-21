from utils import hear, show
from buttle import fight
from NPC import Monsters
from room_class import Room
from heroes import Hero


def show_room_options(room: Room) -> str:
    message = (
        f"Commands: info (check status)\n"
        f"which room do you want to come?\n"
        f'{"\n".join(list(room.next_rooms.keys()))}'
        f'{'\nback (go back)' if room.previous_room else ''}'
    )

    while (choice := hear(message)) not in list(
        room.next_rooms.keys()
    ) and choice not in ("info", "back"):
        hear("Pls take one from list")

    return choice


def handle_choice(hero: Hero, rooms: Room, choice: str) -> Room:
    if choice == "info":
        hero.info()
        return rooms
    elif choice == "back":
        room = rooms.previous_room
        if isinstance(room, Room):
            show(room)
            return room
        else:
            show("You are in the first room")
    elif choice in rooms.next_rooms.keys():
        room = rooms.next_rooms[choice]
        if isinstance(room.creature, Monsters):
            fight(hero, room.creature)
            room.creature = "just a room"
        elif isinstance(room.creature, str):
            show(room.creature)
        else:
            show("The room is empty.")
        return room


def navigate_rooms(hero, rooms):

    while True:
        choice = show_room_options(rooms)
        rooms = handle_choice(hero, rooms, choice)

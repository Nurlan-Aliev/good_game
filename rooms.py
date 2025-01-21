from NPC import Monsters
from room_class import Room


start_room = Room("start_room", None, None)
room1 = Room("room1", Monsters("Mouse", 8, 25, 55), start_room)
room2 = Room("room2", Monsters("Big mouse", 15, 50, 45), start_room)
room3 = Room(
    "room3",
    Monsters(
        "Mouse father", 20, 100, xp=55, ultimate="you will die!!!", ultimate_attack=40
    ),
    start_room,
)


start_room.add_next_room(room1)
start_room.add_next_room(room2)
start_room.add_next_room(room3)

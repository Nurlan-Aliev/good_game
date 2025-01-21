from src.game.NPC import Monsters
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
room4 = Room('room4', Monsters(), room3)
room5 = Room('room5', Monsters(), room4)
room6 = Room('room6', Monsters(), room3)
room7 = Room('room7', Monsters(), room6)
room8 = Room('room8', Monsters(), room6)
room9 = Room('room9', Monsters(), room6)
room10 = Room('room10', Monsters(), room9)
room11 = Room('room11', Monsters(), room8)
room12 = Room('room12', Monsters(), room8)
room13 = Room('room13', Monsters(), room8)
room14 = Room('room14', Monsters(), room13)
room15 = Room('room15', Monsters(), room13)
room16 = Room('room16', Monsters(), room13)
room17 = Room('room17', Monsters(), room12)
room18 = Room('room18', Monsters(), room12)
room19 = Room('room19', Monsters(), room16)
room20 = Room('room20', Monsters(), room19)
room21 = Room('room21', Monsters(), room19)
room22 = Room('room22', Monsters(), room19)
room23 = Room('room23', Monsters(), room22)
room24 = Room('room24', Monsters(), room21)
room25 = Room('room25', Monsters(), room21)
room26 = Room('room26', Monsters(), room25)
room27 = Room('room27', Monsters(), room25)
room28 = Room('room28', Monsters(), room25)
room29 = Room('room29', Monsters(), room25)
room30 = Room('room30', Monsters(), room29)

start_room.add_next_room(room1)
start_room.add_next_room(room2)
start_room.add_next_room(room3)

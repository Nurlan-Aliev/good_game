from src.game.npc.modnster_list import monsters
from src.game.room.room_class import Room
from src.game.npc.persons import npc_list

start_room = Room("start_room", None, None)
room1 = Room("room1", monsters.get("Big mouse"), start_room)
room2 = Room("room2", monsters.get("Mouse"), start_room)
room3 = Room("room3", monsters.get("Mouse father"), start_room)
room4 = Room("room4", None, room3)
room5 = Room("room5", npc_list.get("Groter"), room2)


start_room.add_rooms(room1, room2, room3)
room2.add_next_room(room5)
room3.add_rooms(room4)

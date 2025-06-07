from src.game.rooms.level_1.modnster_list import monsters_dict
from src.game.classes.room import Room
from src.game.rooms.level_1.persons import npcs_dict


start_room = Room("start_room", None)
room1 = Room("room1", monsters_dict["monster_1"])
room2 = Room("room2", monsters_dict["monster_2"])
room3 = Room("room3", monsters_dict["monster_3"])
room4 = Room("room4", monsters_dict["monster_4"])
room5 = Room("room5", npcs_dict["skrivn"])
room6 = Room("room6", monsters_dict["boss_2"])
room7 = Room("room7", monsters_dict["monster_5"])
room8 = Room("room8", monsters_dict["monster_6"], blocked=True)
room9 = Room("room9", npcs_dict["sister_elvari"])
roomA = Room("roomA", monsters_dict["boss_1"])
roomB = Room("roomB", None, blocked=True)


start_room.add_rooms(room1, room2)
room1.add_rooms(start_room, room6, room7)
room2.add_rooms(start_room, room3, room4)
room3.add_rooms(room2, room9)
room4.add_rooms(room2, room5)
room5.add_rooms(room4)
room6.add_rooms(room1)
room7.add_rooms(room1, room8, roomA)
room8.add_rooms(room7)
room9.add_rooms(room3)
roomA.add_rooms(room7, roomB)
roomB.add_rooms(roomA)


npcs_dict["sister_elvari"].room = roomB
npcs_dict["skrivn"].room = room8

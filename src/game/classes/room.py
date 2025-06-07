from src.game.classes.base import Character
from src.utils import show


class Room:
    def __init__(self, name: str, creature: Character | None, blocked: bool = False):
        self.name = name
        self.creature = creature
        self.next_rooms: dict[str, Room] = {}
        self.blocked = blocked

    def add_rooms(self, *args):
        self.next_rooms.update(
            {room.name: room for room in args if isinstance(room, Room)}
        )

    def change_room(self, choice):

        if choice not in self.next_rooms.keys():
            return f"{choice} it is not a room"

        if not self.next_rooms[choice].blocked:
            return self.next_rooms[choice]

        show("this room is blocked")
        return self

    def unblocked(self):
        self.blocked = False

    def __str__(self):
        return self.name

class Room:
    def __init__(self, name: str, creature):
        self.name = name
        self.creature = creature
        self.next_rooms: dict[str, Room] = {}

    def add_rooms(self, *args):
        self.next_rooms.update(
            {room.name: room for room in args if isinstance(room, Room)}
        )

    def __str__(self):
        return self.name

class Room:
    def __init__(self, name: str, creature, previous_room):
        self.name = name
        self.creature = creature
        self.next_rooms: dict[str:Room] = {}
        self.previous_room = previous_room

    def add_next_room(self, room):
        if isinstance(room, Room):
            self.next_rooms[room.name] = room

    def add_rooms(self, *args):
        for room in args:
            self.add_next_room(room)

    def __str__(self):
        return self.name

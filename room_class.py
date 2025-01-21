class Room:
    def __init__(self, name: str, creature, previous_room):
        self.name = name
        self.creature = creature
        self.next_rooms: dict[str:Room] = {}
        self.previous_room = previous_room

    def add_next_room(self, room):
        if isinstance(room, Room):
            self.next_rooms[room.name] = room

    def __repr__(self):
        return self.name

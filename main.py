from start import beginning
from first_room.room1 import looking, rooms


def play_game():
    hero = beginning()
    looking(hero, rooms)


if __name__ == "__main__":
    play_game()

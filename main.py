from src.start import beginning
from src.launch_game import navigate_rooms
from src.game.room.rooms import start_room


def play_game():
    hero = beginning()
    navigate_rooms(hero, start_room)


if __name__ == "__main__":
    play_game()

from start import beginning
from launch_game import start_room, navigate_rooms


def play_game():
    hero = beginning()
    navigate_rooms(hero, start_room)


if __name__ == "__main__":
    play_game()

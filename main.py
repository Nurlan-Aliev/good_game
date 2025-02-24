from src.script import scenario
from src.start import beginning
from src.launch_game import navigate_rooms
from src.game.room.rooms import start_room
from src.utils import show


def play_game():
    # show(scenario.preface, style="green")
    hero = beginning()
    show(hero.info(), style='green')
    navigate_rooms(hero, start_room)


if __name__ == "__main__":
    play_game()

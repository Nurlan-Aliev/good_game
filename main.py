from start import beginning
from monsterts import Monsters
from buttle import fight

mo = Monsters('monster')


def play_game():
    hero = beginning()
    fight(hero, mo)


play_game()

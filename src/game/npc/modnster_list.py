from src.game.classes.monster import Monsters, BossMonster

monsters = {
    "Mouse": Monsters("Mouse", 8, 25, 55),
    "Big mouse": Monsters("Big mouse", 15, 50, 45),
    "Mouse father": BossMonster(
        "Mouse father",
        20,
        100,
        exp_reward=55,
        ultimate_phrase="you will die!!!",
        ultimate_power=40,
    ),
}

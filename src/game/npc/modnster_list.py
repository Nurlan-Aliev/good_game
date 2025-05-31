from src.game.npc.monster_class import Monsters

monsters = {
    "Mouse": Monsters("Mouse", 8, 25, 55),
    "Big mouse": Monsters("Big mouse", 15, 50, 45),
    "Mouse father": Monsters(
        "Mouse father", 20, 100, xp=55, ultimate="you will die!!!", ultimate_attack=40
    ),
}

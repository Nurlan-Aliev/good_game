from src.game.classes.NPC import NPC
from src.game.npc.modnster_list import monsters


npc_list = {
    "Groter": NPC(
        "Groter",
        "Mouses kill my daughter pleas find their father and kill him",
        monsters["Mouse"],
        30,
        1000,
        1000,
    )
}

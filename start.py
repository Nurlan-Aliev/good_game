import heroes


def beginning():
    name = input("what is your name?\n-> ")
    hero = (
        input("what is your hero?\n1.mage\n2.samurai\n3.warrior\n-> ").lower().strip()
    )
    while hero not in ("mage", "1", "samurai", "2", "warrior", "3"):
        print("you have to chose from the list")
        hero = (
            input("what is your hero?\n1.mage\n2.samurai\n3.warrior\n-> ")
            .lower()
            .strip()
        )
    if hero in ("mage", "1"):
        my_hero = heroes.Mage(name)
    elif hero in ("samurai", "2"):
        my_hero = heroes.Samurai(name)
    elif hero in ("warrior", "3"):
        my_hero = heroes.Warrior(name)
    my_hero.info()
    return my_hero

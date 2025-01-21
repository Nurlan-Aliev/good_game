from time import sleep


def show(info: str):
    print(info)
    # sleep(1)


def hear(info: str):
    return input(info + "\n-> ")

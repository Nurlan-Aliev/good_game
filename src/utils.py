from time import sleep
from rich.console import Console


console = Console()


def show(info: str, style: str = "", second: float = 0.05):
    for latter in info:
        console.print(latter, end="", style=style)
        sleep(second)
    print()


def hear(info: str, style=""):
    show(info, style=style)
    return console.input("-> ")

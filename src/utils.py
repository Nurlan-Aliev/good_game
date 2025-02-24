from time import sleep
from rich.console import Console
import questionary

console = Console()


def show(info: str, style: str = "", second: float = 0.05):
    for latter in info:
        console.print(latter, end="", style=style)
        sleep(second)
    print()


def input_data(info: str, style=""):
    show(info, style=style)
    return console.input("-> ")


def select_var(message: str, options: list):
    return questionary.select(
        message, choices=options
    ).ask()

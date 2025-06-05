from time import sleep
from rich.console import Console
import questionary
from prompt_toolkit.styles import Style
from typing import Iterable


console = Console()


def show(info: any, style: str = "", second: float = 0.05):
    if info:
        for latter in info:
            console.print(latter, end="", style=style)
            sleep(second)
        print()


def input_data(info: str, style=""):
    show(info, style=style)
    return console.input("-> ")


def option(message: str, options: Iterable):

    custom_style = Style(
        [
            ("qmark", "red"),  # Цвет вопросительного знака (?)
            ("question", "fg:#00ff00 bold"),  # Цвет текста вопроса
            ("answer", "fg:#ff0000 bold"),  # Цвет выбранного ответа
            ("pointer", "fg:#00ffff bold"),  # Цвет стрелки (›)
            ("highlighted", "fg:#ff00ff bold"),  # Цвет подсвеченного варианта
            ("selected", "fg:#ffff00 bold"),  # Цвет выбранного элемента
            ("separator", "fg:#888888"),  # Цвет разделителя
        ]
    )
    return questionary.select(message, choices=options, style=custom_style).ask()

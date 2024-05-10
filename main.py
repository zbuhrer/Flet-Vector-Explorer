import flet as ft

from static.ui.viewer import MainView
from anki_vector import Robot as R


def main(page: ft.Page) -> None:
    def __init__(self):
        self.page.title = "Vector Synapse"

    mv = MainView()
    page.add(mv.tabs)

if __name__ == "__main__":
    ft.app(main)
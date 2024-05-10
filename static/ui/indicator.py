from flet import Column, Icon, Text, Control
from typing import Callable

class StatusItem(Control):
    def __init__(self, text: str, icon: Icon):
       super().__init__()
       self.controls = [icon, Text(text)]


class Indicator(Column):
    def __init__(self):
        super().__init__()
        self.controls = []

    def add_item(self, text: str, method: Callable[[],bool]) -> None:
        icon = Icon(name = 'check_circle', color = 'green' if method() else 'red')
        self.controls.append(StatusItem(text, icon))

import anki_vector as av

class StatusIndicator(av.Robot):
    with av.Robot() as robot:
        indicator = Indicator()
        indicator.add_item("Status 01", lambda : True)
        indicator.add_item("Status 02", lambda : True)
        indicator.add_item("Status 03", lambda : True)
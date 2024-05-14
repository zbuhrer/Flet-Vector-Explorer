import anki_vector as av
import static.explorer as xp
import flet as ft

import asyncio
import queue
import random

from flet import Page, Container, Text, Column, Icon, Control, WebView, TextField, ElevatedButton, ListView
from typing import Callable
from static.vector_talk import Chatter

ANKI_ROBOT_SERIAL = '00702f96'

currentbot = None
currentbot_name = ''
currentbot_serial = ANKI_ROBOT_SERIAL




class Status(Container):
    def __init__(self):
        super().__init__()
        self.contents = [
            Text("Status Placeholder"),
        ]

class Settings(Container):
    def __init__(self):
        super().__init__()
        self.contents = [Text("Settings Placeholder")]

class StatusItem(Control):
    def __init__(self, text: str, icon: Icon):
        super().__init__()
        self.controls = [icon, Text(text)]

class Indicator(Column):
    def __init__(self):
        super().__init__()
        self.controls = []

    def add_item(self, text: str, method: Callable[[], bool]) -> None:
        icon = Icon(name='check_circle', color='green' if method() else 'red')
        self.controls.append(StatusItem(text, icon))

class StatusIndicator(Chatter):
    async def main(self):
        indicator = Indicator()
        indicator.add_item("Status 01", lambda: True)
        indicator.add_item("Status 02", lambda: True)
        indicator.add_item("Status 03", lambda: True)

class Chat(Column):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.text_field = ft.TextField(label='Vector speak...')
        self.submit_button = ft.ElevatedButton("Say", on_click=self.send)
        self.messages_widget = ft.ListView()
        self.text_field.value = ""
        self.messages_list = []
        self.controls = [
            self.text_field,
            self.submit_button,
            self.messages_widget
            ]
        self.serial = currentbot_serial

    async def send(self, text):

        text = str(self.text_field.value)
        self.text_field.disabled = True
        self.submit_button.disabled = True
        self.update()
        chatter = Chatter()

        try: 
            chatter.talk(text)
            self.messages_widget.controls.append(ft.Text(text))
            self.update()
        except asyncio.TimeoutError as e:
            print(f"Timeout error: {e}")
            self.messages_list.append(e)
            self.update()
            pass

        self.text_field.disabled = False
        self.submit_button.disabled = False
        self.text_field.value = ""
        self.update()

class About(Container):
    def __init__(self):
        super().__init__()
        self.contents = [Text("About")]

class RemoteControl(Column):
    def __init__(self):
        super().__init__()
        self.text_field = ft.TextField(label='Remote Control', read_only=True)
        self.initial_state = ft.Column(
                controls=[
                    self.text_field,
                    ElevatedButton(text="Connect", on_click=_connect),
                ])
        
        self.connected_state = ft.Column(
            controls=[
                self.text_field,
                ElevatedButton(text="Disconnect", on_click=_disconnect)
            ]
        )
        self.controls = [self.initial_state]


def _connect(self):
    print('Connecting to Vector...')
    # connection logic

    xp.run()
    
    return "Connected"        

def _disconnect():
    # disconnection logic
    return "Disconnected"
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

class RemoteControl(Column):
    def __init__(self):
        super().__init__()
        self.connect = RemoteControl._connect
        self.disconnect = RemoteControl._disconnect
        self.connectbutton = ElevatedButton(text="Connect")
        self.connectbutton.on_click='_connect'
        self.controls=[self.connectbutton]
        
    def _connect(self):
        self.connectbutton.disabled=True
        self.connectbutton.text="Connecting..."
        self.update()
        # connect to vector
        xp.run() 
        # might need to wait until confirmation is returned 
        # need error handling 
        self.connectbutton.text="Connected"
        self.connectbutton.on_click=self._disconnect
        self.connectbutton.disabled=False
        self.update()

    def _disconnect(self):
        # disconnection logic
        # need to craft a xp.kill() to disconnect from the bot
        return
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
        self.text_field=ft.TextField(value='Remote Control', read_only=True, disabled=True)
        self.initial_state = ft.Column(
            controls=[
                self.text_field,
                ElevatedButton(text="Connect", on_click=_connect)])
        self.controls = [self.initial_state]


    def update_state(self, state):
        self.text_field=ft.TextField(value='Remote Control', read_only=True, disabled=True)
        connecting_state = ft.Column(
            controls=[
                self.text_field,
                ElevatedButton(text="Connect", on_click=_connect, disabled=True),
                ft.ProgressRing()])
        connected_state = ft.Column(
            controls=[
                self.text_field,
                ElevatedButton(text="Disconnect", on_click=_disconnect, disabled=False)])

        if state == "connecting":
            self.controls = [connecting_state]
        if state == "connected":
            self.controls = [connected_state]
        else:
            RemoteControl.__init__(self)
        return 
        


def _connect(self):
    print('Connecting to Vector...')
    RemoteControl.update_state(self,state="connecting")
    xp.run() 
    # might need to wait until confirmation is returned 
    # need error handling 
    RemoteControl.update_state(self,state="connected")
    return "connected"

def _disconnect(self):
    # disconnection logic
    # need to craft a xp.kill() to disconnect from the bot

    self.state = "initial"
    RemoteControl.update_state(self,state="initial")
    return "Disconnected"
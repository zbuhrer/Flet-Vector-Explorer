import flet as ft
import json, requests

class RemoteControlPage(ft.Container):
  def __init__(self,switch_page):
    super().__init__()
    self.switch_page = switch_page    
    self.content = ft.Column(
      controls=[
      ft.Text(value="Remote Control Page confirmed working!")
      ])
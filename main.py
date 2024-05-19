import flet as ft
import json, requests


from anki_vector import Robot as R

from utils.extras import *

class MainPage(ft.Container):
  def __init__(self,switch_page):
    super().__init__()
    self.switch_page = switch_page    
    self.content = ft.Column(
      controls=[
      ft.Text(value="Main Page confirmed working!")
      ])
    
class BotListPage(ft.Container):
  def __init__(self,switch_page):
    super().__init__()
    self.switch_page = switch_page    
    self.content = ft.Column(
      controls=[
      ft.Text(value="Bot List Page confirmed working!")
      ])

class App(ft.UserControl):
    def __init__(self,pg:ft.Page):
        super().__init__()
        pg.window_title_bar_buttons_hidden = False
        pg.window_width = base_width
        pg.window_height = base_height
        pg.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.VIEW_COMPACT, data='main_page', on_click=self.switch_page),
            title=ft.Text("Vector Explorer"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.PopupMenuButton(
                icon=ft.icons.GAMEPAD,
                items=[
                    ft.PopupMenuItem(text="Connection Info"),
                    ft.PopupMenuItem(text="Remote Controller")
                ]),
                ft.PopupMenuButton(icon=ft.icons.SIGNAL_WIFI_OFF_OUTLINED,items=[
                    ft.PopupMenuItem(text="Connect"),
                    ft.PopupMenuItem(text="Bot List", data='botlist', on_click=self.switch_page),
                ]),
                ft.PopupMenuButton(
                icon=ft.icons.MORE_HORIZ,
                items=[
                    ft.PopupMenuItem(text="Server Settings"),
                    ft.PopupMenuItem(text="Bot Settings"),
                    ft.PopupMenuItem(text="Custom Intents"),
                    ft.PopupMenuItem(text="Logs"),
                    ft.PopupMenuItem(text="Version Info"),
                ]),
            ])

        self.pg = pg
        self.main_page = MainPage(self.switch_page)
        self.botlist_page = BotListPage(self.switch_page)
        self.screen_views = ft.Stack(
            expand=True,
            controls=[self.main_page])
        self.init_helper()
    
    def switch_page(self,e):
        if e.control.data == 'authenticate':
            print("Connecting to Vector...")
            # make a call to connect to a robot
            # confirm that the robot is connected 
            # change values in the UI to reflect that the robot is connected
            # change the page content to the main page
            # page.update()
            return
        
        elif e.control.data == 'botlist':
            print("Loading Bot list")
            # make a call to get the list of available bots 
            self.screen_views.controls.clear()
            # change the page content to the botlist page
            self.screen_views.controls.append(self.botlist_page)
            # page.update()
            self.screen_views.update()
            return
        elif e.control.data == 'main_page':
            print("Loading Main Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.main_page)
            self.screen_views.update()
            return
    
    def _botlist(self, e):
        response = requests.get('https://localhost:5000/api-sdk/get_sdk_info')

        if response.status_code == 200:
            json_response = json.loads(response.text)

            for bot in json_response["robots"]:
                print(f"Bot: {bot['esn']}")
                ft.Text(f"Bot: {bot['esn']}")
        else:
            ft.Text("Error authenticating!")

        return
    
    def init_helper(self):
        self.pg.add(self.screen_views)

ft.app(target=App,assets_dir="assets")
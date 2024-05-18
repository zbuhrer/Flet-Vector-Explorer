import flet as ft
import static.explorer as xp
import anki_vector
import json, requests


from static.ui.viewer import MainView, CameraView
from anki_vector import Robot as R


class MainMenu(ft.UserControl):
    def __init__(self):
        super(MainMenu, self).__init__()

    def _buildmenu(self) -> tuple:
        # items inside menus 
        connectitem = ft.PopupMenuItem(text="Connect", on_click=self._connect)
        connectinfoitem = ft.PopupMenuItem(text="Bot List", on_click=self._botlist)

        # menus 
        connect_menu = ft.PopupMenuButton(icon=ft.icons.SIGNAL_WIFI_OFF_OUTLINED,items=[
                connectitem,
                connectinfoitem,
            ])
        hamburger_menu = ft.PopupMenuButton(
            icon=ft.icons.MORE_HORIZ,
            items=[
                ft.PopupMenuItem(text="Server Settings", on_click=self.show_server_settings),
                ft.PopupMenuItem(text="Bot Settings", on_click=self.show_bot_settings),
                ft.PopupMenuItem(text="Custom Intents", on_click=self.show_custom_intents),
                ft.PopupMenuItem(text="Logs", on_click=self.show_logs),
                ft.PopupMenuItem(text="Version Info", on_click=self.show_version_info),
            ])
        controller_menu = ft.PopupMenuButton(
            icon=ft.icons.GAMEPAD,
            items=[
                ft.PopupMenuItem(text="Connection Info"),
                ft.PopupMenuItem(text="Remote Controller")
            ])        
        return hamburger_menu, connect_menu, controller_menu

    def _connect(self):
        print("Connecting to Vector...")
        return
    
    def show_server_settings(self):
        print("Server Settings page opened!")

    def show_bot_settings(self):
        print("Bot Settings page opened!")

    def show_custom_intents(self):
        print("Custom Intents page opened!")

    def show_logs(self):
        print("Logs page opened!")

    def show_conninfo(self):
        print("Connection info placeholder!")

    def show_version_info(self):
        print("Version Info page opened!")
    
    def _botlist(self):
        response = requests.get('localhost:5000/api-sdk/get_sdk_info')

        if response.status_code == 200:
            json_response = json.loads(response.text)

            for bot in json_response["robots"]:
                print(f"Bot: {bot['esn']}")
                ft.Text(f"Bot: {bot['esn']}")
        else:
            ft.Text("Error authenticating!")

        return
    


def main(page: ft.Page):
    menu_items = MainMenu()._buildmenu()
    connect_menu, hamburger_menu, controller_menu = menu_items

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.VIEW_COMPACT),
        title=ft.Text("Vector Explorer"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            controller_menu,
            connect_menu,
            hamburger_menu,
        ])

    page.add(ft.Text("Body!"))

ft.app(target=main)
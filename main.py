import flet as ft
import static.explorer as xp
import anki_vector


from static.ui.viewer import MainView, CameraView
from anki_vector import Robot as R




def main(page: ft.Page):
    def __init__(self):    
        self.hamburgermenu = ft.PopupMenuButton(
            icon=ft.icons.MORE_HORIZ,
            items=[
                ft.PopupMenuItem(text="Server Settings", on_click=show_server_settings),
                ft.PopupMenuItem(text="Bot Settings", on_click=show_bot_settings),
                ft.PopupMenuItem(text="Custom Intents", on_click=show_custom_intents),
                ft.PopupMenuItem(text="Logs", on_click=show_logs),
                ft.PopupMenuItem(text="Version Info", on_click=show_version_info),
            ])
        

        self.controllermenu = ft.PopupMenuButton(
            icon=ft.icons.GAMEPAD,
            items=[
                ft.PopupMenuItem(text="Connection Info"),
                ft.PopupMenuItem(text="Remote Controller")
            ])
        return self.controllermenu, self.hamburgermenu
    
    def show_server_settings(e):
        print("Server Settings page opened!")

    def show_bot_settings(e):
        print("Bot Settings page opened!")

    def show_custom_intents(e):
        print("Custom Intents page opened!")

    def show_logs(e):
        print("Logs page opened!")

    def show_conninfo(e):
        print("Connection info placeholder!")

    def show_version_info(e):
        print("Version Info page opened!")

    def _connect(e):
        print("Connecting to Vector...")
        xp.run()

        return

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.VIEW_COMPACT),
        title=ft.Text("Vector Explorer"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(icon=ft.icons.SIGNAL_WIFI_OFF_OUTLINED,items=[
                ft.PopupMenuItem(text="Connect", on_click=_connect),
                ft.PopupMenuItem(text="Connection Info", on_click=show_conninfo, disabled=True),
            ])
        ])

    page.add(ft.Text("Body!"))

ft.app(target=main)
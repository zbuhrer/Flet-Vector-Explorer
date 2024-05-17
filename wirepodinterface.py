import flet as ft

def main(page: ft.Page):
    def show_server_settings(e):
        print("Server Settings page opened!")

    def show_bot_settings(e):
        print("Bot Settings page opened!")

    def show_custom_intents(e):
        print("Custom Intents page opened!")

    def show_logs(e):
        print("Logs page opened!")

    def show_version_info(e):
        print("Version Info page opened!")

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        title=ft.Text("Flet App"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                icon=ft.icons.MORE_HORIZ,
                items=[
                    ft.PopupMenuItem(text="Server Settings", on_click=show_server_settings),
                    ft.PopupMenuItem(text="Bot Settings", on_click=show_bot_settings),
                    ft.PopupMenuItem(text="Custom Intents", on_click=show_custom_intents),
                    ft.PopupMenuItem(text="Logs", on_click=show_logs),
                    ft.PopupMenuItem(text="Version Info", on_click=show_version_info),
                ]
            ),
        ],
    )

    page.add(ft.Text("Body!"))

ft.app(target=main)

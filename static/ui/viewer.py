
from flet import Page, Tabs, Tab, Container

from static.ui.pages import WebView, Chat, Settings, About, Status, RemoteControl

class CameraView(Page):
    wv = WebView(
        "localhost:port",
        expand=True,
        on_page_started= lambda _: print("Page Started"),
        on_page_ended=lambda _: print("Page Ended"),
        on_web_resource_error= lambda e: print("Web Resource Error:", e.data)
    )

class MainView(Page):
    def __init__(self):

        # Tab content 
        self.status_content = Container(Status(), padding=10)
        self.chat_content = Container(Chat(),padding=10)
        self.settings_content = Container(Settings(),padding=10)
        self.about_content = Container(About(),padding=10)
        self.remote_control_content = Container(RemoteControl(),padding=10)

        # Tabs
        self.tab_status = Tab(text='Status',content=self.status_content)
        self.tab_chat = Tab(text='Chat',content=self.chat_content)
        self.tab_settings = Tab(text='Settings',content=self.settings_content)
        self.tab_about = Tab(text='About',content=self.about_content)
        self.tab_remote = Tab(text='Remote Control',content=self.remote_control_content)
        self.tabs = Tabs(
            tabs=[
                self.tab_status,
                self.tab_chat, 
                self.tab_settings, 
                self.tab_about,
                self.tab_remote
            ]
        )
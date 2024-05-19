
from flet import Page, Tabs, Tab, Container

from static.ui.pages import WebView, Chat, RemoteControl

class CameraView(Page):
    wv = WebView(
        "localhost:port",
        expand=True,
        on_page_started= lambda _: print("Page Started"),
        on_page_ended=lambda _: print("Page Ended"),
        on_web_resource_error= lambda e: print("Web Resource Error:", e.data)
    )

class MainView(Container):
    def __init__(self, switch_page):
        super().__init__()
        self.switch_page = switch_page

        # Tab content 
        self.chat_content = Container(Chat(),padding=10)
        self.remote_control_content = Container(RemoteControl(),padding=10)

        # Tabs
        self.tab_chat = Tab(text='Chat',content=self.chat_content)
        self.tab_remote = Tab(text='Remote Control',content=self.remote_control_content)
        self.tabs = Tabs(
            tabs=[
                self.tab_chat, 
                self.tab_remote
            ]
        )
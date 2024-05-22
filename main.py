import flet as ft
# import json, requests

from utils.extras import *
from pages.sdk_index import MainPage, WirepodSettings, BotSettings, BotListPage, CustomIntents, Logs
from pages.remote_control import RemoteControlPage

class App(ft.UserControl):
    def __init__(self,pg:ft.Page):
        super().__init__()
        pg.window_title_bar_buttons_hidden = True
        pg.window_frameless = True
        pg.window_width = base_width
        pg.window_height = base_height
        
        self.connect_menu = ft.PopupMenuButton(icon=ft.icons.SIGNAL_WIFI_OFF_OUTLINED,
                    items=[
                        ft.PopupMenuItem(text="Connect", data='connect', on_click=self.switch_page)])
        self.settings_menu = ft.PopupMenuButton(icon=ft.icons.SETTINGS,
                    items=[
                        ft.PopupMenuItem(text="Server Settings", data='serversettings', on_click=self.switch_page),
                        ft.PopupMenuItem(text="Current Bot Settings", data='botsettings', on_click=self.switch_page),
                        ft.PopupMenuItem(text="Bot List", data='botlist', on_click=self.switch_page),
                        ft.PopupMenuItem(text="Custom Intents", data='customintents', on_click=self.switch_page),
                        ft.PopupMenuItem(text="Logs", data='logs', on_click=self.switch_page),
                        ft.PopupMenuItem(text="Version Info", disabled = True)])
        self.remotecontrol_menu =ft.IconButton(icon=ft.icons.GAMEPAD, data='remote_control', on_click=self.switch_page)

        pg.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.FORKLIFT, data='main_page', on_click=self.switch_page),
            title=ft.Text("Vector Explorer"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[self.remotecontrol_menu,self.connect_menu,self.settings_menu])
                

        self.pg = pg
        self.main_page = MainPage(self.switch_page)
        self.botlist_page = BotListPage(self.switch_page)
        self.remotecontrol_page = RemoteControlPage(self.switch_page)
        self.serversettings_page = WirepodSettings(self.switch_page)
        self.botsettings_page = BotSettings(self.switch_page)
        self.customintents_page = CustomIntents(self.switch_page)
        self.logs_page = Logs(self.switch_page)
        
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
        elif e.control.data == 'connect':
            print("Connecting to Vector...")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.remotecontrol_page)
            return  
        elif e.control.data == 'botlist':
            print("Loading Bot list")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.botlist_page)
            self.screen_views.update()
            return
        elif e.control.data == 'main_page':
            print("Loading Main Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.main_page)
            self.screen_views.update()
            return
        elif e.control.data == 'remote_control':
            print("Loading Remote Control Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.remotecontrol_page)
            self.screen_views.update()
            return
        elif e.control.data == 'serversettings':
            print("Loading Server Settings Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.serversettings_page)
            self.screen_views.update()
            return
        elif e.control.data == 'botsettings':
            print("Loading Bot Settings Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.botsettings_page)
            self.screen_views.update()
            return
        elif e.control.data == 'customintents':
            print("Loading Custom Intents Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.customintents_page)
            self.screen_views.update()
            return
        elif e.control.data == 'logs':
            print("Loading Logs Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.logs_page)
            self.screen_views.update()
            return
    
    def init_helper(self):
        self.pg.add(self.screen_views)

ft.app(target=App,assets_dir="assets")
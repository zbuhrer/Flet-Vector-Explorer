import flet as ft
import json, requests

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
        self.botlist_table = ft.Column()
        
        self.botlist_widget = ft.Column(controls=[
            ft.Row(controls=[
                ft.Text("Bot List Placeholder"), 
                ft.IconButton(icon=ft.icons.REPLAY_OUTLINED, on_click=self._botlist)])])
        
        self.content = ft.Column(
        controls=[self.botlist_widget])
    
    def _botlist(self, e):
        response = requests.get('https://escapepod.local:5000/api-sdk/get_sdk_info')
        if response.status_code == 200:
            json_response = json.loads(response.text)
            for bot in json_response["robots"]:
                print(f"Bot: {bot['esn']}")
                # ft.Text(f"Bot: {bot['esn']}")
                self.botlist_table.controls.append(ft.Text(value=f"Bot: {bot['esn']}"))
        else:
            print("Unable to retrieve bot list.")

        return

class WeatherAPI(ft.UserControl):
    def __init__(self, update):
        super().__init__()
        self.update = update
        self.openweathermap_form = ft.Text(value="OpenWeatherMap Form Placeholder")
        self.weatherapi_form = ft.Text(value="WeatherAPI Form Placeholder")
        self.weather_provider = ft.Container(
            content=
                ft.Dropdown(
                    icon=ft.icons.CLOUD,
                    hint_text='Select a Weather API Provider to configure',
                    options=[
                        ft.dropdown.Option("None"),
                        ft.dropdown.Option("OpenWeatherMap", data='owm'),
                        ft.dropdown.Option("WeatherAPI", data='weatherapi'),
                        ]
                    ))
        self.settings_form = self.weather_provider
        self.controls=[self.settings_form]
    
    def update_page(self,e):
        if e.control.data=='owm':
            self.settings_form.clean()
            self.settings_form.content = self.weatherapi_form
            return
        elif e.control.data=='weatherapi':
            self.settings_form.clean()
            self.settings_form.content = self.openweathermap_form
            self.update()
            return

        return
    
    

class WirepodSettings(ft.Container):
    def __init__(self, switch_page):
        super().__init__()
        self.switch_page = switch_page

        self.settingsbody = ft.Column(controls=[ft.Text("Settings Page Placeholder")])
        self.weather = ft.TextButton(
            icon=ft.icons.CLOUD, data='weather', text="Weather", on_click=self._serversettings)
        self.kgraph = ft.TextButton(
            icon=ft.icons.AUTO_GRAPH, data='knowledge_graph', text="Knowledge Graph", on_click=self._serversettings)
        self.setlang = ft.TextButton(
            icon=ft.icons.LANGUAGE, data='setlanguage', text="Set Language", on_click=self._serversettings)
        self.content = ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                self.weather,
                                self.kgraph, 
                                self.setlang,
                                ]),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                self.settingsbody
                            ]
                        )
                            ]
                        )
                    ])

    def _serversettings(self, e):
        weather_page = WeatherAPI(update=self.update)
        knowledgegraph_page = ft.Column(controls=[ft.Text("Knowledge Graph Page Placeholder")])
        setlanguage_page = ft.Column(controls=[ft.Text("Language Config Page Placeholder")])
        if e.control.data == 'weather':
            print("Retrieving weather API settings...")
            self.settingsbody.controls.clear()
            print("Retrieving Weather Page")
            self.settingsbody.controls.append(weather_page)
            self.settingsbody.update()
            return     
        elif e.control.data == 'knowledge_graph':
            print("Retrieving Knowledge Graph settings...")
            self.settingsbody.controls.clear()
            self.settingsbody.controls.append(knowledgegraph_page)
            self.settingsbody.update()
            return 
        elif e.control.data =='setlanguage':
            print("Retrieving Language settings...")
            self.settingsbody.controls.clear()
            self.settingsbody.controls.append(setlanguage_page)
            self.settingsbody.update()
            return

        return

class BotSettings(ft.Container):
    def __init__(self, switch_page):
        super().__init__()
        self.switch_page = switch_page
        self.content = ft.Text(value="Bot Settings Placeholder")

class CustomIntents(ft.Container):
    def __init__(self, switch_page):
        super().__init__()
        self.switch_page = switch_page
        self.content = ft.Column(controls=[
            ft.Text(value="Custom Intents")
        ])

class Logs(ft.Container):
    def __init__(self, switch_page):
        super().__init__()
        self.switch_page = switch_page
        self.content = ft.Text(value="Logs Placeholder")
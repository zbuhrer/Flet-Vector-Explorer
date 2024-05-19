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
        
        self.botlist_widget = ft.Container(content=ft.Text("Bot List Placeholder"))
        
        self.content = ft.Column(
        controls=[self.botlist_widget])
    
    def _botlist(self, e):
        response = requests.get('https://localhost:5000/api-sdk/get_sdk_info')

        

        if response.status_code == 200:
            json_response = json.loads(response.text)

            for bot in json_response["robots"]:
                print(f"Bot: {bot['esn']}")
                # ft.Text(f"Bot: {bot['esn']}")
                self.botlist_widget.content
        else:
            ft.Text("Error authenticating!")

        return
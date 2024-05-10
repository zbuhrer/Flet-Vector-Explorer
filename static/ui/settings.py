from flet import Container, Text

class Settings(Container):
    def __init__(self):
        super().__init__()
        self.contents = [
            Text("Settings")
            ]

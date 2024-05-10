from flet import Container, Text

class About(Container):
    def __init__(self):
        super().__init__()
        self.contents = [
            Text("About")
            ]

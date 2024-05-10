from flet import Container, Text
from static.vector_init import Synapse

class Status(Container):
    botdata = Synapse.loadbot
    
    def __init__(self):
        super().__init__()
        self.contents = [
            Text("Status"),
            Text(f"Current Bot: {self.botdata}")
            ]
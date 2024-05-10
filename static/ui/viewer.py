
from flet import Page, Tabs, Tab, Container
from flet import TextField, Column, ElevatedButton, Switch

from static.ui.chat import Chat
from static.ui.settings import Settings
from static.ui.about import About
from static.ui.status import Status


class RobotSelectorForm(Page):
    def __init__(self, serial):
        self.robot_list = []
        self.addbotform_x1 = TextField(label="Robot Name:", value="")
        self.addbotform_x2 = TextField(label="Serial Number:")
        self.addbotform_x3 = TextField(label="Behavior activation timeout (s):", value='10') # behavior_activation_timeout: int = 10
        self.addbotform_x4 = Switch(label="Enable Face Detection:", value=False) # enable_face_detection: bool = False

        # Add Robot form
        self.add_robot_form = Column([
            self.addbotform_x1,
            self.addbotform_x2,
            self.addbotform_x3,
            self.addbotform_x4,
            ElevatedButton(text="Add Robot", on_click=self.add_robot),
        ])

    def add_robot(self, e):
        # init robot
        self.robotname = self.addbotform_x1.value
        self.serial = self.addbotform_x2.value
        self.face_detection = self.addbotform_x4.value
        self.default_logging = True
        self.robotconfig = {}


        # self.robot = Robot(
        #     serial = self.serial,
        #     name = self.name,
        #     config = self.robotconfig,
        #     default_logging = self.default_logging,
        #     cache_animation_lists = True,
        #     enable_face_detection = False,
        #     estimate_facial_expression = False,
        #     enable_audio_feed = False,
        #     enable_custom_object_detection = False,
        #     enable_nav_map_feed = False,
        #     show_viewer = False,
        #     show_3d_viewer = False,
        #     )
        
        # build the robot config 
        
        print("New robot details:")
        print(f"Serial: {self.serial}")
        print(f"Name: {self.robotname}")
        print(f"Default Logging: {self.default_logging}")
        print(f"Enable Face Detection: {self.face_detection}")



class MainView(Page):
    def __init__(self):

        # Tab content 
        self.status_content = Container(Status(), padding=10)
        self.chat_content = Container(Chat(),padding=10)
        self.settings_content = Container(Settings(),padding=10)
        self.about_content = Container(About(),padding=10)

        # Tabs
        self.tab_status = Tab(text='Status',content=self.status_content)
        self.tab_chat = Tab(text='Chat',content=self.chat_content)
        self.tab_settings = Tab(text='Settings',content=self.settings_content)
        self.tab_about = Tab(text='About',content=self.about_content)
        self.tabs = Tabs(
            tabs=[
                self.tab_status,
                self.tab_chat, 
                self.tab_settings, 
                self.tab_about
            ]
        )
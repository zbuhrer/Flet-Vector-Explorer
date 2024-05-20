import flet as ft
import json, requests
import math
from math import pi
from utils.extras import *

class RemoteControlPage(ft.Container):
  def __init__(self,switch_page):
    super().__init__()
    self.expand=True
    self.switch_page = switch_page    
    self.content = ControlPanel()
    
class ControlPanel(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.dpadwidget = ft.Column(
           controls=[
                ft.Row([ft.IconButton(icon=ft.icons.ARROW_UPWARD_OUTLINED,rotate=pi/-4,tooltip='Forward'), ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT,rotate=pi/-4,tooltip='Turn Right')]),
                ft.Row([ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT,rotate=pi/-4,tooltip='Turn Left'), ft.IconButton(icon=ft.icons.ARROW_DOWNWARD_OUTLINED,rotate=pi/-4,tooltip='Backward')]),
            ])
        self.headwidget = ft.Column(
           controls=[
                ft.Row([ft.IconButton(icon=ft.icons.ARROW_UPWARD_ROUNDED)]),
                ft.Row([ft.IconButton(icon=ft.icons.ARROW_DOWNWARD_ROUNDED)])
            ])
        self.armwidget = ft.Column(
           controls=[
                ft.Row([ft.IconButton(icon=ft.icons.ARROW_UPWARD_ROUNDED)]),
                ft.Row([ft.IconButton(icon=ft.icons.ARROW_DOWNWARD_ROUNDED)])
            ])
        
        self.controlstack = ft.Row(
            expand=True,
            controls=[
                    self.dpadwidget,
                    self.headwidget,
                    self.armwidget
                    ],
            )
        self.wheel_control = None
        self.lift_head_control = None
        self.content = self.controlstack

        self.init_helper()

    def init_helper(self):
        self.dpadwidget.rotate=pi/4
        self.dpadwidget.alignment=ft.MainAxisAlignment.END
        self.headwidget.alignment=ft.MainAxisAlignment.END
        self.armwidget.alignment=ft.MainAxisAlignment.END
        self.controlstack.alignment=ft.MainAxisAlignment.SPACE_EVENLY

        
        return
        

        # self.content=ft.Column(controls=[
        #     ft.Row([
        #             ft.Text("Forward"),
        #             ft.Slider(min=0, max=100, value=50),
        #             ft.IconButton(icon=ft.icons.ARROW_UPWARD, data="mv_forward", on_click=self.move)
        #         ]),
        #     ft.Row([
        #             ft.Text("Backward"),
        #             ft.Slider(min=0, max=100, value=50),
        #             ft.IconButton(icon=ft.icons.ARROW_DOWNWARD ,data="mv_backward", on_click=self.move)
        #         ]),
        #     ft.Row([
        #             ft.Text("Left"),
        #             ft.Slider(min=0, max=100, value=50),
        #             ft.IconButton(icon=ft.icons.ARROW_LEFT, data="mv_left", on_click=self.move)
        #         ]),
        #     ft.Row([
        #             ft.Text("Right"),
        #             ft.Slider(min=0, max=100, value=50),
        #             ft.IconButton(icon=ft.icons.ARROW_RIGHT, data="mv_right", on_click=self.move)
        #         ]),
        #     ft.Row([
        #             ft.Text("Lift Up"),
        #             ft.IconButton(icon=ft.icons.BATTERY_1_BAR,data="arm_up", on_click=self.arm)
        #         ]),
        #     ft.Row([
        #             ft.Text("Lift Down"),
        #             ft.IconButton(icon=ft.icons.BATTERY_2_BAR,data="arm_down", on_click=self.arm)
        #         ]),
        #     ft.Row([
        #             ft.Text("Head Up"),
        #             ft.IconButton(icon=ft.icons.BATTERY_3_BAR, data="head_up", on_click=self.head)
        #         ]),
        #     ft.Row([
        #             ft.Text("Head Down"),
        #             ft.IconButton(icon=ft.icons.BATTERY_4_BAR, data="head_down", on_click=self.head)
        #         ])])

    def move(self, e):
        # Send API request to control robot's movement 
        pass

    def arm(self, e):
        # Send API request to control robot's arm
        pass

    def head(self, e):
        # Send API request to control robot's head
        pass
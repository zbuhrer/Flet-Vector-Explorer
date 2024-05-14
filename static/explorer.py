from flask import Flask, request

from static.vector_talk import Chatter

import io
import json
import sys
import time
import datetime
import logging
import random
import queue

import flet as ft
import anki_vector as av
from anki_vector import Robot as R
from anki_vector import util
from flask import Flask
from flask_socketio import SocketIO

from lib.event_monitor import monitor
from lib import new_flask_socket_helpers as flask_socket_helpers
from lib.animate import animate, init_animate
from lib.viewer import viewer, activate_viewer_if_enabled, create_default_image, update_state_info
from lib.remote_control import remote_control, activate_controls


app = Flask(__name__)
app.register_blueprint(animate)
app.register_blueprint(viewer)
app.register_blueprint(remote_control)

robot = None
async_mode = 'threading'
thread = None
rndID = random.randrange(1000000000, 9999999999)
os_info = ''
animation_list = ''
q = queue.Queue()
active_viewer = False
_default_camera_image = create_default_image(640, 360)

socketio = SocketIO(app, async_mode=async_mode)
flask_socketio_installed = True

app = Flask(__name__)

@app.route('/camera_control', methods=['POST'])
def camera_control():
    data = request.get_json()
    # camera control code here
    return 'OK'

@app.route('/talk', methods=['POST'])
def talk():
    chatter = Chatter()
    data  = request.get_json()
    # talk code here
    return 'OK'

@app.route('/')
def index():
    global explorer_layout
    explorer_layout = ft.Column(
        controls=[
            ft.Text("Anki Vector Explorer"),
            ft.Image(src='static/img/128.png'),
            ft.TextField(label="Remote Control", read_only=True, value="")
            ])
    return 'OK'

def run():
    args = util.parse_command_args()
    global robot

    with R(args.serial, enable_custom_object_detection=True, enable_face_detection=True) as robot:
        global animation_list
        global active_viewer
        global os_info

        os_info = robot.conn.name + ',' + robot.conn.host + ',' + robot.get_version_state().os_version
        animation_list = init_animate(robot) # list of animations
        active_viewer = activate_viewer_if_enabled(robot) # camera and keyboard controls
        monitor(robot, q) # event monitor
        activate_controls(robot) # game controller

        log = logging.getLogger('wekzeug')
        log.setLevel(logging.ERROR)
        flask_socket_helpers.run_flask(socketio, app)

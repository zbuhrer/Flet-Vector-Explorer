import json
from anki_vector.robot import Robot as R, AsyncRobot as AR

class Synapse(R):
    def __init__(self,
                 serial: str,
                 name: str,
                 config: dict,
                 ):
        current_robot_name = name
        currentbot_serial = '00702f96'
        serial = currentbot_serial

        self.currentbot = self.loadbot(self, serial)
        self.config = config

        
    def getcurrentbot(self):
        current_config = self.loadbot(self.serial)
        return current_config

    def json_controller(self):
        self.robot_settings = {}
        return self.robot_settings
        
    def loadbot(self, serial):
        self.serial = serial
        
        try:
            with open("robots.json", "r") as f:
                robot_settings = json.load(f)
                serial = list(robot_settings())[0]
        except FileNotFoundError:
            print("No robots.json found. Creating file.")
            # create a new JSON file with the layout already programmed for an example. 
            example_robot = {"bots": [
                {"serial": '00000', 
                "name": 'Example Bot',
                "config": {},
                "default_logging": True,
                "behavior_activation_timeout": 10,
                "cache_animation_lists": True,
                "enable_face_detection": False,
                "estimate_facial_expression": False,
                "enable_audio_feed": False,
                "enable_custom_object_detection": False,
                "enable_nav_map_feed": False
                }
            ]}
            
            with open("robots.json", "w") as f:
                json.dump(example_robot, f)
            print("Created new robots.json file.")
            return
            
        except Exception as e:
                print(f"Error opening robots.json: {str(e)}")

        for bot in self.robot_settings["bots"]:
            if bot["serial"] == self.serial:
                self.robot_data = {
                    "serial": bot["serial"],
                    "name": bot["name"],
                    "ip": bot["ip"],
                    "config": bot["config"],
                    "default_logging": bot["default_logging"],
                    "behavior_activation_timeout": bot["behavior_activation_timeout"],
                    "cache_animation_lists": bot["cache_animation_lists"],
                    "enable_face_detection": bot["enable_face_detection"],
                    "estimate_facial_expression": bot["estimate_facial_expression"],
                    "enable_audio_feed": bot["enable_audio_feed"],
                    "enable_custom_object_detection": bot["enable_custom_object_detection"],
                    "enable_nav_map_feed": bot["enable_nav_map_feed"],
                    "show_viewer": bot["show_viewer"],
                    "show_3d_viewer": bot["show_3d_viewer"],
                    }
            else:
                print(f"Check robots.json for formatting issues.")
                pass
            return self.robot_data

    # def addbot(self,serial):
    #     global current_robot_serial
    #     current_robot_serial = serial
    #     try:
    #         Synapse.__init__(self, serial, self.name, self.config)
    #     except Exception as e:
    #         print(f"Error: {e}")

    def changebot(self, serial):
        # call and set the global variable to the serial passed to changebot()
        global current_robot_serial
        current_robot_serial  = serial

        try:
            config = Synapse.loadbot(self, serial)
            return config
        except Exception as e:
            print(f"Error: {e}")
        pass

    async def talk(self, serial, text: str = "") -> None: 
        with Synapse(serial, name, config) as robot:
            print(f"Say '{text}'...")
            robot.behavior.say_text(text)

if __name__ == "__main__":
    botdata = Synapse.loadbot
    print(botdata)
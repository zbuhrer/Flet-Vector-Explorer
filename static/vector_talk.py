import argparse
import asyncio

from anki_vector import Robot

ANKI_ROBOT_SERIAL = '00702f96'

currentbot = None
currentbot_name = ''
currentbot_serial = ANKI_ROBOT_SERIAL

class Chatter(Robot):
    def __init__(self): 
        self.serial = currentbot_serial
        self._robot = None
        self._bot = None
        self._chatter = None
        self._last_message = ""
        self._is_running = False
        self._is_connected = False
        self._is_waiting = False
        self._is_listening = False
        self._is_speaking = False
        self._is_thinking = False
        self._is_sleeping = False

    async def talk(self, serial=currentbot_serial, text: str = "") -> None: 
        with Robot(serial) as r:
            print(f"Say '{text}'...")
            r.behavior.say_text(text)

def main ():
    parser = argparse.ArgumentParser(description="Send messages to Vector")
    parser.add_argument('-t', '--text', help = 'Send message to robot')
    args = parser.parse_args()

    chatter = Chatter()

    if not args.text:
        while True:
            user_input = input("(q to quit) >: ")
            if user_input.lower() == 'q':
                break
            asyncio.run(chatter.talk(text = user_input))
    else: 
        asyncio.run(chatter.talk(args.text))

if __name__ == "__main__": 
    main()
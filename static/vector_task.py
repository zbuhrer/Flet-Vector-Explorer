from anki_vector import status as vector_status
import asyncio

def main():
        print(asyncio.run(get_current_task_status()))

async def get_current_task_status():
        current_task = vector_status.RobotStatus.__get()
        return current_task

if __name__ == "__main__":
        main()
from pyrogram import Client
import os
from dotenv import load_dotenv
load_dotenv()


class OD(Client):
    def __init__(self,):
        super().__init__("session_name",
                         bot_token=os.environ.get("BOT_TOKEN"),
                         )

    async def start(self):
        await super().start()
        print(f"{self.get_chat}")

    async def stop(self, *args):
        await super().stop()

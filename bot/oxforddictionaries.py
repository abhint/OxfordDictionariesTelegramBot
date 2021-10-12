from pyrogram import Client
import os
from dotenv import load_dotenv
load_dotenv()


class OD(Client):
    def __init__(self,):
        super().__init__("session_name",
                         api_id=os.environ.get("API_ID"),
                         api_hash=os.environ.get("API_HASH"),
                         bot_token=os.environ.get("BOT_TOKEN"),
                         )

    async def start(self):
        await super().start()
        print(f"{await self.get_chat}")

    async def stop(self, *args):
        await super().stop()

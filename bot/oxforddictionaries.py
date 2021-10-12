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
                         plugins={
                             'root': 'bot/plugins'
                         }
                         )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.me = me.username
        print(f"{me.username} is Online!")

    async def stop(self, *args):
        print(f"\n{self.me} is Offline!")
        await super().stop(*args)

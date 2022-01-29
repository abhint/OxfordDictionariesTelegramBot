from pyrogram import Client
from bot import (API_ID,
                 API_HASH,
                 BOT_TOKEN,
                 LOGGER)


class OD(Client):
    def __init__(self,):
        super().__init__('session_name',
                         api_id=API_ID,
                         api_hash=API_HASH,
                         bot_token=BOT_TOKEN,
                         plugins=dict(root='bot/plugins')
                         )
        self.me = None
        self.logger = LOGGER

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.me = me.username
        self.logger(__name__).info(f"{me.username} is Online!")

    async def stop(self, *args):
        self.logger(__name__).info(f"{self.me} is Offline!")
        await super().stop(*args)

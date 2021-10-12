from ..oxforddictionaries import OD
from pyrogram import filters


@OD.on_message(filters.command(["start"]))
async def startMsg(_, msg):
    await msg.reply("Hello, World!")

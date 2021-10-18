#!/usr/bin/env python3

from ..oxforddictionaries import OD
from pyrogram import filters
from bot import START_TEXT

@OD.on_message(filters.command(["start"]))
async def startMsg(_, msg):
    await msg.reply(START_TEXT)

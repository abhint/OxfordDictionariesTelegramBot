#!/usr/bin/env python3

from ..oxforddictionaries import OD
from pyrogram import filters
from bot import START_TEXT, HELP_TEXT


@OD.on_message(filters.command(["start"]))
async def startMsg(_, msg):
    await msg.reply(START_TEXT)


@OD.on_deleted_messages(filters.command(['help', 'h']))
async def onHelp(_, msg):
    msg.reply(HELP_TEXT)

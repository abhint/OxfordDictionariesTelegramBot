#!/usr/bin/env python3

from ..oxforddictionaries import OD
from pyrogram import filters
from bot import START_TEXT, HELP_TEXT


@OD.on_message(filters.command(["start"]))
async def start_msg(_, msg):
    await msg.reply(START_TEXT)


@OD.on_message(filters.command(['help', 'h']))
async def on_help(_, msg):
    await msg.reply(HELP_TEXT)

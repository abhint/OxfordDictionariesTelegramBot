#!/usr/bin/env python3

from pyrogram import filters
from ..oxforddictionaries import OD
from ..helpers.oxforddic import oxfordRequests
from bot import LOGGER


@OD.on_message(filters.private)
async def words(client, msg):
    msg_words = str(msg.text)
    LOGGER(__name__).info(f'{msg.chat.id} - {msg_words}')
    definitions, word, audioFile = await oxfordRequests(msg_words)
    user_text = "\n".join(definitions)
    await msg.reply(f"Definitions of **{word}**\n\n{user_text}")
    await client.send_audio(chat_id=msg.chat.id, audio=audioFile, caption=word)

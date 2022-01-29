#!/usr/bin/env python3

from pyrogram import filters
from ..oxforddictionaries import OD
from ..helpers.oxforddic import oxford_requests
from bot import LOGGER


@OD.on_message(filters.private)
async def words(client, msg):
    msg_words = str(msg.text)
    LOGGER(__name__).info(f'{msg.chat.id} - {msg_words}')
    definitions, word, audioFile, example_text = await oxfordRequests(msg_words, msg)
    if definitions:
        user_text = "\n".join(definitions)
        user_example_text = "\n".join(example_text)
        await msg.reply((f"Definitions of **{word}**\n"
                        f"\n{user_text}\n"
                        f"\n**Examples of {word}:**\n\n{user_example_text}"))
        await client.send_audio(chat_id=msg.chat.id, audio=audioFile, caption=word)

from ..oxforddictionaries import OD
from pyrogram import filters
from ..helpers.oxforddic import oxfordRequests


@OD.on_message()
async def words(client, msg):
    msg_words = str(msg.text)
    definitions, word, audioFile = await oxfordRequests(msg_words)
    ff = "\n".join(definitions)
    await msg.reply(f"Definitions of **{word}**\n\n{ff}")
    await client.send_audio(chat_id=msg.chat.id, audio=audioFile, caption=word)

#!/usr/bin/env python3

import requests
import json
from pyrogram.types import Message
from bot import (APP_ID,
                 APP_KEY,
                 ERROR_404,
                 LOGGER)


async def oxford_requests(word_id: str, msg: Message):
    app_id = APP_ID
    app_key = APP_KEY
    language = 'en-gb'
    strict_match = 'false'
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'+language+'/' + \
        word_id.lower() + '?strictMatch='+strict_match
    logger = LOGGER(__name__)
    logger.info(f"{url}")
    definitions = []
    example_text = []
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    json_dumps = json.dumps(r.json())
    json_loads = json.loads(json_dumps)
    try:
        audio_file = json_loads['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
        word = json_loads['word']
        for re in json_loads['results']:
            for lex in re['lexicalEntries']:
                definitions.append(f"**{lex['lexicalCategory']['text']}:**")
                for ent in lex['entries']:
                    for sen in ent['senses']:
                        if 'examples' in sen:
                            for ex in sen['examples']:
                                example_text.append(f"**__{ex['text']}__**")
                        for def_ in sen['definitions']:
                            definitions.append(f"{def_}")
        return definitions, word, audio_file, example_text
    except KeyError as e:
        logger.warning(f"{e} - {word_id}")
        await msg.reply(ERROR_404)
        word = None
        audio_file = None
        return definitions, word, audio_file, example_text

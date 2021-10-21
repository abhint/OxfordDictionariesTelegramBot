#!/usr/bin/env python3

import requests
import json
from bot import (APP_ID,
                 APP_KEY,
                 ERROR_404,
                 LOGGER)


async def oxfordRequests(word_id: str, msg):
    app_id = APP_ID
    app_key = APP_KEY
    language = 'en-gb'
    strictMatch = 'false'
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'+language+'/' + \
        word_id.lower() + '?strictMatch='+strictMatch
    logger = LOGGER(__name__)
    logger.info(f"{url}")
    definitions = []
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    json_dumps = json.dumps(r.json())
    json_loads = json.loads(json_dumps)
    try:
        audioFile = json_loads['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
        word = json_loads['word']
        for re in json_loads['results']:
            for lex in re['lexicalEntries']:
                definitions.append(f"**{lex['lexicalCategory']['text']}:**")
                for ent in lex['entries']:
                    for sen in ent['senses']:
                        for def_ in sen['definitions']:
                            definitions.append(f"{def_}")
        return definitions, word, audioFile
    except KeyError as e:
        logger.warning(e)
        await msg.reply(ERROR_404)
        audioFile = None
        word = None
        return definitions, audioFile, word

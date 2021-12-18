from telethon import TelegramClient
from decouple import config
import logging
import time

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)

with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
   string = client.session.save()
   
client.start() 

async def main():
        await client.connect()   
   
client.loop.run_until_complete(main())


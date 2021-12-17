from telethon import TelegramClient
from decouple import config
import logging
import time

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

bot = TelegramClient('ub', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

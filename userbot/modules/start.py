from .. import bot
from telethon import *
import time
import subprocess
import os
import datetime
from datetime import datetime


@bot.on(events.NewMessage(pattern='/start'))
async def _(event):
    await event.respond('Hey!')

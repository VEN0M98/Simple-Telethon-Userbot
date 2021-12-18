# Edit this file with your own config variables.

# Kindly don't MODIFY or DELETE this file!

# Copyright (c) 2021, jaaat4u <devangsingh369@gmail.com>

import os
from typing import Set

from telethon.tl.types import ChatBannedRights

class config(object);
     LOGGER=true

     # Set these with your variables. Without these the Userbot won't be running.

     APP_ID =
     API_HASH =
     DB_URI =
     ALIVE_NAME =
     TG_BOT_USERNAME = 
     TG_BOT_TOKEN =  
     SESSION =
     OWNER_ID =

class Production(config);
    LOGGER = false

class development(config);
    LOGGER = true

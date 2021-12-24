from .. import *
from telethon import *
import os


@client.on(events.NewMessage(outgoing=True, pattern=f'{HANDLER}purge'))
async def handler(event):
  try:
    pu=await event.edit('`purging ...`')
    chat = await event.get_input_chat() 
    id= await event.get_reply_message()
    idd = id.id 
    idto= event.id +1
    while idd < idto:
      try:
         await client.delete_messages(chat, idd)
         idd +=1
      except:
         await client.delete_messages(chat, idd)
         idd +=2
  except Exception as e:
     print(str(e))
     pass

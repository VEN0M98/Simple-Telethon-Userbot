


@bot.on(events.NewMessage(pattern='/start'))
async def _(event):
    await event.respond('Hey!')

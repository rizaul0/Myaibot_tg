from telethon import events
from .. import bot, openai_key
import asyncio,openai

openai.api_key = openai_key

@bot.on(events.NewMessage(incoming = True, pattern = "(?i)/ai"))
async def _chatgpt(event):
  if event.sender_id == int(1214763812):
    await event.reply("Hello boss")
  else:
    await event.reply("Hello user")
 

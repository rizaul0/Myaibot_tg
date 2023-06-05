from telethon import TelegramClient 
import logging
import time

openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6046026747:AAFjZR1Ercq8EMboP5wIYhN4dhT2u2c-Uo8"

bot = TelegramClient("infinix",api_id,api_hash).start(bot_token=bot_token)
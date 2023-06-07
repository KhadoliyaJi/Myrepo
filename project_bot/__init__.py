from telethon import TelegramClient

import logging

import time

openai.my_api_key = openai_key
api_id = "27415472"
api_hash = "33a013ead607b21bd2b77970b1b181e5"
bot_token = "5871165882:AAFWx0ESawBJih8G4RQ6IgW_v4d5Cw2Arv4"

tgbot = TelegramClient("project_bot",api_id,api_hash).start(bot_token = bot_token)
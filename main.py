import discord
import os
import logging
import random
from discord.ext import commands
from dotenv import load_dotenv
from quotes import QUOTES
from trigger_words import TRIGGER_WORDS

load_dotenv()
token = os.getenv('TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    words = message.content.lower().split()
    if any(word in words for word in TRIGGER_WORDS):
        await message.channel.send(random.choice(QUOTES))

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
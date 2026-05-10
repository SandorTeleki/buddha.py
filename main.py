import discord
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

#client = discord.Client(intents=intents)

#@client.event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}!')

# #@client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
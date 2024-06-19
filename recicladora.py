import discord
from discord.ext import commands
import random
import os
import requests 


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

# Define intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Crea un bot con el prefijo deseado
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

# Evento on_ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')




bot.run('----')

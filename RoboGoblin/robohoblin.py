# RoboGoblin is a bot created for quickly sorting and arranging known professions into a list.
import os
import discord
from dotenv import load_dotenv
#from functions import *
from profession import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    #print(f"{message.author}: {message.content}")
    if message.author == client.user:
        return
    
    if message.content.startswith('RG.setup'):
        content = list(message.content.split('\n'))

        for item in content:
            if item[0] == '!':
                profession = Profession(item[1:])
            elif item[0] == '@':
                profession.add_category(item[1:])
            elif item[0] == '-':
                profession.add_pattern(item[1:])
        
        print(profession.print_category('Mail'))
        

client.run(TOKEN)
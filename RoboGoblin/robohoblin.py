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
        
        # print(profession.print_category('Mail'))
        # print(profession.get_all_categories())

        embed = discord.Embed(title=f"{message.author.name}'s {profession.return_name()}", color=0x00ff00)

        for item in profession.get_all_categories():
            embed.add_field(name=item, value=profession.print_category(item), inline=True)

        # embed.add_field(name="Developer", value="devel", inline=True)
        # embed.add_field(name="Techie", value="techie", inline=True)
        

client.run(TOKEN)
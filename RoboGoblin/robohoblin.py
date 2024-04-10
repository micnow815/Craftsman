# RoboGoblin is a bot created for quickly sorting and arranging known professions into a list.
import os
import discord
from dotenv import load_dotenv
from functions import *
from profession import *
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True




message_parts = []
is_processing = False

client=commands.Bot(command_prefix="RG.", intents=intents)

class DynamicButton(discord.ui.Button):
    def __init__(self, label, embed):
        super().__init__(label=label)
        self.embed = embed
    
    async def callback(self, interaction):
        await interaction.response.send_message(embed=self.embed, ephemeral=True)

@client.command()
async def start_processing(ctx):
    global is_processing
    global message_parts
    is_processing = True
    message_parts.append(ctx.message.content)


@client.command()
async def setup(ctx):
    global message_parts
    global is_processing
    if len(message_parts) != 0:
        is_processing = False
        view = discord.ui.View()
        full_message = '\n'.join(message_parts)
        content = full_message.split('\n')
        for item in content:
            if item[0] == '!':
                profession = Profession(item[1:])
            elif item[0] == '@':
                profession.add_category(item[1:])
            elif item[0] == '-':
                profession.add_pattern(item[1:])

        button_info = []
        embed = discord.Embed(title=f"{ctx.author.display_name}'s {profession.return_name()}", color=0x0070DE)
        for item in profession.get_all_categories():
            embed.add_field(name=item, value=f'Patterns: {profession.patterns_in_category(item)}', inline=True)
            button_info.append((item, discord.Embed(title=item, description=list_to_string(profession.print_category(item)))))

        for label, message in button_info:
            view.add_item(DynamicButton(label, message))

        await ctx.send(embed=embed, view=view)
        message_parts = []

    else:
        return
    
@client.command
async def clear_cache():
    global message_parts
    global is_processing
    message_parts = []
    is_processing = False

@client.event

async def on_message(message):
    global message_parts
    global is_processing

    if is_processing == True:
        message_parts.append(message.content)

    if (message.content.startswith(client.command_prefix) and message.author != client.user) or is_processing == True:
        await message.delete()

    await client.process_commands(message)

client.run(TOKEN)
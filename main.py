import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from keep_alive import keep_alive


load_dotenv()

TOKEN = os.environ.get('TOKEN')
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

keep_alive()  # starts the webserver so we can keep the bot up and running


client.load_extension("modules.general_cmds")

client.run(TOKEN)
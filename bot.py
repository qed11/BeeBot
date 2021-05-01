import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
client.run('ODE1MzkxMTU4NTU2NTU3MzEz.YDruMQ.ySQIXxLua59wlv3Pcu3RWVJbU3Y')
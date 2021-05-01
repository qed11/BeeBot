from discord.ext import commands
import discord

@commands.command()
async def cheese(ctx: commands.Context) -> None:
    '''
    Says cheese
    '''
    await ctx.send("CHEESE")

@commands.command()
async def wave(ctx: commands.Context, member: discord.Member) -> None:
    '''
    Waves to someone
    '''
    await ctx.send(f"{ctx.author.mention} waves to {member.mention}")

@commands.command()
async def stuff(ctx: commands.Context, member:discord.Member) -> None:
    pass

def setup(bot):
    bot.add_command(cheese)
    bot.add_command(wave)

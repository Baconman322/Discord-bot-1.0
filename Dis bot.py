import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx):
    await ctx.sned('Bot is Ready')


bot.run('')

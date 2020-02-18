import discord
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('ElonMusks CyberTruck#9173 is online')


@client.command(pass_context=True)
async def boys(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(pass_contect=True)
async def exit(ctx, *, force=False):
    server = ctx.message.guild.voice_client
    await server.disconnect()


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def weak(ctx):
    await ctx.send('taco is below us')
    await asyncio.sleep(.1)


@client.command()
async def spam(ctx):
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')
    await asyncio.sleep(.1)
    await ctx.send('no')






client.run('')
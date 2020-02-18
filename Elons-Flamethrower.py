import discord
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('ElonMusks Flamethrower#0551 is online')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(pass_contect=True)
async def exit(ctx, *, force=False):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command(pass_context=True)
async def boys(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
async def weak(ctx):
    await ctx.send('taco is below us')
    await asyncio.sleep(.1)

@client.command()
async def mute(ctx, member : discord.Member = None):

    if member is None:
        await ctx.send('please pass in a valid user')
        return

    await member.add_roles('Muted')

    await ctx.send(f'{str(member)} was muted!')

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
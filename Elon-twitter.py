import discord
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('ElonMusks Twitter#6962 is online')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.command()
async def weak(ctx):
    await ctx.send('taco is below us')
    await asyncio.sleep(.1)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.event
async def on_guild_role_update(member):
    print (f'{member} role has been updated.')

@client.event
async def on_member_remove(member):
    print (f'{member} has left the server')

@client.event
async def on_guild_channel_create():
    print (f'{role} has been created')

@client.command()
async def members(ctx):
    await ctx.send.user()

@client.command(pass_contect=True)
async def exit(ctx, *, force=False):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command(pass_context=True)
async def boys(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


@client.event
async def on_message(message):
    bad_words = []

    for word in bad_words:
        if message.content.count(word) > 0:
            print("someone is disappointing there parents")
            await message.channel.purge(limit=1)


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
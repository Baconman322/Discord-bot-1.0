import discord
from discord.ext import commands
import random
from discord.ext.commands import Bot
import asyncio
import logging
client = commands.Bot(command_prefix = '.')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.info(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
    print('ElonMusk Bot#1483 is online')

@client.command(aliases=['hullo', 'hi'])
async def _hello(ctx):
    await ctx.send('Im above your petty attempts to make friends.')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(pass_context=True)
async def boys(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(pass_contect=True)
async def exit(ctx, *, force=False):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def bot(ctx):
    await ctx.send(f'{bot}')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def shiny(ctx):
    respone = [
        "Yes",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
        "no",
    ]
    await ctx.send(f'{random.choice(respone)}')



@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clearall(ctx):
    await ctx.channel.purge()

@client.command()
async def allmembers(ctx, members):
    await ctx.send(get_all_members())

@client.command()
async def owner(ctx):
    await ctx.send(f'@Capitalist Bacon#2432 created me')

@client.command()
async def nuke(ctx):
    await ctx.channel.purge()
    await asyncio.sleep(5)
    await ctx.channel.purge()
    await asyncio.sleep(5)
    await ctx.channel.purge()
    await asyncio.sleep(5)
    await ctx.channel.purge()
    await asyncio.sleep(5)
    await ctx.channel.purge()
    await asyncio.sleep(5)
    await ctx.channel.purge()
    await asyncio.sleep(5)
    await ctx.channel.purge()



@client.command()
async def weak(ctx):
    await ctx.send('taco is below us')
    await asyncio.sleep(.1)

@client.command()
async def t(ctx, *, mention):
    await ctx.send(f'Screw {mention}')

@client.command()
async def dm(ctx):
    await ctx.author.send('screw off')

@client.command()
async def dm(ctx, *, mention, *, message):
    if await ctx.mention.send(f'{message}')



@client.command()
async def dm(ctx):
    await ctx.send('screw off')

client.run('')

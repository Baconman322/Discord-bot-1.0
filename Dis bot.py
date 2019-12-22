import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix = '.')





@client.event
async def on_ready():
    print('Bot ElonMusk Bot#1483 is online')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remover(member):
    print (f'{member} has left the server')

@client.command(aliases=['hullo', 'hi'])
async def _hello(ctx):
    await ctx.send('Im above your petty attempts to make friends.')

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

client.run('')

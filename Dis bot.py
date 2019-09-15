import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

Client = commands.Bot(command_prefix='.')


@Client.event
async def on_ready():
    print('bot is ready')

@Client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
@Client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@Client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(Client.latency * 1000)}ms')



@Client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['Yes'
                 'No'
                 'Maybe'
                 'I dont care, figure it out your self'
                 'It is certain.'
                 'It is decidedly so.'
                 'Without a doubt.'
                 'Yes - definitely.'
                 'You may rely on it.'
                 'As I see it, yes.'
                 'Most likely.'
                 'Outlook good.'
                 'Yes.'
                 'Signs point to yes.'
                 'Reply hazy, try again.'
                 'Ask again later.'
                 'Better not tell you now.'
                 'Cannot predict now.'
                 'Concentrate and ask again.'
                 'Don\'t count on it.'
                 'My reply is no.'
                 'My sources say no.'
                 'Outlook not so good.'
                 'Very doubtful.' ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@Client.command()
async def suckit(ctx):
    await ctx.send(f'shut up peasant.')

@Client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@Client.command()
async def hello(ctx):
    await ctx.send(f'Suck my balls')


Client.run('')

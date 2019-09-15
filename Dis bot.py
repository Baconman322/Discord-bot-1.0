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


Client.run('NjIyNjA3NDM1MTYwNjE2OTYw.XX4VGQ.00j805jDFJQqlM__-GCoU4IcJwk')

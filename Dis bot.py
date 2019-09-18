import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import logging

Client = commands.Bot(command_prefix='.')

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.member)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)


@Client.command()
async def who(ctx):
    await ctx.send(ctx.author)

@Client.command()
async def Slap(ctx, *, reason: Slapper):
    await ctx.send(reason)


@Client.command()
async def repeat(ctx, *, arg):
    await ctx.send(arg)

@Client.event
async def on_ready():
    commands.check(ctx)
    print('done')

@Client.event
async def add_cog(ctx):
    print('cog')


@Client.event
async def on_ready():
    print('bot is ready')


@Client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@Client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


@Client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.ban()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.disciminatior) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.name}#{user.mention}')
            return

@Client.event
async def on_raw_bulk_message_delete(payload):
    print('messages deleted')


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
async def clearall(ctx, amount=100000):
    await ctx.channel.purge(limit=amount)


@Client.command()
async def hello(ctx):
    await ctx.send('Suck my balls')


# Anti Spam

@Client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)


Client.run()

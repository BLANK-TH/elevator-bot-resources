import discord
import math
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
from random import choice,randint
import asyncio

client = commands.Bot(command_prefix = 's!')
df = "Elevator Server Bot Ver.1.0.0 Developed By: Kanade Tachibana"
game = cycle(["A Bot for the Elevator Discord Server!",'Developed By: Kanade Tachibana','Use s!help to see my commands!'])
hc = 0x8681bb
client.remove_command('help')

async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Developed by Kanade Tachibana'))
    change_game.start()
    print("Bot is ready.")

@tasks.loop(seconds=10)
async def change_game():
    await client.change_presence(activity=discord.Game(next(game)))

@client.event
async def on_message(message):
    if 'is now level' in message.content.lower() and message.author.id == 365975655608745985:
        embed = discord.Embed(
            description="STFU POKECORD!",
            colour=hc
        )
        embed.set_footer(text=df)
        await message.delete()
        msg = await message.channel.send(embed=embed)
        await msg.delete(delay=10)
    elif len(message.embeds) >= 1:
        for em in message.embeds:
            try:
                if 'is now level' in em.title.lower() or 'level' in em.description.lower():
                    embed = discord.Embed(
                        description="STFU POKECORD!",
                        colour=hc
                    )
                    embed.set_footer(text=df)
                    await message.delete()
                    msg = await message.channel.send(embed=embed)
                    await msg.delete(delay=10)
            except:
                pass
    if 'niger' in message.content.lower():
        embed = discord.Embed(
            description=f"{message.author.mention} the N word is forbidden! Please don't say it. This message will self destruct in 30 seconds!",
            colour=hc
        )
        embed.set_footer(text=df)
        await message.delete()
        msg = await message.channel.send(embed=embed)
        await msg.delete(delay=30)
    await client.process_commands(message)

@client.command()
async def help(ctx,page='1'):
    help_embed = discord.Embed(
        title='Help',
        description="Here are the commands for the Elevator Discord Bot:",
        colour=hc
    )
    help_embed.set_footer(text=df)
    if page == '1':
        help_embed.add_field(name='s!help <page number>',
                             value='Responds with the page your looking at right now!',
                             inline=False
                             )
        help_embed.add_field(name='s!test',
                             value='Responds with a message if the bot is online!',
                             inline=False
                             )
        help_embed.add_field(name='s!pfp <user> | s!profile <user> | s!avatar <user>',
                             value='Responds the mentioned users profile picture!',
                             inline=False
                             )
        #5 more
        help_embed.add_field(name='Page Number', value='1/1')
    else:
        error_embed = discord.Embed(title='Invalid Page Number',colour=discord.Colour.red())
        error_embed.set_image(url='https://i.imgur.com/XgqWMei.jpg')
        await ctx.message.channel.send(embed=error_embed)
        return
    await ctx.message.channel.send(embed=help_embed)

@client.command()
async def test(ctx):
    embed = discord.Embed(
        title="The bot works fine!",
        colour=hc
    )
    embed.set_footer(text=df)
    await ctx.channel.send(embed=embed)

@client.command(pass_context=True, aliases=['pfp','profile','avatar'])
async def _avatar(ctx, member: discord.Member='None'):
    if member == "None":
        member = ctx.message.author
    a_embed = discord.Embed(
        title=f"{member.display_name}'s Avatar/Profile Picture",
        colour=hc
    )
    a_embed.set_footer(text=df)
    a_embed.set_image(url=f'{member.avatar_url}')

    await ctx.message.channel.send(embed=a_embed)

@client.command()
async def mock(ctx,*,phrase:str):
    mock = ''
    for x in phrase:
        if x == ' ':
            mock += ' '
            continue
        rand = randint(1,2)
        if rand == 1:
            mock += x.upper()
            continue
        mock += x.lower()
    if 'theodore' in phrase.lower() or 'kanade' in phrase.lower():
        mock = f"How dare you insult my owner. {ctx.message.author.mention} go f*ck yourself!"
    embed = discord.Embed(
        title="Here is your mocking sentence",
        description=mock,
        colour=hc
    )
    embed.set_footer(text=df)
    embed.set_image(url='https://i.imgur.com/qDhQKQb.gif')
    if 'theodore' in phrase.lower() or 'kanade' in phrase.lower():
        embed.set_image(url='https://nationalpostcom.files.wordpress.com/2019/06/flip-2.png?w=780')

    await ctx.message.channel.send(embed=embed)

client.run('Njk5Njc3MTA4NjA3MTIzNTQ4.XpX3HQ.hIfoh4Q6KzH52D25KYR-QGNMl8k')
import discord
import math
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
from random import choice,randint
import asyncio

client = commands.Bot(command_prefix = 's!')
df = "Elevator Server Bot Ver.1.0.2 Developed By: Kanade Tachibana"
game = cycle(["A Bot for the Elevator Discord Server!",'Developed By: Kanade Tachibana','STFU Pokecord with your annoying level up messages!','Use s!help to see my commands!',df.replace(" Developed By: Kanade Tachibana","")])
hc = 0x8681bb
client.remove_command('help')

@client.event
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
        help_embed.add_field(name='s!mock <phrase>',
                             value='Responds with your phrase in weird capitalization!',
                             inline=False
                             )
        #4 more
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

@client.command(aliases=['pickup','pickupline','pl'])
async def _pickuplines(ctx):
    lines = [
        'Hey did you hear about the restaurant on the moon? The food was great but it had no atmosphere. -Jasmine',
        "If i was a gardener, I'd put our tu-lips together. -Jasmine",
        "I'm sorry, were you talking to me? (No) Well then, please start :) - Megan",
        "I'm not a photographer but I can picture me and you together - Megan",
        "Did your licenses get suspended for driving these guys/girls crazy? - Megan",
        "If you were words on a page, it'd be fine print - Megan",
        "Do you believe in love at first sight or should I walk past you again? -Jasmine",
        "Are you a bank loan? Because you've got my interest. -Jasmine",
        "Are you an alien? Because there's nothing like you on Earth (This can technically be an insult but whtevr) - Megan",
        "If nothing lasts forever, will you be my nothing? - Megan",
        "Hey you're pretty and I'm cute, together we'd be pretty cute ;) - Megan",
        "Did you just come out of the oven because WOO you're hot - Megan",
        "Are you a dictionary? Because you add meaning to my life - Megan",
        "Can I follow you home? Because my parents told me to always follow my dreams - Megan",
        "Feel my shirt. It's made of boyfriend/girlfriend material - Megan",
        "What's on this menu? Me 'N' U - Megan",
        "If I could change one thing about you it'd be to..... change your last name - Megan",
        "Are you my phone charger? Because I'd die without you - Megan",
        "Thank god I brought my library card! Because I am totally checking you out - Megan",
        "I'm studying to become a historian. I'm especially interested in a date (The only history joke I'd ever use) - Megan",
        "Could you please grab my arm so I can tell my friends I've been touched my an angel? - Megan",
        "There must be something wrong with my eyes because I can't take my eyes off you - Megan",
        "Do you have an extra heart? Because you just stole mine :( - Megan",
        "Whoever said Disney Land is the happiest place on Earth. H A H A clearly they haven't stood beside you - Megan",
        "Is there an airport near by or is my heart taking off - Megan",
        "I must be in a museum because you're a work of art ! - Megan",
        "Hi, I'm Microsoft. Can I crash at your place tonight? - Megan",
        "Did you invent the airplane? Because you seem just Wright - Megan",
        "Are you religious? Because you're the answer to all my prayers - Megan",
        "Can I tie your shoes? Because I don't want you falling for anyone else - Megan',"
        "If I can rearrange the alphabet, I'd put U and I together <3 - Megan",
        "Are you a magician because whenever I look at you, you make everyone else disappear! - Megan",
        "I'm lost, can you give me directions to your heart? - Megan",
        "Are you a magnet? Because you're attracting me from over -here!! - Megan",
        "HELP MY PHONES NOT WORKING! IT DOESN'T HAVE YOUR NUMBER - Megan",
        "Are you a camera? Because I smile at you whenever I see you - Megan",
        "Are you a parking ticket because you got fine written all over you - Megan",
        "CALL THE COPS! IT'S A CRIME TO STEAL MY HEART - Megan",
        "Are you French? Because Eiffel for you - Megan",
        "Is your dad a boxer? Because you're a knockout! - Megan",
        "I seem to have lost my number, may i have yours? - Megan",
        "Is it hot in here? Or is it just you.",
        "Are you Google? Because you are all I've been searching for - Megan",
        "Are you a phaser from Star Trek? Because you're set to stun - Megan"
    ]
    line = choice(lines)
    embed = discord.Embed(
        title=f"{ctx.message.author.name} here is your pickup line.",
        description=line,
        colour=hc
    )
    embed.set_footer(text=df)
    embed.set_image(url='https://g2x4w9d4.stackpathcdn.com/wp-content/uploads/2017/02/cheesy.gif')

    await ctx.message.channel.send(embed=embed)

client.run('Njk5Njc3MTA4NjA3MTIzNTQ4.XpX3HQ.hIfoh4Q6KzH52D25KYR-QGNMl8k')
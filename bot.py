import discord
import math
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
from random import choice,randint
from random_word import RandomWords
from PyDictionary import PyDictionary
from unit_converter.converter import converts
from googlesearch import search
from googletrans import Translator
from difflib import SequenceMatcher
from deck_of_cards import deck_of_cards
import urllib
import urllib.request
import json
import asyncio
import arrow
import typing
import requests

client = commands.Bot(command_prefix = 's!')
df = "Elevator Server Bot Ver.14.37.105 Developed By: BLANK"
game = cycle(["A Bot for the Elevator Discord Server!",'Developed By: BLANK','STFU Pokecord with your annoying level up messages!','Use s!help to see my commands!',df.replace(" Developed By: BLANK","")])
hc = 0x8681bb
pastebin_api_key = 'b16274a8e8a31de6671bcb6329528c24'
pastebin_user_key = '33868e180241dca1b863695603b73fc6'
pastebin_url = 'https://pastebin.com/api/api_post.php'
client.remove_command('help')
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Developed by BLANK'))
    change_game.start()
    print("Bot is ready.")

@tasks.loop(seconds=10)
async def change_game():
    await client.change_presence(activity=discord.Game(next(game)))

@client.event
async def on_message(message):
    if 'niger' in message.content.lower():
        embed = discord.Embed(
            description=f"{message.author.mention} the N word is forbidden! Please don't say it. This message will self destruct in 30 seconds!",
            colour=hc
        )
        embed.set_footer(text=df)
        await message.delete()
        msg = await message.channel.send(embed=embed)
        await msg.delete(delay=30)
    for mention in message.mentions:
        if 699677108607123548 == mention.id:
            msg = await message.channel.send("<a:{angryping}:{725393149484335165}>")
            await msg.delete(delay=15)
            break
    #if message.channel.id == 689077082609025089 and not message.author.bot:
    #    try:
    #        cur_num = int(message.content)
    #    except:
    #        await message.delete()
    #        embed = discord.Embed(
    #            title="Please don't chat here, this channel is for counting only.",
    #            colour=hc
    #        )
    #        embed.set_footer(text=df)
    #        msg = await message.channel.send(embed=embed)
    #        await msg.delete(delay=5)
    #        return
    #    file = open("counting.json","r+")
    #    current_count = json.load(file)
    #    if current_count is None:
    #        current_count = (cur_num - 1,None)
    #    if cur_num > current_count[0] + 1 or cur_num < current_count[0] + 1 or current_count[1] == message.author.id:
    #        await message.delete()
    #        embed = discord.Embed(
    #            title="Please don't count by yourself, skip ahead, enter a lower number!",
    #            colour=hc
    #        )
    #        embed.add_field(name="Number You Entered:",value=str(cur_num))
    #        embed.add_field(name="Number You Should Have Entered:",value=str(current_count[0] + 1))
    #        embed.add_field(name="Current Number:",value=str(current_count[0]))
    #        embed.add_field(name="Your User ID:",value=str(message.author.id))
    #        embed.add_field(name="Current User ID:",value=str(current_count[1]))
    #        embed.set_footer(text=df)
    #        msg = await message.channel.send(embed=embed)
    #        await msg.delete(delay=5)
    #    else:
    #        current_count = (cur_num,message.author.id)
    #        file.seek(0)
    #        file.truncate()
    #        json.dump(current_count,file)
    #        file.close()
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
        help_embed.add_field(name='s!pickupline | s!pl | s!pickup',
                             value='Responds with a random pickup line!',
                             inline=False
                             )
        help_embed.add_field(name='s!hug <user>',
                             value='Responds with a message telling people that you are hugging them with a random image.',
                             inline=False
                             )
        help_embed.add_field(name='s!kiss <user>',
                             value='Responds with a message telling people that you are kissing them with a random image.',
                             inline=False
                             )
        help_embed.add_field(name='s!pat <user>',
                             value='Responds with a message telling people that you are patting them with a random image.',
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='1/8')
    elif page == '2':
        help_embed.add_field(name='s!facepalm',
                             value='Responds with a message telling people that you are facepalming with a image.',
                             inline=False
                             )
        help_embed.add_field(name='s!sigh',
                             value='Responds with a message telling people that you are sighing with a image.',
                             inline=False
                             )
        help_embed.add_field(name='s!cute <user>',
                             value='Responds with a message telling people that you are think they are cute with a image.',
                             inline=False
                             )
        help_embed.add_field(name='s!sleep | s!sleepy',
                             value='Responds with a random message and a random GIF or image saying that you are sleepy.',
                             inline=False
                             )
        help_embed.add_field(name='s!rps <your choice> | s!rockpaperscissors <your choice>',
                             value='Play a game of Rock Paper Scissors with the bot, to choose your option use "Rock", "Paper", "Scissors" or "R", "P", "S". This command is case-insensitive.',
                             inline=False
                             )
        help_embed.add_field(name='s!8ball <your question> | s!8b <your question>',
                             value='Ask the Magic 8 Ball a question and it will answer!',
                             inline=False
                             )
        help_embed.add_field(name='s!dice <out of>',
                             value='It will generate a random number out of the range you specify, if you do not specify a range the default will be 6',
                             inline=False
                             )
        help_embed.add_field(name='s!kill <user> <reason>',
                             value='Responds with a random kill message and a random GIF or image with a optional reason.',
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='2/8')
    elif page == '3':
        help_embed.add_field(name='s!say <message>',
                             value='Says a message as the bot',
                             inline=False
                             )
        help_embed.add_field(name='s!dm <user> <message>',
                             value='DMs the user as the bot.',
                             inline=False
                             )
        help_embed.add_field(name='s!slap <user> <reason>',
                             value="Responds with a message that tells the person that you slapped them with a random image and a optional reason.",
                             inline=False
                             )
        help_embed.add_field(name='s!punch <user> <reason>',
                             value="Responds with a message that tells the person that you punched them with a random image and a optional reason.",
                             inline=False
                             )
        help_embed.add_field(name='s!sad <reason> | s!cry <reason>',
                             value='Responds with a random message telling people that you are crying or are sad with a random GIF or image.',
                             inline=False
                             )
        help_embed.add_field(name='s!mad <reason> | s!angry <reason>',
                             value='Responds with a random message telling people that you are angry or mad with a random GIF or image.',
                             inline=False
                             )
        help_embed.add_field(name='s!ship <user 1> <user 2>',
                             value="Responds with a ship name for the 2 mentioned people, I am currently working on a ship image but don't expect that to come anytime soon.",
                             inline=False
                             )
        help_embed.add_field(name='s!steal <user> <item>',
                             value="Responds with a message telling the person you mentioned that you are stealing the item you mentioned from him/her!",
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='3/8')
    elif page == '4':
        help_embed.add_field(name='s!punish <user> <reason>',
                             value="Responds with a message telling everyonethat you are punishing the user you mentioned with a optional reason!",
                             inline=False
                             )
        help_embed.add_field(name='s!insult <user> <reason>',
                             value="Responds with a message telling everyone that you are insulting the user you mentioned with a optional reason!",
                             inline=False
                             )
        help_embed.add_field(name='s!highfive <user> | s!hf <user>',
                             value="Responds with a message telling everyone that you are high-fiving the user you mentioned!",
                             inline=False
                             )
        help_embed.add_field(name='s!chatkilled <user> | s!ck <user>',
                             value="Responds with a message telling everyone that the chat was killed with a optional user!",
                             inline=False
                             )
        help_embed.add_field(name='s!flipacoin | s!fac',
                             value="Responds with heads or tails!",
                             inline=False
                             )
        help_embed.add_field(name='s!goodjob <user> <reason> | s!gj <user> <reason>',
                             value="Responds with a message telling everyone that you are congratualating the user you mentioned for doing a good job with a optional reason!",
                             inline=False
                             )
        help_embed.add_field(name='s!agree <user>',
                             value="Responds with a message telling everyone that you agree with a optional person that you agree with!",
                             inline=False
                             )
        help_embed.add_field(name='s!give <user> <item>>',
                             value="Responds with a message telling everyone that you are giving the user you mentioned a item!",
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='4/8')
    elif page == '5':
        help_embed.add_field(name='s!invite',
                             value="Responds with a message with the invite to the server!",
                             inline=False
                             )
        help_embed.add_field(name='s!x <user> | s!doubt <user>',
                             value="Responds with a message telling everyone to spam x to doubt with a optional user!",
                             inline=False
                             )
        help_embed.add_field(name='s!f <user> | s!respects <user>',
                             value="Responds with a message telling everyone to press f to pay respects with a optional user!",
                             inline=False
                             )
        help_embed.add_field(name='s!hb <user> | s!happybirthday <user> | s!birthday <user>',
                             value="Responds with a message wishing the user you mentioned a happy birthday!",
                             inline=False
                             )
        help_embed.add_field(name='s!boredom | s!bored | s!boredom.exe',
                             value="Responds with a message telling everyone that you are bored with a random message!",
                             inline=False
                             )
        help_embed.add_field(name='s!thinking | s!think | s!thinking.exe',
                             value="Responds with a message telling everyone that you are thinking with a random message and a random image!",
                             inline=False
                             )
        help_embed.add_field(name='s!oof <user>',
                             value="Responds with a message telling everyone that you or a optional user you mentioned oofed!",
                             inline=False
                             )
        help_embed.add_field(name='s!serverinfo',
                             value="Responds with a message telling you various information about the server!",
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='5/8')
    elif page == '6':
        help_embed.add_field(name='s!hangman',
                             value='Play a game of hangman!',
                             inline=False)
        help_embed.add_field(
            name='s!uc <number> <unit of number> <target unit> | s!unitconvert <number> <unit of number> <target unit>',
            value="Convert from a one unit to another!",
            inline=False)
        help_embed.add_field(
            name='s!numguess <lives> <max> | s!numberguess <lives> <max> | s!ng <lives> <max>',
            value="Play a number guessing game. The max number is default 100 if not specified!",
            inline=False)
        help_embed.add_field(
            name='s!ciz <timezone> | s!currentinzone <timezone>',
            value="Show the current time and date in the timezone specified, you can use UTC, GMT, and the abbreviation for the timezone.",
            inline=False)
        help_embed.add_field(
            name='s!cfz <hour> <minute> <original timezone> <target timezone> | s!convertfromzone <hour> <minute> <original timezone> <target timezone>',
            value="Converts the time from the timezone specified to the target timezone, if the timezone has multiple word, put quotation marks on both sides of the timezone." +
                  " Make sure you enter the time in 24 hour format. You can use UTC, GMT, and the abbreviation for the timezone.",
            inline=False)
        help_embed.add_field(
            name='s!google <text>',
            value="Googles the text specified and returns the first result, with an option to return up to 5 results",
            inline=False)
        help_embed.add_field(name='s!translate <phrase>',
                             value='Translates the phrase into english!',
                             inline=False
                             )
        help_embed.add_field(name='s!translateto <language> <phrase>',
                             value='Translates the phrase into the language you specified!',
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='6/8')
    elif page == '7':
        help_embed.add_field(name='s!translatefrom <language> <phrase>',
                             value='Translates the phrase from the language you specified!',
                             inline=False
                             )
        help_embed.add_field(name='s!backwardsname <user> | s!backname <user> | s!bn <user>',
                             value="Shows the mentioned user's name backwards! If you don't mention a user, it'll show your own name backwards.",
                             inline=False
                             )
        help_embed.add_field(name='s!purge <number> | s!prune <number>',
                             value="Erases the given number of messages, this command can only be used by people with the manage messages permissions",
                             inline=False
                             )
        help_embed.add_field(name='s!latency',
                             value='Responds with the current latency between HEARTBEAT and a HEARTBEAT_ACK in milliseconds.',
                             inline=False
                             )
        help_embed.add_field(name='s!setcounting <num> <user>',
                             value='Set the current counting position. Can only be used by bot owner.',
                             inline=False
                             )
        help_embed.add_field(name='s!laugh',
                             value='Responds with a message telling people that you are laughing and a random GIF or image.',
                             inline=False
                             )
        help_embed.add_field(name='s!stare <user>',
                             value='Responds with a message telling people that you are staring at them and a GIF.',
                             inline=False
                             )
        help_embed.add_field(name='s!rankthot <user>',
                             value='Responds with a message that says how much of a thot you are.',
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='7/8')
    elif page == '8':
        help_embed.add_field(name="s!deathbattle <user>",
                             value="Have a battle to the death with the user you mentioned!",
                             inline=False
                             )
        help_embed.add_field(name='rp!userinfo <user>',
                             value="Responds with a message telling you various information about the user you mentioned!",
                             inline=False
                             )
        help_embed.add_field(name='rp!outsideuserinfo <user id>',
                             value="Responds with a message telling you various information about the user you mentioned! "
                                   "This is different from the `userinfo` command because this can be used on anyone not "
                                   "just people in the server.",
                             inline=False
                             )
        help_embed.add_field(name='rp!shiprate <name or userid/ping> <name or userid/ping>',
                             value='Responds with a random percentage of how compatible the 2 people would be.',
                             inline=False
                             )
        help_embed.add_field(name='rp!hdmof | rp!hellodarkness',
                             value='Responds with a link that is perfectly timed for the "Hello Darnkess" song.',
                             inline=False
                             )
        help_embed.add_field(name='Page Number', value='8/8')
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
        description=f"{member.mention}'s Avatar/Profile Picture",
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

@client.command()
async def hug(ctx,users:commands.Greedy[discord.Member]):
    random_hug_image_gif = ['https://i.imgur.com/FICmRtv.jpg',
                            'https://i.imgur.com/Ourqcvo.jpg',
                            'https://i.imgur.com/QIWmEhg.jpg',
                            'https://i.imgur.com/Rcee4gW.png',
                            'https://i.imgur.com/YmiehhV.png',
                            'https://i.imgur.com/hxmRmTm.png',
                            'https://i.imgur.com/fvlm134.jpg',
                            'https://i.imgur.com/m8DXSgw.jpg'
                            ]
    rhi = choice(random_hug_image_gif)
    user = ', '.join(x.mention for x in users)
    if user != ctx.message.author.display_name and len(users) >= 1:
        msg = f'{ctx.message.author.mention} has hugged {user}'
    else:
        msg = f'{ctx.message.author.mention} is hugging themselves?'
    a_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    a_embed.set_footer(text=df)
    a_embed.set_image(url=rhi)

    await ctx.message.channel.send(embed=a_embed)

@client.command()
async def kiss(ctx,users:commands.Greedy[discord.Member]):
    random_kiss_image_gif = ['https://i.imgur.com/0CUZcy1.jpg',
                             'https://i.imgur.com/Bo6FcYk.jpg',
                             'https://i.imgur.com/Gc9eUHC.jpg'
                             ]
    rki = choice(random_kiss_image_gif)
    user = ', '.join(x.mention for x in users)
    if user != ctx.message.author.display_name and len(users) >= 1:
        msg = f'{ctx.message.author.mention} has kissed {user}'
    else:
        msg = f'{ctx.message.author.mention} is kissing themselves?'
    k_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    k_embed.set_footer(text=df)
    k_embed.set_image(url=rki)

    await ctx.message.channel.send(embed=k_embed)

@client.command()
async def pat(ctx,users:commands.Greedy[discord.Member]):
    random_pats_image_gif = ['https://i.imgur.com/pUfhIEx.jpg',
                             'https://i.imgur.com/6IEORJr.jpg',
                             'https://i.imgur.com/26Deeck.jpg',
                             'https://i.imgur.com/Gj0fj7m.jpg',
                             'https://i.imgur.com/xOv9bY1.jpg',
                             'https://i.imgur.com/4t3drCT.jpg'
                             ]
    rpi = choice(random_pats_image_gif)
    user = ', '.join(x.mention for x in users)
    if user != ctx.message.author.display_name and len(users) >= 1:
        msg = f'{ctx.message.author.mention} is patting {user}!'
    else:
        msg = f'{ctx.message.author.mention} is patting themselves?'
    p_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    p_embed.set_footer(text=df)
    p_embed.set_image(url=rpi)

    await ctx.message.channel.send(embed=p_embed)

@client.command()
async def facepalm(ctx):
    f_embed = discord.Embed(
        description=f'{ctx.message.author.mention} is facepalming!',
        colour=hc
    )
    f_embed.set_footer(text=df)
    f_embed.set_image(url='https://i.imgur.com/e1NsTzQ.jpg')

    await ctx.message.channel.send(embed=f_embed)

@client.command()
async def sigh(ctx):
    s_embed = discord.Embed(
        description=f'{ctx.message.author.mention} has sighed!',
        colour=hc
    )
    s_embed.set_footer(text=df)
    s_embed.set_image(url='https://i.imgur.com/JWeTHLT.jpg')

    await ctx.message.channel.send(embed=s_embed)

@client.command()
async def cute(ctx,*,user:discord.Member='empty'):
    random_cute_image_gif = ['https://i.imgur.com/r6CB5T0.jpg',
                             'https://i.imgur.com/pV9V1zj.jpg',
                             'https://i.imgur.com/FICmRtv.jpg',
                             'https://i.imgur.com/IpBEWZK.jpg',
                             'https://i.imgur.com/lLwkl9v.jpg',
                             'https://i.imgur.com/ez9K9wU.gif',
                             'https://i.imgur.com/S5M8tNM.jpg',
                             'https://i.imgur.com/8F4Y4vT.jpg',
                             'https://i.imgur.com/K4QDlLP.jpg',
                             'https://i.imgur.com/K4QDlLP.jpg',
                             'https://i.imgur.com/t8fvHeK.jpg',
                             'https://i.imgur.com/VM0Me3O.png',
                             'https://i.imgur.com/KUBa7EZ.jpg',
                             'https://i.imgur.com/D0qcnNz.jpg',
                             'https://i.imgur.com/NvCX3uF.jpg',
                             'https://i.imgur.com/hpoFYF3.jpg'
                             ]
    rci = choice(random_cute_image_gif)
    if user != 'empty':
        msg = f'{ctx.message.author.mention} thinks that {user.mention} is cute!'
    else:
        msg = f'{ctx.message.author.mention} is calling themselves cute?'
    c_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    c_embed.set_footer(text=df)
    c_embed.set_image(url=rci)

    await ctx.message.channel.send(embed=c_embed)

@client.command(aliases=['rockpaperscissors','rps'])
async def _rps(ctx,choose):
    choose = choose.lower()
    if choose == 'rock' or choose == 'r':
        is_rps = True
        p_choose = 'Rock'
    elif choose == 'scissors' or choose == 's':
        is_rps = True
        p_choose = "Scissors"
    elif choose == 'paper' or choose == 'p':
        is_rps = True
        p_choose = "Paper"
    else:
        is_rps = False
        embed = discord.Embed(title="Invalid Option, Try again!",colour=discord.Colour.red())
        embed.set_image(url='https://i.imgur.com/XgqWMei.jpg')
    if is_rps:
        RPS_options = ['Rock', 'Paper', 'Scissors']
        b_choose = choice(RPS_options)
        #True = Bot Win False = Player Win Tie = Tie
        if b_choose == p_choose:
            wlt = "Tie"
        elif b_choose == 'Rock':
            if p_choose == "Scissors":
                wlt = True
            if p_choose == "Paper":
                wlt = False
        elif b_choose == "Scissors":
            if p_choose == "Rock":
                wlt = False
            if p_choose == "Paper":
                wlt = True
        elif b_choose == "Paper":
            if p_choose == "Rock":
                wlt = True
            if p_choose == "Scissors":
                wlt = False
        if wlt != "Tie":
            if wlt:
                embed = discord.Embed(title=f"I choose {b_choose}, You chose {p_choose}. I Win!",colour=discord.Colour.red())
            else:
                embed = discord.Embed(title=f"I choose {b_choose}, You chose {p_choose}. I Lose!",colour=discord.Colour.green())
        else:
            embed = discord.Embed(title=f"I choose {b_choose}, You chose {p_choose}. We Tie!",colour=discord.Colour.gold())
        if b_choose == "Rock":
            img = 'https://i.imgur.com/xQQE5UA.jpg'
        elif b_choose == "Scissors":
            img = 'https://i.imgur.com/WAuWmFI.png'
        elif b_choose == "Paper":
            img = 'https://i.imgur.com/SK50Kvl.png'
        embed.set_image(url=img)
    embed.set_footer(text=df)
    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['8ball','8b'])
async def _8ball(ctx,*,question):
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
     "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
     "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
     "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

    sel_response = choice(responses)

    embed = discord.Embed(title=f'{sel_response}!',description=f'Your Question: {question}!',colour=hc)
    embed.set_image(url='https://i.imgur.com/Es4mCIe.jpg')
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def dice(ctx,out_of='6'):
    con = True
    try:
        out_of_int = int(out_of)
    except ValueError as e:
        embed = discord.Embed(title='Please enter a actual number!', colour=discord.Colour.red())
        embed.set_image(url='https://i.imgur.com/XgqWMei.jpg')
        embed.add_field(name="Error:", value=str(e))
        con = False
    if con:
        ran_num = str(randint(1,out_of_int))
        embed = discord.Embed(title=f'The Dice Says: {ran_num}', colour=hc)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command(pass_context=True)
async def kill(ctx,user:discord.Member,*,reason='None'):
    random_kill_message = [f'{ctx.message.author.mention} has killed {user.mention}',
                           f'{ctx.message.author.mention} has headshotted {user.mention}',
                           f'{user.mention} was shot by {ctx.message.author.mention}']
    random_kill_gif = ['https://i.imgur.com/qflLsJu.gif',
                       'https://i.imgur.com/Za8sxpF.gif',
                       'https://i.imgur.com/yWyiUnk.gif'
                       ]
    km = choice(random_kill_message)
    kg = choice(random_kill_gif)
    k_embed = discord.Embed(
        description=km,
        colour=hc
    )
    k_embed.set_footer(text=df)
    k_embed.set_image(url=kg)
    if reason != "None":
        k_embed.add_field(name="Reason:",value=reason)
    await ctx.message.channel.send(embed=k_embed)

@client.command()
async def dm(ctx,member: discord.Member,*,message):
    await ctx.message.delete()
    await member.send(message)

@client.command()
async def bsay(ctx,*,message):
    if ctx.message.author.id == 616032766974361640:
        await ctx.message.delete()
        await ctx.send(message)

@client.command()
async def say(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(message + "\n\n **-" + ctx.message.author.display_name + "**")

@client.command()
async def slap(ctx,user:discord.Member,*,reason="None"):
    random_slap_image_gif = ['https://i.imgur.com/8yJ9qoh.jpg',
                             'https://i.imgur.com/LLIKgWT.png'
    ]
    rsi = choice(random_slap_image_gif)
    c_embed = discord.Embed(
        description=f'{ctx.message.author.mention} has slapped {user.mention}!',
        colour=hc
    )
    c_embed.set_footer(text=df)
    c_embed.set_image(url=rsi)
    if reason != "None":
        c_embed.add_field(name="Reason:",value=reason)

    await ctx.message.channel.send(embed=c_embed)

@client.command()
async def punch(ctx,user:discord.Member,*,reason='None'):
    random_punch_image_gif = ['https://i.ibb.co/bsYTnQ4/killgif2.gif',
                             'https://i.imgur.com/Za8sxpF.gif'
    ]
    rpi = choice(random_punch_image_gif)
    p_embed = discord.Embed(
        description=f'{ctx.message.author.mention} has punched {user.mention}!',
        colour=hc
    )
    p_embed.set_footer(text=df)
    p_embed.set_image(url=rpi)
    if reason != "None":
        p_embed.add_field(name="Reason:",value=reason)

    await ctx.message.channel.send(embed=p_embed)

@client.command(aliases=['sco','suggestcommand'])
async def _suggestcommand(ctx,*,command):
    embed = discord.Embed(title="New Command Suggestion!",colour=hc)
    embed.set_footer(text=df)
    embed.add_field(name='Command Name',value=command)
    embed.add_field(name='Requester', value=ctx.message.author)
    log_channel = client.get_channel(683760960820740132)
    await log_channel.send(embed=embed)
    confirm_embed = discord.Embed(title="Command Suggestion Succeeded!",description='A Staff Member will review it shortly.',colour=discord.Colour.green())
    confirm_embed.add_field(name='Command Name', value=command)
    confirm_embed.add_field(name='Requester', value=ctx.message.author)
    confirm_embed.set_footer(text=df)
    await ctx.message.channel.send(embed=confirm_embed)

@client.command(aliases=['cry','sad'])
async def _crysad(ctx,*,reason="None"):
    random_cry_sad_image = ['https://i.imgur.com/2idqzX5.jpg',
                            'https://i.imgur.com/21qHg4N.jpg',
                            'https://i.imgur.com/WEIMm9N.jpg',
                            'https://i.imgur.com/DgYa47G.png',
                            'https://i.imgur.com/ED5vXzC.jpg',
                            'https://i.imgur.com/weekaqO.png',
                            'https://i.imgur.com/yR0oqj8.jpg',
                            'https://i.imgur.com/sM6SvUm.jpg',
                            'https://i.imgur.com/ceHRXvU.jpg'
    ]
    random_cry_sad_message = [f"{ctx.message.author.mention} is sad!",
                              f"{ctx.message.author.mention} is crying!",
                              f"{ctx.message.author.mention} is sad! Someone go hug him/her!",
                              f"{ctx.message.author.mention} is crying! Someone go hug him/her!"
    ]
    rcsi = choice(random_cry_sad_image)
    rcsm = choice(random_cry_sad_message)
    embed = discord.Embed(description=rcsm,colour=hc)
    embed.set_image(url=rcsi)
    embed.set_footer(text=df)
    if reason != "None":
        embed.add_field(name="Reason:",value=reason)
    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['angry','mad'])
async def _angry(ctx,*,reason="None"):
    random_angry_image = ['https://i.imgur.com/1VXQ0cl.jpg',
                          'https://i.imgur.com/lrXbqIq.jpg',
                          'https://i.imgur.com/xCZ8qEr.png'
    ]
    random_angry_message = [f"{ctx.message.author.mention} is mad!",
                              f"{ctx.message.author.mention} is angry!",
                              f"{ctx.message.author.mention} is mad! Don't piss him/her off more",
                              f"{ctx.message.author.mention} is angry! Someone go hug him/her!",
                              f"{ctx.message.author.mention} is mad! Tread lightly",
                              f"{ctx.message.author.mention} is angry! Tread lightly!"
    ]
    rai = choice(random_angry_image)
    ram = choice(random_angry_message)
    embed = discord.Embed(description=ram,colour=hc)
    embed.set_image(url=rai)
    embed.set_footer(text=df)
    if reason != "None":
        embed.add_field(name="Reason:",value=reason)
    await ctx.message.channel.send(embed=embed)

@client.command()
async def ship(ctx,user1: discord.Member,user2: discord.Member):
    length_u1 = math.floor(len(user1.display_name)/2)
    length_u2 = math.floor(len(user2.display_name)/2)
    u1 = user1.display_name[0:length_u1]
    u2 = user2.display_name[length_u2:len(user2.display_name)]
    ship_name = u1 + u2
    ship_embed = discord.Embed(
        title=ship_name,
        description=f"{user1.mention} and {user2.mention}'s Ship Name",
        colour=hc
    )
    ship_embed.set_footer(text=df)
    await ctx.message.channel.send(embed=ship_embed)

@client.command()
async def steal(ctx,user: discord.Member,*,item):
    random_steal_message = [f"{ctx.message.author.mention} has stolen {item} from {user.mention}!",
                            f"{ctx.message.author.mention} has taken {item} from {user.mention}!",
                            f"{user.mention}'s {item} is missing! It seems {ctx.message.author.mention} has taken it!",
                            f"{ctx.message.author.mention} really likes {user.mention}'s {item} so he/she took it!"
                            ]
    rsm = choice(random_steal_message)
    s_embed = discord.Embed(
        description=rsm,
        colour=hc
    )
    s_embed.set_footer(text=df)
    s_embed.set_image(url='https://i.imgur.com/gQNFxGj.jpg')
    await ctx.message.channel.send(embed=s_embed)

@client.command()
async def punish(ctx,user: discord.Member,*,reason="None"):
    p_embed = discord.Embed(
        description=f"{ctx.message.author.mention} has punished {user.mention}!",
        colour=hc
    )
    p_embed.set_footer(text=df)
    p_embed.set_image(url='https://i.imgur.com/RyEErwy.jpg')
    if reason != "None":
        p_embed.add_field(name="Reason:",value=reason)
    await ctx.message.channel.send(embed=p_embed)


@client.command()
async def insult(ctx,user:discord.Member,*,reason="None"):
    random_embed_message = [
        f"{ctx.message.author.mention} has insulted {user.mention}!",
        f"{ctx.message.author.mention} has insulted {user.mention}, what a savage!",
        f"{user.mention} has been insulted by {ctx.message.author.mention}!"
    ]
    rem = choice(random_embed_message)
    i_embed = discord.Embed(
        description=rem,
        colour=hc
    )
    i_embed.set_image(url='https://i.imgur.com/uaz7WXM.jpg')
    if reason != "None":
        i_embed.add_field(name="Reason:",value=reason)
    i_embed.set_footer(text=df)
    await ctx.message.channel.send(embed=i_embed)

@client.command(aliases=['hf','highfive'])
async def _highfive(ctx,user:discord.Member):
    h_embed = discord.Embed(
        description=f"{ctx.message.author.mention} has high-fived {user.mention}",
        colour=hc
    )
    h_embed.set_image(url='https://i.imgur.com/CBdjdbi.jpg')
    h_embed.set_footer(text=df)

    await ctx.message.channel.send(embed=h_embed)

@client.command(aliases=['chatkilled','ck'])
async def _chatkilled(ctx,user:discord.Member="None"):
    if user != "None":
        msg = f"{ctx.message.author.mention} thinks {user.mention} has killed the chat! Someone revive it!"
    else:
        msg = f"{ctx.message.author.mention} thinks the chat has been killed. Someone revive it!"
    c_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    c_embed.set_footer(text=df)
    c_embed.set_image(url='https://i.imgur.com/6Z4bVys.jpg')

    await ctx.message.channel.send(embed=c_embed)

@client.command(aliases=['flipacoin','fac'])
async def _flipacoin(ctx):
    sides = ["Heads","Tails"]
    ans = choice(sides)
    r_embed = discord.Embed(
        title=f"You got {ans}!",
        colour=hc
    )
    if ans == "Heads":
        r_embed.set_image(url='https://i.imgur.com/vmuGKvI.png')
    else:
        r_embed.set_image(url='https://i.imgur.com/47kev45.png')
    r_embed.set_footer(text=df)

    await ctx.message.channel.send(embed=r_embed)

@client.command()
async def agree(ctx,user:discord.Member="None"):
    if user != "None":
        msg = f"{ctx.message.author.mention} agrees with what {user.mention} said!"
    else:
        msg = f"{ctx.message.author.mention} agrees with what was said!"
    a_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    a_embed.set_footer(text=df)
    a_embed.set_image(url="https://i.imgur.com/sxu72BJ.jpg")

    await ctx.message.channel.send(embed=a_embed)

@client.command()
async def give(ctx,user: discord.Member,*,item):
    random_give_image = ['https://i.imgur.com/H0dXCW0.jpg',
                         'https://i.imgur.com/6fR6XYD.jpg',
                         'https://i.imgur.com/54wX55D.png'
                            ]
    rgi = choice(random_give_image)
    g_embed = discord.Embed(
        descritpion=f"{ctx.message.author.mention} has given {item} to {user.mention}",
        colour=hc
    )
    g_embed.set_footer(text=df)
    g_embed.set_image(url=rgi)
    await ctx.message.channel.send(embed=g_embed)

@client.command()
async def invite(ctx):
    #put invite here
    invite = 'https://discord.gg/Cr43nuF'
    i_embed = discord.Embed(
        title="Here is the invite for the Elevator Server",
        colour=hc
    )
    i_embed.set_footer(text=df)
    i_embed.add_field(name="Invite:",value=invite)

    await ctx.message.channel.send(embed=i_embed)

@client.command(aliases=['goodjob','gj'])
async def _goodjob(ctx,user:discord.Member,*,reason="None"):
    random_goodjob_message = [
        f"{ctx.message.author.mention} thinks {user.mention} did a good job!",
        f"{ctx.message.author.mention} is congratulating {user.mention} for doing a good job!",
        f"{user.mention} is getting praised by {ctx.message.author.mention} for doing a good job!"
    ]
    rgjm = choice(random_goodjob_message)

    g_embed = discord.Embed(
        description=rgjm,
        colour=hc
    )
    g_embed.set_footer(text=df)
    g_embed.set_image(url='https://i.imgur.com/YciY7Qo.jpg')
    if reason != "None":
        g_embed.add_field(name="Reason:",value=reason)

    await ctx.message.channel.send(embed=g_embed)

@client.command(aliases=['f','respects'])
async def _f(ctx,user:discord.Member="None"):
    random_f_image = [
            'https://i.imgur.com/Qn4lHqJ.png',
            'https://i.imgur.com/Li6lOuw.jpg'
    ]
    rfi = choice(random_f_image)
    if user != "None":
        msg = f"Press F to pay respects to {user.mention}"
    else:
        msg = "Press F to pay respects!"
    f_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    f_embed.set_footer(text=df)
    f_embed.set_image(url=rfi)

    await ctx.message.channel.send(embed=f_embed)

@client.command(aliases=['x','doubt'])
async def _x(ctx,user:discord.Member="None"):
    random_x_image = [
        'https://i.imgur.com/0GETcS1.jpg',
        'https://i.imgur.com/wutBLAX.png'
    ]
    rxi = choice(random_x_image)
    if user != "None":
        msg = f"Spam X to doubt {user.mention}!"
    else:
        msg = "Spam X to doubt!"
    x_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    x_embed.set_footer(text=df)
    x_embed.set_image(url=rxi)

    await ctx.message.channel.send(embed=x_embed)

@client.command(aliases=['hb','happybirthday','birthday'])
async def _happybirthday(ctx,user:discord.Member):
    random_birthday_image = [
            'https://i.imgur.com/sgJBE5E.jpg',
            'https://i.imgur.com/oHVZmQm.jpg',
            'https://i.imgur.com/SlRPSvc.png'
    ]
    rbi = choice(random_birthday_image)
    b_embed = discord.Embed(
        description=f"{ctx.message.author.mention} wishes a happy birthday to {user.mention}",
        colour=hc
    )
    b_embed.set_footer(text=df)
    b_embed.set_image(url=rbi)

    await ctx.message.channel.send(embed=b_embed)

@client.command(aliases=['boredom','bored','boredom.exe'])
async def _boredom(ctx):
    random_boredom_message = [
        f'{ctx.message.author.mention} is bored!',
        f'{ctx.message.author.mention} has started the process boredom.exe!',
        f'{ctx.message.author.mention} is bored! Someone RP with him/her!'
    ]
    rbm = choice(random_boredom_message)
    b_embed = discord.Embed(
        description=rbm,
        colour=hc
    )
    b_embed.set_footer(text=df)
    b_embed.set_image(url='https://i.imgur.com/JpSbAji.jpg')

    await ctx.message.channel.send(embed=b_embed)

@client.command(aliases=['thinking','think','thinking.exe'])
async def _thinking(ctx):
    random_thinking_message = [
        f'{ctx.message.author.mention} is thinking!',
        f'{ctx.message.author.mention} has started the process thinking.exe!',
    ]
    random_thinking_image = [
        'https://i.imgur.com/tgUNcwr.jpg',
        'https://i.imgur.com/akIMMK9.jpg',
        'https://i.imgur.com/ebHYDox.jpg'
    ]
    rtm = choice(random_thinking_message)
    rti = choice(random_thinking_image)
    t_embed = discord.Embed(
        description=rtm,
        colour=hc
    )
    t_embed.set_footer(text=df)
    t_embed.set_image(url=rti)

    await ctx.message.channel.send(embed=t_embed)

@client.command()
async def oof(ctx,user: discord.Member="None"):
    random_oof_message = [
        f'{ctx.message.author.mention} got oofed!',
        f'{ctx.message.author.mention} had a oof moment!',
    ]
    if user != "None":
        random_oof_message.append(f'{ctx.message.author.mention} thinks {user.mention} had a oof moment!')
        random_oof_message.append(f'{ctx.message.author.mention} has oofed {user.mention}!')
    random_oof_image = [
        'https://i.imgur.com/x4nl4Le.jpg',
        'https://i.imgur.com/yDyG5YY.jpg',
        'https://i.imgur.com/jYJoP7i.jpg'
    ]
    rom = choice(random_oof_message)
    roi = choice(random_oof_image)
    o_embed = discord.Embed(
        descriptione=rom,
        colour=hc
    )
    o_embed.set_footer(text=df)
    o_embed.set_image(url=roi)

    await ctx.message.channel.send(embed=o_embed)

@client.command()
async def serverinfo(ctx):
    guild = ctx.author.guild
    creation_time = guild.created_at
    creation_time = creation_time.strftime("%Y-%m-%d %H:%M UTC")
    channels = [f"Channels of {guild.name}:"]
    roles = []
    for x in guild.channels:
        if type(x) != discord.TextChannel:
            continue
        channels.append(x.name)
    for x in guild.roles:
        roles.append(x.name)
    roles.append(f"Roles of {guild.name}:")
    roles.reverse()
    channel_msg = '\n'.join(x for x in channels)
    role_msg = '\n'.join(x for x in roles)
    channel_params = {'api_dev_key': pastebin_api_key, 'api_option': 'paste',
                      'api_paste_code':channel_msg,'api_paste_name':f"{guild.name}'s Channels",'api_paste_private':0,
                      "api_user_key":pastebin_user_key,"api_paste_expire_date":'1H'}
    role_params = {'api_dev_key': pastebin_api_key, 'api_option': 'paste',
                   'api_paste_code':role_msg,'api_paste_name':f"{guild.name}'s Roles",'api_paste_private':0,
                   "api_user_key":pastebin_user_key,"api_paste_expire_date":'1H'}
    channel_url = requests.post(pastebin_url,data=channel_params).text
    role_url = requests.post(pastebin_url,data=role_params).text
    i_embed = discord.Embed(
        title=f"Server Info for {guild.name}",
        colour=hc
    )
    i_embed.set_footer(text=df)
    i_embed.set_thumbnail(url=guild.icon_url)
    i_embed.add_field(name="Name:",value=guild.name)
    i_embed.add_field(name="Region:", value=str(guild.region))
    i_embed.add_field(name="ID:", value=guild.id)
    i_embed.add_field(name="Owner:", value=guild.owner.display_name)
    i_embed.add_field(name="Member Count:", value=guild.member_count)
    i_embed.add_field(name="Creation Time:", value=creation_time)
    i_embed.add_field(name="Channels (Expires in 1 Hour):",value=channel_url)
    i_embed.add_field(name="Roles (Expires in 1 Hour):",value=role_url)

    await ctx.message.channel.send(embed=i_embed)

@client.command()
async def hangman(ctx):
    m = RandomWords()
    d = PyDictionary()
    word = m.get_random_word(hasDictionaryDef='true').lower()
    definition = d.meaning(word)
    if definition == None:
        definition = "Definition Not Found"
    #remove after test
    print(f"Answer: {word}")
    lives = 6
    word_list = []
    guessed_letters = []
    win = False
    for x in word:
        word_list.append('%')
    s_embed = discord.Embed(
        title=''.join(x for x in word_list),
        description="Welcome to Hangman! You have 6 lives. You can only guess one letter at a time (no full word guesses). Type your response. To quit, enter the word 'quit'."
        + " The word can be any word in the english dictionary, and can contain dashes('-').",
        colour=hc
    )
    s_embed.set_footer(text=df)
    s_embed.add_field(name="Lives:",value=str(lives))
    s_embed.add_field(name="Letters Left:",value=str(len([i for i,l in enumerate(word_list) if l == '%'])))
    await ctx.message.channel.send(embed=s_embed)

    def check(message):
        if message.author == ctx.message.author:
            return True
        else:
            return False
    def result(msg,rnr):
        if rnr:
            c = discord.Colour.dark_green()
        else:
            c = discord.Colour.dark_red()
        t_embed = discord.Embed(
            title=''.join(x for x in word_list),
            colour=c
        )
        t_embed.set_footer(text=df)
        t_embed.add_field(name="You Guessed:",value=msg.upper())
        t_embed.add_field(name="Lives:",value=str(lives))
        t_embed.add_field(name="Letters Left:", value=str(len([i for i, l in enumerate(word_list) if l == '%'])))

        return t_embed
    def check_win():
        num_left = len([i for i,l in enumerate(word_list) if l == '%'])
        if num_left == 0:
            return True
        return False

    while True:
        if lives <= 0:
            break
        msg = await client.wait_for('message',check=check,timeout=None)
        msg = msg.content.lower()
        if msg == 'quit':
            break
        if not len(msg) == 1 or msg in guessed_letters:
            await ctx.message.channel.send("You have either already guessed that letter before or you have entered more or less than 1 letter")
            continue
        indexes = [i for i,l in enumerate(word) if l == msg]
        if len(indexes) == 0:
            lives -= 1
            rnr = False
        else:
            for x in indexes:
                word_list[int(x)] = msg
            rnr = True
        guessed_letters.append(msg)
        await ctx.message.channel.send(embed=result(msg,rnr))
        if check_win():
            win = True
            break
    if win:
        e_embed = discord.Embed(
            title="You win!!!",
            colour=discord.Colour.green()
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Word:",value=word)
        e_embed.add_field(name="Lives Left:",value=str(lives))
        e_embed.add_field(name="Definition:",value=definition,inline=False)
    else:
        e_embed = discord.Embed(
            title="You lose!!!",
            colour=discord.Colour.red()
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Word:", value=word)
        e_embed.add_field(name="Letters Left:", value=str(len([i for i, l in enumerate(word_list) if l == '%'])))
        e_embed.add_field(name="Definition:", value=definition, inline=False)
    await ctx.message.channel.send(embed=e_embed)

@client.command(aliases=['unitconvert','uc'])
async def _unitconvert(ctx,num1,unitfrom,unitto):
    units = [
        'm/meter','g/gram','s/second','A/ampere','K/kelvin','mol/mole','cd/candela','Hz/hertz','N/newton','Pa/pascal',
        'J/joule','W/watt','C/coulomb','V/volt','Ω/ohm','S/siemens','F/farad','T/tesla','Wb/weber','H/henry',
        '°C/celsius','rad/radian','sr/steradian','lm/lumen','lx/lux','Bq/becquerel','Gy/gray','Sv/sievert','kat/katal',
        '°F/fahrenheit','th/thou','in/inch','ft/foot','yd/yard','ch/chain','fur/furlong','ml/mile','lea/league','bar',
        'min/minute','h/hour'
    ]
    full_form = num1 + ' ' + unitfrom
    try:
        ans = float(converts(full_form,unitto))
    except Exception as e:
        embed = discord.Embed(
            title="That unit doesn't exist!",
            colour=hc
        )
        embed.set_footer(text=df)
        if unitfrom in str(e):
            embed.add_field(name="Error Unit:",value=f'The unit "{unitfrom}" ' + "doesn't exist!")
        else:
            embed.add_field(name="Error Unit:",value=f'The unit "{unitto}" ' + "doesn't exist!")
        embed.add_field(name="Error:", value=str(e))
        embed.add_field(name="Supported Units",value=', '.join(x for x in units),inline=False)
        await ctx.message.channel.send(embed=embed)
        return
    embed = discord.Embed(
        title=f'{str(ans)} {unitto}',
        colour=hc
    )
    embed.add_field(name="Convert From:",value=f'{num1} {unitfrom}')
    embed.add_field(name="Convert To:",value=unitto)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['numguess','numberguess','ng'])
async def _numguess(ctx,lives,max=100):
    try:
        lives = int(lives)
        max = int(max)
    except:
        await ctx.message.channel.send("Please enter a number!")
        return
    truenum = randint(0,max)
    win = False
    #remove after test
    print(f"Answer: {str(truenum)}")
    start_embed = discord.Embed(
        title="Welcome to the number guessing game! Guess a number between the range below and follow the clues given to guess the correct number. Type 'quit' to quit.",
        colour=hc
    )
    start_embed.set_footer(text=df)
    start_embed.add_field(name="Lives:",value=str(lives))
    start_embed.add_field(name="Range:",value=f"0-{str(max)}")

    await ctx.message.channel.send(embed=start_embed)

    def check(message):
        if message.author == ctx.message.author:
            return True
        else:
            return False
    def result(num,highlow):
        embed = discord.Embed(
            title=f"You guessed too {highlow}!",
            colour=discord.Colour.dark_red()
        )
        embed.add_field(name="You Guessed:",value=str(num))
        embed.add_field(name='Lives Left:',value=str(lives))
        embed.set_footer(text=df)
        return embed
    while True:
        if lives <= 0:
            break
        msg = await client.wait_for('message',check=check,timeout=None)
        if msg.content == 'quit':
            break
        try:
            guessnum = int(msg.content)
        except:
            await ctx.message.channel.send("Please enter a number!")
            continue
        if guessnum > max or guessnum < 0:
            await ctx.message.channel.send(f"The number you guessed is out of the range specified! The range is 0-{str(max)}")
            continue
        if guessnum == truenum:
            win = True
            break
        else:
            lives -= 1
            if guessnum > truenum: highlow = "high"
            if guessnum < truenum: highlow = "low"
            await ctx.message.channel.send(embed=result(guessnum,highlow))
    if win:
        e_embed = discord.Embed(
            title="You win!!!",
            colour=discord.Colour.green()
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Number:",value=str(truenum))
        e_embed.add_field(name="Lives Left:",value=str(lives))
    else:
        e_embed = discord.Embed(
            title="You loose!!!",
            colour=discord.Colour.red()
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Number:", value=str(truenum))
    await ctx.message.channel.send(embed=e_embed)

@client.command(aliases=['currentinzone','ciz'])
async def _currenttimeintimezone(ctx,*,timezone):
    if ' ' in timezone:
        timezone = timezone.title()
    else:
        timezone = timezone.upper()
    utc = arrow.utcnow()
    try:
        current = utc.to(timezone)
    except Exception as e:
        e_embed = discord.Embed(
            title="Invalid Timezone!",
            description="You have may have entered a invalid timezone, if you are sure that the timezone is correct, try entering it in it's" +
            " short or long form, for example if you entered EDT, enter Eastern Daylight Time, and if you entered Eastern Standard Time enter" +
            " EST. Another important thing to keep in mind is Daylight Savings, for example in Toronto if daylight savings is active, we use EDT" +
            "(Eastern Daylight Time) but normally we use EST (Eastern Standard Time). If you were to enter EST, when daylight savings is active, " +
            "The time will be 1 hour off. The same goes for the other timezones that have Daylight Savings or something similar. " +
            "This command also works with UTC, you can enter something like 'UTC-5' which is EST, or 'UTC-4' which is EDT, The same goes for GMT-5/GMT-4. " +
            "This module is still a bit finicky so if there are bugs, rest assured that I am working on fixing it",
            colour=hc
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Error:",value=str(e))
        await ctx.message.channel.send(embed=e_embed)
        return
    r_embed = discord.Embed(
        title=f"Here is the current time in {timezone}",
        colour=hc
    )
    r_embed.set_footer(text=df)
    r_embed.add_field(name="Current Time:",value=current.format('YYYY-MM-DD HH:mm UTC ZZ'))
    await ctx.message.channel.send(embed=r_embed)

@client.command(aliases=['convertfromzone','cfz'])
async def _convertfromtimezone(ctx,hour,min,cfrom,cto):
    def error_zone(error):
        e_embed = discord.Embed(
            title="Invalid Timezone!",
            description="You have may have entered a invalid timezone, if you are sure that the timezone is correct, try entering it in it's" +
                        " short or long form, for example if you entered EDT, enter Eastern Daylight Time, and if you entered Eastern Standard Time enter" +
                        " EST. Another important thing to keep in mind is Daylight Savings, for example in Toronto if daylight savings is active, we use EDT" +
                        "(Eastern Daylight Time) but normally we use EST (Eastern Standard Time). If you were to enter EST, when daylight savings is active, " +
                        "The time will be 1 hour off. The same goes for the other timezones that have Daylight Savings or something similar. " +
                        "This command also works with UTC, you can enter something like 'UTC-5' which is EST, or 'UTC-4' which is EDT, The same goes for GMT-5/GMT-4. " +
                        "This module is still a bit finicky so if there are bugs, rest assured that I am working on fixing it",
            colour=hc
        )
        e_embed.set_footer(text=df)
        e_embed.add_field(name="Error:", value=str(error))
        return e_embed
    if ' ' in cfrom:
        cfrom = cfrom.title()
    else:
        cfrom = cfrom.upper()
    if ' ' in cto:
        cto = cto.title()
    else:
        cto = cto.upper()
    t_utc = arrow.utcnow()
    try:
        t_time_date = t_utc.to(cfrom)
    except Exception as e:
        await ctx.message.channel.send(embed=error_zone(e))
        return
    if len(hour) == 1:
        hour = '0' + hour
    if len(min) == 1:
        hour = '0' + hour
    format_for_get = t_time_date.format('YYYY-MM-DD') + ' ' + hour + ':' + min + ':00' + t_time_date.format('ZZ')
    c_time = arrow.get(format_for_get)
    try:
        current_to = c_time.to(cto)
    except Exception as e:
        await ctx.message.channel.send(embed=error_zone(e))
        return
    r_embed = discord.Embed(
        title=f"Here is the {str(hour)}:{str(min)} {cfrom} in {cto}",
        colour=hc
    )
    r_embed.set_footer(text=df)
    r_embed.add_field(name="Current Time:",value=current_to.format('YYYY-MM-DD HH:mm UTC ZZ'))
    await ctx.message.channel.send(embed=r_embed)

@client.command()
async def google(ctx,*,question):
    msg_list = []
    async def delete_message():
        for message in msg_list:
            await message.delete(delay=30)
    msg_list.append(ctx.message)
    for j in search(question, tld="co.in", num=10, stop=1, pause=0.9):
        result = j
    msg_list.append(await ctx.message.channel.send(f'Google Search Result For "{question}": {result}'))
    msg_list.append(await ctx.message.channel.send("Do you want more results? If you do, type the number of results (maximum of 5) you want below. If you don't type 'quit' or wait 30 seconds"))
    def check(message):
        if message.author == ctx.message.author:
            return True
        else:
            return False
    try:
        result_num = await client.wait_for('message', check=check, timeout=30)
        await result_num.delete(delay=30)
        if result_num.content == 'quit':
            msg_list.append(await ctx.message.channel.send('Request Quit!'))
            await delete_message()
            return
    except:
        msg_list.append(await ctx.message.channel.send("Request Timed Out"))
        await delete_message()
        return
    try:
        result_num = int(result_num.content)
    except:
        msg_list.append(await ctx.message.channel.send("That isn't a number! Request Timed Out"))
        await delete_message()
        return
    if result_num > 5:
        msg_list.append(await ctx.message.channel.send("Discord will only show a maximum of 5 results."))
        result_num = 5
    result_list = []
    for j in search(question, tld="co.in", num=10, stop=result_num, pause=1.8):
        result_list.append(j)
    result = '  |  '.join(x for x in result_list)
    msg_list.append(await ctx.message.channel.send(f'Google Search Result For "{question}": {result}'))
    await delete_message()

@client.command()
async def translate(ctx,*,text):
    translator = Translator()
    translated = translator.translate(text)
    embed = discord.Embed(
        title="Translation Completed",
        colour=hc
    )
    embed.add_field(name="Translated Text:",value=translated.text,inline=False)
    embed.add_field(name="Pronunciation:",value=translated.pronunciation,inline=True)
    embed.add_field(name="Source Language (Auto-Detected):",value=f"{LANGUAGES[translated.src]} ({translated.src})",inline=True)
    embed.add_field(name="Destination Language:",value=f"{LANGUAGES[translated.dest]} ({translated.dest})",inline=True)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def translateto(ctx,languageto,*,text):
    translator = Translator()
    try:
        translated = translator.translate(text,dest=languageto)
    except Exception as e:
        embed = discord.Embed(title="The language you mentioned doesn't exist!", colour=discord.Colour.red())
        embed.add_field(name="Supported Languages:",value="https://pastebin.com/LMuNGwAK")
        embed.add_field(name="Error:", value=str(e))
        await ctx.message.channel.send(embed=embed)
        return
    embed = discord.Embed(
        title="Translation Completed",
        colour=hc
    )
    embed.add_field(name="Translated Text:", value=translated.text, inline=False)
    embed.add_field(name="Pronunciation:", value=translated.pronunciation, inline=True)
    embed.add_field(name="Source Language (Auto-Detected):",value=f"{LANGUAGES[translated.src]} ({translated.src})",inline=True)
    embed.add_field(name="Destination Language:",value=f"{LANGUAGES[translated.dest]} ({translated.dest})",inline=True)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def translatefrom(ctx,languagefrom,*,text):
    translator = Translator()
    try:
        translated = translator.translate(text,src=languagefrom)
    except Exception as e:
        embed = discord.Embed(title="The language you mentioned doesn't exist!", colour=discord.Colour.red())
        embed.add_field(name="Supported Languages:",value="https://pastebin.com/LMuNGwAK")
        embed.add_field(name="Error:", value=str(e))
        await ctx.message.channel.send(embed=embed)
        return
    embed = discord.Embed(
        title="Translation Completed",
        colour=hc
    )
    embed.add_field(name="Translated Text:", value=translated.text, inline=False)
    embed.add_field(name="Pronunciation:", value=translated.pronunciation, inline=True)
    embed.add_field(name="Source Language:",value=f"{LANGUAGES[translated.src]} ({translated.src})",inline=True)
    embed.add_field(name="Destination Language:",value=f"{LANGUAGES[translated.dest]} ({translated.dest})",inline=True)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['backwardsname','backname','bn'])
async def _backwardsname(ctx,*,user:discord.Member="None"):
    if user == "None":
        user = ctx.message.author
    name = user.display_name
    backwards_name = ''.join(reversed(name))
    embed = discord.Embed(
        title=backwards_name,
        colour=hc
    )
    embed.add_field(name="Original Name:",value=name)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command(aliases=['purge','prune'])
@commands.has_permissions(manage_messages=True)
async def _purge(ctx,number="None"):
    if number == "None":
        embed = discord.Embed(title="Please enter a number!",colour=discord.Colour.red())
        embed.set_image(url='https://i.imgur.com/XgqWMei.jpg')
        embed.set_footer(text=df)
    elif number != "None":
        try:
            num = int(number)
            con = True
        except ValueError as e:
            embed = discord.Embed(title="Please enter a number!", colour=discord.Colour.red())
            embed.set_image(url='https://i.imgur.com/XgqWMei.jpg')
            embed.add_field(name="Error:", value=str(e))
            embed.set_footer(text=df)
            con = False
        if con:
            await ctx.message.delete()
            await ctx.message.channel.purge(limit=num)
            embed = discord.Embed(title="Purge Success!", colour=discord.Colour.green())
            embed.add_field(name="Number of Messages",value=number)
            embed.add_field(name="Command Author",value=ctx.message.author.display_name)
            embed.set_footer(text=df)
    message = await ctx.message.channel.send(embed=embed)
    await message.delete(delay=7)

@client.command()
async def spam(ctx,num:int,*,message):
    if not ctx.message.author.id == 616032766974361640:
        msg = await ctx.message.channel.send("The spam command can only be used by the bot owner a.k.a. **NOT YOU**")
        await msg.delete(delay=30)
        return
    await ctx.message.delete()
    for x in range(0,num):
        await ctx.message.channel.send(message)
        await asyncio.sleep(0.9)

@client.command()
async def fastspam(ctx,num:int,*,message):
    if not ctx.message.author.id == 616032766974361640:
        msg = await ctx.message.channel.send("The spam command can only be used by the bot owner a.k.a. **NOT YOU**")
        await msg.delete(delay=30)
        return
    await ctx.message.delete()
    for x in range(0,num):
        await ctx.message.channel.send(message)

@client.command()
async def latency(ctx):
    current_ping = round(client.latency * 1000)
    embed = discord.Embed(
        title="Here is the current ping for the Elevator Server Bot",
        colour=hc
    )
    embed.set_footer(text=df)
    embed.add_field(name="Ping:",value=str(current_ping) + 'ms')

    await ctx.message.channel.send(embed=embed)

@client.command()
async def setcounting(ctx,num:int,user:discord.Member):
    if not ctx.message.author.id == 616032766974361640:
        await ctx.message.channel.send("This can only be used by the bot owner.")
        return
    current_count = (num,user.id)
    file = open("counting.json", "r+")
    file.seek(0)
    file.truncate()
    json.dump(current_count,file)
    file.close()
    await ctx.message.channel.send("Counting Position Updated!")

@client.command()
async def laugh(ctx):
    random_laugh_gif = ['https://i.imgur.com/hfBNc9K.jpg',
                        'https://i.imgur.com/wmpKu8K.jpg',
                        'https://i.imgur.com/Fc6Rpu7.gif'
                        ]
    lg = choice(random_laugh_gif)
    l_embed = discord.Embed(
        description=f'{ctx.message.author.mention} is laughing!',
        colour=hc
    )
    l_embed.set_footer(text=df)
    l_embed.set_image(url=lg)

    await ctx.message.channel.send(embed=l_embed)

@client.command()
async def stare(ctx,*,user:discord.Member='themselves?!?'):
    s_embed = discord.Embed(
        description=f'{ctx.message.author.mention} is staring at {user.mention}!',
        colour=hc
    )
    s_embed.set_footer(text=df)
    s_embed.set_image(url='https://i.ibb.co/XpNb1s9/stare.gif')

    await ctx.message.channel.send(embed=s_embed)

@client.command()
async def rankthot(ctx,*,user:discord.Member=None):
    if user is None:
        user = ctx.message.author
    if user.id == 616032766974361640:
        thot_level = 0
    elif user.id == 514835126220226580 or user.id == 429504383529517056:
        thot_level = 100
    else:
        thot_level = randint(0,100)
    title = "Thotties be thotting"
    message = f"{user.mention} is **{str(thot_level)}%**"
    if thot_level >= 75:
        embed = discord.Embed(
            title=title,
            description=message,
            colour=discord.Colour.red()
        )
    elif thot_level >= 50:
        embed = discord.Embed(
            title=title,
            description=message,
            colour=discord.Colour.gold()
        )
    else:
        embed = discord.Embed(
            title=title,
            description=message,
            colour=discord.Colour.green()
        )
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def deathbattle(ctx,user:discord.Member):
    p1tup = (ctx.message.author.display_name, 100)
    p2tup = (user.display_name, 100)
    turn = 1
    embed = discord.Embed(
        title="Deathbattle Time!!!",
        description=f"Deathbattle between {ctx.message.author.mention} and {user.mention}!",
        colour=discord.Colour.blue()
    )
    embed.set_footer(text=df)
    embed.add_field(name=p1tup[0],value=f"{str(p1tup[1])}/100")
    embed.add_field(name=p2tup[0], value=f"{str(p2tup[1])}/100")
    show_msg = await ctx.message.channel.send(embed=embed)
    # make sure in responses, the person who is hitting is first, victim is second, damage is third
    responses = [
        "__{}__ shocks __{}__ with lightning for __{}__ dmg!",
        "__{}__ explodes a bomb on __{}__ for __{}__ dmg!",
        "__{}__ explodes a nuclear bomb on __{}__ for __{}__ dmg!",
        "__{}__ runs over __{}__ with a car for __{}__ dmg!",
        "__{}__ runs over __{}__ with a truck for __{}__ dmg!",
        "__{}__ assigns a echelon to kill __{}__, you manage to get away but suffer __{}__ dmg!",
        "__{}__ shoots __{}__ with a AR for __{}__ dmg!",
        "__{}__ shoots __{}__ with a HG for __{}__ dmg!",
        "__{}__ shoots __{}__ with a MG for __{}__ dmg!",
        "__{}__ shoots __{}__ with a RF for __{}__ dmg!",
        "__{}__ shoots __{}__ with a SG for __{}__ dmg!",
        "__{}__ shoots __{}__ with a SMG for __{}__ dmg!",
        "__{}__ slices __{}__ with a sword for __{}__ dmg!",
        "__{}__ hits __{}__ with a whip for __{}__ dmg!",
        "__{}__ slaps __{}__ for __{}__ dmg!",
        "__{}__ punches __{}__ for __{}__ dmg!",
        "__{}__ smacks __{}__ with a chair for __{}__ dmg!",
        "__{}__ stabs __{}__ with knife for __{}__ dmg!",
        "__{}__ bonks __{}__ with a bat for __{}__ dmg!",
        "__{}__ tortures __{}__ for __{}__ dmg!",
        "__{}__ karate chops __{}__ for __{}__ dmg!",
        "__{}__ kicks __{}__ for __{}__ dmg!",
        "__{}__ burns __{}__ for __{}__ dmg!",
        "__{}__ smacks __{}__ with a hammer for __{}__ dmg!",
        "__{}__ fires a torpedo at __{}__ for __{}__ dmg!",
        "__{}__ fires a canonball at __{}__ and dealt __{}__ dmg!",
        "__{}__ smacks __{}__ on the head with a ban and dealt __{}__ dmg!",
        "__{}__ casts the stupefy charm on __{}__ and dealt __{}__ dmg!",
        "__{}__ casts the expelliarmus charm on __{}__ and dealt __{}__ dmg!"
    ]
    past_responses = []
    def check_win(p1life,p2life):
        if p1life <= 0:
            return 2
        if p2life <= 0:
            return 1
        return 0
    def cur_stat(p1tup,p2tup,turn,dmg):
        temp_msg = choice(responses)
        if turn == 1:
            past_responses.append("<:deathbattleright:700815518193680434> " + temp_msg.format(f"**{p1tup[0]}**",f"**{p2tup[0]}**",f"**{str(dmg)}**"))
            if len(past_responses) > 3:
                del past_responses[0]
            msg = '\n'.join(x for x in past_responses)
            embed = discord.Embed(
                description=msg,
                colour=discord.Colour.green()
            )
        else:
            past_responses.append("<:deathbattleleft:700815578499121183> " + temp_msg.format(f"**{p2tup[0]}**",f"**{p1tup[0]}**",f"**{str(dmg)}**"))
            if len(past_responses) > 3:
                del past_responses[0]
            msg = '\n'.join(x for x in past_responses)
            embed = discord.Embed(
                description=msg,
                colour=discord.Colour.red()
            )
        embed.set_footer(text=df)
        embed.add_field(name=f"{p1tup[0]}:",value=str(p1tup[1]))
        embed.add_field(name=f"{p2tup[0]}:",value=str(p2tup[1]))
        past_responses.append(past_responses.pop().replace("**",""))
        return (embed,dmg)
    await asyncio.sleep(1.8)

    while check_win(p1tup[1],p2tup[1]) == 0:
        dmg = randint(0, 35)
        if turn == 1:
            p2tup = (p2tup[0],p2tup[1]-dmg)
        else:
            p1tup = (p1tup[0], p1tup[1] - dmg)
        stat = cur_stat(p1tup, p2tup, turn,dmg)
        await show_msg.edit(embed=stat[0])
        if turn == 1:
            turn = 2
        else:
            turn = 1
        await asyncio.sleep(2.3)

    if check_win(p1tup[1],p2tup[1]) == 1:
        winner = p1tup[0]
    else:
        winner = p2tup[0]
    past_responses.append(f"🏆 {winner} has won!")
    if len(past_responses) > 3:
        del past_responses[0]
    msg = '\n'.join(x for x in past_responses)
    embed = discord.Embed(
        description=msg,
        colour=discord.Colour.gold()
    )
    embed.set_footer(text=df)
    embed.add_field(name=f"{p1tup[0]}:", value=str(p1tup[1]))
    embed.add_field(name=f"{p2tup[0]}:", value=str(p2tup[1]))
    await show_msg.edit(embed=embed)

@client.command()
async def userinfo(ctx,*,user:discord.Member):
    embed = discord.Embed(
        description=user.mention,
        colour=hc
    )
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name=user.name + '#' + user.discriminator,icon_url=user.avatar_url)
    embed.add_field(name="Username:",value=user.nick)
    embed.add_field(name="ID:",value=str(user.id))
    embed.add_field(name="Joined At:",value=user.joined_at.strftime("%Y-%m-%d %H:%M UTC"))
    embed.add_field(name="Created At:", value=user.created_at.strftime("%Y-%m-%d %H:%M UTC"))
    embed.add_field(name="Status:",value=user.status)
    embed.add_field(name="Display Colour:",value=f"RGB: {user.colour.to_rgb()}\nHEX: {str(user.colour)}")
    embed.add_field(name="Top Role:",value=user.top_role.name)
    embed.add_field(name="Bot:", value=user.bot)
    embed.add_field(name="System User:",value=user.system)
    roles = []
    for x in user.roles:
        roles.append(x.name)
    val = ', '.join(x for x in roles)
    embed.add_field(name="Roles:", value=val, inline=False)
    guildperms = user.guild_permissions
    key_perms = {"Administrator":guildperms.administrator,"Ban Members":guildperms.ban_members,
                 "Kick Members":guildperms.kick_members,"Manage Channels":guildperms.manage_channels,
                 "Manage Server":guildperms.manage_guild,"Manage Roles":guildperms.manage_roles,
                 "Manage Nicknames":guildperms.manage_nicknames,"Mute Members":guildperms.mute_members,
                 "Deafen Members":guildperms.deafen_members,"Move Members":guildperms.deafen_members}
    key_permissions = []
    for x,y in key_perms.items():
        if y:
            key_permissions.append(x)
    key_perm = ", ".join(x for x in key_permissions)
    embed.add_field(name="Key Permissions:",value=key_perm,inline=False)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def outsideuserinfo(ctx,id:int):
    user = await client.fetch_user(id)
    embed = discord.Embed(
        colour=hc
    )
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name=user.name + '#' + user.discriminator, icon_url=user.avatar_url)
    embed.add_field(name="ID:", value=str(user.id))
    embed.add_field(name="Created At:", value=user.created_at.strftime("%Y-%m-%d %H:%M UTC"))
    embed.add_field(name="Bot:", value=user.bot)
    embed.set_footer(text=df)

    await ctx.message.channel.send(embed=embed)

@client.command()
async def shiprate(ctx,user1:str,user2:str):
    try:
        user1 = ctx.message.author.guild.get_member(int(user1.replace("<@!", "").replace(">", ""))).display_name
    except:
        pass
    try:
        user2 = ctx.message.author.guild.get_member(int(user2.replace("<@!", "").replace(">", ""))).display_name
    except:
        pass
    rate = randint(0,100)
    bar_full = "<:shipratefull:701950795649777736>"
    bar_empty = "<:shiprateempty:701950795947704340>"
    cur_num = round(rate/10)
    empty_num = 10 - cur_num
    descrip_msg = f"💗 **MATCHMAKING** 💗\n🔻 *`{user1}`*\n🔺 *`{user2}`*"
    bar_msg = ""
    for x in range(0,cur_num):
        bar_msg += bar_full
    for x in range(0,empty_num):
        bar_msg += bar_empty
    if cur_num == 10:
        expression = "Perfect! 💯"
    elif cur_num > 8:
        expression = "Great! 😃"
    elif cur_num > 6:
        expression = "Not Bad! 🙂"
    elif cur_num > 4:
        expression = "Ok... 🙁"
    elif cur_num > 2:
        expression = "Horrible! 😢"
    else:
        expression = "Impossible... 😭"
    embed_msg = f"**{str(rate)}%** {bar_msg} {expression}"
    embed = discord.Embed(
        description=embed_msg,
        colour=0xff81d2
    )

    await ctx.message.channel.send(content=descrip_msg,embed=embed)

@client.command(aliases=['hellodarkness','hdmof'])
async def _hellodarknessmyoldfriend(ctx):
    await ctx.message.channel.send("https://www.youtube.com/watch?v=qYS0EeaAUMw&t=4")

@client.command(aliases=['animatedemoji','animemoji','ae'])
async def _animatedemoji(ctx,*,emoji_name):
    def similar(a,b):
        return SequenceMatcher(None,a,b).ratio()
    emoji_similaritys = {}
    for emoji in ctx.guild.emojis:
        if emoji.animated:
            emoji_similaritys[similar(emoji_name,emoji.name)] = emoji
    highest_emoji = max([*emoji_similaritys]),emoji_similaritys[max([*emoji_similaritys])]
    if highest_emoji[0] < 0.1:
        await ctx.message.channel.send("Could not find any emojis that match `{}`".format(emoji_name))
        return
    await ctx.message.channel.send("<a:{}:{}>".format(highest_emoji[1].name,str(highest_emoji[1].id)))

@client.command()
async def blackjack(ctx):
    def get_card(deck):
        first_len = len(deck.deck)
        card = deck.give_random_card()
        second_len = len(deck.deck)
        for x in range(0,first_len-second_len-1):
            deck.take_card(card)
        return card
    def get_emoji(value,suit):
        suit_values = {0:"S",1:"H",2:"D",3:"C"}
        suit_letter = suit_values[suit]
        for guild in client.guilds:
            for emoji in guild.emojis:
                if emoji.name == str(value) + suit_letter:
                    return "<:{}:{}>".format(emoji.name,str(emoji.id))
        return "Error: Emoji Not Found"
    def generate_deck(num_deck):
        deck_obj = deck_of_cards.DeckOfCards()
        for x in range(0,num_deck):
            deck_obj.add_deck()
        deck_obj.shuffle_deck()
        return deck_obj
    def get_value(hand):
        val = 0
        for card in hand:
            if card.value > 10:
                val += 10
                continue
            if card.value == 1:
                continue
            val += card.value
        for card in hand:
            if card.value == 1:
                if val + 11 <= 21:
                    val += 11
                    continue
                else:
                    val += 1
        return val
    def check_soft(hand):
        val = 0
        for card in hand:
            if card.value > 10:
                val += 10
                continue
            if card.value == 1:
                continue
            val += card.value
        status = []
        for card in hand:
            if card.value == 1:
                if val + 11 <= 21:
                    status.append(True)
                    val += 11
                else:
                    status.append(False)
                    val += 1
        for status in status:
            if status:
                return True
        return False
    def check(message):
        if (message.author == ctx.message.author and message.content.lower() == "hit") or (message.author == ctx.message.author and message.content.lower() == "stand"):
            return True
        return False
    def check_lose(hand):
        val = get_value(hand)
        if val > 21:
            return True
        return False
    def embed_gen(player,dealer,status):
        if status == "lost":
            colour = discord.Colour.red()
        elif status == "won":
            colour = discord.Colour.green()
        elif status == "tied":
            colour = discord.Colour.gold()
        else:
            status = "An Error Has Occured"
            colour = discord.Colour.dark_red()
        embed = discord.Embed(
            description="You {}!".format(status),
            colour=colour
        )
        embed.set_author(name=ctx.message.author.name + '#' + ctx.message.author.discriminator,
                         icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=df)
        player_emoji = " ".join(get_emoji(x.value, x.suit) for x in player)
        dealer_emoji = " ".join(get_emoji(x.value, x.suit) for x in dealer)
        player_value = str(get_value(player_hand))
        dealer_value = str(get_value(dealer_hand))
        if check_soft(player_hand):
            player_value = "Soft " + str(get_value(player_hand))
        if check_soft(dealer_hand):
            dealer_value = "Soft " + str(get_value(dealer_hand))
        if get_value(player_hand) == 21:
            player_value = "Blackjack"
        if get_value(dealer_hand) == 21:
            dealer_value = "Blackjack"
        embed.add_field(name="Your Hand:", value="{}\nValue: {}".format(player_emoji, player_value))
        embed.add_field(name="Dealer's Hand:", value="{}\nValue: {}".format(dealer_emoji, dealer_value))
        return embed
    player_hand = []
    dealer_hand = []
    deck = generate_deck(6)
    dealer_hand.append(get_card(deck))
    dealer_hand.append(get_card(deck))
    player_hand.append(get_card(deck))
    player_hand.append(get_card(deck))
    embed = discord.Embed(
        description="Type `hit` to draw another card or `stand` to pass. If you don't respond for 1 minute, you lose!",
        colour=discord.Colour.blue()
    )
    embed.set_author(name=ctx.message.author.name + '#' + ctx.message.author.discriminator, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text=df)
    player_emoji = " ".join(get_emoji(x.value,x.suit) for x in player_hand)
    dealer_emoji = get_emoji(dealer_hand[0].value,dealer_hand[0].suit) + " " + "<:blue_back:706507690054123561>"
    player_value = str(get_value(player_hand))
    dealer_value = str(dealer_hand[0].value)
    if dealer_hand[0].value > 10:
        dealer_value = "10"
    if check_soft(player_hand):
        player_value = "Soft " + str(get_value(player_hand))
    if check_soft(dealer_hand) and dealer_hand[0].value == 1:
        dealer_value = "Soft 11"
    embed.add_field(name="Your Hand:",value="{}\nValue: {}".format(player_emoji,player_value))
    embed.add_field(name="Dealer's Hand:",value="{}\nValue: {}".format(dealer_emoji,dealer_value))
    message = await ctx.message.channel.send(embed=embed)
    if check_lose(dealer_hand):
        await message.edit(embed=embed_gen(player_hand, dealer_hand,"won"))
        return
    if get_value(player_hand) == 21:
        await message.edit(embed=embed_gen(player_hand,dealer_hand,"won"))
        return
    if get_value(dealer_hand) == 21:
        await message.edit(embed=embed_gen(player_hand,dealer_hand,"lost"))
        return
    if check_lose(player_hand):
        await message.edit(embed=embed_gen(player_hand, dealer_hand,"lost"))
        return
    while True:
        try:
            choice = await client.wait_for("message",check=check,timeout=60)
        except asyncio.TimeoutError:
            await ctx.message.channel.send("You took more than 1 minute to answer, you lost!")
            return
        if choice.content.lower() == "stand":
            break
        player_hand.append(get_card(deck))
        if check_lose(player_hand):
            await message.edit(embed=embed_gen(player_hand,dealer_hand,"lost"))
            return
        if get_value(player_hand) == 21:
            await message.edit(embed=embed_gen(player_hand,dealer_hand,"won"))
            return
        if len(player_hand) >= 7:
            await message.edit(embed=embed_gen(player_hand,dealer_hand,"won"))
            return
        embed = discord.Embed(
            description="Type `hit` to draw another card or `stand` to pass. If you don't respond for 1 minute, you lose!",
            colour=discord.Colour.blue()
        )
        embed.set_author(name=ctx.message.author.name + '#' + ctx.message.author.discriminator,
                         icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=df)
        player_emoji = " ".join(get_emoji(x.value, x.suit) for x in player_hand)
        dealer_emoji = get_emoji(dealer_hand[0].value, dealer_hand[0].suit) + " " + "<:blue_back:706507690054123561>"
        player_value = str(get_value(player_hand))
        dealer_value = str(dealer_hand[0].value)
        if dealer_hand[0].value > 10:
            dealer_value = "10"
        if check_soft(player_hand):
            player_value = "Soft " + str(get_value(player_hand))
        if check_soft(dealer_hand) and dealer_hand[0].value == 1:
            dealer_value = "Soft 11"
        if get_value(player_hand) == 21:
            await message.edit(embed=embed_gen(player_hand, dealer_hand, "won"))
            return
        embed.add_field(name="Your Hand:", value="{}\nValue: {}".format(player_emoji, player_value))
        embed.add_field(name="Dealer's Hand:",value="{}\nValue: {}".format(dealer_emoji,dealer_value))
        await message.edit(embed=embed)
    while get_value(dealer_hand) < 17:
        dealer_hand.append(get_card(deck))
        if check_lose(dealer_hand):
            await message.edit(embed=embed_gen(player_hand,dealer_hand,"won"))
            return
        if get_value(dealer_hand) == 21:
            await message.edit(embed=embed_gen(player_hand,dealer_hand,"lost"))
            return
        if len(dealer_hand) >= 7:
            await message.edit(embed=embed_gen(player_hand, dealer_hand, "lost"))
            return
        embed = discord.Embed(
            description="Dealer is playing!",
            colour=discord.Colour.orange()
        )
        embed.set_author(name=ctx.message.author.name + '#' + ctx.message.author.discriminator,
                         icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=df)
        player_emoji = " ".join(get_emoji(x.value, x.suit) for x in player_hand)
        dealer_emoji = " ".join(get_emoji(x.value, x.suit) for x in dealer_hand)
        player_value = str(get_value(player_hand))
        dealer_value = str(get_value(dealer_hand))
        if check_soft(player_hand):
            player_value = "Soft " + str(get_value(player_hand))
        if check_soft(dealer_hand):
            dealer_value = "Soft " + str(get_value(dealer_hand))
        if get_value(player_hand) == 21:
            player_value = "Blackjack"
        if get_value(dealer_hand) == 21:
            dealer_value = "Blackjack"
        embed.add_field(name="Your Hand:", value="{}\nValue: {}".format(player_emoji, player_value))
        embed.add_field(name="Dealer's Hand:", value="{}\nValue: {}".format(dealer_emoji, dealer_value))
        await message.edit(embed=embed)
        await asyncio.sleep(1)
    if get_value(dealer_hand) == get_value(player_hand):
        await message.edit(embed=embed_gen(player_hand, dealer_hand, "tied"))
        return
    winning_value = min([get_value(player_hand),get_value(dealer_hand)],key=lambda list_value : abs(list_value - 21))
    if winning_value == get_value(player_hand):
        await message.edit(embed=embed_gen(player_hand, dealer_hand,"won"))
        return
    await message.edit(embed=embed_gen(player_hand, dealer_hand,"lost"))
    return

@client.command()
async def version(ctx):
    await ctx.message.channel.send("GFL RP Server Bot is currently at {}".format(
        df.replace(" Developed By: BLANK","").replace("Elevator Server Bot ","")))

@client.command()
async def impersonate(ctx,username,*,message):
    await ctx.message.delete()
    def similar(a,b):
        return SequenceMatcher(None,a,b).ratio()
    user_similarities = {}
    for user in ctx.guild.members:
        if username.replace("<@","").replace(">","").replace("!","").isdigit():
            user_similarities[similar(username.replace("<@","").replace(">","").replace("!",""), str(user.id))] = user
            continue
        con = True
        for letter in username:
            if letter.lower() not in user.display_name.lower():
                con = False
        if con:
            user_similarities[similar(username.lower(), user.display_name.lower())] = user
    if len(user_similarities) <= 0:
        await ctx.message.channel.send("Could not find any users that match `{}`".format(username))
        return
    highest_user = max([*user_similarities]), user_similarities[max([*user_similarities])]
    if highest_user[0] < 0.1:
        await ctx.message.channel.send("Could not find any users that match `{}`".format(username))
        return
    user = highest_user[1]
    webhook = None
    for hook in await ctx.message.channel.webhooks():
        if hook.user.id == 699677108607123548:
            webhook = hook
            break
    if webhook is None:
        webhook = await ctx.message.channel.create_webhook(name="Elevator Bot Webhook")
    await webhook.send(content=message,username=user.display_name,avatar_url=user.avatar_url)

@client.command()
async def usersend(ctx,*,details):
    detail_list = details.split("|")
    if len(detail_list) == 2:
        name = detail_list[0]
        message = detail_list[1]
        avatar = None
    elif len(detail_list) == 3:
        name = detail_list[0]
        message = detail_list[1]
        avatar = detail_list[2]
    else:
        await ctx.message.delete()
        await ctx.message.channel.send("You passed the incorrect number of parameters!")
        return
    if len(ctx.message.attachments) >= 1:
        avatar = ctx.message.attachments[0].url
    supported_image_extension = ["JPEG","JPG","GIF","WEBM","BMP","TIFF","PNG"]
    if not avatar is None:
        con = False
        for extension in supported_image_extension:
            if extension.lower() in avatar:
                con = True
                break
        if not con:
            await ctx.message.channel.send("The avatar link is not in the correct format. Supported formats are {}".format(
                ", ".join("." + x for x in supported_image_extension)
            ))
            await ctx.message.delete()
            return
    webhook = None
    for hook in await ctx.message.channel.webhooks():
        if hook.user.id == 699677108607123548:
            webhook = hook
            break
    if webhook is None:
        webhook = await ctx.message.channel.create_webhook(name="GFL RP Bot Webhook")
    await webhook.send(content=message, username=name, avatar_url=avatar)
    await ctx.message.delete()

@client.command(aliases=["jeopardymusic","jm"])
async def _jeopardymusic(ctx):
    await ctx.message.channel.send("https://www.youtube.com/watch?v=0Wi8Fv0AJA4")

@client.command()
async def disagree(ctx,user:discord.Member="None"):
    if user != "None":
        msg = f"{ctx.message.author.mention} disagrees with what {user.mention} said!"
    else:
        msg = f"{ctx.message.author.mention} disagrees with what was said!"
    a_embed = discord.Embed(
        description=msg,
        colour=hc
    )
    a_embed.set_footer(text=df)
    a_embed.set_image(url="https://i.imgur.com/ErwNJw3.jpg")

    await ctx.message.channel.send(embed=a_embed)

@client.command()
async def celebratemusic(ctx):
    await ctx.message.channel.send("https://www.youtube.com/watch?v=UWLIgjB9gGw")

@client.command()
async def sillyname(ctx,user:discord.Member=None):
    url = urllib.request.urlopen("https://raw.githubusercontent.com/bevacqua/correcthorse/master/wordlist.json")
    words = json.loads(url.read())
    orig_nick = ctx.message.author.display_name
    while True:
        name = choice(words).title() + " " + choice(words).title()
        if not len(name) > 32:
            break
    if user is not None:
        staff_role = get(ctx.guild.roles, id=725082640507469845)
        if staff_role in ctx.message.author.roles:
            try:
                await user.edit(nick=name)
            except discord.errors.Forbidden:
                await ctx.message.channel.send("My role isn't high enough to change your nickname!")
                return
            await ctx.message.channel.send(
                "`{}`'s nickname has been changed to `{}`! Their original name was `{}`".format(user.name,name, str(orig_nick)))
            return
        else:
            await ctx.message.channel.send("You do not have permissions to change someone else's nickname! Only Staff"
                                           " can do this.")
            return
    try:
        await ctx.message.author.edit(nick=name)
    except discord.errors.Forbidden:
        await ctx.message.channel.send("My role isn't high enough to change your nickname!")
        return
    await ctx.message.channel.send("You nickname has been changed to `{}`! If you would like to change it back, "
                                   "your original name was `{}`".format(name,str(orig_nick)))

@client.command()
async def redalert(ctx,*,reason=None):
    if reason is None:
        embed = discord.Embed(
            title="RED ALERT!!! RED ALERT!!! RED ALERT!!!",
            colour=discord.Colour.red()
        )
    else:
        embed = discord.Embed(
            title="RED ALERT!!! RED ALERT!!! RED ALERT!!!",
            description=reason,
            colour=discord.Colour.red()
        )
    embed.set_footer(text=df)
    embed.set_image(url="https://media1.tenor.com/images/5711e293284d2912a5bdec8b9997a2f0/tenor.gif?itemid=14378764")

    await ctx.message.channel.send(embed=embed)

@client.command()
async def mega(ctx):
    url = urllib.request.urlopen("https://raw.githubusercontent.com/bevacqua/correcthorse/master/wordlist.json")
    words = json.loads(url.read())
    await ctx.message.channel.send("MEGA{}".format(choice(words).upper()))

@client.command()
async def ping(ctx, username):
    for x in ctx.guild.members:
        if username.lower() in x.display_name.lower():
            user = x
            await ctx.message.channel.send(f'Ding! {user.mention}')
            break

client.run('Njk5Njc3MTA4NjA3MTIzNTQ4.XpX3HQ.hIfoh4Q6KzH52D25KYR-QGNMl8k')
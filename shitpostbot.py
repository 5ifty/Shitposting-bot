import discord
from discord.ext import commands
import random
import aiohttp
import traceback
from discord.ext.commands import errors
import requests
import secrets
from io import BytesIO
from PIL import Image
from random import getrandbits
from ipaddress import IPv4Network, IPv4Address
import asyncio
from utils import list, default
from gtts import gTTS
from datetime import datetime
import time

description = '''A fun bot to shitpost your server!'''

bot = commands.Bot(command_prefix='!!!', description=description)
bot.remove_command('help')
token = '' # copy paste your token here to run the bot<3


@bot.event
async def on_ready():
    print(f'Logging in as {bot.user.name}\n With the user ID {bot.user.id}')
    print(f'---Logged in---')
    game = "With bad memes| !!!help "  # to avoid syntax errors (Cos im dumb), made it a variable.
    await bot.change_presence(activity=discord.Game(type=3, name=game), status=discord.Status.dnd)






    #  this function does all of the API stuffs, dont delete it.
async def get_response(self, URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            return await response.json()


@bot.command()
async def herewego(ctx, image: str = None):
    """Make the here we go meme from a URL"""
    if image is None and len(ctx.message.attachments) == 1:
        image = ctx.message.attachments[0].url
    elif image is None and len(ctx.message.attachments) == 0:
        return await ctx.send("I need an image to perform this command - Either upload one or use a URL.*here we go again*")
    else:
        image = image.strip('<>') if image else None
    bio = BytesIO()
    back = Image.open((requests.get(f'{image}', stream=True).raw))
    back = back.convert("RGBA")
    front = Image.open(r"herewego.png")
    # background
    bg = Image.new("RGBA", front.size)
    # height
    h = front.height - back.height
    bg.paste(back, (0, h), back)
    bg.paste(front, (0, 0), front)
    bg.save(bio, "PNG")
    bio.seek(0)
    async with ctx.typing():
        file = discord.File(filename="Herewego.png", fp=bio)
        await ctx.send(file=file)


@bot.command()
async def supreme(ctx, *, text: str = None):
    """Who said supreme was just for hype-beasts"""
    if text == None:
        bio = BytesIO()
        image = Image.open(requests.get(f'https://api.alexflipnote.dev/supreme?text=You need to include text to do this commamand...', stream=True).raw)
        image.save(bio, "PNG")
        bio.seek(0)
        async with ctx.typing():
            file = discord.File(filename="Supreme.png", fp=bio)
            await ctx.send(file=file)
    else:
        bio = BytesIO()
        image = Image.open(requests.get(f'https://api.alexflipnote.dev/supreme?text={text}', stream=True).raw)
        image.save(bio, "PNG")
        bio.seek(0)
        async with ctx.typing():
            file = discord.File(filename="Supreme.png", fp=bio)
            await ctx.send(file=file)


@bot.command()
async def drake(ctx, top: str = None, bottom: str = None):
    if top == None:
        return await ctx.send("I need text to perform this command, damn it Kiki...")
    if bottom == None:
        return await ctx.send("I need another text argument for this command, damn it Kiki...")
    else:
        bio = BytesIO()
        image = Image.open(requests.get(f"https://api.alexflipnote.dev/drake?top={top}&bottom={bottom}", stream=True).raw)
        image.save(bio, "PNG")
        bio.seek(0)
        async with ctx.typing():
            file = discord.File(filename="Drake.png", fp=bio)
            await ctx.send(file=file)


@bot.command()
async def woosh(ctx, member: discord.Member = None):
    """r/wooooosh"""
    if member == None:

        bio = BytesIO()
        image = Image.open(requests.get(f'https://api.alexflipnote.dev/jokeoverhead?image={ctx.author.avatar_url}', stream=True).raw)
        image.save(bio, "PNG")
        bio.seek(0)
        async with ctx.typing():
            file = discord.File(filename="whoosh.png", fp=bio)
            return await ctx.send(file=file, content='It appears the command "Wooshed" over your head, try including another user...')

    else:
        bio = BytesIO()
        image = Image.open(requests.get(f'https://api.alexflipnote.dev/jokeoverhead?image={member.avatar_url}', stream=True).raw)
        image.save(bio, "PNG")
        bio.seek(0)
        async with ctx.typing():
            file = discord.File(filename="whoosh.png", fp=bio)
            await ctx.send(file=file)


@bot.command()
async def captcha(ctx, *, text: str = None):
    """Verify you're not a bot"""
    if text == None:
        bio = BytesIO()
        image = Image.open(requests.get(f'https://api.alexflipnote.dev/captcha?text=Verified your IQ is -2', stream=True).raw)
        image.save(bio, "PNG")
        bio.seek(0)
        async with ctx.typing():
            file = discord.File(filename="captcha.png", fp=bio)
            return await ctx.send(file=file, content="I need a text arguement for this command!")

    else:
        bio = BytesIO()
        image = Image.open(requests.get(f'https://api.alexflipnote.dev/captcha?text={text}', stream=True).raw)
        image.save(bio, "PNG")
        bio.seek(0)
        async with ctx.typing():
            file = discord.File(filename="captcha.png", fp=bio)
            await ctx.send(file=file)


@bot.command()
async def blazeit(ctx, *, user: discord.Member= None):
    """Pass Round the Joint"""
    embed = discord.Embed(colour=0x00ff00)
    embed.set_image(url="https://media.giphy.com/media/lbOLc1yrU21AQ/giphy.gif")
    if user is None:
        return await ctx.send(f"**{ctx.author.name}**, 420 blaze it!", embed=embed)
    if user is ctx.author:
        # Targeted themselves
        return await ctx.send(f"**{ctx.author.name}**,420 blaze it!", embed=embed)
    embed = discord.Embed(colour=0x00ff00)
    embed.set_image(url="https://media.giphy.com/media/8anH9hKSfoMwg/giphy.gif")
    await ctx.send(f"**{ctx.author.name}** has plugged **{user.name}**. Time to get Lit!!!", embed=embed)


@bot.command()
async def lifegen(ctx):
    """ generate a random life """
    age = random.choice(list.age)
    sex = random.choice(list.sex)
    school = random.choice(list.school)
    job = random.choice(list.job)
    money = random.choice(list.money)
    kids = random.choice(list.kids)
    death = random.choice(list.death)
    deathcause = random.choice(list.deathcause)
    gay = random.choice(list.gay)
    license = random.choice(list.license)
    country = random.choice(list.country)
    await ctx.send(f"***{ctx.author.name}'s Life story***\n{age} {sex} Born in {country}.\nYou have decided your sexuality; You are a {gay}.\n{school}.\n{license}\n{job}.\n{money}.\n{kids}.\n{death} because {deathcause}\n ```\nPlease pardon our dust on this command. We know some parts may not make sense<3```")


@bot.command()
async def say(ctx, *, text: commands.clean_content = None):
    """Make the bot repeat you"""
    if text == None:
        return await ctx.send(f"You want me to say nothing? That defeats the objective of this command...")
    await ctx.message.delete()
    await ctx.send(text)


@bot.command()
async def hack(ctx, user: discord.Member = None):
    subnet = IPv4Network("10.0.0.0/24")
    bits = getrandbits(subnet.max_prefixlen - subnet.prefixlen)
    addr = IPv4Address(subnet.network_address + bits)
    addr_str = str(addr)   # makes a fake IP for the bot to pretend hack
    # random list of fake email adresses.
    mail = ['@gmail.com', '@hotmail.com', '@outlook.com', '@yahoo.mail', '@mail.com', '@weebhentai.com', '@disco-rd.mail', '@email.com']

    nbytes: int = 8
    for i in range(20):   # random num generator for fake email numbers
        x = (random.randint(5, 9999))

    for i in range(20):   # random num generator for "port closing"
        z = (random.randint(6, 9999))

    if user is None:
        return await ctx.send(f"Please give me someone to hack!")

    if user is ctx.bot.user:
        return await ctx.send(f"I can't hack myself...")
    if user is ctx.author:
        return await ctx.send("Abort Mission. You can't hack yourself sir!")

    e = ("```css\n Collecting info...```")
    message = await ctx.send(e)
    await asyncio.sleep(2)
    e = ("```css\nInfo gathered...```")
    await message.edit(content=e)
    e = ("```css\nInfo gathered...\nFinding Target...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nLocating IP...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nSending Packets to IP adress. Please wait...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent...\nObtaining User Password for network account...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...\nSearching Network Account for Emails, Please wait...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...\nEmails acquired...[{user.name}{x}{random.choice(mail)}]```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...\nEmails acquired...[{user.name}{x}{random.choice(mail)}]\nLocating Sys32 on HDD... Please wait, this may take some time...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...\nEmails acquired...[{user.name}{x}{random.choice(mail)}]\nLocated Sys32 on User HDD... Preparing to delete files...```")
    await asyncio.sleep(3)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...\nEmails acquired...[{user.name}{x}{random.choice(mail)}]\nSys32 Deleted on Users System...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...\nEmails acquired...[{user.name}{x}{random.choice(mail)}]\nSys32 Deleted on Users System...\nClosing connection...```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...\nEmails acquired...[{user.name}{x}{random.choice(mail)}]\nSys32 Deleted on Users System...\nClosing connection...\nConnection Closed on Port [{z}]```")
    await asyncio.sleep(2)
    await message.edit(content=e)
    e = (f"```css\nInfo gathered...\nTarget Found...\nIP found and locked at [{addr_str}]...\nPackets sent.\nObtained User Network password...[{secrets.token_urlsafe(nbytes)}]...\nEmails acquired...[{user.name}{x}{random.choice(mail)}]\nSys32 Deleted on Users System...\nClosing connection...\nConnection Closed on Port [{z}]\nFinsished hacking {user}```")
    await asyncio.sleep(2)
    await message.edit(content=e)


@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question: commands.clean_content = None):
    """ Consult 8ball to receive an answer """
    if question == None:
        return await ctx.send("Please ask a message to the wise 8ball!")
    else:
        answer = random.choice(list.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")


@bot.command(aliases=["virgindetector"])
async def virgin(ctx, user: discord.User = None):
    """How much of a virgin is someone?"""
    num = random.randint(0, 100)
    deci = random.randint(0, 9)
    if num == 100:
        deci == 0

    if user is None:
        user = ctx.author
    await ctx.send(f"**{user.name}** is **{num}.{deci}%** Virgin")


@bot.command(aliases=['howbig'])
async def peepeesize(ctx, *, user: discord.Member = None):
    """ How big is your Peepee? """
    num = random.randint(3, 9)
    deci = random.randint(0, 9)

    if num == 9:
        deci = 0

    if user is None:
        user = ctx.author
    await ctx.send(f"**{user.name}** Has a **{num}.{deci}** inch PeePee")


@bot.command(aliases=['f'])
async def F(ctx, *, user: discord.Member = None):
    """Pay respects for our fallen soliders"""
    emoji = "❤ 🖤 💚 💜 💙 💛 💖"
    a = random.choice(emoji)
    if user is None:
        return await ctx.send(f"**{ctx.author.name}** Has put an F in chat {a}")
    if user is ctx.author:
        # Targeted themselves
        return await ctx.send(f"**{ctx.author.name}** Has oofed, can we get 50 likes?{a}")
    await ctx.send(f"**{ctx.author.name}** has paid respect to **{user.name}**. Our fallen Soldier {a}")


@bot.command(aliases=['tts', 'voice'])
async def gtts(ctx, *, message: str = None):
    if message == None:
        await ctx.send("Please include a message for me to say!")
    tts = gTTS(text=message.lower(), lang='en')
    tts.save('tts.mp3')
    await ctx.send(file=discord.File('tts.mp3'))


@bot.command()
async def reverse(ctx, *, text: str = None):
    if text == None:
        return await ctx.send("Please give me text to reverse!")
    else:
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")


@bot.command()
async def ship(ctx, member: discord.Member = None, othermember: discord.Member = None):
    if member == None:
        return await ctx.send("Please Include 2 members to ship!")
    if othermember == None:
        return await ctx.send("Please include a 2nd memeber to ship!")
    if member == othermember:
        return await ctx.send("You cant ship the same person with themself!")
    else:
        num = random.randint(0, 100)
        deci = random.randint(0, 9)
        if num == 100:
            deci == 0

        emoji = "💔"
        if num > 25:
            emoji = "💜"
        if num > 50:
            emoji = "💖"
        if num > 75:
            emoji = "💞"

        bio = BytesIO()
        image = Image.open(requests.get(f'https://api.alexflipnote.dev/ship?user={member.avatar_url}&user2={othermember.avatar_url}', stream=True).raw)
        image.save(bio, "PNG")
        bio.seek(0)
        async with ctx.typing():
            file = discord.File(filename="shipped.png", fp=bio)
            await ctx.send(file=file)
            await ctx.send(f"I ship **{member}** + **{othermember}** as a **{num}.{deci}** % rating!{emoji}")


@bot.command(aliases=['fish'])
async def fishing(ctx):
    """Try and catch a fish!"""
    fish = random.choice(list.fish)
    await ctx.send(f"{ctx.author.name}, {fish}")



# for the about section -

@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    e = discord.Embed(colour=0xf44242, title="Ping!", description="Checking Server Ping!")
    message = await ctx.send(embed=e)
    end = time.perf_counter()
    duration = (end - start) * 1000
    await asyncio.sleep(1)
    e = discord.Embed(colour=0x0ad80a, title="Pong!", description='Latency {:.2f}ms'.format(duration))
    await message.edit(embed=e)

@bot.command()
async def about(ctx):
    python = "<:python:569621527251910668>"
    embed = discord.Embed(title="Some info and stats of the bot", timestamp=datetime.utcnow())
    embed.add_field(name="Developer 🔧", value="5ifty#0777", inline=False)
    embed.add_field(name=f"Library {python}:", value="discord.py", inline=False)
    embed.add_field(name="Servers🔗:", value=f"{len(ctx.bot.guilds)}", inline=False)
    embed.add_field(name="Prefix", value=f"My prefix is !!!", inline=False)
    embed.set_footer(text=f'Info about {bot.user.name}', icon_url=ctx.bot.user.avatar_url)
    await ctx.send(embed=embed)




# the help command, lol.
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help/Info - To give this bot full functionality give it embed and message management permissions! Bot Prefix is !!!", color=ctx.me.top_role.colour, timestamp=datetime.utcnow())
    embed.add_field(name="Image ShitPosts", value=f"`captcha - Verify you're not a bot!\ndrake - She say do you love me(Use quote marks to point out what the top and bottom is)\nherewego - Makes the meme with your own image\nsupreme - Supremeify your text (Hypebeast warning)\nwoosh - For when someone doesn't get the joke`", inline=False)
    embed.add_field(name="Voice/Text Commands", value=f"`reverse - Reverses your text, gnizama!\nsay - Make the Bot repeat what you say *Echoooo Echooo* (Manage message permissons needed)\ntts - Get a text to speech response!`", inline=False)
    embed.add_field(name="Games", value=f"`8ball - Get a response from the 8ball.\nfishing - Go fishing, maybe you'll catch one!\nlifegen - Makes up a random life for you, living my best life!`", inline=False)
    embed.add_field(name="User Inclusive", value=f"`blazeit - Spark up the joint with your friend!\nf - Can we get an F in the chat?\nhack - Fake hack someone *intensive typing*\nhowbig - Who said size doesn't matter?\nship - See how well 2 users ship toghether, it must be love<3\nvirgin - See how much of a virgin someone is!`", inline=False)
    embed.add_field(name="Other", value=f"`about - Shows stats of the bot.\nhelp - Shows this message.\nping - Pong!`", inline=False)
    embed.set_footer(text="Shitpost bot help for Discord Hack Week", icon_url=ctx.bot.user.avatar_url)
    await ctx.send(embed=embed)





# This not nice part of code handles errors/ commands being used (for owner/Admin purposes only<3



async def on_command_error(self, ctx, err):
    if isinstance(err, errors.CommandInvokeError):
        err = err.original
        _traceback = traceback.format_tb(err.__traceback__)
        _traceback = ''.join(_traceback)
        error = ('```py\n{2}{0}: {3}\n```').format(type(err).__name__, ctx.message.content, _traceback, err)
        await ctx.send(f"Error, please check console for more details.")
        print(error)





bot.run(token)
